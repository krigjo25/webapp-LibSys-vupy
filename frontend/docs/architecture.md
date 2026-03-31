# Frontend Architecture
Vue 3 single-page application bundled by Vite.

---

## Directory Structure
```
frontend/
├── index.html              # HTML shell — contains the #app mount point
├── vite.config.js          # Vite bundler: Vue/JSX/DevTools plugins, @ path alias
├── jsconfig.json           # JS path alias (@ → ./src/) for editor tooling
├── eslint.config.js        # ESLint rules for .js, .mjs, .jsx, and .vue files
├── package.json            # Dependencies and npm scripts
├── public/
│   └── favicon.ico         # Static favicon served as-is
└── src/
    ├── main.js             # Entry point: creates app, installs Pinia and Router, mounts to #app
    ├── App.vue             # Root component — renders AppHeader and RouterView
    ├── assets/
    │   ├── base.css        # Compiled base CSS (do not edit directly)
    │   ├── index.css       # Compiled output of SASS build
    │   ├── img/            # Static image assets
    │   ├── js/
    │   │   ├── apiService.js   # Axios GET — fetches all books; exports reactive data object
    │   │   └── bookCrud.js     # Axios POST/PUT/DELETE — create, update, delete book helpers
    │   └── sass/
    │       ├── index.sass      # Master import file — aggregates all partials
    │       ├── base.sass       # CSS custom properties, fonts, dark mode, element reset
    │       ├── colour.sass     # SASS colour variables (palette, brand colours, overlays)
    │       ├── flexbox.sass    # Utility flex layout classes
    │       ├── form.sass       # Input, textarea, and form layout styles
    │       ├── bookinfo.sass   # Book card, description, and detail section styles
    │       └── btrapicons.sass # Bootstrap Icons colour and size overrides
    ├── components/
    │   ├── Index.vue           # Home page — renders the book grid
    │   ├── Books.vue           # Book card grid; emits book-id on selection
    │   ├── BookDetails.vue     # Full detail view for the book stored in Pinia
    │   ├── BookPanel.vue       # Admin dashboard — book list with CRUD action buttons
    │   ├── UpsertForm.vue      # Shared create/edit form for book records
    │   ├── header_components/
    │   │   ├── AppHeader.vue           # Header shell
    │   │   └── Navigation_route.vue    # Router-link navigation bar
    │   └── misc_components/
    │       ├── ActionButton.vue    # Reusable button with Bootstrap icon and action handler
    │       ├── InputField.vue      # Labelled input/textarea; emits upsert-form on change
    │       └── Navigation.vue      # Row of ActionButton instances for management actions
    ├── router/
    │   └── index.js            # Vue Router 4 — defines the four application routes
    └── stores/
        └── formStore.js        # Pinia store — holds the selected book, shared across views
```

---

## Important Folders

### `src/assets/js/`
The HTTP service layer. `apiService.js` owns the shared reactive `data` object that components bind to; `bookCrud.js` provides the write operations and calls `Response()` to refresh state after each mutation.

### `src/assets/sass/`
All styles are authored in SASS and compiled to `assets/index.css`. Edit partials here, never the compiled output. `index.sass` is the single entry point that imports the rest.

### `src/components/`
Split into two sub-directories:

- **`header_components/`** — layout chrome (header, top nav)
- **`misc_components/`** — generic, reusable UI primitives (`ActionButton`, `InputField`, `Navigation`)

Page-level components (`Index`, `Books`, `BookDetails`, `BookPanel`, `UpsertForm`) live directly in `components/`.

### `src/router/`
Single file (`index.js`) declaring all four routes with lazy-loaded component imports.

| Path           | Component        |
|----------------|------------------|
| `/`            | `Index.vue`      |
| `/BookDetails` | `BookDetails.vue`|
| `/BookPanel`   | `BookPanel.vue`  |
| `/upsertBook`  | `UpsertForm.vue` |

### `src/stores/`
Pinia store (`formStore.js`). Holds the currently selected book in `storedData.data`. Components call `setData(book)` to share a selection and `clearData()` to reset it.
