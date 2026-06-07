# mermaid/A21TrigonometryAndModellingMermaid-002.md

## Asset ID
A21TrigonometryAndModellingMermaid-002

## Source
CCEA A21-TRIG specification alignment; Chapter 7 Trigonometry & Modelling transcript; P2 Chapter 7 slide PDF.

## Related lesson section
Core Theory Part B

## Purpose
Show why sin(A+B) is not sinA+sinB.

```mermaid
flowchart TD
A["False claim: sin(A+B)=sinA+sinB"] --> B["Test A=30°, B=60°"]
B --> C["LHS: sin(90°)=1"]
B --> D["RHS: sin30°+sin60°=(1+√3)/2"]
C --> E["Compare"]
D --> E
E --> F["1 ≠ (1+√3)/2"]
F --> G["Use sin(A+B)=sinA cosB + cosA sinB"]
```
