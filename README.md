# Library Management System
A modern, web-based library management system built with **Python (Flask)** and **Vue 3 (TypeScript)**.

A preview of the project can be accessed at [Screen Dump](frontend/docs/Webapp-libSys.pdf)

## 🚀 Key Features (Modernization)
- **TypeScript Migration:** The entire frontend has been migrated to TypeScript for robust type safety and better developer experience.
- **Comprehensive Testing:** Integrated `pytest` (backend) and `Vitest` (frontend) with automated coverage reporting.
- **Data Validation:** Uses **Pydantic** on the backend and TypeScript interfaces on the frontend for synchronized data contracts.
- **Integrated Styling:** SASS preprocessing is now handled directly by Vite using `sass-embedded`, removing the need for pre-compiled CSS.
- **Architecture Visualization:** System diagrams migrated to `.drawio` for better maintainability and professional visualization.

## 🛠 Tech Stack

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

## 📁 Repository Structure

```text
webapp-LibSys-vupy/
├── README.md
├── backend/
│   ├── tests/          # Pytest suite
│   ├── core_files/     # Flask & DB Initialization
│   └── lib/            # Endpoints, Models (Pydantic/SQLAlchemy), and Utils
├── docs/               # System-level documentation & diagrams
└── frontend/
    ├── src/
    │   ├── types/      # Central TypeScript Interfaces
    │   ├── components/ # Vue components (with __tests__)
    │   └── assets/     # SASS source & images
    └── package.json
```

---

## 📖 Important Documents
| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Repository-level architecture |
| [frontend/docs/architecture.md](frontend/docs/architecture.md) | Frontend runtime structure & data flow |
| [backend/docs/architecture.md](backend/docs/architecture.md) | Backend runtime architecture |
| [backend/docs/backend-diagrams.drawio](backend/docs/backend-diagrams.drawio) | Backend & ER diagrams |
| [frontend/docs/frontend-runtime-architecture.drawio](frontend/docs/frontend-runtime-architecture.drawio) | Frontend runtime diagram |
| [docs/diagrams/system-overview.drawio](docs/diagrams/system-overview.drawio) | End-to-end system overview |

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Node.js 18+

### 1. Clone the repository
```sh
git clone https://github.com/krigjo25/webapp-LibSys-vupy.git
cd webapp-LibSys-vupy
```

### 2. Backend Setup
```sh
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend Setup
```sh
cd ../frontend
npm install
```

---

## 🏃 Running the Application

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

## 🧪 Testing & Coverage

### Backend
```sh
cd backend
source .venv/bin/activate
PYTHONPATH=. pytest
```
Coverage: Check terminal output or open `backend/htmlcov/index.html`.

### Frontend
```sh
cd frontend
npm run test      # Standard tests
npm run coverage  # Tests with coverage (v8)
```
Coverage: Open `frontend/coverage/index.html`.

---

## 📜 Credits
Initialized from [testdriven](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)'s tutorial.

## ✉️ Contact
[Send a mail](mailto:krigjo25@gmail.com)

Sincerely,
@krigjo25
