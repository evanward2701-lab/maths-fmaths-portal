# FA22 Chi-Squared Tests

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | FA22-CHI2 |
| Topic name | \(\chi^2\) tests |
| Topic slug | chi_squared_tests |
| Topic Pascal | ChiSquaredTests |
| Topic ID | FA22ChiSquaredTests |
| Lesson file | FA22_chi_squared_tests_lesson.md |
| Core LO IDs | FA22-CHI2-LO001; FA22-CHI2-LO002; FA22-CHI2-LO003 |
| Bridge tags | A22 Hypothesis Testing; AS2 Data Presentation; AS2 Probability; A22 Normal Distribution; Binomial Distribution; Poisson Distribution |
| Topic tags | Statistics; Chi-Squared; Goodness of Fit; Independence; Contingency Tables; Degrees of Freedom; Hypothesis Testing |

This lesson teaches how to use \(\chi^2\) tests to decide whether observed frequency data are consistent with an expected model. There are two main CCEA FA22 uses: goodness-of-fit tests, and independence tests in contingency tables.

The central statistic is

\[
\chi^2=\sum \frac{(O_i-E_i)^2}{E_i},
\]

where \(O_i\) is an observed frequency and \(E_i\) is the corresponding expected frequency. A large value of \(\chi^2\) means the observed data are far from the expected data. A small value means the observed data are close to the expected data.

## 2. Evidence Map

| Source | Used for | Status |
|---|---|---|
| CCEA GCE Further Mathematics Specification Map | Topic identity, LO IDs, official wording, boundaries, elaboration notes | Primary authority |
| Further Maths README module map | Unit/topic placement and bridge mapping | Project source |
| Further Maths evidence checklist | Evidence and asset planning discipline | Project source |
| `FS1-Chp6-ChiSquaredTests.pdf` | Model definition, goodness-of-fit statistic, alternative statistic, degrees of freedom, full test examples, binomial/Poisson/geometric model tests, contingency tables | Cross-board evidence used only where CCEA confirms the topic is on-spec |
| `transcripts.md` | Teacher explanation, motivation, warnings, notation, derivations, constraints, parameter estimation and conclusions | Cross-board transcript evidence used where mathematically aligned with CCEA |
| `Chapter_6_Chi-Squared_Tests_📊_(Further_Statistics_1)_screenshots.pdf` | Visual layout, die example table, handwritten annotations, calculator-screen evidence, table structure | Visual evidence only; no parsed text available |
| Ordinary A-Level Maths bridge extracts | Probability, data presentation, binomial distribution, normal distribution, hypothesis testing | Bridge context only |

The screenshot PDF has no parsed text, so only visible/readable visual details are used. No uninspected visual detail is claimed.

## 3. Specification Alignment

| LO ID | Official CCEA wording | Lesson coverage | Syllabus boundary | Bridge |
|---|---|---|---|---|
| FA22-CHI2-LO001 | fit a theoretical distribution, as prescribed by a given hypothesis, to given data | Expected frequencies from a theoretical model; \(E_i=Np_i\); prescribed distributions; parameter estimation where required; model assumptions; context conclusions | Questions set will not involve lengthy calculations. | Probability, binomial distribution, Poisson-style modelling, hypothesis testing |
| FA22-CHI2-LO002 | use a \(\chi^2\) test with the appropriate number of degrees of freedom to carry out the corresponding goodness of fit test | \(\chi^2\) statistic; alternative form; upper-tail test; critical value; degrees of freedom; combining expected frequencies; goodness-of-fit examples | Combine classes so each expected frequency is at least 5. Use formula-booklet \(\chi^2\) percentage points. | A22 hypothesis testing, normal distribution and significance levels |
| FA22-CHI2-LO003 | use a \(\chi^2\) test with the appropriate number of degrees of freedom to test for independence in a contingency table | Contingency-table expected frequencies; row/column totals; \((r-1)(c-1)\); independence hypotheses; Yates’ correction for \(2\times2\) tables | Combine rows/columns where required so expected frequencies are at least 5. Use Yates’ correction in \(2\times2\). | Data presentation, independence, conditional probability, hypothesis testing |

CCEA elaboration requires that classes, rows or columns are combined so each expected frequency is at least \(5\), and that Yates’ correction is used for \(2\times2\) contingency tables.

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to:

1. define observed frequencies \(O_i\) and expected frequencies \(E_i\);
2. calculate expected frequencies using \(E_i=Np_i\);
3. calculate a goodness-of-fit statistic using \(\chi^2=\sum\frac{(O_i-E_i)^2}{E_i}\);
4. use the alternative form \(\chi^2=\sum\frac{O_i^2}{E_i}-N\);
5. explain why the statistic uses squaring and division by \(E_i\);
6. choose the correct degrees of freedom;
7. reduce degrees of freedom when a parameter has been estimated from the data;
8. combine classes so that each expected frequency is at least \(5\);
9. find and use a \(\chi^2\) critical value;
10. carry out a \(\chi^2\) goodness-of-fit test;
11. calculate expected frequencies in a contingency table;
12. carry out a \(\chi^2\) test for independence;
13. apply Yates’ correction in a \(2\times2\) contingency table.

### Bridge objectives

You should connect this lesson to ordinary A-Level Maths by remembering hypothesis-testing language, probability models, data tables, independence and normal-distribution standardisation.

## 5. Explicit Prerequisite Recap

### GCSE foundations

You should already be comfortable with frequency tables, totals and percentages, probability, mean from a frequency table, squaring numbers, substitution into formulae and comparing a value with a threshold.

### Ordinary AS/A2 Mathematics foundations

You should already know probability rules, independent events, binomial distribution notation, normal distribution standardisation, hypothesis testing language, significance levels, critical regions and contextual conclusions.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Probability | Probabilities of events, including independent and conditional events. | Probabilities become expected frequencies: \(E_i=Np_i\). | Do not leave answers as probabilities when the test requires expected frequencies. |
| AS2 Data Presentation | Tables, totals and grouped frequency information. | Tables become testing structures; totals create constraints and affect degrees of freedom. | A row total or column total is not decoration. It controls what can vary. |
| AS2/A22 Binomial Distribution | \(X\sim \mathrm{Bin}(n,p)\). | A binomial model can be tested against observed data. | If \(p\) is estimated from data, reduce the degrees of freedom by one more. |
| A22 Normal Distribution | Standardisation and tail probabilities. | \(\chi^2\) can be understood as a sum of squared standardised deviations. | The \(\chi^2\) test looks only in the upper tail. |
| A22 Hypothesis Testing | \(H_0\), \(H_1\), significance level, critical value and conclusion. | Hypotheses describe model fit or independence, not just a single parameter. | Do not write vague conclusions such as “the data is accepted”. |

In ordinary A-Level Maths, this idea appeared as hypothesis testing with a known distribution or parameter. In Further Maths, the same idea becomes a test of whether a whole frequency table behaves as expected. The key upgrade is that you are no longer checking one sample statistic. You are checking many frequency cells at once. The danger is that old habits from binomial or normal tests can make you look for the wrong tail. In a \(\chi^2\) test, the rejection region is in the upper tail.

## 6. Big Picture Explanation

Suppose you roll a fair die \(120\) times. If the die is fair, you expect the six outcomes \(1,2,3,4,5,6\) to appear equally often, so the expected frequency for each face is

\[
\frac{120}{6}=20.
\]

But real data almost never gives exactly \(20,20,20,20,20,20\). The question is: is the variation small enough to be ordinary random variation, or large enough to suggest the model is wrong?

A model is a simplified mathematical representation of a situation. It lets us calculate expected frequencies. Then \(\chi^2\) measures how far the observed frequencies are from those expected frequencies.

If we calculate raw differences \(O_i-E_i\), positive and negative differences can cancel. For the die example from the visual evidence, the observed frequencies are \(26,27,28,21,10,8\), the expected frequencies are \(20\) each, and

\[
O_i-E_i=6,7,8,1,-10,-12.
\]

Adding gives

\[
6+7+8+1-10-12=0.
\]

That total of \(0\) is misleading because the observed frequencies are not perfectly equal to the expected frequencies. So \(\chi^2\) uses squared differences and divides by \(E_i\) to standardise the difference:

\[
\frac{(O_i-E_i)^2}{E_i}.
\]

Watch for five recurring traps: goodness-of-fit versus independence, expected frequencies below \(5\), estimated parameters, \(2\times2\) Yates’ correction, and context in the final conclusion.

## 7. Key Definitions and Notation

### Observed frequency

\[
O_i
\]

is the frequency actually recorded in category \(i\).

### Expected frequency

\[
E_i
\]

is the frequency predicted by the null hypothesis or model. If the model gives probability \(p_i\) and the total frequency is \(N\), then

\[
E_i=Np_i.
\]

### Total frequency

\[
N=\sum O_i=\sum E_i.
\]

### Test statistic

\[
\chi^2=\sum \frac{(O_i-E_i)^2}{E_i}.
\]

### Alternative form

\[
\chi^2=\sum \frac{O_i^2}{E_i}-N.
\]

### Degrees of freedom

Degrees of freedom are denoted by \(\nu\), the Greek letter nu.

For goodness of fit:

\[
\nu=\text{number of classes after combining}-\text{number of constraints}.
\]

Usually \(\nu=k-1\). If one parameter is estimated, \(\nu=k-2\).

### Contingency-table expected frequency

For a cell in row \(i\) and column \(j\),

\[
E_{ij}=\frac{(\text{row total})(\text{column total})}{\text{grand total}}.
\]

### Contingency-table degrees of freedom

For an \(r\times c\) table,

\[
\nu=(r-1)(c-1).
\]

### Yates’ correction

For a \(2\times2\) contingency table, CCEA requires

\[
\chi^2=\sum \frac{(|O-E|-0.5)^2}{E}.
\]

## 8. Core Theory

### 8.1 From probabilities to expected frequencies

If a model predicts probabilities \(p_1,p_2,\ldots,p_k\), and the total frequency is \(N\), then

\[
E_i=Np_i.
\]

For a fair die rolled \(120\) times,

\[
E_i=120\times \frac16=20.
\]

**Bridge Note:** In ordinary A-Level Maths, probabilities such as \(\frac16\) were often final answers. Here, probabilities become expected frequencies.

### 8.2 Why raw differences are not enough

For observed frequencies \(26,27,28,21,10,8\) and expected frequencies \(20,20,20,20,20,20\), the raw differences are

\[
6,7,8,1,-10,-12.
\]

Their sum is

\[
6+7+8+1-10-12=0.
\]

This cancellation is why we square:

\[
(O_i-E_i)^2.
\]

The squared differences are

\[
36,49,64,1,100,144.
\]

**Bridge Note:** This echoes variance, where deviations from the mean are squared to avoid cancellation.

### 8.3 Why divide by expected frequency?

The contribution

\[
\frac{(O_i-E_i)^2}{E_i}
\]

standardises the squared difference. A difference of \(10\) is much more serious when \(E_i=20\) than when \(E_i=1000\).

### 8.4 Goodness-of-fit statistic for the die example

| Outcome | \(O_i\) | \(E_i\) | \(O_i-E_i\) | \((O_i-E_i)^2\) | \(\frac{(O_i-E_i)^2}{E_i}\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 26 | 20 | 6 | 36 | \(\frac{36}{20}\) |
| 2 | 27 | 20 | 7 | 49 | \(\frac{49}{20}\) |
| 3 | 28 | 20 | 8 | 64 | \(\frac{64}{20}\) |
| 4 | 21 | 20 | 1 | 1 | \(\frac{1}{20}\) |
| 5 | 10 | 20 | \(-10\) | 100 | \(\frac{100}{20}\) |
| 6 | 8 | 20 | \(-12\) | 144 | \(\frac{144}{20}\) |

Therefore

\[
\chi^2=\frac{36+49+64+1+100+144}{20}=\frac{394}{20}=19.7.
\]

A value of \(0\) would mean perfect match. A larger value means a worse fit.

### 8.5 Alternative form derivation

Start with

\[
\chi^2=\sum \frac{(O_i-E_i)^2}{E_i}.
\]

Expand:

\[
(O_i-E_i)^2=O_i^2-2O_iE_i+E_i^2.
\]

Then

\[
\chi^2=\sum\left(\frac{O_i^2}{E_i}-2O_i+E_i\right).
\]

So

\[
\chi^2=\sum\frac{O_i^2}{E_i}-2\sum O_i+\sum E_i.
\]

Since

\[
\sum O_i=N,\qquad \sum E_i=N,
\]

we get

\[
\chi^2=\sum\frac{O_i^2}{E_i}-N.
\]

For the die example,

\[
\chi^2=\frac{26^2}{20}+\frac{27^2}{20}+\frac{28^2}{20}+\frac{21^2}{20}+\frac{10^2}{20}+\frac{8^2}{20}-120=19.7.
\]

### 8.6 The \(\chi^2\) distribution

The \(\chi^2\) distribution is right-skewed and non-negative. A goodness-of-fit test is an upper-tail test because unusually large deviations from expectation are evidence against the model.

### 8.7 Degrees of freedom

If a die is rolled \(120\) times, there are six frequency cells. But once five counts are known, the sixth is fixed by the total. Therefore

\[
\nu=6-1=5.
\]

In general:

\[
\nu=k-1
\]

when no parameter is estimated, and

\[
\nu=k-2
\]

when one parameter is estimated.

### 8.8 Combining classes

CCEA requires every expected frequency used in the final test to be at least \(5\). If any \(E_i<5\), combine adjacent or sensible classes before calculating \(\chi^2\).

Correct order:

1. calculate expected frequencies;
2. identify expected frequencies below \(5\);
3. combine classes;
4. recalculate combined observed and expected frequencies;
5. calculate \(\chi^2\).

### 8.9 General method for goodness of fit

1. State \(H_0\) and \(H_1\).
2. Set the significance level.
3. Calculate expected frequencies.
4. Combine classes if any expected frequency is less than \(5\).
5. Calculate degrees of freedom.
6. Find the critical value from the \(\chi^2\) table.
7. Calculate the test statistic.
8. Compare statistic and critical value.
9. Write a conclusion in context.

If

\[
\chi^2_{\text{calc}}>\chi^2_{\text{crit}},
\]

reject \(H_0\). Otherwise, do not reject \(H_0\).

### 8.10 Full fair-die test

Observed frequencies:

| Outcome | 1 | 2 | 3 | 4 | 5 | 6 | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Observed | 23 | 15 | 25 | 18 | 21 | 18 | 120 |
| Expected | 20 | 20 | 20 | 20 | 20 | 20 | 120 |

Hypotheses:

\[
H_0:\text{ the observed distribution can be modelled by a discrete uniform distribution.}
\]

\[
H_1:\text{ the observed distribution cannot be modelled by a discrete uniform distribution.}
\]

Contributions:

\[
\frac{(23-20)^2}{20}=0.45,
\]

\[
\frac{(15-20)^2}{20}=1.25,
\]

\[
\frac{(25-20)^2}{20}=1.25,
\]

\[
\frac{(18-20)^2}{20}=0.2,
\]

\[
\frac{(21-20)^2}{20}=0.05,
\]

\[
\frac{(18-20)^2}{20}=0.2.
\]

So

\[
\chi^2=0.45+1.25+1.25+0.2+0.05+0.2=3.4.
\]

There are six classes, no parameter estimated, so

\[
\nu=6-1=5.
\]

At the \(5\%\) level,

\[
\chi^2_5(5\%)=11.070.
\]

Since

\[
3.4<11.070,
\]

we do not reject \(H_0\). There is insufficient evidence to suggest that the die is biased.

### 8.11 Binomial model testing

If \(X\sim\mathrm{Bin}(n,p)\), then

\[
\Pr(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
\]

and

\[
E_x=N\Pr(X=x).
\]

If \(p\) is given, no parameter is estimated and \(\nu=k-1\). If \(p\) is estimated from data, use

\[
\hat p=\frac{\sum rf}{Nn}
\]

and \(\nu=k-2\).

### 8.12 Poisson model testing

If \(X\sim\mathrm{Po}(\lambda)\), then

\[
\Pr(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}
\]

and

\[
E_x=N\Pr(X=x).
\]

If \(\lambda\) is estimated from data, use

\[
\hat\lambda=\frac{\sum rf}{N}
\]

and lose one additional degree of freedom.

### 8.13 Contingency tables and independence

A contingency table classifies observations by two categorical variables. The hypotheses are usually:

\[
H_0:\text{ the variables are independent.}
\]

\[
H_1:\text{ the variables are not independent.}
\]

Expected frequency:

\[
E=\frac{(\text{row total})(\text{column total})}{\text{grand total}}.
\]

Degrees of freedom:

\[
\nu=(r-1)(c-1).
\]

For a \(2\times2\) table, use Yates’ correction:

\[
\chi^2=\sum\frac{(|O-E|-0.5)^2}{E}.
\]

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsMermaid-001 | Source: CCEA FA22-CHI2 specification + Dr Frost goodness-of-fit workflow evidence | Insert from mermaid/FA22ChiSquaredTestsMermaid-001.md | Purpose: Show the complete goodness-of-fit decision chain from model choice to final conclusion.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsMermaid-002 | Source: CCEA FA22-CHI2 specification + contingency table evidence | Insert from mermaid/FA22ChiSquaredTestsMermaid-002.md | Purpose: Show the contingency-table independence test workflow, including the Yates correction branch for \(2\times2\) tables.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsSVG-001 | Source: Screenshot PDF visible die example + teacher transcript | Insert from svg/FA22ChiSquaredTestsSVG-001.svg | Purpose: Rebuild the die observed/expected goodness-of-fit table with all visible rows and handwritten-style annotations.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsSVG-002 | Source: Dr Frost hypothesis testing slide + CCEA \(\chi^2\) table requirement | Insert from svg/FA22ChiSquaredTestsSVG-002.svg | Purpose: Show a right-skewed \(\chi^2\) distribution with upper-tail critical region.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsSVG-003 | Source: Dr Frost “Testing a Model” visual evidence | Insert from svg/FA22ChiSquaredTestsSVG-003.svg | Purpose: Show the modelling pipeline: data, simplifying assumptions, model, prediction.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA FA22-CHI2 specification | Insert from svg/FA22ChiSquaredTestsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsTikZ-001 | Source: CCEA FA22-CHI2 specification + Dr Frost \(\chi^2\) distribution evidence | Insert from tikz/FA22ChiSquaredTestsTikZ-001.tex | Purpose: Produce a precise mathematical sketch of a \(\chi^2\) distribution with the upper-tail critical region.]

[VISUAL PLACEHOLDER: FA22ChiSquaredTestsTikZ-002 | Source: CCEA FA22-CHI2 specification + contingency table evidence | Insert from tikz/FA22ChiSquaredTestsTikZ-002.tex | Purpose: Show the structure of a contingency table and the expected-frequency formula.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22ChiSquaredTestsWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FA22-CHI2 + goodness-of-fit lesson evidence | Insert from widgets/FA22ChiSquaredTestsWidget-001.html | Purpose: Let the student enter observed and expected frequencies, then calculate \(\chi^2\) step by step.]

[INTERACTIVE PLACEHOLDER: FA22ChiSquaredTestsWidget-002 | Source: AI-proposed teaching enhancement based on CCEA FA22-CHI2 + transcript evidence on constraints | Insert from widgets/FA22ChiSquaredTestsWidget-002.html | Purpose: Help the student calculate degrees of freedom from classes, constraints and estimated parameters.]

[INTERACTIVE PLACEHOLDER: FA22ChiSquaredTestsWidget-003 | Source: AI-proposed teaching enhancement based on CCEA FA22-CHI2 contingency-table requirements | Insert from widgets/FA22ChiSquaredTestsWidget-003.html | Purpose: Let the student enter a contingency table and calculate expected frequencies, degrees of freedom, and the appropriate \(\chi^2\) statistic.]

## 11. Worked Examples

### Worked Example 1: Goodness-of-fit statistic for a die

A die is rolled \(120\) times. Observed frequencies are:

| Outcome | 1 | 2 | 3 | 4 | 5 | 6 | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Observed | 26 | 27 | 28 | 21 | 10 | 8 | 120 |
| Expected | 20 | 20 | 20 | 20 | 20 | 20 | 120 |

Calculate:

\[
\chi^2=\frac{(26-20)^2}{20}+\frac{(27-20)^2}{20}+\frac{(28-20)^2}{20}+\frac{(21-20)^2}{20}+\frac{(10-20)^2}{20}+\frac{(8-20)^2}{20}.
\]

\[
\chi^2=\frac{36}{20}+\frac{49}{20}+\frac{64}{20}+\frac{1}{20}+\frac{100}{20}+\frac{144}{20}.
\]

\[
\chi^2=\frac{394}{20}=19.7.
\]

Final answer:

\[
\boxed{\chi^2=19.7}
\]

### Worked Example 2: Billy and Mel’s spinners

Observed and expected frequencies:

| Sum | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Observed by Billy | 12 | 15 | 22 | 41 | 33 | 21 | 16 |
| Observed by Mel | 6 | 12 | 21 | 37 | 35 | 29 | 20 |
| Expected | 10 | 20 | 30 | 40 | 30 | 20 | 10 |

Hypotheses:

\[
H_0:\text{ the observed distribution is the same as the theoretical distribution.}
\]

\[
H_1:\text{ the observed distribution is different from the theoretical distribution.}
\]

For Billy:

\[
\chi^2_{\text{Billy}}=\frac{12^2}{10}+\frac{15^2}{20}+\frac{22^2}{30}+\frac{41^2}{40}+\frac{33^2}{30}+\frac{21^2}{20}+\frac{16^2}{10}-160.
\]

\[
\chi^2_{\text{Billy}}\approx 7.758.
\]

For Mel:

\[
\chi^2_{\text{Mel}}=\frac{6^2}{10}+\frac{12^2}{20}+\frac{21^2}{30}+\frac{37^2}{40}+\frac{35^2}{30}+\frac{29^2}{20}+\frac{20^2}{10}-160.
\]

\[
\chi^2_{\text{Mel}}\approx 22.608.
\]

Mel’s goodness of fit is higher, so she is more likely to have the biased spinner.

### Worked Example 3: Expected frequencies from probabilities

A \(3\)-sided spinner has probabilities \(0.3,0.2,0.5\) and is spun \(20\) times. Observed frequencies are \(4,7,9\).

Expected frequencies:

\[
20(0.3)=6,
\]

\[
20(0.2)=4,
\]

\[
20(0.5)=10.
\]

Then

\[
\chi^2=\frac{(4-6)^2}{6}+\frac{(7-4)^2}{4}+\frac{(9-10)^2}{10}.
\]

\[
\chi^2=\frac{4}{6}+\frac{9}{4}+\frac{1}{10}=3.0166\ldots.
\]

\[
\boxed{\chi^2=3.02}
\]

### Worked Example 4: Full goodness-of-fit test for fair die

Observed frequencies are \(23,15,25,18,21,18\), expected frequencies are all \(20\), and \(N=120\).

\[
\chi^2=0.45+1.25+1.25+0.2+0.05+0.2=3.4.
\]

Degrees of freedom:

\[
\nu=6-1=5.
\]

Critical value at \(5\%\):

\[
\chi^2_5(5\%)=11.070.
\]

Since

\[
3.4<11.070,
\]

do not reject \(H_0\). There is insufficient evidence to suggest that the die is biased.

### Worked Example 5: Binomial model with \(p\) given

Let \(X\sim\mathrm{Bin}(10,0.2)\), \(N=100\), and observed frequencies for \(x=0,1,2,3,4,5,6,7,8\) be \(12,28,28,17,7,4,2,2,0\).

Expected frequencies from the supplied probabilities are approximately \(10.74,26.84,30.20,20.13,8.81,2.64,0.55,0.08,0.01\). Combine the upper tail into \(x\geq4\):

| Class | 0 | 1 | 2 | 3 | \(\geq4\) |
|---:|---:|---:|---:|---:|---:|
| Observed | 12 | 28 | 28 | 17 | 15 |
| Expected | 10.74 | 26.84 | 30.20 | 20.13 | 12.09 |

\[
\chi^2=1.5453.
\]

There are five classes and no estimated parameter:

\[
\nu=5-1=4.
\]

Since

\[
1.5453<9.488,
\]

do not reject \(H_0\). \(\mathrm{Bin}(10,0.2)\) is a possible model.

### Worked Example 6: Binomial model with \(p\) estimated

For number of girls in \(100\) families with five children:

| Number of girls \(r\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|---:|
| Frequency \(f\) | 13 | 18 | 38 | 20 | 10 | 1 |

Estimate:

\[
\hat p=\frac{\sum rf}{Nn}=\frac{199}{100\times5}=0.398.
\]

After combining \(4\) and \(5\) into \(>3\), the table is:

| Class | 0 | 1 | 2 | 3 | \(>3\) |
|---:|---:|---:|---:|---:|---:|
| Observed | 13 | 18 | 38 | 20 | 11 |
| Expected | 7.91 | 26.14 | 34.56 | 22.85 | 8.54 |

Using \(\chi^2=\sum\frac{O^2}{E}-N\):

\[
\chi^2=107.22-100=7.22.
\]

There are five classes and one estimated parameter:

\[
\nu=5-2=3.
\]

Critical value:

\[
\chi^2_3(5\%)=7.815.
\]

Since

\[
7.22<7.815,
\]

do not reject \(H_0\). There is insufficient evidence to suggest that a binomial model is unsuitable.

### Worked Example 7: Poisson model with \(\lambda\) estimated

Observed frequencies for telephone calls in six-minute periods:

| Calls \(r\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Frequency \(f\) | 8 | 19 | 26 | 13 | 7 | 5 | 1 | 1 | 0 |

\[
N=80,
\]

\[
\hat\lambda=\frac{\sum rf}{N}=\frac{176}{80}=2.2.
\]

After combining the upper tail:

| Class | 0 | 1 | 2 | 3 | 4 | \(\geq5\) |
|---:|---:|---:|---:|---:|---:|---:|
| Observed | 8 | 19 | 26 | 13 | 7 | 7 |
| Expected | 8.864 | 19.504 | 21.448 | 15.728 | 8.656 | 5.800 |

\[
\chi^2=2.1016.
\]

There are six classes and one estimated parameter:

\[
\nu=6-2=4.
\]

Critical value:

\[
\chi^2_4(5\%)=9.488.
\]

Since

\[
2.1016<9.488,
\]

do not reject \(H_0\). The number of calls may be modelled by a Poisson distribution.

### Worked Example 8: Contingency-table independence test

Observed table:

|  | Grade A | Grade B | Grade C | Total |
|---|---:|---:|---:|---:|
| School X | 18 | 12 | 20 | 50 |
| School Y | 26 | 12 | 32 | 70 |
| Total | 44 | 24 | 52 | 120 |

Hypotheses:

\[
H_0:\text{ school and grade are independent.}
\]

\[
H_1:\text{ school and grade are not independent.}
\]

Expected frequency for School X and Grade A:

\[
E=\frac{50\times44}{120}=18.33\ldots.
\]

The full expected table is approximately:

|  | Grade A | Grade B | Grade C | Total |
|---|---:|---:|---:|---:|
| School X | 18.33 | 10.00 | 21.67 | 50 |
| School Y | 25.67 | 14.00 | 30.33 | 70 |
| Total | 44 | 24 | 52 | 120 |

The evidence records

\[
\sum\frac{O^2}{E}=120.916.
\]

So

\[
\chi^2=120.916-120=0.916.
\]

This is a \(2\times3\) table, so

\[
\nu=(2-1)(3-1)=2.
\]

Critical value:

\[
\chi^2_2(5\%)=5.991.
\]

Since

\[
0.916<5.991,
\]

do not reject \(H_0\). There is insufficient evidence to suggest an association between school and grade.

### Worked Example 9: Generated \(2\times2\) Yates example

Observed table:

|  | Improved sleep | No improved sleep | Total |
|---|---:|---:|---:|
| Took supplement | 18 | 12 | 30 |
| Did not take supplement | 20 | 30 | 50 |
| Total | 38 | 42 | 80 |

Expected frequencies:

\[
E_{11}=\frac{30\times38}{80}=14.25,
\]

\[
E_{12}=\frac{30\times42}{80}=15.75,
\]

\[
E_{21}=\frac{50\times38}{80}=23.75,
\]

\[
E_{22}=\frac{50\times42}{80}=26.25.
\]

Because this is \(2\times2\), use Yates:

\[
\chi^2=\sum\frac{(|O-E|-0.5)^2}{E}.
\]

The four absolute differences are all \(3.75\), so \(|O-E|-0.5=3.25\). Contributions:

\[
\frac{3.25^2}{14.25}=0.7412\ldots,
\]

\[
\frac{3.25^2}{15.75}=0.6706\ldots,
\]

\[
\frac{3.25^2}{23.75}=0.4447\ldots,
\]

\[
\frac{3.25^2}{26.25}=0.4024\ldots.
\]

\[
\chi^2\approx2.259.
\]

\[
\nu=(2-1)(2-1)=1.
\]

Since \(2.259<3.841\), do not reject \(H_0\). There is insufficient evidence to suggest an association between taking the supplement and reporting improved sleep.

## 12. Common Mistakes and Exam Traps

1. Saying \(x^2\) instead of \(\chi^2\). The statistic is chi-squared.
2. Averaging \(O-E\), which can cancel to zero.
3. Forgetting to divide by \(E\).
4. Comparing observed frequencies with probabilities instead of expected frequencies.
5. Forgetting to combine expected frequencies below \(5\).
6. Combining observed classes but not expected classes.
7. Using the original number of classes instead of the number after combining.
8. Forgetting that parameter estimation loses a degree of freedom.
9. Putting the critical region in the lower tail.
10. Saying “accept \(H_0\)” too strongly.
11. Writing vague hypotheses.
12. Giving a goodness-of-fit conclusion for a contingency table.
13. Forgetting Yates’ correction for a \(2\times2\) contingency table.
14. Applying Yates’ correction where it is not required.
15. Rounding expected frequencies too early.
16. Writing a numerical parameter in \(H_0\) when it was estimated from the data.

## 13. Practice Questions

### Question 1

A spinner has probabilities \(0.2,0.3,0.5\) for outcomes \(1,2,3\). It is used \(100\) times and observed frequencies are \(18,36,46\). Calculate expected frequencies and \(X^2\).

### Question 2

A goodness-of-fit test has expected frequencies \(24,30,20,10,4,2\). Explain why classes must be combined. State suitable combined classes and give degrees of freedom with no parameter estimated and with one parameter estimated.

### Question 3

Explain why \(\chi^2\) tests use expected frequencies, why the critical region is upper-tail, and why a small \(X^2\) is not evidence against \(H_0\).

### Question 4

A four-sided spinner is spun \(80\) times. Observed frequencies are \(15,23,18,24\). Test at the \(5\%\) level whether the spinner may be regarded as fair. Use \(\chi^2_3(5\%)=7.815\).

### Question 5

The number of errors on a page is thought to follow \(\mathrm{Po}(1.5)\). Observed frequencies for \(0,1,2,3,\ge4\) errors are \(20,36,23,15,6\). Probabilities are \(0.2231,0.3347,0.2510,0.1255,0.0657\). Test at \(5\%\). Use \(\chi^2_4(5\%)=9.488\).

### Question 6

A contingency table records revision method by year group:

|  | Flashcards | Videos | Practice papers | Total |
|---|---:|---:|---:|---:|
| Year 13 | 20 | 15 | 15 | 50 |
| Year 14 | 10 | 25 | 15 | 50 |
| Total | 30 | 40 | 30 | 100 |

Test at \(5\%\) whether year group and revision method are independent. Use \(\chi^2_2(5\%)=5.991\).

### Question 7

A factory checks batches of \(4\) items. In \(50\) batches, defective counts are:

| Defective \(r\) | 0 | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|
| Frequency \(f\) | 5 | 12 | 20 | 10 | 3 |

Estimate \(p\), combine expected classes where needed, and test whether a binomial model is suitable. Expected frequencies for \(\mathrm{Bin}(4,\hat p)\) are \(3.945,13.994,18.619,11.005,2.440\). Use \(\chi^2_1(5\%)=3.841\).

### Question 8

A \(2\times2\) table records training and pass result:

|  | Passed | Did not pass | Total |
|---|---:|---:|---:|
| Completed training | 28 | 12 | 40 |
| Did not complete training | 18 | 22 | 40 |
| Total | 46 | 34 | 80 |

Use Yates’ correction at \(5\%\) to test for association. Use \(\chi^2_1(5\%)=3.841\).

## 14. Worked Solutions

### Solution 1

Expected frequencies:

\[
100(0.2)=20,
\]

\[
100(0.3)=30,
\]

\[
100(0.5)=50.
\]

\[
X^2=\frac{(18-20)^2}{20}+\frac{(36-30)^2}{30}+\frac{(46-50)^2}{50}
\]

\[
=0.2+1.2+0.32=1.72.
\]

### Solution 2

Since \(4<5\) and \(2<5\), combine classes \(4\) and \(5\) to get expected frequency \(6\). Final classes: \(0,1,2,3,4\text{ or }5\), so \(k=5\). With no estimated parameter, \(\nu=5-1=4\). With one estimated parameter, \(\nu=5-2=3\).

### Solution 3

\(\chi^2\) tests use expected frequencies because observed data are counts. Probabilities are converted using \(E_i=Np_i\). The critical region is upper-tail because large \(X^2\) means large total deviation from expectation. A small \(X^2\) means observed frequencies are close to expected, so it is not evidence against \(H_0\).

### Solution 4

Expected frequencies are \(20,20,20,20\). Then

\[
X^2=\frac{(15-20)^2}{20}+\frac{(23-20)^2}{20}+\frac{(18-20)^2}{20}+\frac{(24-20)^2}{20}
\]

\[
=1.25+0.45+0.20+0.80=2.70.
\]

\(\nu=4-1=3\). Since \(2.70<7.815\), do not reject \(H_0\). There is insufficient evidence to suggest that the spinner is not fair.

### Solution 5

Expected frequencies are \(22.31,33.47,25.10,12.55,6.57\). All are at least \(5\). Then

\[
X^2\approx 1.134.
\]

There are five classes and \(\lambda=1.5\) was given, so \(\nu=5-1=4\). Since \(1.134<9.488\), do not reject \(H_0\). There is insufficient evidence to suggest that \(\mathrm{Po}(1.5)\) is unsuitable.

### Solution 6

Expected table:

|  | Flashcards | Videos | Practice papers | Total |
|---|---:|---:|---:|---:|
| Year 13 | 15 | 20 | 15 | 50 |
| Year 14 | 15 | 20 | 15 | 50 |
| Total | 30 | 40 | 30 | 100 |

\[
X^2=\frac{(20-15)^2}{15}+\frac{(15-20)^2}{20}+0+\frac{(10-15)^2}{15}+\frac{(25-20)^2}{20}+0=5.833\ldots.
\]

\(\nu=(2-1)(3-1)=2\). Since \(5.833<5.991\), do not reject \(H_0\). There is insufficient evidence to suggest an association between year group and preferred revision method.

### Solution 7

\[
N=50,
\]

\[
\sum rf=0(5)+1(12)+2(20)+3(10)+4(3)=94.
\]

\[
\hat p=\frac{94}{50\times4}=0.47.
\]

Combine \(0\) and \(1\), and combine \(3\) and \(4\):

| Class | 0 or 1 | 2 | 3 or 4 |
|---:|---:|---:|---:|
| Observed | 17 | 20 | 13 |
| Expected | 17.939 | 18.619 | 13.445 |

\[
X^2\approx0.166.
\]

There are three classes and \(p\) was estimated, so \(\nu=3-2=1\). Since \(0.166<3.841\), do not reject \(H_0\). There is insufficient evidence to suggest that a binomial model is unsuitable.

### Solution 8

Expected frequencies:

\[
E_{11}=\frac{40\times46}{80}=23,
\]

\[
E_{12}=\frac{40\times34}{80}=17,
\]

\[
E_{21}=23,
\]

\[
E_{22}=17.
\]

Use Yates’ correction because the table is \(2\times2\):

\[
X^2=\sum\frac{(|O-E|-0.5)^2}{E}.
\]

All absolute differences are \(5\), so the corrected difference is \(4.5\). Therefore

\[
X^2=\frac{4.5^2}{23}+\frac{4.5^2}{17}+\frac{4.5^2}{23}+\frac{4.5^2}{17}=4.143\ldots.
\]

\(\nu=1\). Since \(4.143>3.841\), reject \(H_0\). There is sufficient evidence to suggest an association between completing the training and passing the skills test.

## 15. Exam Technique Notes

| Question type | What you are testing | Expected-frequency method | Degrees of freedom |
|---|---|---|---|
| Goodness of fit to a given distribution | Does observed distribution fit the specified model? | \(E_i=Np_i\) | \(k-1\), unless parameters are estimated |
| Goodness of fit with estimated parameter | Does observed distribution fit a fitted model? | Estimate parameter, then use \(E_i=Np_i\) | \(k-2\) if one parameter is estimated |
| Contingency table | Are two categorical variables independent? | \(E=\frac{(\text{row total})(\text{column total})}{\text{grand total}}\) | \((r-1)(c-1)\) |
| \(2\times2\) contingency table | Are two categorical variables independent? | Same expected-frequency formula | \(1\), with Yates’ correction |

Good hypothesis wording:

\[
H_0:\text{ the proposed distribution is a suitable model.}
\]

\[
H_1:\text{ the proposed distribution is not a suitable model.}
\]

For independence:

\[
H_0:\text{ the variables are independent.}
\]

\[
H_1:\text{ the variables are not independent.}
\]

Before calculating \(X^2\), check every expected frequency is at least \(5\). The rejection region is upper-tail. Use “do not reject \(H_0\)” rather than overclaiming that \(H_0\) is true.

## 16. Syllabus Gap Check

| LO ID | Official requirement | Covered? |
|---|---|---:|
| FA22-CHI2-LO001 | fit a theoretical distribution, as prescribed by a given hypothesis, to given data | Yes |
| FA22-CHI2-LO002 | use a \(\chi^2\) test with the appropriate number of degrees of freedom to carry out the corresponding goodness of fit test | Yes |
| FA22-CHI2-LO003 | use a \(\chi^2\) test with the appropriate number of degrees of freedom to test for independence in a contingency table | Yes |

### Off-Spec Content Found but Excluded

| Content | Source | Reason excluded from core |
|---|---|---|
| Dr Frost platform registration and promotional slide content | Slide PDF | Not mathematical FA22-CHI2 lesson content |
| MAT/UKMT extension references | Slide PDF | Not CCEA FA22 core |
| Pearson exercise page references | Slide PDF | Cross-board provenance only |
| Old S3 / Edexcel-style exam branding | Slide and transcript evidence | Not CCEA authority |
| Long theoretical derivation from CLT beyond exam need | Transcript | Included only as intuition, not required proof |
| Full geometric model testing as compulsory content | Cross-board evidence | Treated as optional enrichment unless a theoretical distribution is prescribed by the CCEA question |

### Missing evidence log

| Missing evidence | Consequence |
|---|---|
| CCEA past-paper extract or mark scheme for \(\chi^2\) tests | Exam-style wording is based on CCEA specification logic, not a supplied mark scheme |
| Full readable text from screenshot PDF | Later handwritten annotations cannot be exhaustively preserved |
| CCEA-specific Yates example | Generated practice example used instead |
| Formula-booklet \(\chi^2\) table extract | Critical values used are standard values supplied inside examples, not reproduced as a full table |

## 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include a goodness-of-fit workflow flowchart, upper-tail \(\chi^2\) sketch, observed-versus-expected table visual, degrees-of-freedom diagram, contingency-table row/column total diagram, Yates correction comparison visual, dynamic \(O,E\) calculator, degrees-of-freedom checker and contingency-table expected-frequency widget.

These are proposed enhancements, not evidence-backed diagram details.

## 18. Supplementary Sources Used

| Source | Role |
|---|---|
| CCEA GCE Further Mathematics Specification Map | Primary authority for FA22-CHI2 topic boundary, LO IDs and CCEA elaboration |
| Further Maths README module map | Unit/topic placement and bridge mapping |
| Further Maths Evidence Drop Checklist | Evidence-planning discipline and file/asset workflow |
| Ordinary A-Level Maths Bridge Spec Extracts | Bridge context only |
| CCEA GCE Mathematics Specification Map | Ordinary Maths bridge context only |
| `FS1-Chp6-ChiSquaredTests.pdf` | Cross-board slide evidence for model testing, expected versus observed frequencies, \(X^2\), degrees of freedom and examples |
| `transcripts.md` | Teacher explanation evidence for motivation, notation, formula derivation, constraints, parameter estimation, combining classes and conclusion wording |
| `Chapter_6_Chi-Squared_Tests_📊_(Further_Statistics_1)_screenshots.pdf` | Visual evidence for slide structure, table layout and handwritten annotations where visible |

The Dr Frost / Pearson evidence is not CCEA authority. It is used because its mathematics matches the CCEA FA22-CHI2 specification. Ordinary A-Level Mathematics evidence is used only as bridge context.

## 19. Final Student Checklist

### Prerequisite confidence

- [ ] calculate expected frequencies using \(E_i=Np_i\);
- [ ] calculate the mean from a frequency table;
- [ ] use binomial probabilities;
- [ ] use Poisson probabilities;
- [ ] read a significance level and critical value;
- [ ] explain \(H_0\) and \(H_1\);
- [ ] interpret a conclusion in context.

### Further Maths method

- [ ] state \(H_0\) and \(H_1\);
- [ ] calculate expected frequencies;
- [ ] combine classes if any expected frequency is below \(5\);
- [ ] calculate \(X^2=\sum\frac{(O-E)^2}{E}\);
- [ ] use \(X^2=\sum\frac{O^2}{E}-N\);
- [ ] find degrees of freedom;
- [ ] reduce degrees of freedom when a parameter is estimated;
- [ ] compare with the upper-tail critical value;
- [ ] write a contextual conclusion.

### Contingency-table method

- [ ] identify the two categorical variables;
- [ ] state independence hypotheses;
- [ ] calculate expected frequencies using \(E=\frac{(\text{row total})(\text{column total})}{\text{grand total}}\);
- [ ] check expected frequencies are at least \(5\);
- [ ] calculate \(\nu=(r-1)(c-1)\);
- [ ] apply Yates’ correction for \(2\times2\);
- [ ] conclude in terms of association or independence.

You are ready for FA22-CHI2 when you can look at a frequency table and decide: what is being tested, what the expected frequencies are, whether any classes need combining, what the degrees of freedom are, whether Yates’ correction is needed, whether the statistic lies in the upper-tail critical region, and what the conclusion means in context.
