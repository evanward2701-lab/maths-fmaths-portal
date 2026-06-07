# FA22SamplingAndEstimationMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | FA22SamplingAndEstimationMermaid-001 |
| Asset type | Mermaid diagram |
| Unit | FA22 – Further A2 2 Applied Mathematics |
| Topic code | FA22-EST |
| Topic name | Sampling and estimation |
| Related lesson file | FA22_sampling_and_estimation_lesson.md |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22SamplingAndEstimationMermaid-001 ...]` |
| Source | CCEA FA22-EST specification map + teacher transcript + supplied estimation/confidence interval PDF |
| Purpose | Show the conceptual flow from population parameters to sample observations, estimators, bias, standard error, CLT and confidence intervals. |

## Mermaid code

```mermaid
flowchart TD
    A["Population<br/>fixed but usually unknown"] --> B["Parameters<br/>μ, σ, σ²"]
    A --> C["Random sample"]
    C --> D["X₁, X₂, ..., Xₙ"]
    D --> E["Sample-only statistics"]
    E --> F["X̄ = (X₁ + ... + Xₙ)/n"]
    E --> G["S² = Σ(Xᵢ − X̄)²/(n − 1)"]
    F --> H["Estimator for μ"]
    G --> I["Estimator for σ²"]
    H --> J["Bias(T)=E(T)−θ"]
    I --> J
    J --> K["Unbiased if E(T)=θ"]
    H --> L["E(X̄)=μ"]
    L --> M["Var(X̄)=σ²/n"]
    M --> N["SE(X̄)=σ/√n"]
    D --> O["CLT for n ≥ 30"]
    O --> P["X̄ ≈ N(μ, σ²/n)"]
    P --> Q["z critical value"]
    N --> Q
    Q --> R["CI for μ:<br/>x̄ ± zσ/√n"]
    R --> S["Interpret in context"]
    B -. "target" .-> H
    B -. "target" .-> I

    classDef population fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E,stroke-width:2px;
    classDef sample fill:#FFFFF0,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1.5px;
    classDef estimator fill:#FBEFEF,stroke:#D4AF37,color:#2C2C2E,stroke-width:1.5px;
    classDef inference fill:#FAF9F6,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    class A,B population;
    class C,D,E,F,G sample;
    class H,I,J,K,L,M,N estimator;
    class O,P,Q,R,S inference;
```

## Accessibility notes

The diagram uses text labels rather than colour alone. Dotted arrows show that estimators aim at unknown target parameters but are calculated from sample data only.
