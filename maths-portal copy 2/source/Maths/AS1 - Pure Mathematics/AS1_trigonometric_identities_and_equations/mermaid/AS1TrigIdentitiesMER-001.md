# Mermaid Asset: AS1TrigIdentitiesMER-001

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1TrigIdentitiesMER-001 |
| asset_type | Mermaid flowchart |
| unit_code | AS1 |
| topic_code | AS1-TRIG |
| topic_name | Trigonometric Identities and Equations |
| related_lesson_file | AS1_trigonometric_identities_and_equations_lesson.md |
| related_lesson_section | Core Theory: Proof strategy for identities; Worked Examples: identity proofs |
| source | CCEA AS1 Trigonometry specification boundary + Chapter 10 lesson PDF pages 12-15 + transcript videos 8-10 |
| purpose | Show a student decision path for proving trigonometric identities using \(\tan\theta=\frac{\sin\theta}{\cos\theta}\), \(\sin^2\theta+\cos^2\theta=1\), algebraic fraction combining, and final RHS matching. |
| status | Written |
| off_spec_notes | None. This is core AS1 content because the CCEA AS1 trigonometry boundary includes using \(\sin^2\theta+\cos^2\theta=1\) for proving identities. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with the identity to prove"] --> B{"Which side looks messier?"}
    B -->|"Left-hand side"| C["Start from LHS"]
    B -->|"Right-hand side"| D["Start from RHS"]
    B -->|"Both look similar"| E["Choose the side containing more terms, fractions, or tan"]
    C --> F["Write the chosen side clearly"]
    D --> F
    E --> F
    F --> G{"Does the expression contain tan?"}
    G -->|"Yes"| H["Use tan(theta) = sin(theta) / cos(theta)"]
    G -->|"No"| I["Keep current sine and cosine form"]
    H --> J{"Are there added or subtracted fractions?"}
    I --> J
    J -->|"Yes"| K["Find a common denominator"]
    K --> L["Combine into one fraction"]
    J -->|"No"| M["Simplify products, powers, or common factors"]
    L --> N{"Can you use sin^2(theta) + cos^2(theta) = 1?"}
    M --> N
    N -->|"Yes, numerator has sin^2 + cos^2"| O["Replace sin^2(theta) + cos^2(theta) with 1"]
    N -->|"Yes, expression has 1 - sin^2"| P["Replace 1 - sin^2(theta) with cos^2(theta)"]
    N -->|"Yes, expression has 1 - cos^2"| Q["Replace 1 - cos^2(theta) with sin^2(theta)"]
    N -->|"Not yet"| R["Factorise, expand, cancel, or rewrite powers carefully"]
    R --> N
    O --> S["Simplify fully"]
    P --> S
    Q --> S
    S --> T{"Does it now match the other side?"}
    T -->|"Yes"| U["State: chosen side = other side"]
    U --> V["Therefore the identity is proven"]
    T -->|"No"| W{"Is there another legal identity or algebra step?"}
    W -->|"Yes"| R
    W -->|"No"| X["Pause: check algebra, brackets, signs, and whether you chose the better side"]
    X --> B
```

## Student-Facing Caption

When proving a trigonometric identity, do not try to solve for \(\theta\). An identity proof is a tidy-up mission: choose one side, usually the messier side, then rewrite it until it becomes the other side.

The main moves in this chapter are:

\[
\tan\theta=\frac{\sin\theta}{\cos\theta},
\]

\[
\sin^2\theta+\cos^2\theta=1,
\]

\[
1-\sin^2\theta=\cos^2\theta,
\]

\[
1-\cos^2\theta=\sin^2\theta.
\]

The final line should clearly show \(\text{LHS}=\text{RHS}\).
