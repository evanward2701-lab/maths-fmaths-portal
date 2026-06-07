# FA21MaclaurinSeriesMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA21MaclaurinSeriesMermaid-001` |
| Asset type | Mermaid diagram |
| Topic ID | `FA21MaclaurinSeries` |
| Unit | `FA21` - Further A2 1 Pure Mathematics |
| Topic code | `FA21-FAF` |
| Topic name | Further algebra and functions - Maclaurin series |
| Related lesson file | `FA21_maclaurin_series_lesson.md` |
| Related lesson section | Section 9.1 Mermaid learning path |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21MaclaurinSeriesMermaid-001 | Source: CCEA \`FA21-FAF\` LO map + lesson boundary | Insert from mermaid/FA21MaclaurinSeriesMermaid-001.md | Purpose: Show the learning route from ordinary derivatives to Maclaurin coefficients, standard series, compound expansions and small-angle approximations. The diagram must show the chain \`derivatives at x=0 → coefficients → standard series → substitutions → approximations\`, with \`FA21-FAF-LO004\` to \`FA21-FAF-LO007\` attached to the relevant nodes.]` |
| Source | CCEA `FA21-FAF` LO map + Phase 1 lesson boundary + Maclaurin derivative-matching evidence |
| Purpose | Show the learning route from ordinary derivatives to Maclaurin coefficients, standard series, compound expansions and small-angle approximations. |
| Evidence status | Syllabus-backed and evidence-inspired. The Taylor-series boundary node is included only as a warning/enrichment marker, not as CCEA core teaching content. |

## Creation Notes

This diagram is designed as a student-facing route map for the whole lesson.

It shows the sequence:

\[
\text{ordinary derivative idea}
\rightarrow
\text{power series}
\rightarrow
\text{derivatives at }x=0
\rightarrow
\text{Maclaurin coefficient formula}
\rightarrow
\text{standard series}
\rightarrow
\text{compound expansions}
\rightarrow
\text{small-angle approximations}.
\]

The diagram attaches each CCEA learning outcome to the relevant stage:

- `FA21-FAF-LO004`: finding Maclaurin series, including the general term;
- `FA21-FAF-LO005`: recognising and using standard Maclaurin series and validity ranges;
- `FA21-FAF-LO006`: deriving simple compound expansions;
- `FA21-FAF-LO007`: using small-angle approximations in radians.

The boundary guardrail node is included because the lesson-specific evidence is a wider cross-board Taylor chapter. It reminds the student that Taylor expansions about \(x=a\), limits using Taylor/Maclaurin series and differential-equation series solutions are enrichment or excluded from the CCEA core lesson unless separately specified.

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
    A["Ordinary A-Level bridge<br/>A derivative gives local information<br/>value, gradient, curvature"] --> B["Power-series model<br/>P(x)=a0+a1x+a2x^2+a3x^3+..."]

    B --> C["Centre at x=0<br/>Maclaurin series use derivative values at 0"]

    C --> D["Match value<br/>P(0)=a0=f(0)"]
    C --> E["Match gradient<br/>P'(0)=a1=f'(0)"]
    C --> F["Match second derivative<br/>P''(0)=2!a2=f''(0)"]
    C --> G["Match third derivative<br/>P'''(0)=3!a3=f'''(0)"]

    D --> H["General coefficient<br/>ar=f^(r)(0)/r!"]
    E --> H
    F --> H
    G --> H

    H --> I["FA21-FAF-LO004<br/>Find the Maclaurin series<br/>including the general term"]

    I --> J["Maclaurin formula<br/>f(x)=f(0)+f'(0)x+f''(0)x^2/2!+..."]

    J --> K["FA21-FAF-LO005<br/>Recognise and use standard series<br/>and validity ranges"]

    K --> K1["e^x<br/>valid for all real x"]
    K --> K2["sin x<br/>valid for all real x"]
    K --> K3["cos x<br/>valid for all real x"]
    K --> K4["ln(1+x)<br/>range: -1 < x <= 1"]
    K --> K5["(1+x)^n<br/>range depends on n"]

    K1 --> L["FA21-FAF-LO006<br/>Simple compound functions<br/>substitute the whole expression"]
    K2 --> L
    K3 --> L
    K4 --> L
    K5 --> L

    L --> L1["Examples of substitutions<br/>e^(3x), sin(2x), ln(1-2x), (1+4x)^(-1/2)"]
    L --> L2["Range travels with substitution<br/>for example u=-2x or u=4x"]

    K2 --> M["FA21-FAF-LO007<br/>Small-angle approximations<br/>x must be in radians"]
    K3 --> M
    K1 -. "not directly used" .-> M

    M --> M1["sin x ≈ x"]
    M --> M2["cos x ≈ 1 - x^2/2"]
    M --> M3["tan x ≈ x"]

    N["Boundary guardrail<br/>Taylor about x=a, limits using series,<br/>and differential-equation series solutions<br/>are enrichment or excluded here"] -.-> C
    N -.-> L
    N -.-> M

    A --> O["Old habit warning<br/>A tangent line matches only value and gradient"]
    O --> H

    P["Notation warning<br/>finite truncation means approximation<br/>infinite series may be exact within range"] --> J
    P --> L1

    Q["Exam technique<br/>keep factorials, brackets and exact fractions"] --> H
    Q --> L
    Q --> M

    classDef bridge fill:#FAF9F6,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1px;
    classDef core fill:#FFFFF0,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    classDef outcome fill:#FBEFEF,stroke:#D4AF37,color:#2C2C2E,stroke-width:1.5px;
    classDef warning fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px,stroke-dasharray: 5 5;
    classDef technique fill:#FAF9F6,stroke:#D4AF37,color:#2C2C2E,stroke-width:1px,stroke-dasharray: 3 3;

    class A,O bridge;
    class B,C,D,E,F,G,H,J,K1,K2,K3,K4,K5,L1,L2,M1,M2,M3 core;
    class I,K,L,M outcome;
    class N warning;
    class P,Q technique;
```

## Accessibility Notes

The diagram should be read from top to bottom.

The main CCEA core route is:

1. ordinary derivative idea;
2. power-series model;
3. matching derivatives at \(x=0\);
4. coefficient formula;
5. standard Maclaurin series;
6. compound functions;
7. small-angle approximations.

Dashed nodes are warnings or boundary notes, not extra core content.

## Asset Status

Generated in chat for Phase 2.
