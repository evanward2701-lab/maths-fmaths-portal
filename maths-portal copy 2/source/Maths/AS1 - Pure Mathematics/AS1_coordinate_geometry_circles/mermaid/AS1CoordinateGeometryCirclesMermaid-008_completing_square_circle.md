# AS1CoordinateGeometryCirclesMermaid-008

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-008 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, pages 11-12; Chapter 6 Circles transcript, Circles 3 |
| Related lesson section | Core Theory: Completing the square for circle equations |
| Purpose | Show the exact method for changing an expanded circle equation into centre-radius form. |
| CCEA alignment | AS1-CG-LO005, AS1-CG-LO006, AS1-AF-LO005 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given expanded circle equation"] --> B["Group x-terms and y-terms"]
    B --> C["Complete the square for x-terms"]
    B --> D["Complete the square for y-terms"]
    C --> E["Counterbalance the extra constant from x-square"]
    D --> F["Counterbalance the extra constant from y-square"]
    E --> G["Collect constants"]
    F --> G
    G --> H["Rearrange into centre-radius form"]
    H --> I["(x - a)^2 + (y - b)^2 = r^2"]
    I --> J["Read centre as (a,b)"]
    I --> K["Read radius as sqrt(r^2)"]
    J --> L["Check signs carefully"]
    K --> M["Check r^2 is positive"]
```
