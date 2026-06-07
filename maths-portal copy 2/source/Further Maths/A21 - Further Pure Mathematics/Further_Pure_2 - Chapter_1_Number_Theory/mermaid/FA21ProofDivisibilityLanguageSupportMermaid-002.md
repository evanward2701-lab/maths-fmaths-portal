# Mermaid Asset: FA21ProofDivisibilityLanguageSupportMermaid-002

## Asset ID

`FA21ProofDivisibilityLanguageSupportMermaid-002`

## Source

CCEA Further Mathematics specification boundary + uploaded FP2 Number Theory evidence + Phase 1 syllabus gap check.

## Related Lesson Section

- `# 3. Specification Alignment`
- `# 9. Visual Asset Integration`
- `# 16. Syllabus Gap Check`
- `# 17. Recommended Enhancements Not in the Evidence`

## Used Placeholder

```text
[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportMermaid-002 | Source: CCEA Further Maths specification boundary + uploaded FP2 Number Theory evidence | Insert from mermaid/FA21ProofDivisibilityLanguageSupportMermaid-002.md | Purpose: Help students see which uploaded Number Theory topics are core, support, or enrichment.]
```

## Purpose

Show the boundary between the CCEA-core proof outcome, support material from the uploaded Number Theory evidence, off-spec enrichment, and future split-topic content.

## Creation Notes

This diagram is a guardrail map. It prevents the uploaded FP2 Number Theory chapter from being silently treated as an official CCEA Number Theory topic. The only CCEA-core anchor used in this lesson is `FA21-PROOF-LO001`.

## Mermaid Code

```mermaid
flowchart TD
    A["Uploaded FP2 Number Theory evidence"]
    B["CCEA-core anchor<br/>FA21-PROOF-LO001"]
    C["Mathematical induction<br/>Core lesson route"]
    D["Divisor notation<br/>a divides b, a does not divide b, gcd, coprime"]
    E["Direct divisibility proof<br/>a divides b and a divides c<br/>therefore a divides bn + cm"]
    F["Division algorithm"]
    G["Euclidean algorithm"]
    H["Reverse Euclidean algorithm<br/>and Bezout-style identity"]
    I["Modular arithmetic"]
    J["Solving congruence equations"]
    K["Fermat's little theorem"]
    L["Divisibility tests"]
    M["Combinatorics"]
    N["Support for proof language<br/>Use cautiously in FA21 lesson"]
    O["Optional enrichment only<br/>Not CCEA core in this lesson"]
    P["Future split-topic check<br/>FAS2 Probability or FA22 Generating Functions<br/>where official LO evidence supports it"]

    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
    A --> I
    A --> J
    A --> K
    A --> L
    A --> M

    B --> C

    D --> N
    E --> N
    N -. supports .-> C

    F --> O
    G --> O
    H --> O
    I --> O
    J --> O
    K --> O
    L --> O

    M --> P

    classDef core fill:#FAF9F6,stroke:#D4AF37,stroke-width:2px,color:#2C2C2E;
    classDef support fill:#FFFFF0,stroke:#C5A059,stroke-width:1.5px,color:#2C2C2E;
    classDef enrich fill:#FBEFEF,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;
    classDef split fill:#FAF9F6,stroke:#E5E5EA,stroke-width:1.5px,color:#2C2C2E;

    class B,C core;
    class D,E,N support;
    class F,G,H,I,J,K,L,O enrich;
    class M,P split;
    class A split;
```
