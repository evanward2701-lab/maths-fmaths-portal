# AS2ForcesMER-006

**Asset ID:** AS2ForcesMER-006  
**Source:** CCEA specification map + Chapter 5/7 Forces transcript + MechYr2 Chapter 5 Friction PDF  
**Related lesson section:** Core Theory: The friction model  
**Purpose:** Show when to use no friction, $F\leq\mu R$, or $F=\mu R$.

```mermaid
flowchart TD
    A["Surface contact"] --> B{"Is the surface smooth?"}
    B -->|Yes| C["No friction force"]
    B -->|No or rough| D["Include friction F"]
    D --> E["Find normal reaction R"]
    E --> F["Maximum friction = mu R"]
    F --> G{"Is object moving or at limiting equilibrium?"}
    G -->|Moving| H["Use F = mu R"]
    G -->|On point of moving| H
    G -->|Limiting equilibrium| H
    G -->|Static but not limiting| I["Use F <= mu R"]
    I --> J["Friction matches what is needed to maintain equilibrium"]
    H --> K["Use in force equation"]
    J --> K
```
