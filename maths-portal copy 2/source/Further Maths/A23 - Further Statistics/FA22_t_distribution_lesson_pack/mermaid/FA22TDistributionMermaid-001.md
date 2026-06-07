# Mermaid Asset: FA22TDistributionMermaid-001

## Asset ID

`FA22TDistributionMermaid-001`

## Source

- CCEA Further Mathematics topic boundary: `FA22-TDIST`
- Learning outcomes:
  - `FA22-TDIST-LO001`
  - `FA22-TDIST-LO002`
  - `FA22-TDIST-LO003`
- Phase 1 lesson sections:
  - `# 8. Core Theory`
  - `# 9. Visual Asset Integration`
  - `# 15. Exam Technique Notes`
  - `# 16. Syllabus Gap Check`

## Related lesson section

`# 9.1 Distribution-choice flowchart`

## Used placeholder

```text
[VISUAL PLACEHOLDER: FA22TDistributionMermaid-001 | Source: CCEA FA22-TDIST learning outcomes + lesson evidence | Insert from mermaid/FA22TDistributionMermaid-001.md | Purpose: Help the student decide whether a question needs a one-sample t-test, paired t-test, two-sample pooled t-test or ordinary bridge z-test.]
```

## Purpose

This Mermaid diagram helps the student decide which statistical test is appropriate when a question involves a mean or a difference of means.

## Mermaid code

```mermaid
flowchart TD
    A["Start: Read the question carefully"] --> B{"Is the question about a population mean<br/>or a difference of population means?"}
    B -->|No| X["Not a FA22-TDIST t-test route<br/>Check another Statistics topic"]
    B -->|Yes| C{"Is the population standard deviation σ known?"}
    C -->|Yes| Z["Ordinary A-Level bridge route:<br/>use a z-test if other conditions are met<br/><br/>z = (x̄ - μ₀)/(σ/√n)"]
    C -->|No| D{"Is the sample small<br/>and is the population model normal?"}
    D -->|No, large sample or approximation context| L["Bridge / boundary warning:<br/>large-sample approximation may use s ≈ σ<br/>but this is not the core small-sample FA22-TDIST route"]
    D -->|Yes| E{"What is the data structure?"}
    E -->|One sample| F["One-sample t-test for μ<br/><br/>H₀: μ = μ₀<br/>t = (x̄ - μ₀)/(s/√n)<br/>ν = n - 1"]
    E -->|Paired measurements| G["Paired t-test<br/><br/>Define D = after - before<br/>H₀: μ_D = 0<br/>t = (d̄ - 0)/(s_D/√n)<br/>ν = n - 1"]
    E -->|Two independent samples| H{"Can the population variances<br/>be assumed equal?"}
    H -->|No| Y["Boundary warning:<br/>pooled CCEA route is not justified<br/>Do not silently use pooled variance"]
    H -->|Yes| I["Pooled two-sample t-test<br/><br/>H₀: μ_x - μ_y = Δ₀<br/>s_p² = ((n_x-1)s_x² + (n_y-1)s_y²)/(n_x+n_y-2)<br/>t = ((x̄-ȳ)-Δ₀)/(s_p√(1/n_x+1/n_y))<br/>ν = n_x+n_y-2"]
    F --> J{"Alternative hypothesis?"}
    G --> J
    I --> J
    J -->|Less than| K1["Left-tailed test<br/>critical region in left tail"]
    J -->|Greater than| K2["Right-tailed test<br/>critical region in right tail"]
    J -->|Different / changed| K3["Two-tailed test<br/>split α across both tails"]
    K1 --> M["Compare observed t with critical value<br/>then conclude in context"]
    K2 --> M
    K3 --> M
    M --> N["Final exam wording:<br/>Reject H₀ or do not reject H₀<br/>There is sufficient / insufficient evidence that ..."]
    classDef start fill:#FAF9F6,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef decision fill:#FFFFF0,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef core fill:#FAF9F6,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef bridge fill:#FBEFEF,stroke:#C5A059,stroke-width:1px,color:#2C2C2E;
    classDef warning fill:#FBEFEF,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef final fill:#FAF9F6,stroke:#E5E5EA,stroke-width:2px,color:#2C2C2E;
    class A start;
    class B,C,D,E,H,J decision;
    class F,G,I,K1,K2,K3 core;
    class Z,L bridge;
    class X,Y warning;
    class M,N final;
```
