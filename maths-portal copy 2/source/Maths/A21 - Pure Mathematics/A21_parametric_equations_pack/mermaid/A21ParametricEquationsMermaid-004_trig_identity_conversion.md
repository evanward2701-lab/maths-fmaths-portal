# A21ParametricEquationsMermaid-004

## Asset ID
A21ParametricEquationsMermaid-004

## Source
CCEA specification map A21-CG-LO001; transcript section on trig identity conversion.

## Related lesson section
Core Theory; Worked Examples 3, 4 and 5.

## Purpose
Show when to use trig identities rather than inverse trig rearrangement.

```mermaid
flowchart TD
    A["Parametric equations contain trig functions"] --> B{"Can t be eliminated neatly by substitution?"}
    B -->|Yes| C["Rearrange and substitute"]
    C --> D["Simplify to Cartesian form"]
    B -->|No| E["Look for trig identities"]
    E --> F["If sin t and cos t appear, use sin²t + cos²t = 1"]
    E --> G["If sin 2t appears, use sin 2t = 2sin t cos t"]
    E --> H["If cos 2t appears, choose a useful double-angle form"]
    F --> I["Express sin t and cos t using x and y"]
    I --> J["Substitute into the identity"]
    J --> K["Obtain a Cartesian equation"]
    G --> K
    H --> K
    K --> L["Check domain and range"]
```
