# Backend Architecture
The backend is a Flask application that exposes a small book-management API, initializes its own SQLAlchemy data model, and keeps older SQL-based library assets alongside the active runtime code.

- [backend/docs/backend-diagrams.drawio](backend-diagrams.drawio) (Architecture Diagrams)

## Runtime Flow
1. The application starts in `app.py`, imports the shared Flask app, SQLAlchemy instance, and logger from `core_files`, then creates database tables inside an application context.
2. `BookManager` from `lib/endpoints/book_resource.py` is registered as the main HTTP resource for `/` and `/<BID>`.
3. Request handling is centered on a single `MethodView` that supports `GET`, `POST`, `PUT`, and `DELETE` for book records.
4. Data is validated using **Pydantic** schemas before being persisted through the `Book` SQLAlchemy model.
5. Persistent data is stored through the `Book` SQLAlchemy model in `lib/modal/db_init.py`, using the configured SQLite database during development.
6. Sessions are backed by Flask-Session using filesystem storage, while CORS and environment-driven settings are loaded during app boot.

## Main Layers

### Entry and Composition
- `app.py` is the executable entrypoint.
- `core_files/__init__.py` wires together Flask, SQLAlchemy, Flask-Session, dotenv loading, CORS, and logging.
- `lib/config/env_config.py` provides type-safe configuration via Pydantic settings.
- `lib/config/log_config.py` defines logger wrappers used across the backend.

### API Layer
- `lib/endpoints/book_resource.py` contains `BookManager`, the primary API resource.
- `lib/modal/schemas.py` defines Pydantic models for validation and serialization.
- The resource handles list, create, update, and delete operations for books.
- Response formatting and request logging are implemented directly inside the view class.

### Data Layer
- `lib/modal/db_init.py` defines the active `Book` ORM model.
- `db.create_all()` is called during startup, so schema creation is application-driven for the active Flask path.
- The development configuration points to `sqlite:///test.db`.

### Testing
- `tests/test_basic.py` provides baseline unit tests.
- `pytest-cov` is used to generate coverage reports (`htmlcov/`).