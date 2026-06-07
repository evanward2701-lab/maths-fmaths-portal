# mermaid/A21TrigonometryAndModellingMermaid-009.md

## Asset ID
A21TrigonometryAndModellingMermaid-009

## Source
CCEA A21-TRIG specification alignment; Chapter 7 Trigonometry & Modelling transcript; P2 Chapter 7 slide PDF.

## Related lesson section
Core Theory Part L

## Purpose
Strategy for proofs.

```mermaid
flowchart TD
A["Trig identity proof"] --> B["Start with more complicated side"]
B --> C{"Contains 2x?"}
C -- "Yes" --> D["Use double angle formulae"]
C -- "No" --> E{"sec/cosec/cot?"}
E -- "Yes" --> F["Rewrite in sin/cos"]
E -- "No" --> G{"tan?"}
G -- "Yes" --> H["Use tan=sin/cos"]
G -- "No" --> I["Use Pythagorean identities"]
D --> J["Simplify"]
F --> J
H --> J
I --> J
J --> K["Reach other side"]
```
