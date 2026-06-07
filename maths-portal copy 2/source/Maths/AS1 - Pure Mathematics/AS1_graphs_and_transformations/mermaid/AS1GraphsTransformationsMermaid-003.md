# AS1GraphsTransformationsMermaid-003

## Asset ID
`AS1GraphsTransformationsMermaid-003`

## Source
CCEA AS1-AF-LO013 and DrFrost reciprocal graph evidence.

## Related Lesson Section
Core Theory → Reciprocal Graphs

## Purpose
Classify reciprocal graphs and identify asymptotes.

```mermaid
flowchart TD
    A["Start: reciprocal graph"] --> B{"Which form?"}
    B -->|"y = a / x"| C["Standard reciprocal"]
    B -->|"y = a / x^2"| D["Squared reciprocal"]
    B -->|"y = a / (x + h)"| E["Translated reciprocal"]
    B -->|"y = a / (x + h)^2"| F["Translated squared reciprocal"]
    C --> C1{"Sign of a?"}
    C1 -->|"a > 0"| C2["Branches in quadrants 1 and 3"]
    C1 -->|"a < 0"| C3["Branches in quadrants 2 and 4"]
    C2 --> C4["Asymptotes: x = 0 and y = 0"]
    C3 --> C4
    D --> D1{"Sign of a?"}
    D1 -->|"a > 0"| D2["Both branches above x-axis"]
    D1 -->|"a < 0"| D3["Both branches below x-axis"]
    D2 --> D4["Asymptotes: x = 0 and y = 0"]
    D3 --> D4
    E --> E1["Vertical asymptote: x = -h"]
    E1 --> E2["Horizontal asymptote: y = 0"]
    E2 --> E3["Check intercepts after transformation"]
    F --> F1["Vertical asymptote: x = -h"]
    F1 --> F2["Horizontal asymptote: y = 0"]
    F2 --> F3["Check branch position using sign of a"]
```
