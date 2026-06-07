# A22StatisticalHypothesisTestingMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `A22StatisticalHypothesisTestingMermaid-001` |
| Asset type | Mermaid flowchart |
| Unit code | `A22` |
| Topic code | `A22-HT` |
| Topic name | Statistical hypothesis testing |
| Lesson file | `A22_statistical_hypothesis_testing_lesson.md` |
| Related lesson section | Core Theory: Choosing the direction of the test |
| Related LO IDs | `A22-HT-LO001`, `A22-HT-LO003` |
| Source | CCEA Specification Map; Chapter 7 Hypothesis Testing Binomial transcript |
| Purpose | Help the student choose between a lower-tailed, upper-tailed or two-tailed binomial hypothesis test. |

## Mermaid code

```mermaid
flowchart TD
    A["Start: read the context carefully"] --> B["Identify the claimed probability k"]
    B --> C["Write the null hypothesis<br/>H0: p = k"]
    C --> D{"What does the question suggest?"}
    D -->|"Lower, less, overestimating,<br/>fewer successes than expected"| E["Use lower-tailed test<br/>H1: p &lt; k"]
    D -->|"Higher, greater, improvement,<br/>more successes than expected"| F["Use upper-tailed test<br/>H1: p &gt; k"]
    D -->|"Different, changed, biased either way,<br/>not equal to claimed value"| G["Use two-tailed test<br/>H1: p ≠ k"]
    E --> H["Define test statistic<br/>X = number of successes"]
    F --> H
    G --> H
    H --> I["Assume H0 is true<br/>X ~ B(n, k)"]
    I --> J{"Which tail probability is needed?"}
    J -->|"H1: p &lt; k"| K["Calculate lower tail<br/>P(X ≤ observed x)"]
    J -->|"H1: p &gt; k"| L["Calculate upper tail<br/>P(X ≥ observed x)<br/>= 1 - P(X ≤ x - 1)"]
    J -->|"H1: p ≠ k"| M["Use two-tailed logic<br/>compare relevant tail with half the significance level"]
    K --> N{"Is probability less than<br/>the significance level?"}
    L --> N
    M --> O{"Is relevant tail probability less than<br/>half the significance level?"}
    N -->|"Yes"| P["Reject H0"]
    N -->|"No"| Q["Do not reject H0"]
    O -->|"Yes"| P
    O -->|"No"| Q
    P --> R["Write contextual conclusion:<br/>there is evidence for H1"]
    Q --> S["Write contextual conclusion:<br/>there is not enough evidence to reject H0"]
```
