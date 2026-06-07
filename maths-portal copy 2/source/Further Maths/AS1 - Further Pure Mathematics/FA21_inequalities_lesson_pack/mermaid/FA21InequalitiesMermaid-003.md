# FA21InequalitiesMermaid-003

## Asset Metadata

| Field | Entry |
|---|---|
| Asset ID | FA21InequalitiesMermaid-003 |
| Asset type | Mermaid flowchart |
| Lesson file | FA21_inequalities_lesson.md |
| Related lesson section | Section 9.1 Mermaid assets; Section 8.8–8.10 Modulus inequalities; Section 11 Worked Examples 10–18 |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21InequalitiesMermaid-003 | Source: FP1 modulus inequalities transcript + PDF enrichment evidence | Insert from mermaid/FA21InequalitiesMermaid-003.md | Purpose: Flowchart for modulus inequalities: sketch |f(x)|, solve positive branch, solve negative branch, reject phantom roots, write solution.]` |
| Source | FP1 modulus inequalities transcript + PDF enrichment evidence |
| Boundary status | Internal portal enrichment, not official CCEA Further Mathematics specification content |
| Purpose | Show how modulus inequalities are solved by sketching, branch equations and validity checks. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with a modulus inequality"] --> B{"Is the modulus isolated?"}
    B -->|No| C["Rearrange to isolate the modulus if possible"]
    B -->|Yes| D["Identify f(x) inside modulus and comparison g(x)"]
    C --> D
    D --> E["Sketch y = f(x)"]
    E --> F["Reflect negative parts above x-axis"]
    F --> G["This gives sketch of y = |f(x)|"]
    G --> H["Sketch comparison graph y = g(x)"]
    H --> I["Find candidate boundary values"]
    I --> J["Positive branch: solve f(x) = g(x)"]
    I --> K["Negative branch: solve -f(x) = g(x)"]
    J --> L["Collect candidate roots from positive branch"]
    K --> M["Collect candidate roots from negative branch"]
    L --> N["Place all candidate roots on sketch"]
    M --> N
    N --> O{"Does each candidate lie on the branch that produced it?"}
    O -->|Yes| P["Keep as valid boundary"]
    O -->|No| Q["Reject as phantom root"]
    P --> R["Use graph to identify where |f(x)| satisfies inequality"]
    Q --> R
    R --> S{"Is inequality strict?"}
    S -->|Yes| T["Use open endpoints at valid boundaries"]
    S -->|No| U["Use closed endpoints if values are defined"]
    T --> V["Check for isolated touch points"]
    U --> V
    V --> W["Apply any domain restrictions"]
    W --> X["Write final solution set"]
```
