# AS1ExponentialsAndLogarithmsMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1ExponentialsAndLogarithmsMermaid-001 |
| Asset type | Mermaid diagram |
| Suggested file path | `mermaid/AS1ExponentialsAndLogarithmsMermaid-001.md` |
| Unit code | AS1 |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Related lesson section | Core Theory 17-19; Worked Examples 7-9; Exam Technique Notes |
| Source | CCEA AS1 Exponentials and logarithms specification boundary; Chapter 14 lesson PDF and transcript |
| Purpose | Show a decision flow for solving exponential equations, including matching bases, taking logarithms, and collecting $x$-terms. |

```mermaid
flowchart TD
    A["Start with an exponential equation"] --> B{"Can both sides be written with the same base?"}
    B -->|"Yes"| C["Rewrite both sides with matching bases<br/>Example: 27 = 3^3"]
    C --> D["Equate the powers"]
    D --> E["Solve the resulting linear equation"]
    E --> F["State the solution"]
    B -->|"No"| G{"Does the equation contain one exponential term only?<br/>Example: a^x = b"}
    G -->|"Yes"| H["Take logarithms of both sides<br/>Use log_a or ln consistently"]
    H --> I["Use the inverse relationship<br/>log_a(a^x)=x"]
    I --> J["Solve for x"]
    J --> F
    G -->|"No"| K["Take natural logarithms of both sides"]
    K --> L["Use the power law<br/>ln(a^u)=u ln a"]
    L --> M["Expand brackets if needed"]
    M --> N["Collect all x-terms on one side"]
    N --> O["Factorise x"]
    O --> P["Divide to isolate x"]
    P --> F
    F --> Q{"Is a decimal answer required?"}
    Q -->|"Yes"| R["Round to the requested accuracy"]
    Q -->|"No"| S["Leave exact form using logs if appropriate"]
    R --> T["Final answer"]
    S --> T["Final answer"]
```
