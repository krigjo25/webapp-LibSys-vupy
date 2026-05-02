# Backend Architecture
The backend is a Flask application that exposes a small book-management API, initializes its own SQLAlchemy data model, and keeps older SQL-based library assets alongside the active runtime code.

Use Markdown preview for this document. If you want to open only the diagram in a Mermaid renderer, use [docs/diagrams/backend-runtime-architecture.md](docs/diagrams/backend-runtime-architecture.md).

## Runtime Flow
1. The application starts in `app.py`, imports the shared Flask app, SQLAlchemy instance, and logger from `core_files`, then creates database tables inside an application context.
2. `BookManager` from `lib/endpoints/book_resource.py` is registered as the main HTTP resource for `/` and `/<BID>`.
3. Request handling is centered on a single `MethodView` that supports `GET`, `POST`, `PUT`, and `DELETE` for book records.
4. Persistent data is stored through the `Book` SQLAlchemy model in `lib/modal/db_init.py`, using the configured SQLite database during development.
5. Sessions are backed by Flask-Session using filesystem storage, while CORS and environment-driven settings are loaded during app boot.

## Main Layers

### Entry and Composition
- `app.py` is the executable entrypoint.
- `core_files/__init__.py` wires together Flask, SQLAlchemy, Flask-Session, dotenv loading, CORS, and logging.
- `lib/config/env_config.py` provides default and development configuration classes.
- `lib/config/log_config.py` defines logger wrappers used across the backend.

### API Layer
- `lib/endpoints/book_resource.py` contains `BookManager`, the primary API resource.
- The resource handles list, create, update, and delete operations for books.
- Response formatting and request logging are implemented directly inside the view class.

### Data Layer
- `lib/modal/db_init.py` defines the active `Book` ORM model.
- `db.create_all()` is called during startup, so schema creation is application-driven for the active Flask path.
- The development configuration points to `sqlite:///test.db`.

### Utilities and Auxiliary Modules
- `lib/utils/maintance.py` contains helper logic for destructive book operations such as purge.
- `lib/utils/database_connection.py`, `lib/utils/custom_functions.py`, and `lib/utils/send_mail.py` support MariaDB-oriented workflows and email automation.
- These modules appear adjacent to, but not fully integrated with, the active Flask request path.

### SQL Asset Repository
- `lib/SQL Data/` stores SQL scripts for `library`, `libraryArchive`, and `bookOrms` schemas.
- These files include DDL, procedures, views, triggers, seed data, and scheduled events.
- The SQL asset folder documents a broader library-management database design than the currently active Flask `Book` API exposes.

## Directory Map
```text
backend/
├── app.py
├── core_files/
│   └── __init__.py
├── docs/
│   ├── architecture.md
│   └── diagrams/
├── lib/
│   ├── config/
│   ├── endpoints/
│   ├── modal/
│   ├── SQL Data/
│   └── utils/
├── requirements.in
└── requirements.txt
```

## Architectural Notes
- The active runtime is centered on one resource and one ORM model, which keeps the current API surface small.
- The repository also contains a larger historical SQL design that can be treated as reference material or a future expansion path.
- Startup currently mixes bootstrapping, schema creation, route registration, and logging in `app.py`, which is workable for a small service but tightens coupling as the backend grows.