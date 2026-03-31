# Frontend — webapp-LibSys-vupy
Vue 3 single-page application for the library management system, bundled with Vite.

---

## Table of Contents
- [Frontend — webapp-LibSys-vupy](#frontend--webapp-libsys-vupy)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Available Scripts](#available-scripts)
  - [Project Structure](#project-structure)
  - [Configuration](#configuration)
  - [Dependencies](#dependencies)
    - [Runtime](#runtime)
    - [Development](#development)

---

## Overview
The frontend is a Vue 3 SPA that communicates with the Flask backend REST API over port `5000`.

| Technology             | Role                            |
|------------------------|---------------------------------|
| Vue 3                  | Component framework             |
| Vue Router 4           | Client-side routing             |
| Pinia                  | State management                |
| Axios                  | HTTP client                     |
| Bootstrap 5            | UI component library            |
| Bootstrap Icons        | Icon set                        |
| SASS                   | Stylesheet authoring            |
| Vite                   | Build tool and dev server       |

---

## Prerequisites
- Node.js 18 or later
- npm 9 or later
- Flask backend running on `http://localhost:5000`

---

## Getting Started
Install dependencies:

```sh
npm install
```

Start the development server:

```sh
npm run dev
```

The app will be available at `http://localhost:5173` by default.

---

## Available Scripts
| Command            | Description                                        |
|--------------------|----------------------------------------------------|
| `npm run dev`      | Start Vite dev server with hot-reload              |
| `npm run build`    | Compile and minify for production output           |
| `npm run serve`    | Serve the production build locally for inspection  |
| `npm run lint`     | Run ESLint with auto-fix across all JS/Vue files   |
| `npm run format`   | Run Prettier across all files in `src/`            |

---

## Project Structure
See [architecture.md](architecture.md) for detailed descriptions of every file and folder.

---

## Configuration
| File               | Purpose                                                   |
|--------------------|-----------------------------------------------------------|
| `vite.config.js`   | Vue, JSX, and DevTools plugins; `@` path alias to `src/`  |
| `jsconfig.json`    | Editor path alias matching Vite (`@` maps to `./src/`)    |
| `eslint.config.js` | Linting rules for `.js`, `.mjs`, `.jsx`, and `.vue` files |
| `.prettierrc.json` | Prettier formatting rules                                 |

---

## Dependencies

### Runtime
| Package          | Version   | Role                    |
|------------------|-----------|-------------------------|
| vue              | ^3.5.13   | UI framework            |
| vue-router       | ^4.5.0    | Client-side routing     |
| pinia            | ^3.0.1    | State management        |
| axios            | ^1.3.6    | HTTP client             |
| bootstrap        | ^5.3.3    | CSS component library   |
| bootstrap-icons  | ^1.11.3   | Icon set                |

### Development
| Package                     | Version   | Role                        |
|-----------------------------|-----------|-----------------------------|
| vite                        | ^6.1.0    | Build tool and dev server   |
| @vitejs/plugin-vue          | ^5.2.1    | Vite Vue 3 plugin           |
| @vitejs/plugin-vue-jsx      | ^4.1.1    | JSX support                 |
| vite-plugin-vue-devtools    | ^7.7.2    | Vue DevTools integration    |
| eslint                      | ^9.20.1   | Linter                      |
| eslint-plugin-vue           | ^9.32.0   | Vue-specific lint rules     |
| prettier                    | ^3.5.1    | Code formatter              |
