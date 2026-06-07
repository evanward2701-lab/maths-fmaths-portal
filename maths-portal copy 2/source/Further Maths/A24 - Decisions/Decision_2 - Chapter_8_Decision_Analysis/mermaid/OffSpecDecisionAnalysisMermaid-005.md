# Mermaid Asset: OffSpecDecisionAnalysisMermaid-005

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-005 |
| Source | `transcripts.md`, utility function theory and expected utility explanation |
| Related lesson section | Section 8; Section 11; Section 12 |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-005 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-005.md | Purpose: Show the workflow from monetary pay-offs to expected utility.]` |
| Purpose | Show how utility modifies the ordinary EMV workflow. |

## Mermaid code

```mermaid
flowchart TB
    A["Start with a completed decision tree"] --> B["Read monetary pay-offs<br/>x1, x2, ..., xn"]
    B --> C["Choose or use given utility function<br/>U(x)"]
    C --> D["Transform each pay-off:<br/>x1 -> U(x1)<br/>x2 -> U(x2)<br/>...<br/>xn -> U(xn)"]
    D --> E["Use the same probabilities<br/>from chance branches"]
    E --> F["Calculate expected utility:<br/>p1 U(x1) + p2 U(x2) + ... + pn U(xn)"]
    F --> G["Write expected utility<br/>inside the chance node"]
    G --> H["At a decision node,<br/>choose the greatest expected utility"]
    H --> I["Cross off rejected<br/>decision branches only"]
    I --> J["State the strategy in words"]
    B --> WARNING1["Do not compare raw pounds<br/>with utils"]
    H --> WARNING2["Do not cross off<br/>chance branches"]
    classDef step fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef key fill:#FFFFF0,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef warning fill:#FBEFEF,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    class A,B,C,D,E,G,H,I,J step; class F key; class WARNING1,WARNING2 warning;
```
