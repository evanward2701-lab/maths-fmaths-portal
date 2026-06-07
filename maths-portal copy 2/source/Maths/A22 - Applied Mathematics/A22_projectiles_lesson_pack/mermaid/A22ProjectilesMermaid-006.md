# A22ProjectilesMermaid-006

**Source:** Teacher transcript vector projectile example; CCEA A22-KIN two-dimensional kinematics outcomes.  
**Related lesson section:** Worked Example 7.  
**Purpose:** Show how to solve a projectile problem written in vector form.

```mermaid
flowchart TD
    A["Projectile given in vector form"] --> B["Initial velocity vector u"]
    A --> C["Acceleration vector a"]
    B --> D["Separate i component"]
    B --> E["Separate j component"]
    C --> F["Horizontal acceleration is zero"]
    C --> G["Vertical acceleration is -g"]
    D --> H["Horizontal position"]
    H --> I["x = ux t"]
    E --> J["Vertical position"]
    G --> J
    J --> K["y = uy t - 1/2 g t squared"]
    I --> L["Position vector r = x i + y j"]
    K --> L
    D --> M["Horizontal velocity remains ux"]
    E --> N["Vertical velocity vy = uy - g t"]
    M --> O["Velocity vector v = vx i + vy j"]
    N --> O
    O --> P{"Speed required?"}
    P -->|"Yes"| Q["Speed is magnitude of velocity vector"]
    Q --> R["Use square root of vx squared plus vy squared"]
    P -->|"No"| S["State vector result"]
    R --> T["Final answer with units"]
    S --> T
```
