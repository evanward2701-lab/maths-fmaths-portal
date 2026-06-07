# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-05
course: CCEA GCE Further Mathematics
unit_code: FAS2
unit_title: Further AS 2 Applied Mathematics
applied_section: Section C: Statistics
topic_code: FAS2-BIV
topic_area: Bivariate distributions
lesson_title: Product-Moment Correlation Coefficient
topic_name: Product-moment correlation coefficient
topic_slug: product_moment_correlation_coefficient
topic_pascal: ProductMomentCorrelationCoefficient
topic_id: FAS2ProductMomentCorrelationCoefficient
lesson_file: FAS2_product_moment_correlation_coefficient_lesson.md
core_lo_ids:
  - FAS2-BIV-LO001
bridge_tags:
  - AS2 Data Presentation and Interpretation
  - AS2 Correlation
  - AS2 Product-Moment Correlation Coefficient
  - A22 Regression and Correlation
  - A22 Correlation Critical Values
topic_tags:
  - FAS2
  - BIV
  - Statistics
  - BivariateData
  - Correlation
  - PMCC
  - Interpretation
  - Limitations
boundary_risk_tags:
  - SpearmanRank
  - TiedRanks
  - NonParametricTests
  - CorrelationHypothesisTesting
```

# 2. Evidence Map

| Source | Used in this lesson | Notes |
|---|---|---|
| CCEA Further Mathematics specification map | Core authority | Confirms `FAS2-BIV-LO001`: calculate the product-moment correlation coefficient and understand its use, interpretation and limitations. |
| Further Maths module map | Core structure | Confirms `FAS2-BIV` is Bivariate distributions and links to ordinary A-Level Regression and Correlation / AS2 Data Presentation. |
| Evidence checklist | Workflow authority | Controls missing evidence, visual evidence limitations and off-spec logging. |
| Ordinary A-Level Maths bridge extracts | Bridge only | Used to explain what students already know about scatter diagrams, informal correlation, PMCC and correlation interpretation. |
| `Chapter_2_Correlation_📈_(Further_Statistics_2)_screenshots.pdf` | Visual/support evidence | Page images show the chapter title, correlation range from \(-1\) to \(+1\), the visual correlation scale and the chapter menu with PMCC, Spearman and hypothesis testing. No parsed text was available. |
| `transcripts.md` | Core PMCC evidence and boundary-risk evidence | Used for the meaning of correlation, PMCC interpretation, coding warning, and the warning that \(r\) measures closeness to a straight line rather than steepness. Spearman and hypothesis sections are logged as enrichment. |
| `S3-Chp5-RegressionAndCorrelation.pdf` | Cross-board support | PMCC recap and calculation example are used only because CCEA confirms PMCC is on-spec. Spearman and hypothesis-testing parts are boundary-risk. |
| `Spearmans Rank Correlation Coefficient - Lesson.pdf` | Optional enrichment only | Contains non-parametric and Spearman material; not treated as core CCEA FAS2 unless further CCEA evidence is supplied. |

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-BIV-LO001` | calculate the product-moment correlation coefficient and understand its use, interpretation and limitations | Sections 6-8 define bivariate data, PMCC, \(S_{xx}\), \(S_{yy}\), \(S_{xy}\), calculation method, interpretation and limitations. Sections 11-15 provide worked examples, practice and exam technique. | CCEA Further Maths specification map; transcript PMCC explanations; PMCC example evidence. | Core. Spearman and hypothesis testing are not included as required CCEA core. | AS2 informal correlation and PMCC; A22 regression/correlation interpretation. |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. identify when data are **bivariate data**, meaning two linked variables are being measured;
2. define the **product-moment correlation coefficient**, or **PMCC**, denoted by \(r\);
3. calculate

\[
S_{xx}, \quad S_{yy}, \quad S_{xy}
\]

from summary statistics;

4. calculate

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}};
\]

5. interpret values of \(r\) between \(-1\) and \(+1\);
6. explain why \(r\) measures the **strength and direction of linear correlation**, not the steepness of the line;
7. recognise limitations of PMCC, including non-linear patterns, outliers, causation errors and extrapolation risk.

## Bridge objectives

You should connect this lesson to ordinary A-Level Maths by remembering:

1. how scatter diagrams show positive, negative, weak and strong correlation;
2. that correlation does not imply causation;
3. that PMCC may already have appeared in ordinary AS/A2 Mathematics;
4. that regression line language, such as explanatory and response variables, is related but not the main focus of this lesson.

## Exam technique objectives

You should be able to:

1. write down the correct PMCC formula before substituting values;
2. keep exact intermediate values where possible;
3. round \(r\) only at the end unless the question instructs otherwise;
4. interpret \(r\) in context;
5. avoid saying that \(r\) is the gradient;
6. avoid claiming causation from correlation.

# 5. Explicit Prerequisite Recap

## GCSE foundations

Before this lesson, you should be comfortable with plotting coordinates, reading scatter diagrams, calculating sums, substituting into formulae, square roots, rounding, and interpreting positive and negative relationships.

## Ordinary AS/A2 Mathematics foundations

You should already have met scatter diagrams and informal correlation language:

\[
\text{positive correlation}, \qquad
\text{negative correlation}, \qquad
\text{strong correlation}, \qquad
\text{weak correlation}.
\]

You may also have met PMCC in ordinary A-Level Mathematics. In Further Mathematics, the same idea is treated as part of the more formal study of **bivariate distributions**.

## Previous Further Mathematics foundations

No previous Further Mathematics topic is strictly required, but the algebraic discipline matters. You must keep the sums and formula substitutions clean. This is one of those topics where the mathematics is not a dragon, but the arithmetic is wearing tiny roller skates.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Data Presentation and Interpretation | Describe correlation informally from scatter diagrams. | Calculate a numerical measure, \(r\), for the strength and direction of linear correlation. | A visual judgement is not enough when a PMCC calculation is requested. |
| AS2 PMCC | Calculate and interpret the product-moment correlation coefficient. | Treat PMCC as part of bivariate distributions and link it to regression suitability and limitations. | \(r\) is not the gradient. It does not measure steepness. |
| AS2 / A22 Correlation limitations | Correlation does not imply causation. | Interpret \(r\) carefully in applied statistical contexts. | A high value of \(r\) does not prove one variable causes the other. |
| A22 Regression and Correlation | Regression lines, prediction, interpolation and extrapolation warnings. | PMCC helps judge whether a linear model is reasonable, but does not itself create the regression line. | A strong \(r\) does not make extrapolation safe. |
| A22 Hypothesis Testing | Interpret a correlation coefficient using a p-value or critical value. | Uploaded evidence includes this, but it is bridge/enrichment unless confirmed by CCEA FAS2 evidence. | Do not import hypothesis-test procedures into the FAS2 core lesson boundary without CCEA confirmation. |

In ordinary A-Level Maths, this idea appeared as reading scatter diagrams, describing correlation and sometimes calculating PMCC.

In Further Maths, the same idea becomes part of the study of **bivariate distributions**, where the numerical coefficient \(r\) is used more deliberately to judge the strength and direction of a linear relationship.

The key upgrade is that you must connect the calculation to interpretation and limitations.

The danger is thinking that a high \(r\) magically explains everything. It does not. It only measures how closely the data fit a straight-line pattern.

# 6. Big Picture Explanation

Suppose you measure two variables for the same set of items. For example: number of vehicles and number of accidents; study time and test score; 11+ score and later point score; temperature and ice-cream sales; height and weight.

Each pair of values belongs together, so the data are **bivariate**.

The big question is:

\[
\text{How strongly are these two variables associated?}
\]

A scatter diagram gives a visual answer. The PMCC gives a numerical answer.

The product-moment correlation coefficient, \(r\), is a number satisfying

\[
-1 \leq r \leq 1.
\]

The evidence states that \(r=1\) corresponds to perfect positive correlation, \(r=-1\) corresponds to perfect negative correlation, and \(r=0\) corresponds to no linear correlation.

The transcript's key warning is the golden hinge of this lesson: the strength of correlation measures how closely the data fall into a straight line; it does **not** indicate how steep the line is. Steepness is handled by \(b\) in the regression chapter, not by \(r\).

So PMCC answers this:

\[
\text{Do the points lie close to a straight-line pattern?}
\]

It does **not** answer this:

\[
\text{How steep is that line?}
\]

It also does **not** answer this:

\[
\text{Does }x\text{ cause }y?
\]

# 7. Key Definitions and Notation

## Bivariate data

**Bivariate data** are data where two linked variables are measured for each item or individual.

If the variables are \(x\) and \(y\), a data set with \(n\) paired observations is written as

\[
(x_1,y_1),\ (x_2,y_2),\ \ldots,\ (x_n,y_n).
\]

## Product-moment correlation coefficient

The **product-moment correlation coefficient**, or **PMCC**, is denoted by

\[
r.
\]

It measures the strength and direction of **linear correlation** between two variables.

\[
-1 \leq r \leq 1.
\]

## Summary statistics

For paired data \((x_i,y_i)\), define:

\[
\sum x = x_1+x_2+\cdots+x_n,
\]

\[
\sum y = y_1+y_2+\cdots+y_n,
\]

\[
\sum x^2 = x_1^2+x_2^2+\cdots+x_n^2,
\]

\[
\sum y^2 = y_1^2+y_2^2+\cdots+y_n^2,
\]

\[
\sum xy = x_1y_1+x_2y_2+\cdots+x_ny_n.
\]

The corrected sums are:

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n},
\]

\[
S_{yy}=\sum y^2-\frac{(\sum y)^2}{n},
\]

\[
S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n}.
\]

The PMCC is:

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}.
\]

## Interpretation language

| Value of \(r\) | Interpretation |
|---:|---|
| \(r=1\) | Perfect positive linear correlation |
| \(0<r<1\) | Positive linear correlation |
| \(r\approx 0\) | Little or no linear correlation |
| \(-1<r<0\) | Negative linear correlation |
| \(r=-1\) | Perfect negative linear correlation |

## Important notation warning

The coefficient \(r\) is **not** the gradient.

A line with a gentle positive slope and a line with a steep positive slope can both have \(r=1\) if every point lies exactly on a straight line.

The value of \(r\) cares about **closeness to a straight line**, not steepness.

# 8. Core Theory

## 8.1 What PMCC is measuring

For bivariate data, the PMCC measures how closely the points follow a straight-line pattern.

If the points lie exactly on an upward-sloping straight line, then \(r=1\). If the points lie exactly on a downward-sloping straight line, then \(r=-1\). If the points are scattered with no straight-line pattern, then \(r\approx 0\).

**Bridge Note:** In ordinary A-Level Maths, you described this visually from a scatter diagram. Here, Further Maths requires you to attach a numerical coefficient to that visual impression.

## 8.2 Direction and strength

The sign of \(r\) gives the **direction**.

If \(r>0\), larger \(x\)-values tend to be associated with larger \(y\)-values. If \(r<0\), larger \(x\)-values tend to be associated with smaller \(y\)-values. If \(r=0\), there is no linear correlation.

The size of \(|r|\) gives the **strength** of the linear relationship.

If \(|r|\approx 1\), the points lie close to a straight line. If \(|r|\approx 0\), the points do not lie close to a straight line.

## 8.3 PMCC does not measure steepness

Consider two perfect positive straight-line data sets:

\[
y=2x+1
\]

and

\[
y=100x+1.
\]

Both data sets have perfect positive linear correlation because every point lies exactly on a straight line.

So both have

\[
r=1.
\]

But the gradients are different:

\[
2 \neq 100.
\]

Therefore:

\[
\boxed{\text{\(r\) measures linear closeness, not gradient.}}
\]

## 8.4 The PMCC formula

For \(n\) paired observations \((x_i,y_i)\), calculate:

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n},
\]

\[
S_{yy}=\sum y^2-\frac{(\sum y)^2}{n},
\]

\[
S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n}.
\]

Then:

\[
\boxed{r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}}
\]

The numerator \(S_{xy}\) controls the direction; the denominator \(\sqrt{S_{xx}S_{yy}}\) standardises the value so that \(r\) lies between \(-1\) and \(1\).

## 8.5 Why \(S_{xx}\), \(S_{yy}\), and \(S_{xy}\) appear

\(S_{xx}\) measures the corrected spread of the \(x\)-values. \(S_{yy}\) measures the corrected spread of the \(y\)-values. \(S_{xy}\) measures how \(x\) and \(y\) vary together.

If large \(x\)-values tend to come with large \(y\)-values, then \(S_{xy}\) tends to be positive. If large \(x\)-values tend to come with small \(y\)-values, then \(S_{xy}\) tends to be negative. If there is no clear linear association, then \(S_{xy}\) tends to be close to zero.

## 8.6 Fully worked PMCC calculation from summary statistics

The Dr Frost S3 recap slide gives the following paired data context.

| Observation | \(x\) | \(y\) |
|---:|---:|---:|
| 1 | \(119\) | \(287\) |
| 2 | \(103\) | \(265\) |
| 3 | \(110\) | \(137\) |
| 4 | \(37\) | \(300\) |

The summary statistics shown are:

\[
\sum x=369, \quad \sum y=989, \quad \sum x^2=38239, \quad \sum y^2=261363, \quad \sum xy=87618.
\]

There are \(n=4\) paired observations.

\[
S_{xx}=38239-\frac{369^2}{4}=38239-\frac{136161}{4}=38239-34040.25=4198.75.
\]

\[
S_{yy}=261363-\frac{989^2}{4}=261363-\frac{978121}{4}=261363-244530.25=16832.75.
\]

\[
S_{xy}=87618-\frac{(369)(989)}{4}=87618-\frac{364941}{4}=87618-91235.25=-3617.25.
\]

Now substitute into the PMCC formula:

\[
r=\frac{-3617.25}{\sqrt{(4198.75)(16832.75)}}.
\]

\[
(4198.75)(16832.75)=70669215.3125.
\]

\[
r=\frac{-3617.25}{\sqrt{70669215.3125}} \approx \frac{-3617.25}{8406.498}\approx -0.4303.
\]

To two decimal places:

\[
\boxed{r\approx -0.43.}
\]

Interpretation: \(r\approx -0.43\) suggests a **moderate negative linear correlation** in this small data set.

Important caution: the data set has only four observations and is labelled as made-up in the source slide, so it is useful as a calculation example, not as a real-world conclusion.

## 8.7 Coding and PMCC

The transcript states that the correlation coefficient is unaffected by linear coding of the form

\[
ax+b
\]

when \(a>0\).

Suppose \(X=ax+b\), where \(a>0\). This stretches or shifts the \(x\)-axis, but it does not reverse the order of the \(x\)-values. The linear pattern is still equally tight, so the correlation coefficient is unchanged.

Similarly, if \(Y=cy+d\), where \(c>0\), then coding the \(y\)-values also leaves the strength and direction of correlation unchanged.

So, for positive linear coding:

\[
r_{X,Y}=r_{x,y}.
\]

If \(a<0\) or \(c<0\), the direction is reversed. A positive relationship may become negative, or a negative relationship may become positive.

\[
\boxed{\text{Positive coding preserves \(r\); negative coding reverses direction.}}
\]

## 8.8 PMCC and suitability of a linear model

If \(r\approx 1\) or \(r\approx -1\), then the points lie close to a straight line, so a linear model may be suitable.

If \(r\approx 0\), then the points do not show strong linear correlation, so a linear model may not be suitable.

A strong value of \(r\) does not prove the model is perfect. It only supports the idea that a straight-line model is reasonable for the observed data.

## 8.9 Limitation: PMCC detects linear correlation

PMCC is designed to measure **linear** correlation.

A data set can have a clear pattern but still have \(r\approx 0\). For example, points could lie on a curve. There may be a strong non-linear relationship, but PMCC may not detect it because the points do not lie close to a straight line.

\[
\boxed{r\approx 0 \text{ means little/no linear correlation, not necessarily no relationship at all.}}
\]

## 8.10 Limitation: correlation does not imply causation

If two variables have a high positive or negative correlation, that does not prove one causes the other.

From a high \(|r|\), you may say:

\[
\text{There is evidence of a strong linear association.}
\]

You must not automatically say:

\[
\text{One variable causes the other.}
\]

## 8.11 Limitation: PMCC does not protect you from extrapolation

A strong PMCC does not automatically make predictions safe outside the observed range. If your data use \(x\)-values from \(2\leq x\leq 10\), predicting at \(x=100\) is extrapolation. Even if \(r=0.98\), that does not guarantee the straight-line pattern continues beyond the data range.

## 8.12 Boundary note: Spearman’s rank is not core here

The uploaded lesson evidence contains extensive Spearman’s rank material. However, the supplied CCEA Further Mathematics specification map for `FAS2-BIV` confirms PMCC but does not list Spearman’s rank as a required learning outcome.

\[
\boxed{\text{Spearman’s rank is optional enrichment, not CCEA FAS2 core content from the supplied evidence.}}
\]

# 9. Visual Asset Integration

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientMermaid-001 | Source: CCEA FAS2-BIV-LO001 + transcript PMCC method | Insert from mermaid/FAS2ProductMomentCorrelationCoefficientMermaid-001.md | Purpose: Show the full PMCC calculation workflow from bivariate data to interpretation. Description: Flowchart should show paired data, summary statistics, calculation of Sxx/Syy/Sxy, calculation of r, then interpretation and limitation check.]

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientSVG-001 | Source: Chapter_2_Correlation screenshots + transcript visual explanation | Insert from svg/FAS2ProductMomentCorrelationCoefficientSVG-001.svg | Purpose: Preserve the correlation coefficient scale from -1 to +1. Description: A luxury-minimalist row of scatter panels showing perfect positive, strong positive, weak positive, no linear correlation, weak negative, strong negative and perfect negative correlation.]

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientSVG-002 | Source: PMCC formula evidence from transcript and formula booklet reference | Insert from svg/FAS2ProductMomentCorrelationCoefficientSVG-002.svg | Purpose: Provide a formula card for Sxx, Syy, Sxy and r. Description: Show Sxx, Syy, Sxy stacked as corrected sums, feeding into r = Sxy / sqrt(Sxx Syy).]

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2ProductMomentCorrelationCoefficientBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths scatter-diagram interpretation with Further Maths PMCC calculation. Description: Left side: ordinary AS/A2 scatter diagram language. Right side: FAS2 numerical PMCC calculation and interpretation.]

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientTikZ-001 | Source: Transcript warning that r does not measure steepness | Insert from tikz/FAS2ProductMomentCorrelationCoefficientTikZ-001.tex | Purpose: Show that r measures closeness to a straight line, not gradient. Description: Two exact straight-line data sets with different gradients but the same perfect positive correlation r = 1.]

[VISUAL PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientTikZ-002 | Source: AI-proposed teaching enhancement based on PMCC limitations | Insert from tikz/FAS2ProductMomentCorrelationCoefficientTikZ-002.tex | Purpose: Show why r ≈ 0 does not always mean no pattern. Description: Contrast a random cloud with a clear U-shaped non-linear pattern, both labelled as having little/no linear correlation.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2ProductMomentCorrelationCoefficientWidget-001.html | Purpose: PMCC summary-statistics calculator.]

This widget asks the student to input \(n,\sum x,\sum y,\sum x^2,\sum y^2,\sum xy\). It displays \(S_{xx}\), \(S_{yy}\), \(S_{xy}\), then \(r\). It checks that \(n>1\), \(S_{xx}>0\), \(S_{yy}>0\), and \(-1\leq r\leq 1\).

[INTERACTIVE PLACEHOLDER: FAS2ProductMomentCorrelationCoefficientWidget-002 | Source: AI-proposed teaching enhancement based on transcript warnings | Insert from widgets/FAS2ProductMomentCorrelationCoefficientWidget-002.html | Purpose: Correlation interpretation sorter.]

This widget shows \(r\)-values and asks the student to match each value to a correct interpretation, while rejecting trap cards such as “This means the gradient is large”, “This proves \(x\) causes \(y\)”, and “This guarantees safe extrapolation”.

# 11. Worked Examples

## Worked Example 1: Calculating PMCC from paired data

**Evidence source:** Dr Frost S3 PMCC recap slide.  
**On-spec status:** Core, because CCEA FAS2-BIV-LO001 requires calculation and interpretation of PMCC.  
**Ordinary Maths idea used:** Scatter diagrams and PMCC.  
**Further Maths upgrade:** Full interpretation and limitation inside bivariate-distribution work.

### Question

The data below compare \(x\), an 11+ NVR score, with \(y\), an average AS point score.

| Observation | \(x\) | \(y\) |
|---:|---:|---:|
| 1 | \(119\) | \(287\) |
| 2 | \(103\) | \(265\) |
| 3 | \(110\) | \(137\) |
| 4 | \(37\) | \(300\) |

The summary statistics are:

\[
\sum x=369,\qquad \sum y=989,
\]

\[
\sum x^2=38239,\qquad \sum y^2=261363,
\]

\[
\sum xy=87618.
\]

Calculate the product-moment correlation coefficient.

### Solution

There are four paired observations, so \(n=4\).

\[
S_{xx}=38239-\frac{369^2}{4}=38239-\frac{136161}{4}=38239-34040.25=4198.75.
\]

\[
S_{yy}=261363-\frac{989^2}{4}=261363-\frac{978121}{4}=261363-244530.25=16832.75.
\]

\[
S_{xy}=87618-\frac{(369)(989)}{4}=87618-\frac{364941}{4}=87618-91235.25=-3617.25.
\]

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}=\frac{-3617.25}{\sqrt{(4198.75)(16832.75)}}.
\]

\[
(4198.75)(16832.75)=70669215.3125.
\]

\[
r=\frac{-3617.25}{\sqrt{70669215.3125}}\approx \frac{-3617.25}{8406.498}\approx -0.4303.
\]

\[
\boxed{r\approx -0.43.}
\]

### Interpretation

The value \(r\approx -0.43\) suggests a **moderate negative linear correlation**. The sign is negative, so larger \(x\)-values tend to be associated with smaller \(y\)-values in this data set. The magnitude is not close to \(1\), so the linear association is not especially strong.

### Teaching note

This example is useful for PMCC arithmetic, but the original Dr Frost slide labels the data as made-up. So the conclusion is about the sample calculation, not a real claim about school admissions or academic outcomes.

## Worked Example 2: PMCC from summary statistics

**Evidence source:** Teacher transcript for PMCC example.  
**On-spec status:** Core method.  
**Evidence limitation:** The transcript preserves the method and final value clearly, but some original summary-statistic values appear garbled in the transcript. Only the readable mathematical method and stated intermediate/final values are preserved.

### Question

A data set contains \(n=15\) paired observations. The teacher calculates the corrected sums:

\[
S_{xx}=490.2293\ldots,\quad S_{yy}=9034.93\ldots,\quad S_{xy}=197.6266\ldots.
\]

Calculate the PMCC.

### Solution

Use

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}.
\]

Substitute:

\[
r=\frac{197.6266\ldots}{\sqrt{(490.2293\ldots)(9034.93\ldots)}}.
\]

\[
(490.2293\ldots)(9034.93\ldots)\approx 4429044.6.
\]

\[
\sqrt{4429044.6}\approx 2104.529.
\]

\[
r\approx \frac{197.6266}{2104.529}\approx 0.0939.
\]

However, the transcript later states a final value near \(r=0.906\). This is an evidence inconsistency: the displayed intermediate values in the transcript appear to have transcription/OCR errors. The teaching method remains valid, but the numerical example cannot safely be preserved as a fully reliable worked example unless the original slide/table is supplied.

### Preserved method

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n},\quad S_{yy}=\sum y^2-\frac{(\sum y)^2}{n},\quad S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n},\quad r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}.
\]

## Worked Example 3: Positive coding and PMCC

**Evidence source:** Teacher transcript PMCC coding example.  
**On-spec status:** Core-adjacent exam technique. PMCC is core; coding is evidence-backed and useful but should not be treated as a separate CCEA LO.  
**Evidence limitation:** The transcript has some unclear unit wording, but the algebraic structure and final values are readable.

### Question

Data are collected on the amount of supplement \(D\) and oat milk yield \(M\). The data are coded by

\[
x=\frac{D}{2}-6,\qquad y=\frac{M}{20}.
\]

The transcript states:

\[
S_{yy}=0.05915,
\]

and asks us to show that

\[
S_{MM}=23.66.
\]

It also gives:

\[
\sum x=44,\qquad \sum D^2=4592,\qquad S_{DM}=90.6,\qquad n=8.
\]

Find the PMCC between \(D\) and \(M\), using \(S_{MM}=23.66\).

### Solution part 1: Show that \(S_{MM}=23.66\)

Since \(y=M/20\), the spread in \(y\) is scaled by a factor of \(20\) compared with the spread in \(M\). Because variances and corrected sums scale by the square of the scale factor:

\[
S_{MM}=20^2S_{yy}=400S_{yy}.
\]

\[
S_{MM}=400(0.05915)=23.66.
\]

\[
\boxed{S_{MM}=23.66.}
\]

### Solution part 2: Find \(S_{DD}\)

From \(x=D/2-6\), make \(D\) the subject:

\[
x+6=\frac{D}{2},\qquad D=2x+12.
\]

Sum over all \(n=8\) observations:

\[
\sum D=\sum(2x+12)=2\sum x+\sum 12=2\sum x+8(12).
\]

Substitute \(\sum x=44\):

\[
\sum D=2(44)+8(12)=88+96=184.
\]

\[
S_{DD}=\sum D^2-\frac{(\sum D)^2}{n}=4592-\frac{184^2}{8}.
\]

\[
184^2=33856,\qquad \frac{33856}{8}=4232.
\]

\[
S_{DD}=4592-4232=360.
\]

### Solution part 3: Calculate \(r\)

\[
r=\frac{S_{DM}}{\sqrt{S_{DD}S_{MM}}}=\frac{90.6}{\sqrt{(360)(23.66)}}.
\]

\[
360(23.66)=8517.6,
\]

\[
r=\frac{90.6}{\sqrt{8517.6}}\approx \frac{90.6}{92.291}\approx 0.9817.
\]

To three significant figures:

\[
\boxed{r=0.982.}
\]

### Interpretation

The value \(r=0.982\) suggests a **very strong positive linear correlation** between \(D\) and \(M\) for the observed data.

# 12. Common Mistakes and Exam Traps

## Trap 1: Saying \(r\) is the gradient

Wrong: \(r=0.9\) means the line is steep.

Correct: \(r=0.9\) means the points lie close to an upward-sloping straight-line pattern.

## Trap 2: Treating \(r=0\) as “no pattern”

Wrong: \(r=0\Rightarrow\) no relationship of any kind.

Correct: \(r=0\Rightarrow\) no linear correlation. There may still be a non-linear pattern.

## Trap 3: Forgetting the correction terms

Wrong:

\[
S_{xx}=\sum x^2-(\sum x)^2.
\]

Correct:

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n}.
\]

## Trap 4: Mixing up \(S_{xy}\) and \(\sum xy\)

Wrong:

\[
r=\frac{\sum xy}{\sqrt{S_{xx}S_{yy}}}.
\]

Correct:

\[
r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}},\qquad S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n}.
\]

## Trap 5: Rounding too early

Keep intermediate values exact or to several decimal places. Round \(r\) only at the end.

## Trap 6: Saying correlation proves causation

A high value of \(r\) means strong linear association. It does not prove \(x\) causes \(y\).

## Trap 7: Ignoring the scatter diagram

If a question gives both a scatter diagram and \(r\), use both.

## Trap 8: Importing Spearman’s rank into the core answer

The uploaded evidence includes Spearman’s rank, but the supplied CCEA FAS2-BIV LO table confirms only PMCC for this lesson. Spearman’s rank should not be taught as core CCEA FAS2 content unless further official evidence is supplied.

# 13. Practice Questions

These are AI-generated on-spec practice questions. They are not past-paper or textbook questions.

## Question 1: Basic summary-statistics calculation

For \(n=5\) paired observations, the summary statistics are:

\[
\sum x=30,\quad \sum y=40,\quad \sum x^2=220,\quad \sum y^2=390,\quad \sum xy=285.
\]

Calculate the product-moment correlation coefficient.

## Question 2: Interpretation

A set of paired data has \(r=-0.91\). Explain what this tells you about the relationship between the two variables.

## Question 3: Warning about steepness

Two data sets both have \(r=1\). One lies exactly on \(y=2x+5\), and the other lies exactly on \(y=50x-7\). Explain why the two data sets can have the same value of \(r\).

## Question 4: Linear correlation limitation

A scatter diagram shows points lying close to a U-shaped curve. The PMCC is calculated as \(r=0.02\). A student writes: “There is no relationship between the variables.” Explain why this conclusion is not justified.

## Question 5: Coded data

A variable \(x\) is coded as \(X=3x+10\). A variable \(y\) is coded as \(Y=2y-5\). State whether the PMCC between \(X\) and \(Y\) is the same as the PMCC between \(x\) and \(y\). Explain your answer.

## Question 6: Negative coding

A variable \(x\) is coded as \(X=-2x+7\). A variable \(y\) is unchanged. Explain what happens to the sign of the correlation coefficient.

## Question 7: Exam-style full calculation

For \(n=6\) paired observations:

\[
\sum x=42,\quad \sum y=51,\quad \sum x^2=334,\quad \sum y^2=467,\quad \sum xy=389.
\]

1. Calculate \(S_{xx}\), \(S_{yy}\), and \(S_{xy}\).  
2. Calculate \(r\).  
3. Interpret your answer.

# 14. Worked Solutions

## Solution 1

Given \(n=5\), \(\sum x=30\), \(\sum y=40\), \(\sum x^2=220\), \(\sum y^2=390\), \(\sum xy=285\).

\[
S_{xx}=220-\frac{30^2}{5}=220-\frac{900}{5}=220-180=40.
\]

\[
S_{yy}=390-\frac{40^2}{5}=390-\frac{1600}{5}=390-320=70.
\]

\[
S_{xy}=285-\frac{(30)(40)}{5}=285-\frac{1200}{5}=285-240=45.
\]

\[
r=\frac{45}{\sqrt{(40)(70)}}=\frac{45}{\sqrt{2800}}\approx \frac{45}{52.915}\approx 0.8504.
\]

\[
\boxed{r=0.850}\quad \text{to three significant figures.}
\]

This suggests a strong positive linear correlation.

## Solution 2

Since \(r=-0.91\), the correlation is negative. Since \(|r|=0.91\) is close to \(1\), the correlation is strong.

\[
\boxed{\text{There is a strong negative linear correlation between the variables.}}
\]

It does not mean one variable causes the other.

## Solution 3

Both data sets lie exactly on straight lines with positive gradients, so both have \(r=1\). The gradients are different, \(2\neq 50\), but \(r\) does not measure steepness. It measures how closely the points lie to a straight-line pattern.

## Solution 4

\(r=0.02\) means little or no **linear** correlation. A U-shaped curve is a non-linear pattern, so the correct conclusion is:

\[
\boxed{\text{There is little/no linear correlation, but there may be a non-linear relationship.}}
\]

## Solution 5

The codings are \(X=3x+10\) and \(Y=2y-5\). Both multipliers are positive, so the PMCC is unchanged:

\[
\boxed{r_{X,Y}=r_{x,y}.}
\]

## Solution 6

The coding \(X=-2x+7\) has a negative multiplier. Multiplying by a negative number reverses the order of the \(x\)-values, so the sign of the correlation reverses. If the original correlation is \(r\), the new correlation is \(-r\).

## Solution 7

\[
S_{xx}=334-\frac{42^2}{6}=334-\frac{1764}{6}=334-294=40.
\]

\[
S_{yy}=467-\frac{51^2}{6}=467-\frac{2601}{6}=467-433.5=33.5.
\]

\[
S_{xy}=389-\frac{(42)(51)}{6}=389-\frac{2142}{6}=389-357=32.
\]

\[
r=\frac{32}{\sqrt{(40)(33.5)}}=\frac{32}{\sqrt{1340}}\approx \frac{32}{36.606}\approx 0.874.
\]

Since \(r\approx 0.874\), there is a strong positive linear correlation between the variables. This means larger \(x\)-values tend to be associated with larger \(y\)-values. It does not prove causation.

# 15. Exam Technique Notes

## Method selection

Use PMCC when the question asks for product-moment correlation coefficient, PMCC, Pearson correlation coefficient, \(r\), or correlation coefficient from summary statistics.

Do not switch to Spearman’s rank unless the question explicitly asks for rankings or \(r_s\), and remember Spearman is boundary-risk/enrichment for this CCEA FAS2 lesson unless official evidence is supplied.

## Formula layout

Write:

\[
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n},\quad S_{yy}=\sum y^2-\frac{(\sum y)^2}{n},\quad S_{xy}=\sum xy-\frac{(\sum x)(\sum y)}{n},\quad r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}.
\]

This makes your working readable and reduces the chance of dropping \(n\).

## Interpretation sentence template

```text
Since r = ..., there is a [weak/moderate/strong] [positive/negative] linear correlation between [variable x] and [variable y].
```

Then add:

```text
This does not prove causation.
```

when the question asks for interpretation or comment.

## Scatter diagram comment template

If a scatter diagram is supplied, combine visual and numerical evidence:

```text
The value of r is close to 1/-1, and the scatter diagram shows points lying close to a straight line. Therefore a linear model appears suitable.
```

or:

```text
The value of r is close to 0, and the scatter diagram does not show points lying close to a straight line. Therefore a linear model does not appear suitable.
```

## Exact vs decimal

Keep exact or high-accuracy values for \(S_{xx}\), \(S_{yy}\), and \(S_{xy}\). Round \(r\) only at the end.

## Calculator mode

A calculator may calculate PMCC directly from raw data, but when summary statistics are supplied, you should be ready to use the formula. Calculator use should validate the method, not replace clear working when the exam asks for calculation.

## Coding note

For coding of the form \(X=ax+b\), \(Y=cy+d\), if \(a>0\) and \(c>0\), then \(r_{X,Y}=r_{x,y}\). If exactly one of \(a\) and \(c\) is negative, the sign of \(r\) reverses. If both are negative, the direction reverses twice, so the sign is preserved.

# 16. Syllabus Gap Check

## LO coverage table

| LO ID | Official wording | Covered? | Evidence strength |
|---|---|---:|---|
| `FAS2-BIV-LO001` | calculate the product-moment correlation coefficient and understand its use, interpretation and limitations | Yes | Strong for PMCC calculation, interpretation and limitations. |

## Evidence coverage table

| Evidence item | Covered in lesson? | Notes |
|---|---:|---|
| Correlation coefficients vary from \(-1\) to \(+1\) | Yes | Sections 6-8. |
| \(-1\) perfect negative, \(+1\) perfect positive, \(0\) no linear correlation | Yes | Sections 7-8. |
| Strength is closeness to a straight line, not steepness | Yes | Major warning throughout. |
| PMCC formula using \(S_{xx}\), \(S_{yy}\), \(S_{xy}\) | Yes | Sections 7-8, 11-14. |
| Positive linear coding does not change PMCC | Yes | Sections 8, 11, 14-15. |
| Use of scatter diagram and \(r\) to judge linear suitability | Yes | Sections 8, 12, 15. |
| Spearman’s rank | Excluded from core | Logged as optional enrichment. |
| Tied ranks | Excluded from core | Logged as optional enrichment. |
| Correlation hypothesis testing | Excluded from core | Bridge/enrichment only. |

## Bridge coverage table

| Bridge source area | Covered? | Notes |
|---|---:|---|
| Ordinary scatter diagrams | Yes | Used as prerequisite. |
| Ordinary PMCC | Yes | Extended into FAS2 bivariate-distribution context. |
| Correlation does not imply causation | Yes | Preserved as key limitation. |
| A22 regression and extrapolation | Partly | Mentioned as linked context, not fully taught. |
| A22 hypothesis testing | Partly | Logged as bridge/enrichment, not core. |

## Off-Spec Content Found but Excluded

### Spearman’s rank correlation coefficient

The supplied lesson evidence includes Spearman’s rank \(r_s\), including the idea that data are converted to rankings and the coefficient measures agreement of rankings rather than linear relationship of the raw data. Excluded from core because the supplied CCEA FAS2-BIV LO list confirms PMCC but not Spearman’s rank.

### Tied ranks

Excluded from core because tied ranks belong to the Spearman’s rank material, not to confirmed CCEA FAS2-BIV-LO001.

### Non-parametric tests

Excluded from core because non-parametric tests are not confirmed in the supplied FAS2-BIV boundary.

### Correlation hypothesis testing

The transcript treats hypothesis testing as a later part of the chapter and links some of it to ordinary Maths A-Level content. Excluded from core because `FAS2-BIV-LO001` is about PMCC calculation, use, interpretation and limitations.

## Weak evidence warnings

| Issue | Warning |
|---|---|
| Screenshot PDF text not parsed | Only visible/readable diagram details are claimed. |
| Transcript contains OCR/transcription errors | Numerical examples with corrupted values are flagged rather than silently repaired. |
| Spearman evidence is rich but not confirmed by CCEA map | It is enrichment only unless official CCEA evidence is added. |

## Missing evidence log

| Missing item | Effect |
|---|---|
| Official CCEA specimen/past-paper PMCC question for FAS2-BIV | Practice questions are AI-generated, not labelled as past-paper. |
| Full clean PMCC transcript slides | Some worked examples are method-preserved but not fully source-perfect. |
| Official CCEA confirmation of Spearman’s rank | Spearman excluded from core. |

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements, not evidence-backed diagram details.

1. Add a dynamic PMCC calculator widget using summary statistics.
2. Add a scatterplot visual showing the same \(|r|\) with different gradients to kill the “\(r\) is gradient” misconception.
3. Add a comparison card: \(r\) measures strength and direction of linear correlation; \(b\) measures regression-line gradient; \(a\) measures intercept.
4. Add a “correlation courtroom” mini-widget where students reject invalid claims such as “correlation proves causation”.
5. Add a non-linear pattern warning visual showing a U-shaped graph with \(r\approx0\).
6. Add a bridge visual from ordinary scatter diagrams to Further Maths PMCC formulae.
7. Add a short calculator validation panel for Casio CG100 / standard A-Level statistics mode, but only as validation after method.

# 18. Supplementary Sources Used

## Project Sources used

- CCEA GCE Further Mathematics specification map.
- Further Maths README module map.
- Further Maths evidence checklist.
- Further Maths Portal Build Knowledge Evidence.

## Ordinary A-Level Maths bridge sources used

- Ordinary CCEA A-Level Mathematics bridge extracts.
- CCEA GCE Mathematics specification map.

These were used only for bridge context, not as Further Maths authority.

## Lesson-specific evidence used

- `transcripts.md`
- `Chapter_2_Correlation_📈_(Further_Statistics_2)_screenshots.pdf`
- `S3-Chp5-RegressionAndCorrelation.pdf`
- `Spearmans Rank Correlation Coefficient - Lesson.pdf`

## Cross-board source notes

The Dr Frost resources are cross-board/third-party teaching sources. PMCC is used in the core lesson only because the CCEA Further Maths specification map confirms PMCC as on-spec. Spearman’s rank, tied ranks, non-parametric tests and correlation hypothesis testing are logged as optional enrichment or boundary-risk content.

## Evidence limitations

The screenshot PDF did not provide parsed text, so only visible details from the rendered pages are preserved. Some transcript numerical examples contain unclear or corrupted values, so those are flagged instead of silently repaired.

# 19. Final Student Checklist

## Prerequisite confidence checklist

- [ ] identify paired/bivariate data;
- [ ] read a scatter diagram;
- [ ] describe positive and negative correlation;
- [ ] explain that correlation does not imply causation;
- [ ] substitute values carefully into formulae;
- [ ] use square roots and rounding accurately.

## Further Maths method checklist

- [ ] define PMCC as \(r\);
- [ ] state that \(-1\leq r\leq1\);
- [ ] calculate \(S_{xx}\);
- [ ] calculate \(S_{yy}\);
- [ ] calculate \(S_{xy}\);
- [ ] calculate \(r=S_{xy}/\sqrt{S_{xx}S_{yy}}\);
- [ ] interpret \(r\) in context;
- [ ] explain why \(r\) measures linear closeness, not steepness;
- [ ] explain why \(r\approx0\) means little/no linear correlation, not necessarily no relationship.

## Exam technique checklist

- [ ] show the corrected-sum formulae clearly;
- [ ] avoid dropping the denominator \(n\);
- [ ] avoid confusing \(S_{xy}\) with \(\sum xy\);
- [ ] round only at the end;
- [ ] use the scatter diagram and \(r\) together if both are supplied;
- [ ] write a conclusion using “linear correlation”;
- [ ] avoid claiming causation;
- [ ] avoid using Spearman’s rank unless the question explicitly asks for it.

## Bridge checklist

- [ ] ordinary Maths scatter-diagram language becomes a numerical PMCC calculation in FAS2;
- [ ] ordinary regression warnings still matter;
- [ ] \(r\) is not the same as the regression gradient;
- [ ] PMCC supports, but does not prove, the suitability of a linear model.

## Visual understanding checklist

- [ ] what a perfect positive correlation diagram looks like;
- [ ] what a perfect negative correlation diagram looks like;
- [ ] why a random cloud has \(r\approx0\);
- [ ] why a curved pattern may also have \(r\approx0\);
- [ ] why two lines with different steepness can both have \(r=1\).
