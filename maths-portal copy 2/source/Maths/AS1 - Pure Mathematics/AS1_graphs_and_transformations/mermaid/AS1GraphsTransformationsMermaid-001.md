# AS1GraphsTransformationsMermaid-001

## Asset ID
`AS1GraphsTransformationsMermaid-001`

## Source
CCEA AS1-AF-LO012 and DrFrost Chapter 4 polynomial/cubic graph evidence.

## Related Lesson Section
Core Theory → Polynomial Graph Shape  
Worked Examples → Cubic Sketching

## Purpose
Show the cubic sketching routine: identify family, shape, roots, multiplicity and `y`-intercept.

```mermaid
flowchart TD
    A["Start: sketch a curve"] --> B["Identify the graph family"]
    B --> C{"Is the highest power 3?"}
    C -->|"Yes"| D["Cubic graph: on-spec core"]
    C -->|"No, degree above 3"| X["Boundary check: enrichment only for this AS1 lesson"]
    D --> E["Find the sign of the leading x cubed term"]
    E --> F{"Leading coefficient positive?"}
    F -->|"Yes"| G["Positive cubic: uphill from left to right"]
    F -->|"No"| H["Negative cubic: downhill from left to right"]
    G --> I["Find roots by setting each factor equal to zero"]
    H --> I
    I --> J["Check root multiplicity"]
    J --> K["Find y-intercept by setting x = 0"]
    K --> L["Draw the sketch"]
    L --> M["Label axes, roots and y-intercept"]
    X --> N["Do not treat as required CCEA AS1 core content"]
```
