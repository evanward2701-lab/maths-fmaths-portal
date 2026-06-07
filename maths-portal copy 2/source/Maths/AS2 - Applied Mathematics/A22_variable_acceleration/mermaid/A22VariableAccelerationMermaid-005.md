# A22VariableAccelerationMermaid-005

**Asset ID:** `A22VariableAccelerationMermaid-005`  
**Source:** Lesson PDF pages 12 and 13; transcript notes on negative areas and splitting journeys.  
**Related lesson section:** Core Theory 8.7; Worked Examples 9 and 10  
**Purpose:** Distinguish displacement from total distance travelled when velocity changes sign.

```mermaid
flowchart TD
    Start["Asked for displacement or distance?"]
    Type{"Question wording"}

    Disp["Displacement"]
    Dist["Distance travelled"]

    IntSigned["Calculate signed integral<br/>∫ v(t) dt over full interval"]
    Roots["Solve v(t)=0<br/>find direction-change times"]
    Split["Split interval at each valid root"]
    Areas["Find each signed area separately"]
    Abs["Take positive magnitude of each area"]
    Add["Add magnitudes"]

    DispAnswer["Signed displacement<br/>may be negative"]
    DistAnswer["Total distance<br/>always non-negative"]

    Start --> Type
    Type --> Disp --> IntSigned --> DispAnswer
    Type --> Dist --> Roots --> Split --> Areas --> Abs --> Add --> DistAnswer
```
