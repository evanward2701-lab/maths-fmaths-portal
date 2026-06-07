# AS1CoordinateGeometryCirclesMermaid-005

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-005 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, pages 17-18; Chapter 6 Circles transcript, Circles 5 |
| Related lesson section | Core Theory: Tangent-radius theorem; Worked Example 10 |
| Purpose | Show the method for finding a tangent through a given point on the circumference. |
| CCEA alignment | AS1-CG-LO001, AS1-CG-LO003, AS1-CG-LO007, AS1-CG-LO008 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given circle and point P on circumference"] --> B["Read or find centre C"]
    B --> C["Verify P lies on circle if required"]
    C --> D["Find gradient of radius CP"]
    D --> E["m_r = (y_P - y_C)/(x_P - x_C)"]
    E --> F["Tangent is perpendicular to radius"]
    F --> G["m_t = negative reciprocal of m_r"]
    G --> H["Use point-gradient form through P"]
    H --> I["y - y_P = m_t(x - x_P)"]
    I --> J["Rearrange into requested form"]
    J --> K{"Requested form?"}
    K --> L["Leave as point-gradient form if allowed"]
    K --> M["Convert to ax + by + c = 0 if asked"]
    K --> N["Convert to y = mx + c if asked"]
```
