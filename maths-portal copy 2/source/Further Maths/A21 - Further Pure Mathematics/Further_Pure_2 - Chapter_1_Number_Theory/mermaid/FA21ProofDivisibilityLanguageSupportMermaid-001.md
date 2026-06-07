# Mermaid Asset: FA21ProofDivisibilityLanguageSupportMermaid-001

## Asset ID

`FA21ProofDivisibilityLanguageSupportMermaid-001`

## Source

CCEA `FA21-PROOF-LO001` boundary + Phase 1 lesson core theory.

## Related Lesson Section

- `# 8. Core Theory`
- `# 9. Visual Asset Integration`
- `# 15. Exam Technique Notes`

## Used Placeholder

```text
[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportMermaid-001 | Source: CCEA `FA21-PROOF-LO001` + lesson core theory | Insert from mermaid/FA21ProofDivisibilityLanguageSupportMermaid-001.md | Purpose: Show the logical flow of a divisibility induction proof.]
```

## Purpose

Show the CCEA-core logical flow for a divisibility proof by mathematical induction.

## Creation Notes

This diagram deliberately keeps the route centred on induction. Divisor notation appears only as proof language support. Euclidean algorithm, modular arithmetic and other FP2 Number Theory methods are not included in this core proof flow.

## Mermaid Code

```mermaid
flowchart TD
    A["Define the statement<br/>P(n): d divides E_n"]
    B["Base case<br/>Prove P(1), or the first required value"]
    C["Inductive hypothesis<br/>Assume P(k) is true<br/>for some allowed integer k"]
    D["Translate divisibility<br/>d divides E_k means<br/>E_k = d t, where t is an integer"]
    E["Inductive target<br/>Prove P(k+1):<br/>d divides E_(k+1)"]
    F["Algebraic step<br/>Rewrite E_(k+1)<br/>using the hypothesis"]
    G["Factor the divisor<br/>E_(k+1) = d × integer expression"]
    H["Integer check<br/>State why the bracket is an integer"]
    I["Conclusion<br/>P(k) implies P(k+1)"]
    J["Final statement<br/>Therefore P(n) is true<br/>for all required n"]
    K["CCEA-core route<br/>Mathematical induction"]

    A --> B --> C --> D --> E --> F --> G --> H --> I --> J
    K -. guides .-> A
    K -. guides .-> C
    K -. guides .-> J

    classDef core fill:#FAF9F6,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef step fill:#FFFFF0,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef warning fill:#FBEFEF,stroke:#C5A059,stroke-width:1.5px,color:#2C2C2E;

    class K core;
    class A,B,C,E,F,I,J step;
    class D,G,H warning;
```
