# AS1StraightLineGraphsMermaid-001

## Asset ID

`AS1StraightLineGraphsMermaid-001`

## Source

- `P1-Chp5-StraightLineGraphs_RevealBlocksRemoved.pdf`
- `Chapter_5_Straight_Line_Graphs_🤖_(Pure_Year_1)_Transcript.md`
- CCEA GCE Mathematics Specification Map: AS1-CG-LO001

## Related lesson section

Core Theory, Section 8: Deriving \(y-y_1=m(x-x_1)\)  
Core Theory, Section 9: Equation of a line through two points

## Purpose

Show the decision route for finding the equation of a straight line.

```mermaid
flowchart TD
    A["Need equation of a straight line"] --> B{"What information is given?"}
    B --> C["Gradient m and point (x1, y1)"]
    B --> D["Two points (x1, y1) and (x2, y2)"]
    B --> E["Line equation already given"]
    C --> F["Use point-gradient form"]
    F --> G["y - y1 = m(x - x1)"]
    D --> H["Find gradient first"]
    H --> I["m = (y2 - y1) / (x2 - x1)"]
    I --> J["Choose either given point"]
    J --> F
    E --> K{"What form is needed?"}
    G --> L{"What form does the question ask for?"}
    L --> M["Leave as point-gradient form if no specific form is requested"]
    L --> N["Standard form ax + by + c = 0"]
    L --> O["Slope-intercept form y = mx + c"]
    K --> N
    K --> O
    K --> P["Use as given if already suitable"]
    N --> Q["Clear fractions"]
    Q --> R["Expand brackets carefully"]
    R --> S["Move all terms to one side"]
    S --> T["Final answer: ax + by + c = 0"]
    O --> U["Make y the subject"]
    U --> V["Split terms if needed"]
    V --> W["Read gradient m and y-intercept c"]
    M --> X["Final answer accepted unless a form is specified"]
    T --> Y["Check a, b, c are integers"]
    W --> Z["Check equation is exactly y = mx + c"]
    Y --> AA["Done"]
    Z --> AA
    X --> AA
    P --> AA
```
