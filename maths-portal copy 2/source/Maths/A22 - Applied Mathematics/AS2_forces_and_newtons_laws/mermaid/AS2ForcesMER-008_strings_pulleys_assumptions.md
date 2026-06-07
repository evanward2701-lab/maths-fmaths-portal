# AS2ForcesMER-008

**Asset ID:** AS2ForcesMER-008  
**Source:** Chapter 5/7 Forces transcript + MechYr2 Chapter 7 Applications of Forces PDF  
**Related lesson section:** Core Theory: Strings, pulleys and connected particles  
**Purpose:** Separate common modelling assumptions for strings, beads and pulleys.

```mermaid
flowchart TD
    A["String or pulley model"] --> B{"Single light inextensible string?"}
    B -->|Yes| C["Use one string model"]
    B -->|No| D["Use separate tensions if separate strings"]
    C --> E{"Smooth pulley or smooth bead?"}
    E -->|Yes| F["Tension same throughout string"]
    E -->|No or not stated| G["Do not assume same tension without justification"]
    C --> H["Inextensible means connected particles have linked acceleration"]
    H --> I["Same magnitude of acceleration along string"]
    D --> J["Use T1, T2, ..."]
    F --> K["Use common T"]
    G --> L["State assumption or use separate variables"]
```
