# A22StatisticalHypothesisTestingMERMAID-004

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-004
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Core Theory, Section 8: Critical value method for correlation tests
- Source: CCEA specification map; lesson transcript; Stats Yr2 Chapter 1 PDF
- Purpose: Give students a reusable decision flowchart for correlation coefficient hypothesis tests.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart TD
    A["Start correlation hypothesis test"] --> B["Write null hypothesis<br/>H0: rho = 0"]
    B --> C["Read the question wording"]
    C --> D{"What is being tested?"}
    D --> E["Positive correlation"]
    E --> E1["H1: rho > 0"]
    E1 --> E2["One-tailed upper test"]
    D --> F["Negative correlation"]
    F --> F1["H1: rho < 0"]
    F1 --> F2["One-tailed lower test"]
    D --> G["Any correlation"]
    G --> G1["H1: rho not equal 0"]
    G1 --> G2["Two-tailed test"]
    E2 --> H["Find n and significance level"]
    F2 --> H
    G2 --> H
    H --> I["Find correct critical value<br/>from correlation table"]
    I --> J["Compare sample r with critical value"]
    J --> K{"Is r in the critical region?"}
    K -->|Yes| L["Reject H0"]
    K -->|No| M["Do not reject H0"]
    L --> N["Write conclusion in context<br/>There is evidence of correlation"]
    M --> O["Write conclusion in context<br/>There is insufficient evidence of correlation"]
```
