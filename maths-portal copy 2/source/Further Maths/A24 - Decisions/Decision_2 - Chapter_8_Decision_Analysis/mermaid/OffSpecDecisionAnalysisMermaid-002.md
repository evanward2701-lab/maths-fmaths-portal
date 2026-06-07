# Mermaid Asset: OffSpecDecisionAnalysisMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-002 |
| Source | `transcripts.md`, decision trees versus probability trees warning |
| Related lesson section | Section 5; Section 8; Section 12 |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-002 | Source: transcripts.md + ordinary A-Level Maths bridge | Insert from mermaid/OffSpecDecisionAnalysisMermaid-002.md | Purpose: Compare probability-tree thinking with decision-tree thinking.]` |
| Purpose | Prevent the classic trap: putting probabilities on decision branches. |

## Mermaid code

```mermaid
flowchart TB
    START["Tree diagram thinking"] --> P["Ordinary probability tree"]
    START --> D["Decision tree"]
    P --> P1["Every branch usually represents<br/>a random outcome"]
    P1 --> P2["Probabilities are written<br/>on outcome branches"]
    P2 --> P3["Question asks:<br/>What is the probability?"]
    D --> D1["Some branches represent<br/>choices"]
    D1 --> D2["Decision branches have<br/>no probability"]
    D2 --> D3["Only chance branches<br/>carry probabilities"]
    D3 --> D4["Question asks:<br/>Which strategy is best?"]
    D4 --> WARNING["Warning:<br/>Do not put probabilities<br/>after a decision box"]
    classDef bridge fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef prob fill:#FFFFF0,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef decision fill:#FBEFEF,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef warning fill:#FBEFEF,stroke:#C5A059,stroke-width:3px,color:#2C2C2E;
    class START bridge;
    class P,P1,P2,P3 prob;
    class D,D1,D2,D3,D4 decision;
    class WARNING warning;
```
