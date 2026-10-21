---
name: vault-janitor
description: "Use when running a scheduled or on-the-fly Delta Vault Hygiene audit to check for broken links, non-compliant Wikilinks, missing YAML keys, unindexed Memories/ notes, skill anatomy/registry compliance, empty files, and stale projects. Do NOT use for sweeping IDE conversation transcripts (use transcript-sweeper) or authoring individual notes/skills (use note-architect)."
aliases:
  - vault-janitor
up: "[[AI-OS/Maps/skill-map.md|skill-map]]"
related:
  - "[[AI-OS/Maps/vault-map.md|vault-map]]"
  - "[[AI-OS/Maps/skill-map.md|skill-map]]"
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
  - "[[AI-OS/History/sync-state.md|sync-state]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
  - "[[X/Templates/log-template.md|log-template]]"
  - "[[X/Templates/skill-template.md|skill-template]]"
created: 2026-10-16
collections:
  - ai-os
  - agents
  - skills
tags:
  - read-only
  - skill
---
# 🤖 Skill: Delta Vault Janitor & Hygiene Agent (`vault-janitor`)

## Objective & Trigger Boundaries
Audit the Second Brain across the delta window (`last_janitor_timestamp -> now`) and verify vault-wide structural integrity (broken links, non-compliant Wikilinks, unindexed `Memories/` notes, skill anatomy & registry compliance, missing YAML keys, semantic tags, empty files/directories, and stale projects), whether triggered on a schedule or manually on the fly by the user.
- **Use when:** Triggered for a scheduled or on-the-fly vault hygiene, link integrity, YAML frontmatter, or skill/memory registry audit.
- **Do NOT use when:** Extracting insights from IDE conversation logs (use [[AI-OS/Skills/transcript-sweeper/SKILL.md|transcript-sweeper]]) or creating a new note, memory, or skill from scratch (use [[AI-OS/Skills/note-architect/SKILL.md|note-architect]]).

## Execution Protocol
Read [[AI-OS/History/sync-state.md|sync-state]] to get `last_janitor_timestamp` (defining the delta window `last_janitor_timestamp -> now`) and read [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] as the single source of truth for required YAML frontmatter keys, permission tags, semantic tags (`memory`, `skill`, `log`, `project`, `decisions`, `changelog`), watermarking, skill anatomy, and link syntax. Use native search tools (`find_by_name`/`grep_search`/`Glob`/`Grep`) or cross-platform Python one-liners rather than reading every Markdown file into the LLM context window:

1. **Empty Files & Folders:**
   - Detect `0-byte` files and unexpected empty directories across the vault (ignoring `.obsidian/`, `.git/`, and empty root `Efforts/` or `Memories/` directories when no projects or memories exist yet).
2. **Link Format & Broken Target Audit:**
   - Scan `.md` files (prioritizing files added or modified since `last_janitor_timestamp` while verifying vault-wide link integrity) for Wikilinks (`[[...]]`), ignoring example links inside fenced code blocks (triple backticks), inline code spans (`code`), and `{{...}}` placeholders inside `X/Templates/`.
   - Flag any link that does NOT follow the Path-Complete Alias syntax defined in [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] (`[[path/to/file.md|alias]]`, unescaping `\|` inside Markdown tables).
   - Verify that the file path before the `|` exists on disk.
3. **YAML, Semantic Tag, Permission, Memory Index & Skill Compliance Audit:**
   - Verify every `.md` file starts with a valid YAML frontmatter block containing all mandatory keys, a permission tag (`read-only` or `write`), and the matching semantic type tag defined in [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] (exempting single-line IDE include files `GEMINI.md` and `CLAUDE.md` at the vault root).
   - Verify that every `.md` file in `Memories/` (including manual notes written in Obsidian) has a registered 1-line row in [[AI-OS/Maps/memory-map.md|memory-map]], and propose adding any unindexed memory notes in the cleanup plan.
   - **Skill Anatomy & Registry Check:** Verify that every `AI-OS/Skills/<skill-name>/SKILL.md` is registered in [[AI-OS/Maps/skill-map.md|skill-map]], includes both `"Use when..."` and `"Do NOT use when..."` in its YAML `description`, and contains all 6 mandatory sections from [[X/Templates/skill-template.md|skill-template]].
4. **Stale Project Check:**
   - Flag any `Efforts/<Project>/context.md` with `status: active` where `changelog.md` has not been modified in $>6$ months.
1. **Generate Cleanup Plan in the IDE (Do Not Modify Vault Yet):**
   - Present the audit findings (including Acting Agent `vault-janitor` and Time Window `<last_janitor_timestamp> -> <now>`) and exact remediation steps as an `implementation_plan.md` directly **in the IDE** and await user approval. Do **not** advance `last_janitor_timestamp` before approval.

## Subagent & Parallel Delegation Guidance
- **Execute in Main Thread:** Because vault-wide audits run via fast CLI/Python one-liners or native Grep/Glob searches in seconds, execute the audit and generate `implementation_plan.md` directly in the main thread without spawning subagents.

## Failure Recovery & Fallback Protocol
- **False-Positive Wikilink Matches in Code/Templates:** Always strip fenced code blocks (` ```...``` `), inline code spans (`` `...` ``), and `X/Templates/` `{{...}}` placeholders in your regex/Python check before flagging broken or unaliased links.

## Verification & Self-Check Gate
After executing approved cleanup actions, re-run the CLI/Python link and YAML validation check to confirm **0 broken links, 0 non-compliant Wikilinks, 0 missing YAML keys, and 100% `memory-map.md` / `skill-map.md` index coverage** before logging completion.

## Second Brain Continuity & Dependency Handoff
Once approved by the user and verified:
- Create (or append a new `## Run Summary` block and append the window to the `time_window:` YAML list if today's file already exists) `AI-OS/History/YYYY-MM-DD janitor-log.md` using [[X/Templates/log-template.md|log-template]], populating:
  - `agent: "vault-janitor"`
  - `time_window:` list entry `"<last_janitor_timestamp> -> <now>"`
  - Trigger mode (`Scheduled` or `On-the-Fly`), files touched, findings resolved, and vault updates performed.
- Update `last_janitor_timestamp: "<now>"` and append a run summary line (including agent name and time window) in [[AI-OS/History/sync-state.md|sync-state]].
