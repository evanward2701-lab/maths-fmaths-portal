# AS1QuadraticsMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1QuadraticsMermaid-004 |
| asset_type | Mermaid modelling workflow |
| lesson | AS1 Quadratics |
| related lesson section | Core Theory Part I – Modelling with Quadratics |
| source | Lesson PDF “Why do we care about quadratics?” pages and transcript modelling section |
| purpose | Show how to move from a real-world quadratic model to algebraic answers and contextual interpretation. |

```mermaid
flowchart TD
    A["Start: read the modelling context"] --> B["Identify variables and units"]
    B --> C["Write or use the given quadratic model"]
    C --> D["Record any domain restriction, e.g. t >= 0"]
    D --> E["Interpret constant term by setting input = 0"]
    E --> F{"What is the question asking?"}
    F -- "When object hits ground" --> G["Set height equal to 0"]
    G --> H["Solve the quadratic"]
    H --> I["Reject impossible values, e.g. negative time"]
    F -- "Maximum or minimum" --> J["Complete the square"]
    J --> K["Use squared term >= 0"]
    K --> L["Read maximum or minimum value and when it occurs"]
    F -- "Value at a given input" --> M["Substitute the input"]
    M --> N["Calculate output with units"]
    F -- "Find model from information" --> O{"What information is given?"}
    O -- "Roots" --> P["Use y = a(x - r1)(x - r2)"]
    O -- "Turning point" --> Q["Use y = a(x - h)^2 + k"]
    O -- "Three points" --> R["Use y = ax^2 + bx + c"]
    P --> S["Use another point to find a"]
    Q --> S
    R --> T["Substitute points and solve simultaneous equations"]
    I --> U["State answer in context with units"]
    L --> U
    N --> U
    S --> U
    T --> U
    U --> V["Check reasonableness of answer"]
```
