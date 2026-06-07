# AS1DifferentiationMERMAID-004

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-004`
- Asset type: Mermaid flowchart
- Source: CCEA AS1-DIFF-LO006 + Chapter 12 Differentiation PDF pp.11–20
- Related lesson section: Core Theory 7–13
- Purpose: Show the AS1 decision process for rewriting expressions before differentiating.
- Status: Final

```mermaid
flowchart TD
    A["Expression to differentiate"] --> B{"Is it a sum or difference of ax^n terms?"}
    B --> C["Yes"]
    B --> D["No"]
    C --> E["Apply power rule"]
    E --> F["d/dx of ax^n = anx^(n-1)"]
    D --> G{"Contains roots?"}
    G --> H["Rewrite roots as fractional powers"]
    G --> I{"Contains fractions?"}
    H --> B
    I --> J["Split numerator only where valid"]
    J --> K["Use index laws to rewrite powers"]
    K --> B
    I --> L{"Contains brackets/products?"}
    L --> M["Expand brackets first"]
    M --> B
    L --> N{"Number in denominator?"}
    N --> O["Keep number in denominator"]
    O --> P["Example: 1/(3x) = (1/3)x^-1"]
    P --> B
    N --> Q["If still not rewriteable, do not use off-spec rules"]
    Q --> R["Product, quotient and chain rules are not AS1 core here"]
```
