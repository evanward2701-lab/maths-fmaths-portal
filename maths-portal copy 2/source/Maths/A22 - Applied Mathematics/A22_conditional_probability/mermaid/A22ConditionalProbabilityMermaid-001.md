# A22ConditionalProbabilityMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A22ConditionalProbabilityMermaid-001 |
| Unit | A22: A2 2 Applied Mathematics |
| Topic code | A22-PROB |
| Topic name | Conditional Probability |
| Topic ID | A22ConditionalProbability |
| Related lesson file | A22_conditional_probability_lesson.md |
| Related lesson section | Exam Technique Notes / Common CCEA-Style Wording / Visual and Interactive Asset Plan |
| Source | CCEA GCE Mathematics Specification Map, A22-PROB; Conditional Probability lesson PDF and transcript |
| Purpose | Provide a decision flow for choosing between conditional probability formula, Venn diagram, two-way table, tree diagram, independence test, mutually exclusive rule and modelling critique. |
| Linked LO IDs | A22-PROB-LO001, A22-PROB-LO002, A22-PROB-LO003 |
| Phase | Phase 2: Mermaid Diagrams |
| Status | Complete |

## Mermaid Code

```mermaid
flowchart TD
    A["Start: Read the probability question carefully"] --> B{"Does it say 'given that' or use P(A|B)?"}
    B -->|Yes| C["Identify the condition: the event after the vertical bar"]
    C --> D["Restrict the sample space to the condition"]
    D --> E{"What representation is given or easiest?"}
    E -->|Formula only| F["Use P(A|B) = P(A and B) / P(B)"]
    F --> F1["Numerator: both events happen"]
    F --> F2["Denominator: the given condition"]
    E -->|Venn diagram| G["Use the condition region as the denominator"]
    G --> G1["Favourable region = overlap with target event"]
    G1 --> G2["Conditional probability = favourable region / condition region"]
    E -->|Two-way table| H["Use the row or column named by the condition"]
    H --> H1["Denominator = row or column total"]
    H1 --> H2["Numerator = entry matching target and condition"]
    E -->|Tree diagram| I["Label later branches as conditional probabilities"]
    I --> I1["Multiply along a complete path"]
    I1 --> I2["Add mutually exclusive paths if needed"]
    B -->|No| J{"Does the question mention independence?"}
    J -->|Yes| K["Test independence"]
    K --> K1["Check P(A and B) = P(A)P(B)"]
    K --> K2["Or check P(A|B) = P(A)"]
    K1 --> K3["If equal: independent"]
    K2 --> K3
    K1 --> K4["If not equal: not independent"]
    K2 --> K4
    J -->|No| L{"Does the question mention mutually exclusive events?"}
    L -->|Yes| M["Use P(A and B) = 0"]
    M --> M1["Then P(A or B) = P(A) + P(B)"]
    L -->|No| N{"Does it ask for 'or' / union?"}
    N -->|Yes| O["Use P(A or B) = P(A) + P(B) - P(A and B)"]
    O --> O1["Subtract the overlap once"]
    N -->|No| P{"Does it ask about assumptions or realism?"}
    P -->|Yes| Q["Critique the model"]
    Q --> Q1["Question fairness, independence, equal likelihood or changing probabilities"]
    Q1 --> Q2["Explain likely effect of more realistic assumptions"]
    P -->|No| R["Return to event definitions and draw a diagram"]
    R --> R1["Define events clearly"]
    R1 --> R2["Choose Venn diagram, table or tree as a working model"]
    F2 --> S["Final answer: probability with correct notation and interpretation"]
    G2 --> S
    H2 --> S
    I2 --> S
    K3 --> S
    K4 --> S
    M1 --> S
    O1 --> S
    Q2 --> S
    R2 --> S
```
