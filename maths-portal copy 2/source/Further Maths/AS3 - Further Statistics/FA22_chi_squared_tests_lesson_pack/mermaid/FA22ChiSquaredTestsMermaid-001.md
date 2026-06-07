# Mermaid Asset: FA22ChiSquaredTestsMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | FA22ChiSquaredTestsMermaid-001 |
| Topic ID | FA22ChiSquaredTests |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | FA22-CHI2 |
| Related lesson file | FA22_chi_squared_tests_lesson.md |
| Related lesson section | # 9. Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22ChiSquaredTestsMermaid-001 | Source: CCEA FA22-CHI2 specification + Dr Frost goodness-of-fit workflow evidence | Insert from mermaid/FA22ChiSquaredTestsMermaid-001.md | Purpose: Show the complete goodness-of-fit decision chain from model choice to final conclusion.]` |
| Source | CCEA FA22-CHI2 specification boundary + Dr Frost goodness-of-fit workflow evidence + teacher transcript |
| Purpose | Show the complete goodness-of-fit decision chain from model choice to final conclusion. |
| Status | Generated in Phase 2 |

## Mermaid code

```mermaid
flowchart TD
    A["Observed frequency data O_i"] --> B["Choose or read the prescribed theoretical model"]
    B --> C["State hypotheses"]
    C --> C1["H0: proposed model is suitable<br/>H1: proposed model is not suitable"]
    C1 --> D["Set significance level alpha"]
    D --> P{"Was a parameter estimated<br/>from the observed data?"}
    P -- "Yes" --> P1["Record one extra constraint<br/>Lose one additional degree of freedom"]
    P -- "No" --> P2["No extra parameter constraint"]
    P1 --> E["Calculate expected frequencies<br/>E_i = N p_i"]
    P2 --> E
    E --> F{"Any expected frequency<br/>less than 5?"}
    F -- "Yes" --> G["Combine adjacent or sensible classes<br/>Recalculate combined O and E"]
    G --> F
    F -- "No" --> H["Count final number of classes k<br/>after combining"]
    H --> I["Find degrees of freedom<br/>nu = k - number of constraints"]
    I --> J["Find upper-tail chi-squared<br/>critical value from table"]
    J --> K["Calculate test statistic<br/>X^2 = sum((O_i - E_i)^2 / E_i)"]
    K --> K2["Alternative calculation allowed<br/>X^2 = sum(O_i^2 / E_i) - N"]
    K2 --> L{"Is X^2 calculated<br/>greater than the critical value?"}
    L -- "Yes" --> M["Reject H0"]
    L -- "No" --> N["Do not reject H0"]
    M --> O["Context conclusion:<br/>sufficient evidence that the model is unsuitable"]
    N --> Q["Context conclusion:<br/>insufficient evidence that the model is unsuitable"]
```
