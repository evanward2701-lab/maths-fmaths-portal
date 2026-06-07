---
asset_id: FAS1ComplexNumbersLociRegionsMermaid-001
asset_type: Mermaid
unit_code: FAS1
topic_code: FAS1-CN
topic_slug: complex_numbers_loci_regions
topic_id: FAS1ComplexNumbersLociRegions
related_lesson_file: FAS1_complex_numbers_loci_regions_lesson.md
related_lesson_section: "# 9. Visual Asset Integration"
used_placeholder: "[VISUAL PLACEHOLDER: FAS1ComplexNumbersLociRegionsMermaid-001 | Source: CCEA `FAS1-CN-LO012` + lesson structure | Insert from mermaid/FAS1ComplexNumbersLociRegionsMermaid-001.md | Purpose: Show the decision process for identifying whether a complex locus is a circle, perpendicular bisector, ray, or region. The diagram must begin with “Read the complex condition”, then branch into modulus equality, modulus inequality, equal-modulus condition, argument equality, and combined region.]"
source: "CCEA FAS1-CN-LO012 boundary + Phase 1 lesson structure + transcript recap of standard complex-number loci"
purpose: "Show the decision process for identifying whether a complex-number condition gives a circle, perpendicular bisector, ray, angular sector, inside/outside region, or overlap."
creation_notes: "This Mermaid diagram is CCEA-safe. It includes only simple loci and simple regions from the Phase 1 core lesson. It deliberately excludes FP2-only ratio loci, quotient-argument circular arcs, and complex-plane transformations."
---

# FAS1ComplexNumbersLociRegionsMermaid-001

## Purpose

This diagram helps a student decide what type of Argand diagram object is produced by a complex-number condition.

## Mermaid code

```mermaid
flowchart TD
    A["Read the complex condition involving z"] --> B{"What type of expression appears?"}
    B --> C["One modulus from one fixed point<br/>|z - a| = r"]
    B --> D["Modulus inequality<br/>|z - a| < r, ≤ r, > r, or ≥ r"]
    B --> E["Equal moduli from two fixed points<br/>|z - a| = |z - b|"]
    B --> F["Argument from one fixed point<br/>arg(z - a) = θ"]
    B --> G["Argument inequality<br/>α < arg(z - a) < β"]
    B --> H["More than one condition<br/>condition 1 AND condition 2"]
    C --> C1["Plot fixed point a<br/>If a = p + qi, plot (p, q)"]
    C1 --> C2["Draw circle centred at a"]
    C2 --> C3["Radius = r"]
    C3 --> C4["Boundary only"]
    D --> D1["Plot fixed point a"]
    D1 --> D2["Draw boundary circle |z - a| = r"]
    D2 --> D3{"Which inequality?"}
    D3 --> D4["< : shade inside<br/>boundary excluded"]
    D3 --> D5["≤ : shade inside<br/>boundary included"]
    D3 --> D6["> : shade outside<br/>boundary excluded"]
    D3 --> D7["≥ : shade outside<br/>boundary included"]
    E --> E1["Plot fixed points a and b"]
    E1 --> E2["Join a to b with a line segment"]
    E2 --> E3["Find midpoint"]
    E3 --> E4["Draw perpendicular bisector"]
    E4 --> E5["Every point on this line is equidistant from a and b"]
    F --> F1["Rewrite as arg(z - a) = θ if needed"]
    F1 --> F2["Plot fixed point a"]
    F2 --> F3["Draw ray from a at angle θ<br/>measured from positive real direction"]
    F3 --> F4["Use open circle at a<br/>because arg(0) is undefined"]
    G --> G1["Plot fixed point a"]
    G1 --> G2["Draw boundary ray arg(z - a) = α"]
    G2 --> G3["Draw boundary ray arg(z - a) = β"]
    G3 --> G4["Shade the sector between the rays"]
    G4 --> G5{"Are inequalities strict?"}
    G5 --> G6["Strict < or > : boundary ray excluded"]
    G5 --> G7["Inclusive ≤ or ≥ : boundary ray included"]
    G6 --> G8["Vertex a still excluded if argument is undefined"]
    G7 --> G8
    H --> H1["Sketch each condition separately"]
    H1 --> H2["Apply boundary rules to each condition"]
    H2 --> H3["Shade only the overlap"]
    H3 --> H4["Use AND for intersection<br/>Both conditions must be true"]
    C4 --> Z["Final check:<br/>fixed points, boundary, shading, exclusions"]
    D4 --> Z
    D5 --> Z
    D6 --> Z
    D7 --> Z
    E5 --> Z
    F4 --> Z
    G8 --> Z
    H4 --> Z
```

## Student-facing interpretation notes

- \(|z-a|=r\): circle centred at \(a\), radius \(r\).
- \(|z-a|=|z-b|\): perpendicular bisector of the segment joining \(a\) and \(b\).
- \(\arg(z-a)=\theta\): ray from \(a\); \(a\) is excluded because \(\arg(0)\) is undefined.
- Inequalities create regions. The word “and” means overlap.
