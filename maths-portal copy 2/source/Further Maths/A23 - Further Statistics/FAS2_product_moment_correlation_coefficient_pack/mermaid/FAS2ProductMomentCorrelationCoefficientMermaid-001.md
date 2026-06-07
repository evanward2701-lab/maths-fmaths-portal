# FAS2ProductMomentCorrelationCoefficientMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2ProductMomentCorrelationCoefficientMermaid-001` |
| Unit | `FAS2` |
| Topic code | `FAS2-BIV` |
| Topic ID | `FAS2ProductMomentCorrelationCoefficient` |
| Related lesson file | `FAS2_product_moment_correlation_coefficient_lesson.md` |
| Related lesson section | `# 9. Visual Asset Integration`; supports `# 8. Core Theory`, `# 11. Worked Examples`, `# 15. Exam Technique Notes` |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientMermaid-001 | Source: CCEA FAS2-BIV-LO001 + transcript PMCC method | Insert from mermaid/FAS2ProductMomentCorrelationCoefficientMermaid-001.md | Purpose: Show the full PMCC calculation workflow from bivariate data to interpretation. Description: Flowchart should show paired data, summary statistics, calculation of Sxx/Syy/Sxy, calculation of r, then interpretation and limitation check.]` |
| Source | CCEA FAS2-BIV-LO001 + teacher transcript PMCC method + lesson Phase 1 core theory |
| Purpose | Show the full PMCC calculation workflow from paired bivariate data to final interpretation and limitation checks. |
| Creation notes | This is a teaching workflow diagram. It preserves the core PMCC method from the lesson: start with paired observations, compute summary statistics, calculate corrected sums, compute \(r\), interpret direction/strength, then check limitations. Spearman’s rank and hypothesis testing are deliberately excluded because Phase 1 logged them as boundary-risk/enrichment, not core CCEA FAS2 PMCC content. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with bivariate data<br/>(x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)"] --> B["Identify variables<br/>x = first measured variable<br/>y = second measured variable<br/>n = number of paired observations"]
    B --> C["Calculate summary statistics<br/>Σx, Σy, Σx², Σy², Σxy"]
    C --> D["Calculate corrected x-spread<br/>Sxx = Σx² − (Σx)² / n"]
    C --> E["Calculate corrected y-spread<br/>Syy = Σy² − (Σy)² / n"]
    C --> F["Calculate corrected co-variation<br/>Sxy = Σxy − (Σx)(Σy) / n"]
    D --> G["Check denominator is valid<br/>Sxx > 0 and Syy > 0"]
    E --> G
    F --> G
    G --> H{"Can PMCC be calculated?"}
    H -->|No| I["Stop and check data<br/>One variable may have no variation<br/>or a summary statistic may be wrong"]
    H -->|Yes| J["Calculate PMCC<br/>r = Sxy / √(Sxx Syy)"]
    J --> K["Check range<br/>−1 ≤ r ≤ 1"]
    K --> L{"Sign of r"}
    L -->|r > 0| M["Positive linear correlation<br/>larger x tends to go with larger y"]
    L -->|r < 0| N["Negative linear correlation<br/>larger x tends to go with smaller y"]
    L -->|r ≈ 0| O["Little or no linear correlation<br/>but non-linear patterns may still exist"]
    M --> P{"Magnitude of r"}
    N --> P
    O --> P
    P -->|r close to 1 or −1| Q["Strong linear correlation<br/>points lie close to a straight line"]
    P -->|r not close to 1 or −1| R["Weak/moderate linear correlation<br/>points are more scattered"]
    Q --> S["Interpret in context<br/>Use variable names and direction"]
    R --> S
    S --> T["Limitation check"]
    T --> U["Do not say r is gradient<br/>r measures closeness to a straight line, not steepness"]
    T --> V["Do not claim causation<br/>correlation does not prove cause"]
    T --> W["Do not ignore non-linear patterns<br/>r measures linear correlation only"]
    T --> X["Do not assume extrapolation is safe<br/>strong r only describes observed range"]
    U --> Y["Final exam-style conclusion"]
    V --> Y
    W --> Y
    X --> Y
    Y["Example conclusion:<br/>There is a strong positive linear correlation between x and y.<br/>This does not prove causation."]
```
