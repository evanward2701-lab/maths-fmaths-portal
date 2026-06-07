# AS1QuadraticsMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1QuadraticsMermaid-003 |
| asset_type | Mermaid decision tree |
| lesson | AS1 Quadratics |
| related lesson section | Core Theory Part H – The Discriminant |
| source | CCEA AS1-AF-LO004; lesson PDF discriminant section; teacher transcript discriminant work |
| purpose | Connect `b^2-4ac` to root type and graph behaviour. |

```mermaid
flowchart TD
    A["Start: ax^2 + bx + c = 0"] --> B["Identify a, b, and c carefully"]
    B --> C["Compute discriminant D = b^2 - 4ac"]
    C --> D{"What is the sign of D?"}
    D -- "D > 0" --> E["Two distinct real roots"]
    E --> F["Graph crosses the x-axis twice"]
    F --> G["If solving, use factorisation or quadratic formula"]
    D -- "D = 0" --> H["One repeated real root"]
    H --> I["Graph touches the x-axis at the turning point"]
    I --> J["Use b^2 - 4ac = 0 for equal-root parameter questions"]
    D -- "D < 0" --> K["No real roots"]
    K --> L["Graph does not meet the x-axis"]
    L --> M["State no real roots, not no roots"]
    C --> N{"Parameter question?"}
    N -- "Yes" --> O["Translate root condition into an equation or inequality"]
    O --> P["Solve carefully, flipping inequality signs when dividing by a negative"]
    P --> Q["Apply any restrictions, e.g. p positive"]
    N -- "No" --> R["State root type clearly"]
```
