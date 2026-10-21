---
up: "[[Efforts/FakestNews/context.md|context]]"
related:
  - "[[Efforts/FakestNews/changelog.md|changelog]]"
created: 2026-10-17
collections:
  - efforts
  - architecture
tags:
  - write
  - decisions
---
# 🤖 Architecture & Dependency Decisions: FakestNews

## Dependencies & Libraries
| Package / Service | Version / Tier | Purpose & Justification | Reference / Memory |
| :---------------- | :------------- | :---------------------- | :----------------- |
| `express` | `^5.2.1` | Core web application framework handling routes and HTTP endpoints | None |
| `mongoose` | `^9.9.5` | ODM for MongoDB persistence (articles, users, notes, logs) | None |
| `express-session` | `^1.19.0` | Cookie-based session tracking for authenticated users | None |
| `connect-mongo` | `^5.1.0` | Persistent MongoDB session store for Express | None |
| `bcrypt` | `^5.1.1` | Password hashing for user authentication | None |
| `ejs` | `^6.0.1` | Server-rendered view templates | None |
| `dotenv` | `^17.4.2` | Environment variable management | None |
| `mongodb-memory-server` | `^11.2.0` | In-memory MongoDB testing environment | None |

## Decision Log (ADR)

### [2026-10-17] Writer's Hub View Count Visibility
- **Context:** In the Writer's Hub dashboard, cards in the Drafts, Returned for Revision, and Pending columns displayed view counts (`Views: 0` or inherited published counts from parent articles during revision). Drafts and unpublished submissions are not live and should not display view statistics.
- **Decision:** Restrict view count rendering in `createArticleCard()` to only published articles (`isPublished === true`).
- **Consequences:** Improves UX and prevents misleading view counts on non-published working copies and pending reviews.
- **References & Memories:** None
