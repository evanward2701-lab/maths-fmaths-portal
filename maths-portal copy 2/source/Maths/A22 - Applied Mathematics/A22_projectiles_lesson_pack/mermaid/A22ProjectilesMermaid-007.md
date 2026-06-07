# A22ProjectilesMermaid-007

**Source:** Phase 1 exam traps and transcript warning about time as the bridge value.  
**Related lesson section:** Common Mistakes and Exam Traps, Exam Technique.  
**Purpose:** Show danger signs in projectile questions.

```mermaid
flowchart TD
    A["Projectile exam trap check"] --> B{"Have you chosen a sign convention?"}
    B -->|"No"| C["Choose upwards or downwards as positive before using SUVAT"]
    B -->|"Yes"| D["Keep that sign convention throughout"]
    C --> D
    D --> E{"Are you using the same time in both directions?"}
    E -->|"No"| F["Time is the bridge between vertical and horizontal motion"]
    E -->|"Yes"| G["Continue"]
    F --> G
    G --> H{"At maximum height?"}
    H -->|"Yes"| I["Set vertical velocity to zero, not total speed"]
    H -->|"No"| J["Use the correct vertical condition"]
    I --> K{"Need speed?"}
    J --> K
    K -->|"Yes"| L["Find velocity components first"]
    L --> M["Use magnitude for speed"]
    K -->|"No"| N["Answer the requested displacement, time, height, or range"]
    M --> O{"Question asks distance from original point?"}
    N --> O
    O -->|"Straight-line distance"| P["Use Pythagoras"]
    O -->|"Distance travelled along path"| Q["Do not assume this unless explicitly asked"]
    P --> R["Final check: units, rounding, context"]
    Q --> R
```
