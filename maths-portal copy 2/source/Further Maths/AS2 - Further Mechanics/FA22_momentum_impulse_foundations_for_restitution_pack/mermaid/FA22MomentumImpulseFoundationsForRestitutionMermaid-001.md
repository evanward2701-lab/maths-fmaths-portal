# Mermaid Asset: FA22MomentumImpulseFoundationsForRestitutionMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA22MomentumImpulseFoundationsForRestitutionMermaid-001` |
| Asset type | Mermaid diagram |
| Topic ID | `FA22MomentumImpulseFoundationsForRestitution` |
| Lesson file | `FA22_momentum_impulse_foundations_for_restitution_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22MomentumImpulseFoundationsForRestitutionMermaid-001 | Source: CCEA Further Mathematics specification boundary + Ordinary A-Level Maths bridge sources + supplied momentum/impulse evidence | Insert from mermaid/FA22MomentumImpulseFoundationsForRestitutionMermaid-001.md | Purpose: Show the course pathway from ordinary A22 Impulse and Momentum into FA22 Restitution. Description: The diagram should show GCSE/AS mechanics foundations feeding into ordinary A22 impulse and momentum, then into FA22 Restitution. It must mark momentum/impulse as bridge content and restitution as the Further Maths destination.]` |
| Source | CCEA Further Mathematics specification boundary + Ordinary A-Level Maths bridge sources + supplied momentum/impulse evidence |
| Purpose | Show the pathway from ordinary A-Level mechanics foundations into FA22 Restitution. |
| Boundary note | Momentum and impulse are shown as bridge/prerequisite content, not as a standalone CCEA Further Mathematics topic. |

## Creation Notes

This diagram helps the student see that GCSE and ordinary A-Level mechanics introduce motion, force and vector ideas; ordinary A22 Impulse and Momentum develops \(P=mv\), \(I=m(v-u)\), \(I=Ft\) and PCLM; and FA22 Restitution is the Further Maths destination.

## Mermaid Code

```mermaid
flowchart TD
    A["GCSE Mechanics Foundations<br/>speed, force, mass, units"] --> B["Ordinary AS/A2 Mechanics<br/>velocity, acceleration, F = ma"]
    B --> C["Ordinary A-Level Vector Skills<br/>direction, components, magnitude"]
    B --> D["Ordinary A22 Impulse and Momentum<br/>bridge topic"]
    C --> D

    D --> E["Momentum<br/>P = mv<br/>vector quantity"]
    D --> F["Impulse<br/>I = m(v - u)<br/>I = Ft"]
    D --> G["PCLM<br/>total momentum before = total momentum after"]

    E --> H["This lesson<br/>Momentum and Impulse Foundations<br/>for Restitution"]
    F --> H
    G --> H

    H --> I["FA22-REST Restitution<br/>Further Maths destination"]
    I --> J["Newton's law of restitution<br/>required later"]
    I --> K["Direct elastic collisions<br/>smooth spheres or sphere and fixed plane"]

    L["Boundary warning<br/>Momentum and impulse are bridge foundations,<br/>not a standalone CCEA Further Maths topic"] -.-> H
    M["Missing from current evidence<br/>full restitution law and CCEA restitution examples"] -.-> J

    classDef foundation fill:#FAF9F6,stroke:#E5E5EA,color:#2C2C2E;
    classDef bridge fill:#FFFFF0,stroke:#D4AF37,color:#2C2C2E;
    classDef further fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E;
    classDef warning fill:#FFF7E6,stroke:#C5A059,color:#2C2C2E,stroke-dasharray: 5 3;

    class A,B,C foundation;
    class D,E,F,G,H bridge;
    class I,J,K further;
    class L,M warning;
```
