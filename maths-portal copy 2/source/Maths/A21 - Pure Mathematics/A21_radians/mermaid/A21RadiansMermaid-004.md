# A21RadiansMermaid-004

## Asset metadata

- Asset ID: A21RadiansMermaid-004
- Unit code: A21
- Topic code: A21-TRIG
- Topic ID: A21Radians
- Source: CCEA A21-TRIG-LO001, Chapter 5 Radians transcript and P2 Chapter 5 Radians slide PDF
- Related lesson section: Core Theory 8.5 to 8.7, Worked Examples 4 to 10
- Purpose: Help students choose the correct radian geometry formula.
- Phase: Phase 2 Mermaid

```mermaid
flowchart TD
    A["Circle sector or arc question"] --> B{"What is being asked?"}
    B --> C["Arc length"]
    C --> C1["Use l = r theta"]
    B --> D["Sector area"]
    D --> D1["Use A = 1/2 r squared theta"]
    B --> E["Sector perimeter"]
    E --> E1["Use P = 2r + r theta"]
    B --> F["Segment area"]
    F --> F1["Use segment = sector minus triangle"]
    F1 --> F2["Use 1/2 r squared theta minus 1/2 r squared sin theta"]
    F2 --> F3["So segment = 1/2 r squared bracket theta minus sin theta"]
    B --> G["Unknown angle"]
    G --> G1["Use l = r theta if arc length known"]
    G --> G2["Use trig or cosine rule if chord/radii known"]
    C1 --> H["Check theta is in radians"]
    D1 --> H
    E1 --> H
    F3 --> H
    G1 --> H
    G2 --> H
```
