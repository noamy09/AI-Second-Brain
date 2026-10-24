#!/usr/bin/env python3
"""
Self-Service Onboarding Script for Google Antigravity (AGY).
Configures:
1. ~/.gemini/config/skills.json -> Registers ~/Second Brain/AI-OS/Skills (excluding scripts/) for dynamic 1-hop skill discovery.
2. ~/.gemini/config/GEMINI.md   -> Preserves Global Planning Rule and enforces the Strict Home.md Step-0 Funnel (zero duplicated vault rules).
3. <Vault-Root>/GEMINI.md       -> Uses Antigravity's native @[Home.md](Home.md) file-include directive (0-call auto-expansion, atomic-save safe, zero bypass routes).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[3]
VAULT_POSIX = VAULT_ROOT.as_posix()

# Always use absolute POSIX path to avoid tilde expansion issues with spaces on Windows
SKILLS_DIR_ENTRY = f"{VAULT_POSIX}/AI-OS/Skills"

GEMINI_CONFIG_DIR = Path.home() / ".gemini" / "config"
SKILLS_JSON_PATH = GEMINI_CONFIG_DIR / "skills.json"
GLOBAL_GEMINI_MD = GEMINI_CONFIG_DIR / "GEMINI.md"
VAULT_GEMINI_POINTER = VAULT_ROOT / "GEMINI.md"
SWEEPER_SKILL_MD = VAULT_ROOT / "AI-OS" / "Skills" / "transcript-sweeper" / "SKILL.md"

GLOBAL_GEMINI_CONTENT = f"@[Home.md]({VAULT_POSIX}/Home.md)\n"

WORKSPACE_GEMINI_CONTENT = "@[Home.md](Home.md)\n"


def resolve_python_posix() -> str:
    local_py_bin = Path.home() / "AppData" / "Local" / "Python" / "bin" / "python.exe"
    if local_py_bin.exists():
        return local_py_bin.as_posix()
    return Path(sys.executable).resolve().as_posix()


def setup_skills_json() -> None:
    GEMINI_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    data: dict = {"entries": []}
    if SKILLS_JSON_PATH.exists():
        try:
            data = json.loads(SKILLS_JSON_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {"entries": []}

    raw_entries = data.get("entries", [])
    cleaned_entries: list[dict] = []
    for entry in raw_entries:
        if isinstance(entry, dict):
            entry_path = str(entry.get("path", "")).lower().replace("\\", "/")
            if not entry_path.endswith("ai-os/skills"):
                cleaned_entries.append(entry)

    cleaned_entries.append(
        {
            "path": SKILLS_DIR_ENTRY,
            "exclude": ["scripts"],
        }
    )
    data["entries"] = cleaned_entries

    SKILLS_JSON_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] Registered dynamic skills directory in: {SKILLS_JSON_PATH} ({SKILLS_DIR_ENTRY})")


def setup_global_gemini_md() -> None:
    GEMINI_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    GLOBAL_GEMINI_MD.write_text(GLOBAL_GEMINI_CONTENT, encoding="utf-8")
    print(f"[OK] Updated global Antigravity rules in: {GLOBAL_GEMINI_MD}")


def setup_vault_root_include() -> None:
    if VAULT_GEMINI_POINTER.exists() or VAULT_GEMINI_POINTER.is_symlink():
        VAULT_GEMINI_POINTER.unlink()
    VAULT_GEMINI_POINTER.write_text(WORKSPACE_GEMINI_CONTENT, encoding="utf-8")
    print(f"[OK] Wrote native @[Home.md](Home.md) root include: {VAULT_GEMINI_POINTER}")


def sync_sweeper_python_path() -> None:
    py_posix = resolve_python_posix()
    cmd_str = f"{py_posix} -X utf8 AI-OS/Skills/transcript-sweeper/scripts/sanitize_transcripts.py"

    if SWEEPER_SKILL_MD.exists():
        skill_text = SWEEPER_SKILL_MD.read_text(encoding="utf-8")
        updated_skill = re.sub(
            r"```powershell\r?\n\s*[^\r\n]*sanitize_transcripts\.py[^\r\n]*\r?\n\s*```",
            f"```powershell\n  {cmd_str}\n  ```",
            skill_text,
        )
        if updated_skill != skill_text:
            SWEEPER_SKILL_MD.write_text(updated_skill, encoding="utf-8")
            print(f"[OK] Synced local Python path in: {SWEEPER_SKILL_MD}")


def main() -> None:
    print(f"Setting up Second Brain harness for Google Antigravity (Vault: {VAULT_ROOT})...")
    setup_skills_json()
    setup_global_gemini_md()
    setup_vault_root_include()
    sync_sweeper_python_path()
    print("\nAntigravity setup complete!")


if __name__ == "__main__":
    main()
