# AS2ForcesMER-002

**Asset ID:** AS2ForcesMER-002  
**Source:** Chapter 5/7 Forces transcript + MechYr2 Chapter 5 Friction PDF  
**Related lesson section:** Core Theory: Resolving a force into components  
**Purpose:** Show the decision workflow for resolving an angled force.

```mermaid
flowchart TD
    A["Start with an angled force F"] --> B["Choose two perpendicular directions"]
    B --> C{"Which direction is adjacent to angle theta?"}
    C --> D["Adjacent component = F cos theta"]
    C --> E["Opposite component = F sin theta"]
    D --> F["Label arrows with directions"]
    E --> F
    F --> G["Use components instead of original angled force"]
    G --> H["Write resolved equations"]
    H --> I{"Particle in equilibrium?"}
    I -->|Yes| J["Forces in one direction = forces in opposite direction"]
    I -->|No| K["Resultant force in acceleration direction = ma"]
```
