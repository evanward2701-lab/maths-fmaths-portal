# A21ParametricEquationsMermaid-002

## Asset ID
A21ParametricEquationsMermaid-002

## Source
CCEA specification map A21-CG-LO001; transcript explanation of eliminating \(t\) from \(x=2t,\ y=t^2\).

## Related lesson section
Core Theory; Worked Example 1.

## Purpose
Give students a clean conversion workflow for algebraic parametric equations.

```mermaid
flowchart TD
    A["Start with x = p(t), y = q(t)"] --> B{"Which equation is easiest to rearrange?"}
    B --> C["Make t the subject"]
    C --> D["Substitute this expression into the other equation"]
    D --> E["Simplify until only x and y remain"]
    E --> F["Cartesian equation found"]
    F --> G{"Was a restriction on t given?"}
    G -->|Yes| H["Use the restriction to find possible x-values"]
    H --> I["State the domain"]
    I --> J["Use the restriction to find possible y-values"]
    J --> K["State the range"]
    G -->|No| L["Check natural restrictions from logs, roots and denominators"]
```
