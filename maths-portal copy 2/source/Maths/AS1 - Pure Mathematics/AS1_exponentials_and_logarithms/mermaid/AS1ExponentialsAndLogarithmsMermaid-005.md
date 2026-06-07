# AS1ExponentialsAndLogarithmsMermaid-005

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1ExponentialsAndLogarithmsMermaid-005 |
| Asset type | Mermaid diagram |
| Suggested file path | `mermaid/AS1ExponentialsAndLogarithmsMermaid-005.md` |
| Unit code | AS1 |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Related lesson section | Core Theory 22; Worked Examples 10-11; Guided Practice 11-12 |
| Source | CCEA AS1 Exponentials and logarithms specification boundary; Chapter 14 lesson PDF and transcript |
| Purpose | Show how to interpret and use exponential growth and decay models. |

```mermaid
flowchart TD
    A["Start with an exponential model"] --> B{"Which form is given?"}
    B -->|"A a^t"| C["Initial value is A<br/>because a^0 = 1"]
    B -->|"A e^(kt)"| D["Initial value is A<br/>because e^0 = 1"]
    C --> E{"Multiplier a"}
    E -->|"a > 1"| F["Growth model"]
    E -->|"0 < a < 1"| G["Decay model"]
    D --> H{"Sign of k"}
    H -->|"k > 0"| F
    H -->|"k < 0"| G
    F --> I["Interpret growth in context<br/>Example: 1.04 means 4 percent increase per time unit"]
    G --> J["Interpret decay in context<br/>Example: 0.86 means 14 percent decrease per time unit"]
    I --> K["Substitute the required time value"]
    J --> K
    K --> L["Check the time unit<br/>years, days, hours, etc."]
    L --> M["Calculate using a calculator"]
    M --> N["Round as requested"]
    N --> O{"Comment on long-term behaviour or model validity?"}
    O -->|"Yes"| P["Discuss whether predictions are sensible for large t"]
    O -->|"No"| Q["State final answer in context"]
    P --> Q
```
