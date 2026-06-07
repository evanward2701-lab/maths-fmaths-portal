# A21ParametricEquationsMermaid-007

## Asset ID
A21ParametricEquationsMermaid-007

## Source
CCEA specification map A21-CG-LO002; transcript and slide modelling examples.

## Related lesson section
Worked Example 7; Syllabus Gap Check.

## Purpose
Show the modelling cycle for parametric equations in contexts such as plane motion.

```mermaid
flowchart TD
    A["Real context"] --> B["Identify quantities"]
    B --> C["Choose parameter, often time t"]
    C --> D["Write x = p(t)"]
    C --> E["Write y = q(t)"]
    D --> F["Use equations to answer the question"]
    E --> F
    F --> G{"What is being asked?"}
    G -->|Position at a time| H["Substitute t"]
    G -->|Time at a position| I["Solve x(t) or y(t) first"]
    G -->|Path shape| J["Eliminate t"]
    G -->|Model realism| K["Inspect domain and assumptions"]
    H --> L["Interpret in context"]
    I --> L
    J --> L
    K --> L
```
