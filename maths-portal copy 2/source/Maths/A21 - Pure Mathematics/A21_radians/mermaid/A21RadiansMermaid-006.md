# A21RadiansMermaid-006

## Asset metadata

- Asset ID: A21RadiansMermaid-006
- Unit code: A21
- Topic code: A21-TRIG
- Topic ID: A21Radians
- Source: Chapter 5 Radians transcript and P2 Chapter 5 Radians slide PDF
- Related lesson section: Common Mistakes and Exam Traps, Exam Technique
- Purpose: Show the main calculator and unit traps in radian questions.
- Phase: Phase 2 Mermaid

```mermaid
flowchart TD
    A["Radian question"] --> B{"Does the question contain trig functions?"}
    B --> C["Yes"]
    C --> D["Set calculator to radians mode"]
    B --> E["No"]
    E --> F["Multiplication formulas such as l = r theta do not depend on calculator angle mode"]
    A --> G{"Is theta in degrees?"}
    G --> H["Yes"]
    H --> I["Convert to radians before using l = r theta or A = 1/2 r squared theta"]
    G --> J["No"]
    J --> K["Proceed using radians directly"]
    A --> L{"Is the answer exact?"}
    L --> M["If possible, keep pi form"]
    L --> N["If decimal required, round sensibly and include units"]
    A --> O{"Is it a segment?"}
    O --> P["Use sector minus triangle"]
    P --> Q["Do not use sector area alone"]
    A --> R["Final scan"]
    R --> S["Check interval, mode, units, and radians"]
```
