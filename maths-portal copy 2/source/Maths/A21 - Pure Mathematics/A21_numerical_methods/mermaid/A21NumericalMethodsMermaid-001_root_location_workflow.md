# A21NumericalMethodsMermaid-001_root_location_workflow

**Asset ID:** A21NumericalMethodsMermaid-001  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Root-location workflow using sign change and continuity.

```mermaid
flowchart TD
    A["Start with f(x)=0"] --> B["Choose interval: a < x < b"]
    B --> C["Calculate f(a)"]
    B --> D["Calculate f(b)"]
    C --> E{"Do f(a) and f(b) have opposite signs?"}
    D --> E
    E -- "Yes" --> F{"Is f(x) continuous on the interval?"}
    E -- "No" --> G["No guaranteed root from sign-change method"]
    F -- "Yes" --> H["Conclude: at least one root lies in the interval"]
    F -- "No" --> I["Cannot conclude: graph may jump past zero"]
```
