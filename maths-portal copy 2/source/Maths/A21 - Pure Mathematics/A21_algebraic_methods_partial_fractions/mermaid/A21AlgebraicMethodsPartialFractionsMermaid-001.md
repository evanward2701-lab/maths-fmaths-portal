# A21AlgebraicMethodsPartialFractionsMermaid-001

## Asset ID

`A21AlgebraicMethodsPartialFractionsMermaid-001`

## Asset Type

Mermaid flowchart

## Source

- CCEA GCE Mathematics Specification Map: A21-AF-LO001 and A21-AF-LO008
- Dr Frost / Pure Year 2 transcript evidence on algebraic fractions, simple partial fractions, repeated linear factors and improper fractions
- Phase 1 placeholder:  
  `[VISUAL PLACEHOLDER: A21AlgebraicMethodsPartialFractionsMermaid-001 | Source: CCEA specification map + transcript | Insert from mermaid/A21AlgebraicMethodsPartialFractionsMermaid-001.md | Purpose: Flowchart for choosing between proper partial fractions, repeated linear factors and improper fractions.]`

## Related Lesson Section

- Core Theory
- Worked Examples
- Common Mistakes and Exam Traps
- Exam Technique Notes
- Visual and Interactive Asset Plan

## Purpose

Show the decision route for choosing the correct partial-fractions method:

1. factorise first;
2. check whether the fraction is proper or improper;
3. choose the correct denominator template;
4. stay inside the CCEA squared-linear-factor boundary;
5. use substitution, comparing coefficients or algebraic division as needed;
6. verify the final answer by recombining.

## Mermaid Code

```mermaid
flowchart TD
    A["Start with rational expression P(x) / Q(x)"] --> B["Factorise Q(x) completely"]
    B --> C{"Is deg P(x) >= deg Q(x)?"}

    C -- "Yes" --> D["Improper fraction"]
    D --> E["Do algebraic division OR include quotient in one identity"]
    E --> F["Remainder fraction is now proper"]
    F --> G{"What type of denominator remains?"}

    C -- "No" --> H["Proper fraction"]
    H --> G

    G -- "Distinct linear factors only" --> I["Use template: A/(x-a) + B/(x-b) + ..."]
    G -- "Repeated squared linear factor" --> J["Use both levels: A/(x-a) + B/(x-a)^2"]
    G -- "Beyond squared linear factors" --> K["Boundary warning: not core for this CCEA lesson"]

    I --> L["Multiply through by full denominator"]
    J --> L

    L --> M["Use substitution values that make factors zero"]
    M --> N{"Have all constants been found?"}

    N -- "Yes" --> O["Write final partial fractions"]
    N -- "No" --> P["Compare coefficients of x powers or constants"]
    P --> O

    O --> Q["Check by recombining fractions"]
    Q --> R["Final answer"]

    K --> S["Log as off-spec or enrichment only"]
```
