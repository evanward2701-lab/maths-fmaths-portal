# FA21FurtherCalculusMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA21FurtherCalculusMermaid-001` |
| Asset type | Mermaid diagram |
| Related lesson file | `FA21_further_calculus_lesson.md` |
| Related lesson section | Section 9.2 Boundary decision flow |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21FurtherCalculusMermaid-001 | Source: CCEA Further Mathematics specification map + uploaded FP1 Methods in Calculus evidence | Insert from mermaid/FA21FurtherCalculusMermaid-001.md | Purpose: Decide whether a method is CCEA-core, boundary-risk, bridge-only or optional enrichment.]` |
| Source | CCEA Further Mathematics specification map + uploaded FP1 Methods in Calculus PDF/transcript |
| Purpose | Decide whether a method belongs in CCEA-core Further calculus, bridge context, optional enrichment, or the missing evidence log. |
| Boundary note | Leibnitz’s theorem, L’Hospital’s rule and Weierstrass substitution are treated as enrichment / boundary-risk content because they were present in uploaded FP1 evidence but not explicitly confirmed in the supplied CCEA `FA21-FCALC` LO list. |

## Creation notes

This diagram is a syllabus-boundary guardrail. It is designed to stop a student from importing a cross-board method into the CCEA-core lesson merely because it appears in the uploaded lesson evidence.

## Mermaid code

```mermaid
flowchart TD
    A["Start: calculus method or technique"] --> B{"Is it explicitly listed in supplied CCEA FA21-FCALC LOs?"}
    B -->|"Yes"| C["Teach as CCEA-core Further calculus"]
    C --> C1["Examples from supplied LO list:<br/>FA21-FCALC-LO001 Improper integrals<br/>FA21-FCALC-LO002 Partial fractions with quadratic factors<br/>FA21-FCALC-LO003 Inverse trig differentiation<br/>FA21-FCALC-LO004 Trig substitutions<br/>FA21-FCALC-LO005 Repeated integration by parts<br/>FA21-FCALC-LO006 Reduction formulae"]
    B -->|"No"| D{"Is it ordinary A-Level Maths prerequisite content?"}
    D -->|"Yes"| E["Use as bridge context only"]
    E --> E1["Bridge examples:<br/>Product rule<br/>Chain rule<br/>Substitution<br/>Integration by parts<br/>Partial fractions basics<br/>Trig identities<br/>Exponentials and logarithms"]
    D -->|"No"| F{"Is it in the uploaded FP1 Methods in Calculus evidence?"}
    F -->|"Yes"| G["Preserve as optional enrichment / boundary-risk"]
    G --> G1["Uploaded FP1 enrichment examples:<br/>Leibnitz's theorem<br/>L'Hospital's rule<br/>Weierstrass substitution"]
    F -->|"No"| H["Do not teach as core"]
    H --> H1["Record in Missing Evidence Log<br/>or Off-Spec / Boundary-Risk Log"]
    C1 --> I["Lesson content status recorded"]
    E1 --> I
    G1 --> I
    H1 --> I
    I --> J["Final rule:<br/>CCEA specification boundary wins"]
```

## Accessibility text description

This flowchart begins with a calculus method or technique and asks whether it is explicitly listed in the supplied CCEA `FA21-FCALC` learning outcomes. If it is, it is taught as CCEA-core Further calculus. If not, the diagram checks whether it is ordinary A-Level Mathematics prerequisite content, in which case it becomes bridge context only. If it is not bridge content, the diagram checks whether it appears in the uploaded FP1 Methods in Calculus evidence. If so, it is preserved as optional enrichment or boundary-risk content. If not, it is not taught as core and is logged as missing or off-spec evidence. The final rule is that the CCEA specification boundary wins.
