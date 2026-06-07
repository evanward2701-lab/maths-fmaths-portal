# AS2ProbabilityMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS2ProbabilityMermaid-003 |
| Asset type | Mermaid flowchart |
| Source | DrFrost three-set Venn diagram examples plus Phase 1 worked examples |
| Related lesson section | Venn Diagrams with Frequencies; Worked Examples; Common Mistakes and Exam Traps |
| Purpose | Show the centre-outwards method for filling a three-set Venn diagram. |

```mermaid
flowchart TD
    A["Start with the question data"] --> B["Draw the sample-space rectangle"]
    B --> C["Draw three overlapping event circles"]
    C --> D["Label the three events"]
    D --> E["Step 1: put the all-three value in the centre"]
    E --> F["Step 2: calculate each pairwise-only region"]
    F --> F1["Pairwise only = pairwise total minus all-three"]
    F1 --> G["Step 3: calculate each single-only region"]
    G --> G1["Single only = event total minus all regions already inside that event"]
    G1 --> H["Step 4: calculate the outside region"]
    H --> H1["Outside = grand total minus all regions inside the circles"]
    H1 --> I["Step 5: answer the probability question"]
    I --> I1["Probability = required frequency / grand total"]
    I1 --> J["Final check: all regions must add to the grand total"]
```
