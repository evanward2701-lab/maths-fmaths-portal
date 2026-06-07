# AS2CorrelationAndRegressionLinesMermaid-002

## Asset ID
`AS2CorrelationAndRegressionLinesMermaid-002`

## Source
CCEA AS2-DPI-LO004 + lesson variable-axis explanation.

## Related Lesson Section
Key Definitions and Notation; Exam Technique Notes.

## Purpose
Flowchart for identifying explanatory and response variables and writing contextual interpretations.

```mermaid
flowchart LR
    A[Real context] --> B[Choose two variables]
    B --> C[Horizontal axis: independent / explanatory variable]
    B --> D[Vertical axis: dependent / response variable]
    C --> E[Used to explain or predict]
    D --> F[Responds to explanatory variable]
    E --> G[Describe trend]
    F --> G
    G --> H{Correlation type?}
    H -- Positive --> I[As explanatory variable increases, response tends to increase]
    H -- Negative --> J[As explanatory variable increases, response tends to decrease]
    H -- No correlation --> K[No clear relationship]
    I --> L[Add context-specific variable names]
    J --> L
    K --> L
    L --> M[Final interpretation sentence]
```
