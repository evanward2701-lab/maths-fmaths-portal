# AS2CorrelationAndRegressionLinesMermaid-004

## Asset ID
`AS2CorrelationAndRegressionLinesMermaid-004`

## Source
CCEA AS2-DPI-LO004 + regression-line interpretation examples.

## Related Lesson Section
Core Theory; Worked Examples 4 and 5.

## Purpose
Flowchart for interpreting `a` and `b` in `y = a + bx`.

```mermaid
flowchart TD
    A[Given regression line: y = a + bx] --> B[Identify x and y from the context]
    B --> C[x is the explanatory variable]
    B --> D[y is the response variable]
    C --> E[Interpret b, the gradient]
    D --> E
    E --> F{Is b positive or negative?}
    F -- Positive --> G[For each 1-unit increase in x, y increases by b units]
    F -- Negative --> H[For each 1-unit increase in x, y decreases by |b| units]
    A --> I[Interpret a, the intercept]
    I --> J[a is the predicted value of y when x = 0]
    J --> K{Is x = 0 sensible and within the data range?}
    K -- Yes --> L[Intercept may have a useful context meaning]
    K -- No --> M[Interpret with caution]
    G --> N[Use variable names and units]
    H --> N
    L --> N
    M --> N
    N --> O[Final answer in context]
```
