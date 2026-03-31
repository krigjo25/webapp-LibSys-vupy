# Project Architecture
This document describes how the frontend and backend are composed at the repository level.
Use [docs/diagrams/system-architecture.md](docs/diagrams/system-architecture.md) if you want the standalone diagram file.

## Scope
- The frontend is a Vite-powered Vue single-page application.
- The backend is a Flask service exposing book-management endpoints.
- The active runtime persists book data through SQLAlchemy and SQLite.
- Additional SQL scripts remain in the repository as supporting or legacy assets.
## Related Documents
- [backend/docs/architecture.md](backend/docs/architecture.md)
- [frontend/docs/architecture.md](frontend/docs/architecture.md)
- [backend/docs/diagrams/backend-runtime-architecture.md](backend/docs/diagrams/backend-runtime-architecture.md)
- [frontend/docs/diagrams/frontend-runtime-architecture.md](frontend/docs/diagrams/frontend-runtime-architecture.md)