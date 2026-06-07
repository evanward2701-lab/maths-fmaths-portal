# Mermaid Asset: FA22GameTheoryEnrichmentMermaid-001

## Asset Metadata

| Field | Entry |
|---|---|
| Asset ID | `FA22GameTheoryEnrichmentMermaid-001` |
| Asset type | Mermaid flowchart |
| Lesson file | `FA22_game_theory_enrichment_lesson.md` |
| Related lesson section | `# 9. Visual Asset Integration` |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentMermaid-001 | Source: CCEA boundary check + Decision 2 transcript evidence | Insert from mermaid/FA22GameTheoryEnrichmentMermaid-001.md | Purpose: Show that Game Theory is optional enrichment and map the learning flow from pay-off matrices to mixed strategies and linear programming.]` |
| Source | CCEA boundary check + Decision 2 transcript evidence |
| Core CCEA status | Optional enrichment only |
| Purpose | Show that Game Theory is not confirmed as official CCEA Further Mathematics content, then map the enrichment learning flow from pay-off matrices to mixed strategies and linear programming. |

## Mermaid Code

```mermaid
flowchart TD
    A["CCEA Further Maths boundary check"] --> B{"Official CCEA Game Theory<br/>topic code or LO found?"}
    B -->|No| C["Game Theory must be labelled<br/>Optional Enrichment"]
    B -->|Yes, if later supplied| D["Reclassify only after official<br/>CCEA evidence is provided"]
    C --> E["Enrichment Topic ID:<br/>FA22GameTheoryEnrichment"]
    E --> F["Pay-off matrices"]
    F --> G["Read each entry from<br/>player A's point of view"]
    G --> H["Zero-sum games:<br/>A's gain plus B's gain equals 0"]
    H --> I["Play-safe strategies"]
    I --> J["For A:<br/>row minima then row maximin"]
    I --> K["For B:<br/>column maxima then column minimax"]
    J --> L["Stable solution theorem"]
    K --> L
    L --> M{"Row maximin equals<br/>column minimax?"}
    M -->|Yes| N["Stable solution"]
    N --> O["Saddle point:<br/>smallest in its row<br/>largest in its column"]
    O --> P["Value of game to A<br/>is the common value"]
    M -->|No| Q["Unstable game"]
    Q --> R["Dominance reduction"]
    R --> S["Delete dominated rows<br/>or dominated columns"]
    S --> T{"Can one player be reduced<br/>to two strategies?"}
    T -->|Yes| U["Mixed strategies"]
    U --> V["Use p and 1 minus p"]
    V --> W["Expected winnings lines"]
    W --> X["Graphical method:<br/>choose highest minimum winning"]
    T -->|No| Y["Linear programming enrichment"]
    Y --> Z["Augment matrix if needed<br/>so entries are positive"]
    Z --> AA["Define probabilities p1, p2, p3"]
    AA --> AB["Maximise augmented value V"]
    AB --> AC["Undo augmentation:<br/>original value v = V minus k"]
    X --> AD["Final enrichment warning:<br/>Not core CCEA unless official<br/>CCEA evidence is later supplied"]
    AC --> AD
    P --> AD
```
