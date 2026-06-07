# AS1VectorsMermaid-005

## Asset ID
AS1VectorsMermaid-005

## Source
P1-Chp11-Vectors.pdf, Magnitude and Unit Vectors slides; Chapter_11_Vectors transcript.

## Related lesson section
Core Theory: Magnitude of a vector; Unit vectors; Worked Examples 7 and 8.

## Purpose
Show the calculation pathway from component form to magnitude and then to a unit vector.

```mermaid
flowchart TD
    A["Given vector a = (x, y)"] --> B["Magnitude formula"]
    B --> C["|a| = sqrt(x^2 + y^2)"]
    C --> D["This is Pythagoras"]
    D --> E{"Need a unit vector?"}
    E -->|"No"| F["Stop with |a|"]
    E -->|"Yes"| G["Divide vector by its magnitude"]
    G --> H["a-hat = a / |a|"]
    H --> I["a-hat has magnitude 1"]
    I --> J["Same direction as original vector"]
    K["Example"] --> L["a = (3, 4)"]
    L --> M["|a| = 5"]
    M --> N["a-hat = (3/5, 4/5)"]
```
