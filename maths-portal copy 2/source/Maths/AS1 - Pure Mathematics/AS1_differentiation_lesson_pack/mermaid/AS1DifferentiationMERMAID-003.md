# AS1DifferentiationMERMAID-003

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-003`
- Asset type: Mermaid flowchart
- Source: Chapter 12 Differentiation PDF pp.5–10
- Related lesson section: Core Theory 3–4
- Purpose: Show the correct first-principles algebra route and the danger of substituting \(h=0\) too early.
- Status: Final

```mermaid
flowchart TD
    A["Start with first principles"] --> B["f'(x) = lim as h -> 0 of (f(x+h)-f(x))/h"]
    B --> C{"Substitute h = 0 immediately?"}
    C --> D["No"]
    C --> E["Yes"]
    E --> F["Usually creates 0/0"]
    F --> G["0/0 is indeterminate"]
    G --> H["Cannot evaluate yet"]
    D --> I["Expand f(x+h)"]
    I --> J["Simplify numerator"]
    J --> K["Factorise if possible"]
    K --> L["Cancel common factor h"]
    L --> M["Now take the limit h -> 0"]
    M --> N["Exact derivative obtained"]
    H --> I
```
