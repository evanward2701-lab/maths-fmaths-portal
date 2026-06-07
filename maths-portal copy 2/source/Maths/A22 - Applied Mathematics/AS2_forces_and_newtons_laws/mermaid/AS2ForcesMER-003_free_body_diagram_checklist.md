# AS2ForcesMER-003

**Asset ID:** AS2ForcesMER-003  
**Source:** Chapter 5/7 Forces transcript  
**Related lesson section:** Core Theory: Drawing force diagrams  
**Purpose:** Give a checklist for building a complete force diagram before calculation.

```mermaid
flowchart TD
    A["Read the mechanics scenario"] --> B["Identify the object or particle"]
    B --> C["Draw weight mg vertically downward"]
    C --> D{"Is the object on a surface?"}
    D -->|Yes| E["Draw normal reaction R perpendicular to surface"]
    D -->|No| F["No surface reaction"]
    E --> G{"Is there a string or cable?"}
    F --> G
    G -->|Yes| H["Draw tension T along the string away from the particle"]
    G -->|No| I["No tension force"]
    H --> J{"Is the surface rough?"}
    I --> J
    J -->|Yes| K["Draw friction opposing motion or tendency to move"]
    J -->|No| L["No friction force"]
    K --> M{"Are there applied forces?"}
    L --> M
    M -->|Yes| N["Draw applied forces with angle labels"]
    M -->|No| O["Check all standard forces included"]
    N --> P["Resolve angled forces"]
    O --> P
    P --> Q["Write equations"]
```
