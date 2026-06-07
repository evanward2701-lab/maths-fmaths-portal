# Mermaid Asset: OffSpecDecisionAnalysisMermaid-003

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-003 |
| Source | `transcripts.md`, James tetrahedral dice worked example |
| Related lesson section | Section 11 Worked Example 1 |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-003 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-003.md | Purpose: Show James’s play/not-play EMV decision tree.]` |
| Purpose | Represent the James example with probabilities, pay-offs, EMV and rejected branch. |

## Mermaid code

```mermaid
flowchart LR
    D0["Decision node<br/>James chooses"] -->|p: play| C1(("Chance node<br/>EMV = 0.25"))
    D0 -->|~p: do not play<br/>rejected after EMV comparison| E0["◁ End/pay-off<br/>0"]
    C1 -->|Total 6 or more<br/>3/8| E1["◁ End/pay-off<br/>+4"]
    C1 -->|Less than 6<br/>5/8| E2["◁ End/pay-off<br/>-2"]
    E1 --> CALC["EMV(play)<br/>= (3/8)(4) + (5/8)(-2)<br/>= 1/4 = 0.25"]
    E2 --> CALC
    CALC --> CHOOSE["Compare at decision node:<br/>play = 0.25<br/>do not play = 0<br/>Choose play"]
    classDef decision fill:#FAF9F6,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef chance fill:#FFFFF0,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef payoff fill:#FBEFEF,stroke:#E5E5EA,stroke-width:2px,color:#2C2C2E;
    classDef calc fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef choice fill:#FFFFF0,stroke:#C5A059,stroke-width:3px,color:#2C2C2E;
    class D0 decision; class C1 chance; class E0,E1,E2 payoff; class CALC calc; class CHOOSE choice;
```
