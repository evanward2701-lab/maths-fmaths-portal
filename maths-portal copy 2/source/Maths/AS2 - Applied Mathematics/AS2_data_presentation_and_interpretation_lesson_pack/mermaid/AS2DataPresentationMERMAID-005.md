# AS2DataPresentationMERMAID-005

**Asset ID:** AS2DataPresentationMERMAID-005  
**Source:** Cumulative frequency diagram evidence  
**Related lesson section:** Core Theory, Cumulative Frequency Diagrams  
**Purpose:** Show the workflow for plotting and reading cumulative frequency diagrams.

```mermaid
flowchart TD
    A[Grouped frequency table] --> B[Calculate cumulative frequencies]
    B --> C[Plot upper class boundary against cumulative frequency]
    C --> D[Include starting point at lower boundary with CF = 0]
    D --> E[Join points with straight line segments]
    E --> F[Total frequency n]
    F --> G[Q1 position = n / 4]
    F --> H[Median position = n / 2]
    F --> I[Q3 position = 3n / 4]
    G --> J[Read across to graph then down to x-axis]
    H --> J
    I --> J
    J --> K[Estimate Q1, median and Q3]
    K --> L[IQR = Q3 - Q1]
    E --> M[Less than a value: read CF directly]
    E --> N[More than a value: total minus CF]
    E --> O[Between two values: subtract two CF readings]
```
