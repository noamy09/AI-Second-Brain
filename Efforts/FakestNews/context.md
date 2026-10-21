---
up: "[[AI-OS/Maps/vault-map.md|vault-map]]"
created: 2026-10-17
related:
  - "[[Efforts/FakestNews/changelog.md|changelog]]"
  - "[[Efforts/FakestNews/decisions.md|decisions]]"
collections:
  - efforts
ide: antigravity
repo_path: "C:/Users/noamy/OneDrive/Desktop/לימודים/תואר/שנה ב/סמסטר ג/אפליקציות אינטרנטיות/Final Task/FakestNews"
log_path: "C:/Users/noamy/.gemini/antigravity/brain/"
status: active
tags:
  - write
  - project
---
# 🤖 Project: FakestNews

## 1. High-Level Context & Objective
- **Goal:** News publishing web platform supporting role-based workflows for Writers, Editors, and Administrators (drafting, editorial reviews, revisions, publishing, and analytics).
- **Tech Stack:** Node.js, Express, MongoDB (Mongoose), EJS templates, CSS/Vanilla JS.
- **Repository:** `C:/Users/noamy/OneDrive/Desktop/לימודים/תואר/שנה ב/סמסטר ג/אפליקציות אינטרנטיות/Final Task/FakestNews`

## 2. Low-Level Architecture & Key Components
- **Entry Points:** `server.js` (Express app server), `routes/router.js` (modular route registry).
- **Core Modules / Services:**
  - `controllers/`: Route controllers (`articleController.js`, `writersHubController.js`, `editorController.js`, `adminHubController.js`, `authController.js`, etc.).
  - `models/`: Mongoose schemas (`Article.js`, `User.js`, `Note.js`, `SecurityLog.js`, etc.).
  - `middlewares/`: Role-based access control, security logger, and session auth.
  - `views/`: EJS frontend templates with partials (`writersHub.ejs`, `editor.ejs`, `adminHub.ejs`, etc.).
  - `public/`: Static client scripts and stylesheets (`writersHub.js`, `writersHubEdit.js`, `writersHub.css`, etc.).
- **Data Flow & Storage:** Express REST endpoints interacting with MongoDB via Mongoose models; session authentication via `express-session` and `connect-mongo`.

## 3. Active Roadmap & Next Steps
- [x] Initialize project structure and `.brain` junction
- [x] Remove view counts for non-published articles in Writer's Hub

## 4. Linked Vault Memories & Domain References
- *(No active memory notes matched yet)*
