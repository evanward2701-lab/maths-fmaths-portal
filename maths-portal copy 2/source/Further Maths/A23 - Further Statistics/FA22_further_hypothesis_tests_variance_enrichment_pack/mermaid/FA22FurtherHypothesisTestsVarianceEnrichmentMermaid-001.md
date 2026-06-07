# Mermaid Asset: FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| `asset_id` | `FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001` |
| `unit_code` | `FA22` |
| `topic_id` | `FA22FurtherHypothesisTestsVarianceEnrichment` |
| `topic_slug` | `further_hypothesis_tests_variance_enrichment` |
| `asset_type` | Mermaid diagram |
| `related_lesson_file` | `FA22_further_hypothesis_tests_variance_enrichment_lesson.md` |
| `related_lesson_section` | Section 9: Visual Asset Integration |
| `used_placeholder` | `[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001 | Source: Lesson synthesis from transcript and bridge context | Insert from mermaid/FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001.md | Purpose: Decision tree for choosing between S² calculation, χ² variance confidence interval, one-variance χ² test and two-variance F-test.]` |
| `source` | Lesson synthesis from teacher transcript and ordinary A-Level Maths bridge context |
| `source_status` | Off-spec enrichment evidence, not CCEA core |
| `purpose` | Decision tree for choosing between \(S^2\) calculation, \(\chi^2\) variance confidence interval, one-variance \(\chi^2\) test and two-variance \(F\)-test |
| `visual_style_note` | Luxury-minimalist palette to be applied in later rendered versions: ivory/cream background, muted dividers, gold accents, dark mathematical text |

## Creation Notes

This Mermaid diagram is a method-selection map for the off-spec enrichment lesson.

It preserves the key boundary:

- the CCEA-safe overlap is calculating \(S^2\) as an unbiased estimator of \(\sigma^2\);
- \(\chi^2\) variance confidence intervals, one-variance \(\chi^2\) tests, \(F\)-distribution theory and \(F\)-tests are enrichment only.

## Mermaid Code

```mermaid
flowchart TD
    A["Start: What is the statistical question?"] --> B{"Are you only calculating a sample estimate of variance?"}

    B -->|"Yes"| C["Use the unbiased sample variance<br/>S^2 = sum((X_i - Xbar)^2) / (n - 1)"]
    C --> C1["CCEA-safe overlap:<br/>point estimate of population variance sigma^2"]
    C1 --> C2["Stop here for core CCEA boundary"]

    B -->|"No"| D{"Is this enrichment inference about variance?"}

    D -->|"No"| E["Use the correct CCEA topic instead:<br/>mean CI, t-test, chi-squared goodness-of-fit, or independence"]
    D -->|"Yes"| F["Off-spec enrichment route<br/>Requires normal population assumptions"]

    F --> G{"How many samples?"}

    G -->|"One sample"| H{"What do you want?"}

    H -->|"Confidence interval for sigma^2"| I["Use chi-squared variance interval"]
    I --> I1["Known result:<br/>(n - 1)S^2 / sigma^2 ~ chi-square with n - 1 df"]
    I1 --> I2["For 95% CI:<br/>(n - 1)S^2 / chi-square(0.025)<br/> &lt; sigma^2 &lt;<br/>(n - 1)S^2 / chi-square(0.975)"]
    I2 --> I3["Warning:<br/>upper-tail table values make 0.025 the large critical value"]

    H -->|"Hypothesis test for sigma^2"| J["Use one-variance chi-squared test"]
    J --> J1["State hypotheses:<br/>H0: sigma^2 = sigma0^2"]
    J1 --> J2["Choose alternative:<br/>sigma^2 > sigma0^2, sigma^2 < sigma0^2, or sigma^2 != sigma0^2"]
    J2 --> J3["Test statistic:<br/>T = (n - 1)S^2 / sigma0^2"]
    J3 --> J4["Under H0:<br/>T ~ chi-square with n - 1 df"]
    J4 --> J5["Compare with critical region<br/>then conclude in context"]

    G -->|"Two independent samples"| K{"Are you comparing variances?"}

    K -->|"No"| L["This may be a test about means instead:<br/>consider two-sample t-test or other relevant method"]
    K -->|"Yes"| M["Use F-test for two variances"]
    M --> M1["State hypotheses:<br/>H0: sigma1^2 = sigma2^2"]
    M1 --> M2["Choose numerator to match the alternative where possible"]
    M2 --> M3["Test statistic:<br/>F = S1^2 / S2^2"]
    M3 --> M4["Under H0:<br/>F ~ F with df (n1 - 1, n2 - 1)"]
    M4 --> M5["Order matters:<br/>numerator variance gives first df"]
    M5 --> M6["For lower-tail values:<br/>switch df, take reciprocal, reverse inequality"]
    M6 --> M7["Compare with critical region<br/>then conclude in context"]

    F --> N["Assumption checkpoint"]
    N --> N1["One-sample chi-squared variance methods:<br/>random sample from a normal population"]
    N --> N2["F-test:<br/>two independent random samples from normal populations"]
    N --> N3["Use S^2 with denominator n - 1"]

    C2 -.-> O["Boundary reminder:<br/>Do not treat enrichment routes as required CCEA content"]
    I3 -.-> O
    J5 -.-> O
    M7 -.-> O
```

## Accessibility Description

This flowchart begins with the question “What is the statistical question?” It first separates the CCEA-safe task of calculating the unbiased sample variance \(S^2\) from the off-spec enrichment tasks. The enrichment branch splits into one-sample and two-sample routes. The one-sample route splits again into confidence intervals for \(\sigma^2\) and hypothesis tests for \(\sigma^2\), both using the \(\chi^2\) distribution with \(n-1\) degrees of freedom. The two-sample route leads to the \(F\)-test for comparing population variances, using \(F=S_1^2/S_2^2\) with degrees of freedom \(n_1-1\) and \(n_2-1\). A final assumption checkpoint reminds the student that normality and correct use of \(S^2\) are required, and that the whole inference route is enrichment rather than CCEA core.

## Off-Spec Boundary Note

This asset supports an enrichment lesson only. It must not be used to imply that \(\chi^2\) variance confidence intervals, one-variance \(\chi^2\) tests, the \(F\)-distribution or \(F\)-tests are required CCEA FA22 content unless official CCEA evidence is later supplied.
