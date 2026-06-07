# A21ParametricEquationsMermaid-005

## Asset ID
A21ParametricEquationsMermaid-005

## Source
CCEA specification map A21-CG-LO001; PowerPoint chapter overview on sketching parametric curves.

## Related lesson section
Core Theory; Visual Asset Integration; Exam Technique Notes.

## Purpose
Give students a route-choice diagram for sketching parametric curves.

```mermaid
flowchart TD
    A["Need to sketch a parametric curve"] --> B{"Can you convert to a recognisable Cartesian equation?"}
    B -->|Yes| C["Convert to Cartesian form"]
    C --> D{"Recognise the curve"}
    D --> E["Line"]
    D --> F["Parabola"]
    D --> G["Circle"]
    D --> H["Reciprocal/exponential-style curve"]
    E --> I["Apply parameter restrictions"]
    F --> I
    G --> I
    H --> I
    I --> J["Sketch only the allowed part"]
    B -->|No| K["Use a table of parameter values"]
    K --> L["Choose values across the interval"]
    L --> M["Calculate x and y for each value"]
    M --> N["Plot points in order"]
    N --> O["Join smoothly"]
```
