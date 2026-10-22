---
name: vault-consultant
description: "Use when brainstorming new features, researching Obsidian ecosystem updates, evaluating community or IDE plugins, streamlining vault architecture/navigation/context usage, or seeking creative and structural improvements. Do NOT use when authoring standard notes/skills (use note-architect), running hygiene audits (use vault-janitor), or extracting insights from past session transcripts (use transcript-sweeper)."
aliases:
  - vault-consultant
up: "[[AI-OS/Maps/skill-map.md|skill-map]]"
related:
  - "[[Home.md|Home]]"
  - "[[AI-OS/Maps/vault-map.md|vault-map]]"
  - "[[AI-OS/Maps/skill-map.md|skill-map]]"
  - "[[AI-OS/Maps/memory-map.md|memory-map]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
  - "[[AI-OS/Skills/show-me/SKILL.md|show-me]]"
  - "[[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]]"
  - "[[X/Templates/skill-template.md|skill-template]]"
created: 2026-10-22
collections:
  - ai-os
  - skills
tags:
  - read-only
  - skill
---
# 🤖 Skill: Vault Architect & Innovation Consultant (`vault-consultant`)

## Objective & Trigger Boundaries
Serve as an on-demand creative sparring partner, research engine, and architectural advisor for the Second Brain. The consultant evaluates new Obsidian releases, community plugins, IDE capabilities, and competitor personal knowledge management (PKM) implementations, crossing external innovations with the current vault architecture to suggest streamlined, high-leverage improvements.
- **Use when:**
  - Brainstorming new vault capabilities, architectural refactors, or automation workflows.
  - Researching new features in Obsidian releases, official APIs, or community plugins.
  - Investigating IDE features (Antigravity, Cursor, Claude Code) and agentic developer tool advancements.
  - Benchmarking against competitor PKM/AI systems (e.g., Dendron, Foam, Mem, Logseq, PARA, Linking Your Thinking).
  - Streamlining vault navigation, context window consumption, lazy-loading protocols, or token economy.
- **Do NOT use when:**
  - Templating, structuring, or writing standard vault notes and skills (use [[AI-OS/Skills/note-architect/SKILL.md|note-architect]]).
  - Auditing vault hygiene, broken links, missing YAML keys, or stale projects (use [[AI-OS/Skills/vault-janitor/SKILL.md|vault-janitor]]).
  - Extracting retrospective insights from past session transcripts (use [[AI-OS/Skills/transcript-sweeper/SKILL.md|transcript-sweeper]]).
  - Bootstrapping `.brain/` junctions for code repositories outside the vault (use [[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]]).

## Execution Protocol

### 1. Phase 1 — Baseline Constraints Discovery (Zero-Token Overhead)
Before proposing new ideas or external tools, establish the vault's architectural baseline:
1. **Read Core Identity & Preferences:** Inspect [[Home.md|Home]] for the user briefing, universal preferences, and boot protocols.
2. **Read System Routing Maps:** Inspect [[AI-OS/Maps/vault-map.md|vault-map]] and [[AI-OS/Maps/skill-map.md|skill-map]] to verify existing capabilities, folder structures, and active skills to avoid recommending already-solved patterns.
3. **Scan Domain Knowledge:** Check [[AI-OS/Maps/memory-map.md|memory-map]] if the consultation involves specific past architectural decisions or domain topics.

### 2. Phase 2 — Hybrid Research & Competitive Benchmarking
Gather external intelligence without polluting the active conversation context:
- **Targeted Lookups (Inline):** For specific version verifications, single plugin lookups, or targeted API queries, run `search_web` directly in the main thread.
- **Broad Surveys (Delegated):** When surveying broad ecosystem shifts (e.g., multi-agent coordination frameworks, comparing multiple Obsidian plugins, or evaluating new IDE agent workflows), spawn a `research` subagent. The subagent conducts multi-source web searches and returns a concise synthesis matrix back to the main thread.
- **Key Discovery Targets:**
  - *Obsidian Core & APIs:* New releases, capabilities, frontmatter/property advancements, headless/CLI hooks.
  - *Community Ecosystem:* High-impact plugins evaluated for reliability, maintenance status, and security and potential added value.
  - *IDE & Agent Advancements:* new and interesting IDE features.
  - *Competitor Implementations:* Modular PKM structures, Zettelkasten adaptations, AI-native personal knowledge graphs or any other broad feature semblance.

### 3. Phase 3 — Balanced Innovation Evaluation Matrix
Critique every prospective feature, plugin, or structural proposal through two complementary evaluation lenses:
1. **Token & Architectural Leanliness:**
   - *Token Economy:* Does it respect lazy-loading or inflate system prompt sizes?
   - *CLI / Headless Tooling:* Can it be manipulated via standard terminal tools, Python, or shell scripts?
   - *Plaintext Durability:* Does it preserve clean, human-readable Markdown without vendor lock-in?
   - *Maintenance Overhead:* Will it break across IDE harnesses or require constant upkeep?
2. **High-Leverage Power Features:**
   - *Cognitive Leverage:* Does it dramatically accelerate navigation, visualization, or retrieval?
   - *Visual & Interactive Power:* Can it leverage visual canvases, IDE inline lenses, or custom UI panels to reduce user cognitive load?
1. **Explicit Trade-off Analysis:** Always summarize findings by contrasting gains against costs. Challenge flawed assumptions directly: if an idea adds bloat or duplicates existing functionality, state it plainly.

### 4. Phase 4 — Visual Sparring & Interactive Alignment
Present architectural concepts interactively:
- Follow [[AI-OS/Skills/show-me/SKILL.md|show-me]] to communicate proposed designs if suitable.
- Spar collaboratively with the user, debating alternatives and refining the design based on real feedback.

### 5. Phase 5 — Two-Track Handoff
Once alignment is reached, transition the decision into action:
- **Track 1 (Immediate Tweaks & Minor Enhancements):**
  If the proposal involves modifying existing skills, maps, rules, or templates, generate an in-IDE `implementation_plan.md` with visual diffs and await user approval to execute immediately.
- **Track 2 (Multi-Phase Initiatives & Major Capabilities):**
  If the proposal represents a significant multi-step feature or architectural overhaul, formulate a structured RFC and invoke note-architect to to initialize a new memory documenting the RFC for later referencing.
## Subagent & Parallel Delegation Guidance
- **Main Thread Execution:** Sparring, debate, architectural critique, and implementation planning execute directly in the main agent thread to maintain fast interactive communication with the user.
- **Delegated Research:** Delegate heavy, multi-source external surveys to a `research` subagent to prevent raw web pages and documentation tokens from exhausting the primary context window.

## Failure Recovery & Fallback Protocol
- **Search Failures & API Timeouts:** If external web searches fail or timeout, fall back to analyzing the local vault architecture (`vault-map.md`, `skill-map.md`, `Memories/`) and ask the user for specific version context.
- **Hallucinated or Deprecated Plugins:** Always verify that proposed Obsidian plugins or IDE extensions exist, are actively maintained, and are compatible with recent versions before recommending them.
- **Over-Engineering Guardrail:** If an ideation session veers into unnecessary structural complexity that conflicts with [[Home.md|Home]], intervene with the "Strict Anti-Bloat Litmus Test" to propose a minimal plaintext alternative.

## Verification & Self-Check Gate
Before completing any consultation or handoff, verify:
1. Frontmatter contains all mandatory keys (`name`, `description`, `aliases`, `up`, `related`, `created`, `collections`, `tags`) with `tags: [read-only, skill]`.
2. All internal links follow Path-Complete Wikilink syntax (`[[path/to/file.md|alias]]`).
3. Heading 1 starts with the `'🤖'` watermark (`# 🤖 Skill: ...`).
4. Proposed features are grounded in the user's specific workflow (Data Science, SecOps/GCP, team leadership) rather than generic PKM advice.

## Second Brain Continuity & Dependency Handoff
- **Skill Map Registry:** Registered in [[AI-OS/Maps/skill-map.md|skill-map]] with positive and negative triggers.
- **Memory Persistence:** When a consultation session produces reusable architectural principles or benchmark findings, persist them to `Memories/<Topic>.md` via [[AI-OS/Skills/note-architect/SKILL.md|note-architect]] and register them in [[AI-OS/Maps/memory-map.md|memory-map]].
- **Project Handoff:** For approved multi-phase initiatives, hand off to [[AI-OS/Skills/project-bootstrap/SKILL.md|project-bootstrap]] to create the dedicated project hub in `Efforts/`.
