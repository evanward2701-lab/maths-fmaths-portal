# AS2ConstantAccelerationMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS2ConstantAccelerationMermaid-001 |
| file_name | AS2ConstantAccelerationMermaid-001.md |
| asset_type | Mermaid flowchart |
| source | CCEA specification map + Chapter 9 Constant Acceleration transcript |
| related lesson section | Visual and Interactive Asset Plan; Exam Technique Notes; Core Theory: SUVAT Formula Set |
| related LO IDs | AS2-KIN-LO003 |
| purpose | Help students choose the correct SUVAT equation by identifying which quantity is excluded |
| status | Written |

```mermaid
flowchart TD
    A["Start a constant-acceleration question"] --> B["Write the SUVAT list:<br/>s, u, v, a, t"]
    B --> C{"Is acceleration constant?"}
    C -- "No" --> D["Do not use SUVAT.<br/>Use graph methods or another model."]
    C -- "Yes" --> E{"Is a velocity-time graph given<br/>or requested?"}
    E -- "Yes" --> F["Use graph facts first:<br/>gradient = acceleration<br/>area = displacement or distance"]
    E -- "No" --> G["Fill in known values<br/>and mark the unknown with ?"]
    F --> G
    G --> H{"Do you have enough information?<br/>Usually 3 known quantities<br/>and 1 quantity to find."}
    H -- "No" --> I["Look for hidden information:<br/>rest means u = 0 or v = 0<br/>vertical gravity means a = +/-9.8<br/>meeting point means equal displacement"]
    I --> G
    H -- "Yes" --> J{"Which SUVAT quantity<br/>is NOT needed?"}
    J -- "Exclude s" --> K["Use:<br/>v = u + at"]
    J -- "Exclude a" --> L["Use:<br/>s = ((u + v) / 2)t"]
    J -- "Exclude t" --> M["Use:<br/>v^2 = u^2 + 2as"]
    J -- "Exclude v" --> N["Use:<br/>s = ut + (1/2)at^2"]
    J -- "Exclude u" --> O["Use:<br/>s = vt - (1/2)at^2"]
    K --> P["Substitute values before rearranging"]
    L --> P
    M --> P
    N --> P
    O --> P
    P --> Q["Solve carefully<br/>with units"]
    Q --> R{"Does the answer need<br/>a direction or interpretation?"}
    R -- "Yes" --> S["State direction clearly:<br/>negative velocity means opposite<br/>to the chosen positive direction"]
    R -- "No" --> T["Give final answer<br/>with correct units"]
    S --> T
```
