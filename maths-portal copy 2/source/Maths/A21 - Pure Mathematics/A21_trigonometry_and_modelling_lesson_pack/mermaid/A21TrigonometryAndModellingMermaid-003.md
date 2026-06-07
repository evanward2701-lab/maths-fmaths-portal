# mermaid/A21TrigonometryAndModellingMermaid-003.md

## Asset ID
A21TrigonometryAndModellingMermaid-003

## Source
CCEA A21-TRIG specification alignment; Chapter 7 Trigonometry & Modelling transcript; P2 Chapter 7 slide PDF.

## Related lesson section
Worked Example 7

## Purpose
Map tangent addition formula proof.

```mermaid
flowchart TD
A["tan(A+B)=sin(A+B)/cos(A+B)"] --> B["Substitute addition formulae"]
B --> C["(sinA cosB + cosA sinB)/(cosA cosB - sinA sinB)"]
C --> D["Divide all terms by cosA cosB"]
D --> E["Numerator: tanA + tanB"]
D --> F["Denominator: 1 - tanA tanB"]
E --> G["tan(A+B)=(tanA+tanB)/(1-tanA tanB)"]
F --> G
```
