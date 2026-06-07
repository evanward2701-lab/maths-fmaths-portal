# Mermaid Asset: FAS2GroupTheoryMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2GroupTheoryMermaid-001` |
| Topic ID | `FAS2GroupTheory` |
| Related lesson file | `FAS2_group_theory_lesson.md` |
| Used placeholder | `FAS2GroupTheoryMermaid-001` |
| Source | CCEA FAS2-GROUP specification + transcript sections on group axioms |
| Purpose | Show the four group axioms as a decision process. |

```mermaid
flowchart TD
    A["Start with proposed structure<br/>(G, *)"] --> B{"Is * a binary operation<br/>on G?"}
    B -- "No" --> NG1["Not a group<br/>Binary operation / closure fails"]
    B -- "Yes" --> C{"Closure:<br/>For all a,b in G,<br/>is a*b in G?"}
    C -- "No" --> NG2["Not a group<br/>Closure fails"]
    C -- "Yes" --> D{"Identity:<br/>Is there e in G with<br/>a*e=e*a=a?"}
    D -- "No" --> NG3["Not a group<br/>Identity fails"]
    D -- "Yes" --> E{"Inverse:<br/>For every a in G,<br/>is there a^-1 in G with<br/>a*a^-1=a^-1*a=e?"}
    E -- "No" --> NG4["Not a group<br/>Inverse fails"]
    E -- "Yes" --> F{"Associativity:<br/>a*(b*c)=(a*b)*c?"}
    F -- "No" --> NG5["Not a group<br/>Associativity fails"]
    F -- "Yes" --> G["Group confirmed"]
```
