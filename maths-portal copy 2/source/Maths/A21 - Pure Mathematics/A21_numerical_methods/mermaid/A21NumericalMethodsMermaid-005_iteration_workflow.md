# A21NumericalMethodsMermaid-005_iteration_workflow

**Asset ID:** A21NumericalMethodsMermaid-005  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Iteration workflow.

```mermaid
flowchart LR
    A["Start with f(x)=0"] --> B["Rearrange into x = g(x)"]
    B --> C["Write x_next = g(x_current)"]
    C --> D["Choose starting value"]
    D --> E["Substitute to find next approximation"]
    E --> F["Use new value as next input"]
    F --> G{"Values settling?"}
    G -- "Yes" --> H["Convergent"]
    G -- "No" --> I["Divergent or non-convergent"]
```
