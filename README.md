# 🧠 AI-Second-Brain

An Obsidian-based AI knowledge management system and persistent context engine tailored for IDE-native AI coding assistants (**Google Antigravity** & **Claude Code**).

AI-Second-Brain acts as an externalized, long-term cognitive layer for your AI pair programmer. Instead of losing architectural context across chat sessions or stuffing multi-megabyte histories into LLM context windows, the Second Brain maintains project architectures, architectural decision records (ADRs), distilled memories, and operational guardrails through an OS-like hierarchy.

---

## 🌟 Key Capabilities

### ⚡ Context-Lean Token Architecture
- **Progressive 1-Hop Map Routing:** Low-overhead navigation maps (`AI-OS/Maps/`) route agents directly to relevant skills, project files, and memory notes. Agents never crawl directories recursively, preserving your LLM token budget.
- **Lowest-Token Search Escalation:** Standardized retrieval protocols escalate from fast filename scans to targeted frontmatter/heading queries, reading only line-sliced excerpts when resolving specific facts.

### 🛠️ Coding Lifestyle Enhancements
- **Autonomous Project Bootstrapping:** Seamlessly provisions new project memory hubs and links them to external codebases on first prompt.
- **Visual-First Planning Mode:** Agents enforce strict planning mode with visual architecture diagrams, control flow maps, and shape-matched code diffs prior to executing code changes.
- **Zero-Pollution Project Linking:** Connects external code repositories to vault project hubs using OS-level directory junctions (`.brain/`), keeping personal vault notes completely isolated from your Git commits.

### 💡 Proactive Learning & Memory Capture
- **Cross-Project Knowledge Distillation:** Automatically extracts reusable technical insights, API patterns, and domain conventions discovered during coding sessions into long-term memory (`Memories/`).
- **Architectural Decision Persistence:** Captures key decisions, technical trade-offs, and environmental constraints in dedicated project ADRs (`decisions.md`).
- **Transcript Continuity Sweeping:** Periodic sweepers analyze session logs to ensure no architectural decisions or documentation references are lost between sessions.

### 🧹 Automated Vault Maintenance & Hygiene
- **Background Health Audits:** Scheduled and on-the-fly janitor sweeps check for broken links, non-compliant Wikilinks, missing YAML frontmatter keys, and unindexed memory notes.
- **AI Watermarking & Access Control:** Strict permission tags (`read-only` vs `write`) and standardized `🤖` Markdown heading watermarks prevent accidental data loss and keep file paths clean.

---

## 🚀 Quickstart: New User Initialization

Follow these four steps to initialize your Second Brain and connect your IDE agent.

### Prerequisites
- **Python 3.10+** installed and available in your system path.
- **Git** installed.
- **Google Antigravity** or **Claude Code** installed as your AI coding harness.
- *(Optional)* **Obsidian Desktop** for visual graph navigation and `.base` database views.

---

### Step 1: Clone & Place the Vault
Clone or place this repository into your local personal workspace directory:
```bash
# Example clone location
git clone <repository-url> "C:/Users/<YourUsername>/Obsidian Vaults/Second Brain"
# Or on macOS/Linux:
# git clone <repository-url> "$HOME/Obsidian Vaults/Second Brain"
```

---

### Step 2: Personalize `Home.md` (Safe Customization Guide)

`Home.md` is the single source of truth auto-included by your IDE AI agent. It contains both your personal profile and the vault's core operating system logic.

To ensure your agent understands you while **avoiding accidental breakage of vault logic**, follow this customization map:

#### 🟢 Safe & Recommended to Customize
Open [Home.md](file:///Home.md) in your editor and personalize the following sections:

| Section | What to Put | Purpose |
| :--- | :--- | :--- |
| `## Job` | Your current role, organization, and primary technology stack | Grounds the agent in your day-to-day engineering context |
| `## Interests` | Technologies, frameworks, or subjects you want to deepen understanding in | Helps the agent highlight relevant patterns and learning points |
| `## Preferences` | Communication style (e.g., concise, challenge assumptions, direct answers) | Guides how the agent speaks and reasons with you |
| `Vault Root` *(under Boot Protocol)* | Set to your **exact absolute path** to this vault directory | Essential: agents and setup scripts use this to resolve vault files |

> [!IMPORTANT]
> **Example Vault Root Format:**
> - Windows: `- **Vault Root:** C:/Users/<YourUsername>/Obsidian Vaults/Second Brain`
> - macOS/Linux: `- **Vault Root:** /home/<YourUsername>/Obsidian Vaults/Second Brain`

#### 🛑 Protected System Logic (Do NOT Modify)
The remaining sections in [Home.md](file:///Home.md) govern agent operating safety, token conservation, and link integrity. Leave these sections intact:
- **`## Boot & Navigation Protocol` (Steps 1–5):** Enforces lazy-loading sequences and the project bootstrap gate.
- **`### Subject Matter Search & Retrieval Protocol`:** Prevents recursive token-wasting file reads.
- **`## Universal Rules & Permissions`:** Enforces strict visual planning, read-only permissions, and internal link formatting.

---

### Step 3: Run the Automated Harness Setup Script

Run the automated onboarding script for your IDE harness. This dynamically registers the Second Brain skills and links global agent instructions to your personalized `Home.md`.

#### For Google Antigravity
Open a terminal in the vault root and execute:
```bash
python AI-OS/Skills/scripts/setup_antigravity.py
```
**What this configures:**
1. Registers `AI-OS/Skills/` in `~/.gemini/config/skills.json` for dynamic 1-hop skill discovery.
2. Points global `~/.gemini/config/GEMINI.md` directly to `<Vault-Root>/Home.md` via native include directive (`@[Home.md](...)`).
3. Ensures vault-root `GEMINI.md` includes `@[Home.md](Home.md)` for 0-call atomic auto-expansion.
4. Resolves your real local Python interpreter path (bypassing Windows Store `WindowsApps` execution aliases) in `AI-OS/Skills/transcript-sweeper/SKILL.md`.

#### For Claude Code
Open a terminal in the vault root and execute:
```bash
python AI-OS/Skills/scripts/setup_claude.py
```
**What this configures:**
1. Creates a Directory Junction (Windows) or symlink (macOS/Linux) at `~/.claude/skills` pointing to `AI-OS/Skills/`.
2. Points global `~/.claude/CLAUDE.md` to `<Vault-Root>/Home.md` via `@<Vault-Root>/Home.md`.
3. Ensures vault-root `CLAUDE.md` includes `@Home.md`.

---

### Step 4: Connecting Your First Code Repository (`.brain` Junctions)

Once your harness is configured, you can connect any external coding repository to the Second Brain:

#### Automated Agent Flow (Recommended)
Open your project repository in your IDE and prompt your agent with any development task. 
1. The agent inspects the repository root for `.brain/`.
2. When missing, it automatically creates a project memory hub in `Efforts/<Project-Name>/` (`context.md`, `decisions.md`, `changelog.md`).
3. It appends `.brain` and `.brain/` to your `.gitignore`.
4. It creates an OS-level directory junction linking `<repo_path>/.brain` to `<vault_root>/Efforts/<Project-Name>`.

#### Manual Setup Alternative
You can also link any repository manually at any time:

**Windows (PowerShell — No Administrator Privileges Required):**
```powershell
# 1. Add .brain to your project's .gitignore
Add-Content -Path "<repo_path>/.gitignore" -Value "`n.brain`n.brain/"

# 2. Create the directory junction
New-Item -ItemType Junction -Path "<repo_path>/.brain" -Target "<vault_root>/Efforts/<Project-Name>"
```

**Linux / macOS:**
```bash
# 1. Add .brain to your project's .gitignore
echo -e "\n.brain\n.brain/" >> "<repo_path>/.gitignore"

# 2. Create the symbolic link
ln -s "<vault_root>/Efforts/<Project-Name>" "<repo_path>/.brain"
```

---

### Step 5 (Optional): Vault Maintenance — On-Demand vs. Scheduled Automations

The Second Brain includes two maintenance skills—`transcript-sweeper` (continuity sweeping across IDE transcripts) and `vault-janitor` (link, frontmatter, and map hygiene audits). You can trigger them **on-demand** whenever you want, or configure them as **scheduled automations**.

#### Option A: Run On-Demand (Prompt When Wanted)
Simply ask your agent in chat whenever you want a sweep or audit:
- **Continuity Sweep:** *"Run `transcript-sweeper` to check for unlogged session updates."*
- **Vault Hygiene Audit:** *"Run `vault-janitor` to audit vault links and frontmatter."*

#### Option B: Scheduled Background Automations (Google Antigravity)
If you prefer these skills to run unattended on a schedule, run `/automation` in Antigravity chat (or open the **Automations** panel) to create them:

1. **Vault Hygiene Audit (`vault-janitor`):**
   - **Workspace:** `<Vault-Root>`
   - **Required Access Grants:** `read_file(<Vault-Root>)`, `write_file(<Vault-Root>)`
2. **Daily Transcript Sweeper (`transcript-sweeper`):**
   - **Workspace:** `<Vault-Root>`
   - **Required Access Grants:**
     - `read_file(<Vault-Root>)`, `write_file(<Vault-Root>)`
     - `read_file(<User-Home>/.gemini/antigravity/brain)`
     - `read_file(<User-Home>/.claude/projects)`
     - `unsandboxed(<Python-Posix-Path> -X utf8 AI-OS/Skills/transcript-sweeper/scripts/sanitize_transcripts.py)`
   > [!NOTE]
   > Because Windows AppContainer sandboxing isolates sibling conversation folders in `~/.gemini/antigravity/brain/` and Antigravity's `unsandboxed(...)` rule requires an exact 1:1 full-string match (no `*` wildcards), `sanitize_transcripts.py` reads watermarks directly from `AI-OS/History/sync-state.md` with zero CLI arguments so the command string stays static across scheduled runs.

---

## 📂 Vault Architecture Overview

```text
Second Brain/
├── Home.md                       # Single source of truth (profile, guardrails, boot protocol)
├── GEMINI.md / CLAUDE.md         # Native IDE entry points (0-call auto-expansion)
├── AI-OS/
│   ├── Maps/                     # Low-token routing maps (vault-map, skill-map, memory-map)
│   ├── Skills/                   # Modular agent skills & automated onboarding scripts
│   │   ├── scripts/              # setup_antigravity.py, setup_claude.py
│   │   └── <skill>/SKILL.md      # Procedural workflows (planning, bootstrap, hygiene, etc.)
│   └── History/                  # Activity logs, sweep records, and sync-state watermarks
├── Efforts/                      # Active and archived project hubs (.brain targets)
│   └── <Project-Name>/
│       ├── context.md            # High-level architecture, roadmap, tech stack
│       ├── decisions.md          # Architectural Decision Records (ADRs)
│       └── changelog.md          # Chronological project update logs
├── Memories/                     # Distilled cross-project technical concepts & domain notes
└── X/Templates/                  # Standardized templates for notes, projects, skills, and logs
```

---

## 🖥️ Obsidian UI Integration

While the Second Brain is optimized for CLI and IDE agents, human developers can browse it interactively inside **Obsidian**:
- **Database Views (`.base`):** Use `Efforts/Projects.base`, `Memories/Knowledge.base`, and `AI-OS/History/Logs.base` for filtered tabular views of projects, distilled knowledge, and activity history.
- **Path-Complete Wikilinks:** All internal vault links use strict path-complete syntax with aliases (e.g., `[[Folder/note.md|note]]`), rendering seamlessly in Obsidian's interactive graph while remaining directly resolvable by CLI tools.
