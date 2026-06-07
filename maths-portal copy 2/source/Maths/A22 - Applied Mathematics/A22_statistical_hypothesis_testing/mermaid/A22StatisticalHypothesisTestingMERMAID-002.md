# A22StatisticalHypothesisTestingMERMAID-002

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-002
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Core Theory, Section 3: Turning an exponential model into a straight-line model
- Source: Lesson transcript; Stats Yr2 Chapter 1 PDF pages on exponential regression; AS1 exponentials/logarithms support
- Purpose: Preserve the algebraic pathway from an exponential model to a straight-line model.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart TD
    A["Start with exponential model<br/>y = kb^x"] --> B["Take logs of both sides"]
    B --> C["log y = log(kb^x)"]
    C --> D["Use product law<br/>log(AB) = log A + log B"]
    D --> E["log y = log k + log(b^x)"]
    E --> F["Use power law<br/>log(b^x) = x log b"]
    F --> G["log y = log k + x log b"]
    G --> H["Straight-line form"]
    H --> I["Vertical variable: log y"]
    H --> J["Horizontal variable: x"]
    H --> K["Intercept: log k"]
    H --> L["Gradient: log b"]
    C --> M["Common trap"]
    M --> N["Do not write<br/>log(kb^x) = x log(kb)"]
    N --> O["Reason: x applies only to b,<br/>not to the whole product kb"]
```
