# AS1AlgebraicExpressionsMER-003

## Asset Metadata

- **Asset ID:** `AS1AlgebraicExpressionsMER-003`
- **Source:** Dr Frost expansion examples and transcript warnings about signs and collecting like terms
- **Related lesson section:** Core Theory, Worked Examples, Common Mistakes and Exam Traps
- **Purpose:** Show the safe workflow for expanding brackets and collecting terms without sign slips.

```mermaid
flowchart TD
    A["Expression with brackets"] --> B{"How many brackets?"}

    B --> C["One bracket with multiplier"]
    B --> D["Two brackets"]
    B --> E["Three or more brackets"]

    C --> C1["Multiply every term inside by the outside factor"]
    C1 --> C2{"Is the outside factor negative?"}
    C2 -->|Yes| C3["Check every sign carefully"]
    C2 -->|No| C4["Continue expansion"]

    D --> D1["Multiply each term in first bracket by each term in second"]
    D1 --> D2["Avoid relying only on FOIL"]
    D2 --> D3["Write all products before collecting"]

    E --> E1["Multiply two brackets first"]
    E1 --> E2["Reduce number of brackets by one"]
    E2 --> E3["Repeat until fully expanded"]

    C3 --> F["Collect like terms"]
    C4 --> F
    D3 --> F
    E3 --> F

    F --> G{"Are terms actually like terms?"}
    G -->|Yes| H["Add or subtract coefficients only"]
    G -->|No| I["Do not combine"]

    H --> J["Write final polynomial in descending powers"]
    I --> J

    J --> K["Final simplified expression"]
```
