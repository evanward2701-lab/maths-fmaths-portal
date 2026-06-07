# AS1CoordinateGeometryCirclesMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-003 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, page 7; Chapter 6 Circles transcript, Circles 2 |
| Related lesson section | Core Theory: Equation of a circle centred at \((a,b)\) |
| Purpose | Show why a shifted centre gives horizontal distance \(x-a\) and vertical distance \(y-b\). |
| CCEA alignment | AS1-CG-LO005 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Circle centred at C(a,b)"] --> B["Point P(x,y) lies on circle"]
    B --> C["Radius CP has length r"]
    B --> D["Horizontal distance = x - a"]
    B --> E["Vertical distance = y - b"]
    D --> F["Right-angled triangle from centre to point"]
    E --> F
    C --> F
    F --> G["Use Pythagoras"]
    G --> H["(x - a)^2 + (y - b)^2 = r^2"]
    H --> I["Centre is (a,b), radius is r"]
    I --> J["Sign warning"]
    J --> K["x + 3 means x - (-3), so centre x-coordinate is -3"]
```
