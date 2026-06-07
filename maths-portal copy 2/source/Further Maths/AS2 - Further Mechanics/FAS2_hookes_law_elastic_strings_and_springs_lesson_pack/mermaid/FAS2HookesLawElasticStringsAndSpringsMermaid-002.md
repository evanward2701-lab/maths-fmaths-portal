# Mermaid Asset: FAS2HookesLawElasticStringsAndSpringsMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2HookesLawElasticStringsAndSpringsMermaid-002` |
| Asset type | Mermaid decision tree |
| Source | FM1 Elastic Strings and Springs problem-solving evidence + linked CCEA `FAS2-WENG` work-energy boundary |
| Related lesson section | Section 8.17: When to use energy instead; Section 15.5: Choosing equations |
| Used placeholder | `FAS2HookesLawElasticStringsAndSpringsMermaid-002` |
| Purpose | Help students choose between Hooke's Law with force equations and the work-energy method. |
| Creation notes | Preserves the method distinction: acceleration and force need force equations; speed, distance and work usually call for energy. |

## Mermaid code

```mermaid
flowchart TD
    A["Start: What does the question ask for?"] --> B{"Main target quantity?"}
    B -->|Tension, thrust, force| C["Use Hooke's Law plus force equations"]
    B -->|Acceleration| D["Use F = ma plus Hooke's Law"]
    B -->|Equilibrium position| E["Use ΣF = 0 plus Hooke's Law"]
    B -->|Maximum speed position| F["Use a = 0<br/>Resultant force = 0"]
    B -->|Speed value| G["Use energy"]
    B -->|Greatest distance or maximum displacement| H["Use energy and set v = 0"]
    B -->|Work done| I["Use work-energy or ΔEPE"]
    C --> J["Write T = λx / l"]
    D --> J
    E --> J
    F --> J
    J --> K["Find x from geometry or length data"]
    K --> L["Build the mechanics equation"]
    L --> M["Solve for the unknown"]
    G --> N["Energy method"]
    H --> N
    I --> N
    N --> O["Write energy stores:<br/>KE = 1/2 mv²<br/>GPE = mgh<br/>EPE = λx² / 2l"]
    O --> P{"Are external forces or resistance present?"}
    P -->|Yes| Q["Include work in or work out:<br/>W = Fd"]
    P -->|No| R["Use conservation of mechanical energy"]
    Q --> S["Initial energy + work in<br/>=<br/>Final energy + work out"]
    R --> T["Initial KE + GPE + EPE<br/>=<br/>Final KE + GPE + EPE"]
    S --> U["Solve and interpret"]
    T --> U
    M --> U
    U --> V{"Final check"}
    V --> V1["Maximum speed? a = 0"]
    V --> V2["Greatest distance? v = 0"]
    V --> V3["Length asked? Use l + x, not just x"]
    V --> V4["Energy asked? Use joules"]
```
