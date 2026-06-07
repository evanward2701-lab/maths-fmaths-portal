# A21RadiansMermaid-007

## Asset metadata

- Asset ID: A21RadiansMermaid-007
- Unit code: A21
- Topic code: A21-TRIG
- Topic ID: A21Radians
- Source: Chapter 5 Radians transcript and P2 Chapter 5 Radians slide PDF
- Related lesson section: Core Theory 8.9, Boundary-Risk Log
- Purpose: Show how small angle approximation questions are handled while preserving the CCEA boundary warning.
- Phase: Phase 2 Mermaid

```mermaid
flowchart TD
    A["Small angle approximation question"] --> B{"Is theta small?"}
    B --> C["Yes"]
    C --> D{"Is theta in radians?"}
    D --> E["Yes"]
    E --> F["Use approximations"]
    F --> G["sin theta approximately theta"]
    F --> H["tan theta approximately theta"]
    F --> I["cos theta approximately 1 - theta squared over 2"]
    G --> J["Substitute carefully"]
    H --> J
    I --> J
    J --> K["Expand brackets"]
    K --> L["Collect constant, theta and theta squared terms"]
    L --> M["Give final approximation"]
    B --> N["No"]
    N --> O["Approximation may be poor"]
    D --> P["No"]
    P --> Q["Convert to radians first or do not use formula"]
    A --> R["Boundary note"]
    R --> S["Evidence-backed A-Level support, but not explicit in supplied CCEA LO table"]
```
