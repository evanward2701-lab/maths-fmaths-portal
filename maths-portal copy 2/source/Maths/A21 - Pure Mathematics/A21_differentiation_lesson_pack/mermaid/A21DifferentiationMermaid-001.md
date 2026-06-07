# A21DifferentiationMermaid-001

## Asset Metadata
- Asset ID: A21DifferentiationMermaid-001
- Source: Chapter 9 Differentiation transcript + slide PDF + CCEA A21-DIFF-LO001
- Related lesson section: Core Theory 1
- Purpose: Show proof pathway from first principles to \(d/dx(\sin x)=\cos x\).

```mermaid
flowchart TD
    A["y = f(x) = sin x"] --> B["Use first principles"]
    B --> C["f'(x)=lim h->0 [f(x+h)-f(x)]/h"]
    C --> D["Substitute sin x"]
    D --> E["lim h->0 [sin(x+h)-sin x]/h"]
    E --> F["sin(x+h)=sin x cos h + cos x sin h"]
    F --> G["Collect terms: sin x(cos h-1)+cos x sin h"]
    G --> H["Split fractions"]
    H --> I["sin x((cos h-1)/h)+cos x(sin h/h)"]
    I --> J["sin h/h -> 1"]
    I --> K["(cos h-1)/h -> 0"]
    J --> L["f'(x)=sin x(0)+cos x(1)"]
    K --> L
    L --> M["f'(x)=cos x"]
```
