# AS2StatisticalSamplingMER-001

## Asset Metadata

**Asset ID:** AS2StatisticalSamplingMER-001  
**Unit code:** AS2  
**Topic code:** AS2-SAMP  
**Topic name:** Statistical sampling  
**Topic ID:** AS2StatisticalSampling  
**Asset type:** Mermaid flowchart  
**Related lesson section:** Visual Asset Integration; Core Theory; Exam Technique Notes  
**Source:** CCEA AS2 Statistical sampling specification boundary + supplied Data Collection PDF/transcript evidence  
**Purpose:** Decision flowchart for choosing or critiquing a sampling method based on whether there is a sampling frame, whether the population has important strata, whether randomness is possible, and whether speed/convenience is prioritised.  
**Linked LO IDs:** AS2-SAMP-LO003, AS2-SAMP-LO004

```mermaid
flowchart TD
    A["Start: choose or critique a sampling method"] --> B{"Is the whole population tested?"}

    B -->|"Yes"| C["Census"]
    C --> C1["Advantage: should give a completely accurate result"]
    C --> C2["Disadvantages: time consuming, expensive, large volume of data"]
    C --> C3{"Does testing destroy or damage items?"}
    C3 -->|"Yes"| C4["Census unsuitable: use a sample instead"]
    C3 -->|"No"| C5["Census may be suitable if time, cost and data size are acceptable"]

    B -->|"No"| D["Use a sample"]
    D --> E{"Is there a complete sampling frame?"}

    E -->|"Yes"| F{"Are important groups or strata present?"}
    F -->|"Yes"| G["Stratified sampling"]
    G --> G1["Divide population into distinct strata"]
    G1 --> G2["Calculate each stratum sample size proportionally"]
    G2 --> G3["Randomly select within each stratum"]
    G3 --> G4["Strength: reflects population structure"]
    G4 --> G5["Critique: strata must be clear; random selection still needs a sampling frame"]

    F -->|"No"| H{"Is a fully random method practical?"}
    H -->|"Yes"| I["Simple random sampling"]
    I --> I1["Number each sampling unit"]
    I1 --> I2["Use a random number generator or lottery sampling"]
    I2 --> I3["Select the corresponding sampling units"]
    I3 --> I4["Strength: each unit has a known equal chance"]
    I4 --> I5["Critique: not suitable when population is very large"]

    H -->|"No"| J["Systematic sampling"]
    J --> J1["Calculate interval k = population size / sample size"]
    J1 --> J2["Choose a random starting point from 1 to k"]
    J2 --> J3["Select every kth item"]
    J3 --> J4["Strength: simple, quick, useful for large lists"]
    J4 --> J5["Critique: can introduce bias if the list has a pattern"]

    E -->|"No"| K{"Can quotas be set for important groups?"}
    K -->|"Yes"| L["Quota sampling"]
    L --> L1["Divide population into groups by characteristic"]
    L1 --> L2["Set quotas to reflect group proportions"]
    L2 --> L3["Interviewer selects units until quotas are full"]
    L3 --> L4["Strength: no sampling frame required"]
    L4 --> L5["Critique: non-random, so interviewer bias may occur"]

    K -->|"No"| M["Opportunity or convenience sampling"]
    M --> M1["Use people or items available at the time"]
    M1 --> M2["Strength: easy and inexpensive"]
    M2 --> M3["Critique: unlikely to be representative"]

    D --> N["Final critique check"]
    N --> N1{"Could different samples lead to different conclusions?"}
    N1 -->|"Yes"| N2["Mention sampling variability and representativeness"]
    N1 -->|"No or unclear"| N3["Still state any limits: size, bias, missing groups, missing frame"]
```

## Off-Spec Control Note

Systematic, quota and opportunity sampling are included as supporting method-selection and critique vocabulary because they appear in the supplied evidence. The named CCEA core methods remain simple random sampling and stratified sampling.
