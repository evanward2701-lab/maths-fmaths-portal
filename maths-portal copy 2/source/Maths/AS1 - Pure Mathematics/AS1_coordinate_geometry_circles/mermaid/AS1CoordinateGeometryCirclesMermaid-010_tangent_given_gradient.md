# AS1CoordinateGeometryCirclesMermaid-010

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1CoordinateGeometryCirclesMermaid-010 |
| Unit code | AS1 |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Source | Chapter 6 Circles PDF, page 18; Chapter 6 Circles transcript, Circles 5 |
| Related lesson section | Worked Example: Tangents with a given gradient |
| Purpose | Show how to find tangent equations when the tangent gradient is known but the points of contact are not. |
| CCEA alignment | AS1-CG-LO001, AS1-CG-LO003, AS1-CG-LO005, AS1-CG-LO007, AS1-CG-LO008 |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Given circle and tangent gradient m_t"] --> B["Read centre C(a,b) from circle equation"]
    B --> C["Find radius gradient m_r"]
    C --> D["m_r is negative reciprocal of m_t"]
    D --> E["Write equation of radius line through centre"]
    E --> F["Substitute radius line into circle equation"]
    F --> G["Solve for points of contact"]
    G --> H["Point of contact 1"]
    G --> I["Point of contact 2"]
    H --> J["Use tangent gradient m_t through point 1"]
    I --> K["Use tangent gradient m_t through point 2"]
    J --> L["Tangent equation 1"]
    K --> M["Tangent equation 2"]
    L --> N["Give answers in requested form"]
    M --> N
```
