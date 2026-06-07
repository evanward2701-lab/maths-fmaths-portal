# AS2DataPresentationMERMAID-003

**Asset ID:** AS2DataPresentationMERMAID-003  
**Source:** Outlier rule and anomaly/cleaning data evidence  
**Related lesson section:** Core Theory, Outliers and Cleaning Data  
**Purpose:** Show the decision chain for detecting outliers and deciding whether a value is an anomaly.

```mermaid
flowchart TD
    A[Start with ordered data or summary statistics] --> B{Which outlier rule is stated?}
    B --> C[Quartile rule]
    B --> D[Mean and standard deviation rule]
    C --> C1[IQR = Q3 - Q1]
    C1 --> C2[Lower boundary = Q1 - 1.5 IQR]
    C2 --> C3[Upper boundary = Q3 + 1.5 IQR]
    D --> D1[Use mean xbar and standard deviation sigma]
    D1 --> D2[Lower boundary = xbar - 2 sigma]
    D2 --> D3[Upper boundary = xbar + 2 sigma]
    C3 --> E[Compare data values with boundaries]
    D3 --> E
    E --> F{Value outside boundary?}
    F -->|No| G[Not an outlier by this rule]
    F -->|Yes| H[Outlier]
    H --> I{Context suggests error or impossible value?}
    I -->|No| J[Treat as possible genuine outlier]
    I -->|Yes| K[Likely anomaly]
    K --> L[Clean data by removing or correcting if justified]
```
