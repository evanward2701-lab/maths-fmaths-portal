# Mermaid Asset: FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001` |
| File path | `mermaid/FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001.md` |
| Topic ID | `FA22RestitutionElasticCollisionsInTwoDimensions` |
| Unit | `FA22` |
| Topic code | `FA22-REST` |
| Related lesson file | `FA22_restitution_elastic_collisions_in_two_dimensions_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration; Section 8: Core Theory; Section 15: Exam Technique Notes |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001 | Source: CCEA FA22-REST specification boundary + lesson evidence | Insert from mermaid/FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001.md | Purpose: Show the decision flow from “smooth impact” to “resolve components” to “apply Newton’s law of restitution”.]` |
| Source | CCEA FA22-REST lesson boundary + lesson evidence from `FM1-Chp5-ObliqueCollisions.pdf` and `transcripts.md` |
| Purpose | Show the decision flow from smooth impact assumptions to component resolution, Newton’s law of restitution, conservation of momentum where needed, and final interpretation. |

## Creation notes

This flowchart is designed as the lesson’s collision compass.

## Mermaid code

```mermaid
flowchart TD
    A["Collision problem<br/>FA22-REST: Restitution"] --> B{"What is in contact?"}
    B --> C["Smooth sphere<br/>with fixed smooth plane"]
    B --> D["Two smooth spheres"]
    C --> E["Identify plane/wall"]
    E --> F["Draw normal direction<br/>perpendicular to plane"]
    F --> G["Draw parallel direction<br/>along plane"]
    G --> H["Smooth contact<br/>no frictional impulse"]
    H --> I["Parallel velocity component unchanged"]
    H --> J["Impulse acts normal to plane"]
    I --> K["Write v_parallel = u_parallel"]
    J --> L["Apply NLR:<br/>normal speed after = e × normal speed before"]
    K --> M["Combine final components"]
    L --> M
    D --> N["Draw line of centres"]
    N --> O["Draw common tangent"]
    O --> P["Smooth spheres:<br/>impulse along line of centres"]
    P --> Q["Tangential components unchanged"]
    P --> R["Line-of-centres components changed"]
    R --> S["Use conservation of momentum"]
    R --> T["Use Newton's law of restitution"]
    Q --> U["Combine final sphere components"]
    S --> U
    T --> U
    M --> V{"What does the question ask for?"}
    U --> V
    V --> W["Velocity: vector/components"]
    V --> X["Speed: magnitude/Pythagoras"]
    V --> Y["Angle: tan ratio/scalar product"]
    V --> Z["Impulse: I = m(v - u)"]
    V --> AA["Kinetic energy loss"]
    W --> AB["Check units, directions, assumptions"]
    X --> AB
    Y --> AB
    Z --> AB
    AA --> AB
    AB --> AC["Final answer with interpretation"]
```
