---
name: show-me
description: Use when writing an implementation_plan.md in the IDE or when prompted to do so by the user to visually explain proposed code or structural changes prior to making them, or when asked to explain logic, control flow, architecture, UI hierarchy, or diffs visually. Do NOT use when answering trivial single-line questions that require no structural or code explanation.
aliases:
  - show-me
up: "[[AI-OS/Maps/skill-map.md|skill-map]]"
related:
  - "[[Home.md|Home]]"
  - "[[AI-OS/Skills/note-architect/SKILL.md|note-architect]]"
sources:
  - https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md
created: 2026-10-20
collections:
  - ai-os
  - skills
tags:
  - read-only
  - skill
---
# 🤖 Skill: Visual Code & Plan Explanation (`show-me`)

## Objective & Trigger Boundaries
Help the user understand the current topic or proposed code changes visually with concise diagrams, code-shape sketches, Mermaid flows, shape-matched diffs, and focused HTML artifacts—eliminating walls of conversational prose.
- **Use when:** Writing an `implementation_plan.md` in the IDE to explain proposed code or structural changes prior to making them, or when explaining logic, algorithms, runtime control flow, UI hierarchy, file layout, or architecture visually.
- **Do NOT use when:** Answering quick single-sentence questions with no code or structural explanation needed, or running automated maintenance workflows ([[AI-OS/Skills/transcript-sweeper/SKILL.md|transcript-sweeper]], [[AI-OS/Skills/vault-janitor/SKILL.md|vault-janitor]]).

## Execution Protocol

### 1. Core Visual Principle
Skip the preamble and keep prose brief. Pick the **smallest view** that makes the key point clear.

### 2. Static Visual Formats (When Explaining Existing Shape or New Architecture)

1. **Show logic or an algorithm as pseudocode:**
   ```text
   on(save)
     if content is unchanged
       return cached result
     write new content
     return fresh result
   ```

2. **Show runtime control flow as a call tree:**
   ```text
   submitForm
     createSession
       persistPrompt
       launchAgent
       navigateToSession
   ```

3. **Show UI structure as a component tree, including state and module boundaries that matter:**
   ```text
   <SessionPage> (apps/example/src/routes/session.tsx)
     useSessionEvents()
     <SessionToolbar>
       <RunSkillButton> (packages/ui)
   ```

4. **Show file responsibility or a broad refactor as a shallow file tree:**
   ```text
   src/
   ├── commands/      # parses user actions
   ├── sessions/      # owns session state
   └── transport/     # sends API requests
   ```

5. **Show component interaction, control flow, or data flow with Mermaid:**
   ```mermaid
   sequenceDiagram
       participant User
       participant UI
       participant Daemon
       User->>UI: choose command
       UI->>Daemon: send expanded prompt
       Daemon-->>UI: stream result
   ```

### 3. Shape-Matched Diffs (Mandatory When Explaining Proposed Changes in `implementation_plan.md`)
Use `diff` when the point is what changes and the surrounding shape already exists. Match the diff shape to the topic:

1. **For a component change:**
   ```diff
   <SessionPage>
     useSessionEvents()
     <SessionToolbar>
   +   <RunSkillButton />
     <SessionTimeline>
   +   <SkillResultCard />
   ```

2. **For a file-layout change:**
   ```diff
   src/
   ├── commands/
   +   └── show-me.ts   # expands the slash command
   ├── sessions/
   -   └── transport.ts
   +   └── transport/
   +       ├── client.ts
   +       └── stream.ts
   ```

3. **For a call-tree or call-stack change:**
   ```diff
   submitForm
     createSession
       persistPrompt
   +   expandSkillMention
       launchAgent
   -   navigateToSession
   +   navigateToSession
   +     subscribeToEvents
   ```

4. **For a state or control-flow change:**
   ```diff
   on(save)
   - write content
   + if content is unchanged
   +   return cached result
   + write new content
   + invalidate cache
   + return fresh result
   ```

### 4. Focused HTML Artifacts
When a visual layout mockup or interactive widget is the clearest way to demonstrate a UI or structural concept, generate a compact, self-contained HTML artifact rather than describing the layout in long paragraphs.

## Subagent & Parallel Delegation Guidance
- **Execute in Main Thread:** Visual explanations and `implementation_plan.md` change sketches are authored directly in the main agent thread as part of user communication and plan approval.

## Failure Recovery & Fallback Protocol
- **Mermaid Syntax Pitfalls:** Quote node labels containing parentheses, brackets, or special characters (e.g., `id["Label (Extra Info)"]`) and avoid HTML tags inside Mermaid node labels so IDE Markdown renderers never fail to parse the diagram.
- **Overly Large Diffs:** If a raw line-by-line code diff spans dozens of boilerplate lines, collapse it into a **pseudocode diff**, **call-tree diff**, or **file-tree diff** so the structural intent remains immediately scannable.

## Verification & Self-Check Gate
Before presenting an `implementation_plan.md` or visual explanation to the user, verify:
1. Preambles and redundant prose paragraphs are stripped; the visual sketch leads the explanation.
2. Every proposed code or structural modification in `implementation_plan.md` uses the smallest effective visual representation (shape-matched `diff`, pseudocode, call tree, component tree, shallow file tree, or Mermaid diagram).

## Second Brain Continuity & Dependency Handoff
- Whenever `implementation_plan.md` is generated for code or vault changes, apply `show-me` visual views prior to asking for user approval per [[Home.md|Home]].
