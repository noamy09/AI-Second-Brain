---
name: note-architect
description: Use when creating, structuring, or templating any vault note, when asked to remember/save information into Memories/ (or when reusable insights are discovered), or when designing, creating, or updating an agent skill in AI-OS/Skills/. DO NOT use if the task won't require updating or creating a new vault note.
aliases:
  - note-architect
  - skill-architect
up: "[[AI-OS/Maps/skill-map.md|skill-map]]"
related:
  - "[[AI-OS/Maps/vault-map.md|vault-map]]"
  - "[[AI-OS/Maps/skill-map.md|skill-map]]"
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
  - "[[AI-OS/Skills/show-me/SKILL.md|show-me]]"
  - "[[X/Templates/base-template.md|base-template]]"
  - "[[X/Templates/log-template.md|log-template]]"
  - "[[X/Templates/skill-template.md|skill-template]]"
  - "[[X/Templates/project-template.md|project-template]]"
  - "[[X/Templates/decisions-template.md|decisions-template]]"
  - "[[X/Templates/changelog-template.md|changelog-template]]"
created: 2026-10-16
collections:
  - ai-os
  - skills
tags:
  - read-only
  - skill
---
# 🤖 Skill: Note, Memory & Skill Architect (`note-architect`)

## Objective & Trigger Boundaries
Provide the single source of truth for structuring, templating, and governing all notes, memories, and agent skills across the Second Brain.
- **Use when:** Creating or updating any vault note, persisting reusable insights into `Memories/` ("Remember" workflow), or designing, creating, or upgrading an agent skill in `AI-OS/Skills/<skill-name>/SKILL.md` ("Skill Architect" workflow).
- **Do NOT use when:** Initializing a `.brain` directory junction for a code repository (use [[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]]), running delta continuity sweeps across IDE transcripts (use [[AI-OS/Skills/transcript-sweeper/SKILL.md|transcript-sweeper]]), or running vault-wide hygiene audits (use [[AI-OS/Skills/vault-janitor/SKILL.md|vault-janitor]]).

## Execution Protocol

### 1. Core Vault Note & YAML Rules
1. **Always Use a Template:** Every note or skill created in the vault must use a template from `X/Templates/`. When in doubt, default to [[X/Templates/base-template.md|base-template]].
2. **Required YAML Frontmatter:** Every note must begin with these mandatory keys:
   - `up`: Path-complete Wikilink to the parent map or note (e.g., `"[[AI-OS/Maps/vault-map.md|vault-map]]"`).
   - `related`: List of path-complete Wikilinks to related notes.
   - `created`: Creation date in `YYYY-MM-DD` format.
   - `collections`: Array of lowercase category groupings.
   - `tags`: Must include permission tag (`read-only` or `write`) AND the semantic type tag (`memory`, `skill`, `log`, `project`, `decisions`, or `changelog`).
   - **Path-Complete Wikilinks:** Every internal link in YAML or note bodies must include the path from vault root plus an alias: `[[Folder/Subfolder/file.md|file]]`.
3. **AI Watermarking (`🤖`):** Every note or skill created by an AI agent must include the `'🤖'` emoji in its **H1 Markdown heading** (`# 🤖 <Title>`), keeping filenames clean ASCII/kebab-case for CLI and IDE routing.
4. **Memory $\leftrightarrow$ Project Context & ADR Linking:** Whenever technical documentation, user instructions, or reusable insights are saved into `Memories/<Topic Name>.md` during a project or sweep:
   - Record any external URLs or doc paths under `sources:` in the memory note's YAML frontmatter.
   - Register or update the note's 1-line row in [[AI-OS/Maps/memory-map.md|memory-map]].
   - When inside a project scope (`.brain/` or `Efforts/<Project>/`), cross-link `[[Memories/<Topic Name>.md|<Topic Name>]]` in `Efforts/<Project>/context.md` (`## 4. Linked Vault Memories & Domain References` + `related:` YAML) and `Efforts/<Project>/decisions.md` (if architectural).

### 2. Template Routing Table

| Note Type | Target Folder | Template Link | Naming Syntax | Semantic Tag | Default Permission |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **General / Memory** | `Memories/` | [[X/Templates/base-template.md\|base-template]] | `Topic Name.md` | `memory` | `read-only` |
| **Agent Skill** | `AI-OS/Skills/<skill-name>/` | [[X/Templates/skill-template.md\|skill-template]] | `SKILL.md` | `skill` | `read-only` |
| **Activity / Sweep / Janitor Log** | `AI-OS/History/` | [[X/Templates/log-template.md\|log-template]] | `YYYY-MM-DD <sweep\|janitor>-log.md` | `log` | `write` |
| **Transcript** | `AI-OS/History/` | [[X/Templates/log-template.md\|log-template]] | `YYYY-MM-DD transcript-<slug>.md` | `log` | `write` |
| **Project Context** | `Efforts/<Project>/` | [[X/Templates/project-template.md\|project-template]] | `context.md` | `project` | `write` |
| **Project Decisions** | `Efforts/<Project>/` | [[X/Templates/decisions-template.md\|decisions-template]] | `decisions.md` | `decisions` | `write` |
| **Project Changelog** | `Efforts/<Project>/` | [[X/Templates/changelog-template.md\|changelog-template]] | `changelog.md` | `changelog` | `write` |

### 3. Memory Creation & Update Protocol ("Remember" Workflow)
Whenever the user asks you to remember/save information—or when you discover reusable domain or technical knowledge worth persisting in `Memories/`:
1. **Check Existing Memories:** Read [[AI-OS/Maps/memory-map.md|memory-map]] (and scan `Memories/` if needed) to check whether a relevant memory note already exists.
2. **Create or Update the Memory Note:**
   - **New Memory:** Instantiate `Memories/<Topic Name>.md` from [[X/Templates/base-template.md|base-template]] (`up: "[[AI-OS/Maps/memory-map.md|memory-map]]"`, `tags: [read-only, memory]`, `# 🤖 <Topic Name>`, and `sources:` if derived from external docs).
   - **Existing Memory:** Append or update the relevant section in `Memories/<Topic Name>.md` (include the edit in your `implementation_plan.md` or confirm with the user since `Memories/` notes default to `read-only`).
3. **Update `memory-map.md`:** Append or update the corresponding row in [[AI-OS/Maps/memory-map.md|memory-map]] with `[[Memories/<Topic Name>.md|<Topic Name>]]`, its `collections`, and a concise 1-line summary/trigger description.
4. **Link to Active Project (If in Project Scope):**
   - If working inside a project with `.brain/` (or `Efforts/<Project>/`):
     - Add `[[Memories/<Topic Name>.md|<Topic Name>]]` under `## 4. Linked Vault Memories & Domain References` and `related:` YAML in `.brain/context.md`.
     - If the memory informs an architectural or dependency decision, also link it in `.brain/decisions.md` (`Reference / Memory` column or ADR `- **References & Memories:**`).
     - Add `"[[Efforts/<Project>/context.md|context]]"` to the memory note's `related:` YAML array.

### 4. Skill Architecture & Creation Protocol ("Skill Architect" Workflow)
Whenever creating a new skill or upgrading an existing skill in `AI-OS/Skills/<skill-name>/SKILL.md`:

1. **Step 1 — Pre-Plan Discovery & Overlap Audit:**
   - Read [[AI-OS/Maps/skill-map.md|skill-map]] and [[AI-OS/Maps/memory-map.md|memory-map]] to check for overlapping skills, boundary conflicts, or relevant domain notes in `Memories/`.
   - If trigger boundaries, failure modes, or expected vault outputs are ambiguous, ask **1–2 targeted clarifying questions** before generating `implementation_plan.md`.
2. **Step 2 — Single-File First Design & Edge-Case Guardrails:**
   - Provision `AI-OS/Skills/<skill-name>/` using lowercase `kebab-case` for `<skill-name>`.
   - **Single-File First:** Default to placing all instructions, examples, and inline CLI/code snippets directly inside `AI-OS/Skills/<skill-name>/SKILL.md`. Only create `scripts/` or `references/` subfolders when the user explicitly requests them or when deterministic external sanitization is strictly required.
   - **No Rule Duplication:** Do not repeat universal rules from [[Home.md|Home]]. Only include task-specific context or safety guardrails inside `SKILL.md` for **edge cases** not already covered by [[Home.md|Home]] (e.g., prompt-injection sanitization for untrusted external transcripts, or destructive cloud/database operations).
3. **Step 3 — YAML Trigger Engineering & Mandatory Skill Anatomy:**
   - Instantiate `AI-OS/Skills/<skill-name>/SKILL.md` from [[X/Templates/skill-template.md|skill-template]].
   - **Positive + Negative `description` Engineering:** Because IDE harnesses only inject `name` and `description` into the system prompt before skill activation, `description` MUST include both:
     - **Positive Triggers (`Use when...`):** Explicit task scenarios, keywords, and tool contexts.
     - **Negative Triggers (`Do NOT use when...`):** Clear disambiguation boundaries against neighboring skills or risky edge cases.
   - Set `aliases: ["<skill-name>"]` and standard YAML keys (`up: "[[AI-OS/Maps/skill-map.md|skill-map]]"`, `related`, `created`, `collections: [ai-os, skills]`, `tags: [read-only, skill]`).
   - Populate all **6 mandatory anatomical sections** from [[X/Templates/skill-template.md|skill-template]]:
     1. `## Objective & Trigger Boundaries`
     2. `## Execution Protocol`
     3. `## Subagent & Parallel Delegation Guidance`
     4. `## Failure Recovery & Fallback Protocol`
     5. `## Verification & Self-Check Gate`
     6. `## Second Brain Continuity & Dependency Handoff`
4. **Step 4 — Second Brain Dependency & Integration Checklist:**
   Every skill creation or update plan must verify and include necessary updates across these 5 vault dependencies:
   - [ ] **Skill Registry (`skill-map.md`):** Append or update the skill's row in [[AI-OS/Maps/skill-map.md|skill-map]] with `[[AI-OS/Skills/<skill-name>/SKILL.md|<skill-name>]]` and its Positive/Negative trigger summary.
   - [ ] **Sibling Skill Overlap & Cross-Linking (`AI-OS/Skills/`):** Check existing skills via [[AI-OS/Maps/skill-map.md|skill-map]] first—only read or edit a sibling `SKILL.md` file if `skill-map.md` indicates a direct trigger boundary conflict that requires updating its `related:` YAML or `"Do NOT use when..."` triggers.
   - [ ] **Domain Memory Cross-Linking (`Memories/`):** Link relevant `[[Memories/<Topic>.md|<Topic>]]` notes in the skill's `related:` YAML and `## Execution Protocol` so the agent loads domain constraints alongside procedural steps.
   - [ ] **Hygiene & Watermark Governance (`vault-janitor` & `sync-state.md`):** If the skill introduces a new scheduled/maintenance agent or file convention, update [[AI-OS/Skills/vault-janitor/SKILL.md|vault-janitor]] audit rules and/or [[AI-OS/History/sync-state.md|sync-state]] watermark keys.
   - [ ] **Global Entry Point (`Home.md`):** Check if [[Home.md|Home]] requires an update—**strictly** when the skill introduces a new mandatory global boot or planning gate.
   - *(Note: No harness script re-run is needed; Antigravity's `skills.json` and Claude Code's `skills` junction dynamically discover any new `AI-OS/Skills/<skill-name>/SKILL.md` folder).*

## Subagent & Parallel Delegation Guidance
- **Execute in Main Thread:** Note creation, memory persistence, and skill authoring require direct user alignment (via `ask_question` and `implementation_plan.md`) and fast file writes; execute them directly in the main agent thread.
- **Optional Research Delegation:** Only delegate to a `research` subagent if distilling a new memory or skill requires surveying a large external codebase or multiple documentation sources first.

## Verification & Self-Check Gate
Before completing any note, memory, or skill creation/update task, verify:
1. All mandatory YAML keys (`up`, `related`, `created`, `collections`, `tags`) are present and properly formatted.
2. Every internal Wikilink uses Path-Complete Alias syntax (`[[path/from/vault/root.md|alias]]`, with `\|` escaped inside Markdown tables) and resolves to an existing file on disk.
3. The H1 heading includes the `'🤖'` watermark (`# 🤖 ...`).
4. For skills: `description` contains both `"Use when..."` and `"Do NOT use when..."`, all 6 anatomical sections from [[X/Templates/skill-template.md|skill-template]] are populated, and [[AI-OS/Maps/skill-map.md|skill-map]] is updated.
5. For memories: [[AI-OS/Maps/memory-map.md|memory-map]] is updated, `sources:` is populated if derived from external docs, and `.brain/context.md` / `.brain/decisions.md` are cross-linked if in project scope.

## Second Brain Continuity & Dependency Handoff
- **Memory Handoff:** Register every new/updated memory in [[AI-OS/Maps/memory-map.md|memory-map]] and link it to `.brain/context.md` and `.brain/decisions.md` when working inside an active project.
- **Skill Handoff:** Register every new/updated skill in [[AI-OS/Maps/skill-map.md|skill-map]], cross-link related skills/memories, and update [[AI-OS/Skills/vault-janitor/SKILL.md|vault-janitor]] or [[AI-OS/History/sync-state.md|sync-state]] if new structural conventions or watermarks were introduced.
