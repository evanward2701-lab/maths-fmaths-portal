# A21NumericalMethodsMermaid-007_staircase_cobweb_process

**Asset ID:** A21NumericalMethodsMermaid-007  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Staircase/cobweb process.

```mermaid
flowchart TD
    A["Start at initial x-value"] --> B["Move vertically to curve y = g(x)"]
    B --> C["Move horizontally to line y = x"]
    C --> D["Move vertically to curve y = g(x)"]
    D --> E["Move horizontally to line y = x"]
    E --> F{"Path moves towards intersection?"}
    F -- "Yes" --> G["Iteration converges"]
    F -- "No" --> H["Iteration diverges or oscillates"]
```
