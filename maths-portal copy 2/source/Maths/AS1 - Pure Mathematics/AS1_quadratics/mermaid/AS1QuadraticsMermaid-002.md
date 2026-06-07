# AS1QuadraticsMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1QuadraticsMermaid-002 |
| asset_type | Mermaid flowchart |
| lesson | AS1 Quadratics |
| related lesson section | Core Theory Part F – Sketching Quadratic Graphs |
| source | CCEA AS1-AF-LO003, AS1-AF-LO012, AS1-AF-LO014; lesson PDF quadratic graphs section; teacher transcript video 7 |
| purpose | Provide a graph-sketching checklist for a quadratic such as `y=x^2+4x-5`. |

```mermaid
flowchart TD
    A["Start: sketch y = ax^2 + bx + c"] --> B["Draw x-axis and y-axis"]
    B --> C["Do not use a full scale unless required"]
    C --> D{"Is a positive?"}
    D -- "Yes" --> E["Shape: U-shaped parabola with a minimum"]
    D -- "No" --> F["Shape: upside-down parabola with a maximum"]
    E --> G["Find x-intercepts by setting y = 0"]
    F --> G
    G --> H{"Can the quadratic be solved?"}
    H -- "Yes" --> I["Label roots as points: (r1, 0), (r2, 0)"]
    H -- "No real roots" --> J["Show graph not crossing the x-axis"]
    I --> K["Find y-intercept by setting x = 0"]
    J --> K
    K --> L["Complete the square"]
    L --> M["Read turning point from vertex form"]
    M --> N["Draw line of symmetry through turning point"]
    N --> O["Label all key coordinates"]
    O --> P["Final sketch: correct shape, intercepts, turning point, symmetry"]
```
