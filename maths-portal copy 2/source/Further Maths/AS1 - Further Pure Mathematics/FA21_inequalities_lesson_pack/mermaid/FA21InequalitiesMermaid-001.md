# FA21InequalitiesMermaid-001

## Asset Metadata

| Field | Entry |
|---|---|
| Asset ID | FA21InequalitiesMermaid-001 |
| Asset type | Mermaid flowchart |
| Lesson file | FA21_inequalities_lesson.md |
| Related lesson section | Section 9.1 Mermaid assets; Section 8.2 The denominator-squared method; Section 11 Worked Examples 1–4 |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21InequalitiesMermaid-001 | Source: FP1 inequalities transcript + PDF enrichment evidence | Insert from mermaid/FA21InequalitiesMermaid-001.md | Purpose: Flowchart for solving rational inequalities algebraically: identify exclusions, multiply by denominator squares, rearrange, factorise, find critical values, sketch, remove undefined values, write solution.]` |
| Source | FP1 inequalities transcript + PDF enrichment evidence |
| Boundary status | Internal portal enrichment, not official CCEA Further Mathematics specification content |
| Purpose | Show the safe algebraic workflow for rational inequalities, especially the denominator-squared method. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with a rational inequality"] --> B["Identify every denominator"]
    B --> C["Write excluded values from denominator = 0"]
    C --> D{"Are you about to multiply by an expression involving x?"}
    D -->|Yes| E{"Is the expression definitely positive on the domain?"}
    D -->|No| H["Continue with safe algebra"]
    E -->|No or unknown sign| F["Do NOT multiply directly by it"]
    F --> G["Multiply by squared denominator factors instead"]
    E -->|Yes| H
    G --> I["Squared denominator product is positive away from excluded values"]
    H --> I
    I --> J["Cancel factors carefully"]
    J --> K["Move everything to one side"]
    K --> L["Factorise before expanding where possible"]
    L --> M["Solve equality case to find critical values"]
    M --> N["Order critical values on a number line"]
    N --> O["Sketch transformed polynomial or build sign chart"]
    O --> P{"Which intervals satisfy the inequality sign?"}
    P --> Q["Select required intervals"]
    Q --> R["Remove excluded denominator values"]
    R --> S{"Are endpoints allowed?"}
    S -->|Strict sign or undefined value| T["Use open endpoint"]
    S -->|Weak sign and defined value| U["Use closed endpoint"]
    T --> V["Write final answer with OR or union"]
    U --> V
    V --> W["Final solution set"]
```
