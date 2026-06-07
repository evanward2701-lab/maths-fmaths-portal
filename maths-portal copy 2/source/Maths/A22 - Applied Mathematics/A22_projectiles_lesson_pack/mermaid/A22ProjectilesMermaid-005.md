# A22ProjectilesMermaid-005

**Source:** CCEA elaboration for projectile formula derivation, Phase 1 Core Theory.  
**Related lesson section:** Core Theory.  
**Purpose:** Show how standard projectile formulae are derived.

```mermaid
flowchart TD
    A["Start with component equations"] --> B["x = U cos theta times t"]
    A --> C["y = U sin theta times t - 1/2 g t squared"]
    C --> D{"Formula needed?"}
    D -->|"Greatest height"| E["Use vertical motion at top"]
    E --> F["vy = 0"]
    F --> G["H = U squared sin squared theta / 2g"]
    D -->|"Time of flight on same level"| H["Set y = 0"]
    H --> I["0 = t times U sin theta - 1/2 g t"]
    I --> J["T = 2U sin theta / g"]
    D -->|"Range on same level"| K["Use R = horizontal speed times total time"]
    K --> L["R = U cos theta times T"]
    L --> M["R = U squared sin 2theta / g"]
    D -->|"Path equation"| N["Make t the subject from horizontal motion"]
    N --> O["t = x / U cos theta"]
    O --> P["Substitute into vertical equation"]
    P --> Q["y = x tan theta - gx squared / 2U squared cos squared theta"]
    G --> R["Use only when conditions match"]
    J --> R
    M --> R
    Q --> R
```
