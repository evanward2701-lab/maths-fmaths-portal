# A22NormalDistributionMER-002

## Asset ID
`A22NormalDistributionMER-002`

## Source
Teacher transcript and slide PDF normal probability workflow; CCEA `A22-NORMAL-LO001`, `A22-NORMAL-LO002`, and `A22-NORMAL-LO003`.

## Related lesson section
`Core Theory Part 2`, `Core Theory Part 3`, and `Core Theory Part 4`.

## Purpose
Give students a decision route for normal probability questions: symmetry, 68-95-99.7 rule, calculator Normal CD, inverse normal, or standardising.

```mermaid
flowchart TD
    A["Normal distribution question"] --> B["Write the distribution clearly: X ~ N(mu, sigma^2)"]
    B --> C["Identify what is unknown"]
    C --> D{"Is the probability being asked for?"}
    D -->|Yes| E{"Is the boundary exactly the mean?"}
    E -->|Yes| F["Use symmetry: P(X > mu) = 0.5 and P(X < mu) = 0.5"]
    E -->|No| G{"Are the bounds exactly 1, 2, or 3 standard deviations from the mean?"}
    G -->|Yes| H["Use the 68-95-99.7 rule"]
    G -->|No| I["Use Normal CD on calculator"]
    I --> I1{"What region is shaded?"}
    I1 -->|Left tail| I2["Lower bound: very small number. Upper bound: given value"]
    I1 -->|Right tail| I3["Lower bound: given value. Upper bound: very large number"]
    I1 -->|Interval| I4["Lower bound: lower value. Upper bound: upper value"]
    I1 -->|Outside region| I5["Find middle probability and subtract from 1"]
    C --> J{"Is a boundary value unknown?"}
    J -->|Yes| K["Use inverse normal"]
    K --> K1["Convert the region into a left-tail probability if needed"]
    K1 --> K2["Enter area, mu, and sigma"]
    C --> L{"Are mu or sigma unknown?"}
    L -->|Yes| M["Standardise using Z = (X - mu) / sigma"]
    M --> M1["Find the relevant z-value from inverse normal or table"]
    M1 --> M2["Form an equation and solve"]
    F --> N["Check answer is sensible from sketch"]
    H --> N
    I2 --> N
    I3 --> N
    I4 --> N
    I5 --> N
    K2 --> N
    M2 --> N
```
