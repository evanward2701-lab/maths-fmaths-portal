# Mermaid Asset: FAS2GroupTheoryMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2GroupTheoryMermaid-002` |
| Topic ID | `FAS2GroupTheory` |
| Related lesson file | `FAS2_group_theory_lesson.md` |
| Used placeholder | `FAS2GroupTheoryMermaid-002` |
| Source | Transcript proof and group-check examples |
| Purpose | Decide whether to prove a group or disprove it using one failed axiom. |

```mermaid
flowchart TD
    A["Does this set with this operation form a group?"] --> B{"Prove or disprove?"}
    B --> C["Prove group"]
    C --> C1["Use arbitrary a,b,c in G"]
    C1 --> C2["Show closure"]
    C2 --> C3["Find identity e"]
    C3 --> C4["Find inverse a^-1"]
    C4 --> C5["Prove associativity"]
    C5 --> C6["Conclude group"]
    B --> D["Disprove group"]
    D --> D1{"Can closure fail?"}
    D1 -- "Yes" --> D1A["Give a,b in G with a*b not in G"]
    D1 -- "No" --> D2{"Can identity fail?"}
    D2 -- "Yes" --> D2A["Show no two-sided identity"]
    D2 -- "No" --> D3{"Can inverse fail?"}
    D3 -- "Yes" --> D3A["Find one element with no inverse"]
    D3 -- "No" --> D4{"Can associativity fail?"}
    D4 -- "Yes" --> D4A["Give one counterexample"]
    D4 -- "No" --> C
```
