# A22StatisticalHypothesisTestingMERMAID-005

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-005
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Exam Technique; Common Mistakes and Exam Traps
- Source: CCEA specification map; lesson transcript; Stats Yr2 Chapter 1 PDF
- Purpose: Compare positive, negative and two-tailed correlation tests so students choose the correct critical region.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart TD
    A["Choose alternative hypothesis"] --> B{"Form of H1"}
    B --> C["H1: rho > 0"]
    C --> C1["Positive one-tailed test"]
    C1 --> C2["Use positive critical value"]
    C2 --> C3["Reject H0 if<br/>r > positive critical value"]
    B --> D["H1: rho < 0"]
    D --> D1["Negative one-tailed test"]
    D1 --> D2["Use negative critical value"]
    D2 --> D3["Reject H0 if<br/>r < negative critical value"]
    B --> E["H1: rho not equal 0"]
    E --> E1["Two-tailed test"]
    E1 --> E2["Split significance level across two tails"]
    E2 --> E3["Reject H0 if<br/>r is less than negative critical value<br/>or greater than positive critical value"]
    E2 --> F["Example warning"]
    F --> G["For a 10 percent two-tailed test,<br/>use 5 percent in each tail"]
```
