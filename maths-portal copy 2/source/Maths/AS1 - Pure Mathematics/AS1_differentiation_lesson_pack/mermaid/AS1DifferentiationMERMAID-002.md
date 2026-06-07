# AS1DifferentiationMERMAID-002

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-002`
- Asset type: Mermaid flowchart
- Source: Chapter 12 Differentiation PDF pp.4–6; transcript on first principles
- Related lesson section: Core Theory 2–5
- Purpose: Show the secant-to-tangent limit idea behind differentiation by first principles.
- Status: Final

```mermaid
flowchart TD
    A["Choose a point on the curve"] --> B["Example point: (x, x^2)"]
    B --> C["Choose a nearby point"]
    C --> D["Nearby point: (x + h, (x + h)^2)"]
    D --> E["Find gradient between the two points"]
    E --> F["Gradient = change in y / change in x"]
    F --> G["Gradient = ((x + h)^2 - x^2) / h"]
    G --> H["Let h tend towards 0"]
    H --> I["Nearby point moves closer to original point"]
    I --> J["Secant becomes tangent"]
    J --> K["Limit gives exact tangent gradient"]
    K --> L["Derivative: f'(x) = lim as h -> 0 of (f(x+h)-f(x))/h"]
```
