# A22ProjectilesMermaid-004

**Source:** Teacher transcript: angled projection examples and formula derivations.  
**Related lesson section:** Core Theory, Worked Example 4, Worked Example 5.  
**Purpose:** Show the angled projection workflow.

```mermaid
flowchart TD
    A["Particle projected with speed U at angle theta"] --> B["Resolve initial velocity"]
    B --> C["Horizontal component ux = U cos theta"]
    B --> D["Vertical component uy = U sin theta"]
    C --> E["Horizontal motion"]
    E --> F["Acceleration ax = 0"]
    F --> G["x = U cos theta times t"]
    D --> H["Vertical motion"]
    H --> I["Acceleration ay = -g if upwards is positive"]
    I --> J["y = U sin theta times t - 1/2 g t squared"]
    J --> K{"What is required?"}
    K -->|"Greatest height"| L["At top, vertical velocity is zero"]
    L --> M["Use v squared = u squared + 2as"]
    K -->|"Time of flight"| N["Use vertical displacement"]
    N --> O["If same level, set y = 0"]
    K -->|"Range"| P["Find total time first"]
    P --> Q["Use horizontal distance x = ux t"]
    K -->|"Path equation"| R["Eliminate t using t = x / ux"]
    M --> S["Final answer"]
    O --> S
    Q --> S
    R --> S
```
