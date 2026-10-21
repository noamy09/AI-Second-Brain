---
up: "[[Home.md|Home]]"
related:
  - "[[AI-OS/Maps/skill-map.md|skill-map]]"
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
created: 2026-10-16
collections:
  - ai-os
tags:
  - read-only
  - system-core
---
# 🤖 Vault Navigation Map

This is your manual to navigate and work in the Second Brain.

## Core System Files
- [[Home.md|Home]] — Single mandatory entry point: briefing on who I am, universal guardrails, and boot sequence (natively auto-included via `@[Home.md](...)` in `GEMINI.md` and `@...Home.md` in `CLAUDE.md`).
- [[AI-OS/Maps/vault-map.md|vault-map]] — Directory architecture and folder-specific retrieval router.
- [[AI-OS/Maps/skill-map.md|skill-map]] — Registry of all specialized skills in `AI-OS/Skills/<skill-name>/SKILL.md` you can load on demand.
- [[AI-OS/Maps/memory-map.md|memory-map]] — 1-line-per-note registry of all notes in `Memories/` so agents can identify relevant domain knowledge before planning or coding.
- [[AI-OS/History/sync-state.md|sync-state]] — Per-harness delta watermark tracker (`last_sweep_timestamp_agy`, `last_sweep_timestamp_claude`, and `last_janitor_timestamp`) for maintenance agents.

## Directory Structure
- `AI-OS/Maps/` — System routing maps (`vault-map.md`, `skill-map.md`, `memory-map.md`).
- `AI-OS/Skills/` — On-demand procedural workflows (`AI-OS/Skills/<skill-name>/SKILL.md`) and setup scripts (`AI-OS/Skills/scripts/`).
- `AI-OS/History/` — Timestamped activity logs (`sweep-log.md`, `janitor-log.md`), session transcripts, `sync-state.md`, and `Logs.base` (Obsidian UI view).
- `Efforts/` — Active and archived project hubs (`Efforts/<Project-Name>/context.md`, `decisions.md`, `changelog.md`) and `Projects.base` (Obsidian UI view).
- `Memories/` — Distilled concepts, architecture notes, reusable knowledge checkpoints, and `Knowledge.base` (Obsidian UI view).
- `X/Templates/` — Mandatory Markdown templates for note and skill creation.
- *(Note: `.base` files are Obsidian UI database views for human navigation; AI agents should ignore `.base` files and query `.md` files directly).*

## Folder-Specific Retrieval Guide
To minimize context window usage, select the retrieval method matching the target folder:
- **`Memories/`:** Check [[AI-OS/Maps/memory-map.md|memory-map]] first $\rightarrow$ if searching unindexed content, run `list_dir` / `find_by_name` / `Glob` $\rightarrow$ `grep_search` / `Grep` / `rg -n` on YAML (`collections:`, `related:`, `sources:`, `tags:`) or headings (`^#` / `^##`) $\rightarrow$ `view_file` (`StartLine`/`EndLine`) or `Read` for partial reads.
- **`Efforts/<Project-Name>/`:** Read `context.md` and `decisions.md` first for current architecture, active roadmap, ADRs, and linked memories; grep `changelog.md` when investigating session history.
- **`AI-OS/History/`:** Filter by ISO date filename (`YYYY-MM-DD`) or grep on `agent:` / `time_window:`—never read historical logs sequentially.
- **Optional Human / Terminal CLI:** When the Obsidian desktop application is open, `obsidian search query="..."` or `obsidian daily` can also be used from the terminal.