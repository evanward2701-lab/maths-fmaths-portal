# A22NormalDistributionMER-003

## Asset ID
`A22NormalDistributionMER-003`

## Source
CCEA `A22-HT-LO001`, `A22-HT-LO002`, and `A22-HT-LO004`; Phase 1 adjacent hypothesis-testing section.

## Related lesson section
`Core Theory Part 8: Hypothesis Testing on the Sample Mean`

## Purpose
Show the decision route for a hypothesis test for the mean of a normal distribution with known, given or assumed variance.

```mermaid
flowchart TD
    A["Hypothesis test for a normal mean"] --> B["Define the population mean mu"]
    B --> C["Write hypotheses"]
    C --> C1["H0: mu = claimed value"]
    C --> C2{"What does the alternative claim say?"}
    C2 -->|Mean is less| D1["H1: mu < claimed value. Lower-tail test"]
    C2 -->|Mean is greater| D2["H1: mu > claimed value. Upper-tail test"]
    C2 -->|Mean has changed| D3["H1: mu is not equal to claimed value. Two-tail test"]
    D1 --> E["State distribution under H0"]
    D2 --> E
    D3 --> E
    E --> F["If X ~ N(mu, sigma^2), then Xbar ~ N(mu, sigma^2 / n)"]
    F --> G["Calculate the p-value or critical region"]
    G --> H{"Using p-value method?"}
    H -->|Yes| I["Find probability of observed sample mean or more extreme"]
    I --> J{"Compare p-value with significance level alpha"}
    J -->|p <= alpha| K["Reject H0"]
    J -->|p > alpha| L["Do not reject H0"]
    H -->|No| M["Find critical value or critical region"]
    M --> N{"Does observed sample mean lie in critical region?"}
    N -->|Yes| K
    N -->|No| L
    K --> O["Write conclusion in context: sufficient evidence for H1"]
    L --> P["Write conclusion in context: insufficient evidence for H1"]
```
