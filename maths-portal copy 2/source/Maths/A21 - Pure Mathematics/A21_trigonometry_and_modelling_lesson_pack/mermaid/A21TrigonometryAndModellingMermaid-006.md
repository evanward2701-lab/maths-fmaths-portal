# mermaid/A21TrigonometryAndModellingMermaid-006.md

## Asset ID
A21TrigonometryAndModellingMermaid-006

## Source
CCEA A21-TRIG specification alignment; Chapter 7 Trigonometry & Modelling transcript; P2 Chapter 7 slide PDF.

## Related lesson section
Core Theory Part I

## Purpose
Workflow for harmonic identity.

```mermaid
flowchart TD
A["a sinx + b cosx"] --> B["Choose R sin(x+α)"]
B --> C["Expand"]
C --> D["Rsinx cosα + Rcosx sinα"]
D --> E["Compare coefficients"]
E --> F["Rcosα=a"]
E --> G["Rsinα=b"]
F --> H["R=√(a²+b²)"]
G --> H
F --> I["tanα=b/a"]
G --> I
H --> J["Final form"]
I --> J
```
