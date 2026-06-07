# Linear Regression

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | FAS2: Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Official topic code | FAS2-BIV |
| Official topic name | Bivariate distributions |
| Lesson topic name | Linear Regression |
| Topic slug | linear_regression |
| Topic Pascal | LinearRegression |
| Topic ID | FAS2LinearRegression |
| Lesson file name | FAS2_linear_regression_lesson.md |
| Core LO IDs | FAS2-BIV-LO001; FAS2-BIV-LO002; FAS2-BIV-LO003; FAS2-BIV-LO004; FAS2-BIV-LO005 |
| Bridge tags | GCSE scatter diagrams; CCEA AS2 data presentation; CCEA AS2 PMCC; CCEA A22 regression and correlation |
| Topic tags | regression; least squares; bivariate data; explanatory variable; response variable; interpolation; extrapolation; residuals; coding; RSS |

## Lesson Boundary Statement

This lesson is written for **FAS2-BIV: Bivariate distributions** in **CCEA GCE Further Mathematics**.

The core CCEA content is:

- identifying explanatory/independent and response/dependent variables;
- calculating the equation of a least squares regression line;
- using the regression line to make predictions within the range of the explanatory variable;
- understanding the dangers of extrapolation;
- connecting regression with PMCC interpretation and limitations where appropriate.

Residuals, residual plots, coding and residual sum of squares are included because they are strongly present in the supplied lesson-specific evidence and directly support the meaning of “least squares”. They are treated as **evidence-backed extensions around the regression method**, not as separate official CCEA LO wording unless the question explicitly supplies them.

Spearman’s rank correlation, correlation hypothesis testing and proofs requiring Year 2 differentiation are not taught as core FAS2-BIV content in this lesson.

---

## 2. Evidence Map

| Source | Type | Use in this lesson | Status |
|---|---:|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | CCEA Further Maths specification map | Governs unit, topic code, official LO IDs and syllabus boundary | Core authority |
| `Further_Maths_README_module_map.md` | Further Maths module map | Confirms metadata rules, prefix rules, bridge protocol and FAS2-BIV bridge mapping | Core project authority |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence checklist | Used for evidence completeness and limitation logging | Core project authority |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary Maths bridge | Used only for bridge context | Bridge only |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary CCEA Maths spec map | Used for AS2 data presentation and A22 regression/correlation bridge | Bridge only |
| `transcripts.md` | Teacher transcript | Main lesson-specific source for explanations, warnings, examples and teacher phrasing | Core lesson evidence, bounded by CCEA |
| `Chapter_1_Linear_Regression_📈_(Further_Statistics_2)_screenshots.pdf` | Screenshot PDF | Visual evidence for diagrams, formula displays, section structure and annotations | Visual evidence, partly unclear |
| `S3-Chp5-RegressionAndCorrelation.pdf` | Cross-board PDF | PMCC/regression support only; Spearman and hypothesis testing excluded from core | Cross-board enrichment |

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

---

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary | Bridge |
|---|---|---|---|---|---|
| FAS2-BIV-LO001 | calculate the product-moment correlation coefficient and understand its use, interpretation and limitations | PMCC is introduced as a related measure for bivariate data. RSS connection to \(r\) is marked as evidence-backed extension. | CCEA spec map; transcript; Dr Frost PDF as cross-board support | Core PMCC idea included; PMCC testing excluded | AS2 PMCC; A22 correlation bridge |
| FAS2-BIV-LO002 | demonstrate understanding of explanatory independent variables and response dependent variables | Identify explanatory/independent variable on \(x\)-axis and response/dependent variable on \(y\)-axis. | Transcript; screenshot GCSE recap | Core | AS2 data presentation |
| FAS2-BIV-LO003 | calculate the equation of a regression line using the method of least squares | Calculate \(S_{xx}\), \(S_{xy}\), \(b=S_{xy}/S_{xx}\), \(a=\bar y-b\bar x\), then write \(y=a+bx\). | Transcript; screenshot formula panel | Core | Straight lines and regression bridge |
| FAS2-BIV-LO004 | use the equation of the regression line to make predictions within the range of the explanatory variable | Substitute a given explanatory value into the regression equation and interpret the predicted response. | Transcript | Core | Interpolation bridge |
| FAS2-BIV-LO005 | demonstrate understanding of the dangers of extrapolation | Explain that outside the observed \(x\)-range, the linear relationship may level off, curve, change gradient or cease to apply. | Transcript | Core | Extrapolation limitation bridge |

---

## 4. Learning Objectives

By the end of this lesson, you should be able to:

1. Explain the difference between an **explanatory/independent variable** and a **response/dependent variable**.
2. Decide which variable should be placed on the \(x\)-axis and which should be placed on the \(y\)-axis.
3. Understand that the regression line of \(y\) on \(x\) is written as

   \[
   y=a+bx.
   \]

4. Calculate

   \[
   S_{xx}=\sum x_i^2-\frac{(\sum x_i)^2}{n},
   \]

   and

   \[
   S_{xy}=\sum x_i y_i-\frac{(\sum x_i)(\sum y_i)}{n}.
   \]

5. Calculate

   \[
   b=\frac{S_{xy}}{S_{xx}},\qquad a=\bar y-b\bar x.
   \]

6. Use the regression line to make predictions for \(y\) from values of \(x\) inside the observed data range.
7. Explain why predictions outside the observed data range are examples of extrapolation and may be unreliable.
8. Interpret the gradient and intercept of a regression line in context.
9. Understand residuals as

   \[
   \varepsilon_i=y_i-\hat y_i.
   \]

10. Use coding substitutions to move between coded variables and original variables when the question gives a coding.

---

## 5. Explicit Prerequisite Recap

### GCSE foundations

At GCSE, a line of best fit was usually drawn by eye. A typical teacher instruction was to aim for roughly the same number of points above and below the line, and to place the line through the middle of the cloud of points. In this Further Maths lesson, the line is calculated by the least squares rule.

### AS/A2 Mathematics foundations

You should already be comfortable with plotting points, reading scatter diagrams, recognising positive/negative/strong/weak correlation, understanding that correlation does not imply causation, substituting into a straight-line equation, and distinguishing interpolation from extrapolation.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| GCSE scatter diagrams | Draw a line of best fit by eye | Calculate the least squares regression line | A visually plausible line may not be the least squares line |
| CCEA AS2 Data Presentation and Interpretation | Interpret scatter diagrams and regression lines; identify independent and dependent variables | Use explanatory/response variable language consistently and calculate \(y\) on \(x\) regression | Reversing \(x\) and \(y\) changes the regression equation |
| CCEA AS2 PMCC | Calculate and interpret PMCC | Use correlation ideas to judge strength and limitations of bivariate modelling | Strong correlation does not prove causation |
| CCEA AS2 interpolation/extrapolation | Make cautious predictions inside the range and avoid unsupported extrapolation | Use a calculated regression equation for prediction, then comment on reliability | A numerical prediction outside the range can look precise while being statistically fragile |
| CCEA A22 Regression and Correlation bridge | Regression/correlation ideas may be extended into testing and interpretation | Helps prepare for later ordinary Maths links | Hypothesis testing is bridge context only here, not core FAS2-BIV content |

In ordinary A-Level Maths, this idea appeared as interpreting scatter diagrams, correlation and sometimes a given regression line. In Further Maths, the same idea becomes a calculated modelling method: we find the line of \(y\) on \(x\) using the least squares rule. The key upgrade is that the line is not chosen by eye. It is forced to minimise the sum of the squares of the residuals. The danger is that the calculation can make the answer feel more trustworthy than the data deserves.

---

## 6. Big Picture Explanation

Linear regression solves the problem of finding the best straight-line model for paired data

\[
(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n).
\]

The regression line of \(y\) on \(x\) is

\[
y=a+bx.
\]

Here \(x\) is the explanatory variable and \(y\) is the response variable. The phrase “of \(y\) on \(x\)” means that \(y\) is predicted from \(x\). The least squares line is chosen to minimise

\[
\sum \varepsilon_i^2,
\]

where

\[
\varepsilon_i=y_i-\hat y_i,
\qquad
\hat y_i=a+bx_i.
\]

Predictions inside the observed \(x\)-range are interpolation. Predictions outside it are extrapolation and may be unreliable because the linear pattern may not continue.

Bridge Note: In ordinary A-Level Maths, the line of best fit may have been given, drawn or interpreted. Here, Further Maths extends this by requiring calculation of the least squares line from \(S_{xx}\), \(S_{xy}\), \(\bar x\) and \(\bar y\).

---

## 7. Key Definitions and Notation

### Paired data

\[
(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n).
\]

Here \(n\) is the number of pairs, \(x_i\) is the \(i\)-th explanatory value, and \(y_i\) is the \(i\)-th response value.

### Explanatory or independent variable

The explanatory variable is used to explain or predict another variable. It is placed on the \(x\)-axis.

### Response or dependent variable

The response variable is being predicted. It is placed on the \(y\)-axis.

### Regression line of \(y\) on \(x\)

\[
y=a+bx.
\]

The predicted value at \(x=x_i\) is

\[
\hat y_i=a+bx_i.
\]

### Mean values

\[
\bar x=\frac{\sum x_i}{n},\qquad \bar y=\frac{\sum y_i}{n}.
\]

The least squares regression line passes through \((\bar x,\bar y)\), so

\[
\bar y=a+b\bar x,
\]

and therefore

\[
a=\bar y-b\bar x.
\]

### Summary statistics

\[
S_{xx}=\sum (x_i-\bar x)^2=\sum x_i^2-\frac{(\sum x_i)^2}{n}.
\]

\[
S_{yy}=\sum (y_i-\bar y)^2=\sum y_i^2-\frac{(\sum y_i)^2}{n}.
\]

\[
S_{xy}=\sum (x_i-\bar x)(y_i-\bar y)=\sum x_iy_i-\frac{(\sum x_i)(\sum y_i)}{n}.
\]

### Regression coefficient

\[
b=\frac{S_{xy}}{S_{xx}}.
\]

If \(b>0\), the line slopes upwards. If \(b<0\), the line slopes downwards.

### Residual

\[
\varepsilon_i=y_i-\hat y_i=y_i-(a+bx_i).
\]

A positive residual means the point is above the line. A negative residual means the point is below the line.

For the least squares regression line,

\[
\sum \varepsilon_i=0.
\]

### Residual sum of squares

\[
RSS=\sum \varepsilon_i^2.
\]

RSS has units of \(y^2\).

### Interpolation and extrapolation

Interpolation means predicting for an \(x\)-value inside the observed range. Extrapolation means predicting outside the observed range, which is unreliable unless there is strong contextual evidence that the linear trend continues.

### Coding

A question may define coded variables, for example

\[
X=10C,
\qquad
Y=\frac{M-700}{5}.
\]

Find the regression line in \(X,Y\), then substitute back to obtain a line in the original variables.

---

## 8. Core Theory

### 8.1 From line of best fit to least squares line

At GCSE, a line of best fit was drawn by eye. Further Maths replaces this with a calculation. For each point,

\[
\varepsilon_i=y_i-(a+bx_i).
\]

The least squares line is the line for which

\[
\sum \varepsilon_i^2=\varepsilon_1^2+\varepsilon_2^2+\cdots+\varepsilon_n^2
\]

is as small as possible.

Bridge Note: In ordinary A-Level Maths, we used a line of best fit as a visual summary. Here, Further Maths defines “best” as minimising a specific quantity.

### 8.2 Why square the residuals?

Residuals can be positive or negative. If we simply added them, they would cancel. For the least squares regression line,

\[
\sum \varepsilon_i=0.
\]

Squaring makes every contribution non-negative, so \(\sum\varepsilon_i^2\) measures total squared error.

### 8.3 Calculation method

To calculate the regression line of \(y\) on \(x\):

1. Identify \(x\), the explanatory variable, and \(y\), the response variable.
2. Write \(y=a+bx\).
3. Calculate

   \[
   S_{xx}=\sum x^2-\frac{(\sum x)^2}{n}.
   \]

4. Calculate

   \[
   S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n}.
   \]

5. Calculate

   \[
   b=\frac{S_{xy}}{S_{xx}}.
   \]

6. Calculate

   \[
   a=\bar y-b\bar x.
   \]

7. Write the final line.

### 8.4 Notation warning

\[
\sum x^2
\]

means square first, then add. But

\[
(\sum x)^2
\]

means add first, then square. For \(x=2,4,6\),

\[
\sum x^2=2^2+4^2+6^2=56,
\]

but

\[
(\sum x)^2=(2+4+6)^2=144.
\]

### 8.5 Interpreting \(a\) and \(b\)

The intercept \(a\) is the predicted value of \(y\) when \(x=0\). This may be unreliable if \(x=0\) is outside the observed data range.

The gradient \(b\) is the predicted change in \(y\) for a one-unit increase in \(x\). Its units are

\[
\frac{\text{units of }y}{\text{units of }x}.
\]

### 8.6 Prediction and reliability

Substitute \(x=x_0\) into \(y=a+bx\). Then check whether \(x_0\) is inside the observed \(x\)-range.

A strong exam sentence for interpolation is:

> The prediction is more reliable because it is inside the range of the observed \(x\)-values, so it is interpolation.

A strong exam sentence for extrapolation is:

> The prediction is unreliable because it is outside the range of the observed \(x\)-values, so it is extrapolation.

### 8.7 Variables with different letters

If the regression line is of \(h\) on \(f\), then \(f\) behaves like \(x\) and \(h\) behaves like \(y\). The line is

\[
h=a+bf,
\]

with

\[
b=\frac{S_{fh}}{S_{ff}},
\qquad
 a=\bar h-b\bar f.
\]

### 8.8 Coding

Suppose

\[
Y=\frac{507}{14}-\frac{85}{21}X,
\qquad X=10C,
\qquad Y=\frac{M-700}{5}.
\]

Substitute:

\[
\frac{M-700}{5}=\frac{507}{14}-\frac{85}{21}(10C).
\]

Then

\[
M-700=\frac{2535}{14}-\frac{4250}{21}C,
\]

so

\[
M=700+\frac{2535}{14}-\frac{4250}{21}C.
\]

Since

\[
700=\frac{9800}{14},
\]

we obtain

\[
M=\frac{12335}{14}-\frac{4250}{21}C.
\]

### 8.9 Residual plots

A residual plot places the explanatory variable on the horizontal axis and the residual on the vertical axis. Random scatter about zero supports a linear model. A curve or systematic pattern suggests a non-linear relationship. All-positive or all-negative residuals are not feasible for least squares residuals because \(\sum \varepsilon_i=0\).

### 8.10 RSS

The residual sum of squares is

\[
RSS=\sum \varepsilon_i^2.
\]

If residuals are given, square each residual then add. If summary statistics are given, use

\[
RSS=S_{yy}-\frac{S_{xy}^2}{S_{xx}}.
\]

Where PMCC is connected and the formula is supplied or appropriate,

\[
RSS=S_{yy}(1-r^2).
\]

Boundary note: this connection is included because it appears in supplied evidence and links to PMCC. PMCC hypothesis testing is excluded from core.

---

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2LinearRegressionMermaid-001 | Source: CCEA FAS2-BIV specification boundary + teacher transcript | Insert from mermaid/FAS2LinearRegressionMermaid-001.md | Purpose: Show the conceptual flow from scatter diagram to least squares line, prediction, interpolation/extrapolation and residual checking. Description: A flowchart beginning with paired data \((x_i,y_i)\), then explanatory/response variable choice, scatter diagram, least squares calculation, regression line \(y=a+bx\), prediction, reliability comment, and residual/RSS check.]

[VISUAL PLACEHOLDER: FAS2LinearRegressionSVG-001 | Source: Screenshot PDF GCSE recap pages + transcript explanation | Insert from svg/FAS2LinearRegressionSVG-001.svg | Purpose: Preserve the visual idea that the explanatory variable is on the \(x\)-axis, the response variable is on the \(y\)-axis, predictions inside the observed \(x\)-range are interpolation and predictions outside are extrapolation. Description: A scatter plot with \(x\)-axis labelled explanatory variable, \(y\)-axis labelled response variable, upward trend points, a fitted straight line, a shaded inside-data-range region labelled interpolation, and outside-data-range regions labelled extrapolation/unreliable.]

[VISUAL PLACEHOLDER: FAS2LinearRegressionSVG-002 | Source: Screenshot PDF least squares residual diagram + teacher transcript | Insert from svg/FAS2LinearRegressionSVG-002.svg | Purpose: Show residuals as vertical distances from observed data points to the fitted regression line. Description: A scatter plot with data points, fitted line, dashed vertical residuals, labels \(\hat y_i=a+bx_i\), \(y_i\), and \(\varepsilon_i=y_i-\hat y_i\).]

[VISUAL PLACEHOLDER: FAS2LinearRegressionSVG-003 | Source: Teacher transcript residual plot discussion | Insert from svg/FAS2LinearRegressionSVG-003.svg | Purpose: Help students distinguish random residual scatter from patterned residuals. Description: Three mini residual plots: random scatter about zero labelled linear model suitable, curved pattern labelled non-linear relationship likely, and all-positive residuals labelled not feasible.]

[VISUAL PLACEHOLDER: FAS2LinearRegressionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2LinearRegressionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: Split panel comparing by-eye line of best fit with calculated least squares line.]

[VISUAL PLACEHOLDER: FAS2LinearRegressionTikZ-001 | Source: Teacher transcript + formula evidence | Insert from tikz/FAS2LinearRegressionTikZ-001.tex | Purpose: Give a precise mathematical diagram for a single residual. Description: Coordinate axes, a regression line \(y=a+bx\), a point \((x_i,y_i)\), the predicted point \((x_i,\hat y_i)\) on the line, and vertical segment labelled \(\varepsilon_i=y_i-\hat y_i\).]

[VISUAL PLACEHOLDER: FAS2LinearRegressionTikZ-002 | Source: Teacher transcript prediction reliability example | Insert from tikz/FAS2LinearRegressionTikZ-002.tex | Purpose: Show the observed \(x\)-range and classify prediction points. Description: A horizontal number line with observed range \([20,100]\), point \(58\) inside labelled interpolation/reliable, point \(130\) outside labelled extrapolation/unreliable.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2LinearRegressionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2LinearRegressionWidget-001.html | Purpose: Let students input \(n\), \(\sum x\), \(\sum y\), \(\sum x^2\), \(\sum xy\), then calculate \(S_{xx}\), \(S_{xy}\), \(b\), \(a\), and the regression line.]

[INTERACTIVE PLACEHOLDER: FAS2LinearRegressionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2LinearRegressionWidget-002.html | Purpose: Let students adjust a line and see residuals, squared residuals and RSS change dynamically.]

[INTERACTIVE PLACEHOLDER: FAS2LinearRegressionWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2LinearRegressionWidget-003.html | Purpose: Classify predictions as interpolation or extrapolation and prompt students to write a reliability sentence.]

---

## 11. Worked Examples

### Worked Example 1: Least squares regression line for a spring experiment

The supplied evidence gives:

\[
n=5,
\quad \sum x=300,
\quad \sum x^2=22000,
\quad \sum y=288.2,
\quad \sum xy=18238,
\quad \bar x=60,
\quad \bar y=57.72.
\]

Here \(x\) is applied mass in kg and \(y\) is spring length in cm.

Calculate

\[
S_{xx}=22000-\frac{300^2}{5}=22000-18000=4000.
\]

The transcript states that

\[
S_{xy}=922.
\]

Evidence correction note: using the transcribed totals,

\[
18238-\frac{300(288.2)}{5}=946,
\]

not \(922\). The later transcript solution uses \(S_{xy}=922\), so this worked example preserves that value while logging the discrepancy.

Then

\[
b=\frac{922}{4000}=0.2305.
\]

Next,

\[
a=57.72-0.2305(60)=57.72-13.83=43.89.
\]

So the regression line is

\[
y=43.89+0.2305x.
\]

Predict at \(x=58\):

\[
y=43.89+0.2305(58)=43.89+13.369=57.259\approx57.3\text{ cm}.
\]

Predict at \(x=130\):

\[
y=43.89+0.2305(130)=43.89+29.965=73.855\approx73.9\text{ cm}.
\]

If the observed masses run from \(20\) to \(100\), then \(58\) is interpolation and more reliable, while \(130\) is extrapolation and unreliable.

### Worked Example 2: Regression line when the variables are \(h\) and \(f\)

The supplied evidence gives

\[
n=7,
\quad \sum f=56,
\quad \sum h=45.8,
\quad \sum f^2=560,
\quad \sum fh=422.6,
\quad \bar f=8,
\quad \bar h=6.543.
\]

The regression line of \(h\) on \(f\) is

\[
h=a+bf.
\]

Calculate

\[
S_{fh}=422.6-\frac{56(45.8)}{7}=422.6-366.4=56.2.
\]

Calculate

\[
S_{ff}=560-\frac{56^2}{7}=560-448=112.
\]

So

\[
b=\frac{56.2}{112}=0.501785714\ldots\approx0.502.
\]

Then

\[
a=6.543-(0.501785714\ldots)(8)=2.528714286\ldots\approx2.53.
\]

Therefore

\[
h=2.53+0.502f.
\]

The gradient means each extra \(1\) gram of food supplement is predicted to increase shell hardness by about \(0.502\) units.

### Worked Example 3: Pressure-gauge calibration

Given

\[
n=8,
\quad \sum x=19.2,
\quad \sum y=18.86,
\quad \sum x^2=52.8,
\quad \sum xy=52.04.
\]

Calculate

\[
S_{xy}=52.04-\frac{19.2(18.86)}{8}=52.04-45.264=6.776.
\]

Calculate

\[
S_{xx}=52.8-\frac{19.2^2}{8}=52.8-46.08=6.72.
\]

Then

\[
b=\frac{6.776}{6.72}=1.008333333\ldots.
\]

Also

\[
\bar x=\frac{19.2}{8}=2.4,
\qquad
\bar y=\frac{18.86}{8}=2.3575.
\]

So

\[
a=2.3575-(1.008333333\ldots)(2.4)=-0.0625.
\]

The regression line is

\[
y=-0.0625+1.008333333\ldots x.
\]

For \(x=2\),

\[
y=-0.0625+1.008333333\ldots(2)=1.954166666\ldots\approx1.95\text{ bars}.
\]

### Worked Example 4: Coding in linear regression

Given

\[
n=8,
\quad \sum X=36,
\quad \sum Y=144,
\quad \sum X^2=204,
\quad \sum XY=478.
\]

Then

\[
S_{XY}=478-\frac{36(144)}{8}=478-648=-170.
\]

and

\[
S_{XX}=204-\frac{36^2}{8}=204-162=42.
\]

So

\[
b=\frac{-170}{42}=-\frac{85}{21}.
\]

Also

\[
\bar Y=\frac{144}{8}=18,
\qquad
\bar X=\frac{36}{8}=\frac{9}{2}.
\]

Then

\[
a=18-\left(-\frac{85}{21}\right)\left(\frac92\right)=18+\frac{255}{14}=\frac{507}{14}.
\]

So

\[
Y=\frac{507}{14}-\frac{85}{21}X.
\]

Given

\[
X=10C,
\qquad
Y=\frac{M-700}{5},
\]

substitute:

\[
\frac{M-700}{5}=\frac{507}{14}-\frac{85}{21}(10C).
\]

Thus

\[
M=\frac{12335}{14}-\frac{4250}{21}C.
\]

For \(C=0.25\),

\[
M=\frac{12335}{14}-\frac{4250}{21}(0.25)=830.4761905\ldots\approx830^\circ\mathrm C.
\]

Evidence ambiguity note: the transcript/OCR contains wording that appears to suggest “83.5”, but the coding and algebra give approximately \(830^\circ\mathrm C\). This should be checked against the original visual page before final publication.

### Worked Example 5: Calculating residuals

If

\[
y=0.2+0.8x,
\]

and an observed point has \(x=2\), \(y=1.7\), then

\[
\hat y=0.2+0.8(2)=1.8.
\]

Therefore

\[
\varepsilon=y-\hat y=1.7-1.8=-0.1.
\]

The residual is negative, so the point lies below the line.

### Worked Example 6: Missing value from residual sum

For a least squares regression line,

\[
\sum\varepsilon_i=0.
\]

Given residuals

\[
-0.3855,
\quad 0.6452,
\quad -0.7934,
\quad P-20.2627,
\quad -0.2013,
\]

write

\[
-0.3855+0.6452-0.7934+(P-20.2627)-0.2013=0.
\]

Collecting constants gives

\[
P-20.9977=0,
\]

so

\[
P=20.9977\approx21.0.
\]

### Worked Example 7: RSS from residuals

For residuals

\[
0.2,\quad -0.1,\quad -0.3,\quad 0.2,\quad 0,
\]

\[
RSS=(0.2)^2+(-0.1)^2+(-0.3)^2+(0.2)^2+0^2.
\]

Thus

\[
RSS=0.04+0.01+0.09+0.04+0=0.18.
\]

### Worked Example 8: RSS from summary statistics

Given

\[
S_{yy}=3.68,
\quad S_{xy}=6.74,
\quad S_{xx}=123.52,
\]

\[
RSS=3.68-\frac{6.74^2}{123.52}=3.3122304097\ldots\approx3.31.
\]

### Worked Example 9: RSS and \(r^2\)

Given

\[
S_{yy}=1774155,
\qquad RSS=166567,
\]

and

\[
RSS=S_{yy}(1-r^2),
\]

\[
166567=1774155(1-r^2).
\]

Then

\[
r^2=1-\frac{166567}{1774155}=0.9061169962\ldots,
\]

so, assuming \(r>0\),

\[
r=0.951901779\ldots\approx0.952.
\]

Evidence discrepancy note: the transcript appears to imply a value near \(0.246\). If the intended RSS was \(1665667\), then \(r\approx0.247\). This must be checked against the original question before final publication.

---

## 12. Common Mistakes and Exam Traps

1. Putting variables on the wrong axes. The explanatory variable is \(x\), the response variable is \(y\).
2. Writing the line in the wrong form. Use \(y=a+bx\).
3. Confusing \(\sum x^2\) and \((\sum x)^2\).
4. Rounding \(b\) too early.
5. Forgetting that \(a=\bar y-b\bar x\) depends on \(b\).
6. Treating the intercept as automatically meaningful when \(x=0\) is outside the data range.
7. Making extrapolated predictions without warning.
8. Reversing residuals. Residual is observed minus predicted:

   \[
   \varepsilon_i=y_i-\hat y_i.
   \]

9. Forgetting that for the least squares line,

   \[
   \sum\varepsilon_i=0.
   \]

10. Thinking random residuals are bad. Random scatter about zero supports the model. Patterned residuals are the warning sign.
11. Comparing RSS values in different units.
12. Treating correlation as causation.
13. Substituting coding equations backwards.

---

## 13. Practice Questions

### Basic fluency

1. A researcher records hours studied and test score. Identify the explanatory variable, response variable, \(x\)-axis variable and \(y\)-axis variable.
2. Given \(n=6\), \(\sum x=42\), \(\sum y=93\), \(\sum x^2=322\), \(\sum xy=692\), calculate \(S_{xx}\) and \(S_{xy}\).
3. Using Question 2 with \(\bar x=7\), \(\bar y=15.5\), find the regression line of \(y\) on \(x\).
4. For \(y=5.25+1.464285714x\) and observed \(x\)-range \(3\le x\le 11\), predict at \(x=8\) and \(x=14\), then classify each prediction.

### Bridge questions

5. Explain how least squares improves a by-eye line of best fit. Mention residuals, squaring, minimising and \(y=a+bx\).
6. For observed range \(12\le x\le 30\), compare predictions at \(x=25\) and \(x=40\).
7. Interpret \(a\) and \(b\) in \(y=12.4+0.85x\) where \(x\) is machine age and \(y\) is annual repair cost.

### Standard exam-style questions

8. Given \(n=8\), \(\sum x=64\), \(\sum y=174\), \(\sum x^2=560\), \(\sum xy=1498\), and observed \(x\)-range \(3\le x\le13\), find the regression line and predict at \(x=10\) and \(x=16\).
9. Given \(n=5\), \(\sum t=35\), \(\sum w=141\), \(\sum t^2=255\), \(\sum tw=1035\), find the regression line of \(w\) on \(t\) and predict at \(t=8.5\).
10. For proposed line \(y=3+2x\) and data \((1,6),(2,6.5),(3,9.2),(4,10.4),(5,13.9)\), calculate residuals and decide whether the line can be the least squares regression line.
11. For line \(y=1.5+0.7x\) and points \((2,2.7),(4,4.5),(6,P),(8,7.2)\), use residuals summing to zero to find \(P\).
12. Residuals are \(0.4,-0.2,-0.1,-0.5,0.4\). Show they sum to zero and calculate RSS.
13. Given \(S_{yy}=80\), \(S_{xy}=54\), \(S_{xx}=45\), calculate RSS.
14. Given \(Y=3-2X\), \(X=(C-10)/5\), \(Y=(M-100)/20\), find the line in \(M,C\) and estimate \(M\) when \(C=15\).

### Harder synthesis

15. A biologist wants to predict body mass \(M\) from wing length \(L\). Which regression line is required and why?
16. Interpret residual plot descriptions: all positive; random scatter; curved pattern; all negative; steadily increasing residuals.
17. Given \(S_{yy}=250\) and \(r=0.8\), use \(RSS=S_{yy}(1-r^2)\) to calculate RSS.

---

## 14. Worked Solutions

### Solution 1

Hours studied is the explanatory variable and goes on the \(x\)-axis. Test score is the response variable and goes on the \(y\)-axis.

### Solution 2

\[
S_{xx}=322-\frac{42^2}{6}=322-294=28.
\]

\[
S_{xy}=692-\frac{42(93)}{6}=692-651=41.
\]

### Solution 3

\[
b=\frac{41}{28}=1.464285714\ldots.
\]

\[
a=15.5-\frac{41}{28}(7)=15.5-10.25=5.25.
\]

So

\[
y=5.25+\frac{41}{28}x.
\]

### Solution 4

At \(x=8\),

\[
y=5.25+1.464285714(8)=16.964285712\approx17.0.
\]

At \(x=14\),

\[
y=5.25+1.464285714(14)=25.749999996\approx25.7.
\]

Since \(8\) is inside \([3,11]\), it is interpolation and more reliable. Since \(14>11\), it is extrapolation and unreliable.

### Solution 5

For each point, \(\hat y_i=a+bx_i\) and \(\varepsilon_i=y_i-\hat y_i\). The least squares line is the line \(y=a+bx\) that minimises \(\sum\varepsilon_i^2\). This improves a by-eye line by giving a precise calculation rule.

### Solution 6

\(x=25\) is inside \([12,30]\), so it is interpolation and more reliable. \(x=40\) is outside the range, so it is extrapolation. The prediction at \(x=40\) may be unreliable because it is outside the observed range of \(x\)-values.

### Solution 7

The gradient \(0.85\) means each additional year of machine age is predicted to increase annual repair cost by £0.85. The intercept \(12.4\) predicts annual repair cost when \(x=0\), but this may be unreliable if \(0\) years is outside the data range or not meaningful.

### Solution 8

\[
S_{xx}=560-\frac{64^2}{8}=560-512=48.
\]

\[
S_{xy}=1498-\frac{64(174)}{8}=1498-1392=106.
\]

\[
b=\frac{106}{48}=\frac{53}{24}=2.208333333\ldots.
\]

\[
\bar x=8,
\qquad \bar y=21.75.
\]

\[
a=21.75-\frac{53}{24}(8)=4.08333333\ldots.
\]

So

\[
y=4.08333333+\frac{53}{24}x.
\]

At \(x=10\),

\[
y=26.16666666\ldots\approx26.2.
\]

At \(x=16\),

\[
y=39.41666666\ldots\approx39.4.
\]

Since \(10\in[3,13]\), it is interpolation. Since \(16>13\), it is extrapolation.

### Solution 9

\[
S_{tt}=255-\frac{35^2}{5}=255-245=10.
\]

\[
S_{tw}=1035-\frac{35(141)}{5}=1035-987=48.
\]

\[
b=\frac{48}{10}=4.8.
\]

\[
\bar t=7,
\qquad \bar w=28.2.
\]

\[
a=28.2-4.8(7)=-5.4.
\]

So

\[
w=-5.4+4.8t.
\]

At \(t=8.5\),

\[
w=-5.4+4.8(8.5)=35.4.
\]

This is interpolation because \(5\le8.5\le9\).

### Solution 10

For \(y=3+2x\), predicted values are \(5,7,9,11,13\). Residuals are

\[
1,
\quad -0.5,
\quad 0.2,
\quad -0.6,
\quad 0.9.
\]

Their sum is

\[
1-0.5+0.2-0.6+0.9=1.0.
\]

Since this is not zero, the proposed line cannot be the least squares regression line.

### Solution 11

Predicted values are:

\[
\hat y(2)=2.9,
\quad \hat y(4)=4.3,
\quad \hat y(6)=5.7,
\quad \hat y(8)=7.1.
\]

Residuals are:

\[
-0.2,
\quad 0.2,
\quad P-5.7,
\quad 0.1.
\]

Use \(\sum\varepsilon_i=0\):

\[
-0.2+0.2+(P-5.7)+0.1=0.
\]

\[
P-5.6=0.
\]

\[
P=5.6.
\]

### Solution 12

\[
0.4-0.2-0.1-0.5+0.4=0.
\]

\[
RSS=(0.4)^2+(-0.2)^2+(-0.1)^2+(-0.5)^2+(0.4)^2=0.62.
\]

### Solution 13

\[
RSS=80-\frac{54^2}{45}=80-64.8=15.2.
\]

### Solution 14

\[
\frac{M-100}{20}=3-2\left(\frac{C-10}{5}\right).
\]

\[
\frac{M-100}{20}=\frac{35-2C}{5}.
\]

\[
M-100=4(35-2C)=140-8C.
\]

\[
M=240-8C.
\]

At \(C=15\),

\[
M=240-8(15)=120.
\]

### Solution 15

Wing length \(L\) is explanatory and body mass \(M\) is response. The required regression line is \(M\) on \(L\), in the form \(M=a+bL\). The reverse line \(L\) on \(M\) would predict wing length from body mass and answers a different question.

### Solution 16

All positive residuals: not feasible because they cannot sum to zero.

Random scatter above and below zero: feasible and supports a linear model.

Curved pattern above and below zero: feasible but suggests a non-linear relationship.

All negative residuals: not feasible because they cannot sum to zero.

Residuals increasing steadily with \(x\): feasible but suggests a pattern, so the linear model may be unsuitable.

### Solution 17

\[
r^2=0.8^2=0.64.
\]

\[
RSS=250(1-0.64)=250(0.36)=90.
\]

---

## 15. Exam Technique Notes

Start by identifying variables. Use \(y=a+bx\). Show enough working for \(S_{xx}\) and \(S_{xy}\). Keep exact or stored values. Interpret the gradient as change in response for one-unit increase in the explanatory variable. Interpret the intercept carefully, especially if \(x=0\) is outside the data range. Always comment on interpolation or extrapolation.

Residual technique:

\[
\hat y_i=a+bx_i,
\qquad
\varepsilon_i=y_i-\hat y_i.
\]

For least squares residuals:

\[
\sum\varepsilon_i=0.
\]

For RSS:

\[
RSS=\sum\varepsilon_i^2
\]

or

\[
RSS=S_{yy}-\frac{S_{xy}^2}{S_{xx}}.
\]

If the PMCC relationship is supplied:

\[
RSS=S_{yy}(1-r^2).
\]

RSS has units of \(y^2\), so only compare RSS values with the same response-variable units.

Safe exam phrases:

- “The residuals are randomly scattered about zero, so a linear model appears suitable.”
- “The residuals show a pattern, so a linear model may not be suitable.”
- “The prediction is unreliable because it is outside the observed range of \(x\)-values, so it is extrapolation.”

---

## 16. Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---:|---|
| FAS2-BIV-LO001 | Partly | PMCC is included as related context and through RSS. A separate PMCC lesson may be needed for full PMCC calculation and interpretation. |
| FAS2-BIV-LO002 | Yes | Explanatory and response variables covered throughout. |
| FAS2-BIV-LO003 | Yes | Least squares line calculation covered in detail. |
| FAS2-BIV-LO004 | Yes | Prediction within observed range covered through interpolation. |
| FAS2-BIV-LO005 | Yes | Extrapolation warnings covered throughout. |

### Off-Spec Content Found but Excluded

| Content | Source | Why excluded |
|---|---|---|
| Spearman’s rank correlation coefficient | Dr Frost S3 PDF | Not confirmed by supplied CCEA FAS2-BIV boundary |
| Spearman no-ties formula | Dr Frost S3 PDF | Cross-board content, not imported as core |
| Proof of Spearman/PMCC equivalence | Dr Frost S3 PDF | Cross-board enrichment |
| PMCC hypothesis testing | Dr Frost S3 PDF and ordinary A22 bridge | Bridge only, not FAS2-BIV linear regression core |
| Least squares proof using Year 2 differentiation | Transcript optional link | Not compulsory in evidence |

### Missing Evidence and Weak Evidence Warnings

- Screenshot PDF text extraction was incomplete because the PDF is image-based.
- The spring example contains a numerical inconsistency in \(S_{xy}\).
- The carbon steel example contains a likely OCR/speech ambiguity in the final temperature.
- The RSS and \(r\) example may contain a missing digit in RSS.
- Formulae are supported by transcript/screenshot evidence, but the official formula booklet extract was not directly supplied.

---

## 17. Recommended Enhancements Not in the Evidence

Suggested enhancements include:

- a regression role diagram comparing explanatory and response variables;
- a notation warning card for \(\sum x^2\) versus \((\sum x)^2\);
- a moving regression-line animation showing RSS changing;
- a residual plot builder;
- a coding converter widget;
- extra examples involving negative regression coefficient, wrong regression direction and outlier influence.

These are proposed enhancements, not evidence-backed source content.

---

## 18. Supplementary Sources Used

Project sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`;
- `Further_Maths_README_module_map.md`;
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`;
- `Further Maths Portal Build – Knowledge Evidence.txt`.

Lesson-specific sources used:

- `transcripts.md`;
- `Chapter_1_Linear_Regression_📈_(Further_Statistics_2)_screenshots.pdf`;
- `S3-Chp5-RegressionAndCorrelation.pdf`.

Ordinary A-Level Maths bridge sources used:

- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`;
- `CCEA_GCE_Mathematics_Specification_Map.md`.

Cross-board source note: the Dr Frost S3 PDF was used only as supplementary context where it aligns with bivariate data, PMCC and regression ideas. Spearman’s rank and PMCC hypothesis testing were not imported into the core lesson.

---

## 19. Final Student Checklist

### Prerequisite confidence

- [ ] I can read a scatter diagram.
- [ ] I can identify positive, negative, strong and weak correlation.
- [ ] I know correlation does not prove causation.
- [ ] I can substitute into a straight-line equation.
- [ ] I understand interpolation and extrapolation.

### Further Maths method

- [ ] I can identify explanatory and response variables.
- [ ] I can write the regression line as \(y=a+bx\).
- [ ] I can calculate \(S_{xx}\).
- [ ] I can calculate \(S_{xy}\).
- [ ] I can calculate \(b=S_{xy}/S_{xx}\).
- [ ] I can calculate \(a=\bar y-b\bar x\).
- [ ] I can use the regression equation to predict.
- [ ] I can state interpolation or extrapolation.

### Residual and RSS checklist

- [ ] I can calculate \(\hat y_i=a+bx_i\).
- [ ] I can calculate \(\varepsilon_i=y_i-\hat y_i\).
- [ ] I can use \(\sum\varepsilon_i=0\) for least squares residuals.
- [ ] I can calculate \(RSS=\sum\varepsilon_i^2\).
- [ ] I understand that RSS has units of \(y^2\).

### Final self-test formulae

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n}
\]

\[
S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n}
\]

\[
b=\frac{S_{xy}}{S_{xx}}
\]

\[
a=\bar y-b\bar x
\]

\[
\varepsilon_i=y_i-\hat y_i
\]

\[
RSS=\sum\varepsilon_i^2
\]
