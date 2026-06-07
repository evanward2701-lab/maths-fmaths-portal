# A22ProjectilesMermaid-003

**Source:** Teacher transcript: horizontally projected particle examples.  
**Related lesson section:** Worked Examples 1 to 3.  
**Purpose:** Show the method for a particle projected horizontally from a height.

```mermaid
flowchart TD
    A["Horizontally projected particle"] --> B["Initial horizontal speed is U"]
    A --> C["Initial vertical speed is zero"]
    C --> D["Choose vertical sign convention"]
    D --> E["Usually take downwards as positive for falling motion"]
    E --> F["Vertical data"]
    F --> G["s = height fallen"]
    F --> H["u = 0"]
    F --> I["a = g"]
    G --> J["Use s = ut + 1/2 at squared"]
    H --> J
    I --> J
    J --> K["Find time t"]
    B --> L["Horizontal motion"]
    K --> L
    L --> M["Use distance = speed x time"]
    M --> N["x = U t"]
    N --> O{"Question asks straight-line distance from start to impact?"}
    O -->|"Yes"| P["Use Pythagoras with height and horizontal distance"]
    O -->|"No"| Q["State horizontal distance or time"]
    P --> R["Final answer with units"]
    Q --> R
```
