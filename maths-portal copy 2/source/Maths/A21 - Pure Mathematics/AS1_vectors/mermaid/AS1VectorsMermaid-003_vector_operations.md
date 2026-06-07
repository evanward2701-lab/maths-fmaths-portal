# AS1VectorsMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1VectorsMermaid-003 |
| Asset type | Mermaid diagram |
| Suggested file | mermaid/AS1VectorsMermaid-003_vector_operations.md |
| Source | CCEA AS1-VEC-LO003; Phase 1 Core Theory 5 |
| Related lesson section | Core Theory: Vector addition, subtraction and scalar multiplication |
| Purpose | Summarise the algebraic and geometric meaning of vector operations. |
| Boundary note | Uses two-dimensional column vectors only. |

## Mermaid Code

```mermaid
flowchart TD
    A["Vector operations"] --> B["Addition"]
    A --> C["Subtraction"]
    A --> D["Scalar multiplication"]
    B --> B1["Algebra:<br/>(a1, a2) + (b1, b2)<br/>= (a1 + b1, a2 + b2)"]
    B --> B2["Geometry:<br/>follow first vector,<br/>then follow second vector"]
    B2 --> B3["Triangle law"]
    B2 --> B4["Parallelogram law"]
    C --> C1["Algebra:<br/>(a1, a2) - (b1, b2)<br/>= (a1 - b1, a2 - b2)"]
    C --> C2["Geometry:<br/>add the opposite vector"]
    D --> D1["Algebra:<br/>k(a1, a2) = (ka1, ka2)"]
    D --> D2["Geometry:<br/>same direction if k > 0"]
    D --> D3["opposite direction if k < 0"]
    D --> D4["length multiplied by |k|"]
```
