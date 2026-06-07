# AS1DifferentiationMERMAID-001

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-001`
- Asset type: Mermaid flowchart
- Source: CCEA AS1-DIFF specification map + Chapter 12 Differentiation PDF pp.2–3
- Related lesson section: Big Picture Explanation; Core Theory 1
- Purpose: Show why a curve needs a gradient function rather than a single gradient.
- Status: Final

```mermaid
flowchart TD
    A["Start: We want the gradient"] --> B{"Type of graph?"}
    B --> C["Straight line"]
    B --> D["Curve"]
    C --> E["Gradient is constant"]
    E --> F["Example: y = 3x + 2"]
    F --> G["m = 3 everywhere"]
    D --> H["Gradient varies from point to point"]
    H --> I["Example: y = x^2"]
    I --> J["At x = -3, gradient = -6"]
    I --> K["At x = 0, gradient = 0"]
    I --> L["At x = 3, gradient = 6"]
    J --> M["Need a rule in terms of x"]
    K --> M
    L --> M
    M --> N["Gradient function"]
    N --> O["For y = x^2, gradient function = 2x"]
```
