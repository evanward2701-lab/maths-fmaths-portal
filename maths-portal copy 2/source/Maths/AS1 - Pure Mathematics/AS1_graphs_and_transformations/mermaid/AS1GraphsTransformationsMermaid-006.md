# AS1GraphsTransformationsMermaid-006

## Asset ID
`AS1GraphsTransformationsMermaid-006`

## Source
CCEA AS1-AF boundary and DrFrost Chapter 4.

## Related Lesson Section
Syllabus Gap Check

## Purpose
Control what becomes core lesson content versus enrichment.

```mermaid
flowchart TD
    A["Evidence item from Chapter 4"] --> B{"Does CCEA AS1-AF include it?"}
    B -->|"Cubic polynomial sketch"| C["Core: AS1-AF-LO012"]
    B -->|"Reciprocal graph"| D["Core: AS1-AF-LO013"]
    B -->|"Graph intersection"| E["Core: AS1-AF-LO014 and AS1-AF-LO015"]
    B -->|"Simple transformation"| F["Core: AS1-AF-LO016"]
    B -->|"Quartic polynomial sketch"| G["Boundary risk"]
    B -->|"Quintic or higher polynomial sketch"| H["Off-spec extension"]
    B -->|"Cross-board extension question"| I["Check against CCEA outcome"]
    G --> J["Log as optional enrichment, not required core"]
    H --> K["Exclude from core lesson"]
    I --> L{"Matches CCEA outcome?"}
    L -->|"Yes"| M["Use as on-spec support and label source"]
    L -->|"No"| N["Exclude or mark enrichment only"]
```
