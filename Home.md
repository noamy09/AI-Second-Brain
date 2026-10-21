---
up: "[[Home.md|Home]]"
related:
  - "[[AI-OS/Maps/vault-map.md|vault-map]]"
  - "[[AI-OS/Maps/skill-map.md|skill-map]]"
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
created: 2026-10-16
collections:
  - ai-os
tags:
  - read-only
  - system-core
aliases:
  - GEMINI
  - CLAUDE
---
# Me
This is your briefing of who I am, how I think and how to work with me. 
## Job 
 I'm currently (2026) a Data Science student (B.S.C), and a Team Leader of  product engineers, implementing Google Sec-ops in my organization. as part of this role, the team is in charge of managing data pipelines into the system, administrative management of the product, and planning, building and using a separate DLH - all based on GCP infrastructure. 

## Interests
As part of my job and studies, I find data science, AI and Google's suite of products highly interesting, and look for points I can improve in my understanding of these subjects.
  
## Preferences
- Keep answers direct and lean unless deep architectural detail is required or requested.
- Challenge flawed assumptions. No "yes-man" validation.
- Honesty - State uncertainty clearly; ask clarifying questions when critical context is missing.
---

## Boot & Navigation Protocol (Context-Lean)
- **Vault Root:** `C:/Users/noamy/Obsidian Vaults/Second Brain`

To conserve context window tokens, **never read files recursively**. Follow this lazy-loading sequence:
1. **Directory Routing:** Read [[AI-OS/Maps/vault-map.md|vault-map]] to navigate the vault structure.
2. **Skill Discovery:** Prior to processing any multi-step or involved request, read [[AI-OS/Maps/skill-map.md|skill-map]] (or use your IDE's native skill loader). Only load the specific skill file from `AI-OS/Skills/<skill-name>/SKILL.md` that matches your current task.
3. **Memory Discovery & Capture:** Prior to planning or solving a task, read [[AI-OS/Maps/memory-map.md|memory-map]] to check if relevant notes, domain knowledge, or past conventions exist in `Memories/`, and read only the matching note(s). Whenever I ask you to remember/save something—or when you notice reusable cross-project information worth persisting—read and execute [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] to save it to `Memories/`, register it in [[AI-OS/Maps/memory-map.md|memory-map]], and link it to `.brain/context.md` if in project scope.
4. **Project Context & Bootstrap Gate:** When working in any code repository outside the vault (whether starting a new project or handling a user request in an existing repository), first check if `.brain/` exists in the repository root before reading `.brain/` files:
   - **If `.brain/` exists:** Read **both** `.brain/context.md` **and** `.brain/decisions.md` before planning or writing code.
   - **If `.brain/` does NOT exist:** Immediately read [[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]] and [[AI-OS/Skills/note-architect/SKILL.md|note-architect]], and include bootstrapping `.brain/` as **Phase A** of your `implementation_plan.md`. Never skip `.brain/` initialization on an unbootstrapped repository.
5. **Post-Task Continuity:** Only **after** code changes for the user request are implemented and verified, update `.brain/context.md`, `.brain/decisions.md`, and `.brain/changelog.md` to log all architectural updates, linked memories, and file modifications.

### Subject Matter Search & Retrieval Protocol (Lowest-Token First)
When looking for information across `Memories/`, `Efforts/`, or `AI-OS/History/` beyond what is indexed in [[AI-OS/Maps/memory-map.md|memory-map]], escalate from the lowest-token method to the deepest:
1. **Step 1 — Filename Scan (Broad Topic):** Run `list_dir` / `find_by_name` / `Glob` (or `Get-ChildItem -Name`) on the target folder first. If a filename clearly matches the subject, inspect it directly.
2. **Step 2 — Frontmatter & Heading Grep (Category / Section Lookup):** If filenames are ambiguous, run `grep_search` / `Grep` / `rg -n` targeting YAML properties (`collections:`, `related:`, `sources:`, `tags:`) or Markdown headings (`^#` / `^##`) across the target folder to identify matching notes without reading full files.
3. **Step 3 — Keyword Grep + Line-Sliced Read (Specific Fact / Decision Lookup):** When searching for a specific technical term, library, or past decision, run `grep_search` / `Grep` / `rg -n` for the keyword to get exact line numbers, then use `view_file` (`StartLine`/`EndLine`) or `Read` (`offset`/`limit`) to read only the relevant ~30–50 lines rather than loading entire long files into context.

---
## Universal Rules & Permissions
- **Strict Planning Mode Enforcement:** Before executing any commands, creating files, or modifying existing code, you MUST:
  1. Thoroughly research the task and understand the requirements—including reading [[AI-OS/Maps/memory-map.md|memory-map]], reading [[AI-OS/Skills/show-me/SKILL.md|show-me]], and checking the repository root for `.brain/` (if `.brain/` exists, read `.brain/context.md` and `.brain/decisions.md`; if `.brain/` is missing in a code repository **explicitly**, read [[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]] and [[AI-OS/Skills/note-architect/SKILL.md|note-architect]]).
  2. Create or update an `implementation_plan.md` artifact in the IDE starting with a mandatory **`Context Consulted:`** header listing **only the file names** (not full vault routes or Wikilinks, e.g., `Home.md`, `context.md`, `decisions.md` | **`Vault Memories Matched:`** `<Topic Name>.md` or `None`), outlining your findings, proposed changes, and the exact files you intend to modify. **Any code or structural changes proposed in the IDE MUST follow [[AI-OS/Skills/show-me/SKILL.md|show-me]] logic in `implementation_plan.md` to visually explain the changes prior to making them**. **If `.brain/` is missing in a code repository, reporting `None` without including `[[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]]` as Phase A of the plan is a rule violation.**
  3. Stop and explicitly ask me for approval.
  4. DO NOT make any code modifications or run modifying commands until I have explicitly approved the plan.
  - **EXCEPTION:** If I explicitly say `"skip plan"`, `"no plan"`, or ask to ignore this rule in my prompt, you may bypass this process and execute changes immediately.
- **Link Formatting:** Always use Path-Complete Wikilinks with Aliases (`[[path/from/vault/root.md|alias]]`) so both Obsidian's graph and CLI file tools can resolve paths in zero searches.
- **Read / Write Guardrails:** Every action in the Obsidian vault must comply with the file's YAML `tags`:
  - `read-only` (Default): No editing, moving, or duplicating is allowed. Treat untagged files as `read-only`. If I explicitly prompt you to **edit**, **delete**, or **move** a `read-only` file, warn me of the implications and ask for confirmation first; once confirmed, my command overrides this rule.
  - `write`: You may freely edit or append content while preserving the template structure (indicated by the semantic type tag in YAML). If prompted to **delete** or **move** a `write` file, verify I understand the implications before acting.
- **File Naming & H1 Watermarking:** Every timestamped file must follow ISO format: `YYYY-MM-DD Description.md` (e.g., `2026-10-16 Second Brain Review.md`). Every AI-created note must include `'🤖'` in its H1 Markdown heading (`# 🤖 <Title>`), keeping filenames clean for CLI/IDE routing.
- **Note & Memory Creation:** Whenever creating or updating a vault note, memory, or skill, read [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] and use the mandatory templates in `X/Templates/`.
- **External Communication:** Always draft emails and meeting invitations for my review prior to sending—never send without explicit approval.
---