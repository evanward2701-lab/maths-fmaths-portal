# Mermaid Asset: FA22SimplexAlgorithmTableauMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | FA22SimplexAlgorithmTableauMermaid-001 |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | FA22-ALGGRAPH |
| Topic ID | FA22SimplexAlgorithmTableau |
| Related LO | FA22-ALGGRAPH-LO003 |
| Related lesson file | FA22_simplex_algorithm_tableau_lesson.md |
| Related lesson section | #9. Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauMermaid-001 | Source: CCEA FA22-ALGGRAPH-LO003 + Decision 1 simplex tableau evidence + teacher transcript | Insert from mermaid/FA22SimplexAlgorithmTableauMermaid-001.md | Purpose: Show the full two-variable simplex tableau algorithm as a decision flow.]` |
| Source | CCEA FA22-ALGGRAPH-LO003 + Decision 1 simplex tableau evidence + teacher transcript |
| Purpose | Show the full two-variable simplex tableau algorithm as a decision flow. |
| Creation status | Generated in Phase 2 |
| On-spec status | Core CCEA Further Mathematics content, restricted to two-variable linear programming problems. |

## Creation notes

This Mermaid flowchart represents the simplex tableau algorithm for two-variable CCEA FA22 linear programming problems.

It deliberately excludes:

- three-variable simplex;
- four-variable simplex;
- integer solutions;
- two-stage simplex;
- Big-M method;
- artificial variables.

The algorithm follows the lesson convention:

\[
P=ax+by
\]

is rewritten as

\[
P-ax-by=0.
\]

For a maximisation tableau, the pivot column is selected from the most negative entry in the objective row.

Theta values are calculated only from rows with a positive pivot-column entry:

\[
\theta=\frac{\text{value entry}}{\text{positive pivot-column entry}}.
\]

The tableau is optimal when no negative entries remain in the objective row.

## Mermaid code

```mermaid
flowchart TD
    A["Start: two-variable linear programming problem"] --> B["Define decision variables x and y clearly in context"]
    B --> C["Write objective function, for example P = ax + by"]
    C --> D["Write constraints, for example αx + βy ≤ c and γx + δy ≤ d"]
    D --> E["Add non-negativity constraints: x ≥ 0, y ≥ 0"]
    E --> F["Introduce a separate slack variable for each ≤ constraint"]
    F --> G["Convert inequalities into equations"]
    G --> G1["Example: αx + βy + r = c"]
    G1 --> G2["Example: γx + δy + s = d"]
    G2 --> H["Write objective in tableau standard form"]
    H --> H1["Example: P = ax + by becomes P - ax - by = 0"]
    H1 --> I["Build the initial simplex tableau"]
    I --> J["Initial basic variables are usually slack variables and P"]
    J --> K["Read non-basic decision variables as x = 0 and y = 0"]
    K --> L{"Are there any negative entries in the objective row?"}

    L -- "No" --> M["Tableau is optimal"]
    M --> N["Read basic variable values from the value column"]
    N --> O["Set non-basic variables equal to 0"]
    O --> P["State x, y and the optimal value of P"]
    P --> Q["Interpret the answer in the original context"]
    Q --> R["Finish"]

    L -- "Yes" --> S["Choose the most negative objective-row entry"]
    S --> T["This gives the pivot column"]
    T --> U["Calculate theta values for valid constraint rows"]
    U --> V["theta = value entry ÷ positive pivot-column entry"]
    V --> W{"Are there positive theta values?"}
    W -- "No" --> X["No finite optimum in this improving direction"]
    X --> R

    W -- "Yes" --> Y["Choose the smallest positive theta"]
    Y --> Z["This gives the pivot row"]
    Z --> AA["Pivot = entry where pivot row and pivot column meet"]
    AA --> AB["Divide the whole pivot row by the pivot"]
    AB --> AC["Replace leaving basic variable with entering pivot-column variable"]
    AC --> AD["Use row operations to make all other pivot-column entries zero"]
    AD --> AE["New pivot column should contain one 1 and otherwise zeros"]
    AE --> L

    F -. "Warning" .-> F1["Do not reuse the same slack variable for different constraints"]
    U -. "Warning" .-> U1["Ignore zero or negative pivot-column entries when calculating theta"]
    AB -. "Warning" .-> AB1["Divide every entry in the pivot row, not just the pivot"]
    M -. "Stopping rule" .-> M1["Optimal only when no negative entries remain in the objective row"]
```

## Accessibility description

The diagram is a top-to-bottom flowchart of the simplex tableau process.

It begins with a two-variable linear programming problem, then moves through:

1. defining \(x\) and \(y\);
2. writing objective and constraints;
3. adding slack variables;
4. forming the tableau;
5. checking the objective row;
6. selecting pivot column and pivot row;
7. performing row operations;
8. repeating until optimal;
9. reading and interpreting the solution.

The warning branches highlight the most common exam traps:

- reusing slack variables;
- using invalid theta values;
- dividing only part of the pivot row;
- stopping before the objective row is non-negative.

## Lesson integration note

This asset should be inserted in Section 9 of:

```text
FA22_simplex_algorithm_tableau_lesson.md
```

at the placeholder:

```text
[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauMermaid-001 | Source: CCEA FA22-ALGGRAPH-LO003 + Decision 1 simplex tableau evidence + teacher transcript | Insert from mermaid/FA22SimplexAlgorithmTableauMermaid-001.md | Purpose: Show the full two-variable simplex tableau algorithm as a decision flow.]
```
