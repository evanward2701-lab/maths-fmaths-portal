# AS1EquationsInequalitiesMermaid-005

## Asset ID
AS1EquationsInequalitiesMermaid-005

## Source
- CCEA AS1-AF-LO009: inequalities with fractions reducible to linear/quadratic inequalities
- P1 Chapter 3 PDF: fractional inequality example
- Chapter 3 transcript: warning that multiplying directly by x is unsafe when x may be negative

## Related lesson section
Core Theory: Inequalities Involving Division by x

## Purpose
Show the safe route for fractional inequalities such as 6/x > 2, including the domain restriction.

## Mermaid code

```mermaid
flowchart TD
    A["Start: 6/x > 2"] --> B["State restriction: x ≠ 0"]
    B --> C{"Can we multiply directly by x?"}
    C -->|No| D["x could be negative<br/>Inequality direction might reverse"]
    D --> E["Use a safe positive multiplier: x²"]
    E --> F["x² · 6/x > 2x²"]
    F --> G["6x > 2x²"]
    G --> H["0 > 2x² - 6x"]
    H --> I["2x² - 6x < 0"]
    I --> J["Divide by 2: x² - 3x < 0"]
    J --> K["Factorise: x(x - 3) < 0"]
    K --> L["Critical values: x = 0 and x = 3"]
    L --> M["Sketch sign regions"]
    M --> N["Choose where expression is negative"]
    N --> O["Solution: 0 < x < 3"]
```
