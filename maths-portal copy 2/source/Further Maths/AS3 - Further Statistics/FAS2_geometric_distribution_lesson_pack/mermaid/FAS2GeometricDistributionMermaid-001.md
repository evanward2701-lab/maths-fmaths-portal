---
asset_id: FAS2GeometricDistributionMermaid-001
asset_type: mermaid
unit_code: FAS2
topic_code: FAS2-DIST
topic_slug: geometric_distribution
topic_pascal: GeometricDistribution
topic_id: FAS2GeometricDistribution
lesson_file: FAS2_geometric_distribution_lesson.md
related_lesson_section: "9. Visual Asset Integration"
used_placeholder: "[VISUAL PLACEHOLDER: FAS2GeometricDistributionMermaid-001 | Source: CCEA FAS2-DIST boundary + lesson evidence | Insert from mermaid/FAS2GeometricDistributionMermaid-001.md | Purpose: Help the student choose between binomial, geometric, Poisson boundary-link and excluded negative binomial.]"
source: "CCEA FAS2-DIST boundary + supplied FS1 geometric distribution evidence + ordinary A-Level Maths bridge context"
purpose: "Help the student choose between binomial, geometric, Poisson boundary-link and excluded negative binomial by asking what the random variable is counting."
creation_notes: "Poisson is included only as a boundary-link. Negative binomial is included only as an excluded/boundary-risk branch."
---

# FAS2GeometricDistributionMermaid-001

```mermaid
flowchart TD
    A["Start: What is the random variable counting?"] --> B{"Is the number of trials fixed first?"}
    B -- "Yes" --> C["Count the number of successes"]
    C --> D["Binomial bridge from ordinary AS2 Maths<br/>X ~ Bin(n,p)<br/>Possible values: 0,1,2,...,n"]
    D --> DNote["Use when wording says:<br/>'in 10 trials', 'out of n attempts', 'number of wins in n games'"]
    B -- "No" --> E{"Are you waiting until a success occurs?"}
    E -- "Yes, until the first success" --> F["Geometric distribution<br/>X ~ Geo(p)<br/>X = number of trials until first success"]
    F --> FCond["Required assumptions:<br/>1. Trials are independent<br/>2. Probability of success is fixed<br/>3. Each trial has success/failure outcomes<br/>4. Stop after first success"]
    F --> FFormula["Core formulae:<br/>P(X=x)=p(1-p)^(x-1)<br/>P(X≤x)=1-(1-p)^x<br/>P(X>x)=(1-p)^x<br/>E(X)=1/p<br/>Var(X)=(1-p)/p²"]
    E -- "Yes, until the rth success where r > 1" --> G["Negative binomial style situation"]
    G --> GWarn["Boundary-risk / excluded from this CCEA core lesson<br/>Appears in supplied FS1 evidence<br/>Not listed in supplied CCEA FAS2-DIST LO list"]
    E -- "No" --> H{"Are you counting events in a fixed interval?"}
    H -- "Yes" --> I["Poisson boundary-link<br/>X ~ Po(λ)<br/>Separate FAS2-DIST lesson"]
    H -- "No" --> J["Not enough information<br/>Define success, trials, independence and what X counts"]
    A --> K["First action in any exam question:<br/>Define X clearly in context"]
    K --> L["Then choose the distribution"]
```
