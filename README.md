# Library Management System
A web-based library management system has been developed employing SQLite as the database,<br>
Flask for the backend framework, and Vue.js with Sass for the frontend user interface.<br>

A preview of the project can be accessed at [Screen Dump](frontend/docs/Webapp-libSys.pdf)

**Images:**

* Images used in this project have been sourced from Google.com search results.
* We make no claim to ownership of these images. Copyright remains with the original creators.
* Images are used for educational purposes only.
* We have made reasonable efforts to identify and attribute image sources where possible. However, due to the nature of web search, accurate attribution may not always be feasible.
* If you are a copyright holder and believe your work is being used without permission, or without proper attribution, please [See Contact Details Details below](#Contact Details) section with details and we will promptly address the issue.
* Use of these images does not imply endorsement by the copyright holders.
* Images may be subject to copyright restrictions. Users are responsible for ensuring their own compliance with copyright law.
* We do not guarantee the accuracy, suitability, or legality of any image found via Google.com.

**General:**

* This project is provided "as is" without warranty of any kind, express or implied.
* The project creators shall not be liable for any direct, indirect, incidental, consequential, or punitive damages arising out of your access to or use of this project.
* Links to external resources are provided for convenience and informational purposes only. We do not endorse or take responsibility for the content or privacy practices of these resources.
* Please review our Privacy Policy [Link to Privacy Policy] for information on how we handle personal data.
* For any questions regarding these disclaimers, please vitit the [See Contact Details Details below](#Contact Details)

## Tech Stack

| Layer           | Technology                              | Version  |
|-----------------|-----------------------------------------|----------|
| Frontend        | Vue 3                                   | ^3.5.13  |
| Routing         | Vue Router                              | ^4.5.0   |
| State           | Pinia                                   | ^3.0.1   |
| HTTP Client     | Axios                                   | ^1.3.6   |
| UI              | Bootstrap / Bootstrap Icons             | ^5.3.3   |
| Styling         | SASS                                    | —        |
| Build Tool      | Vite                                    | ^6.1.0   |
| Backend         | Flask                                   | 3.1.3    |
| ORM             | Flask-SQLAlchemy                        | 3.1.1    |
| Database        | SQLite                                  | —        |
| Session         | Flask-Session                           | 0.8.0    |
| Validation      | Pydantic                                | 2.12.5   |
| Testing         | pytest                                  | 9.0.2    |

---

## Architecture

The system is split into two independently running processes:

```
webapp-LibSys-vupy/
├── backend/        # Flask REST API and backend documentation
├── docs/           # Repository-level architecture documents and diagrams
└── frontend/       # Vue 3 SPA, assets, and frontend documentation
```

For a full breakdown see [docs/architecture.md](docs/architecture.md), [backend/docs/architecture.md](backend/docs/architecture.md), and [frontend/docs/architecture.md](frontend/docs/architecture.md).

## Repository Structure

```text
webapp-LibSys-vupy/
├── README.md
├── backend/
│   ├── app.py
│   ├── core_files/
│   ├── docs/
│   │   ├── README.md
│   │   ├── architecture.md
│   │   └── diagrams/
│   ├── lib/
│   │   ├── config/
│   │   ├── endpoints/
│   │   ├── modal/
│   │   ├── SQL Data/
│   │   └── utils/
│   ├── requirements.in
│   └── requirements.txt
├── docs/
│   ├── architecture.md
│   └── diagrams/
└── frontend/
	├── docs/
	│   ├── architecture.md
	│   ├── diagrams/
	│   └── Webapp-libSys.pdf
	├── public/
	├── src/
	│   ├── assets/
	│   ├── components/
	│   ├── router/
	│   └── stores/
	├── index.html
	├── package.json
	└── vite.config.js
```

---

## Important Documents

| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Repository-level architecture covering frontend, backend, and persistence |
| [frontend/docs/architecture.md](frontend/docs/architecture.md) | Frontend runtime structure, folders, and data flow |
| [frontend/README.md](frontend/README.md) | Frontend setup, scripts, configuration, and dependencies |
| [backend/docs/README.md](backend/docs/README.md) | Backend documentation index and structure overview |
| [backend/docs/architecture.md](backend/docs/architecture.md) | Backend runtime architecture and service breakdown |
| [backend/docs/diagrams/backend-runtime-architecture.md](backend/docs/diagrams/backend-runtime-architecture.md) | Backend runtime diagram |
| [frontend/docs/diagrams/frontend-runtime-architecture.md](frontend/docs/diagrams/frontend-runtime-architecture.md) | Frontend runtime diagram |
| [docs/diagrams/system-architecture.md](docs/diagrams/system-architecture.md) | End-to-end system architecture diagram |
| [backend/docs/diagrams/book-erdiagram.md](backend/docs/diagrams/book-erdiagram.md) | Entity-relationship diagram for the library domain |
| [backend/docs/diagrams/sequencediagram.md](backend/docs/diagrams/sequencediagram.md) | Sequence diagram for library interactions |
| [backend/docs/diagrams/statediagram.md](backend/docs/diagrams/statediagram.md) | State diagram for core lending decisions |

---

## Installation
1. Clone the repository:
```sh
#   Using HTTPS
git clone https://github.com/krigjo25/webapp-LibSys-vupy.git

#   Using SSH
git clone git@github.com:krigjo25/webapp-LibSys-vupy.git

#   Using Github CLI
gh repo clone krigjo25/webapp-LibSys-vupy
```

2. Navigate to the project directory
```sh
cd webapp-LibSys-vupy
```

3. Install backend dependencies
```sh
cd backend
pip install -r requirements.txt
```

4. Install frontend dependencies
```sh
cd ../frontend
npm install
npm run dev
```

5. Run the server
```sh
cd ../backend
flask run --debug
```

## Credits

This project was initialized using the [testdriven](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)'s tutorial.

##  Contact Details
* For prompt assistance, email is the preferred method of communication.
[ Send a mail](mailto:krigjo25@gmail.com)

Images 
Sincerely,
@krigjo25
