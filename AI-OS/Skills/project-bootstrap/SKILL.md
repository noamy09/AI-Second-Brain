---
name: project-bootstrap
description: Use when initializing a new coding project/repository or when working in an existing repository that lacks a .brain directory link to the Second Brain. Do NOT use when .brain/ already exists in the repository root and when working directly inside the Second Brain vault.
aliases:
  - project-bootstrap
up: "[[AI-OS/Maps/skill-map.md|skill-map]]"
related:
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
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
# 🤖 Skill: Automated Project Bootstrap (`project-bootstrap`)

## Objective & Trigger Boundaries
Provision a project's memory hub in the Second Brain (`Efforts/<Project-Name>/`) and link it to the local code repository via a `.brain` directory junction.
- **Use when:** Initializing a new coding repository, or working in an existing code repository outside the vault where `.brain/` is missing (**Phase A** of `implementation_plan.md`).
- **Do NOT use when:** `.brain/` already exists and resolves in the repository root or when working directly inside the Second Brain vault,

## Execution Protocol

### 1. Provision or Reuse the Vault Project Hub
Check if `Efforts/<Project-Name>/` already exists in the vault (using `kebab-case` or `PascalCase` matching the repo name, avoiding spaces).
- If `Efforts/<Project-Name>/` already exists with its project files, reuse it and proceed to **Step 3**.
- Otherwise, create a new directory at `Efforts/<Project-Name>/`.

### 2. Instantiate Baseline Project Files from Templates
First read [[AI-OS/Skills/note-architect/SKILL.md|note-architect]], [[AI-OS/Maps/memory-map.md|memory-map]], and the corresponding templates from `X/Templates/`, then create three files inside `Efforts/<Project-Name>/`:
1. **`Efforts/<Project-Name>/context.md`** (from [[X/Templates/project-template.md|project-template]]):
   - Populate `created` with today's `YYYY-MM-DD`.
   - Set `ide` to the active harness (`antigravity`, `claude-code`, or any other IDE currently being used).
   - Set `repo_path` to the absolute path of the code repository.
   - Set `log_path` to the IDE's local session log directory (`~/.gemini/antigravity/brain/` for Antigravity, or `~/.claude/projects/` for Claude Code).
   - Fill in the initial High-Level Overview, Tech Stack, and Architecture based on the repository and user prompt, and link any relevant existing `[[Memories/<Topic>.md|<Topic>]]` notes from [[AI-OS/Maps/memory-map.md|memory-map]] under `## 4. Linked Vault Memories & Domain References` and `related:` YAML.
   - **Baseline Only:** When bootstrapping an existing repository alongside a user request, record the **existing baseline state** here and keep the pending user request unchecked (`- [ ]`) until after the code changes are actually implemented and verified.
2. **`Efforts/<Project-Name>/decisions.md`** (from [[X/Templates/decisions-template.md|decisions-template]]):
   - Record initial architectural choices, existing library selections, environment constraints, and any linked `[[Memories/<Topic>.md|<Topic>]]` reference notes.
3. **`Efforts/<Project-Name>/changelog.md`** (from [[X/Templates/changelog-template.md|changelog-template]]):
   - Add the initial baseline entry (`YYYY-MM-DD`) documenting project bootstrap and `.brain` initialization. Do **not** log unexecuted code changes in past tense before implementing them.

### 3. Git Hygiene First (Prevent Accidental Staging)
Check whether `.gitignore` or `.git/` exists in `<repo_path>`:
- If `.gitignore` (or `.git/info/exclude`) exists, ensure `.brain` and `.brain/` are appended before creating the directory link so personal vault files are never staged or committed to remote Git repositories.
- Only run `git` CLI commands if `.git/` exists in the repository.

### 4. Create the `.brain` Link in the Code Repository
Link the repository directly to the vault's project folder so all future agent sessions can access `.brain/context.md`, `.brain/decisions.md`, and `.brain/changelog.md` locally without requiring Administrator privileges:
- **Windows (PowerShell — Directory Junction, No Admin Required):**
  ```powershell
  New-Item -ItemType Junction -Path "<repo_path>\.brain" -Target "<vault_root>\Efforts\<Project-Name>"
  ```
- **Linux / WSL / macOS:**
  ```bash
  ln -s "<vault_root>/Efforts/<Project-Name>" "<repo_path>/.brain"
  ```

## Subagent & Parallel Delegation Guidance
- **Execute in Main Thread:** Bootstrapping `.brain/` is a lightweight, mandatory Phase A prerequisite before project execution and must run directly in the main agent thread.

## Failure Recovery & Fallback Protocol
- **Existing Broken `.brain` Junction or Conflicting Directory:** If `<repo_path>\.brain` exists as a broken junction (target moved/renamed), remove the junction link (`(Get-Item "<repo_path>\.brain").Delete()` in PowerShell without deleting target contents) and recreate it pointing to `<vault_root>\Efforts\<Project-Name>`.
- **Sandbox Restriction on External Vault Path:** If creating files in `<vault_root>\Efforts\<Project-Name>` or linking `<repo_path>\.brain` is blocked when running inside a workspace sandbox outside the vault, use `BypassSandbox: true` for the junction/vault creation step after plan approval.

## Verification & Self-Check Gate
Before moving from Phase A (Bootstrap) to code implementation, verify:
1. `.brain/context.md`, `.brain/decisions.md`, and `.brain/changelog.md` are readable via `<repo_path>/.brain/`.
2. If the repository is a Git project, `git status` confirms `.brain` is ignored and untracked.
3. All three files contain valid YAML frontmatter and Path-Complete Wikilinks per [[AI-OS/Skills/note-architect/SKILL.md|note-architect]].

## Second Brain Continuity & Dependency Handoff
Only **after** the user request's code modifications are implemented and verified (and at the end of every subsequent session on this project):
- Append the completed code and project-specific vault changes to `.brain/changelog.md`.
- Update `.brain/decisions.md` if new dependencies or design decisions were introduced, and cross-link any newly distilled `[[Memories/<Topic>.md|<Topic>]]` reference notes in both the ADR entry and `related:` YAML.
- Update `.brain/context.md` (checking off completed roadmap items `- [x]` and updating entry points, architecture, or next steps if changed).
