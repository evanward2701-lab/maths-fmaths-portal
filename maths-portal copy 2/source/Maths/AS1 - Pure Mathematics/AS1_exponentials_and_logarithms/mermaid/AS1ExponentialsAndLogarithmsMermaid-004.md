# AS1ExponentialsAndLogarithmsMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1ExponentialsAndLogarithmsMermaid-004 |
| Asset type | Mermaid diagram |
| Suggested file path | `mermaid/AS1ExponentialsAndLogarithmsMermaid-004.md` |
| Unit code | AS1 |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Related lesson section | Core Theory 8-11; Worked Example 5; Natural logarithm examples |
| Source | CCEA AS1 Exponentials and logarithms specification boundary; Chapter 14 lesson PDF and transcript |
| Purpose | Show how logarithmic form and exponential form convert into each other. |

```mermaid
flowchart LR
    A["Logarithmic form<br/>log_a n = x"] --> B["Meaning<br/>The power of a that gives n is x"]
    B --> C["Exponential form<br/>a^x = n"]
    C --> D["Example<br/>2^3 = 8"]
    D --> E["Log form<br/>log_2 8 = 3"]
    C --> F["Example<br/>3^4 = 81"]
    F --> G["Log form<br/>log_3 81 = 4"]
    A --> H["Example<br/>log_5 125 = 3"]
    H --> I["Exponential form<br/>5^3 = 125"]
    A --> J["Example<br/>log_2(1/8) = -3"]
    J --> K["Exponential form<br/>2^(-3) = 1/8"]
    A --> L["Domain reminder<br/>n must be positive"]
    L --> M["Logs can output negative numbers<br/>but log inputs cannot be zero or negative"]
```
