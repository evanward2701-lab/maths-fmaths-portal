# FAS1ConicSections1Mermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FAS1ConicSections1Mermaid-001` |
| Asset type | Mermaid flowchart |
| Topic ID | `FAS1ConicSections1` |
| Lesson file | `FAS1_conic_sections_1_lesson.md` |
| Related lesson sections | Section 5; Section 6; Section 8; Section 9 |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS1ConicSections1Mermaid-001 | Source: Ordinary A-Level Maths bridge + Conics 1 evidence | Insert from mermaid/FAS1ConicSections1Mermaid-001.md | Purpose: Show how ordinary quadratics, reciprocal graphs, coordinate geometry, differentiation and parametric equations flow into Conic Sections 1. Description: A flowchart beginning with ordinary A-Level Maths skills and ending with parabola \(y^2=4ax\), rectangular hyperbola \(xy=c^2\), tangents, normals and loci.]` |
| Source | Ordinary CCEA A-Level Mathematics bridge context + `FP1-Chp2-ConicSections1.pdf` + `transcripts.md` |
| Source status | Cross-board Conics 1 evidence used as core under user override; ordinary A-Level Mathematics used as bridge context only |
| Purpose | Show how ordinary A-Level Mathematics ideas grow into the Conic Sections 1 methods used in this assumed FAS1 extension lesson. |

## Creation Notes

This diagram is a bridge map. It should help a first-time Further Mathematics student see that Conic Sections 1 grows from ordinary quadratic graphs, reciprocal graphs, coordinate geometry, simultaneous equations, differentiation and parametric equations.

## Mermaid Code

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "background": "#FAF9F6",
    "primaryColor": "#FFFFF0",
    "primaryTextColor": "#2C2C2E",
    "primaryBorderColor": "#E5E5EA",
    "lineColor": "#C5A059",
    "secondaryColor": "#FBEFEF",
    "tertiaryColor": "#FAF9F6",
    "fontFamily": "Inter, Arial, sans-serif"
  }
}}%%

flowchart TD
    A["Ordinary A-Level Maths bridge"]:::bridge

    A --> B["Quadratic graphs<br/>vertical parabolas<br/>y = ax^2 + bx + c"]:::ordinary
    A --> C["Reciprocal graphs<br/>y = k / x"]:::ordinary
    A --> D["Coordinate geometry<br/>gradient, midpoint, line equations"]:::ordinary
    A --> E["Simultaneous equations<br/>line and curve intersections"]:::ordinary
    A --> F["Differentiation<br/>tangents and normals"]:::ordinary
    A --> G["Parametric equations<br/>x and y in terms of a parameter"]:::ordinary

    H["Conic Sections 1<br/>assumed FAS1 extension topic"]:::core

    B --> B1["Further Maths upgrade:<br/>horizontal parabola<br/>y^2 = 4ax"]:::upgrade
    C --> C1["Further Maths upgrade:<br/>rectangular hyperbola<br/>xy = c^2"]:::upgrade
    D --> D1["Use on conics:<br/>focus, directrix, chords,<br/>midpoints, perpendicular bisectors"]:::upgrade
    E --> E1["Use on conics:<br/>find second intersections<br/>and exploit known roots"]:::upgrade
    F --> F1["Use on conics:<br/>parametric differentiation<br/>for tangent and normal formulae"]:::upgrade
    G --> G1["Use on conics:<br/>P(at^2, 2at)<br/>and P(ct, c/t)"]:::upgrade

    B1 --> H
    C1 --> H
    D1 --> H
    E1 --> H
    F1 --> H
    G1 --> H

    H --> I["Core curve 1:<br/>Parabola<br/>Cartesian: y^2 = 4ax<br/>Parametric: x = at^2, y = 2at"]:::core
    H --> J["Core curve 2:<br/>Rectangular hyperbola<br/>Cartesian: xy = c^2<br/>Parametric: x = ct, y = c/t"]:::core

    I --> I1["Geometry:<br/>focus (a,0)<br/>directrix x = -a<br/>vertex (0,0)<br/>axis y = 0"]:::method
    I --> I2["Methods:<br/>locus proof<br/>intersections<br/>chords<br/>tangents and normals<br/>areas and loci"]:::method

    J --> J1["Geometry:<br/>asymptotes x = 0 and y = 0<br/>two branches<br/>t must not be 0"]:::method
    J --> J2["Methods:<br/>intersections<br/>perpendicular bisectors<br/>tangents<br/>normals<br/>axis intercepts and areas"]:::method

    H --> K["Preview only:<br/>ellipse, general hyperbola,<br/>full eccentricity theory,<br/>hyperbolic parametrisation"]:::warning
    L["Main warning:<br/>do not confuse variables x,y<br/>with parameters t,p,q<br/>or constants a,c"]:::warning

    I --> L
    J --> L

    classDef bridge fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    classDef ordinary fill:#FFFFF0,stroke:#E5E5EA,color:#2C2C2E;
    classDef upgrade fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E;
    classDef core fill:#FFF7D6,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    classDef method fill:#FFFFFF,stroke:#E5E5EA,color:#2C2C2E;
    classDef warning fill:#FBEFEF,stroke:#D4AF37,color:#2C2C2E,stroke-dasharray: 4 3;
```
