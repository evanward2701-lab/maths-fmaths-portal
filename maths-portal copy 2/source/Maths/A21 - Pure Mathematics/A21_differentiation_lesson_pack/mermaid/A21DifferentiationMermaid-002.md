# A21DifferentiationMermaid-002

## Asset Metadata
- Asset ID: A21DifferentiationMermaid-002
- Source: CCEA A21-DIFF-LO002 + Chapter 9 transcript
- Related lesson section: Chain, Product and Quotient Rules
- Purpose: Rule-selection flowchart.

```mermaid
flowchart TD
    A["Look at the expression"] --> B{"Explicit y in x?"}
    B -- Yes --> C{"Function inside function?"}
    C -- Yes --> C1["Chain rule"]
    C -- No --> D{"Functions multiplied?"}
    D -- Yes --> D1["Product rule"]
    D -- No --> E{"Function divided by function?"}
    E -- Yes --> E1["Quotient rule"]
    E -- No --> F["Use standard rule or simplify"]
    B -- No --> G{"x and y in terms of t?"}
    G -- Yes --> G1["Parametric: dy/dx=(dy/dt)/(dx/dt)"]
    G -- No --> H{"x and y mixed?"}
    H -- Yes --> H1["Implicit differentiation"]
    H -- No --> I{"Rate context?"}
    I -- Yes --> I1["Connected rates"]
    I -- No --> J["Review boundary"]
```
