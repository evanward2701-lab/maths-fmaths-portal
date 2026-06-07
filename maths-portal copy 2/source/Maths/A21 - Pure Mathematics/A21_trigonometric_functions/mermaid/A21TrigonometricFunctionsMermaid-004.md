# A21TrigonometricFunctionsMermaid-004

**Asset ID:** `A21TrigonometricFunctionsMermaid-004`  
**Source:** CCEA A21-TRIG-LO002 and A21-TRIG-LO003; Chapter 6 inverse trig evidence  
**Related lesson section:** Inverse Trig Functions  
**Purpose:** Explain why inverse trig functions need restricted domains before reflecting in $y=x$.

```mermaid
flowchart TD
    A["Start with y = sin x, y = cos x or y = tan x"] --> B{"Is the full graph one-to-one?"}
    B -- "No" --> C["Restrict the domain first"]
    C --> D["For arcsin:<br/>restrict sin x to -π/2 ≤ x ≤ π/2"]
    C --> E["For arccos:<br/>restrict cos x to 0 ≤ x ≤ π"]
    C --> F["For arctan:<br/>restrict tan x to -π/2 < x < π/2"]
    D --> G["Reflect the restricted graph in y = x"]
    E --> G
    F --> G
    G --> H["Obtain inverse trig graph"]
    H --> I["State domain and range of arcsin, arccos or arctan"]
```
