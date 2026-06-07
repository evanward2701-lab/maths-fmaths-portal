# A21NumericalMethodsMermaid-008_newton_raphson_workflow

**Asset ID:** A21NumericalMethodsMermaid-008  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Newton-Raphson workflow.

```mermaid
flowchart TD
    A["Start with f(x)=0"] --> B["Choose approximation x_n"]
    B --> C["Calculate f(x_n)"]
    B --> D["Calculate f'(x_n)"]
    C --> E["x_(n+1) = x_n - f(x_n)/f'(x_n)"]
    D --> E
    E --> F["New approximation x_(n+1)"]
    F --> G{"Accurate enough?"}
    G -- "Yes" --> H["State approximate root"]
    G -- "No" --> B
```
