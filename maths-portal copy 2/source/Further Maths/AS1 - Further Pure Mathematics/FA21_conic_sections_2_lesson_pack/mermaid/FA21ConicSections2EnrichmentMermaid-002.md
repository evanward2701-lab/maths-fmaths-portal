# Mermaid Asset: FA21ConicSections2EnrichmentMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA21ConicSections2EnrichmentMermaid-002` |
| Type | Mermaid classification chart |
| Source | DrFrost/Pearson Conics 2 recap + screenshot visual evidence |
| Related lesson sections | Sections 6, 8.1, 9 |
| Purpose | Map the double-cone slicing idea into circle, ellipse, parabola and hyperbola. |
| Boundary status | Off-spec enrichment until official CCEA conics evidence is supplied. |

## Mermaid Code

```mermaid
flowchart TD
    A["Non-solid double cone"] --> B["Plane intersects cone"]
    B --> C["Conic section"]
    C --> D["Circle"]
    C --> E["Ellipse"]
    C --> F["Parabola"]
    C --> G["Hyperbola"]
    D --> D1["Plane parallel to base"]
    E --> E1["Plane less steep than cone surface"]
    E --> E2["x^2/a^2 + y^2/b^2 = 1"]
    F --> F1["Plane parallel to cone surface"]
    F --> F2["e = 1"]
    G --> G1["Plane steeper than cone surface"]
    G --> G2["Intersects both cones"]
    G --> G3["x^2/a^2 - y^2/b^2 = 1"]
    C --> H["Important warning"]
    H --> H1["The conic is the line of intersection"]
    H --> H2["The shaded region is not part of the conic"]
```
