---
up: "[[Home.md|Home]]"
related:
  - "[[AI-OS/Maps/vault-map.md|vault-map]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
created: 2026-10-16
collections:
  - ai-os
tags:
  - read-only
  - system-core
---
# 🤖 Skill Registry Map

To minimize context overhead, **only read a skill file below when your current task matches its trigger condition.** (In Antigravity and Claude Code, these skills are also natively registered for 1-hop activation).

| Skill Link | Trigger Condition |
| :--- | :--- |
| [[AI-OS/Skills/project-bootstrap/SKILL.md\|project-bootstrap]] | **Use when:** Initializing a new coding project/repository, or working in an existing repository that lacks a `.brain` directory junction. **Do NOT use when:** `.brain/` already exists and is linked, or when working directly inside the Second Brain vault. |
| [[AI-OS/Skills/note-architect/SKILL.md\|note-architect]] | **Use when:** Creating or updating any vault note, remembering/saving reusable information into `Memories/` (and registering it in [[AI-OS/Maps/memory-map.md\|memory-map]]), or designing, creating, or updating an agent skill in `AI-OS/Skills/` ("Skill Architect" workflow). **Do NOT use when:** Running transcript sweeps, vault hygiene audits, or `.brain` junction bootstrapping. |
| [[AI-OS/Skills/transcript-sweeper/SKILL.md\|transcript-sweeper]] | **Use when:** Running a scheduled or on-the-fly Delta Continuity Sweep across IDE transcripts and active projects since `last_sweep_timestamp_<harness>`. **Do NOT use when:** Performing real-time in-session `.brain/` updates after a coding task or auditing vault link/YAML hygiene. |
| [[AI-OS/Skills/vault-janitor/SKILL.md\|vault-janitor]] | **Use when:** Running a scheduled or on-the-fly Delta Vault Hygiene audit for broken links, unindexed `Memories/` notes, skill anatomy/registry compliance, missing YAML keys, semantic tags, empty files, and stale projects since `last_janitor_timestamp`. **Do NOT use when:** Sweeping IDE conversation transcripts or creating individual notes/skills. |
| [[AI-OS/Skills/show-me/SKILL.md\|show-me]] | **Use when:** Writing an `implementation_plan.md` in the IDE to visually explain proposed code or structural changes prior to making them, or explaining logic, control flow, architecture, UI hierarchy, or diffs visually. **Do NOT use when:** Answering trivial single-line questions that require no structural or code explanation, or running background transcript sweeps/hygiene audits. |
| [[AI-OS/Skills/vault-consultant/SKILL.md\|vault-consultant]] | **Use when:** Brainstorming new vault capabilities, researching Obsidian releases/plugins or IDE features, analyzing competitor note systems, streamlining vault architecture/navigation/context usage, or seeking structural advice. **Do NOT use when:** Templating/authoring standard notes/skills (use [[AI-OS/Skills/note-architect/SKILL.md\|note-architect]]), running hygiene audits (use [[AI-OS/Skills/vault-janitor/SKILL.md\|vault-janitor]]), or sweeping past session transcripts (use [[AI-OS/Skills/transcript-sweeper/SKILL.md\|transcript-sweeper]]). |
