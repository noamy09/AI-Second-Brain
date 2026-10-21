---
up: "[[Efforts/FakestNews/context.md|context]]"
related:
  - "[[Efforts/FakestNews/decisions.md|decisions]]"
created: 2026-10-17
collections:
  - efforts
  - logs
tags:
  - write
  - changelog
---
# 🤖 Project Changelog: FakestNews

## [2026-10-17] — Project Bootstrap & Writer's Hub View Count Visibility
- **IDE / Harness:** antigravity
- **Codebase Changes:**
  - Added `.brain` and `.brain/` to `.gitignore`.
  - Updated `public/js/writersHub.js` to remove view counts from cards that are not published (Drafts, Returned for Revision, and Pending columns).
- **Vault Changes:**
  - Bootstrapped project hub in `Efforts/FakestNews/` (`context.md`, `decisions.md`, `changelog.md`).
  - Linked `<repo_path>\.brain` directory junction to `C:\Users\noamy\Second Brain\Efforts\FakestNews`.
