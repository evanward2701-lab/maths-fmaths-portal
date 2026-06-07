# A22MomentsMermaid-004

## Asset ID

`A22MomentsMermaid-004`

## Source

Rigid Bodies transcript sections 2 and 3.

## Related lesson section

Core Theory 4; Exam Technique Notes.

## Purpose

Choosing where to take moments.

```mermaid
flowchart TD
    A["Need to solve a moments problem"] --> B["Draw all forces first"]
    B --> C["List unknowns"]
    C --> D{"Is there an awkward unknown<br/>reaction or tension?"}
    D -->|Yes| E["Take moments about the point<br/>where that unknown acts"]
    E --> F["Its distance is 0<br/>so its moment disappears"]
    D -->|No| G{"Would resolving forces<br/>give a useful equation first?"}
    G -->|Yes| H["Resolve first"]
    G -->|No| I["Choose the point giving<br/>simplest distances"]
    F --> J["Write clockwise moments<br/>= anticlockwise moments"]
    H --> J
    I --> J
    J --> K["Solve cleanly"]
```
