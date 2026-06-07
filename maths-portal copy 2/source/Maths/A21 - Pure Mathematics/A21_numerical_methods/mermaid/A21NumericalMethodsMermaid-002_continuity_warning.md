# A21NumericalMethodsMermaid-002_continuity_warning

**Asset ID:** A21NumericalMethodsMermaid-002  
**Source:** CCEA specification map + Chapter 10 Numerical Methods evidence  
**Related lesson section:** A21 Numerical Methods lesson  
**Purpose:** Continuity warning using f(x)=1/x.

```mermaid
flowchart TD
    A["Example: f(x)=1/x"] --> B["f(-1) = -1"]
    A --> C["f(1) = 1"]
    B --> D["There is a change in sign"]
    C --> D
    D --> E{"Can we conclude there is a root in [-1,1]?"}
    E -- "No" --> F["f(x)=1/x is not continuous at x=0"]
    F --> G["Vertical asymptote"]
    G --> H["Graph jumps from negative to positive without crossing zero"]
```
