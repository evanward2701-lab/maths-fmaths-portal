# A22StatisticalHypothesisTestingMERMAID-001

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-001
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Big Picture Explanation
- Source: CCEA specification map; lesson transcript; Stats Yr2 Chapter 1 PDF
- Purpose: Show how regression, correlation and hypothesis testing form a connected workflow.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart LR
    A["Bivariate data<br/>paired values of x and y"] --> B["Regression<br/>choose a model to explain or predict y from x"]
    A --> C["Correlation<br/>measure strength and direction of linear association"]
    C --> D["PMCC r<br/>sample correlation coefficient"]
    D --> E["Hypothesis test for correlation"]
    E --> F["Use H0: rho = 0"]
    E --> G["Choose H1<br/>rho > 0, rho < 0, or rho not equal 0"]
    G --> H["Compare r with critical value<br/>or use p-value"]
    H --> I["Conclusion in context"]
    B --> B1["Model example<br/>y = a + bx"]
    B --> B2["Non-linear support example<br/>y = kb^x"]
    B2 --> B3["Use logs to linearise<br/>log y = log k + x log b"]
    C --> C1["Positive correlation"]
    C --> C2["Negative correlation"]
    C --> C3["Weak or no linear correlation"]
    I --> I1["Reject H0<br/>evidence of correlation"]
    I --> I2["Do not reject H0<br/>insufficient evidence"]
```
