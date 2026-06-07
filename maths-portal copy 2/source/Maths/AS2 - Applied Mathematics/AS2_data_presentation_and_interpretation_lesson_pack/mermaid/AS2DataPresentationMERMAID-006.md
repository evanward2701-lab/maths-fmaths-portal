# AS2DataPresentationMERMAID-006

**Asset ID:** AS2DataPresentationMERMAID-006  
**Source:** Histogram recap and A-Level scaling evidence  
**Related lesson section:** Core Theory, Histograms  
**Purpose:** Show why frequency density is needed and how A-Level histogram scaling works.

```mermaid
flowchart TD
    A[Continuous grouped data] --> B{Are class widths equal?}
    B -->|Yes| C[Raw frequency heights may be easier to interpret]
    B -->|No| D[Raw frequency heights can mislead]
    D --> E[Use frequency density]
    E --> F[Frequency density = frequency / class width]
    F --> G[Frequency = frequency density times class width]
    G --> H[Histogram bar area = width times height]
    H --> I{Is vertical scale true frequency density?}
    I -->|Yes| J[Area equals frequency]
    I -->|No or scaled| K[Area is proportional to frequency]
    K --> L[Area = k times frequency]
    L --> M[Find k from known area and known frequency]
    M --> N[Use same k throughout the histogram]
```
