# AS1GraphsTransformationsMermaid-004

## Asset ID
`AS1GraphsTransformationsMermaid-004`

## Source
CCEA AS1-AF-LO014 and AS1-AF-LO015 plus DrFrost intersections evidence.

## Related Lesson Section
Core Theory → Points of Intersection

## Purpose
Show the full intersection-solving workflow, including the “do not divide by `x`” trap.

```mermaid
flowchart TD
    A["Two graphs: y = f(x) and y = g(x)"] --> B["Intersection x-values occur when f(x) = g(x)"]
    B --> C["Set the expressions equal"]
    C --> D["Expand brackets carefully"]
    D --> E["Rearrange to make one side zero"]
    E --> F["Factorise where possible"]
    F --> G{"Common factor such as x?"}
    G -->|"Yes"| H["Keep the factor: x = 0 may be a solution"]
    G -->|"No"| I["Continue solving remaining equation"]
    H --> J["Solve all remaining factors"]
    I --> J
    J --> K{"Quadratic left over?"}
    K -->|"Yes"| L["Use factorisation, formula or discriminant"]
    K -->|"No"| M["List all real x-values"]
    L --> M
    M --> N["Substitute each x-value into either graph"]
    N --> O["Write full coordinate pairs"]
    O --> P["Use the sketch to check the number of intersections"]
```
