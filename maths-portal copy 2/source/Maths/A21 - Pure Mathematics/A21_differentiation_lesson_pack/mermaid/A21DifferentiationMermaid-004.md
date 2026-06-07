# A21DifferentiationMermaid-004

## Asset Metadata
- Asset ID: A21DifferentiationMermaid-004
- Source: Chapter 9 implicit differentiation transcript + CCEA A21-DIFF-LO004
- Related lesson section: Implicit Differentiation
- Purpose: Workflow for collecting \(dy/dx\) terms.

```mermaid
flowchart TD
    A["Start: x^2 + xy + y^2 = 7"] --> B["Differentiate every term w.r.t. x"]
    B --> C["2x + (x dy/dx + y) + 2y dy/dx = 0"]
    C --> D["Collect dy/dx terms"]
    D --> E["x dy/dx + 2y dy/dx = -(2x+y)"]
    E --> F["Factor dy/dx"]
    F --> G["dy/dx(x+2y)=-(2x+y)"]
    G --> H["dy/dx=-(2x+y)/(x+2y)"]
```
