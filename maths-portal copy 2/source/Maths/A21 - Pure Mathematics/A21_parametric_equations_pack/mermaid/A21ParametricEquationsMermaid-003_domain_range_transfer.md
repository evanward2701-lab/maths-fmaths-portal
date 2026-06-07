# A21ParametricEquationsMermaid-003

## Asset ID
A21ParametricEquationsMermaid-003

## Source
CCEA specification map A21-CG-LO001; transcript explanation of domain and range transfer.

## Related lesson section
Core Theory; Common Mistakes and Exam Traps.

## Purpose
Prevent the common error of finding the Cartesian equation but forgetting the restricted domain and range.

```mermaid
flowchart TD
    A["Given x = p(t), y = q(t), and a restriction on t"] --> B["Find possible values of x = p(t)"]
    B --> C["These x-values become the domain"]
    A --> D["Find possible values of y = q(t)"]
    D --> E["These y-values become the range"]
    B --> F{"Check endpoints"}
    D --> F
    F --> G["Use < or > if endpoint is excluded"]
    F --> H["Use ≤ or ≥ if endpoint is included"]
    B --> I{"Check turning points inside the interval"}
    D --> I
    I --> J["Quadratics and trig functions may have max/min values away from endpoints"]
    C --> K["Do not sketch the full Cartesian curve unless allowed"]
    E --> K
```
