# AS2ProbabilityMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS2ProbabilityMermaid-002 |
| Asset type | Mermaid flowchart |
| Source | CCEA AS2 Probability specification map plus DrFrost independent-events evidence |
| Related lesson section | Independent and Dependent Events; Exam Technique Notes |
| Purpose | Show the exact decision process for testing whether two events are independent. |

```mermaid
flowchart TD
    A["Start: determine whether A and B are independent"] --> B["Find P(A)"]
    B --> C["Find P(B)"]
    C --> D["Find P(A and B)"]
    D --> E["Calculate P(A) x P(B)"]
    E --> F{"Is P(A and B) equal to P(A) x P(B)?"}
    F -- "Yes" --> G["A and B are independent"]
    F -- "No" --> H["A and B are not independent"]
    G --> I["Write a conclusion in words"]
    H --> I
    I --> J["Do not decide independence from the shape of the Venn diagram"]
    J --> K["Check that every probability used came from the correct region or total"]
```
