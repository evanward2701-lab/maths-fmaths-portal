# AS1AlgebraicExpressionsMER-007

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-007`
- **Source:** Dr Frost rationalising denominator examples
- **Related lesson section:** Rationalising the Denominator, Worked Examples
- **Purpose:** Show why the conjugate works for denominators like `sqrt(a) + b`.

```mermaid
flowchart TD
    A["Denominator: sqrt(a) + b"] --> B["Choose conjugate: sqrt(a) - b"]

    B --> C["Multiply numerator by conjugate"]
    B --> D["Multiply denominator by conjugate"]

    D --> E["(sqrt(a) + b)(sqrt(a) - b)"]
    E --> F["Use difference of two squares"]
    F --> G["(sqrt(a))^2 - b^2"]
    G --> H["a - b^2"]

    H --> I{"Is denominator rational?"}
    I -->|Yes| J["Rationalising complete"]
    I -->|No| K["Check algebra and simplify again"]

    C --> L["Expand numerator carefully"]
    L --> J

    J --> M["Final exact answer"]
```
