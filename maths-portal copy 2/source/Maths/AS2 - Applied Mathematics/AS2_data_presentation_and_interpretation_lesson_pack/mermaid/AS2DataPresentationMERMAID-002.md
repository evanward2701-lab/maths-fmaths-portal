# AS2DataPresentationMERMAID-002

**Asset ID:** AS2DataPresentationMERMAID-002  
**Source:** Box plot recap and interpretation evidence  
**Related lesson section:** Core Theory, Box Plots  
**Purpose:** Explain the components of a box plot and the 25% interpretation trap.

```mermaid
flowchart LR
    A[Ordered data] --> B[Minimum]
    A --> C[Lower Quartile Q1]
    A --> D[Median Q2]
    A --> E[Upper Quartile Q3]
    A --> F[Maximum]
    C --> G[IQR = Q3 - Q1]
    B --> H[Range = Maximum - Minimum]
    F --> H
    B --> I[Minimum to Q1: 25 percent]
    C --> J[Q1 to Median: 25 percent]
    D --> K[Median to Q3: 25 percent]
    E --> L[Q3 to Maximum: 25 percent]
    I --> M[Wider section means more spread out]
    J --> M
    K --> M
    L --> M
    M --> N[Do not say wider section means more people]
```
