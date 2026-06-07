# AS1AlgebraicExpressionsMER-006

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-006`
- **Source:** Dr Frost surds and rationalising denominator slides and transcript
- **Related lesson section:** Surds, Rationalising the Denominator, Common Mistakes and Exam Traps
- **Purpose:** Show the decision process for simplifying surds and rationalising denominators.

```mermaid
flowchart TD
    A["Expression involving surds"] --> B{"What is required?"}

    B --> C["Simplify surd"]
    B --> D["Add or subtract surds"]
    B --> E["Multiply surds"]
    B --> F["Rationalise denominator"]

    C --> C1["Find square factor"]
    C1 --> C2["Split root into product"]
    C2 --> C3["Simplify square root part"]

    D --> D1["Simplify each surd first"]
    D1 --> D2{"Same surd part?"}
    D2 -->|Yes| D3["Collect coefficients"]
    D2 -->|No| D4["Leave as unlike surds"]

    E --> E1["Multiply coefficients"]
    E1 --> E2["Multiply surd parts"]
    E2 --> E3["Simplify result"]

    F --> F1{"Denominator type?"}
    F1 --> G["Single surd"]
    F1 --> H["Binomial with surd"]

    G --> G1["Multiply top and bottom by same surd"]
    G1 --> G2["Denominator becomes rational"]

    H --> H1["Use conjugate"]
    H1 --> H2["Change sign in the middle"]
    H2 --> H3["Apply difference of two squares"]
    H3 --> H4["Middle surd terms cancel"]

    C3 --> Z["Exact simplified form"]
    D3 --> Z
    D4 --> Z
    E3 --> Z
    G2 --> Z
    H4 --> Z
```
