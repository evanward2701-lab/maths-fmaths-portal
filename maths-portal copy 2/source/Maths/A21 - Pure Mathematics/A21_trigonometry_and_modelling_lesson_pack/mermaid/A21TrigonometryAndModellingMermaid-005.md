# mermaid/A21TrigonometryAndModellingMermaid-005.md

## Asset ID
A21TrigonometryAndModellingMermaid-005

## Source
CCEA A21-TRIG specification alignment; Chapter 7 Trigonometry & Modelling transcript; P2 Chapter 7 slide PDF.

## Related lesson section
Core Theory Parts G-H

## Purpose
Decision process for trig equations.

```mermaid
flowchart TD
A["Trig equation"] --> B{"Same argument?"}
B -- "No" --> C{"Compound angle?"}
C -- "Yes" --> D["Use addition formula"]
C -- "No" --> E{"Double angle?"}
E -- "Yes" --> F["Use double angle formula"]
B -- "Yes" --> G{"Can create tan?"}
G -- "Yes" --> H["Divide carefully by cos"]
G -- "No" --> I["Factorise or use identity"]
D --> I
F --> I
H --> J["Solve basic trig equation"]
I --> J
J --> K["Apply interval"]
K --> L["Final solutions"]
```
