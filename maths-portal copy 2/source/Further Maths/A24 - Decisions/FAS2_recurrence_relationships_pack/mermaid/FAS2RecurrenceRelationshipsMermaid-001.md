# FAS2RecurrenceRelationshipsMermaid-001

## Asset ID

`FAS2RecurrenceRelationshipsMermaid-001`

## Source

- CCEA FAS2-REC specification boundary.
- Uploaded recurrence relations transcript.
- Phase 1 lesson placeholder from Section 9.2.

## Related lesson section

`# 9. Visual Asset Integration`

## Used placeholder

```text
[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsMermaid-001 | Source: CCEA FAS2-REC specification boundary + uploaded recurrence transcript | Insert from mermaid/FAS2RecurrenceRelationshipsMermaid-001.md | Purpose: Show the full recurrence workflow: define variable, identify previous-term dependence, write recurrence relation, add initial conditions, generate terms, verify or solve for closed form.]
```

## Purpose

Show the complete recurrence workflow:

1. begin with a written context;
2. define the variable;
3. identify whether the recurrence is first-order or second-order;
4. write the recurrence relation;
5. add the required initial condition or initial conditions;
6. choose whether to generate, verify, solve or interpret;
7. warn that missing initial conditions mean the recurrence does not define one unique sequence.

## Creation notes

This diagram is designed as the student’s “recurrence control panel”. It keeps the modelling workflow separate from the solving workflow, then joins them at the decision point where the student chooses the task type.

The missing-initial-condition branch is deliberately shown as a red warning route, because the transcript repeatedly treats initial conditions as essential for generating the sequence or modelling context.

## Mermaid code

```mermaid
flowchart TD
    A["Written context<br/>sequence, money, dosage, population or counting"] --> B["Define the variable<br/>Example: u_n = state at step n"]
    B --> C["Identify the dependency<br/>Which earlier term or terms are used?"]

    C --> D{"Order of recurrence?"}

    D --> E["First-order recurrence<br/>uses u_(n-1)"]
    D --> F["Second-order recurrence<br/>uses u_(n-1) and u_(n-2)"]

    E --> G["Write the recurrence relation<br/>u_n = a u_(n-1) + g(n)"]
    F --> H["Write the recurrence relation<br/>u_n = a u_(n-1) + b u_(n-2) + g(n)"]

    G --> I["State one initial condition<br/>Example: u_0 or u_1"]
    H --> J["State two initial conditions<br/>Example: u_0 and u_1"]

    I --> K{"Initial condition supplied?"}
    J --> L{"Initial conditions supplied?"}

    K -- "No" --> M["Warning<br/>Not enough information for one unique sequence"]
    L -- "No" --> M

    K -- "Yes" --> N{"Task type?"}
    L -- "Yes" --> N

    N --> O["Generate terms<br/>Apply the rule repeatedly"]
    N --> P["Verify a closed form<br/>Substitute u_(n-1) or u_(n-2)"]
    N --> Q["Solve for a closed form<br/>Find a formula using n only"]
    N --> R["Interpret the model<br/>Check units, timing and limitations"]

    Q --> S{"Solving route"}

    S --> T["First-order homogeneous<br/>u_n = C a^n"]
    S --> U["First-order non-homogeneous with a = 1<br/>u_n = u_0 + sum from r = 1 to n of g(r)"]
    S --> V["First-order non-homogeneous with a not equal to 1<br/>Complementary function + particular solution"]
    S --> W["Second-order recurrence<br/>Use the auxiliary equation"]

    W --> X["Fibonacci-type relation<br/>u_n = u_(n-1) + u_(n-2)<br/>auxiliary equation: r^2 - r - 1 = 0"]

    R --> Y["Context check<br/>Does the model eventually give impossible values?"]
    Y --> Z["Example warning<br/>A loan model should not keep producing negative balances"]

    M --> AA["Fix the model<br/>Add the missing starting value or values"]
    AA --> N

    classDef main fill:#FAF9F6,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1px;
    classDef decision fill:#FFFFF0,stroke:#C5A059,color:#2C2C2E,stroke-width:1px;
    classDef warning fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1px;
    classDef method fill:#FFFFF0,stroke:#D4AF37,color:#2C2C2E,stroke-width:1px;

    class A,B,C,E,F,G,H,I,J,O,P,Q,R,T,U,V,W,X,Y,Z,AA main;
    class D,K,L,N,S decision;
    class M warning;
```

## Accessibility notes

- The diagram avoids colour-only meaning by using explicit text labels such as “Warning” and “Task type”.
- The missing-initial-condition path is labelled in words, not just colour.
- The notation uses plain text inside Mermaid labels to reduce rendering errors.

## Lesson integration note

Insert this asset at Section 9.2 of `FAS2_recurrence_relationships_lesson.md`.
