# A21NumericalMethodsMermaid-009_newton_raphson_failure_cases

**Asset ID:** A21NumericalMethodsMermaid-009  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Newton-Raphson failure cases.

```mermaid
flowchart TD
    A["Apply Newton-Raphson"] --> B{"Is f'(x_n)=0?"}
    B -- "Yes" --> C["Division by zero"]
    C --> D["Horizontal tangent"]
    D --> E["Method fails"]
    B -- "No" --> F["Calculate next approximation"]
    F --> G{"Sequence settles?"}
    G -- "Yes" --> H["Converges"]
    G -- "No" --> I["May diverge or approach wrong root"]
```
