# A22MomentsMermaid-006

## Asset ID

`A22MomentsMermaid-006`

## Source

Rigid Bodies transcript section 4.

## Related lesson section

Worked Example 7; Worked Example 8.

## Purpose

Suspended beam with tensions.

```mermaid
flowchart TD
    A["Suspended horizontal beam"] --> B["Left string gives tension TA upward"]
    A --> C["Right string gives tension TB upward"]
    A --> D["Beam weight acts downward"]
    A --> E["Any attached particle weight acts downward"]
    B --> F["Take moments about A<br/>to remove TA"]
    C --> F
    D --> F
    E --> F
    F --> G["Find TB"]
    G --> H["Resolve vertically"]
    H --> I["TA + TB = total downward weight"]
    I --> J["Find TA"]
    J --> K["Same structure as rods on supports"]
```
