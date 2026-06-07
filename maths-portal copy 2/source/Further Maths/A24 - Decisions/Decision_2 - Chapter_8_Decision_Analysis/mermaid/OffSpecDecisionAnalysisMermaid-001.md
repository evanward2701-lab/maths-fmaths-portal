# Mermaid Asset: OffSpecDecisionAnalysisMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-001 |
| Source | `transcripts.md`, Decision Analysis 1, node-shape and decision-tree method explanation |
| Related lesson section | Section 7: Key Definitions and Notation; Section 8: Core Theory |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-001 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-001.md | Purpose: Summarise the decision-tree node grammar.]` |
| Purpose | Show the core diagram grammar: decision node, chance node, end/pay-off node, probabilities, pay-offs and EMV placement. |

## Mermaid code

```mermaid
flowchart LR
    A["Decision node<br/>Box or rectangle<br/>A choice is made"] -->|Decision branch<br/>no probability| B(("Chance node<br/>Circle<br/>random event"))
    A -->|Alternative decision<br/>no probability| E["◁ End/pay-off node<br/>Pay-off written next to it"]
    B -->|Probability p<br/>Outcome 1| C["◁ End/pay-off node<br/>Pay-off x1"]
    B -->|Probability 1-p<br/>Outcome 2| D["◁ End/pay-off node<br/>Pay-off x2"]
    C --> F["EMV at chance node:<br/>p x1 + (1-p) x2"]
    D --> F
    F --> G["Best value written<br/>back into decision box"]
    classDef decision fill:#FAF9F6,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef chance fill:#FFFFF0,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef payoff fill:#FBEFEF,stroke:#E5E5EA,stroke-width:2px,color:#2C2C2E;
    classDef calc fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    class A decision;
    class B chance;
    class C,D,E payoff;
    class F,G calc;
```
