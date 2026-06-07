# Regression, Correlation and Hypothesis Testing for Correlation

## Title and Metadata

- Course: CCEA GCE Mathematics
- Unit code: A22
- Unit name: A2 2 Applied Mathematics
- Applied section: Statistics
- Topic code: A22-HT
- Topic name: Statistical hypothesis testing
- Lesson focus: Regression, correlation, PMCC and hypothesis testing for correlation
- Topic slug: statistical_hypothesis_testing
- Topic Pascal: StatisticalHypothesisTesting
- Topic ID: A22StatisticalHypothesisTesting
- Lesson file: A22_statistical_hypothesis_testing_lesson.md

### Core LO IDs

- A22-HT-LO001
- A22-HT-LO002
- A22-HT-LO005

### Supporting A-Level links

- AS1 exponentials and logarithms: used for log-linear modelling recap.
- AS2 data presentation and interpretation: used for PMCC calculation and correlation interpretation.

---

## Evidence Map

| Evidence source | Use in lesson | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Official unit, topic and LO boundary | Core authority |
| Project module map | Metadata conventions and file naming | Core workflow evidence |
| Project evidence checklist | Missing evidence and off-spec logging rules | Core workflow evidence |
| Teacher transcript: Chapter 1 Regression & Correlation | Explanations, warnings, examples and calculator discussion | Core lesson evidence, controlled by CCEA boundary |
| DrFrost/Pearson-style PDF: Stats Year 2 Chapter 1 | Slide text, examples, tables and diagrams | Third-party lesson evidence, used only where on-spec |
| Screenshot PDF | Visual reference for diagram placeholders | Image-only support |

---

## Specification Alignment

### Core alignment

| LO ID | Official skill focus | Lesson section |
|---|---|---|
| A22-HT-LO001 | Use hypothesis testing language: null hypothesis, alternative hypothesis, significance level, test statistic, 1-tail test, 2-tail test, critical value, critical region, acceptance region and p-value | Definitions, Core Theory, Worked Examples |
| A22-HT-LO002 | Understand sample-to-population inference and the meaning of significance level | Big Picture, Core Theory, Hypothesis Testing Examples |
| A22-HT-LO005 | Interpret a given correlation coefficient using a p-value or critical value | PMCC section, Critical Value Tests, Exam Technique |

### Syllabus gaps within A22-HT

This lesson does **not** cover:

- A22-HT-LO003: hypothesis tests for a binomial proportion.
- A22-HT-LO004: hypothesis tests for a normal mean.

Those need separate lessons.

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain what regression means in the context of fitting a model to bivariate data.
2. Explain why some data are better modelled by an exponential model than a linear model.
3. Transform an exponential model of the form \(y=kb^x\) into a straight-line form using logarithms.
4. Understand that PMCC \(r\) measures **linear** correlation only.
5. Interpret values of \(r\) between \(-1\) and \(1\).
6. Use calculator output for \(a\), \(b\) and \(r\) in a regression model \(y=a+bx\).
7. Distinguish between the sample PMCC \(r\) and the population PMCC \(\rho\).
8. Set up and carry out a hypothesis test for correlation using a critical value.
9. Write a two-part statistical conclusion: comparison plus context.
10. Recognise when “no significant linear correlation” does not mean “no relationship at all”.

---

## Prerequisite Recap: A-Level Knowledge Needed

This lesson uses earlier A-Level ideas only.

### 1. Straight-line models

A straight-line model is often written as

\[
y=a+bx.
\]

Here:

- \(a\) is the \(y\)-intercept;
- \(b\) is the gradient;
- \(x\) is the explanatory variable;
- \(y\) is the response variable.

For example, the evidence uses the model

\[
y=20+3x,
\]

where:

- \(x\) is time spent revising;
- \(y\) is exam mark.

If \(x=0\),

\[
y=20+3(0)=20.
\]

So the model predicts 20 marks for no revision.

If \(x=5\),

\[
y=20+3(5)
\]

\[
y=20+15
\]

\[
y=35.
\]

So the model predicts 35 marks after 5 hours of revision.

### 2. Logarithm laws

For positive values:

\[
\log(AB)=\log A+\log B,
\]

\[
\log(A^n)=n\log A.
\]

These laws are the little gears inside the exponential regression work.

### 3. Exponentials

An exponential model may have the form

\[
y=kb^x,
\]

where:

- \(k\) is the initial multiplier;
- \(b\) is the growth or decay factor;
- \(x\) is the explanatory variable.

If \(b>1\), the model grows as \(x\) increases.

If \(0<b<1\), the model decays as \(x\) increases.

---

## Big Picture Explanation

Regression, correlation and hypothesis testing are three connected ideas.

### Regression

Regression asks:

> What model best explains the data?

In the simplest case, the model is a line:

\[
y=a+bx.
\]

The “regression” part is the act of choosing the model parameters, such as \(a\) and \(b\), so that the model fits the data as closely as possible.

For a straight-line model, this means choosing:

- the \(y\)-intercept;
- the gradient.

The evidence describes this as setting the parameters of the model, here the gradient and \(y\)-intercept of the line of best fit, to best explain the data.

### Correlation

Correlation asks:

> How strongly are the two variables related?

The PMCC, written \(r\), gives a numerical measure of **linear** correlation.

### Hypothesis testing for correlation

Hypothesis testing asks:

> Is the observed correlation strong enough to suggest a real population correlation, or could it have appeared just by chance?

That is the statistical heart of this lesson.

---

## Key Definitions and Notation

### Regression line

A regression line is a mathematically chosen line of best fit. It is not just a line drawn by eye.

For a linear model,

\[
y=a+bx.
\]

The constants \(a\) and \(b\) are chosen so that the model’s predicted \(y\)-values match the observed \(y\)-values as closely as possible.

### Extrapolation

Extrapolation means making predictions outside the original data range.

If the data only cover \(1\le x\le 12\), then using the model to predict at \(x=100\) would be extrapolation.

**Warning.** Extrapolation is unreliable because the trend may not continue outside the data range.

### Product Moment Correlation Coefficient

The Product Moment Correlation Coefficient, or PMCC, is denoted by

\[
r.
\]

It describes the **linear** correlation between two variables.

\[
-1\le r\le 1.
\]

Interpretation:

| Value of \(r\) | Meaning |
|---|---|
| \(r=-1\) | Perfect negative linear correlation |
| \(r=0\) | No linear correlation |
| \(r=1\) | Perfect positive linear correlation |

Rule of thumb from the evidence:

\[
r<-0.7
\]

or

\[
r>0.7
\]

is usually considered strong correlation.

A tidier way to say this is:

\[
|r|>0.7
\]

suggests strong linear correlation.

### Sample PMCC and population PMCC

The sample PMCC is

\[
r.
\]

The population PMCC is

\[
\rho.
\]

The Greek letter \(\rho\), called rho, represents the PMCC for the whole population.

So:

- \(r\) is the test statistic;
- \(\rho\) is the population parameter.

### Null hypothesis

The null hypothesis is written

\[
H_0.
\]

For correlation testing, the null hypothesis is usually:

\[
H_0:\rho=0.
\]

This means:

> There is no underlying linear correlation in the population.

### Alternative hypothesis

The alternative hypothesis is written

\[
H_1.
\]

For a positive correlation test:

\[
H_1:\rho>0.
\]

For a negative correlation test:

\[
H_1:\rho<0.
\]

For a two-tailed test, where we are testing for any correlation:

\[
H_1:\rho\ne0.
\]

### Critical value

A critical value is the threshold value that the test statistic must pass before we reject \(H_0\).

For correlation tests, the evidence uses critical values from a correlation coefficient table.

### Critical region

The critical region is the set of values that would make us reject \(H_0\).

For example, if the critical value is \(0.4428\) in a positive one-tailed test, then the critical region is:

\[
r>0.4428.
\]

---

## Core Theory

## 1. What regression means

Suppose we record:

- time spent revising, \(x\);
- exam mark, \(y\).

A simple model might be:

\[
y=20+3x.
\]

This says:

- if \(x=0\), then \(y=20\);
- for every extra hour of revision, the predicted mark increases by 3.

The model is not saying every student follows this exactly. It is giving a rule that tries to explain the overall pattern in the data.

The regression line is chosen to make the predicted \(y\)-values as close as possible to the actual \(y\)-values.

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-001 | Source: Lesson PDF page 4 and transcript | Insert from svg/A22StatisticalHypothesisTestingSVG-001.svg | Purpose: Show a scatter diagram of exam mark against revision time with regression line \(y=20+3x\).]

---

## 2. Why use exponential regression?

A straight line is not always the best model.

For some variables, such as population over time, an exponential model may fit better:

\[
y=kb^x.
\]

Here \(k\) and \(b\) are constants chosen to best match the data.

A linear model

\[
y=a+bx
\]

may not fit curved growth data well, while an exponential model

\[
y=kb^x
\]

may fit much better.

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-002 | Source: Lesson PDF pages 5-6 | Insert from svg/A22StatisticalHypothesisTestingSVG-002.svg | Purpose: Compare a poor linear fit with a better exponential fit for population-time data.]

---

## 3. Turning an exponential model into a straight-line model

Start with:

\[
y=kb^x.
\]

Take logarithms of both sides:

\[
\log y=\log(kb^x).
\]

Use the product law:

\[
\log(kb^x)=\log k+\log(b^x).
\]

So:

\[
\log y=\log k+\log(b^x).
\]

Now use the power law:

\[
\log(b^x)=x\log b.
\]

Therefore:

\[
\log y=\log k+x\log b.
\]

This has the structure of a straight-line equation.

Compare:

\[
Y=C+mX
\]

with

\[
\log y=\log k+x\log b.
\]

So if we plot:

- \(x\) on the horizontal axis;
- \(\log y\) on the vertical axis;

then the data should form a straight line if the exponential model is suitable.

The straight-line features are:

\[
\text{\(y\)-intercept}=\log k,
\]

\[
\text{gradient}=\log b.
\]

### Important algebra warning

Do **not** do this:

\[
\log(kb^x)=x\log(kb).
\]

That is wrong because \(x\) only applies to \(b\), not to the whole product \(kb\).

The correct split is:

\[
\log(kb^x)=\log k+\log(b^x)
\]

\[
=\log k+x\log b.
\]

This is a classic log-law trapdoor. Step gently.

---

## 4. PMCC measures linear correlation only

The PMCC \(r\) measures closeness to a straight-line relationship.

It does **not** measure every possible kind of relationship.

So:

- a low \(r\) means weak or no **linear** correlation;
- it does not prove the variables are unrelated;
- the data might follow a curved model, such as exponential or logarithmic.

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-003 | Source: Lesson PDF page 11 | Insert from svg/A22StatisticalHypothesisTestingSVG-003.svg | Purpose: Show the PMCC scale from \(-1\) to \(1\), including perfect negative, no correlation and perfect positive correlation.]

---

## 5. Calculator regression output

When using a calculator in statistics/regression mode with a linear model

\[
y=a+bx,
\]

the calculator can output:

- \(a\), the intercept;
- \(b\), the gradient;
- \(r\), the PMCC.

The evidence example uses the data:

\[
(1,3),\ (2,6),\ (3,5),\ (4,8).
\]

Calculator output:

\[
a=2,
\]

\[
b=1.4,
\]

\[
r=0.868\quad\text{approximately}.
\]

Therefore the regression line is:

\[
y=2+1.4x.
\]

The value

\[
r=0.868
\]

shows strong positive linear correlation.

[INTERACTIVE PLACEHOLDER: A22StatisticalHypothesisTestingWIDGET-001 | Source: Lesson PDF page 12 and transcript | Insert from widgets/A22StatisticalHypothesisTestingWIDGET-001.html | Purpose: Allow the student to enter paired data and see \(a\), \(b\), \(r\) and the regression line.]

---

## 6. Why hypothesis testing is needed for correlation

Suppose a spreadsheet randomly generates Maths marks and separately randomly generates English marks.

Because the two sets of marks are generated independently, the true population PMCC should be:

\[
\rho=0.
\]

There is no underlying population correlation.

But a sample might still give:

\[
r=0.219.
\]

Another random sample might give:

\[
r=-0.094.
\]

These sample values are not exactly zero because samples wobble. Randomness makes little ripples.

The question is:

> Is the sample PMCC statistically significant, or could it have appeared just by chance?

That is why we use a hypothesis test.

---

## 7. Hypothesis tests for correlation

For a correlation hypothesis test, the null hypothesis is:

\[
H_0:\rho=0.
\]

This means there is no underlying linear correlation in the population.

The alternative hypothesis depends on the wording.

### Positive correlation

If the question asks whether there is evidence of a positive correlation:

\[
H_1:\rho>0.
\]

This is a one-tailed test.

### Negative correlation

If the question asks whether there is evidence of a negative correlation:

\[
H_1:\rho<0.
\]

This is also a one-tailed test.

### Any correlation

If the question asks whether there is evidence of correlation, without specifying positive or negative:

\[
H_1:\rho\ne0.
\]

This is a two-tailed test.

---

## 8. Critical value method for correlation tests

The evidence uses critical values for the PMCC.

The general decision process is:

1. State \(H_0\) and \(H_1\).
2. Identify the sample size \(n\).
3. Identify the significance level.
4. Choose the correct critical value from the table.
5. Compare \(r\) with the critical value.
6. Decide whether to reject \(H_0\).
7. Write a conclusion in context.

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-004 | Source: Lesson PDF pages 17-19 | Insert from svg/A22StatisticalHypothesisTestingSVG-004.svg | Purpose: Flowchart for one-tailed and two-tailed PMCC hypothesis tests.]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-005 | Source: Lesson evidence and generated asset plan | Insert from svg/A22StatisticalHypothesisTestingSVG-005.svg | Purpose: Show one-tailed and two-tailed critical regions for \(r\).]

[INTERACTIVE PLACEHOLDER: A22StatisticalHypothesisTestingWIDGET-002 | Source: Lesson evidence and generated asset plan | Insert from widgets/A22StatisticalHypothesisTestingWIDGET-002.html | Purpose: Let the student check correlation-test decisions using \(r\), critical value and tail type.]

---

# Worked Examples

## Worked Example 1: Exponential regression with bacteria growth

The table shows data collected on the temperature \(t\), in degrees Celsius, of a colony of bacteria and its growth rate \(g\).

| Temperature \(t\) | 3 | 5 | 6 | 8 | 9 | 11 |
|---|---:|---:|---:|---:|---:|---:|
| Growth rate \(g\) | 1.04 | 1.49 | 1.79 | 2.58 | 3.1 | 4.46 |

The data are coded using:

\[
x=t
\]

and

\[
y=\log g.
\]

The regression line of \(y\) on \(x\) is:

\[
y=-0.2215+0.0792x.
\]

### Part (a)

Mika says that the constant \(-0.2215\) means the colony is shrinking when the temperature is \(0^\circ C\). Explain why Mika is wrong.

When:

\[
t=0,
\]

we have:

\[
x=t=0.
\]

Substitute into the regression line:

\[
y=-0.2215+0.0792x
\]

\[
y=-0.2215+0.0792(0)
\]

\[
y=-0.2215+0
\]

\[
y=-0.2215.
\]

But \(y\) is not the growth rate. The coding says:

\[
y=\log g.
\]

So:

\[
\log g=-0.2215.
\]

Using base 10 logs, undo the logarithm:

\[
g=10^{-0.2215}.
\]

Calculate:

\[
g=0.600\quad\text{to 3 significant figures}.
\]

Since:

\[
0.600>0,
\]

the growth rate is positive.

Therefore the colony is not shrinking at \(0^\circ C\). Mika confused \(\log g\) with \(g\).

### Part (b)

Given that the data can be modelled by:

\[
g=kb^t,
\]

where \(k\) and \(b\) are constants, find \(k\) and \(b\).

Start with the model:

\[
g=kb^t.
\]

Take logs:

\[
\log g=\log(kb^t).
\]

Use the product law:

\[
\log g=\log k+\log(b^t).
\]

Use the power law:

\[
\log g=\log k+t\log b.
\]

The given regression line is:

\[
y=-0.2215+0.0792x.
\]

Using the coding:

\[
y=\log g
\]

and

\[
x=t.
\]

So:

\[
\log g=-0.2215+0.0792t.
\]

Compare:

\[
\log g=\log k+t\log b
\]

with

\[
\log g=-0.2215+0.0792t.
\]

Therefore:

\[
\log k=-0.2215
\]

and

\[
\log b=0.0792.
\]

Now solve for \(k\):

\[
k=10^{-0.2215}
\]

\[
k=0.600\quad\text{to 3 significant figures}.
\]

Solve for \(b\):

\[
b=10^{0.0792}
\]

\[
b=1.20\quad\text{to 3 significant figures}.
\]

Therefore:

\[
\boxed{k=0.600,\quad b=1.20}.
\]

So the model is approximately:

\[
\boxed{g=0.600(1.20)^t}.
\]

---

## Worked Example 2: Rabbit population exponential model

Robert wants to model a rabbit population \(P\) with respect to time \(t\), in years.

He proposes:

\[
P=kb^t.
\]

The data are coded using:

\[
x=t
\]

and

\[
y=\log P.
\]

The regression line of \(y\) on \(x\) is:

\[
y=2+0.3x.
\]

Find \(k\) and \(b\).

Start with:

\[
P=kb^t.
\]

Take logs:

\[
\log P=\log(kb^t).
\]

Use the product law:

\[
\log P=\log k+\log(b^t).
\]

Use the power law:

\[
\log P=\log k+t\log b.
\]

The regression equation is:

\[
y=2+0.3x.
\]

Using the coding:

\[
y=\log P,
\]

\[
x=t.
\]

So:

\[
\log P=2+0.3t.
\]

Compare:

\[
\log P=\log k+t\log b
\]

with

\[
\log P=2+0.3t.
\]

Therefore:

\[
\log k=2
\]

and

\[
\log b=0.3.
\]

Solve for \(k\):

\[
k=10^2
\]

\[
k=100.
\]

Solve for \(b\):

\[
b=10^{0.3}
\]

\[
b=1.995\ldots
\]

\[
b=2.00\quad\text{to 3 significant figures}.
\]

Therefore:

\[
\boxed{k=100,\quad b=2.00}.
\]

The model is approximately:

\[
\boxed{P=100(2.00)^t}.
\]

### Interpretation

When:

\[
t=0,
\]

\[
P=100(2.00)^0.
\]

Since:

\[
(2.00)^0=1,
\]

\[
P=100.
\]

So the initial rabbit population is 100.

Each year, the population is multiplied by about 2, so the population approximately doubles each year.

---

## Worked Example 3: PMCC and a regression line

Use the paired data:

\[
(1,3),\ (2,6),\ (3,5),\ (4,8).
\]

A calculator in linear regression mode gives:

\[
a=2,
\]

\[
b=1.4,
\]

\[
r=0.868\quad\text{approximately}.
\]

The regression model is:

\[
y=a+bx.
\]

Substitute \(a=2\) and \(b=1.4\):

\[
y=2+1.4x.
\]

The value of \(r\) is close to \(1\), so there is strong positive linear correlation.

---

## Worked Example 4: Large data set windspeed and gust

From the large data set, the daily mean windspeed \(w\), in knots, and daily maximum gust \(g\), in knots, were recorded for the first 10 days in September in Hurn in 1987.

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(w\) | 4 | 4 | 8 | 7 | 12 | 12 | 3 | 4 | 7 | 10 |
| \(g\) | 13 | 12 | 19 | 23 | 33 | 37 | 10 | n/a | n/a | 23 |

### Part (a)

State the meaning of n/a.

“n/a” means the data are not available for those days.

### Part (b)

Calculate the PMCC for the remaining eight days.

The days with missing gust data are excluded.

Using the remaining eight paired values in calculator regression mode gives:

\[
r=0.9533\quad\text{to 4 significant figures}.
\]

### Part (c)

Comment on the suitability of a linear regression model.

Since:

\[
r=0.9533,
\]

and this is close to \(1\), there is a strong positive linear correlation.

The data points lie close to a straight line.

Therefore, a linear regression model is suitable for these data.

---

## Worked Example 5: Hypothesis test for positive correlation

A sample of size:

\[
n=10
\]

has sample PMCC:

\[
r=0.219.
\]

Test whether there is positive correlation at the \(10\%\) significance level.

### Step 1: State the hypotheses

The null hypothesis is:

\[
H_0:\rho=0.
\]

This means there is no underlying population correlation.

The alternative hypothesis is:

\[
H_1:\rho>0.
\]

This means there is positive population correlation.

### Step 2: Identify the test type

Since:

\[
H_1:\rho>0,
\]

this is a one-tailed positive correlation test.

### Step 3: Use the critical value

For:

\[
n=10
\]

at the \(10\%\) significance level, the critical value from the evidence is:

\[
0.4428.
\]

The critical region is:

\[
r>0.4428.
\]

### Step 4: Compare

The observed value is:

\[
r=0.219.
\]

Compare:

\[
0.219<0.4428.
\]

So \(r\) is not in the critical region.

### Step 5: Conclusion

Do not reject \(H_0\).

There is insufficient evidence at the \(10\%\) significance level to suggest positive correlation between English and Maths marks.

---

## Worked Example 6: Two-tailed correlation test

A scientist takes 30 observations of the masses of two reactants in an experiment.

She calculates:

\[
r=-0.45.
\]

The scientist believes there is no correlation between the masses of the two reactants.

Test the scientist’s claim at the \(10\%\) significance level.

### Step 1: State the hypotheses

The null hypothesis is:

\[
H_0:\rho=0.
\]

The alternative hypothesis is:

\[
H_1:\rho\ne0.
\]

This is a two-tailed test because we are testing for any correlation, positive or negative.

### Step 2: Sample size

\[
n=30.
\]

### Step 3: Significance level

The total significance level is:

\[
10\%.
\]

Because this is two-tailed, each tail uses:

\[
5\%.
\]

### Step 4: Critical value

The evidence gives the critical value at \(5\%\) significance for \(n=30\) as:

\[
0.3061.
\]

Because this is a two-tailed test, the critical regions are:

\[
r<-0.3061
\]

or

\[
r>0.3061.
\]

### Step 5: Compare

The observed value is:

\[
r=-0.45.
\]

Compare with the negative critical value:

\[
-0.45<-0.3061.
\]

So \(r\) lies in the critical region.

### Step 6: Conclusion

Reject \(H_0\).

There is evidence, at the \(10\%\) significance level, that there is correlation between the masses of the two reactants.

The scientist’s claim that there is no correlation is incorrect.

---

## Worked Example 7: Large data set gust and humidity

The table shows the daily maximum gust \(x\), in knots, and daily maximum relative humidity \(y\), as a percentage, in Leeming for a sample of eight days in May 2015.

| \(x\) | 31 | 28 | 38 | 37 | 18 | 17 | 21 | 29 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(y\) | 99 | 94 | 87 | 80 | 80 | 89 | 84 | 86 |

### Part (a)

Find the PMCC.

Using calculator regression mode:

\[
r=0.1149.
\]

### Part (b)

Test, at the \(10\%\) significance level, whether there is evidence of a positive correlation between daily maximum gust and daily maximum relative humidity.

#### Step 1: State the hypotheses

\[
H_0:\rho=0,
\]

\[
H_1:\rho>0.
\]

#### Step 2: Sample size

\[
n=8.
\]

#### Step 3: Critical value

For a one-tailed test at the \(10\%\) significance level, with \(n=8\), the critical value is:

\[
0.5067.
\]

The critical region is:

\[
r>0.5067.
\]

#### Step 4: Compare

\[
0.1149<0.5067.
\]

So \(r\) is not in the critical region.

#### Step 5: Conclusion

Do not reject \(H_0\).

There is insufficient evidence, at the \(10\%\) significance level, of a positive correlation between daily maximum gust and daily maximum relative humidity.

---

# Guided Practice

## Practice Question 1

A sample has:

\[
n=10,
\]

\[
r=0.219.
\]

The critical value for a one-tailed positive correlation test at the \(10\%\) significance level is:

\[
0.4428.
\]

Test whether there is evidence of positive correlation.

---

## Practice Question 2

A scientist records:

\[
r=-0.45
\]

from:

\[
n=30
\]

paired observations.

Test for any correlation at the \(10\%\) significance level, given that the \(5\%\) critical value is:

\[
0.3061.
\]

---

## Practice Question 3

The PMCC for a sample of eight days is:

\[
r=0.1149.
\]

The critical value for a positive correlation test at the \(10\%\) significance level is:

\[
0.5067.
\]

Test whether there is evidence of positive correlation.

---

## Practice Question 4

A model is given by:

\[
P=kb^t.
\]

The coded regression line is:

\[
y=2+0.3x,
\]

where:

\[
x=t
\]

and

\[
y=\log P.
\]

Find \(k\) and \(b\).

---

# Common Mistakes and Exam Traps

## Mistake 1: Thinking \(r\) is the gradient

The value of \(r\) does not tell you the gradient of the line.

For the model:

\[
y=a+bx,
\]

the gradient is:

\[
b.
\]

The PMCC \(r\) tells you how close the data are to a straight-line relationship, and whether that relationship is positive or negative.

## Mistake 2: Thinking \(r=-1\) means gradient \(-1\)

If:

\[
r=-1,
\]

the points lie perfectly on a straight line with negative gradient.

It does **not** mean the gradient is \(-1\).

## Mistake 3: Forgetting PMCC is only linear

A low value of \(r\) means weak or no linear correlation.

It does not rule out a curved relationship.

## Mistake 4: Using a positive critical value for a negative one-tailed test

If testing:

\[
H_1:\rho<0,
\]

use the negative critical value.

For example, if the table gives:

\[
0.4428,
\]

then the negative critical boundary is:

\[
-0.4428.
\]

## Mistake 5: Forgetting to split the significance level in a two-tailed test

If the total significance level is \(10\%\) and the test is two-tailed, use:

\[
5\%
\]

in each tail.

## Mistake 6: Writing a conclusion with no context

Do not stop at:

> Reject \(H_0\).

You must say what it means in the original context.

For example:

> There is evidence, at the \(10\%\) significance level, that the masses of the two reactants are correlated.

## Mistake 7: Confusing \(r\) and \(\rho\)

Use:

\[
r
\]

for the sample PMCC.

Use:

\[
\rho
\]

for the population PMCC.

Hypotheses should be written using \(\rho\), not \(r\):

\[
H_0:\rho=0.
\]

---

# Exam Technique

## 1. How to structure a correlation hypothesis test

Use this template:

\[
H_0:\rho=0
\]

Then choose one of:

\[
H_1:\rho>0,
\]

\[
H_1:\rho<0,
\]

\[
H_1:\rho\ne0.
\]

Then write:

- sample size \(n\);
- significance level;
- critical value;
- comparison;
- conclusion in context.

## 2. The two-mark conclusion

The evidence notes that the conclusion usually has two parts.

### Part 1: Compare and decide

Example:

\[
0.219<0.4428,
\]

so do not reject \(H_0\).

### Part 2: Put it in context

Example:

There is insufficient evidence to suggest positive correlation between English and Maths marks.

## 3. Extrapolation warning

If a question asks for a prediction outside the original data range, say:

> This is extrapolation and is unreliable because the trend may not continue outside the given range.

## 4. Model suitability wording

If \(r\) is close to \(1\) or \(-1\), write:

> The points lie close to a straight line, so a linear regression model is suitable.

If \(r\) is close to \(0\), write:

> There is weak/no linear correlation, so a linear regression model may not be suitable.

But be careful:

> A weak linear correlation does not prove there is no relationship; the relationship may be non-linear.

---

# Full Worked Solutions to Guided Practice

## Solution 1

Given:

\[
n=10,
\]

\[
r=0.219,
\]

critical value:

\[
0.4428.
\]

Hypotheses:

\[
H_0:\rho=0,
\]

\[
H_1:\rho>0.
\]

Compare:

\[
0.219<0.4428.
\]

So \(r\) is not in the critical region.

Therefore, do not reject \(H_0\).

There is insufficient evidence at the \(10\%\) significance level to suggest positive correlation.

---

## Solution 2

Given:

\[
n=30,
\]

\[
r=-0.45.
\]

This is a two-tailed test for any correlation.

Hypotheses:

\[
H_0:\rho=0,
\]

\[
H_1:\rho\ne0.
\]

The total significance level is \(10\%\), so use \(5\%\) in each tail.

Critical value:

\[
0.3061.
\]

Critical regions:

\[
r<-0.3061
\]

or

\[
r>0.3061.
\]

Compare:

\[
-0.45<-0.3061.
\]

So \(r\) lies in the critical region.

Therefore, reject \(H_0\).

There is evidence at the \(10\%\) significance level that the two variables are correlated.

---

## Solution 3

Given:

\[
r=0.1149,
\]

critical value:

\[
0.5067.
\]

Hypotheses:

\[
H_0:\rho=0,
\]

\[
H_1:\rho>0.
\]

Compare:

\[
0.1149<0.5067.
\]

So \(r\) is not in the critical region.

Therefore, do not reject \(H_0\).

There is insufficient evidence at the \(10\%\) significance level to suggest positive correlation.

---

## Solution 4

Given:

\[
P=kb^t,
\]

\[
x=t,
\]

\[
y=\log P,
\]

and:

\[
y=2+0.3x.
\]

Start with:

\[
P=kb^t.
\]

Take logs:

\[
\log P=\log(kb^t).
\]

Use the product law:

\[
\log P=\log k+\log(b^t).
\]

Use the power law:

\[
\log P=\log k+t\log b.
\]

Using \(x=t\) and \(y=\log P\):

\[
\log P=2+0.3t.
\]

Compare:

\[
\log P=\log k+t\log b
\]

with

\[
\log P=2+0.3t.
\]

Therefore:

\[
\log k=2
\]

and

\[
\log b=0.3.
\]

So:

\[
k=10^2=100,
\]

and:

\[
b=10^{0.3}=1.995\ldots.
\]

Therefore:

\[
\boxed{k=100,\quad b=2.00\text{ to 3 significant figures}.}
\]

---

# Companion Diagram Assets

The Mermaid and TikZ assets are supplementary build assets. They are listed in the manifest and source reference and can be used for printable notes, portal diagrams or alternate rendering formats.

---

# Syllabus Gap Check

| LO ID | Status in this lesson | Notes |
|---|---|---|
| A22-HT-LO001 | Covered | Hypothesis language, one-tailed/two-tailed tests, critical values and conclusions. |
| A22-HT-LO002 | Covered | Sample \(r\), population \(\rho\), significance and inference. |
| A22-HT-LO003 | Not covered | Needs separate binomial proportion hypothesis testing lesson. |
| A22-HT-LO004 | Not covered | Needs separate normal mean hypothesis testing lesson. |
| A22-HT-LO005 | Covered | Correlation coefficient interpreted using critical values. |

---

# Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A22StatisticalHypothesisTestingSVG-001 | SVG | Regression line \(y=20+3x\) on a scatter diagram. |
| A22StatisticalHypothesisTestingSVG-002 | SVG | Compare linear and exponential fits. |
| A22StatisticalHypothesisTestingSVG-003 | SVG | PMCC scale from \(-1\) to \(1\). |
| A22StatisticalHypothesisTestingSVG-004 | SVG | Correlation hypothesis test decision flowchart. |
| A22StatisticalHypothesisTestingSVG-005 | SVG | Two-tailed critical regions for \(r\). |
| A22StatisticalHypothesisTestingWIDGET-001 | Widget | Enter paired data and calculate/visualise \(r\). |
| A22StatisticalHypothesisTestingWIDGET-002 | Widget | Hypothesis test decision checker using \(r\), \(n\), tail and critical value. |

---

# Supplementary Sources Used

The lesson evidence includes a DrFrost/Pearson-style Year 2 Statistics chapter and transcript. This is not CCEA-branded evidence, so it has been controlled by the CCEA specification boundary.

Used as core support where it matches CCEA:

- PMCC interpretation.
- Hypothesis testing for correlation using critical values.
- Sample \(r\) versus population \(\rho\).
- One-tailed and two-tailed correlation tests.
- Model suitability and extrapolation warnings.

Used as prerequisite or enrichment only:

- Exponential regression.
- Polynomial/log-log modelling.
- Wider contextual modelling discussion.

Excluded from core:

- Logistic curve discussion.
- Spearman’s coefficient.
- Any cross-board-only practice not confirmed by the CCEA boundary.

---

# Final Student Checklist

Before moving on, you should be able to answer yes to each of these.

- I can explain what a regression line represents.
- I can explain why extrapolation is unreliable.
- I can derive

\[
y=kb^x
\quad\Rightarrow\quad
\log y=\log k+x\log b.
\]

- I know that PMCC \(r\) measures linear correlation only.
- I know that

\[
-1\le r\le 1.
\]

- I can interpret \(r=-1\), \(r=0\) and \(r=1\).
- I know that \(r\) is the sample PMCC and \(\rho\) is the population PMCC.
- I can write

\[
H_0:\rho=0.
\]

- I can choose between

\[
H_1:\rho>0,\quad H_1:\rho<0,\quad H_1:\rho\ne0.
\]

- I can compare \(r\) with a critical value.
- I can decide whether to reject \(H_0\).
- I can write a conclusion in context.
- I remember that “no significant linear correlation” does not automatically mean “no relationship”.
