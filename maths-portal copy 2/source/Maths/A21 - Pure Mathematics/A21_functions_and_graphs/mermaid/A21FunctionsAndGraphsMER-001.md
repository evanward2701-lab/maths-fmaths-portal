# A21FunctionsAndGraphsMER-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `A21FunctionsAndGraphsMER-001` |
| Asset type | Mermaid diagram |
| Unit | A21: A2 1 Pure Mathematics |
| Topic code | A21-AF |
| Topic | Functions and Graphs |
| Related LO IDs | `A21-AF-LO002`, `A21-AF-LO003` |
| Related lesson section | Mappings, Functions, Domain and Range |
| Source | CCEA specification map; Chapter 2 Functions and Graphs transcript section on mappings/functions; P2 Chapter 2 slides on mapping, function, domain and range |
| Purpose | Compare a general mapping, a function, a one-to-one function and a many-to-one function. |
| Status | Final |

## Mermaid Code

```mermaid
flowchart LR

subgraph M["General mapping: allowed to be messy"]
  direction LR
  M0["Input: 0"] --> M44["Output: 4.4"]
  M0 --> M72["Output: 7.2"]
  M31["Input: 3.1"] --> M72
  Mnote["One input can map to multiple outputs, so this may fail to be a function."]
end

subgraph F["Function: every input has exactly one output"]
  direction LR
  F1["Input x1"] --> FY1["Output f(x1)"]
  F2["Input x2"] --> FY2["Output f(x2)"]
  F3["Input x3"] --> FY3["Output f(x3)"]
  Fnote["Each input has one, and only one, output."]
end

subgraph O["One-to-one function"]
  direction LR
  O1["Input a"] --> OA["Output p"]
  O2["Input b"] --> OB["Output q"]
  O3["Input c"] --> OC["Output r"]
  Onote["Each output comes from exactly one input."]
end

subgraph N["Many-to-one function"]
  direction LR
  N1["Input -2"] --> N4["Output 4"]
  N2["Input 2"] --> N4
  N3["Input 3"] --> N9["Output 9"]
  Nnote["Still a function: each input has one output. But two inputs may share one output."]
end
```
