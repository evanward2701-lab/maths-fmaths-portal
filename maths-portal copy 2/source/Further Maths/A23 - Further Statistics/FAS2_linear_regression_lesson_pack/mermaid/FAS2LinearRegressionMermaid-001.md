# Mermaid Asset: FAS2LinearRegressionMermaid-001

| Field | Value |
|---|---|
| Asset ID | FAS2LinearRegressionMermaid-001 |
| Asset type | Mermaid flowchart |
| Lesson file | FAS2_linear_regression_lesson.md |
| Topic ID | FAS2LinearRegression |
| Unit | FAS2 |
| Topic code | FAS2-BIV |
| Source | CCEA FAS2-BIV specification boundary + teacher transcript |
| Related lesson section | Section 9.1 Concept flow diagram |
| Purpose | Show paired data to variable roles, least squares calculation, prediction and residual checking. |

```mermaid
flowchart TD
    A["Paired bivariate data<br/>(x_i, y_i), i = 1,...,n"] --> B{"Choose variable roles"}
    B --> C["x = explanatory / independent<br/>horizontal axis"]
    B --> D["y = response / dependent<br/>vertical axis"]
    C --> E["Scatter diagram"]
    D --> E
    E --> F{"Straight-line model sensible?"}
    F -->|Yes| G["Calculate summary statistics"]
    F -->|No| H["Linear regression may be unsuitable"]
    G --> G1["S_xx = Σx² − (Σx)²/n"]
    G --> G2["S_xy = Σxy − (Σx)(Σy)/n"]
    G1 --> I["b = S_xy/S_xx"]
    G2 --> I
    I --> J["a = ȳ − bx̄"]
    J --> K["Regression line of y on x<br/>y = a + bx"]
    K --> L["Predict: substitute x = x₀"]
    L --> M{"Is x₀ inside observed x-range?"}
    M -->|Yes| N["Interpolation<br/>more reliable"]
    M -->|No| O["Extrapolation<br/>may be unreliable"]
    K --> P["Residual check"]
    P --> Q["ŷ_i = a + bx_i"]
    Q --> R["ε_i = y_i − ŷ_i"]
    R --> S["Σ ε_i = 0"]
    R --> T["RSS = Σ ε_i²"]
    T --> U{"Residual pattern?"}
    U -->|Random scatter| V["Linear model appears suitable"]
    U -->|Pattern or curve| W["Linear model may be unsuitable"]
    U -->|All one side| X["Not feasible for least squares residuals"]
    N --> Y["Final answer: prediction, units, context, reliability"]
    O --> Y
    V --> Y
    W --> Y
    X --> Y
```
