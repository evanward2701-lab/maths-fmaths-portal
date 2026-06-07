# AS1AlgebraicMethodsMER-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | AS1AlgebraicMethodsMER-001 |
| Asset type | Mermaid flowchart |
| Unit code | AS1 |
| Topic code | AS1-AF |
| Topic ID | AS1AlgebraicMethodsFactorTheorem |
| Related LO IDs | AS1-AF-LO010, AS1-AF-LO011 |
| Source | CCEA Mathematics Specification Map; Chapter 7a Algebraic Methods transcript; Dr Frost Algebraic Methods PDF |
| Related lesson section | Visual Asset Integration; Core Theory B-F; Exam Technique Notes |
| Purpose | Help students choose between algebraic fraction simplification, polynomial division, remainder theorem and factor theorem. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start: What does the question ask?"] --> B{"Is it an algebraic fraction to simplify?"}

    B -->|Yes| C["Factorise numerator and denominator first"]
    C --> D{"Is there a common factor?"}
    D -->|Yes| E["Cancel whole common factors only"]
    D -->|No| F["Leave in factorised or original form as required"]
    E --> G["Check sign traps, e.g. 2 - x = -(x - 2)"]
    G --> H["Final simplified expression"]

    B -->|No| I{"Does it ask to divide a polynomial?"}

    I -->|Yes| J{"Is the divisor linear?"}
    J -->|Yes| K["Use polynomial long division"]
    K --> L["Divide leading terms"]
    L --> M["Multiply by the whole divisor"]
    M --> N["Subtract carefully"]
    N --> O["Bring down the next term"]
    O --> P{"More terms left?"}
    P -->|Yes| L
    P -->|No| Q{"Remainder zero?"}
    Q -->|Yes| R["Write quotient only; divisor is a factor"]
    Q -->|No| S["Write quotient + remainder/divisor"]
    J -->|No| T["Not core AS1 algebraic division boundary; use factorisation if possible or log as enrichment"]

    I -->|No| U{"Does it ask for a remainder?"}

    U -->|Yes| V["Use remainder theorem"]
    V --> W["Write divisor as x - a, or solve ax + b = 0"]
    W --> X["Substitute the value into f(x)"]
    X --> Y["Remainder = f(a)"]

    U -->|No| Z{"Does it ask to show a factor?"}

    Z -->|Yes| AA["Use factor theorem"]
    AA --> AB["Write f(x) = the polynomial"]
    AB --> AC["Find the x-value that makes the factor zero"]
    AC --> AD["Evaluate f(a)"]
    AD --> AE{"Is f(a) = 0?"}
    AE -->|Yes| AF["State: By the factor theorem, the expression is a factor"]
    AE -->|No| AG["Not a factor; f(a) is the remainder when dividing by x - a"]

    Z -->|No| AH{"Does it ask to fully factorise a cubic?"}
    AH -->|Yes| AI["Try simple values: 1, -1, 2, -2, 3, -3"]
    AI --> AJ{"Found f(a) = 0?"}
    AJ -->|Yes| AK["Use x - a as a factor"]
    AK --> AL["Divide cubic by x - a"]
    AL --> AM["Factorise the resulting quadratic"]
    AM --> AN["Write final product of factors"]
    AJ -->|No| AO["Try another value or use calculator table to search"]

    AH -->|No| AP["Return to wording: identify whether it is simplify, divide, remainder, factor or solve"]
```
