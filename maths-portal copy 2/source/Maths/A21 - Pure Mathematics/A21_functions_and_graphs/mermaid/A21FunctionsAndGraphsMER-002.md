# A21FunctionsAndGraphsMER-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `A21FunctionsAndGraphsMER-002` |
| Asset type | Mermaid diagram |
| Unit | A21: A2 1 Pure Mathematics |
| Topic code | A21-AF |
| Topic | Functions and Graphs |
| Related LO IDs | `A21-AF-LO004` |
| Related lesson section | Composite Functions |
| Source | CCEA specification map; Chapter 2 Functions and Graphs transcript section on composite functions; P2 Chapter 2 slides on composite functions |
| Purpose | Show that `gf(x)=g(f(x))` applies `f` first, then `g`, while `fg(x)=f(g(x))` applies `g` first, then `f`. |
| Status | Final |

## Mermaid Code

```mermaid
flowchart LR

subgraph Rule1["Composite rule: gf(x) = g(f(x))"]
  direction LR
  X1["Input x"] --> F1["Apply f"]
  F1 --> FX["Output f(x)"]
  FX --> G1["Apply g"]
  G1 --> GFX["Final output g(f(x)) = gf(x)"]
end

subgraph Rule2["Composite rule: fg(x) = f(g(x))"]
  direction LR
  X2["Input x"] --> G2["Apply g"]
  G2 --> GX["Output g(x)"]
  GX --> F2["Apply f"]
  F2 --> FGX["Final output f(g(x)) = fg(x)"]
end

subgraph Example["Example: f(x)=x²+1 and g(x)=4x−2"]
  direction TB
  E0["Start with x"]
  E0 --> E1["For fg(x), apply g first: g(x)=4x−2"]
  E1 --> E2["Then apply f: f(g(x))=(4x−2)²+1"]
  E2 --> E3["Expand: fg(x)=16x²−16x+5"]
  E0 --> E4["For gf(x), apply f first: f(x)=x²+1"]
  E4 --> E5["Then apply g: g(f(x))=4(x²+1)−2"]
  E5 --> E6["Simplify: gf(x)=4x²+2"]
end
```
