# Mermaid Asset: OffSpecDecisionAnalysisMermaid-006

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-006 |
| Source | `transcripts.md`, utility theory explanation of risk aversion and parameter R |
| Related lesson section | Section 8; Section 15 |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-006 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-006.md | Purpose: Summarise how the risk parameter R affects utility decisions.]` |
| Purpose | Explain the interpretation of R in utility modelling. |

## Mermaid code

```mermaid
flowchart TB
    A["Utility model<br/>U(x) = 1 - e^(-x/R)"] --> B["x is the monetary pay-off"]
    A --> C["R is positive"]
    C --> D{"Size of R?"}
    D -->|Smaller R| E["More risk averse"]
    E --> F["Losses make utility<br/>very negative very quickly"]
    F --> G["Decision-maker avoids<br/>risky losses"]
    D -->|Larger R| H["More willing to take risk"]
    H --> I["Losses are still bad,<br/>but utility falls less sharply"]
    I --> J["Risky options may remain attractive"]
    B --> K["Positive x:<br/>profit or gain"]
    B --> L["Negative x:<br/>loss"]
    L --> M["For risk-averse models,<br/>losses can dominate the decision"]
    classDef model fill:#FFFFF0,stroke:#C5A059,stroke-width:3px,color:#2C2C2E;
    classDef idea fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef risk fill:#FBEFEF,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef decision fill:#FFFFF0,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    class A model; class B,C,K,L,M idea; class D decision; class E,F,G,H,I,J risk;
```
