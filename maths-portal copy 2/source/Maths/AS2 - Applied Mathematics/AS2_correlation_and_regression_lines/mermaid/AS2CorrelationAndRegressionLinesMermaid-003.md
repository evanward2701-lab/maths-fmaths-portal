# AS2CorrelationAndRegressionLinesMermaid-003

## Asset ID
`AS2CorrelationAndRegressionLinesMermaid-003`

## Source
CCEA AS2-DPI-LO007 + Hideko causation example.

## Related Lesson Section
Core Theory; Worked Example 3; Common Mistakes.

## Purpose
Causation warning flowchart showing association, causal claim and lurking variable.

```mermaid
flowchart TD
    A[Scatter diagram shows correlation] --> B[There is an association]
    B --> C{Can we conclude one variable causes the other?}
    C -- No, not from correlation alone --> D[Correlation does not imply causation]
    C -- Only with stronger evidence --> E[Need more evidence before a causal claim]
    D --> F[Look for another possible explanation]
    F --> G[Possible lurking variable]
    G --> H[Example: work experience]
    H --> I[Leaving education later may mean less work experience at age 25]
    I --> J[Lower pay may be linked to work experience, not education itself]
    D --> K[Safe exam wording]
    K --> L[The data suggests an association, but does not prove causation]
```
