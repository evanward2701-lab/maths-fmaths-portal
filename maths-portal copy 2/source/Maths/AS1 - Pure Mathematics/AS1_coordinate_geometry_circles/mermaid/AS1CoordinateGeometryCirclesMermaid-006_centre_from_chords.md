# AS1CoordinateGeometryCirclesMermaid-006

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-006 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, pages 17-20; Chapter 6 Circles transcript, Circles 6 and Circles 8 |
| Related lesson section | Core Theory: Perpendicular bisector of a chord; Guided Practice 5 |
| Purpose | Show how two chord perpendicular bisectors meet at the circle centre. |
| CCEA alignment | AS1-CG-LO001, AS1-CG-LO002, AS1-CG-LO003, AS1-CG-LO005, AS1-CG-LO007 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given three points on a circle"] --> B["Choose two chords"]
    B --> C["Chord 1"]
    B --> D["Chord 2"]
    C --> E["Find midpoint of chord 1"]
    C --> F["Find gradient of chord 1"]
    F --> G["Find perpendicular gradient of chord 1"]
    E --> H["Equation of perpendicular bisector 1"]
    G --> H
    D --> I["Find midpoint of chord 2"]
    D --> J["Find gradient of chord 2"]
    J --> K["Find perpendicular gradient of chord 2"]
    I --> L["Equation of perpendicular bisector 2"]
    K --> L
    H --> M["Solve bisectors simultaneously"]
    L --> M
    M --> N["Intersection is centre of circle"]
    N --> O["Find radius using centre and one point"]
    O --> P["Write circle equation"]
    P --> Q["(x - a)^2 + (y - b)^2 = r^2"]
```
