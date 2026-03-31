# Backend Documentation
This folder documents the Flask backend used by the library web application. The active service exposes book CRUD operations over HTTP, uses SQLAlchemy for the runtime data model, and keeps a separate collection of SQL assets for a broader library-management schema.

## Purpose
The backend is responsible for:

- bootstrapping the Flask application
- loading environment and logging configuration
- exposing book management endpoints
- persisting active book data through SQLAlchemy
- keeping supporting SQL scripts and legacy database assets in the repository

## Backend Structure

```text
backend/
├── app.py                    # Application entrypoint and route registration
├── core_files/
│   └── __init__.py           # Flask app, SQLAlchemy, session, CORS, dotenv, logger setup
├── docs/
│   ├── README.md             # This file
│   ├── architecture.md       # Backend architecture overview and system diagram
│   └── diagrams/             # Existing Mermaid sequence, state, and ER diagrams
├── lib/
│   ├── config/               # Environment and logging configuration
│   ├── endpoints/            # HTTP resource classes
│   ├── modal/                # SQLAlchemy models and seed data
│   ├── SQL Data/             # MariaDB DDL, procedures, views, triggers, events, seed data
│   └── utils/                # Helper functions, mail scripts, and DB utilities
├── requirements.in           # Source dependency list
└── requirements.txt          # Locked dependency set
```

## Core Components

### Application Boot

- `app.py` creates tables, registers routes, and applies cache-control headers after requests.
- `core_files/__init__.py` centralizes the Flask app instance and shared extensions.

### HTTP API

- `lib/endpoints/book_resource.py` contains the main `BookMananger` `MethodView`.
- The root route `/` supports `GET` and `POST`.
- The parameterized route `/<BID>` supports `PUT` and `DELETE`.

### Data Model

- `lib/modal/db_init.py` defines the active `Book` model.
- The development environment uses SQLite through Flask-SQLAlchemy.

### Supporting Utilities

- `lib/utils/maintance.py` contains deletion helpers used by the API.
- `lib/utils/database_connection.py` and related mail utilities reflect MariaDB-based workflows that sit outside the main Flask request path.

### SQL Assets

- `lib/SQL Data/` stores database scripts for `library`, `bookOrms`, and `libraryArchive`.
- These scripts describe a richer schema with procedures, triggers, views, archive tables, and events.
- They should be read as repository assets rather than the complete source of truth for the active Flask runtime.

## Existing Documentation

- `docs/architecture.md` provides the current backend architecture and component relationships.
- `docs/diagrams/book-erdiagram.md` describes the database relationships in Mermaid.
- `docs/diagrams/sequencediagram.md` and `docs/diagrams/statediagram.md` capture behavioral flows.

## Dependencies

The backend currently depends on:

- Flask
- Flask-Session
- Flask-SQLAlchemy
- python-dotenv
- simplified-logging
- pytest
- Pydantic

## Recommended Reading Order

1. Start with `docs/architecture.md` for the high-level structure.
2. Review `app.py` and `core_files/__init__.py` for application composition.
3. Inspect `lib/endpoints/book_resource.py` and `lib/modal/db_init.py` for the active request/data path.
4. Use the files in `docs/diagrams/` and `lib/SQL Data/` when you need broader domain context.