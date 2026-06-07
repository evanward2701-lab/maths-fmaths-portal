# Mermaid Asset: FAS2PoissonDistributionMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2PoissonDistributionMermaid-001` |
| Topic ID | `FAS2PoissonDistribution` |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Topic name | Statistical distributions: Poisson Distribution |
| Related lesson file | `FAS2_poisson_distribution_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration; Section 8.9: Modelling assumptions; Section 8.10: Deciding whether Poisson is suitable |
| Source | CCEA FAS2-DIST boundary + lesson evidence from `FS1-Chp2-PoissonDistribution.pdf` and `transcripts.md` |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS2PoissonDistributionMermaid-001 | Source: CCEA FAS2-DIST boundary + lesson evidence | Insert from mermaid/FAS2PoissonDistributionMermaid-001.md | Purpose: Decision flowchart for choosing Poisson: count variable, fixed interval, average rate, singly, independently, constant rate.]` |
| Purpose | Decision flowchart for choosing whether a Poisson distribution is suitable. |
| Status | Generated in Phase 2 |

## Creation notes

This Mermaid diagram is designed as a syllabus-bound model-selection flowchart.

It checks the key Poisson modelling conditions preserved in the lesson:

1. The random variable counts events.
2. The events occur in a fixed interval of time, length, area, volume or space.
3. An average rate or mean number of events is known.
4. The rate can be scaled to match the interval in the question.
5. Events occur singly.
6. Events occur independently.
7. Events occur at a constant rate.

The diagram also preserves the lesson warning that a question may switch from Poisson to Binomial if the random variable changes from counting events to counting successful intervals.

## Mermaid code

```mermaid
flowchart TD
    A["Start: Read the question carefully"] --> B{"What is the random variable counting?"}

    B -->|Events in an interval| C{"Is the interval fixed?"}
    B -->|Successes out of fixed trials| D["Use Binomial thinking instead<br/>Example: X ~ B(n,p)"]
    B -->|Measurements, times, masses, lengths| E["Poisson is not suitable<br/>Poisson counts whole-number events only"]

    C -->|Yes| F{"Is an average rate or mean number of events given?"}
    C -->|No| G["Poisson is not suitable yet<br/>Define the interval first"]

    F -->|Yes| H["Identify lambda, λ<br/>λ = mean number of events<br/>in the chosen interval"]
    F -->|No| I["Poisson may not be possible<br/>A rate or mean is needed"]

    H --> J{"Does λ match the interval in the question?"}

    J -->|Yes| K["Keep λ as given"]
    J -->|No| L["Scale the rate<br/>λ_new = λ_old × interval multiplier"]

    K --> M{"Do events occur singly?"}
    L --> M

    M -->|Yes| N{"Are events independent?"}
    M -->|No| O["Poisson model is doubtful<br/>Multiple simultaneous events break the model"]

    N -->|Yes| P{"Is the rate constant?"}
    N -->|No| Q["Poisson model is doubtful<br/>One event affects another"]

    P -->|Yes| R["Poisson model is suitable<br/>Write X ~ Po(λ)"]
    P -->|No| S["Poisson model is doubtful<br/>Rate changes across the interval"]

    R --> T{"What probability is required?"}

    T -->|Exact value| U["Use Poisson PD or formula<br/>P(X=x)=e^(-λ)λ^x / x!"]
    T -->|Lower tail| V["Use cumulative probability<br/>P(X≤k)"]
    T -->|Upper tail| W["Use complement<br/>P(X≥k)=1-P(X≤k-1)"]
    T -->|Strict inequality| X["Convert carefully because X is discrete<br/>X<5 means X≤4<br/>X>6 means X≥7"]
    T -->|Interval probability| Y["Subtract cumulative probabilities<br/>P(a≤X≤b)=P(X≤b)-P(X≤a-1)"]

    U --> Z["Interpret answer in context"]
    V --> Z
    W --> Z
    X --> Z
    Y --> Z

    Z --> AA{"Does the question now count successful intervals?"}
    AA -->|Yes| AB["Switch to Binomial<br/>Y ~ B(n,p), where p came from Poisson"]
    AA -->|No| AC["Continue with Poisson model"]

    AB --> AD["Final answer with context"]
    AC --> AD
```

## Accessibility notes

- The diagram is text-first and does not rely on colour.
- Every decision node is written as a question.
- Every terminal warning gives the reason Poisson may be unsuitable.
- The flow explicitly separates Poisson event-counting from Binomial fixed-trial counting.
