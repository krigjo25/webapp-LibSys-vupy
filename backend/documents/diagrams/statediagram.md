```mermaid
---
title : Decision-making Process
---
stateDiagram-v2
    [*] --> System: Request to Lend a book
    state System {
        [*] --> system: Receive Request
        system --> LENDINGS(table): Does the user have any outstanding fines?
        LENDINGS(table) --> NO --> system: No outstanding fines
        LENDINGS(table) --> YES --> system: Outstanding fines exist
    }
```