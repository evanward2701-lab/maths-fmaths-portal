# AS1VectorsMermaid-005

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1VectorsMermaid-005 |
| Asset type | Mermaid diagram |
| Suggested file | mermaid/AS1VectorsMermaid-005_unit_vector.md |
| Source | CCEA AS1-VEC-LO002; Phase 1 Core Theory 4 |
| Related lesson section | Core Theory: Unit vectors; Worked Example 4 |
| Purpose | Show the step-by-step process for finding a unit vector in the direction of a given vector. |
| Boundary note | 2D unit vectors only. |

## Mermaid Code

```mermaid
flowchart TD
    A["Given vector a = (x, y)"] --> B["Find its magnitude"]
    B --> C["|a| = sqrt(x^2 + y^2)"]
    C --> D["Divide the vector by its magnitude"]
    D --> E["a-hat = a / |a|"]
    E --> F["a-hat = (x / sqrt(x^2 + y^2), y / sqrt(x^2 + y^2))"]
    F --> G["Check magnitude"]
    G --> H["|a-hat| = 1"]
    H --> I["Therefore a-hat is a unit vector<br/>in the direction of a"]
```
