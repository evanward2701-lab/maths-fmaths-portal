# AS1CoordinateGeometryCirclesMermaid-011

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-011 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Full Chapter 6 Circles PDF and transcript |
| Related lesson section | Exam Technique Notes |
| Purpose | Help students choose the correct method when a circle question starts with different information. |
| CCEA alignment | AS1-CG-LO001 to AS1-CG-LO008, plus AS1-AF-LO004 to AS1-AF-LO007 as support |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Circle question"] --> B{"What information is given?"}
    B --> C["Centre and radius"]
    C --> D["Use (x-a)^2 + (y-b)^2 = r^2"]
    B --> E["Endpoints of diameter"]
    E --> F["Centre = midpoint"]
    F --> G["Radius = distance from centre to endpoint"]
    G --> D
    B --> H["Expanded circle equation"]
    H --> I["Complete the square"]
    I --> J["Read centre and radius"]
    B --> K["Line and circle"]
    K --> L["Substitute line into circle"]
    L --> M["Solve quadratic or use discriminant"]
    B --> N["Tangent at known point"]
    N --> O["Find radius gradient"]
    O --> P["Tangent gradient = negative reciprocal"]
    P --> Q["Use point-gradient line equation"]
    B --> R["Three points on circle"]
    R --> S["Find two perpendicular bisectors"]
    S --> T["Their intersection is centre"]
    T --> U["Find radius and write equation"]
    B --> V["Triangle in circle"]
    V --> W{"Right angle or diameter involved?"}
    W --> X["Use angle in semicircle"]
    W --> Y["Otherwise use perpendicular bisectors"]
```
