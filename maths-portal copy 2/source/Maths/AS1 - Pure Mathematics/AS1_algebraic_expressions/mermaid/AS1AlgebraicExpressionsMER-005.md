# AS1AlgebraicExpressionsMER-005

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-005`
- **Source:** Dr Frost fractional and negative indices examples
- **Related lesson section:** Core Theory, Worked Examples, Exam Technique
- **Purpose:** Show how to unpack a rational exponent without muddling root, power and reciprocal operations.

```mermaid
flowchart TD
    A["Expression with rational exponent"] --> B{"Exponent type?"}

    B --> C["Zero exponent"]
    B --> D["Negative exponent"]
    B --> E["Fractional exponent"]
    B --> F["Negative fractional exponent"]

    C --> C1["a^0 = 1 for a not equal to 0"]

    D --> D1["Take reciprocal"]
    D1 --> D2["a^(-m) = 1 / a^m"]

    E --> E1["Identify numerator and denominator"]
    E1 --> E2["Denominator gives the root"]
    E2 --> E3["Numerator gives the power"]
    E3 --> E4["a^(m/n) = (nth root of a)^m"]

    F --> F1["Deal with negative sign"]
    F1 --> F2["Take reciprocal"]
    F2 --> F3["Then apply fractional exponent"]
    F3 --> F4["Root first, then power"]

    C1 --> Z["Simplify"]
    D2 --> Z
    E4 --> Z
    F4 --> Z

    Z --> W["Check exact form"]
```
