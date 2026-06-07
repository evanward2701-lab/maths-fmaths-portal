# A22MomentsMermaid-010

## Asset ID

`A22MomentsMermaid-010`

## Source

MechYr2 Chapter 7 Applications of Forces, page 16; Rigid Bodies transcript ladder sections.

## Related lesson section

Worked Example 12.

## Purpose

Ladder model.

```mermaid
flowchart TD
    A["Ladder in limiting equilibrium"] --> B["Uniform ladder<br/>weight acts at midpoint"]
    A --> C["Rough ground at A"]
    A --> D["Smooth wall at B"]
    C --> E["Ground reaction R upward"]
    C --> F["Friction mu R horizontal"]
    D --> G["Wall reaction P horizontal"]
    D --> H["No wall friction<br/>because wall is smooth"]
    B --> I["Resolve vertically<br/>R = total weight"]
    F --> J["Resolve horizontally<br/>mu R = P"]
    G --> J
    I --> K["Take moments about a useful point"]
    J --> K
    K --> L["Use perpendicular distances<br/>with sin and cos"]
    L --> M["Solve for mu"]
```
