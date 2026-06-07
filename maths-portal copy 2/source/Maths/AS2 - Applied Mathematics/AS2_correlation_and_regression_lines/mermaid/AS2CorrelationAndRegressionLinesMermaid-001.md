# AS2CorrelationAndRegressionLinesMermaid-001

## Asset ID
`AS2CorrelationAndRegressionLinesMermaid-001`

## Source
CCEA AS2-DPI-LO005 + lesson correlation examples.

## Related Lesson Section
Key Definitions and Notation; Core Theory; Worked Example 1.

## Purpose
Flowchart for classifying correlation by type and strength.

```mermaid
flowchart TD
    A[Start with a scatter diagram] --> B{Is there a clear pattern?}
    B -- No --> C[No correlation]
    C --> C1[Do not add strong or weak]
    B -- Yes --> D{Does y tend to increase as x increases?}
    D -- Yes --> E[Positive correlation]
    D -- No --> F[Negative correlation]
    E --> G{How close are the points to a straight-line trend?}
    F --> H{How close are the points to a straight-line trend?}
    G -- Close together --> I[Strong positive correlation]
    G -- Spread out --> J[Weak positive correlation]
    H -- Close together --> K[Strong negative correlation]
    H -- Spread out --> L[Weak negative correlation]
    I --> M[Write a contextual sentence if asked to interpret]
    J --> M
    K --> M
    L --> M
```
