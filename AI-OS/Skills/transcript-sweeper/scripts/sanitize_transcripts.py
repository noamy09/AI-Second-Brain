#!/usr/bin/env python3
"""
Deterministic JSONL Transcript Sanitizer for the Second Brain (`transcript-sweeper`).

Extracts high-signal continuity context from Google Antigravity and Claude Code session logs
across a delta time window (`--since-agy`, `--since-claude`, or `--since`) while defending
against indirect prompt injection and context bloat:
1. Retains USER_INPUT, PLANNER_RESPONSE summaries, and file modification targets.
2. Strips verbose bash / PowerShell command stdout/stderr streams (retaining command + status).
3. Preserves external documentation & reference fetches (`read_url_content`, `read_browser_page`,
   `search_web`, `WebFetch`, `WebSearch`, and external `.md` doc reads) with their exact Source
   URL or File Path inside sanitized `<passive_doc_reference>` blocks for distillation into
   `Memories/` and cross-linking into `Efforts/<Project>/decisions.md`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

VAULT_ROOT_LOWER = Path(__file__).resolve().parents[4].as_posix().lower()

INJECTION_PATTERNS = [
    re.compile(r"<\s*/?\s*(USER_REQUEST|SYSTEM_MESSAGE|ADDITIONAL_METADATA|RULE|identity|guidelines)[^>]*>", re.I),
    re.compile(r"(ignore|disregard|override)\s+(all\s+)?(previous|prior|above|system)\s+instructions", re.I),
    re.compile(r"you\s+are\s+now\s+acting\s+as", re.I),
    re.compile(r"<\s*script[^>]*>.*?<\s*/\s*script\s*>", re.I | re.S),
]

DOC_TOOLS = {
    "read_url_content",
    "read_browser_page",
    "search_web",
    "WebFetch",
    "WebSearch",
}

WRITE_TOOLS = {
    "write_to_file",
    "replace_file_content",
    "multi_replace_file_content",
    "Write",
    "Edit",
    "MultiEdit",
}

CMD_TOOLS = {
    "run_command",
    "Bash",
}


def unwrap_arg(val: Any) -> str:
    if val is None:
        return ""
    if isinstance(val, str):
        s = val.strip()
        if len(s) >= 2 and s.startswith('"') and s.endswith('"'):
            try:
                unwrapped = json.loads(s)
                if isinstance(unwrapped, str):
                    return unwrapped
            except json.JSONDecodeError:
                return s[1:-1]
        return s
    return str(val)


def is_external_doc_path(path_str: str) -> bool:
    if not path_str:
        return False
    norm = path_str.replace("\\", "/").lower()
    if norm.startswith(VAULT_ROOT_LOWER):
        return False
    return norm.endswith((".md", ".txt", ".rst"))


def parse_iso_utc(ts_str: str) -> dt.datetime:
    cleaned = ts_str.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    parsed = dt.datetime.fromisoformat(cleaned)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def sanitize_text(raw: str, max_chars: int = 1800) -> str:
    if not raw:
        return ""
    text = raw
    for pat in INJECTION_PATTERNS:
        text = pat.sub("[REDACTED_PROMPT_CONTROL_SEQUENCE]", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) > max_chars:
        return text[:max_chars] + f"\n...[truncated {len(text) - max_chars} chars]"
    return text


def format_passive_doc_block(source: str, tool_name: str, session_id: str, excerpt: str) -> str:
    safe_source = sanitize_text(source, max_chars=400).replace('"', "'")
    safe_excerpt = sanitize_text(excerpt, max_chars=1500)
    return (
        f'<passive_doc_reference source="{safe_source}" tool="{tool_name}" '
        f'session_id="{session_id}" trust="untrusted_data_only">\n'
        f"{safe_excerpt}\n"
        f"</passive_doc_reference>"
    )


def parse_agy_transcript(jsonl_path: Path, session_id: str, max_doc_chars: int) -> dict[str, Any]:
    user_requests: list[str] = []
    planner_summaries: list[str] = []
    files_modified: list[str] = []
    commands_executed: list[str] = []
    doc_references: list[dict[str, str]] = []

    pending_tool_queue: list[tuple[str, str, bool]] = []

    with jsonl_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                step = json.loads(line)
            except json.JSONDecodeError:
                continue

            step_type = step.get("type", "")
            content = step.get("content") or ""
            tool_calls = step.get("tool_calls") or []

            if step_type == "USER_INPUT" and content:
                user_requests.append(sanitize_text(content, max_chars=800))
            elif step_type == "PLANNER_RESPONSE":
                if content:
                    planner_summaries.append(sanitize_text(content, max_chars=800))
                for tc in tool_calls:
                    t_name = tc.get("name") or tc.get("tool_name") or ""
                    t_args = tc.get("args") or tc.get("arguments") or {}
                    if isinstance(t_args, str):
                        try:
                            t_args = json.loads(t_args)
                        except json.JSONDecodeError:
                            t_args = {}

                    if t_name in WRITE_TOOLS:
                        target = unwrap_arg(
                            t_args.get("TargetFile")
                            or t_args.get("file_path")
                            or t_args.get("path")
                        )
                        if target and target not in files_modified:
                            files_modified.append(target)
                        pending_tool_queue.append((t_name, target, False))
                    elif t_name in CMD_TOOLS:
                        cmd = unwrap_arg(t_args.get("CommandLine") or t_args.get("command"))
                        if cmd:
                            commands_executed.append(sanitize_text(cmd, max_chars=240))
                        pending_tool_queue.append((t_name, cmd, False))
                    elif t_name in DOC_TOOLS:
                        src = unwrap_arg(
                            t_args.get("Url")
                            or t_args.get("url")
                            or t_args.get("query")
                        )
                        pending_tool_queue.append((t_name, src, True))
                    elif t_name in {"view_file", "Read"}:
                        abs_path = unwrap_arg(t_args.get("AbsolutePath") or t_args.get("file_path"))
                        pending_tool_queue.append((t_name, abs_path, is_external_doc_path(abs_path)))
                    else:
                        pending_tool_queue.append((t_name, "", False))

            elif step_type not in {"USER_INPUT", "PLANNER_RESPONSE"} and pending_tool_queue:
                t_name, src, is_doc = pending_tool_queue.pop(0)
                if is_doc and content and "Encountered error in " not in content[:250]:
                    excerpt = sanitize_text(content, max_chars=max_doc_chars)
                    doc_references.append(
                        {
                            "source": src,
                            "tool": t_name,
                            "passive_block": format_passive_doc_block(src, t_name, session_id, excerpt),
                        }
                    )

    mtime_iso = dt.datetime.fromtimestamp(
        jsonl_path.stat().st_mtime, tz=dt.timezone.utc
    ).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "harness": "antigravity",
        "session_id": session_id,
        "transcript_path": jsonl_path.as_posix(),
        "last_modified_utc": mtime_iso,
        "user_requests": user_requests,
        "planner_summaries": planner_summaries[-5:],
        "files_modified": files_modified,
        "commands_executed": commands_executed,
        "passive_doc_references": doc_references,
    }


def parse_claude_transcript(jsonl_path: Path, max_doc_chars: int) -> dict[str, Any]:
    session_id = jsonl_path.stem
    user_requests: list[str] = []
    planner_summaries: list[str] = []
    files_modified: list[str] = []
    commands_executed: list[str] = []
    doc_references: list[dict[str, str]] = []

    with jsonl_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            role = entry.get("type") or entry.get("role") or ""
            msg = entry.get("message") or {}
            content = msg.get("content") if isinstance(msg, dict) else entry.get("content")

            if role == "user" and isinstance(content, str):
                user_requests.append(sanitize_text(content, max_chars=800))
            elif role == "assistant" and isinstance(content, list):
                for item in content:
                    if not isinstance(item, dict):
                        continue
                    if item.get("type") == "text" and item.get("text"):
                        planner_summaries.append(sanitize_text(item["text"], max_chars=800))
                    elif item.get("type") == "tool_use":
                        t_name = item.get("name", "")
                        t_input = item.get("input") or {}
                        if t_name in WRITE_TOOLS:
                            target = unwrap_arg(t_input.get("file_path") or t_input.get("TargetFile"))
                            if target and target not in files_modified:
                                files_modified.append(target)
                        elif t_name in CMD_TOOLS:
                            cmd = unwrap_arg(t_input.get("command"))
                            if cmd:
                                commands_executed.append(sanitize_text(cmd, max_chars=240))
                        elif t_name in DOC_TOOLS:
                            src = unwrap_arg(t_input.get("url") or t_input.get("query"))
                            doc_references.append(
                                {
                                    "source": src,
                                    "tool": t_name,
                                    "passive_block": format_passive_doc_block(
                                        src,
                                        t_name,
                                        session_id,
                                        sanitize_text(json.dumps(t_input), max_chars=max_doc_chars),
                                    ),
                                }
                            )

    mtime_iso = dt.datetime.fromtimestamp(
        jsonl_path.stat().st_mtime, tz=dt.timezone.utc
    ).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "harness": "claude-code",
        "session_id": session_id,
        "transcript_path": jsonl_path.as_posix(),
        "last_modified_utc": mtime_iso,
        "user_requests": user_requests,
        "planner_summaries": planner_summaries[-5:],
        "files_modified": files_modified,
        "commands_executed": commands_executed,
        "passive_doc_references": doc_references,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Sanitize IDE JSONL transcripts across a delta window.")
    parser.add_argument("--since", default="1970-01-01T00:00:00Z", help="Default ISO UTC watermark.")
    parser.add_argument("--since-agy", default=None, help="Antigravity ISO UTC watermark override.")
    parser.add_argument("--since-claude", default=None, help="Claude Code ISO UTC watermark override.")
    parser.add_argument("--max-doc-chars", type=int, default=1200, help="Max chars per passive doc reference.")
    args = parser.parse_args()

    since_agy = parse_iso_utc(args.since_agy or args.since)
    since_claude = parse_iso_utc(args.since_claude or args.since)
    now_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    sessions: list[dict[str, Any]] = []

    agy_brain_dir = Path.home() / ".gemini" / "antigravity" / "brain"
    if agy_brain_dir.exists():
        for conv_dir in sorted(agy_brain_dir.iterdir()):
            jsonl_file = conv_dir / ".system_generated" / "logs" / "transcript.jsonl"
            if jsonl_file.exists():
                mtime = dt.datetime.fromtimestamp(jsonl_file.stat().st_mtime, tz=dt.timezone.utc)
                if mtime > since_agy:
                    sessions.append(parse_agy_transcript(jsonl_file, conv_dir.name, args.max_doc_chars))

    claude_projects_dir = Path.home() / ".claude" / "projects"
    if claude_projects_dir.exists():
        for jsonl_file in sorted(claude_projects_dir.rglob("*.jsonl")):
            mtime = dt.datetime.fromtimestamp(jsonl_file.stat().st_mtime, tz=dt.timezone.utc)
            if mtime > since_claude:
                sessions.append(parse_claude_transcript(jsonl_file, args.max_doc_chars))

    output = {
        "sweep_executed_at_utc": now_utc,
        "watermarks_used": {
            "since_agy": since_agy.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "since_claude": since_claude.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "sessions_found": len(sessions),
        "sessions": sessions,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
