# AS1GraphsTransformationsMermaid-005

## Asset ID
`AS1GraphsTransformationsMermaid-005`

## Source
CCEA AS1-AF-LO016 and DrFrost transformation summary evidence.

## Related Lesson Section
Core Theory → Transformations of Graphs

## Purpose
Summarise AS1 graph transformations and coordinate effects.

```mermaid
flowchart TD
    A["Start with y = f(x)"] --> B{"Where is the change?"}
    B -->|"Outside f"| C["Affects y-coordinates"]
    B -->|"Inside f"| D["Affects x-coordinates"]
    C --> C1["y = f(x) + a"]
    C1 --> C2["Translate by vector (0, a)"]
    C --> C3["y = a f(x)"]
    C3 --> C4["Stretch in y-direction by scale factor a"]
    C --> C5["y = -f(x)"]
    C5 --> C6["Reflect in the x-axis"]
    D --> D1["y = f(x + a)"]
    D1 --> D2["Translate by vector (-a, 0)"]
    D --> D3["y = f(a x)"]
    D3 --> D4["Stretch in x-direction by scale factor 1/a"]
    D --> D5["y = f(-x)"]
    D5 --> D6["Reflect in the y-axis"]
    C --> E["Outside rule: does what you expect"]
    D --> F["Inside rule: x-values do the opposite"]
```
