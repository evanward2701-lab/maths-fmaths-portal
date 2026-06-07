# AS2 Correlation and Regression Lines

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS2 |
| Unit name | AS 2 Applied Mathematics |
| Section | Statistics |
| Parent topic code | AS2-DPI |
| Parent topic name | Data presentation and interpretation |
| Lesson topic | Correlation and Regression Lines |
| Topic slug | correlation_and_regression_lines |
| Topic Pascal | CorrelationAndRegressionLines |
| Topic ID | AS2CorrelationAndRegressionLines |
| Lesson file | AS2_correlation_and_regression_lines_lesson.md |
| Core LO IDs | AS2-DPI-LO004, AS2-DPI-LO005, AS2-DPI-LO006, AS2-DPI-LO007 |
| Partial related LO | AS2-DPI-LO008 |
| Tags | `#AS2`, `#Statistics`, `#DataPresentation`, `#Correlation`, `#Regression`, `#InterpretContext`, `#EvaluateModel` |

---

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Official AS2 unit structure, AS2-DPI topic identity and LO boundaries. |
| `S1-Chp4-Correlation.pdf` | Slide-based definitions, diagrams, regression examples and interpolation/extrapolation warnings. |
| `Chapter_4_Correlation_🤖_(Applied_Year_1)_Transcript.md` | Spoken explanations, exam-style interpretation wording and worked examples. |
| `Chapter_4_Correlation_🤖_(Applied_Year_1)_Screenshots.pdf` | Visual reference for annotated scatter diagrams. Text was not parsed, so details are not over-claimed. |
| Project README/module-map conventions | Naming fields, unit prefixes, topic IDs and lesson file conventions. |
| Project evidence checklist | Missing evidence, visual limitations and off-spec risk logging. |

---

## Specification Alignment

| LO ID | CCEA requirement | Where covered in this lesson |
|---|---|---|
| AS2-DPI-LO004 | Interpret scatter diagrams and regression lines for bivariate data, including distinct population sections, excluding regression-line calculations | Definitions, scatter diagram interpretation, regression line theory, model suitability, interpolation and extrapolation |
| AS2-DPI-LO005 | Informal interpretation of correlation | Positive, negative, weak, strong and no correlation examples |
| AS2-DPI-LO006 | Calculate and interpret PMCC | Interpretation and prediction limitations covered. PMCC calculation is not covered because evidence is missing |
| AS2-DPI-LO007 | Correlation does not imply causation | Causal relationship section and Hideko example |
| AS2-DPI-LO008 | Interpret outliers | Lightly referenced through outlier effects on apparent correlation |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Recognise **bivariate data** and explain what a scatter diagram shows.
2. Describe correlation using both **type** and **strength**.
3. Interpret correlation in the context of a real problem.
4. Identify independent/explanatory and dependent/response variables.
5. Explain why correlation does not necessarily imply causation.
6. Interpret a given regression line of the form  
   \[
   y=a+bx.
   \]
7. Interpret the gradient and intercept of a regression line in context.
8. Decide whether a linear regression model is suitable.
9. Distinguish between interpolation and extrapolation.
10. Explain why extrapolation or reverse prediction can be unreliable.

---

## Prerequisite Recap

This lesson assumes you are already comfortable with:

| Skill | Why it matters here |
|---|---|
| Reading coordinates from graphs | Scatter diagrams are made from plotted pairs of data. |
| Understanding gradients of straight lines | Regression lines are interpreted through their gradient. |
| Substituting values into formulae | Predictions use equations such as \(y=a+bx\). |
| Writing sentence conclusions in context | Statistics marks often live inside the words, not just the arithmetic. |

No external GCSE source is used. The recap above is drawn only from the A-Level lesson evidence.

---

## Big Picture Explanation

So far in statistics, one variable can be summarised using averages, spread, box plots or histograms. Correlation asks a different question:

> What happens when we record **two variables** for each item, person, place or day?

For example, we might record:

\[
(\text{English score},\text{Maths score})
\]

for each student, or

\[
(\text{mean wind speed},\text{maximum gust})
\]

for each day.

A scatter diagram becomes a little statistical weather map. The cloud of points tells us whether the variables seem to move together, move against each other, or not really move together at all.

Regression then adds a straight-line model to that cloud. The line is not magic. It is a model. It is useful only when the data behaves roughly linearly and when predictions stay inside the safe territory of the data range.

---

## Key Definitions and Notation

### Bivariate data

**Bivariate data** is data with two variables.

Example:

\[
(14,33),\ (13,37),\ (13,29),\ldots
\]

could represent paired values such as daily mean wind speed and daily maximum gust.

### Correlation

**Correlation** describes:

1. the **type** of relationship between two variables, and  
2. the **strength** of that relationship.

The type can be:

| Type | Meaning |
|---|---|
| Positive correlation | As one variable increases, the other tends to increase. |
| Negative correlation | As one variable increases, the other tends to decrease. |
| No correlation | There is no clear increasing or decreasing pattern. |

The strength can be:

| Strength | Meaning |
|---|---|
| Strong | Points lie close to an imagined straight-line trend. |
| Weak | Points show a trend, but are more spread out. |

Important: correlation does **not** describe how steep the trend is. It describes direction and closeness to a pattern.

### Independent / explanatory variable

The **independent** or **explanatory** variable is usually placed on the horizontal axis.

It is the variable used to help explain or predict another variable.

Example:

\[
\text{Distance travelled} \rightarrow \text{Cost of train fare}
\]

Distance travelled would usually be the independent/explanatory variable.

### Dependent / response variable

The **dependent** or **response** variable is usually placed on the vertical axis.

It is the variable that responds to the explanatory variable.

Example:

\[
\text{Distance travelled} \rightarrow \text{Cost of train fare}
\]

Cost of train fare would usually be the dependent/response variable.

### Interpret

To **interpret** correlation means to write a worded description in the context of the problem.

A bare label such as:

\[
\text{negative correlation}
\]

is not enough if the question asks for an interpretation.

A proper interpretation would be:

> As age increases, weekly time spent on the internet tends to decrease.

### Causal relationship

Two variables have a **causal relationship** if a change in one variable directly causes a change in the other.

Warning:

\[
\text{Correlation} \nRightarrow \text{Causation}
\]

Variables can be correlated without one causing the other. A third hidden variable may be responsible.

### Regression line

A **regression line** is a line of best fit used as a model for bivariate data.

In this lesson, we use linear regression lines of the form:

\[
y=a+bx.
\]

Here:

| Symbol | Meaning |
|---|---|
| \(x\) | Independent/explanatory variable |
| \(y\) | Dependent/response variable |
| \(a\) | Intercept, the predicted value of \(y\) when \(x=0\) |
| \(b\) | Gradient, the predicted change in \(y\) for each 1-unit increase in \(x\) |

CCEA AS2-DPI requires interpretation of scatter diagrams and regression lines, but excludes calculating regression lines in this outcome.

### Interpolation

**Interpolation** means estimating a value **inside** the range of the data.

This is usually more reliable than extrapolation.

### Extrapolation

**Extrapolation** means estimating a value **outside** the range of the data.

This is risky because the model is being used beyond the evidence.

---

## Core Theory

### 1. Describing correlation

When asked to describe correlation, give:

\[
\text{strength}+\text{type}.
\]

Examples:

| Scatter pattern | Description |
|---|---|
| Points loosely trend upward | Weak positive correlation |
| Points loosely trend downward | Weak negative correlation |
| Points tightly trend upward | Strong positive correlation |
| No visible trend | No correlation |

Do not say “strong no correlation”. If there is no correlation, the strength is not needed.

### 2. Interpreting correlation in context

A question may ask:

> Describe the correlation.

or:

> Interpret the correlation.

These are not always the same. The second demands context.

Example: age and weekly time on the internet.

State:

\[
\text{weak negative correlation}
\]

Interpret:

> As age increases, weekly time spent on the internet tends to decrease.

Equivalent valid interpretation:

> Younger people tend to spend more time on the internet per week.

### 3. Correlation does not imply causation

Suppose a scatter diagram shows negative correlation between:

\[
\text{age left education}
\]

and

\[
\text{hourly pay at age 25}.
\]

A student says:

> More education causes people to earn a lower hourly rate of pay.

This conclusion may not be valid.

Reason:

People who left education later may have less work experience by age 25. Work experience could be affecting pay. So even if the variables are correlated, this does not prove that one directly causes the other.

A better statistical conclusion is:

> The data suggests a negative association, but it does not prove that staying in education longer causes lower pay.

### 4. Regression lines as models

At school level, you may have drawn a line of best fit by eye. At A-Level, the regression line is calculated, but in this lesson and under the CCEA AS2-DPI boundary, you are not required to calculate the regression-line equation.

You may be given an equation such as:

\[
y=20+3x.
\]

This is a model.

If:

\[
x=\text{time spent revising in hours}
\]

and

\[
y=\text{exam mark},
\]

then the model predicts the exam mark from the number of hours spent revising.

### 5. Interpreting the gradient

For:

\[
y=20+3x,
\]

the gradient is:

\[
3.
\]

This means:

\[
\text{for each increase of }1\text{ in }x,\ y\text{ increases by }3.
\]

In context:

> For each extra hour spent revising, the exam mark increases by 3 marks.

Do not write only:

> The gradient is 3.

That is a calculation label, not an interpretation.

### 6. Interpreting the intercept

For:

\[
y=20+3x,
\]

the intercept is:

\[
20.
\]

This is the predicted value of \(y\) when:

\[
x=0.
\]

So:

\[
y=20+3(0)
\]

\[
y=20+0
\]

\[
y=20.
\]

In context:

> A student who did no revision would be predicted to get 20 marks.

However, intercepts can sometimes be unrealistic. If \(x=0\) is outside the data range or impossible in context, treat the intercept carefully.

### 7. Suitability of a linear regression model

A linear regression line is more suitable when:

1. the scatter diagram shows a roughly straight-line pattern, and  
2. the correlation is reasonably strong.

If the data curves, a straight line may be a poor model.

Example:

Rabbit population over time may grow exponentially rather than linearly. A straight line may not fit the data well. Exponential regression is not part of this AS2 lesson; it is logged as enrichment only.

### 8. Interpolation and extrapolation

Suppose a regression equation was created from data where:

\[
30\leq x\leq 40.
\]

If you estimate at:

\[
x=39,
\]

then \(39\) is inside the data range, so this is interpolation.

If you estimate at:

\[
x=30
\]

but the original data range begins above 30, then this is extrapolation.

General rule:

\[
\text{Inside data range} \Rightarrow \text{more reliable}
\]

\[
\text{Outside data range} \Rightarrow \text{less reliable}
\]

### 9. Predicting the dependent variable only

If the regression line is the regression line of \(y\) on \(x\), then it is designed to predict:

\[
y
\]

from:

\[
x.
\]

It should not normally be used backwards to predict \(x\) from \(y\).

Example:

If the equation predicts head circumference \(y\) from gestation period \(x\), then using head circumference to predict gestation period is not appropriate for that regression equation.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesMermaid-001 | Source: CCEA AS2-DPI-LO005 + lesson correlation examples | Insert from mermaid/AS2CorrelationAndRegressionLinesMermaid-001.md | Purpose: Flowchart for classifying correlation by type and strength.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesMermaid-002 | Source: CCEA AS2-DPI-LO004 + lesson variable-axis explanation | Insert from mermaid/AS2CorrelationAndRegressionLinesMermaid-002.md | Purpose: Flowchart for identifying explanatory and response variables and writing contextual interpretations.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesMermaid-003 | Source: CCEA AS2-DPI-LO007 + lesson causation examples | Insert from mermaid/AS2CorrelationAndRegressionLinesMermaid-003.md | Purpose: Causation warning flowchart showing association, causal claim and lurking variable.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesMermaid-004 | Source: CCEA AS2-DPI-LO004 + lesson regression-line interpretation examples | Insert from mermaid/AS2CorrelationAndRegressionLinesMermaid-004.md | Purpose: Flowchart for interpreting \(a\) and \(b\) in \(y=a+bx\).]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesMermaid-005 | Source: CCEA AS2-DPI-LO006 + lesson interpolation/extrapolation examples | Insert from mermaid/AS2CorrelationAndRegressionLinesMermaid-005.md | Purpose: Reliability decision flowchart for interpolation, extrapolation and reverse prediction.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesSVG-001 | Source: S1-Chp4-Correlation.pdf page 5 + transcript section 1 | Insert from svg/AS2CorrelationAndRegressionLinesSVG-001.svg | Purpose: Show weak positive, weak negative, strong positive and no correlation scatter diagrams.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesSVG-002 | Source: S1-Chp4-Correlation.pdf page 5 | Insert from svg/AS2CorrelationAndRegressionLinesSVG-002.svg | Purpose: Label independent/explanatory and dependent/response variables on a scatter diagram.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesSVG-003 | Source: S1-Chp4-Correlation.pdf pages 8 to 10 | Insert from svg/AS2CorrelationAndRegressionLinesSVG-003.svg | Purpose: Show a regression line with vertical residual distances and labelled gradient/intercept.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesSVG-004 | Source: S1-Chp4-Correlation.pdf page 12 + transcript section 4 | Insert from svg/AS2CorrelationAndRegressionLinesSVG-004.svg | Purpose: Show interpolation inside the data range and extrapolation outside the data range.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesTikZ-001 | Source: CCEA AS2-DPI-LO005 + lesson correlation examples | Insert from tikz/AS2CorrelationAndRegressionLinesTikZ-001.tex | Purpose: Printable TikZ grid for weak positive, weak negative, strong positive and no correlation.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesTikZ-002 | Source: CCEA AS2-DPI-LO004 + lesson explanatory/response variable explanation | Insert from tikz/AS2CorrelationAndRegressionLinesTikZ-002.tex | Purpose: Printable TikZ scatter diagram labelling independent/explanatory and dependent/response variables.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesTikZ-003 | Source: CCEA AS2-DPI-LO004 + lesson regression-line examples | Insert from tikz/AS2CorrelationAndRegressionLinesTikZ-003.tex | Purpose: Printable TikZ regression-line diagram showing \(y=a+bx\), gradient, intercept and residual gaps.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesTikZ-004 | Source: CCEA AS2-DPI-LO006 + lesson interpolation/extrapolation examples | Insert from tikz/AS2CorrelationAndRegressionLinesTikZ-004.tex | Purpose: Printable TikZ safe-zone diagram for interpolation, extrapolation and reverse-prediction warnings.]

[VISUAL PLACEHOLDER: AS2CorrelationAndRegressionLinesTikZ-005 | Source: CCEA AS2-DPI-LO007 + lesson causation examples | Insert from tikz/AS2CorrelationAndRegressionLinesTikZ-005.tex | Purpose: Printable TikZ causation warning card.]

[INTERACTIVE PLACEHOLDER: AS2CorrelationAndRegressionLinesWidget-001 | Source: CCEA AS2-DPI boundary + lesson evidence | Insert from widgets/AS2CorrelationAndRegressionLinesWidget-001.html | Purpose: Let the student adjust scatter strength and see how correlation description changes.]

[INTERACTIVE PLACEHOLDER: AS2CorrelationAndRegressionLinesWidget-002 | Source: Lesson regression examples | Insert from widgets/AS2CorrelationAndRegressionLinesWidget-002.html | Purpose: Let the student enter \(a\), \(b\), and \(x\) in \(y=a+bx\), then identify interpolation/extrapolation status.]

---

## Worked Examples

### Worked Example 1: Four types of correlation

Classify each scatter diagram.

#### A. English score and Maths score

The points trend upward, but they are not tightly packed around a straight line.

So the correlation is:

\[
\boxed{\text{weak positive correlation}}
\]

Interpretation:

> Students with higher English scores tend to have higher Maths scores, but the relationship is not very strong.

#### B. Age and weekly time on the internet

The points trend downward, but they are spread out.

So the correlation is:

\[
\boxed{\text{weak negative correlation}}
\]

Interpretation:

> As age increases, weekly time spent on the internet tends to decrease.

#### C. Distance travelled and cost of train fare

The points trend upward and are close to a straight-line pattern.

So the correlation is:

\[
\boxed{\text{strong positive correlation}}
\]

Interpretation:

> As distance travelled increases, the cost of the train fare tends to increase.

#### D. Number of people in a city called Dave and crime rate

The points do not show a clear upward or downward pattern.

So the correlation is:

\[
\boxed{\text{no correlation}}
\]

No strength is needed because there is no clear correlation.

### Worked Example 2: Interpreting rather than just naming

A scatter diagram shows a negative correlation between age and weekly time on the internet.

#### Part A: State the correlation shown.

\[
\boxed{\text{negative correlation}}
\]

A fuller answer could be:

\[
\boxed{\text{weak negative correlation}}
\]

if the points are not tightly grouped.

#### Part B: Interpret the relationship.

A proper interpretation must mention the variables:

\[
\boxed{\text{As age increases, weekly time spent on the internet tends to decrease.}}
\]

Do not write only:

\[
\text{negative correlation}
\]

because that does not interpret the relationship in context.

### Worked Example 3: Correlation and causation

Hideko investigates the relationship between what people earn and the age they left education or training. Her data appears to show that people who left education later earn a lower hourly rate at age 25.

She concludes:

> More education causes people to earn a lower hourly rate of pay.

Give one reason why this conclusion might not be valid.

#### Solution

The data may show correlation, but it does not prove causation.

People who left education later may have significantly less work experience by age 25 than those who left education earlier.

So a better answer is:

\[
\boxed{\text{Those who left education later may have less work experience, and this could explain the lower pay.}}
\]

Therefore:

\[
\boxed{\text{The correlation does not prove that more education causes lower pay.}}
\]

### Worked Example 4: Interpreting \(y=20+3x\)

A regression model links revision time and exam mark:

\[
y=20+3x
\]

where:

\[
x=\text{time spent revising in hours}
\]

and

\[
y=\text{exam mark}.
\]

#### Part A: Interpret the gradient.

The gradient is:

\[
3.
\]

This means:

\[
\text{for each increase of }1\text{ in }x,\ y\text{ increases by }3.
\]

Since \(x\) is time in hours and \(y\) is exam mark:

\[
\boxed{\text{For each extra hour spent revising, the exam mark increases by 3 marks.}}
\]

#### Part B: Interpret the intercept.

The intercept is:

\[
20.
\]

This is the predicted value of \(y\) when:

\[
x=0.
\]

Substitute:

\[
y=20+3(0)
\]

\[
y=20+0
\]

\[
y=20.
\]

So:

\[
\boxed{\text{A student who did no revision would be predicted to get 20 marks.}}
\]

### Worked Example 5: Wind speed and maximum gust

From a large dataset, the daily mean wind speed \(w\) knots and the daily maximum gust \(g\) knots were recorded for the first 15 days of May in Camborne in 2015.

The regression line of \(g\) on \(w\) is:

\[
g=7.23+1.82w.
\]

#### Part A: Describe the correlation between daily mean wind speed and daily maximum gust.

The scatter diagram shows points trending upward and fairly close to a straight-line pattern.

\[
\boxed{\text{strong positive correlation}}
\]

In context:

\[
\boxed{\text{The higher the daily mean wind speed, the higher the daily maximum gust tends to be.}}
\]

#### Part B: Interpret the gradient.

The gradient is:

\[
1.82.
\]

This means that for each increase of:

\[
1
\]

knot in daily mean wind speed, \(g\) increases by:

\[
1.82
\]

knots.

So:

\[
\boxed{\text{For each increase of 1 knot in daily mean wind speed, the daily maximum gust increases by about 1.82 knots.}}
\]

#### Part C: Justify using a linear regression line.

A linear regression line is suitable when the data shows a roughly linear relationship.

Here, the points are strongly positively correlated and close to a straight-line trend.

\[
\boxed{\text{A linear regression model is suitable because the scatter diagram suggests a strong linear relationship.}}
\]

### Worked Example 6: Interpolation and extrapolation with babies

The head circumference \(y\) cm and gestation period \(x\) weeks are recorded for eight newborn babies.

The regression line of \(y\) on \(x\) is:

\[
y=8.91+0.624x.
\]

The regression equation is used to estimate head circumference for babies born at:

\[
39\text{ weeks}
\]

and:

\[
30\text{ weeks}.
\]

#### Part A: Comment on the reliability of the estimate for 39 weeks.

From the scatter diagram, \(39\) weeks is within the range of the data.

So this is interpolation.

\[
\boxed{\text{The estimate for 39 weeks is more likely to be reliable because it is within the data range.}}
\]

#### Part B: Comment on the reliability of the estimate for 30 weeks.

From the scatter diagram, \(30\) weeks is outside the range of the data.

So this is extrapolation.

\[
\boxed{\text{The estimate for 30 weeks is less reliable because it is outside the data range.}}
\]

#### Part C: Why should this regression equation not be used to estimate gestation period from head circumference?

The regression equation is:

\[
y=8.91+0.624x.
\]

It is the regression line of:

\[
y\text{ on }x.
\]

So it predicts:

\[
\text{head circumference}
\]

from:

\[
\text{gestation period}.
\]

It should not be used backwards to predict \(x\) from \(y\).

\[
\boxed{\text{The equation is designed to predict head circumference from gestation period, not gestation period from head circumference.}}
\]

### Worked Example 7: Job evaluation scheme

A company introduces a job evaluation scheme. Points \(x\) are awarded based on qualifications, skills and responsibility. Pay \(y\) pounds is allocated according to the number of points.

The regression equation is:

\[
y=4.5x-47.
\]

#### Part A: Describe the correlation between points and pay.

The gradient is positive:

\[
4.5>0.
\]

So the model implies:

\[
\boxed{\text{positive correlation}}
\]

In context:

\[
\boxed{\text{Jobs with more points tend to have higher pay.}}
\]

#### Part B: Interpret the gradient.

The gradient is:

\[
4.5.
\]

This means:

\[
\text{for every additional point, pay increases by }4.5\text{ pounds}.
\]

So:

\[
\boxed{\text{For every additional responsibility point, the pay increases by £4.50.}}
\]

#### Part C: Explain why this model might not be appropriate for all jobs.

Test a low point score, for example:

\[
x=10.
\]

Substitute into the model:

\[
y=4.5(10)-47
\]

\[
y=45-47
\]

\[
y=-2.
\]

This predicts:

\[
-£2.
\]

That does not make sense as pay.

So:

\[
\boxed{\text{The model may be inappropriate for low point scores because it can predict negative pay.}}
\]

### Worked Example 8: Sleep and aptitude score

A regression model relates sleep \(s\), in hours, to aptitude test score \(p\), in marks.

Suppose the gradient of the regression line is:

\[
5.60.
\]

This means:

\[
\text{for each extra }1\text{ hour of sleep, predicted score increases by }5.60\text{ marks}.
\]

Question:

> Describe the effect that an extra \(0.5\) hours of sleep may have on average on a student’s performance.

Since:

\[
0.5=\frac12,
\]

the increase in predicted score is:

\[
\frac12\times 5.60
\]

\[
=2.80.
\]

So:

\[
\boxed{\text{An extra 0.5 hours of sleep is predicted to increase the score by 2.8 marks on average.}}
\]

Model limitation:

The model may suggest that more and more sleep always improves performance. That is not sensible for all possible sleep times.

### Worked Example 9: Plant growth model

The relationship between two variables \(H\) and \(T\) is modelled by:

\[
H=46+2.24T.
\]

The model is based on observations of the independent variable \(T\) between:

\[
30\leq T\leq 80.
\]

Here:

\[
H=\text{height of a plant species in cm}
\]

and:

\[
T=\text{number of weeks since its seed was planted}.
\]

#### Part A: Describe the correlation implied by the model.

The gradient is:

\[
2.24.
\]

Since:

\[
2.24>0,
\]

the model implies:

\[
\boxed{\text{positive correlation}}
\]

#### Part B: Estimate the height after 45 weeks.

Since:

\[
T=45
\]

and \(45\) is inside the observed range \(30\leq T\leq80\), this is interpolation.

Substitute:

\[
H=46+2.24(45)
\]

Calculate:

\[
2.24(45)=100.8
\]

So:

\[
H=46+100.8
\]

\[
H=146.8.
\]

Therefore:

\[
\boxed{H=146.8\text{ cm}}
\]

#### Part C: Calculate the predicted growth over a 5-week period.

The gradient is:

\[
2.24.
\]

This means the model predicts growth of:

\[
2.24\text{ cm per week}.
\]

Over \(5\) weeks:

\[
2.24\times5=11.2.
\]

Therefore:

\[
\boxed{11.2\text{ cm}}
\]

#### Part D: Estimate the reliability of using the model at \(T=0\).

The data range is:

\[
30\leq T\leq80.
\]

But:

\[
0<30.
\]

So \(T=0\) is outside the data range.

\[
\boxed{\text{The estimate is not reliable because }T=0\text{ is outside the range of observed values.}}
\]

Also, in context, a newly planted seed being predicted as \(46\) cm tall is not sensible.

### Worked Example 10: Outliers and correlation

This example is retained as a general modelling idea, not as CCEA Large Data Set content.

A scatter diagram initially suggests weak negative correlation. Three outliers are then removed. The remaining points show no clear correlation.

The effect is:

\[
\boxed{\text{The correlation changes from weak negative correlation to no correlation.}}
\]

Exam-style wording:

> Removing the outliers weakens or removes the apparent negative correlation.

Core lesson:

Outliers can strongly affect how a scatter diagram appears. This links to AS2-DPI-LO008, but the main focus of this lesson remains AS2-DPI-LO004 to AS2-DPI-LO007.

---

## Guided Practice

### Practice Question 1: Describe and interpret correlation

A scatter diagram compares hours spent practising piano per week and score in a piano exam. The points trend upward and are close to a straight line.

1. Describe the correlation.
2. Interpret the relationship in context.

### Practice Question 2: Interpret a regression equation

A regression model for cost \(C\) pounds and distance \(d\) km is:

\[
C=3.50+0.42d.
\]

1. Interpret the gradient.
2. Interpret the intercept.
3. Estimate the cost for a journey of \(25\) km.

### Practice Question 3: Reliability

A regression line was based on data where:

\[
10\leq x\leq50.
\]

A student uses the model to estimate \(y\) when:

1. \(x=30\)
2. \(x=75\)

Comment on the reliability of each estimate.

### Practice Question 4: Causation

A study finds positive correlation between the number of ice creams sold and the number of people visiting the beach.

A student concludes:

> Buying ice cream causes people to visit the beach.

Explain why this conclusion may not be valid.

### Practice Question 5: Model limitation

A regression model predicts:

\[
y=12x-20
\]

where \(x\) is the number of hours worked and \(y\) is daily pay in pounds.

Explain why this model may not be suitable for very small values of \(x\).

---

## Common Mistakes and Exam Traps

### Trap 1: Naming correlation instead of interpreting it

Weak answer:

\[
\text{negative correlation}
\]

Better answer:

> As age increases, weekly time spent on the internet tends to decrease.

### Trap 2: Thinking steepness means strength

A steep line does not automatically mean strong correlation.

Strength depends on how close the points are to a trend, not how steep the trend is.

### Trap 3: Claiming causation from correlation

Do not write:

> \(x\) causes \(y\).

unless the context justifies a causal claim.

Safer wording:

> The data suggests an association between \(x\) and \(y\), but this does not prove causation.

### Trap 4: Using a regression line outside the data range

If the original data range is:

\[
30\leq x\leq80,
\]

then using:

\[
x=0
\]

is extrapolation and may be unreliable.

### Trap 5: Predicting the wrong variable

If the regression line is of \(y\) on \(x\), use it to predict \(y\) from \(x\), not \(x\) from \(y\).

### Trap 6: Treating the intercept as automatically meaningful

In:

\[
g=7.23+1.82w,
\]

the intercept \(7.23\) would be the predicted maximum gust when mean wind speed is \(0\). That may not be meaningful or within the data range.

Interpret intercepts carefully.

---

## Exam Technique Notes

1. **For “describe the correlation”**, give strength and type where possible:
   \[
   \text{strong positive},\quad \text{weak negative},\quad \text{no correlation}.
   \]
2. **For “interpret the correlation”**, write a sentence using both variables.
3. **For gradient interpretation**, use:
   > For each 1-unit increase in \(x\), \(y\) increases/decreases by [gradient] units.
4. **For extrapolation**, use:
   > This estimate is unreliable because the value used is outside the range of the data.
5. **For causation**, use:
   > Correlation does not imply causation. There may be another variable affecting both.
6. **For linear model suitability**, look for:
   \[
   \text{strong correlation}+\text{roughly straight-line pattern}.
   \]
7. **For model limitations**, test awkward values:
   \[
   x=0,\quad x\text{ very small},\quad x\text{ very large}.
   \]

---

## Full Worked Solutions to Guided Practice

### Solution 1

The points trend upward and are close to a straight line.

So:

\[
\boxed{\text{strong positive correlation}}
\]

Interpretation:

\[
\boxed{\text{Students who practise piano for more hours per week tend to score higher in the piano exam.}}
\]

### Solution 2

The model is:

\[
C=3.50+0.42d.
\]

#### 1. Gradient

The gradient is:

\[
0.42.
\]

This means:

\[
\boxed{\text{For each extra kilometre travelled, the cost increases by £0.42.}}
\]

#### 2. Intercept

The intercept is:

\[
3.50.
\]

This is the predicted cost when:

\[
d=0.
\]

So:

\[
\boxed{\text{The fixed starting cost is £3.50, according to the model.}}
\]

#### 3. Estimate for \(d=25\)

Substitute:

\[
C=3.50+0.42(25)
\]

Calculate:

\[
0.42(25)=10.50
\]

So:

\[
C=3.50+10.50
\]

\[
C=14.00.
\]

Therefore:

\[
\boxed{C=£14.00}
\]

### Solution 3

The data range is:

\[
10\leq x\leq50.
\]

#### 1. \(x=30\)

Since:

\[
10\leq30\leq50,
\]

the estimate is inside the data range.

\[
\boxed{\text{This is interpolation, so it is more likely to be reliable.}}
\]

#### 2. \(x=75\)

Since:

\[
75>50,
\]

the estimate is outside the data range.

\[
\boxed{\text{This is extrapolation, so it is less reliable.}}
\]

### Solution 4

There may be positive correlation between ice cream sales and beach visitors, but that does not prove that buying ice cream causes people to visit the beach.

A third variable may affect both. For example, hot weather may increase both beach visits and ice cream sales.

\[
\boxed{\text{The conclusion may not be valid because correlation does not imply causation.}}
\]

### Solution 5

The model is:

\[
y=12x-20.
\]

For a small value such as:

\[
x=1,
\]

we get:

\[
y=12(1)-20
\]

\[
y=12-20
\]

\[
y=-8.
\]

This predicts negative daily pay, which is not sensible.

\[
\boxed{\text{The model may not be suitable for small values of }x\text{ because it can predict negative pay.}}
\]

---

## Common CCEA-Style Wording

| Command phrase | What to do |
|---|---|
| Describe the correlation | Say positive/negative/no correlation and, if appropriate, strong/weak. |
| Interpret the correlation | Explain the relationship using the variables in the question. |
| Give an interpretation of the gradient | Say what happens to the dependent variable for each 1-unit increase in the independent variable. |
| Comment on reliability | Discuss data range, interpolation, extrapolation and whether the model is being used appropriately. |
| Justify the use of a linear regression model | Refer to the scatter diagram showing a roughly linear pattern and sufficiently strong correlation. |
| Explain why a conclusion may not be valid | Mention correlation does not imply causation or identify a possible lurking variable. |

---

## Syllabus Gap Check

| LO ID | Status | Comment |
|---|---|---|
| AS2-DPI-LO004 | Covered | Scatter diagrams, bivariate data and regression-line interpretation covered. Regression-line calculation excluded. |
| AS2-DPI-LO005 | Covered | Informal correlation language covered. |
| AS2-DPI-LO006 | Partially covered | Interpolation/extrapolation and interpretation covered. PMCC calculation method is missing from evidence. |
| AS2-DPI-LO007 | Covered | Correlation versus causation covered. |
| AS2-DPI-LO008 | Lightly touched | Outliers mentioned through effect on correlation, but not developed as a full outliers lesson. |

### Off-spec content excluded from core

- Calculating regression-line equations.
- Full least-squares derivation.
- Exponential regression.
- Edexcel Large Data Set facts.
- DrFrost/Pearson exercise page references as required CCEA tasks.
- PMCC non-coverage claim from old S1, because CCEA AS2 does require PMCC calculation.

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| AS2CorrelationAndRegressionLinesMermaid-001 | Mermaid | Correlation classification flowchart |
| AS2CorrelationAndRegressionLinesMermaid-002 | Mermaid | Explanatory/response variable flowchart |
| AS2CorrelationAndRegressionLinesMermaid-003 | Mermaid | Correlation versus causation flowchart |
| AS2CorrelationAndRegressionLinesMermaid-004 | Mermaid | Regression-line interpretation flowchart |
| AS2CorrelationAndRegressionLinesMermaid-005 | Mermaid | Interpolation/extrapolation reliability flowchart |
| AS2CorrelationAndRegressionLinesSVG-001 | SVG | Correlation type and strength grid |
| AS2CorrelationAndRegressionLinesSVG-002 | SVG | Independent/dependent variable labelling |
| AS2CorrelationAndRegressionLinesSVG-003 | SVG | Regression line with gradient/intercept and residuals |
| AS2CorrelationAndRegressionLinesSVG-004 | SVG | Interpolation vs extrapolation |
| AS2CorrelationAndRegressionLinesTikZ-001 | TikZ | Printable correlation grid |
| AS2CorrelationAndRegressionLinesTikZ-002 | TikZ | Printable variable-role scatter diagram |
| AS2CorrelationAndRegressionLinesTikZ-003 | TikZ | Printable regression-line interpretation diagram |
| AS2CorrelationAndRegressionLinesTikZ-004 | TikZ | Printable interpolation/extrapolation diagram |
| AS2CorrelationAndRegressionLinesTikZ-005 | TikZ | Printable causation warning card |
| AS2CorrelationAndRegressionLinesWidget-001 | HTML widget | Interactive scatter strength classifier |
| AS2CorrelationAndRegressionLinesWidget-002 | HTML widget | Regression prediction and reliability checker |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| DrFrost/Pearson Year 1 Applied Statistics correlation material | Cross-board support. Used only where matching CCEA AS2-DPI. |
| CCEA Specification Map | Core authority. |
| Project README/module map/checklist | Workflow and metadata authority. |

---

## Final Student Checklist

Before moving on, check that you can:

- [ ] Define bivariate data.
- [ ] Describe positive, negative and no correlation.
- [ ] Distinguish weak and strong correlation.
- [ ] Explain why steepness is not the same as strength.
- [ ] Identify the independent/explanatory variable.
- [ ] Identify the dependent/response variable.
- [ ] Interpret correlation in context.
- [ ] Explain why correlation does not imply causation.
- [ ] Use a given regression equation \(y=a+bx\).
- [ ] Interpret the gradient \(b\) in context.
- [ ] Interpret the intercept \(a\) carefully.
- [ ] Decide whether a linear regression model is suitable.
- [ ] Explain interpolation.
- [ ] Explain extrapolation.
- [ ] Comment on reliability using the data range.
- [ ] Avoid predicting the wrong variable from a regression line.
- [ ] Recognise that PMCC calculation still needs separate evidence and teaching for full CCEA AS2-DPI-LO006 coverage.
