# AS1DifferentiationMERMAID-006

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-006`
- Asset type: Mermaid flowchart
- Source: CCEA AS1-DIFF-LO007 and LO008 + Chapter 12 Differentiation stationary-point evidence
- Related lesson section: Core Theory 17–21
- Purpose: Show how \(f'(x)\) and \(f''(x)\) are used to locate and classify stationary points.
- Status: Final

```mermaid
flowchart TD
    A["Given y = f(x)"] --> B["Differentiate"]
    B --> C["Find f'(x)"]
    C --> D["Stationary points occur when f'(x) = 0"]
    D --> E["Solve f'(x) = 0 for x-values"]
    E --> F["Substitute each x into original f(x)"]
    F --> G["Get stationary point coordinates"]
    G --> H["Differentiate again"]
    H --> I["Find f''(x)"]
    I --> J{"At stationary point, what is f''(x)?"}
    J --> K["f''(x) > 0"]
    K --> L["Local minimum"]
    J --> M["f''(x) < 0"]
    M --> N["Local maximum"]
    J --> O["f''(x) = 0"]
    O --> P["Test inconclusive"]
    P --> Q["Use sign changes in f'(x) or further curve reasoning"]
```
