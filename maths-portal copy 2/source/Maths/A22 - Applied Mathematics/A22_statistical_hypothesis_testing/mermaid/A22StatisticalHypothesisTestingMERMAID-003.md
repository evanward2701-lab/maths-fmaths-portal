# A22StatisticalHypothesisTestingMERMAID-003

## Asset metadata

- Asset ID: A22StatisticalHypothesisTestingMERMAID-003
- Unit code: A22
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Related lesson section: Key Definitions and Notation; Core Theory, Section 4
- Source: CCEA specification map; lesson transcript; Stats Yr2 Chapter 1 PDF
- Purpose: Show the interpretation of PMCC values and remind students that PMCC measures linear correlation only.
- Status: Phase 2 Mermaid draft

## Mermaid code

```mermaid
flowchart LR
    A["r = -1<br/>perfect negative<br/>linear correlation"] --> B["-1 < r < 0<br/>negative linear correlation"]
    B --> C["r close to 0<br/>weak or no linear correlation"]
    C --> D["0 < r < 1<br/>positive linear correlation"]
    D --> E["r = 1<br/>perfect positive<br/>linear correlation"]
    C --> F["Important warning"]
    F --> G["r measures linear correlation only"]
    G --> H["Low r does not prove<br/>there is no relationship"]
    H --> I["The relationship may be curved<br/>or affected by outliers"]
    B --> J["Stronger if r is closer to -1"]
    D --> K["Stronger if r is closer to 1"]
```
