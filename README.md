# Library Management System
A web-based library management system developed using **Python (Flask)** for the backend and **Vue.js (TypeScript)** for the frontend.

A preview of the project can be accessed at [Screen Dump](frontend/docs/Webapp-libSys.pdf)

## Tech Stack

| Layer           | Technology                              | Version  |
|-----------------|-----------------------------------------|----------|
| **Frontend**    | Vue 3 (TypeScript)                      | ^3.5.13  |
| Routing         | Vue Router                              | ^4.5.0   |
| State           | Pinia                                   | ^3.0.1   |
| HTTP Client     | Axios                                   | ^1.3.6   |
| UI              | Bootstrap / Bootstrap Icons             | ^5.3.3   |
| Styling         | SASS (Vite-integrated)                  | —        |
| Build Tool      | Vite                                    | ^6.1.0   |
| **Backend**     | Flask                                   | 3.1.3    |
| ORM             | Flask-SQLAlchemy                        | 3.1.1    |
| Database        | SQLite                                  | —        |
| Validation      | Pydantic                                | 2.12.5   |
| **Testing**     | pytest / Vitest                         | 9.0.2 / 4.1.5 |
| Coverage        | pytest-cov / @vitest/coverage-v8        | 7.1.0 / 4.1.5 |

---

## Repository Structure

```text
webapp-LibSys-vupy/
├── README.md
├── backend/            # Flask API & SQLAlchemy Models
├── docs/               # System-level documentation & diagrams
├── frontend/           # Vue 3 SPA (TypeScript)
└── tests/              # Backend test suite
```

---

## Important Documents
| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Repository-level architecture covering frontend, backend, and persistence |
| [frontend/docs/architecture.md](frontend/docs/architecture.md) | Frontend runtime structure, folders, and data flow |
| [backend/docs/architecture.md](backend/docs/architecture.md) | Backend runtime architecture and service breakdown |
| [backend/docs/backend-diagrams.drawio](backend/docs/backend-diagrams.drawio) | Backend architecture and ER diagrams |
| [frontend/docs/frontend-runtime-architecture.drawio](frontend/docs/frontend-runtime-architecture.drawio) | Frontend runtime diagram |
| [docs/diagrams/system-overview.drawio](docs/diagrams/system-overview.drawio) | End-to-end system overview |
| [backend/docs/diagrams/sequencediagram.md](backend/docs/diagrams/sequencediagram.md) | Sequence diagram for library interactions |
| [backend/docs/diagrams/statediagram.md](backend/docs/diagrams/statediagram.md) | State diagram for core lending decisions |

---

## Installation

### Prerequisites
- Python 3.10+
- Node.js 18+

### 1. Clone the repository
```sh
git clone https://github.com/krigjo25/webapp-LibSys-vupy.git
cd webapp-LibSys-vupy
```

### 2. Backend Setup
We recommend using a virtual environment.
```sh
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend Setup
```sh
cd ../frontend
npm install
```

---

## Running the Application

### Start Backend
```sh
cd backend
source .venv/bin/activate
flask run --debug
```

### Start Frontend
```sh
cd frontend
npm run dev
```

---

## Testing & Coverage

### Backend
```sh
cd backend
source .venv/bin/activate
PYTHONPATH=. pytest
```
Coverage reports are generated in `backend/htmlcov/`.

### Frontend
```sh
cd frontend
npm run test      # Run tests
npm run coverage  # Run tests with coverage reporting
```
Coverage reports are generated in `frontend/coverage/`.

---

## Credits
This project was initialized using the [testdriven](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)'s tutorial.

## Contact Details
[Send a mail](mailto:krigjo25@gmail.com)

Sincerely,
@krigjo25
