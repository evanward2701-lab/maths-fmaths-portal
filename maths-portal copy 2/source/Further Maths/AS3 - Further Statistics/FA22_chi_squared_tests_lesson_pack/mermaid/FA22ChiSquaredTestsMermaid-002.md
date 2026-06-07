# Mermaid Asset: FA22ChiSquaredTestsMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | FA22ChiSquaredTestsMermaid-002 |
| Topic ID | FA22ChiSquaredTests |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | FA22-CHI2 |
| Related lesson file | FA22_chi_squared_tests_lesson.md |
| Related lesson section | # 9. Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22ChiSquaredTestsMermaid-002 | Source: CCEA FA22-CHI2 specification + contingency table evidence | Insert from mermaid/FA22ChiSquaredTestsMermaid-002.md | Purpose: Show the contingency-table independence test workflow, including the Yates correction branch for \(2\times2\) tables.]` |
| Source | CCEA FA22-CHI2 specification boundary + Dr Frost contingency-table evidence + teacher transcript |
| Purpose | Show the contingency-table independence test workflow, including the Yates correction branch for \(2\times2\) tables. |
| Status | Generated in Phase 2 |

## Mermaid code

```mermaid
flowchart TD
    A["Observed contingency table"] --> B["Add row totals,<br/>column totals and grand total"]
    B --> C["State hypotheses"]
    C --> C1["H0: variables are independent<br/>or there is no association"]
    C --> C2["H1: variables are not independent<br/>or there is an association"]
    C1 --> D["Calculate expected frequency for each cell"]
    C2 --> D
    D --> D1["E = row total × column total ÷ grand total"]
    D1 --> E{"Any expected frequency<br/>less than 5?"}
    E -- "Yes" --> F["Combine whole rows or whole columns<br/>where appropriate"]
    F --> B
    E -- "No" --> G{"Is the final table<br/>2 × 2?"}
    G -- "Yes" --> H["Use Yates correction"]
    H --> H1["X^2 = sum((|O - E| - 0.5)^2 / E)"]
    G -- "No" --> I["Use ordinary chi-squared statistic"]
    I --> I1["X^2 = sum((O - E)^2 / E)"]
    H1 --> J["Find degrees of freedom<br/>nu = (r - 1)(c - 1)"]
    I1 --> J
    J --> K["Find upper-tail chi-squared<br/>critical value from table"]
    K --> L{"Is X^2 calculated<br/>greater than the critical value?"}
    L -- "Yes" --> M["Reject H0"]
    L -- "No" --> N["Do not reject H0"]
    M --> O["Context conclusion:<br/>sufficient evidence of association"]
    N --> P["Context conclusion:<br/>insufficient evidence of association"]
```
