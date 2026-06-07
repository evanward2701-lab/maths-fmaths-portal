# AS2DataPresentationMERMAID-009

**Asset ID:** AS2DataPresentationMERMAID-009  
**Source:** Frequency polygon evidence  
**Related lesson section:** Core Theory, Frequency Polygons  
**Purpose:** Show how to form a frequency polygon from histogram bars, including zero-frequency intervals.

```mermaid
flowchart TD
    A[Start with histogram or grouped frequency table] --> B[Find midpoint of each class interval]
    B --> C[Plot each midpoint at the top of its histogram bar]
    C --> D{Does an interval have frequency zero?}
    D -->|Yes| E[Plot midpoint at height zero]
    D -->|No| F[Plot midpoint at bar height]
    E --> G[Do not skip the interval]
    F --> H[Continue with all intervals]
    G --> I[Join plotted midpoint points with straight line segments]
    H --> I
    I --> J[Frequency polygon completed]
```
