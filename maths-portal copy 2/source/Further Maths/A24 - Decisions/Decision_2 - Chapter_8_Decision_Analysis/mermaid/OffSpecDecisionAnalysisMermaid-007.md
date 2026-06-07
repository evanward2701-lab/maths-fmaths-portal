# Mermaid Asset: OffSpecDecisionAnalysisMermaid-007

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | OffSpecDecisionAnalysisMermaid-007 |
| Source | `transcripts.md`, school fair EMV and utility motivation |
| Related lesson section | Section 8; Section 11 Worked Examples 3 and 4 |
| Used placeholder | `[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-007 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-007.md | Purpose: Show why positive EMV does not always settle a risky decision.]` |
| Purpose | Explain why positive EMV may still be rejected by a risk-averse organisation. |

## Mermaid code

```mermaid
flowchart TB
    A["School fair game"] --> B["400 players expected<br/>£1 each"]
    A --> C["Prize if six dice<br/>all show sixes"]
    C --> D["Only one £2000 prize paid<br/>even if multiple winners"]
    B --> E["If no prize claimed:<br/>pay-off = +400"]
    D --> F["If prize claimed:<br/>pay-off = 400 - 2000 = -1600"]
    E --> G["Calculate EMV<br/>using probabilities"]
    F --> G
    G --> H["EMV is positive<br/>so EMV may suggest:<br/>offer the game"]
    H --> I["But one bad outcome<br/>means losing £1600"]
    I --> J["School is likely risk averse"]
    J --> K["Use expected utility<br/>instead of only EMV"]
    K --> L["Transform pay-offs:<br/>x -> U(x)"]
    L --> M["Compare expected utilities"]
    M --> N["Final decision depends<br/>on risk attitude"]
    classDef scenario fill:#FFFFF0,stroke:#C5A059,stroke-width:2px,color:#2C2C2E;
    classDef payoff fill:#FBEFEF,stroke:#E5E5EA,stroke-width:2px,color:#2C2C2E;
    classDef calc fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef risk fill:#FBEFEF,stroke:#D4AF37,stroke-width:3px,color:#2C2C2E;
    class A,B,C,D scenario; class E,F payoff; class G,H,K,L,M,N calc; class I,J risk;
```
