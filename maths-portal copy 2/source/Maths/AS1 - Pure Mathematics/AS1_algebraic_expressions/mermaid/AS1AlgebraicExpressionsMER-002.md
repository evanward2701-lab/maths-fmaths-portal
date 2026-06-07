# AS1AlgebraicExpressionsMER-002

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-002`
- **Source:** Dr Frost index laws slide and transcript explanation
- **Related lesson section:** Core Theory, Worked Examples, Common Mistakes and Exam Traps
- **Purpose:** Help students decide which index law applies before simplifying.

```mermaid
flowchart TD
    A["Expression with powers"] --> B{"What is happening?"}

    B --> C["Multiplication"]
    B --> D["Division"]
    B --> E["Power of a power"]
    B --> F["Power of a product"]
    B --> G["Negative exponent"]
    B --> H["Fractional exponent"]

    C --> C1{"Same base?"}
    C1 -->|Yes| C2["Add indices: a^m times a^n = a^(m+n)"]
    C1 -->|No| C3["Do not add indices"]
    C3 --> C4["Check for same exponent instead"]

    D --> D1{"Same base?"}
    D1 -->|Yes| D2["Subtract indices: a^m / a^n = a^(m-n)"]
    D1 -->|No| D3["Do not subtract indices"]

    E --> E1["Multiply indices: (a^m)^n = a^(mn)"]

    F --> F1["Apply power to every factor"]
    F1 --> F2["(ab)^n = a^n b^n"]

    G --> G1["Take reciprocal"]
    G1 --> G2["a^(-m) = 1 / a^m"]

    H --> H1["Denominator gives root"]
    H1 --> H2["Numerator gives power"]
    H2 --> H3["a^(m/n) = (nth root of a)^m"]

    C2 --> Z["Simplify fully"]
    D2 --> Z
    E1 --> Z
    F2 --> Z
    G2 --> Z
    H3 --> Z
```
