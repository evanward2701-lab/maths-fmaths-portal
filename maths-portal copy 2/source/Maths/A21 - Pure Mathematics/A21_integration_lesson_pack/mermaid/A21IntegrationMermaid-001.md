# A21IntegrationMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21IntegrationMermaid-001 |
| Asset type | Mermaid flowchart |
| Lesson | A21 Integration |
| Related section | Exam Technique Notes |
| Source | CCEA specification map + Chapter 11 lesson evidence |
| Purpose | Help students choose an integration method. |

```mermaid
flowchart TD
    A["Start: inspect the integral"] --> B{"Standard result?"}
    B -- Yes --> B1["Use standard result"]
    B1 --> Z["Differentiate answer to check"]
    B -- No --> C{"Can it be simplified?"}
    C -- Yes --> C1["Simplify algebra/trig first"]
    C1 --> A
    C -- No --> D{"Inside linear ax+b?"}
    D -- Yes --> D1["Integrate normally, divide by a"]
    D1 --> Z
    D -- No --> E{"Trig identity?"}
    E -- Yes --> E1["Rewrite with identity"]
    E1 --> A
    E -- No --> F{"One part derivative of another?"}
    F -- Yes --> F1["Reverse chain rule: consider, differentiate, scale"]
    F1 --> Z
    F -- No --> G{"Product?"}
    G -- Yes --> G1["Integration by parts"]
    G1 --> Z
    G -- No --> H{"Rational expression?"}
    H -- Yes --> H1["Algebraic division or partial fractions"]
    H1 --> Z
    H -- No --> I{"Application?"}
    I -- Area --> I1["Top minus bottom"]
    I -- Sum --> I2["Limit of rectangle sum"]
    I -- Volume --> I3["V = pi integral y squared dx"]
    I -- DE --> I4["Separate variables, integrate, interpret"]
```
