# AS1CoordinateGeometryCirclesMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-001 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, page 3; Chapter 6 Circles transcript, Circles 1 |
| Related lesson section | Core Theory: Perpendicular bisectors; Worked Example 1 |
| Purpose | Show the calculation pathway for the perpendicular bisector of a chord or line segment. |
| CCEA alignment | AS1-CG-LO001, AS1-CG-LO002, AS1-CG-LO003, AS1-CG-LO007 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given two points A(x1,y1) and B(x2,y2)"] --> B["Find midpoint M"]
    B --> C["M = ((x1+x2)/2, (y1+y2)/2)"]
    C --> D["Find gradient of AB"]
    D --> E["m_AB = (y2-y1)/(x2-x1)"]
    E --> F["Find perpendicular gradient"]
    F --> G["m_perp = negative reciprocal of m_AB"]
    G --> H["Use point-gradient form through M"]
    H --> I["y - y_M = m_perp(x - x_M)"]
    I --> J["Equation of perpendicular bisector"]
    K["Circle fact"] --> L["Perpendicular bisector of a chord passes through the centre"]
    J --> L
```
