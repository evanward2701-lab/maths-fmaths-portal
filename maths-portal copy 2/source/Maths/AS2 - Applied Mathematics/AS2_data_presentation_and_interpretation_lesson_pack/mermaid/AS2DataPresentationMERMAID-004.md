# AS2DataPresentationMERMAID-004

**Asset ID:** AS2DataPresentationMERMAID-004  
**Source:** Box plot drawing example  
**Related lesson section:** Worked Example 5  
**Purpose:** Capture the correct order for constructing a box plot when outliers are present.

```mermaid
flowchart TD
    A[Given summary data] --> B[Find missing quartile if needed]
    B --> C[Calculate IQR]
    C --> D[Calculate lower outlier boundary]
    D --> E[Calculate upper outlier boundary]
    E --> F[Identify outliers]
    F --> G[Draw box from Q1 to Q3]
    G --> H[Draw median line inside box]
    H --> I[Draw lower whisker to smallest non-outlier]
    I --> J{Upper outlier exists?}
    J -->|No| K[Draw upper whisker to maximum]
    J -->|Yes| L{Choose allowed whisker endpoint}
    L --> M[Largest value that is not an outlier]
    L --> N[Outlier boundary]
    M --> O[Mark outlier with cross]
    N --> O
    O --> P[Show boundary calculations in working]
```
