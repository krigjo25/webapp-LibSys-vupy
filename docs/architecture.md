# Project Architecture
This document describes how the frontend and backend are composed at the repository level.
- [docs/diagrams/system-overview.drawio](diagrams/system-overview.drawio) (High-level Overview)

## Scope
- The frontend is a Vite-powered Vue single-page application (TypeScript).
- The backend is a Flask service exposing book-management endpoints.
- The active runtime persists book data through SQLAlchemy and SQLite.
- Additional SQL scripts remain in the repository as supporting or legacy assets.
## Related Documents
- [backend/docs/architecture.md](../backend/docs/architecture.md)
- [frontend/docs/architecture.md](../frontend/docs/architecture.md)
- [backend/docs/backend-diagrams.drawio](../backend/docs/backend-diagrams.drawio)
- [frontend/docs/frontend-runtime-architecture.drawio](../frontend/docs/frontend-runtime-architecture.drawio)
