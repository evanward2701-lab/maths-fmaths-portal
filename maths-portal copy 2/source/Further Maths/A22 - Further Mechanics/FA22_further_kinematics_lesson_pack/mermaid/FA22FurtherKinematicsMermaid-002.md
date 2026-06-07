# Mermaid Asset: FA22FurtherKinematicsMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA22FurtherKinematicsMermaid-002` |
| Asset type | Mermaid diagram |
| Topic ID | `FA22FurtherKinematics` |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Topic code | `FA22-FKIN` |
| Related lesson file | `FA22_further_kinematics_lesson.md` |
| Related lesson section | `# 3. Specification Alignment`, `# 16. Syllabus Gap Check` |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22FurtherKinematicsMermaid-002 | Source: CCEA Further Mathematics specification map | Insert from mermaid/FA22FurtherKinematicsMermaid-002.md | Purpose: Separate the two CCEA FKIN learning outcomes and show which parts of the lesson support each one.]` |
| Source | CCEA Further Mathematics specification map |
| Purpose | Show how the lesson separates `FA22-FKIN-LO001` and `FA22-FKIN-LO002`, including the evidence strength for each strand. |

## Creation notes

This diagram is a coverage map, not a method diagram.

It records the important syllabus distinction:

- `FA22-FKIN-LO001` requires **three-dimensional kinematics** using calculus and \(\mathbf{i},\mathbf{j},\mathbf{k}\).
- `FA22-FKIN-LO002` requires **straight-line variable acceleration** where acceleration may be a function of time, velocity or displacement, including examples involving constant power.

The supplied lesson evidence is strong for `FA22-FKIN-LO002`, but weak for `FA22-FKIN-LO001`. The diagram preserves that evidence limitation rather than hiding it.

## Mermaid code

```mermaid
flowchart TD
    A["FA22-FKIN<br/>Further kinematics"] --> B["FA22-FKIN-LO001"]
    A --> C["FA22-FKIN-LO002"]

    B --> B1["Solve problems involving kinematics in three dimensions"]
    B1 --> B2["Use calculus"]
    B1 --> B3["Use i, j, k unit vectors"]
    B2 --> B4["Position vector r(t)"]
    B2 --> B5["Velocity v(t) = dr/dt"]
    B2 --> B6["Acceleration a(t) = dv/dt = d²r/dt²"]
    B3 --> B7["Componentwise differentiation and integration"]
    B7 --> B8["Vector constants when integrating"]
    B --> B9["Evidence status:<br/>required by CCEA<br/>lesson-specific evidence is weak"]

    C --> C1["Solve problems involving variable acceleration along a straight line"]
    C1 --> C2["Acceleration as a function of time<br/>a = f(t)"]
    C1 --> C3["Acceleration as a function of displacement<br/>a = f(x)"]
    C1 --> C4["Acceleration as a function of velocity<br/>a = f(v)"]
    C1 --> C5["Examples involving constant power"]
    C2 --> C6["Use a = dv/dt<br/>then integrate with respect to t"]
    C3 --> C7["Use a = v dv/dx<br/>or d/dx(1/2 v²)"]
    C4 --> C8["Need time or velocity:<br/>use a = dv/dt"]
    C4 --> C9["Need displacement or distance:<br/>use a = v dv/dx"]
    C5 --> C10["Use P = Fv<br/>so driving force may involve 1/v"]
    C --> C11["Evidence status:<br/>strong support from transcript, screenshots and FM2 PDF"]

    B9 --> D["Syllabus gap check"]
    C11 --> D
    D --> E["Core lesson includes both LO strands"]
    D --> F["Further evidence recommended:<br/>CCEA-specific 3D vector examples<br/>CCEA-specific constant power examples"]
```
