# FAS1ConicSections1Mermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FAS1ConicSections1Mermaid-002` |
| Asset type | Mermaid decision tree |
| Topic ID | `FAS1ConicSections1` |
| Lesson file | `FAS1_conic_sections_1_lesson.md` |
| Related lesson sections | Section 8; Section 11; Section 12; Section 15 |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS1ConicSections1Mermaid-002 | Source: FP1-Chp2-ConicSections1.pdf and transcripts.md | Insert from mermaid/FAS1ConicSections1Mermaid-002.md | Purpose: Help students choose between Cartesian and parametric methods. Description: A decision tree asking whether a point is given as \((at^2,2at)\) or \((ct,c/t)\), whether a line/axis condition is given, whether a tangent/normal is required, and whether elimination or substitution is cleaner.]` |
| Source | `FP1-Chp2-ConicSections1.pdf` + `transcripts.md` |
| Source status | Cross-board Conics 1 evidence used as core under user override |
| Purpose | Help students choose a clean method when solving parabola and rectangular hyperbola problems. |

## Creation Notes

This decision tree supports exam technique. It reflects the repeated lesson pattern: identify the conic, choose Cartesian or parametric form, use coordinate geometry for specific points and lines, use parametric differentiation for general tangents/normals, and keep preview-only material out of Conics 1 core work.

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
    A["Start with the question"]:::start
    A --> B{"Which conic form<br/>appears?"}:::choice

    B -->|y^2 = 4ax| C["Parabola route"]:::core
    B -->|xy = c^2| D["Rectangular hyperbola route"]:::core
    B -->|ellipse or general hyperbola| E["Preview-only warning:<br/>not core in Conics 1"]:::warning

    C --> C1["Write key facts:<br/>focus (a,0)<br/>directrix x = -a<br/>P(at^2, 2at)"]:::method
    D --> D1["Write key facts:<br/>asymptotes x = 0, y = 0<br/>P(ct, c/t)<br/>t cannot be 0"]:::method

    C1 --> F{"What is being asked?"}:::choice
    D1 --> G{"What is being asked?"}:::choice

    F -->|focus or directrix| F1["Compare with y^2 = 4ax"]:::method
    F -->|specific line intersection| F2{"Given coordinates<br/>or a line in x,y?"}:::choice
    F -->|general tangent or normal| F3["Parametric differentiation:<br/>dx/dt = 2at<br/>dy/dt = 2a<br/>dy/dx = 1/t"]:::method
    F -->|locus or midpoint| F4["Name moving point (X,Y),<br/>write coordinates,<br/>eliminate the parameter"]:::method

    F2 -->|yes| F2A["Cartesian method:<br/>substitute line into parabola<br/>solve quadratic"]:::method
    F2 -->|point written as parameter| F2B["Parametric method:<br/>substitute x = at^2, y = 2at"]:::method
    F2A --> F2C["If one intersection is known,<br/>use it as a known root or factor"]:::tip
    F2B --> F2C

    F3 --> F3A["Tangent:<br/>ty = x + at^2"]:::result
    F3 --> F3B["Normal:<br/>y + tx = 2at + at^3"]:::result

    G -->|specific line intersection| G1{"Given coordinates<br/>or parametric point?"}:::choice
    G -->|general tangent| G2["Parametric differentiation:<br/>dx/dt = c<br/>dy/dt = -c/t^2<br/>dy/dx = -1/t^2"]:::method
    G -->|general normal| G3["Use normal gradient t^2<br/>at P(ct, c/t)"]:::method
    G -->|axis intercepts or area| G4["Use tangent intercepts:<br/>set y = 0 for x-axis<br/>set x = 0 for y-axis"]:::method

    G1 -->|line in x,y| G1A["Cartesian method:<br/>substitute into xy = c^2"]:::method
    G1 -->|point as ct, c/t| G1B["Parametric method:<br/>substitute x = ct, y = c/t"]:::method

    G2 --> G2A["Tangent:<br/>x + t^2y = 2ct"]:::result
    G3 --> G3A["Normal:<br/>p^3x - py + c(1 - p^4) = 0"]:::result

    F1 --> H["Check exact values<br/>and draw a quick sketch"]:::finish
    F2C --> H
    F3A --> H
    F3B --> H
    F4 --> H
    G1A --> H
    G1B --> H
    G2A --> H
    G3A --> H
    G4 --> H

    I["Always check symbol roles:<br/>x,y are variables;<br/>t,p,q are parameters;<br/>a,c are constants"]:::warning
    C1 --> I
    D1 --> I
    I --> H

    classDef start fill:#FFF7D6,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    classDef choice fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    classDef core fill:#FFFFF0,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    classDef method fill:#FFFFFF,stroke:#E5E5EA,color:#2C2C2E;
    classDef result fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    classDef tip fill:#FFFFF0,stroke:#C5A059,color:#2C2C2E,stroke-dasharray: 4 3;
    classDef warning fill:#FBEFEF,stroke:#D4AF37,color:#2C2C2E,stroke-dasharray: 4 3;
    classDef finish fill:#FFF7D6,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
```
