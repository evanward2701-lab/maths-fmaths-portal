# Mermaid Asset: FA22CentralLimitTheoremMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA22CentralLimitTheoremMermaid-001` |
| Unit | `FA22` |
| Topic ID | `FA22CentralLimitTheorem` |
| Related lesson file | `FA22_central_limit_theorem_lesson.md` |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22CentralLimitTheoremMermaid-001 | Source: CCEA Further Maths specification + transcript method checklist | Insert from mermaid/FA22CentralLimitTheoremMermaid-001.md | Purpose: Give students an exam workflow for deciding when and how to use CLT.]` |
| Purpose | Exam workflow for deciding when and how to use CLT. |

```mermaid
flowchart TD
    A["Read the question"] --> B{"Is it about a mean or average?"}
    B -- "No" --> C["CLT may not be needed"]
    B -- "Yes" --> D["Define original random variable X"]
    D --> E["Find mu = E(X)"]
    E --> F["Find sigma squared = Var(X)"]
    F --> G["Identify sample size n"]
    G --> H{"Can we use a normal model for X-bar?"}
    H -- "n >= 30" --> I["Use CLT"]
    H -- "X already normal" --> J["X-bar is normal even for smaller n"]
    H -- "n < 30 and X not normal" --> K["Do not assume CLT is reliable"]
    I --> L["X-bar approx N(mu, sigma squared / n)"]
    J --> L
    L --> M["Calculator SD = sqrt(sigma squared / n)"]
    M --> N{"Question type?"}
    N -- "Probability" --> O["Use normal CDF"]
    N -- "Threshold" --> P["Use inverse normal"]
    N -- "Minimum n" --> Q["Standardise: Z = (X-bar - mu)/(sigma/sqrt(n))"]
    Q --> R["Use inverse normal critical z"]
    R --> S["Solve inequality in n"]
    S --> T["Round up to smallest valid integer"]
    O --> U["Interpret in context"]
    P --> U
    T --> U
    U --> V["Final check: X-bar not X; SD not variance"]
```
