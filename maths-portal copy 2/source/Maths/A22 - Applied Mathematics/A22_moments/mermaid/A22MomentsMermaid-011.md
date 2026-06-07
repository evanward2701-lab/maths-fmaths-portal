# A22MomentsMermaid-011

## Asset ID

`A22MomentsMermaid-011`

## Source

CCEA A22-MOM boundary mentioning hinged beams; Rigid Bodies transcript hinge sections.

## Related lesson section

Worked Example 13; Core Theory 8.

## Purpose

Hinged beam moment method.

```mermaid
flowchart TD
    A["Hinged beam or rod"] --> B["Hinge at P"]
    B --> C["Horizontal hinge reaction X"]
    B --> D["Vertical hinge reaction Y"]
    A --> E["Other forces act on beam<br/>weight, tension, applied force"]
    C --> F["Take moments about hinge P"]
    D --> F
    F --> G["X has distance 0<br/>so moment is 0"]
    F --> H["Y has distance 0<br/>so moment is 0"]
    E --> I["Only non-hinge forces<br/>appear in moment equation"]
    G --> J["Cleaner equation"]
    H --> J
    I --> J
    J --> K["Find unknown force or tension"]
    K --> L["Then resolve horizontally or vertically<br/>if hinge components are needed"]
```
