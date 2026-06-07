# Mermaid Asset: FAS2DiscreteRandomVariablesMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2DiscreteRandomVariablesMermaid-001` |
| Asset type | Mermaid flowchart |
| Source | CCEA FAS2-DIST specification boundary + uploaded transcript method flow + Phase 1 lesson structure |
| Related lesson section | `# 9. Visual Asset Integration`, `# 8. Core Theory`, `# 15. Exam Technique Notes` |
| Used placeholder | `FAS2DiscreteRandomVariablesMermaid-001` |
| Purpose | Show the decision pathway for solving a discrete random variable table question. |
| Evidence-backed? | AI-proposed visual structure based on evidence-backed methods. |
| CCEA boundary | Supports `FAS2-DIST-LO002`, `FAS2-DIST-LO003`, and `FAS2-DIST-LO006`. |

## Creation Notes

This Mermaid flowchart is designed for the lesson section on discrete random variable method selection.

## Mermaid Code

```mermaid
flowchart TD
    A["Start: read the discrete random variable table<br/>Identify outcomes x and probabilities P(X=x)"]
    A --> B{"Are all probabilities known?"}
    B -- "No" --> C["Use ∑P(X=x)=1<br/>Form the first equation"]
    C --> D{"Is E(X), Var(X), or E(X²) given?"}
    D -- "E(X) given" --> E["Use E(X)=∑xP(X=x)<br/>Form another equation"]
    D -- "Var(X) given" --> F["Use Var(X)=E(X²)-[E(X)]²"]
    D -- "E(X²) given" --> G["Use E(X²)=∑x²P(X=x)"]
    D -- "No extra information" --> H["Not enough information yet"]
    E --> I["Solve simultaneous equations<br/>Check each probability is between 0 and 1"]
    F --> I
    G --> I
    B -- "Yes" --> J["Check probabilities sum to 1"]
    I --> J
    J --> K{"What is the question asking for?"}
    K -- "Probability such as P(a ≤ X ≤ b)" --> L["Select only listed outcomes satisfying the inequality<br/>Add their probabilities"]
    K -- "Expected value E(X)" --> M["Use E(X)=∑xP(X=x)"]
    K -- "E(X²)" --> N["Square each outcome first<br/>Use E(X²)=∑x²P(X=x)"]
    K -- "Variance Var(X)" --> O["Find E(X) and E(X²)<br/>Use Var(X)=E(X²)-[E(X)]²"]
    K -- "Standard deviation" --> P["Use σ=√Var(X)"]
    K -- "Linear coding Y=aX+b" --> Q["Use E(Y)=aE(X)+b<br/>Use Var(Y)=a²Var(X)"]
    K -- "Probability involving Y" --> R["Substitute Y=aX+b<br/>Solve for X<br/>Read from X table"]
    Q --> S{"Is the transformation linear?"}
    S -- "Yes" --> T["Linear coding rules are valid"]
    S -- "No" --> U["Do not use E(f(X))=f(E(X))<br/>Apply the function to each outcome"]
    L --> V["Final check: probability between 0 and 1"]
    M --> W["Final check: E(X) is long-run mean"]
    N --> X["Final check: E(X²) is not usually [E(X)]²"]
    O --> Y["Final check: variance cannot be negative"]
    P --> Z["Final check: standard deviation has original units"]
    R --> V
    T --> AA["Final check: variance scaled by a², not a"]
    U --> X
```
