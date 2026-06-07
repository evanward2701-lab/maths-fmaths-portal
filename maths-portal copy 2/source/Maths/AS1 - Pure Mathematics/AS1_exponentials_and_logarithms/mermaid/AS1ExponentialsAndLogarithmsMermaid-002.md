# AS1ExponentialsAndLogarithmsMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1ExponentialsAndLogarithmsMermaid-002 |
| Asset type | Mermaid diagram |
| Suggested file path | `mermaid/AS1ExponentialsAndLogarithmsMermaid-002.md` |
| Unit code | AS1 |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Related lesson section | Core Theory 12-16; Worked Example 6; Guided Practice 4-5 |
| Source | CCEA AS1 Exponentials and logarithms specification boundary; Chapter 14 lesson PDF and transcript |
| Purpose | Help students choose the correct logarithm law and avoid false laws such as splitting a logarithm of a sum. |

```mermaid
flowchart TD
    A["Start with a logarithmic expression"] --> B{"What operation is inside or between the logs?"}
    B -->|"Addition between logs"| C["Use the product law"]
    C --> C1["log_a x + log_a y = log_a(xy)"]
    B -->|"Subtraction between logs"| D["Use the quotient law"]
    D --> D1["log_a x - log_a y = log_a(x/y)"]
    B -->|"Number multiplying a log"| E["Use the power law"]
    E --> E1["k log_a x = log_a(x^k)"]
    B -->|"A power inside the log"| F["Move the power to the front if useful"]
    F --> F1["log_a(x^k)=k log_a x"]
    B -->|"A sum inside one log"| G["No log law applies"]
    G --> G1["Do not write log_a(x+y)=log_a x + log_a y"]
    B -->|"A single log equation"| H["Check whether both sides can be written as logs with the same base"]
    H --> I{"Same base on both sides?"}
    I -->|"Yes"| J["Equate the inputs<br/>but only after checking domains"]
    I -->|"No"| K["Use definitions or convert constants into logs if valid"]
    C1 --> L["Simplify carefully"]
    D1 --> L
    E1 --> L
    F1 --> L
    G1 --> M["Use another algebraic method"]
    J --> N["Solve and check all log inputs are positive"]
    K --> N
    L --> N
    M --> N
    N --> O["Final answer"]
```
