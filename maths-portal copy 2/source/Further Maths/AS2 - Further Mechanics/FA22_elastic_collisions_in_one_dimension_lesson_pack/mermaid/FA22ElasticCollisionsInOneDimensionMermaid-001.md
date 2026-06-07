# Mermaid Asset: FA22ElasticCollisionsInOneDimensionMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | FA22ElasticCollisionsInOneDimensionMermaid-001 |
| Asset type | Mermaid flowchart |
| Lesson file | FA22_elastic_collisions_in_one_dimension_lesson.md |
| Related lesson section | Section 9.1 Method flow diagram; Section 8 Core Theory; Section 15 Exam Technique Notes |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionMermaid-001 | Source: CCEA FA22-REST boundary + transcript explanation of PCLM and NLR | Insert from mermaid/FA22ElasticCollisionsInOneDimensionMermaid-001.md | Purpose: Show the full solution flow for direct collision questions.]` |
| Source | CCEA FA22-REST boundary + lesson transcript explanation of PCLM and NLR |
| Purpose | Show the full solution flow for direct one-dimensional collision questions using PCLM and Newton's Law of Restitution. |
| Status | Generated in Phase 2 |

## Mermaid code

```mermaid
flowchart TD
    A["Read the question carefully"] --> B["Identify collision type"]
    B --> C{"What kind of direct impact?"}
    C -->|Two smooth spheres| D["Draw before-and-after sphere diagram"]
    C -->|Smooth sphere and fixed plane| E["Draw before-and-after wall / plane diagram"]
    C -->|Successive direct impacts| F["Split into separate collision events"]
    D --> G["Choose a positive direction"]
    E --> G
    F --> G
    G --> H["Label known masses and velocities"]
    H --> I["Label unknown final velocities"]
    I --> J{"Are final directions given?"}
    J -->|Yes| K["Use the given directions in the diagram"]
    J -->|No| L["Draw unknown final velocities in the positive direction"]
    K --> M["Write PCLM equation"]
    L --> M
    M --> M1["PCLM uses signed velocities"]
    M1 --> M2["Total momentum before = total momentum after"]
    M2 --> N["Write NLR equation"]
    N --> N1["NLR uses scalar speeds"]
    N1 --> N2["e = speed of separation / speed of approach"]
    N2 --> O{"Do the particles approach before impact?"}
    O -->|Yes| P["Form simultaneous equations"]
    O -->|No| Q["Collision cannot occur under this diagram or data"]
    P --> R{"Are equations numerical or algebraic?"}
    R -->|Numerical| S["Solve manually or with calculator simultaneous-equation solver"]
    R -->|Algebraic| T["Solve manually by substitution or elimination"]
    S --> U["Find final velocities"]
    T --> U
    U --> V{"Any final velocity negative?"}
    V -->|Yes| W["Interpret as motion opposite to chosen positive direction"]
    V -->|No| X["Direction matches chosen diagram"]
    W --> Y["Check coefficient of restitution"]
    X --> Y
    Y --> Z{"Is 0 ≤ e ≤ 1?"}
    Z -->|Yes| AA["Check physical logic: separating after impact, no impossible overtaking"]
    Z -->|No| AB["Answer is physically impossible or algebra/sign error exists"]
    AA --> AC["Write final answer with units and direction"]
    AB --> AD["Review NLR, PCLM, signs and model assumptions"]
    AC --> AE["Final exam-style conclusion"]
    AD --> A
```
