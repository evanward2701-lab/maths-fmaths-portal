# AS1VectorsMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1VectorsMermaid-002 |
| Asset type | Mermaid diagram |
| Suggested file | mermaid/AS1VectorsMermaid-002_magnitude_direction.md |
| Source | CCEA AS1-VEC-LO002; Phase 1 Core Theory 2 and 3 |
| Related lesson section | Core Theory: Magnitude of a two-dimensional vector; Direction of a vector |
| Purpose | Show the calculation route from vector components to magnitude and direction. |
| Boundary note | Direction is for a 2D vector measured from the positive \(x\)-axis. Quadrant checking is included. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with vector a = (x, y)"] --> B["Magnitude"]
    A --> C["Direction angle theta"]
    B --> D["Use Pythagoras"]
    D --> E["|a| = sqrt(x^2 + y^2)"]
    C --> F["Use trigonometry"]
    F --> G["tan(theta) = y / x"]
    G --> H["theta = tan^-1(y / x)"]
    H --> I{"Which quadrant<br/>is the vector in?"}
    I --> J["x > 0, y > 0<br/>Quadrant I"]
    I --> K["x < 0, y > 0<br/>Quadrant II"]
    I --> L["x < 0, y < 0<br/>Quadrant III"]
    I --> M["x > 0, y < 0<br/>Quadrant IV"]
    J --> N["Calculator angle may be direct"]
    K --> O["Adjust angle"]
    L --> O
    M --> O
    N --> P["Final direction angle"]
    O --> P
```
