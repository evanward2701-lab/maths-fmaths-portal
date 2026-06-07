# AS1ExponentialsAndLogarithmsMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1ExponentialsAndLogarithmsMermaid-003 |
| Asset type | Mermaid diagram |
| Suggested file path | `mermaid/AS1ExponentialsAndLogarithmsMermaid-003.md` |
| Unit code | AS1 |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Related lesson section | Core Theory 1-7; Worked Examples 1-4; Exam Technique Notes |
| Source | CCEA AS1 Exponentials and logarithms specification boundary; Chapter 14 lesson PDF and transcript |
| Purpose | Provide a sketching checklist for exponential graphs, including shape, intercept and asymptote. |

```mermaid
flowchart TD
    A["Sketch an exponential graph"] --> B["Identify the base and exponent structure"]
    B --> C{"Is the graph based on a^x with a > 1?"}
    C -->|"Yes"| D["Growth shape<br/>Graph increases left to right"]
    C -->|"No"| E{"Is the graph based on 0 < a < 1<br/>or a negative exponent such as e^(-x)?"}
    E -->|"Yes"| F["Decay shape<br/>Graph decreases left to right"]
    E -->|"No"| G["Rewrite if possible<br/>Example: (1/2)^x = 2^(-x)"]
    D --> H["Find the y-intercept"]
    F --> H
    G --> H
    H --> I["Set x = 0"]
    I --> J["Calculate y exactly"]
    J --> K["Find the horizontal asymptote"]
    K --> L{"Has the graph been shifted up or down?"}
    L -->|"No"| M["Asymptote is usually y = 0"]
    L -->|"Yes"| N["Move the asymptote by the same vertical shift<br/>Example: y = 2 + e^(x/3) has asymptote y = 2"]
    M --> O["Draw and label the sketch"]
    N --> O
    O --> P["Check: shape, intercept, asymptote, labels"]
```
