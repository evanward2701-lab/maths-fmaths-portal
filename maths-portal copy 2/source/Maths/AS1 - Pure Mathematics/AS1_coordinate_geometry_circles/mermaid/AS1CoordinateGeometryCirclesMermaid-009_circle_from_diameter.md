# AS1CoordinateGeometryCirclesMermaid-009

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-009 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, pages 9-10; Chapter 6 Circles transcript, Circles 2 |
| Related lesson section | Worked Example: Equation of a circle from a diameter |
| Purpose | Show how a diameter gives the centre and radius needed for the circle equation. |
| CCEA alignment | AS1-CG-LO002, AS1-CG-LO005 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given endpoints A(x1,y1), B(x2,y2) of a diameter"] --> B["Find centre C as midpoint of AB"]
    B --> C["C = ((x1+x2)/2, (y1+y2)/2)"]
    C --> D["Find radius"]
    D --> E{"Which distance is easiest?"}
    E --> F["Use CA"]
    E --> G["Use CB"]
    E --> H["Or find AB then halve it"]
    F --> I["r^2 = (x_A - x_C)^2 + (y_A - y_C)^2"]
    G --> J["r^2 = (x_B - x_C)^2 + (y_B - y_C)^2"]
    H --> K["r = AB/2"]
    I --> L["Write circle equation"]
    J --> L
    K --> L
    L --> M["(x - a)^2 + (y - b)^2 = r^2"]
    M --> N["Use centre C(a,b)"]
```
