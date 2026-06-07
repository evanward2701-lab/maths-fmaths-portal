# AS2ForcesMER-007

**Asset ID:** AS2ForcesMER-007  
**Source:** Chapter 5/7 Forces transcript + MechYr2 Chapter 5 Friction PDF  
**Related lesson section:** Core Theory: Inclined planes  
**Purpose:** Show the preferred resolving directions and weight components on an inclined plane.

```mermaid
flowchart TD
    A["Object on inclined plane"] --> B["Choose axes"]
    B --> C["Parallel to plane"]
    B --> D["Perpendicular to plane"]
    C --> E["Weight component down slope = mg sin theta"]
    D --> F["Weight component into plane = mg cos theta"]
    F --> G["Normal reaction R acts perpendicular out of plane"]
    C --> H{"Is surface rough?"}
    H -->|No| I["No friction"]
    H -->|Yes| J["Friction acts opposite motion or tendency to move"]
    E --> K{"Is object accelerating along plane?"}
    J --> K
    I --> K
    K -->|Yes| L["Resultant force parallel to plane = ma"]
    K -->|No| M["Forces parallel balance"]
    G --> N["Usually no acceleration perpendicular to plane"]
    N --> O["Forces perpendicular balance"]
```
