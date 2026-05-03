# Frontend Architecture
Vue 3 single-page application built with **TypeScript** and bundled by Vite.

## System View
- [frontend/docs/diagrams/frontend-high-level.drawio](diagrams/frontend-high-level.drawio) (High-level Overview)
- [frontend/docs/frontend-runtime-architecture.drawio](frontend-runtime-architecture.drawio) (Detailed Architecture)

## Directory Structure
```
frontend/
├── index.html              # HTML shell — contains the #app mount point
├── vite.config.js          # Vite config: Vue/JSX, Vitest, and coverage settings
├── tsconfig.json           # TypeScript configuration
├── eslint.config.js        # ESLint rules
├── package.json            # Dependencies and scripts (test, coverage, dev)
└── src/
    ├── main.ts             # Entry point: initializes app, Pinia, Router, and SASS
    ├── App.vue             # Root component
    ├── env.d.ts            # Type definitions for Vue files
    ├── types/
    │   └── index.ts        # Central interfaces (Book, ActionButtonData, etc.)
    ├── assets/
    │   ├── img/            # Static image assets
    │   ├── js/             # (Migrated to TS)
    │   │   ├── apiService.ts   # Axios GET — fetches books; exports reactive state
    │   │   └── bookCrud.ts     # Axios POST/PUT/DELETE helpers
    │   └── sass/           # SASS source files (compiled by Vite)
    │       ├── index.sass      # Master import file
    │       └── ...             # SASS partials
    ├── components/         # Vue components (lang="ts")
    │   ├── __tests__/      # Vitest unit tests
    │   └── ...
    ├── router/
    │   └── index.ts        # Vue Router configuration
    └── stores/
        └── formStore.ts    # Pinia store for shared book data
```

---

## Technical Stack
- **Language:** TypeScript
- **Styling:** SASS (compiled on-the-fly by Vite via `sass-embedded`)
- **State:** Pinia (TypeScript enabled)
- **Testing:** Vitest with `@vitest/coverage-v8`
- **Validation:** Type-safe components via interfaces in `src/types/`
