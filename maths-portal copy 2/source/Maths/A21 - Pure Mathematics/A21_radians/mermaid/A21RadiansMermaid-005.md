# A21RadiansMermaid-005

## Asset metadata

- Asset ID: A21RadiansMermaid-005
- Unit code: A21
- Topic code: A21-TRIG
- Topic ID: A21Radians
- Source: Chapter 5 Radians transcript and P2 Chapter 5 Radians slide PDF
- Related lesson section: Core Theory 8.8, Worked Examples 11 and 12
- Purpose: Show the safe workflow for solving trig equations in radians.
- Phase: Phase 2 Mermaid

```mermaid
flowchart TD
    A["Trig equation in radians"] --> B["Check calculator is in radians mode"]
    B --> C{"Is the angle x, 2x, 3x or similar?"}
    C --> D["Angle is x"]
    D --> E["Solve within given x interval"]
    C --> F["Angle is multiple of x"]
    F --> G["Adjust interval first"]
    G --> H["Example: if 0 <= x < 2pi, then 0 <= 3x < 6pi"]
    E --> I["Find principal solution"]
    H --> I
    I --> J["Use symmetry and period"]
    J --> K["Sine and cosine period: 2pi"]
    J --> L["Tangent period: pi"]
    K --> M["List all solutions in adjusted interval"]
    L --> M
    M --> N{"Was the angle multiplied?"}
    N --> O["Yes: divide final angle values by multiplier"]
    N --> P["No: keep solutions as found"]
    O --> Q["Reject values outside original interval"]
    P --> Q
    Q --> R["Final answer in radians"]
```
