# A21NumericalMethodsMermaid-004_accuracy_interval_workflow

**Asset ID:** A21NumericalMethodsMermaid-004  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Accuracy interval workflow.

```mermaid
flowchart TD
    A["Claim: alpha = 2.307 correct to 3 d.p."] --> B["Choose lower bound: 2.3065"]
    A --> C["Choose upper bound: 2.3075"]
    B --> D["Calculate f(2.3065)"]
    C --> E["Calculate f(2.3075)"]
    D --> F{"Opposite signs?"}
    E --> F
    F -- "Yes" --> G["Root lies between 2.3065 and 2.3075"]
    G --> H["Every value in this interval rounds to 2.307"]
    H --> I["Therefore alpha = 2.307 correct to 3 d.p."]
```
