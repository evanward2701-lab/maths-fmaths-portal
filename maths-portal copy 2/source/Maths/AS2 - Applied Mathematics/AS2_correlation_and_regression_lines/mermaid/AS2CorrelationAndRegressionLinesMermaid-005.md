# AS2CorrelationAndRegressionLinesMermaid-005

## Asset ID
`AS2CorrelationAndRegressionLinesMermaid-005`

## Source
CCEA AS2-DPI-LO006 + interpolation/extrapolation lesson evidence.

## Related Lesson Section
Core Theory; Worked Example 6; Exam Technique.

## Purpose
Reliability decision flowchart for interpolation, extrapolation and reverse prediction.

```mermaid
flowchart TD
    A[Use a regression line to estimate a value] --> B[Identify the variable being predicted]
    B --> C{Are you predicting response variable from explanatory variable?}
    C -- No --> D[Do not use this regression line backwards]
    C -- Yes --> E[Check the data range for x]
    E --> F{Is x-value inside observed data range?}
    F -- Yes --> G[Interpolation]
    G --> H[Estimate is more likely to be reliable]
    F -- No --> I[Extrapolation]
    I --> J[Estimate is less reliable]
    J --> K[Explain: outside the original data range]
    H --> L[Still mention model suitability if needed]
    D --> M[Final reliability comment]
    K --> M
    L --> M
```
