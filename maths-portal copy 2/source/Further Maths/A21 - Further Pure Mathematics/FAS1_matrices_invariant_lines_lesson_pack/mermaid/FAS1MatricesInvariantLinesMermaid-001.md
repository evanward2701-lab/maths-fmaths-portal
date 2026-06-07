# Mermaid Asset: FAS1MatricesInvariantLinesMermaid-001

## Asset Metadata

| Field | Detail |
|---|---|
| Asset ID | `FAS1MatricesInvariantLinesMermaid-001` |
| Unit | `FAS1` |
| Topic Code | `FAS1-MAT` |
| Topic ID | `FAS1MatricesInvariantLines` |
| Lesson File | `FAS1_matrices_invariant_lines_lesson.md` |
| Related Lesson Section | `# 9. Visual Asset Integration` |
| Used Placeholder | `[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesMermaid-001 | Source: CCEA FAS1-MAT specification boundary | Insert from mermaid/FAS1MatricesInvariantLinesMermaid-001.md | Purpose: Show the decision flow from matrix transformation to invariant point, invariant line and determinant interpretation.]` |
| Source | CCEA FAS1-MAT specification boundary |
| Purpose | Show the decision flow from a matrix transformation to image point, invariant point, invariant line and determinant interpretation. |
| Core LO Links | `FAS1-MAT-LO003`, `FAS1-MAT-LO004`, `FAS1-MAT-LO006`, `FAS1-MAT-LO007`, `FAS1-MAT-LO008`, `FAS1-MAT-LO009`, `FAS1-MAT-LO010` |
| Off-Spec Control | Eigenvalues, eigenvectors and characteristic equations are deliberately excluded from this flowchart. |

## Creation Notes

This diagram is a navigation map for the CCEA-safe method used in the lesson.

## Mermaid Code

```mermaid
flowchart TD
    A["Start with a 2 x 2 matrix<br/>A = [[a, b], [c, d]]"] --> B["Choose what the question asks"]

    B --> C["Image of a point or vector"]
    B --> D["Invariant points"]
    B --> E["Invariant lines through origin"]
    B --> F["Determinant and transformation meaning"]

    C --> C1["Write point as column vector<br/>[x, y]^T"]
    C1 --> C2["Multiply A[x, y]^T"]
    C2 --> C3["Image is<br/>[ax + by, cx + dy]^T"]

    D --> D1["Use invariant point condition"]
    D1 --> D2["A[x, y]^T = [x, y]^T"]
    D2 --> D3["Equate components:<br/>ax + by = x<br/>cx + dy = y"]
    D3 --> D4["Solve simultaneous equations"]
    D4 --> D5{"Solution set?"}
    D5 --> D6["Only (0,0)<br/>Origin is the only invariant point"]
    D5 --> D7["A line of solutions<br/>Line of invariant points"]

    E --> E1["Let line be y = mx"]
    E1 --> E2["Use general point:<br/>[x, mx]^T"]
    E2 --> E3["Transform it:<br/>A[x, mx]^T = [x', y']^T"]
    E3 --> E4["Force image to stay on same line:<br/>y' = mx'"]
    E4 --> E5["Solve for gradient m"]
    E5 --> E6["Write final invariant lines"]
    E6 --> E7["Check vertical line separately:<br/>x = 0"]

    F --> F1["Calculate determinant:<br/>det A = ad - bc"]
    F1 --> F2{"det A value?"}
    F2 --> F3["det A > 0<br/>Area scale factor = det A<br/>Orientation preserved"]
    F2 --> F4["det A < 0<br/>Area scale factor = |det A|<br/>Orientation reversed"]
    F2 --> F5["det A = 0<br/>Singular matrix<br/>Area collapses to zero"]

    D6 --> G["Final exam answer:<br/>state point, line, or determinant interpretation clearly"]
    D7 --> G
    E7 --> G
    F3 --> G
    F4 --> G
    F5 --> G

    classDef start fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E,stroke-width:2px;
    classDef process fill:#FFFFF0,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1px;
    classDef decision fill:#FBEFEF,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    classDef answer fill:#FAF9F6,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;

    class A start;
    class B,D5,F2 decision;
    class C,C1,C2,C3,D,D1,D2,D3,D4,D6,D7,E,E1,E2,E3,E4,E5,E6,E7,F,F1,F3,F4,F5 process;
    class G answer;
```
