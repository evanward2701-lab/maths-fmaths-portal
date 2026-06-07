# AS1AlgebraicExpressionsMER-004

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-004`
- **Source:** Dr Frost factorising slides and transcript comments on common factors
- **Related lesson section:** Core Theory, Worked Examples, Guided Practice
- **Purpose:** Give a factorisation decision tree for “factorise fully” questions.

```mermaid
flowchart TD
    A["Factorise fully"] --> B["Look for a common factor first"]

    B --> C{"Common factor exists?"}
    C -->|Yes| D["Factor it out"]
    C -->|No| E["Move to structure check"]

    D --> E

    E --> F{"Difference of two squares?"}
    F -->|Yes| G["Use a^2 - b^2 = (a - b)(a + b)"]
    F -->|No| H{"Quadratic?"}

    G --> I["Check whether each factor can factorise again"]

    H -->|Yes| J{"Coefficient of x^2 is 1?"}
    H -->|No| K{"Cubic or higher?"}

    J -->|Yes| L["Find two numbers that add to b and multiply to c"]
    J -->|No| M["Use split middle term method"]

    M --> M1["Multiply first coefficient by constant"]
    M1 --> M2["Find two numbers that add to middle coefficient"]
    M2 --> M3["Split the middle term"]
    M3 --> M4["Factorise by grouping"]
    M4 --> M5["Factor out repeated bracket"]

    K -->|Common factor remains| B
    K -->|Known pattern| F
    K -->|No core AS1 method here| N["Log as boundary or later lesson"]

    L --> O["Write bracket product"]
    M5 --> O
    I --> O

    O --> P{"Can it factorise further?"}
    P -->|Yes| B
    P -->|No| Q["Final factorised form"]
```
