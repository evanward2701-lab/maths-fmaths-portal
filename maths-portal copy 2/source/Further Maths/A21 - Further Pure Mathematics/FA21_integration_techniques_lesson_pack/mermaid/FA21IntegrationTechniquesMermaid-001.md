# Mermaid Asset: FA21IntegrationTechniquesMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA21IntegrationTechniquesMermaid-001` |
| Unit | `FA21` Further A2 1 Pure Mathematics |
| Topic code | `FA21-FCALC` |
| Topic ID | `FA21IntegrationTechniques` |
| Related lesson file | `FA21_integration_techniques_lesson.md` |
| Related lesson section | `# 9. Visual Asset Integration` |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21IntegrationTechniquesMermaid-001 | Source: CCEA Further Mathematics specification boundary + transcript reduction formula examples | Insert from mermaid/FA21IntegrationTechniquesMermaid-001.md | Purpose: Show the decision process for choosing between integration by parts, trig identity reshaping, reverse chain rule, and recurrence substitution.]` |
| Source | CCEA Further Mathematics specification boundary + teacher transcript reduction formula examples |
| Evidence status | AI-generated Mermaid teaching visual based on on-spec reduction formula evidence |
| Purpose | Show the decision process for choosing between integration by parts, trig identity reshaping, reverse chain rule, and recurrence substitution. |

## Creation Notes

This diagram is a decision map for reduction formula questions. It keeps arc length and surface area outside the core flow because those topics were logged as boundary-risk in Phase 0 and Phase 1.

## Mermaid Code

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#FAF9F6", "primaryColor": "#FAF9F6", "primaryTextColor": "#2C2C2E", "primaryBorderColor": "#E5E5EA", "lineColor": "#C5A059", "secondaryColor": "#FFFFF0", "tertiaryColor": "#FBEFEF", "fontFamily": "Inter, Arial, sans-serif"}}}%%
flowchart TD
    A["Start with an indexed integral<br/>I_n"] --> B["Write the definition clearly"]
    B --> C{"What type of structure is visible?"}
    C --> D["Polynomial times exponential"]
    C --> E["Power of sine or cosine"]
    C --> F["Power of tan, cot, sec, or cosec"]
    C --> G["Definite integral with limits"]
    C --> H["Difference of indexed integrals"]
    D --> D1["Try integration by parts"] --> D2["Choose u = polynomial power<br/>Choose v' = remaining easy factor"] --> D3["Differentiate u so the power drops"] --> D4["Look for I_{n-1}"] --> R["Rewrite in I-notation"]
    E --> E1["Split the power"] --> E2["Example: sin^n x = sin^{n-1}x sin x"] --> E3["Use integration by parts"] --> E4["Use identity: cos^2 x = 1 - sin^2 x"] --> E5["Look for I_{n-2} and I_n"] --> R
    F --> F1{"Can a square identity help?"}
    F1 --> F2["tan^2 x = sec^2 x - 1"] --> F5["Use reverse chain rule"] --> R
    F1 --> F3["cot^2 x = cosec^2 x - 1"] --> F6["Use reverse chain rule or integration by parts"] --> R
    F1 --> F4["Use integration by parts if identity route stalls"] --> F7["Choose v' to integrate cleanly"] --> R
    G --> G1["Apply same reduction method first"] --> G2["Keep the boundary term"] --> G3["Evaluate endpoints exactly"] --> G4{"Does boundary term vanish?"}
    G4 -->|Yes| G5["Write simplified definite recurrence"] --> R
    G4 -->|No| G6["Keep boundary contribution"] --> R
    H --> H1["Write both indexed integrals"] --> H2["Combine into one integral"] --> H3["Use suitable identity"] --> H4["Cancel common factors"] --> H5["Integrate simplified expression"] --> R
    R --> S{"Does I_n appear on both sides?"}
    S -->|Yes| T["Collect all I_n terms on the left"] --> V["Factorise I_n"] --> W["Divide to make I_n the subject"]
    S -->|No| U["Move directly to recurrence use"] --> W
    W --> X{"Need to calculate a value?"}
    X -->|Yes| Y["Build recurrence chain"] --> Y1{"Odd or even chain?"}
    Y1 -->|Odd| Y2["Use odd base case"] --> AA["Substitute carefully and keep exact values"]
    Y1 -->|Even| Y3["Use even base case"] --> AA
    X -->|No| Z["State reduction formula clearly"] --> AB["Final answer"]
    AA --> AB
    AB --> AC["Exam check: define I_n, show method, identify earlier I-terms, handle limits"]
```
