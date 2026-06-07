# AS1VectorsMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1VectorsMermaid-004 |
| Asset type | Mermaid diagram |
| Suggested file | mermaid/AS1VectorsMermaid-004_position_vectors.md |
| Source | CCEA AS1-VEC-LO004, AS1-VEC-LO005; Phase 1 Core Theory 6 and 7 |
| Related lesson section | Core Theory: Position vectors and vectors between points; Distance between two points |
| Purpose | Show the route from position vectors to \(\overrightarrow{AB}\) and then to distance \(AB\). |
| Boundary note | 2D position vectors only. |

## Mermaid Code

```mermaid
flowchart TD
    O["Origin O"] --> A["Point A(x1, y1)"]
    O --> B["Point B(x2, y2)"]
    A --> OA["Position vector OA = (x1, y1)"]
    B --> OB["Position vector OB = (x2, y2)"]
    OA --> AB["Vector AB"]
    OB --> AB
    AB --> RULE["AB vector = OB - OA"]
    RULE --> COMP["AB = (x2 - x1, y2 - y1)"]
    COMP --> DIST["Distance AB = |AB vector|"]
    DIST --> FORMULA["AB = sqrt((x2 - x1)^2 + (y2 - y1)^2)"]
    FORMULA --> WARN["Distance is scalar.<br/>Vector AB has direction."]
```
