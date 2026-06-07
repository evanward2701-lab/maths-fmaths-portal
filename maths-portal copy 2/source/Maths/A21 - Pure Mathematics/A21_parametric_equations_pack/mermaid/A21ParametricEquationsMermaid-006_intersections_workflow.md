# A21ParametricEquationsMermaid-006

## Asset ID
A21ParametricEquationsMermaid-006

## Source
CCEA specification map A21-CG-LO001; transcript and slide evidence on intersections.

## Related lesson section
Worked Examples 6; Exam Technique Notes.

## Purpose
Show that intersections are usually found by solving for the parameter first, then substituting back.

```mermaid
flowchart TD
    A["Need an intersection point"] --> B{"What is the curve meeting?"}
    B -->|x-axis| C["Set y(t)=0"]
    B -->|y-axis| D["Set x(t)=0"]
    B -->|Line or Cartesian curve| E["Substitute x(t), y(t) into the Cartesian equation"]
    C --> F["Solve for t"]
    D --> F
    E --> F
    F --> G{"Is t inside the allowed interval?"}
    G -->|No| H["Reject this value"]
    G -->|Yes| I["Substitute t into x(t)"]
    I --> J["Substitute t into y(t)"]
    J --> K["Write the coordinate pair (x,y)"]
```
