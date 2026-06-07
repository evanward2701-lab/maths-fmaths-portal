# AS1QuadraticsMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1QuadraticsMermaid-001 |
| asset_type | Mermaid flowchart |
| lesson | AS1 Quadratics |
| related lesson section | Core Theory Part A; Consolidated Exam Technique |
| source | CCEA AS1-AF-LO006; lesson PDF solving quadratics section; teacher transcript video 1 |
| purpose | Help students choose a suitable method for solving a quadratic equation. |

```mermaid
flowchart TD
    A["Start: quadratic equation or disguised quadratic"] --> B{"Can it be written as ax^2 + bx + c = 0?"}
    B -- "Not yet" --> C["Use substitution, e.g. y = sqrt(x), y = x^2, or y = function of x"]
    C --> D["Solve the resulting normal quadratic"]
    D --> E["Convert back to the original variable"]
    E --> F["Check for invalid values, especially after square roots or squaring"]
    B -- "Yes" --> G{"Does the unknown appear only once inside a squared bracket?"}
    G -- "Yes" --> H["Square root both sides"]
    H --> I["Remember the plus/minus"]
    I --> F
    G -- "No" --> J{"Does it factorise cleanly?"}
    J -- "Yes" --> K["Factorise"]
    K --> L["Use zero product rule"]
    L --> F
    J -- "No" --> M{"Does the question require completing the square?"}
    M -- "Yes" --> N["Complete the square, then solve by inverse operations"]
    N --> F
    M -- "No" --> O["Use the quadratic formula"]
    O --> P["Simplify exact surd answers where possible"]
    P --> F
    F --> Q{"Context or domain restrictions?"}
    Q -- "Yes" --> R["Reject impossible values, e.g. negative time or invalid square-root values"]
    Q -- "No" --> S["State final solutions clearly"]
    R --> S
    S --> T["Use calculator solver only as a check unless the question allows it"]
```
