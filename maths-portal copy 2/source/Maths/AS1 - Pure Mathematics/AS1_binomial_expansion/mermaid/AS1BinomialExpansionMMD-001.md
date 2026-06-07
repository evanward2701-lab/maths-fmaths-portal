# AS1BinomialExpansionMMD-001

## Asset Metadata

| Field | Value |
|---|---|
| asset_id | AS1BinomialExpansionMMD-001 |
| file_path | mermaid/AS1BinomialExpansionMMD-001.md |
| unit_code | AS1 |
| topic_code | AS1-SS |
| topic_id | AS1BinomialExpansion |
| lesson_file | AS1_binomial_expansion_lesson.md |
| related_lesson_section | Exam Technique Notes; Worked Examples; Common Mistakes and Exam Traps |
| source | CCEA AS1 Sequences and series specification boundary; Dr Frost Chapter 8 Binomial Expansion evidence |
| purpose | Help the student decide whether to use Pascal’s triangle, binomial coefficients, a single-term method, or an estimation method. |
| linked_LOs | AS1-SS-LO001, AS1-SS-LO002 |

## Mermaid Code

```mermaid
flowchart TD
    A["Start: binomial expansion question"] --> B{"Is the power n a positive integer?"}

    B -- "No" --> C["Do not use the AS1 finite binomial formula as core method"]
    C --> C1["Log as boundary risk or Year 2 content"]

    B -- "Yes" --> D{"What does the question ask for?"}

    D -- "Full expansion with small n" --> E["Use Pascal's triangle"]
    E --> E1["Choose row n"]
    E1 --> E2["Write powers of first term decreasing"]
    E2 --> E3["Write powers of second term increasing"]
    E3 --> E4["Multiply each column and simplify"]

    D -- "First few terms" --> F["Use binomial coefficients or Pascal row"]
    F --> F1["Start with r equals 0"]
    F1 --> F2["Use term: nCr times first term to power n-r times second term to power r"]
    F2 --> F3["Stop after the requested number of terms"]
    F3 --> F4["Use dots if terms are omitted"]

    D -- "Single coefficient or single term" --> G["Use the single-term method"]
    G --> G1["Match the required power of x"]
    G1 --> G2["Find the correct r value"]
    G2 --> G3["Write only that term"]
    G3 --> G4["Equate coefficient if needed"]

    D -- "Estimation" --> H["Use truncated expansion"]
    H --> H1["First expand the required bracket"]
    H1 --> H2["Match the bracket to the number being estimated"]
    H2 --> H3["Substitute the small value of x"]
    H3 --> H4["Round to the requested accuracy"]

    E4 --> I["Final check"]
    F4 --> I
    G4 --> I
    H4 --> I

    I --> J{"Any danger signs?"}
    J -- "Negative term" --> K["Keep the negative term in brackets"]
    J -- "Expression like 3x squared" --> L["Square the whole bracket: (3x)^2 = 9x^2"]
    J -- "Coefficient comparison" --> M["Translate the sentence carefully"]
    J -- "No issues" --> N["Write final answer clearly"]
```
