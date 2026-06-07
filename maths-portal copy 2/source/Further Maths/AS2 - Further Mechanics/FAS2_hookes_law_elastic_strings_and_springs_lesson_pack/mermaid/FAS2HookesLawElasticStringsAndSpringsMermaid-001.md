# Mermaid Asset: FAS2HookesLawElasticStringsAndSpringsMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2HookesLawElasticStringsAndSpringsMermaid-001` |
| Asset type | Mermaid flowchart |
| Source | CCEA Further Mathematics specification map + FM1 Elastic Strings and Springs lesson evidence |
| Related lesson section | Section 8: Core Theory; Section 15: Exam Technique Notes |
| Used placeholder | `FAS2HookesLawElasticStringsAndSpringsMermaid-001` |
| Purpose | Show the standard two-equation method for Hooke's Law problems. |
| Creation notes | AI-proposed teaching visual based on the evidence-backed method. |

## Mermaid code

```mermaid
flowchart TD
    A["Start: Read the problem carefully"] --> B["Draw a large mechanics diagram"]
    B --> C["Identify the elastic object"]
    C --> C1{"Is it a string or a spring?"}
    C1 -->|String| C2["String can pull only<br/>If compressed or slack: T = 0"]
    C1 -->|Spring| C3["Spring can pull or push<br/>Tension if stretched<br/>Thrust if compressed"]
    C2 --> D["Record the natural length l"]
    C3 --> D
    D --> E["Find current length L"]
    E --> F{"Is the object stretched or compressed?"}
    F -->|Stretched| G["Extension: x = L - l"]
    F -->|Compressed spring| H["Compression: x = l - L"]
    F -->|Natural length| I["x = 0, so elastic force = 0"]
    G --> J["Hooke's Law:<br/>T = λx / l"]
    H --> J
    I --> J
    B --> K["Write the mechanics equation"]
    K --> K1{"What type of problem is it?"}
    K1 -->|Equilibrium| K2["Use ΣF = 0"]
    K1 -->|Dynamics| K3["Use ΣF = ma"]
    K1 -->|Limiting friction| K4["Use F = μR and resolve forces"]
    K1 -->|Resolving forces| K5["Use components:<br/>Tsinθ, Tcosθ, etc."]
    J --> L["Connect elastic force to mechanics force"]
    K2 --> L
    K3 --> L
    K4 --> L
    K5 --> L
    L --> M["Solve the equation or simultaneous equations"]
    M --> N["Check the answer requested:<br/>extension x or total length l + x?"]
    N --> O["Check units:<br/>N for force, m for lengths, J for energy"]
    O --> P["Final answer with interpretation"]
```
