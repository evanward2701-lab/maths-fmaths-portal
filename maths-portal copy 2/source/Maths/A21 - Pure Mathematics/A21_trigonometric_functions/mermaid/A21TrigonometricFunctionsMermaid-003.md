# A21TrigonometricFunctionsMermaid-003

**Asset ID:** `A21TrigonometricFunctionsMermaid-003`  
**Source:** Chapter 6 solving examples involving reciprocal trig equations  
**Related lesson section:** Worked Examples → Solving reciprocal trig equations  
**Purpose:** Show the standard solving route for equations involving `sec`, `cosec` and `cot`.

```mermaid
flowchart TD
    A["Equation contains sec, cosec or cot"] --> B["Rewrite using reciprocal definitions"]
    B --> C{"Would this require taking the reciprocal of 0?"}
    C -- "Yes" --> D["Do not divide by 0.<br/>Use graph/asymptote interpretation instead"]
    C -- "No" --> E["Convert into a sin, cos or tan equation"]
    E --> F{"Is the argument kθ,<br/>such as 2θ or 3θ?"}
    F -- "Yes" --> G["Expand the interval for kθ"]
    F -- "No" --> H["Use the given interval"]
    G --> I["Find the reference angle or exact value"]
    H --> I
    I --> J["Use quadrant signs and periodicity<br/>to list all valid solutions"]
    J --> K{"Was the argument kθ?"}
    K -- "Yes" --> L["Divide every solution by k"]
    K -- "No" --> M["Keep solutions as found"]
    L --> N["Round only at the end<br/>and list in increasing order"]
    M --> N
```
