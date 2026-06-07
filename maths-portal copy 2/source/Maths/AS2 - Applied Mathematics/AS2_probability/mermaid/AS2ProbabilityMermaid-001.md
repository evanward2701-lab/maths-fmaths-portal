# AS2ProbabilityMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS2ProbabilityMermaid-001 |
| Asset type | Mermaid flowchart |
| Source | CCEA AS2 Probability specification map plus Phase 1 lesson plan |
| Related lesson section | Core Theory; Exam Technique Notes |
| Purpose | Help the student choose the right probability representation: sample-space table, Venn diagram, tree diagram or two-way table. |

```mermaid
flowchart TD
    A["Read the probability question carefully"] --> B{"Are there two simple experiments<br/>with equally likely outcomes?"}
    B -- "Yes" --> C["Use a sample-space table"]
    C --> C1["List all outcomes"]
    C1 --> C2["Count favourable outcomes"]
    C2 --> C3["Probability = favourable / total"]
    B -- "No" --> D{"Does the question combine event sets<br/>using and, or, not, neither, at least?"}
    D -- "Yes" --> E["Use a Venn diagram"]
    E --> E1["Draw the sample-space box"]
    E1 --> E2["Fill overlaps first if frequencies are given"]
    E2 --> E3["Use union, intersection and complement rules"]
    D -- "No" --> F{"Do events happen in succession?"}
    F -- "Yes" --> G["Use a tree diagram"]
    G --> G1["Put branch probabilities on each branch"]
    G1 --> G2["Multiply along each path"]
    G2 --> G3["Add separate successful paths"]
    F -- "No" --> H{"Are outcomes sorted by two categories?"}
    H -- "Yes" --> I["Use a two-way table"]
    I --> I1["Fill cells and totals"]
    I1 --> I2["Extract row, column and intersection probabilities"]
    I2 --> I3["Test independence if required"]
    H -- "No" --> J["Return to definitions"]
    J --> J1["Identify sample space, events and required probability"]
    E3 --> K["Check answer is between 0 and 1"]
    G3 --> K
    I3 --> K
    J1 --> K
    C3 --> K
```
