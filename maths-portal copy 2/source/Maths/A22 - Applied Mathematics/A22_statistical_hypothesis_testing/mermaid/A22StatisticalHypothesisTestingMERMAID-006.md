# A22StatisticalHypothesisTestingMERMAID-006

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-006
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Exam Technique; Full Worked Solutions
- Source: CCEA specification map; lesson transcript; Stats Yr2 Chapter 1 PDF
- Purpose: Show the required two-part conclusion structure: statistical decision plus contextual interpretation.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart TD
    A["After comparing r with the critical value"] --> B{"Decision"}
    B --> C["r is in the critical region"]
    C --> C1["Reject H0"]
    C1 --> C2["Context sentence:<br/>There is evidence of correlation"]
    C2 --> C3["Include direction if relevant:<br/>positive or negative"]
    B --> D["r is not in the critical region"]
    D --> D1["Do not reject H0"]
    D1 --> D2["Context sentence:<br/>There is insufficient evidence of correlation"]
    D2 --> D3["Do not say H0 is proven true"]
    C3 --> E["Final answer complete"]
    D3 --> E
    E --> F["Exam polish"]
    F --> G["Mention significance level"]
    F --> H["Mention variables from the question"]
    F --> I["Use population wording carefully"]
```
