# 1. Lesson Title and Metadata

# FA22 Sampling and Estimation

**Date generated:** 2026-06-04  
**Course:** CCEA GCE Further Mathematics  
**Unit:** FA22 – Further A2 2 Applied Mathematics  
**Applied section:** Section C: Statistics  
**Topic code:** FA22-EST  
**Topic name:** Sampling and estimation  
**Topic slug:** sampling_and_estimation  
**Topic Pascal:** SamplingAndEstimation  
**Topic ID:** FA22SamplingAndEstimation  
**Lesson file:** FA22_sampling_and_estimation_lesson.md  

## Learning outcome IDs

- FA22-EST-LO001
- FA22-EST-LO002
- FA22-EST-LO003
- FA22-EST-LO004

## Bridge tags

- AS2 Sampling
- AS2 Data Presentation and Interpretation
- A22 Normal Distribution
- A22 Hypothesis Testing

## Topic tags

- #FA22
- #Statistics
- #Sampling
- #Estimation
- #CentralLimitTheorem
- #PointEstimates
- #UnbiasedEstimator
- #StandardError
- #ConfidenceIntervals

This lesson covers the FA22 topic **Sampling and estimation**. It includes population parameters, sample statistics, sampling distributions, estimators, point estimates, standard error, the central limit theorem and confidence intervals for a population mean. Normal-distribution testing material from the supplied wider Chapter 5 evidence is excluded from this core lesson.

---

# 2. Evidence Map

| Evidence source | How it is used |
|---|---|
| CCEA Further Mathematics Specification Map | Authority for topic code, LO IDs and boundary. |
| Further Maths README Module Map | Authority for file naming, phase structure and bridge requirements. |
| Further Maths Evidence Drop Checklist | Authority for missing evidence, off-spec and asset logs. |
| `transcripts.md` | Core lesson evidence for estimators, standard error and confidence intervals. |
| `Chapter_5_Estimation,_Confidence_Intervals_&_Tests_using_a_Normal_Distribution_📈_(Further_Statistics_2)_screenshots.pdf` | Visual evidence only; parsed text unavailable. |
| `S3-Chp3-EstimationConfidenceIntervals.pdf` | Cross-board support used only where aligned with CCEA FA22-EST. |
| Ordinary A-Level Maths bridge extracts | Bridge context only. |

## Visual evidence limitation

The screenshot PDF was visual-only in this environment. Only visible/readable details from rendered previews were used. No uninspected visual detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary | Bridge |
|---|---|---|---|---|---|
| FA22-EST-LO001 | demonstrate understanding of and use the central limit theorem for samples of 30 or more observations | CLT, \(\bar X\approx N(\mu,\sigma^2/n)\), \(n\ge30\) rule | CCEA spec, transcript, PDF | Core | A22 Normal |
| FA22-EST-LO002 | calculate point estimates of the population mean and variance, including use of \(S^2=\frac{\sum(X_i-\bar X)^2}{n-1}\) as an unbiased estimator of \(\sigma^2\) | Estimator/estimate, bias, \(\hat\mu=\bar x\), \(s^2\) | CCEA spec, transcript, PDF | Core | AS2 data |
| FA22-EST-LO003 | demonstrate understanding of and use the standard error of the mean | \(\operatorname{SE}(\bar X)=\sigma/\sqrt n\), estimated \(s/\sqrt n\) | CCEA spec, transcript, PDF | Core | A22 Normal |
| FA22-EST-LO004 | calculate confidence intervals for the population mean | \(\bar x\pm z\sigma/\sqrt n\), 95%, 99%, width and sample-size work | CCEA spec, transcript, PDF | Core | A22 Normal/inference |

---

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Distinguish between a **population parameter** and a **sample statistic**.
2. Decide whether a formula is a statistic by checking whether it depends only on sample observations.
3. Define the sampling distribution of a statistic.
4. Explain why \(\bar X\) is an estimator for \(\mu\).
5. Use the bias formula
   \[
   \operatorname{Bias}(T)=E(T)-\theta.
   \]
6. Show that \(\bar X\) is an unbiased estimator for \(\mu\).
7. Use
   \[
   \operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad
   \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}.
   \]
8. Calculate point estimates
   \[
   \hat\mu=\bar x,\qquad
   \hat\sigma^2=s^2=\frac{\sum(x_i-\bar x)^2}{n-1}.
   \]
9. Use the central limit theorem for samples of size \(30\) or more.
10. Calculate and interpret confidence intervals for the population mean.

## 4.2 Bridge objectives

Connect ordinary A-Level sampling, mean, variance, normal distribution and hypothesis-testing language to Further Maths estimation. The upgrade is that a sample statistic becomes a random variable with its own distribution.

## 4.3 Exam technique objectives

Use correct notation, show enough expectation/variance working, use \(n-1\) for \(s^2\), use \(\sqrt n\) in standard error, round sample sizes up and interpret intervals in context.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You should know the mean formula, frequency table calculations, square roots, squared quantities, inequalities and rearranging.

## 5.2 Ordinary AS/A2 Mathematics foundations

You should know sampling, population and sample language, variance and standard deviation, normal notation \(X\sim N(\mu,\sigma^2)\), standardisation
\[
Z=\frac{X-\mu}{\sigma},
\]
and inference from sample to population.

## 5.3 Previous Further Mathematics foundations

For independent variables:
\[
E(aX+bY)=aE(X)+bE(Y)
\]
and
\[
\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y).
\]

If independent normal variables are combined linearly, the result is also normal:
\[
aX\pm bY\sim N(a\mu_X\pm b\mu_Y,\ a^2\sigma_X^2+b^2\sigma_Y^2).
\]

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Sampling | Population, sample and sampling bias | Samples become \(X_1,\ldots,X_n\); statistics have sampling distributions | A sample result is not the exact population value |
| AS2 Data Presentation | Mean, variance, standard deviation and summaries | \(\bar X\) estimates \(\mu\); \(S^2\) estimates \(\sigma^2\) | Dividing by \(n\) underestimates \(\sigma^2\) |
| A22 Normal Distribution | \(X\sim N(\mu,\sigma^2)\), standardisation | \(\bar X\sim N(\mu,\sigma^2/n)\) exactly for normal populations or approximately by CLT | Do not confuse \(X\) with \(\bar X\) |
| A22 Hypothesis Testing | Samples support inference | Confidence intervals quantify uncertainty around \(\mu\) | “95% confident” is not the same as a moving \(\mu\) |

In ordinary A-Level Maths, this idea appeared as sampling, averages and normal probabilities. In Further Maths, the same idea becomes a full inference machine: \(\bar X\) and \(S^2\) are statistics whose reliability can be measured.

---

# 6. Big Picture Explanation

A population parameter such as \(\mu\) or \(\sigma^2\) describes the whole population. Usually it is unknown. A sample gives observations \(X_1,\ldots,X_n\). From these we calculate statistics such as
\[
\bar X=\frac{X_1+\cdots+X_n}{n}
\]
and
\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}.
\]

The central question is:

> How reliable is this statistic as an estimate of the true population parameter?

This lesson answers that using bias, standard error, the central limit theorem and confidence intervals.

---

# 7. Key Definitions and Notation

## 7.1 Population and parameter

A **population** is the whole group being studied. A **population parameter** is a true measure of the whole population:
\[
\mu=\text{population mean},\qquad \sigma=\text{population standard deviation},\qquad \sigma^2=\text{population variance}.
\]

## 7.2 Sample and statistic

A random sample of size \(n\) is
\[
X_1,X_2,\ldots,X_n.
\]

A **statistic** is calculated only from sample observations and constants. It must not contain unknown population parameters such as \(\mu\) or \(\sigma\).

Statistics include:
\[
\frac{X_1+X_2+X_3}{3},\qquad
\max(X_1,\ldots,X_n),\qquad
\frac{\sum_{i=1}^{n}X_i}{n}.
\]

Not a statistic:
\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2,
\]
because it contains \(\mu\) and \(\sigma\).

## 7.3 Sample mean

\[
\bar X=\frac1n\sum_{i=1}^n X_i
\]
before the sample is observed, and
\[
\bar x=\frac1n\sum_{i=1}^n x_i
\]
after a particular sample is observed.

## 7.4 Estimator and estimate

An **estimator** is a statistic used to estimate a population parameter. For example, \(\bar X\) estimates \(\mu\). An **estimate** is the value after observation, for example \(\bar x=5.30\).

## 7.5 Bias

If \(T\) estimates \(\theta\), then
\[
\operatorname{Bias}(T)=E(T)-\theta.
\]
If \(E(T)=\theta\), then \(T\) is unbiased.

## 7.6 Unbiased sample variance

\[
S^2=\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}.
\]
For observed data:
\[
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar x)^2}{n-1}
=\frac{\sum x_i^2-n\bar x^2}{n-1}.
\]
For frequency data:
\[
s^2=\frac{\sum fx^2-n\bar x^2}{n-1},\qquad n=\sum f.
\]

## 7.7 Standard error

\[
\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}.
\]
If \(\sigma\) is unknown in a suitable large-sample setting:
\[
\operatorname{SE}(\bar X)\approx \frac{s}{\sqrt n}.
\]

## 7.8 Confidence interval

For critical value \(z\):
\[
\bar x\pm z\frac{\sigma}{\sqrt n}.
\]
For 95%:
\[
\bar x\pm 1.96\frac{\sigma}{\sqrt n}.
\]
For 99%:
\[
\bar x\pm 2.5758\frac{\sigma}{\sqrt n}.
\]

---

# 8. Core Theory

## 8.1 Statistic or not?

Let \(X_1,\ldots,X_n\) be a sample from a population with unknown \(\mu\) and \(\sigma\).

\[
\frac{X_1+X_2+X_3}{3}
\]
is a statistic because it uses only sample observations.

\[
\max(X_1,\ldots,X_n)
\]
is a statistic because it uses only sample observations.

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2
\]
is not a statistic because it contains population parameters.

\[
\frac{\sum_{i=1}^{n}X_i}{n}
\]
is a statistic because it equals \(\bar X\).

**Bridge Note:** In ordinary A-Level Maths, you calculated averages from data. Here, the average becomes a statistic whose sampling behaviour matters.

## 8.2 Sampling distribution of a statistic

The sampling distribution of a statistic is the probability distribution of that statistic across possible samples. It describes how the statistic varies when different samples are taken.

### Example: \(R=X_{25}-X_1\), \(T=X_1+\cdots+X_{25}\)

Suppose
\[
X\sim N(\mu,4^2).
\]
A random sample of size 25 is taken.

For
\[
R=X_{25}-X_1,
\]
\[
E(R)=\mu-\mu=0,
\]
and
\[
\operatorname{Var}(R)=4^2+4^2=16+16=32.
\]
Therefore
\[
R\sim N(0,32).
\]

For
\[
T=X_1+\cdots+X_{25},
\]
\[
E(T)=25\mu,
\]
and
\[
\operatorname{Var}(T)=25\times4^2=400=20^2.
\]
Therefore
\[
T\sim N(25\mu,20^2).
\]

## 8.3 \(\bar X\) is unbiased for \(\mu\)

\[
\bar X=\frac{X_1+\cdots+X_n}{n}.
\]
Then
\[
E(\bar X)=E\left(\frac{X_1+\cdots+X_n}{n}\right)
=\frac1n[E(X_1)+\cdots+E(X_n)].
\]
Since each \(E(X_i)=\mu\),
\[
E(\bar X)=\frac1n(n\mu)=\mu.
\]
Therefore
\[
\boxed{\bar X\text{ is an unbiased estimator of }\mu.}
\]

For a particular sample,
\[
\hat\mu=\bar x.
\]

## 8.4 Variance of \(\bar X\) and standard error

\[
\operatorname{Var}(\bar X)
=
\operatorname{Var}\left(\frac{X_1+\cdots+X_n}{n}\right)
=
\frac1{n^2}\left[\operatorname{Var}(X_1)+\cdots+\operatorname{Var}(X_n)\right].
\]
Since each variance is \(\sigma^2\),
\[
\operatorname{Var}(\bar X)=\frac1{n^2}(n\sigma^2)=\frac{\sigma^2}{n}.
\]
So
\[
\operatorname{SE}(\bar X)=\sqrt{\frac{\sigma^2}{n}}=\frac{\sigma}{\sqrt n}.
\]

As \(n\) increases, the standard error decreases. Bigger samples give less variable sample means.

## 8.5 Why \(S^2\) uses \(n-1\)

The divide-by-\(n\) sample variance-like expression
\[
V=\frac1n\sum_{i=1}^{n}(X_i-\bar X)^2
\]
is biased downward. In fact
\[
E(V)=\frac{n-1}{n}\sigma^2.
\]
Since \((n-1)/n<1\), it underestimates \(\sigma^2\) on average.

The unbiased correction is
\[
S^2=\frac1{n-1}\sum_{i=1}^{n}(X_i-\bar X)^2.
\]
This satisfies
\[
E(S^2)=\sigma^2.
\]

**Bridge Note:** The \(n-1\) denominator is not decoration. It corrects the downward bias caused by measuring deviations from \(\bar X\), which was itself calculated from the same sample.

## 8.6 Central limit theorem

For a random sample \(X_1,\ldots,X_n\) from a population with mean \(\mu\) and variance \(\sigma^2\), for sufficiently large \(n\):
\[
\bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right).
\]
For CCEA FA22-EST, use this for samples of 30 or more observations:
\[
\boxed{n\ge30\implies \bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right).}
\]

If the original population is already normal, then \(\bar X\) is normal without needing the large-sample approximation.

The CLT does not say \(X\) becomes normal. It says \(\bar X\) is approximately normal.

## 8.7 Confidence interval derivation

If
\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right),
\]
then
\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
\]
For a 95% central interval:
\[
P(-1.96<Z<1.96)=0.95.
\]
So
\[
P\left(-1.96<\frac{\bar X-\mu}{\sigma/\sqrt n}<1.96\right)=0.95.
\]
Multiply through by \(\sigma/\sqrt n\):
\[
P\left(-1.96\frac{\sigma}{\sqrt n}<\bar X-\mu<1.96\frac{\sigma}{\sqrt n}\right)=0.95.
\]
Rearrange for \(\mu\):
\[
P\left(\bar X-1.96\frac{\sigma}{\sqrt n}<\mu<\bar X+1.96\frac{\sigma}{\sqrt n}\right)=0.95.
\]
After observing \(\bar x\):
\[
\boxed{\bar x\pm1.96\frac{\sigma}{\sqrt n}.}
\]

## 8.8 Width and sample size

Margin of error:
\[
z\frac{\sigma}{\sqrt n}.
\]
Full width:
\[
\boxed{\text{Width}=2z\frac{\sigma}{\sqrt n}.}
\]

If a desired width is at most \(W\):
\[
2z\frac{\sigma}{\sqrt n}\le W
\]
so
\[
n\ge\left(\frac{2z\sigma}{W}\right)^2.
\]
Always round \(n\) up.

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationMermaid-001 | Source: CCEA FA22-EST specification map + lesson transcript | Insert from mermaid/FA22SamplingAndEstimationMermaid-001.md | Purpose: Show the full conceptual flow from population parameter to sample statistic, estimator, bias, standard error and confidence interval. The diagram should include \(\mu\), \(\sigma^2\), \(X_1,\ldots,X_n\), \(\bar X\), \(S^2\), \(\operatorname{SE}(\bar X)\) and confidence interval.]

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA Further Maths specification | Insert from svg/FA22SamplingAndEstimationBridgeSVG-001.svg | Purpose: Compare ordinary AS2/A22 sampling and normal distribution with FA22 sampling distributions and confidence intervals.]

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationSVG-001 | Source: Teacher transcript + screenshot PDF visible pages | Insert from svg/FA22SamplingAndEstimationSVG-001.svg | Purpose: Show population parameter vs sample statistic.]

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationSVG-002 | Source: Teacher transcript + Dr Frost S3 PDF | Insert from svg/FA22SamplingAndEstimationSVG-002.svg | Purpose: Show repeated samples generating different values of \(\bar X\), with the distribution of \(\bar X\) centred at \(\mu\) and variance \(\sigma^2/n\).]

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationTikZ-001 | Source: Teacher transcript confidence interval derivation | Insert from tikz/FA22SamplingAndEstimationTikZ-001.tex | Purpose: Draw the standard normal curve with central 95%, tail areas 2.5%, and critical values \(z=-1.96\), \(z=1.96\).]

[VISUAL PLACEHOLDER: FA22SamplingAndEstimationTikZ-002 | Source: Teacher transcript + CCEA FA22-EST LO004 | Insert from tikz/FA22SamplingAndEstimationTikZ-002.tex | Purpose: Show \(\bar x\), lower limit, upper limit, margin of error and interval width.]

Diagram evidence is partially unclear here. The description above preserves the visible/readable details only. No uninspected visual detail is claimed.

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22SamplingAndEstimationWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22SamplingAndEstimationWidget-001.html | Purpose: Statistic-or-not classifier.]

[INTERACTIVE PLACEHOLDER: FA22SamplingAndEstimationWidget-002 | Source: AI-proposed teaching enhancement based on FA22-EST-LO002 and transcript warnings | Insert from widgets/FA22SamplingAndEstimationWidget-002.html | Purpose: Compare divide-by-\(n\) and divide-by-\(n-1\) variance calculations.]

[INTERACTIVE PLACEHOLDER: FA22SamplingAndEstimationWidget-003 | Source: AI-proposed teaching enhancement based on FA22-EST-LO003 and FA22-EST-LO004 | Insert from widgets/FA22SamplingAndEstimationWidget-003.html | Purpose: Confidence interval and sample-size calculator.]

---

# 11. Worked Examples

## Worked Example 1: Decide whether each expression is a statistic

A sample \(X_1,\ldots,X_n\) is taken from a population with unknown parameters \(\mu\) and \(\sigma\). Decide whether each expression is a statistic.

\[
\frac{X_1+X_2+X_3}{3}
\]
is a statistic because it uses only sample observations and constants.

\[
\max(X_1,\ldots,X_n)
\]
is a statistic because it uses only sample observations.

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2
\]
is not a statistic because it contains \(\mu\) and \(\sigma\).

\[
\frac{\sum_{i=1}^{n}X_i}{n}
\]
is a statistic because it uses only sample observations and sample size.

## Worked Example 2: Sampling distributions of two statistics

If \(X\sim N(\mu,4^2)\), and
\[
R=X_{25}-X_1,\qquad T=X_1+\cdots+X_{25},
\]
then
\[
E(R)=\mu-\mu=0,
\]
and
\[
\operatorname{Var}(R)=4^2+4^2=32.
\]
Thus
\[
\boxed{R\sim N(0,32).}
\]

For \(T\):
\[
E(T)=25\mu,
\]
and
\[
\operatorname{Var}(T)=25\times4^2=400=20^2.
\]
Thus
\[
\boxed{T\sim N(25\mu,20^2).}
\]

## Worked Example 3: Unbiased estimates from a frequency table

The table summarises the number of breakdowns, \(x\), on 30 randomly chosen days.

| \(x\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(f\) | 3 | 5 | 4 | 3 | 5 | 4 | 4 | 2 |

Given:
\[
\sum fx=160,\qquad \sum fx^2=990,\qquad n=30.
\]

Estimate of the mean:
\[
\hat\mu=\bar x=\frac{160}{30}=\frac{16}{3}=5.333\ldots
\]
so
\[
\boxed{\hat\mu=5.33.}
\]

Estimate of the variance:
\[
s^2=\frac{\sum fx^2-n\bar x^2}{n-1}
=\frac{990-30(16/3)^2}{29}.
\]
Since
\[
(16/3)^2=\frac{256}{9},
\]
\[
s^2=\frac{990-30\cdot256/9}{29}
=\frac{990-853.333\ldots}{29}
=4.7126\ldots
\]
so
\[
\boxed{\hat\sigma^2=4.71.}
\]

## Worked Example 4: Combine two samples and find standard error

First sample:
\[
n_1=30,\qquad \sum x=160,\qquad \sum x^2=990.
\]
Second sample:
\[
n_2=20,\qquad \bar y=6.0,\qquad s_y^2=5.0.
\]

From \(\bar y=6.0\):
\[
\sum y=20\times6=120.
\]

From
\[
s_y^2=\frac{\sum y^2-20(6)^2}{19}=5,
\]
\[
95=\sum y^2-720,
\]
so
\[
\sum y^2=815.
\]

Combined:
\[
n=50,\qquad \sum w=160+120=280,\qquad \sum w^2=990+815=1805.
\]

Mean estimate:
\[
\bar w=\frac{280}{50}=5.6.
\]

Variance estimate:
\[
s^2=\frac{1805-50(5.6)^2}{49}
=\frac{1805-1568}{49}
=\frac{237}{49}=4.8367\ldots
\]
so
\[
\boxed{\hat\sigma^2=4.84.}
\]

Standard error:
\[
\operatorname{SE}(\bar W)\approx\frac{s}{\sqrt n}
=\frac{\sqrt{4.8367\ldots}}{\sqrt{50}}
=0.3110\ldots
\]
so
\[
\boxed{\operatorname{SE}=0.311.}
\]

For standard error less than \(0.25\):
\[
\frac{\sqrt{4.8367\ldots}}{\sqrt n}<0.25.
\]
Square:
\[
\frac{4.8367\ldots}{n}<0.0625.
\]
Thus
\[
n>77.3877\ldots
\]
so
\[
\boxed{n=78.}
\]

## Worked Example 5: Biased estimator for a uniform distribution

Let \(X\sim U[0,\alpha]\). Then
\[
E(X)=\frac{\alpha}{2}.
\]
Since \(E(\bar X)=E(X)\),
\[
E(\bar X)=\frac{\alpha}{2}.
\]
If \(\bar X\) estimates \(\alpha\), then
\[
\operatorname{Bias}(\bar X)=E(\bar X)-\alpha
=\frac{\alpha}{2}-\alpha
=-\frac{\alpha}{2}.
\]
So \(\bar X\) is biased for \(\alpha\).

To create an unbiased estimator:
\[
T=2\bar X.
\]
Then
\[
E(T)=2E(\bar X)=2\cdot\frac{\alpha}{2}=\alpha.
\]
Therefore
\[
\boxed{2\bar X\text{ is an unbiased estimator for }\alpha.}
\]

## Worked Example 6: CLT probability for a discrete die

A die has three faces marked \(1\), two faces marked \(3\), one face marked \(6\). Let \(X\) be one score.

\[
E(X)=1\cdot\frac36+3\cdot\frac26+6\cdot\frac16
=\frac{15}{6}=2.5.
\]

\[
E(X^2)=1^2\cdot\frac36+3^2\cdot\frac26+6^2\cdot\frac16
=\frac{57}{6}=9.5.
\]

\[
\operatorname{Var}(X)=9.5-(2.5)^2=3.25=\frac{13}{4}.
\]

For \(n=40\):
\[
\bar X\approx N\left(2.5,\frac{13/4}{40}\right)
=N\left(2.5,\frac{13}{160}\right).
\]

\[
P(\bar X>3)
=
P\left(Z>\frac{3-2.5}{\sqrt{13/160}}\right).
\]

\[
\frac{0.5}{\sqrt{13/160}}=1.754\ldots
\]

\[
P(Z>1.754\ldots)=0.0397\ldots
\]
so
\[
\boxed{P(\bar X>3)\approx0.040.}
\]

## Worked Example 7: 95% confidence interval

The breaking strains of reels of string have standard deviation \(1.5\) kg. A sample of \(100\) reels has mean \(5.30\) kg.

\[
\sigma=1.5,\qquad n=100,\qquad \bar x=5.30.
\]

For 95% confidence:
\[
z=1.96.
\]

\[
\bar x\pm z\frac{\sigma}{\sqrt n}
=
5.30\pm1.96\frac{1.5}{10}.
\]
\[
1.96\frac{1.5}{10}=1.96(0.15)=0.294.
\]
So
\[
5.30\pm0.294.
\]
Lower limit:
\[
5.30-0.294=5.006.
\]
Upper limit:
\[
5.30+0.294=5.594.
\]
Therefore
\[
\boxed{5.006<\mu<5.594}
\]
or
\[
\boxed{5.01<\mu<5.59}
\]
to 3 significant figures.

## Worked Example 8: Sample size for margin of error

A population standard deviation is \(3\) kg. Find the minimum \(n\) so a 95% estimate lies within \(0.8\) kg.

\[
1.96\frac{3}{\sqrt n}\le0.8.
\]
\[
5.88\le0.8\sqrt n.
\]
\[
7.35\le\sqrt n.
\]
\[
54.0225\le n.
\]
Round up:
\[
\boxed{n=55.}
\]

## Worked Example 9: Compare two unbiased estimators

Let
\[
X\sim\operatorname{Bin}(n,p),\qquad Y\sim\operatorname{Bin}(m,p)
\]
with independent samples and \(m\ne n\).

\[
S=\frac{X+Y}{m+n},\qquad
T=\frac12\left(\frac Xn+\frac Ym\right).
\]

\[
E(S)=\frac{E(X)+E(Y)}{m+n}
=\frac{np+mp}{m+n}=p.
\]
So \(S\) is unbiased.

\[
E(T)=\frac12\left(\frac{E(X)}n+\frac{E(Y)}m\right)
=\frac12(p+p)=p.
\]
So \(T\) is unbiased.

\[
\operatorname{Var}(S)=\frac{\operatorname{Var}(X)+\operatorname{Var}(Y)}{(m+n)^2}
=\frac{np(1-p)+mp(1-p)}{(m+n)^2}
=\frac{p(1-p)}{m+n}.
\]

\[
\operatorname{Var}(T)
=
\frac14\left(\frac{\operatorname{Var}(X)}{n^2}+\frac{\operatorname{Var}(Y)}{m^2}\right)
=
\frac{p(1-p)}4\left(\frac1n+\frac1m\right)
=
\frac{p(1-p)(m+n)}{4mn}.
\]

Compare:
\[
\frac1{m+n}<\frac{m+n}{4mn}
\]
is equivalent to
\[
4mn<(m+n)^2.
\]
\[
4mn<m^2+2mn+n^2
\]
is equivalent to
\[
0<(m-n)^2,
\]
which is true since \(m\ne n\). Therefore
\[
\operatorname{Var}(S)<\operatorname{Var}(T),
\]
so
\[
\boxed{S\text{ is the better estimator.}}
\]

---

# 12. Common Mistakes and Exam Traps

1. Calling an expression a statistic when it contains \(\mu\) or \(\sigma\).
2. Writing \(\mu=\bar x\) instead of \(\bar x=...\).
3. Dividing by \(n\) instead of \(n-1\) for \(s^2\).
4. Reporting \(s\) when the question asks for \(s^2\).
5. Using \(\sigma^2\) in the confidence interval instead of \(\sigma\).
6. Dividing by \(n\) instead of \(\sqrt n\) in standard error.
7. Thinking CLT makes \(X\) normal; it describes \(\bar X\).
8. Applying continuity correction to \(\bar X\) without being asked.
9. Saying “there is a 95% probability that \(\mu\) is in this interval” without care.
10. Rounding sample size down.

---

# 13. Practice Questions

## Basic fluency

1. Decide whether each is a statistic:
   \[
   X_1+2X_2,\quad
   \frac{\sum(X_i-\bar X)^2}{n-1},\quad
   \frac{X_1-\mu}{\sigma},\quad
   \min(X_1,\ldots,X_n).
   \]

2. Show that \(E(\bar X)=\mu\).

3. A sample of \(8\) observations has
   \[
   \sum x=52,\qquad \sum x^2=366.
   \]
   Calculate unbiased estimates of the population mean and variance.

## Bridge questions

4. Explain why \(s^2=\frac{\sum x^2-n\bar x^2}{n-1}\) is used when estimating a population variance.

5. A sample of size \(36\) is taken from a population with mean \(50\) and variance \(81\). State the approximate distribution of \(\bar X\).

## Standard exam-style questions

6. A population has standard deviation \(12\). A sample of size \(64\) has mean \(103.5\). Find a 95% confidence interval for \(\mu\).

7. A component lifetime has known standard deviation \(18\). A sample of \(100\) has mean \(240\). Find a 99% confidence interval for \(\mu\).

8. A manufacturer wants a 95% confidence interval to have total width no more than \(4\). The population standard deviation is \(10\). Find the minimum sample size.

## Harder synthesis

9. A random variable has distribution:

| \(x\) | 0 | 2 | 5 |
|---:|---:|---:|---:|
| \(P(X=x)\) | 0.2 | 0.5 | 0.3 |

A sample of size \(50\) is taken. Approximate \(P(\bar X>2.8)\).

10. If \(X\sim\operatorname{Bin}(n,p)\), show that \(X/n\) is an unbiased estimator of \(p\) and find its variance.

---

# 14. Worked Solutions

## Solution 1

- \(X_1+2X_2\): statistic.
- \(\frac{\sum(X_i-\bar X)^2}{n-1}\): statistic.
- \(\frac{X_1-\mu}{\sigma}\): not a statistic, because it contains \(\mu\) and \(\sigma\).
- \(\min(X_1,\ldots,X_n)\): statistic.

## Solution 2

\[
E(\bar X)
=E\left(\frac{X_1+\cdots+X_n}{n}\right)
=\frac1n[E(X_1)+\cdots+E(X_n)]
=\frac1n(n\mu)=\mu.
\]

## Solution 3

\[
\bar x=\frac{52}{8}=6.5.
\]
\[
s^2=\frac{366-8(6.5)^2}{8-1}
=\frac{366-338}{7}
=4.
\]
So
\[
\boxed{\hat\mu=6.5,\qquad \hat\sigma^2=4.}
\]

## Solution 4

The divide-by-\(n\) variance underestimates \(\sigma^2\) on average because deviations are measured from the sample mean \(\bar x\), which is itself chosen from the data. The denominator \(n-1\) corrects this bias:
\[
E(S^2)=\sigma^2.
\]

## Solution 5

\[
\bar X\approx N\left(50,\frac{81}{36}\right)
=N\left(50,\frac94\right).
\]
The approximation is allowed because \(n=36\ge30\).

## Solution 6

\[
103.5\pm1.96\frac{12}{\sqrt{64}}
=
103.5\pm1.96\frac{12}{8}
=
103.5\pm2.94.
\]
\[
\boxed{100.56<\mu<106.44.}
\]

## Solution 7

\[
240\pm2.5758\frac{18}{\sqrt{100}}
=
240\pm2.5758(1.8)
=
240\pm4.63644.
\]
\[
\boxed{235.36<\mu<244.64.}
\]

## Solution 8

\[
2(1.96)\frac{10}{\sqrt n}\le4.
\]
\[
\frac{39.2}{\sqrt n}\le4.
\]
\[
9.8\le\sqrt n.
\]
\[
96.04\le n.
\]
So
\[
\boxed{n=97.}
\]

## Solution 9

\[
E(X)=0(0.2)+2(0.5)+5(0.3)=2.5.
\]
\[
E(X^2)=0^2(0.2)+2^2(0.5)+5^2(0.3)=9.5.
\]
\[
\sigma^2=9.5-(2.5)^2=3.25.
\]
For \(n=50\):
\[
\bar X\approx N\left(2.5,\frac{3.25}{50}\right)=N(2.5,0.065).
\]
\[
P(\bar X>2.8)=P\left(Z>\frac{2.8-2.5}{\sqrt{0.065}}\right)
=P(Z>1.1767\ldots)=0.1196\ldots
\]
\[
\boxed{P(\bar X>2.8)\approx0.120.}
\]

## Solution 10

If \(X\sim\operatorname{Bin}(n,p)\), then \(E(X)=np\) and \(\operatorname{Var}(X)=np(1-p)\).

\[
E\left(\frac Xn\right)=\frac1nE(X)=\frac{np}{n}=p.
\]
So \(X/n\) is unbiased.

\[
\operatorname{Var}\left(\frac Xn\right)=\frac1{n^2}\operatorname{Var}(X)
=\frac{np(1-p)}{n^2}
=\frac{p(1-p)}n.
\]

---

# 15. Exam Technique Notes

- Always identify whether the random variable is \(X\), \(\bar X\), \(S^2\), or an observed value.
- Write \(\bar X\approx N(\mu,\sigma^2/n)\) before using CLT.
- Use \(\bar x\) for the observed sample mean, not \(\mu\).
- Use \(s^2\), not the divide-by-\(n\) variance, when estimating \(\sigma^2\).
- Confidence interval:
  \[
  \bar x\pm z\frac{\sigma}{\sqrt n}.
  \]
- 95% uses \(z=1.96\).
- 99% uses \(z=2.5758\).
- Interpret in context: “We are 95% confident that \(\mu\) lies between ...”
- Sample-size answers must be rounded up.

---

# 16. Syllabus Gap Check

## LO coverage

| LO ID | Coverage |
|---|---|
| FA22-EST-LO001 | CLT for \(n\ge30\), distribution of \(\bar X\) |
| FA22-EST-LO002 | Point estimates, \(\hat\mu=\bar x\), \(S^2\) |
| FA22-EST-LO003 | Standard error of the mean |
| FA22-EST-LO004 | Confidence intervals for \(\mu\) |

## Off-Spec Content Found but Excluded

| Content | Reason excluded |
|---|---|
| Tests using a normal distribution | Not part of FA22-EST core lesson |
| Difference of means tests | Later inference/testing material |
| Unknown variance tests | Boundary-risk with later \(t\)-distribution and testing material |
| Full \(t\)-distribution confidence interval theory | Separate FA22 topic |
| \(\chi^2\) tests | Separate FA22 topic |

## Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| CCEA textbook pages | Worked examples use supplied transcript/PDF evidence |
| CCEA past-paper mark schemes | Practice questions are labelled AI-generated |
| Full parsed screenshot PDF text | Visual descriptions are cautious |
| Calculator screenshots | Calculator warnings included without screen paths |

---

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements:

- population vs sample diagram;
- sampling distribution diagram;
- variance denominator comparison visual;
- confidence interval number line;
- standard normal 95% area diagram;
- statistic-or-not widget;
- sample variance widget;
- confidence interval and sample-size widget;
- CLT simulator.

These are teaching enhancements, not evidence-backed diagram details unless separately labelled.

---

# 18. Supplementary Sources Used

## Project sources used

- CCEA Further Mathematics Specification Map.
- Further Maths README Module Map.
- Further Maths Evidence Drop Checklist.
- CCEA ordinary Mathematics Specification Map.
- Ordinary A-Level Maths Bridge Spec Extracts.

## Lesson-specific evidence used

- `transcripts.md`, especially Estimators and Confidence Intervals videos.
- `Chapter_5_Estimation,_Confidence_Intervals_&_Tests_using_a_Normal_Distribution_📈_(Further_Statistics_2)_screenshots.pdf`.
- `S3-Chp3-EstimationConfidenceIntervals.pdf`.

## Cross-board source notes

The Dr Frost S3 PDF is not a CCEA authority. It is used only where CCEA confirms the content is on-spec.

## Evidence boundary statement

The core syllabus authority is the CCEA Further Mathematics `FA22-EST` boundary. Ordinary A-Level material is bridge context only. Off-spec testing material is excluded from core teaching.

---

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] I can calculate means from raw and frequency data.
- [ ] I can use \(\sum x\), \(\sum x^2\), \(\sum fx\), \(\sum fx^2\).
- [ ] I can work with \(X\sim N(\mu,\sigma^2)\).
- [ ] I can standardise using \(Z=(X-\mu)/\sigma\).

## Further Maths method

- [ ] I can distinguish population parameter from sample statistic.
- [ ] I can decide whether an expression is a statistic.
- [ ] I can define estimator and estimate.
- [ ] I can use \(\operatorname{Bias}(T)=E(T)-\theta\).
- [ ] I can prove \(E(\bar X)=\mu\).
- [ ] I can use \(\operatorname{Var}(\bar X)=\sigma^2/n\).
- [ ] I can use \(\operatorname{SE}(\bar X)=\sigma/\sqrt n\).
- [ ] I can calculate \(s^2=\frac{\sum(x_i-\bar x)^2}{n-1}\).

## CLT and confidence intervals

- [ ] I can state \(\bar X\approx N(\mu,\sigma^2/n)\) for \(n\ge30\).
- [ ] I know CLT describes \(\bar X\), not necessarily \(X\).
- [ ] I can use \(\bar x\pm z\sigma/\sqrt n\).
- [ ] I can use 1.96 for 95% and 2.5758 for 99%.
- [ ] I can interpret a confidence interval in context.
- [ ] I can round sample sizes up.

## Visual understanding

- [ ] I can explain why a sample statistic varies across samples.
- [ ] I can explain why \(\bar X\) has its own distribution.
- [ ] I can explain why the distribution of \(\bar X\) narrows as \(n\) grows.
- [ ] I can explain why a 95% interval uses tails of 2.5%.
- [ ] I can explain why interval width is twice the margin of error.
