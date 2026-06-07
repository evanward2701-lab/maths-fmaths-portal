# A22ProjectilesMermaid-001

**Source:** CCEA A22-KIN specification map, teacher transcript, Phase 1 lesson structure.  
**Related lesson section:** Core Theory, Exam Technique, Worked Examples.  
**Purpose:** Show the overall projectile problem-solving workflow.

```mermaid
flowchart TD
    A["Projectile question"] --> B["Draw a clear diagram"]
    B --> C["Choose axes and sign convention"]
    C --> D{"How is it projected?"}
    D -->|"Horizontally"| E["Initial vertical velocity uy = 0"]
    D -->|"At an angle"| F["Resolve velocity into components"]
    F --> G["ux = U cos theta"]
    F --> H["uy = U sin theta"]
    E --> I["Vertical motion"]
    H --> I
    I --> J["Use SUVAT with acceleration due to gravity"]
    J --> K["Find time, height, or vertical speed"]
    G --> L["Horizontal motion"]
    E --> L
    L --> M["Horizontal acceleration is zero"]
    M --> N["Use distance = speed x time"]
    K --> O["Use time as the bridge value"]
    N --> O
    O --> P["Answer requested quantity"]
    P --> Q{"Need speed or direction?"}
    Q -->|"Yes"| R["Recombine components using Pythagoras or trigonometry"]
    Q -->|"No"| S["State final answer with units and sensible rounding"]
    R --> S
```
