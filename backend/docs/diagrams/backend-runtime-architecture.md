```mermaid
---
title: Backend Runtime Architecture
---
block-beta
    columns 1

    block:clients:1
        columns 1
        frontend["fa:fa-desktop Frontend SPA"]
    end

    downArrow1:1["fa:fa-arrow-down"]


    block:runtime:1
        columns 4
        config["fa:fa-cog Config"]
        app["fa:fa-rocket Flask App"]
        endpoint["fa:fa-link BookManager"]
        utils["fa:fa-wrench Utils"]
    end

    downArrow2:1["fa:fa-arrow-down"]
    block:storage_assets:1
        columns 4
        model["fa:fa-table SQLAlchemy"]
        sqlite[("fa:fa-database SQLite")]
        session[("fa:fa-save Session")]
        scripts["fa:fa-file-code SQL Scripts"]
    end

    %% Koblinger (logiske piler)
    config --> app
    app --> endpoint
    endpoint --> model
    model --> sqlite
    app --> session
    utils --> endpoint
    utils --> scripts

    %% Styling (GitHub-vennlig)
    style clients fill:#f9f,stroke:#333,stroke-width:2px
    style runtime fill:#bbf,stroke:#333,stroke-width:2px
    style storage_assets fill:#dfd,stroke:#333,stroke-width:2px
```