# AS2ProbabilityMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS2ProbabilityMermaid-004 |
| Asset type | Mermaid flowchart |
| Source | DrFrost tree diagram evidence plus CCEA AS2 Probability specification map |
| Related lesson section | Tree Diagrams; Worked Examples; Exam Technique Notes |
| Purpose | Show the calculation logic for tree diagrams: multiply along paths and add separate successful paths. |

```mermaid
flowchart TD
    A["Start: events happen in succession"] --> B["Draw the first set of branches"]
    B --> C["Write the probability on each first branch"]
    C --> D{"Is there replacement or unchanged probability?"}
    D -- "With replacement or independent repeat" --> E["Use the same probabilities on later matching branches"]
    D -- "Without replacement" --> F["Update the number remaining and the denominator"]
    E --> G["Draw later branches"]
    F --> G
    G --> H["Identify the successful path or paths"]
    H --> I["Multiply probabilities along each successful path"]
    I --> J{"Is there more than one successful path?"}
    J -- "Yes" --> K["Add the path probabilities"]
    J -- "No" --> L["Use the single path probability"]
    K --> M["Final probability"]
    L --> M
    M --> N["Check branch probabilities from each split add to 1"]
    N --> O["Check final answer is between 0 and 1"]
```
