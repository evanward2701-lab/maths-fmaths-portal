# AS1DifferentiationMERMAID-008

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-008`
- Asset type: Mermaid flowchart
- Source: CCEA AS1-DIFF-LO003 and LO007 + Chapter 12 optimisation/modelling evidence
- Related lesson section: Core Theory 23–25
- Purpose: Show the standard optimisation workflow for AS1 differentiation modelling problems.
- Status: Final

```mermaid
flowchart TD
    A["Optimisation problem"] --> B["Identify target quantity"]
    B --> C["Example targets: area, volume, cost, distance"]
    C --> D["Identify constraint"]
    D --> E["Use constraint to remove one variable"]
    E --> F["Write target as a function of one variable"]
    F --> G["Differentiate target function"]
    G --> H["Set derivative equal to zero"]
    H --> I["Solve for variable"]
    I --> J["Substitute back to find required value"]
    J --> K["Check maximum or minimum"]
    K --> L{"Use second derivative or sign test"}
    L --> M["f''(x) < 0: maximum"]
    L --> N["f''(x) > 0: minimum"]
    L --> O["If inconclusive: use sign test or context"]
    M --> P["State final answer with units if applicable"]
    N --> P
    O --> P
```
