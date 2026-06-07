# AS1CoordinateGeometryCirclesMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-004 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, pages 14-15; Chapter 6 Circles transcript, Circles 4 |
| Related lesson section | Core Theory: Line-circle intersections; Worked Examples 7 to 9 |
| Purpose | Show how substitution produces a quadratic and how the discriminant identifies secant, tangent or no intersection. |
| CCEA alignment | AS1-CG-LO005, AS1-AF-LO004, AS1-AF-LO006, AS1-AF-LO007 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given a line and a circle"] --> B["Substitute the line equation into the circle equation"]
    B --> C["Simplify to a quadratic in x"]
    C --> D["Quadratic: ax^2 + bx + c = 0"]
    D --> E["Compute discriminant D = b^2 - 4ac"]
    E --> F{"Value of D?"}
    F --> G["D > 0"]
    F --> H["D = 0"]
    F --> I["D < 0"]
    G --> J["Two real roots"]
    J --> K["Two intersection points"]
    K --> L["Line is a secant"]
    H --> M["One repeated root"]
    M --> N["One point of contact"]
    N --> O["Line is a tangent"]
    I --> P["No real roots"]
    P --> Q["No intersection"]
    Q --> R["Line misses the circle"]
```
