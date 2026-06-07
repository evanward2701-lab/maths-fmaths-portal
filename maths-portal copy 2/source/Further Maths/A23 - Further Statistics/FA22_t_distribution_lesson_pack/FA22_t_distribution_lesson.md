# FA22-TDIST: The t-distribution

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FA22-TDIST` |
| Topic name | The t-distribution |
| Topic slug | `t_distribution` |
| Topic Pascal | `TDistribution` |
| Topic ID | `FA22TDistribution` |
| Lesson file name | `FA22_t_distribution_lesson.md` |
| Learning outcome IDs | `FA22-TDIST-LO001`, `FA22-TDIST-LO002`, `FA22-TDIST-LO003` |
| Bridge tags | `#Sampling`, `#NormalDistribution`, `#ZTests`, `#HypothesisTesting`, `#SampleVariance`, `#StandardError` |
| Topic tags | `#FA22`, `#TDIST`, `#Statistics`, `#TDistribution`, `#HypothesisTesting`, `#SectionC` |

## Student-facing lesson title

# The \(t\)-distribution and \(t\)-tests

This lesson is about what happens when you want to test a population mean but the population variance is unknown. In ordinary A-Level Statistics, the normal distribution was the familiar compass. In Further Statistics, the \(t\)-distribution appears when the compass needle wobbles because the sample is small and the standard deviation has to be estimated from the same sample.

---

# 2. Evidence Map

| Evidence source | Lesson role | Content used | Limitation |
|---|---|---|---|
| CCEA Further Mathematics specification map | Authority | Topic code, LO IDs, official wording, CCEA boundary | None identified |
| Further Maths README module map | Planning | Links `FA22-TDIST` to ordinary A-Level hypothesis testing, normal distribution and sampling | General project map, not topic-local |
| Further Maths evidence checklist | Process | Evidence logging, missing evidence and boundary-risk checks | General project checklist |
| Ordinary A-Level Maths bridge extracts | Bridge only | Sampling, normal distribution, hypothesis testing, uncertainty in variance | Not Further Maths authority |
| `t-Tests - Lesson.pdf` | Lesson-specific supporting source | \(z\)-test recap, sample standard deviation, \(t\)-distribution, degrees of freedom, one-sample \(t\), paired \(t\), non-paired example, calculator guidance | Dr Frost resource is not CCEA-specific; formula conflicts are logged |
| `transcripts.md` | Lesson-specific supporting source | Motivation, small-sample unknown variance, fatter tails, table use, one-sample tests, paired tests, pooled variance, two-sample tests, warnings | Transcript includes cross-topic confidence interval material |
| `Chapter_7_t-distribution_📈_(Further_Statistics_2)_screenshots.pdf` | Visual evidence | Visible screenshots show the Chapter 7 title slide, Guinness story, unknown variance plus large sample slide, formulas and annotations | Image-only; no uninspected visual detail is claimed |

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

The screenshot PDF visibly includes a slide titled **“FS2: Chapter 7, The \(t\)-distribution”**, with the Guinness/Gosset story and an image of Guinness. It also visibly includes the slide **“Unknown Variance + Large Sample Size”**, where the standardisation formula changes from using \(\sigma\) to using \(S\), and one screenshot shows the word “true” crossed out and replaced by a handwritten “good”. This warning is preserved in the lesson: replacing \(\sigma\) by \(S\) is an approximation that becomes good for large \(n\), not an exact truth for small samples.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| `FA22-TDIST-LO001` | demonstrate understanding of when it is appropriate to use the t-distribution | Explain unknown \(\sigma^2\), small sample, normal population, \(S\) replacing \(\sigma\), fatter tails, \(\nu\), and \(t_\nu\) critical values | CCEA map, transcript, Dr Frost slides | Core | Builds from \(z\)-scores, normal distribution, sample mean and hypothesis tests |
| `FA22-TDIST-LO002` | carry out a hypothesis test for the population mean using a small sample drawn from a normally distributed variable | Full one-sample \(t\)-test method and examples | CCEA map, transcript, Dr Frost slides | Core | Extends one-sample \(z\)-test for a mean |
| `FA22-TDIST-LO003` | formulate a hypothesis and carry out either a two-sample or paired-sample t-test as appropriate for the difference of the sample means, and demonstrate understanding of the conditions for these tests to be valid | Paired-test method using differences; two-sample method using pooled variance; conditions for validity | CCEA map, transcript, Dr Frost paired-test slides | Core; pooled variance route used for two-sample test | Extends difference-of-means and before/after comparison ideas |

---

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. decide when the \(t\)-distribution is appropriate;
2. explain why using \(S\) instead of \(\sigma\) changes the distribution of the test statistic;
3. use degrees of freedom \(\nu=n-1\) for a one-sample or paired-sample \(t\)-test;
4. carry out a one-sample \(t\)-test for a population mean;
5. carry out a paired-sample \(t\)-test by forming differences;
6. carry out a two-sample \(t\)-test for the difference of means using the pooled variance route where the required conditions are met;
7. state the conditions needed for the tests to be valid;
8. interpret the final conclusion in the context of the question.

## Bridge objectives

You should be able to connect this topic to ordinary A-Level Statistics by recalling:

1. the meaning of a \(z\)-score;
2. the normal standardisation formula;
3. how a hypothesis test uses \(H_0\), \(H_1\), a significance level and a critical region;
4. how \(\bar X\), \(s\), \(S^2\), \(\sigma\) and \(\mu\) differ;
5. why \(\bar X\) is a statistic but \(\mu\) is a population parameter.

## Exam technique objectives

You should be able to:

1. state hypotheses using population parameters, not sample values;
2. decide whether the test is one-tailed or two-tailed;
3. use the correct degrees of freedom;
4. avoid using a \(z\)-test when \(\sigma\) is unknown and the sample is small;
5. avoid treating paired data as independent samples;
6. state assumptions before or during a two-sample \(t\)-test;
7. make a final conclusion using cautious hypothesis-test language.

---

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should already be confident with mean, standard deviation, substitution into formulae, square roots, inequalities and interpreting values in context.

## Ordinary AS/A2 Mathematics foundations

You should already know the normal distribution, standardisation, inverse normal critical values, hypothesis tests for means where the population variance or standard deviation is known, sample means and sample standard deviations, significance levels, critical regions and the difference between a population parameter and a sample statistic.

## Previous Further Mathematics foundations

This lesson also leans on earlier FA22 Section C Statistics ideas: linear combinations of independent variables; sampling and estimation; \(S^2=\dfrac{\sum(X_i-\bar X)^2}{n-1}\) as an unbiased estimator of \(\sigma^2\); and standard error of the mean.

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Normal distribution | Standardise using \(Z=\dfrac{X-\mu}{\sigma}\) or \(Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\) | When \(\sigma\) is unknown, the denominator uses \(S\), giving \(T=\dfrac{\bar X-\mu}{S/\sqrt n}\) | \(S\) is calculated from the sample, so it varies from sample to sample |
| Hypothesis testing | Set up \(H_0\), \(H_1\), choose critical region, compare test statistic, conclude | Same logic, but use \(t_\nu\) instead of \(Z\) | Wrong distribution means wrong critical value |
| Sampling | A sample statistic estimates a population parameter | Small samples make uncertainty in \(S\) more visible, so the \(t\)-distribution has fatter tails | Small samples are more liable to extreme test statistics |
| Sample variance | Divide by \(n-1\) for the unbiased sample variance | The same loss of one degree of freedom appears as \(\nu=n-1\) | Using \(n\) instead of \(n-1\) damages both \(s\) and \(\nu\) |
| Difference of means | Compare two group means through \(\bar X-\bar Y\) | Use paired differences or pooled two-sample \(t\)-tests | Pairing must be recognised; otherwise the model is wrong |
| Calculator distribution work | Use normal distribution functions and inverse normal | Use \(t\)-distribution functions and inverse \(t\), where available | Calculator output cannot replace assumptions, hypotheses or context |

In ordinary A-Level Maths, this idea appeared as normal-distribution hypothesis testing: assume the null hypothesis, calculate a standardised value, compare it with a critical value, then make a decision.

In Further Maths, the same idea becomes more delicate. We no longer always know \(\sigma\), the population standard deviation. When the sample is small, the sample standard deviation \(S\) is not a stable replacement for \(\sigma\). The key upgrade is that the \(t\)-distribution accounts for this extra uncertainty.

The danger is that the method looks nearly identical to a \(z\)-test. In the formula, only one symbol changes, \(\sigma\) becomes \(S\), but the whole distribution changes from \(Z\) to \(T\).

---

# 6. Big Picture Explanation

The \(t\)-distribution exists because real data is often stingy.

In an ideal \(z\)-test, you know the population standard deviation \(\sigma\). That means the denominator in

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

is known. The only randomness comes from \(\bar X\).

But in real sampling, especially with small samples, you often do not know \(\sigma\). So you estimate it from the sample and use \(S\). That gives

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

Now both the numerator and denominator depend on the sample. The denominator is no longer a fixed measuring stick. It is a measuring stick made of jelly, firmer as \(n\) grows, wobblier when \(n\) is small. The \(t\)-distribution is the probability model that accounts for that wobble.

The evidence uses the story of William Sealy Gosset, who worked for Guinness Brewery in Dublin, as motivation. He needed methods for estimating means and variances using small samples from normally distributed populations. The historical story is useful for memory, but the examinable mathematics is this:

\[
\text{small sample}+\text{unknown population variance}+\text{normal population model}
\quad\Longrightarrow\quad
t\text{-distribution}.
\]

For small samples, the \(t\)-distribution has fatter tails than the standard normal distribution. This means extreme values are more likely than they would be under \(Z\). As the sample size becomes large,

\[
S\approx \sigma,
\]

so the \(t\)-distribution approaches the standard normal distribution.

---

# 7. Key Definitions and Notation

## Population mean

The population mean is denoted by

\[
\mu.
\]

It is the true mean of the whole population. In a hypothesis test, the null hypothesis often gives a claimed value for \(\mu\), such as

\[
H_0:\mu=150.
\]

## Sample mean

For a sample \(X_1,X_2,\ldots,X_n\), the sample mean is

\[
\bar X=\frac{1}{n}\sum_{i=1}^{n}X_i.
\]

For observed data, we often write the calculated sample mean as

\[
\bar x.
\]

## Population standard deviation

The population standard deviation is

\[
\sigma.
\]

If \(\sigma\) is known, normal \(z\)-methods may be available.

## Sample standard deviation

The sample standard deviation is

\[
S.
\]

For observed data, we often write the calculated sample standard deviation as

\[
s.
\]

The sample variance is

\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}.
\]

For observed data,

\[
s^2=\frac{\sum(x_i-\bar x)^2}{n-1}.
\]

## Standard error of the sample mean

If \(\sigma\) is known, the standard error of \(\bar X\) is

\[
\frac{\sigma}{\sqrt n}.
\]

If \(\sigma\) is unknown and estimated by \(S\), the estimated standard error is

\[
\frac{S}{\sqrt n}.
\]

For observed data,

\[
\frac{s}{\sqrt n}.
\]

## The \(t\)-statistic for one sample

For a one-sample test of a population mean,

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

For observed data and a null hypothesis value \(\mu_0\),

\[
t=\frac{\bar x-\mu_0}{s/\sqrt n}.
\]

## Degrees of freedom

The degrees of freedom are denoted by

\[
\nu.
\]

For a one-sample \(t\)-test,

\[
\nu=n-1.
\]

This is read as “nu equals \(n-1\)”.

## \(t_\nu\)-distribution

If \(T\) follows a \(t\)-distribution with \(\nu\) degrees of freedom, we write

\[
T\sim t_\nu.
\]

For a one-sample \(t\)-test,

\[
T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1},
\]

provided the required conditions are met.

## Paired differences

For paired data, define the difference for pair \(i\) by

\[
D_i=\text{after}_i-\text{before}_i
\]

or by another clearly stated convention.

The mean difference is

\[
\bar D=\frac{1}{n}\sum_{i=1}^{n}D_i.
\]

The sample standard deviation of the differences is

\[
S_D=\sqrt{\frac{\sum(D_i-\bar D)^2}{n-1}}.
\]

The paired \(t\)-statistic is

\[
T=\frac{\bar D-\mu_D}{S_D/\sqrt n}.
\]

Most paired tests use

\[
H_0:\mu_D=0.
\]

## Two-sample pooled variance

For two independent samples with sample sizes \(n_x,n_y\) and sample variances \(s_x^2,s_y^2\), the pooled variance is

\[
s_p^2=
\frac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}.
\]

This is used when the two population variances are assumed equal but unknown.

The corresponding two-sample test statistic is

\[
t=
\frac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}
{s_p\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}}.
\]

The degrees of freedom are

\[
\nu=n_x+n_y-2.
\]

---

# 8. Core Theory

## 8.1 Why the \(z\)-test is not enough

In ordinary A-Level Statistics, when the population standard deviation is known, the sample mean can be standardised by

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
\]

This works because \(\sigma\) is fixed. If

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right),
\]

then

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).
\]

**Bridge Note:** In ordinary A-Level Maths, we used the normal distribution as the probability engine for hypothesis tests. Here, Further Maths changes the engine because the population standard deviation is no longer known.

If \(\sigma\) is unknown, it is tempting to replace it with the sample standard deviation \(S\):

\[
\frac{\bar X-\mu}{S/\sqrt n}.
\]

For a large sample, this can be a good approximation because

\[
S\approx \sigma.
\]

But for a small sample, \(S\) can vary a lot from sample to sample. The denominator is not stable.

Therefore,

\[
\frac{\bar X-\mu}{S/\sqrt n}
\]

does not follow the standard normal distribution. It follows a \(t\)-distribution, assuming the original population is normal.

So the one-sample \(t\)-statistic is

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

## 8.2 The shape of the \(t\)-distribution

The \(t\)-distribution is symmetric about \(0\), shaped like the standard normal distribution, fatter in the tails for small degrees of freedom, and closer to the standard normal distribution as the sample size increases.

For small samples, the \(t\)-distribution has more probability in the tails because extreme values are more plausible when \(S\) is estimated from a small amount of data. The transcript explains this visually as taking probability from the middle hump and spreading more of it into the tails. That is why critical values for small-\(\nu\) \(t\)-distributions can be much larger in magnitude than normal critical values.

**Bridge Note:** In ordinary A-Level Maths, the standard normal curve \(Z\sim N(0,1)\) was fixed. In Further Maths, \(t_\nu\) is a family of distributions. The shape depends on \(\nu\), the degrees of freedom.

As

\[
\nu\to\infty,
\]

the \(t\)-distribution approaches the standard normal distribution:

\[
t_\nu\to N(0,1).
\]

## 8.3 Degrees of freedom

The degrees of freedom measure how many values are free to vary after a constraint has been imposed.

Suppose a sample has four values and the sample mean is known to be \(10\). Then the total of the four values must be

\[
4\times 10=40.
\]

The first three values can be chosen freely. For example, if the first three values are

\[
4,\quad 3,\quad 12,
\]

then the fourth value is forced by the total:

\[
4+3+12+x_4=40.
\]

So

\[
19+x_4=40,
\]

and therefore

\[
x_4=21.
\]

Only three values were free. So for \(n=4\),

\[
\nu=3.
\]

In general, for one-sample \(t\)-tests,

\[
\nu=n-1.
\]

**Bridge Note:** In ordinary A-Level Statistics, you met the sample variance formula

\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}.
\]

That \(n-1\) is not decorative algebra. It reflects that estimating \(\bar X\) uses up one degree of freedom.

## 8.4 Reading \(t\)-tables

The CCEA map states that percentage point tables for the \(t\)-distribution are included in the formula booklet.

A typical \(t\)-table gives upper-tail values. For example, for \(\nu=2\), if the table gives

\[
t=2.920
\]

under the \(0.05\) column, this means

\[
P(T>2.920)=0.05.
\]

Since the \(t\)-distribution is symmetric,

\[
P(T<-2.920)=0.05.
\]

Therefore,

\[
P(T<2.920)=1-0.05=0.95.
\]

Similarly, if for \(\nu=2\)

\[
P(T>1.886)=0.10,
\]

then by symmetry

\[
P(T<-1.886)=0.10.
\]

This gives

\[
P(T< -1.886)=0.10.
\]

**Bridge Note:** This is the same tail-area thinking used with inverse normal values. The new part is that the row depends on \(\nu\).

## 8.5 One-sample \(t\)-test for a population mean

A one-sample \(t\)-test is used when:

1. the test concerns a population mean \(\mu\);
2. the sample size is small;
3. the population variance \(\sigma^2\) is unknown;
4. the sample is drawn from a normally distributed variable.

The test statistic is

\[
t=\frac{\bar x-\mu_0}{s/\sqrt n},
\]

where \(\bar x\) is the sample mean, \(\mu_0\) is the value of \(\mu\) assumed under \(H_0\), \(s\) is the sample standard deviation and \(n\) is the sample size. The degrees of freedom are

\[
\nu=n-1.
\]

### Method

1. State hypotheses in terms of the population mean.
2. Calculate \(\bar x\), \(s\) and \(n\).
3. Calculate \(t=\dfrac{\bar x-\mu_0}{s/\sqrt n}\).
4. Find the critical value from \(t_{n-1}\).
5. Compare the observed value with the critical region.
6. Conclude in context.

For a left-tailed test:

\[
H_0:\mu=\mu_0,\qquad H_1:\mu<\mu_0.
\]

For a right-tailed test:

\[
H_0:\mu=\mu_0,\qquad H_1:\mu>\mu_0.
\]

For a two-tailed test:

\[
H_0:\mu=\mu_0,\qquad H_1:\mu\ne\mu_0.
\]

**Bridge Note:** In ordinary A-Level Maths, the standardisation formula measured how far a value was from the mean in standard deviations. Here, the same idea measures how far the sample mean is from the null-hypothesis mean in estimated standard errors.

## 8.6 Paired-sample \(t\)-test

A paired-sample \(t\)-test is used when the data comes in pairs: the same people measured before and after a treatment, the same roads measured before and after a campaign, or the same objects measured using two different methods.

Let

\[
D_i=\text{second measurement}_i-\text{first measurement}_i.
\]

Then calculate

\[
\bar d=\frac{1}{n}\sum d_i
\]

and

\[
s_d^2=\frac{\sum(d_i-\bar d)^2}{n-1}.
\]

The test statistic is

\[
t=\frac{\bar d-\mu_{D,0}}{s_d/\sqrt n}.
\]

Most paired tests use

\[
H_0:\mu_D=0,
\]

because “no mean change” means the mean difference is zero. The degrees of freedom are

\[
\nu=n-1.
\]

**Bridge Note:** In ordinary statistics, paired comparisons often looked like “before versus after”. Further Maths turns this into a one-sample \(t\)-test on the difference variable \(D\). Once the differences are formed, the machine is the same.

## 8.7 Non-paired two-sample \(t\)-test using pooled variance

A two-sample \(t\)-test is used when two independent samples are taken from two populations and we want to test a difference between population means.

Let the two populations have means

\[
\mu_x,\quad \mu_y.
\]

Let the samples have sizes

\[
n_x,\quad n_y,
\]

sample means

\[
\bar x,\quad \bar y,
\]

and sample variances

\[
s_x^2,\quad s_y^2.
\]

For the CCEA boundary in this lesson, use the pooled variance route where appropriate. The supplied CCEA map notes that the formula for pooled variance will be given.

The pooled variance is

\[
s_p^2=
\frac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}.
\]

The pooled standard deviation is

\[
s_p=\sqrt{s_p^2}.
\]

The test statistic is

\[
t=
\frac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}
{s_p\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}}.
\]

The degrees of freedom are

\[
\nu=n_x+n_y-2.
\]

### Conditions for the pooled two-sample \(t\)-test

1. the samples are independent;
2. the populations are normally distributed;
3. the population variances are unknown but can be assumed equal;
4. the sample sizes are small enough that a \(t\)-model is required rather than a large-sample normal approximation.

If testing whether the means are equal:

\[
H_0:\mu_x-\mu_y=0.
\]

If testing whether \(X\) has a larger mean than \(Y\):

\[
H_1:\mu_x-\mu_y>0.
\]

If testing whether \(X\) has a smaller mean than \(Y\):

\[
H_1:\mu_x-\mu_y<0.
\]

If testing whether the means differ:

\[
H_1:\mu_x-\mu_y\ne 0.
\]

If the question says “does \(\mu_x\) exceed \(\mu_y\) by more than \(4\)?”, then the hypotheses become

\[
H_0:\mu_x-\mu_y=4,
\]

\[
H_1:\mu_x-\mu_y>4.
\]

Then

\[
(\mu_x-\mu_y)_0=4
\]

is used in the test statistic.

**Bridge Note:** In ordinary A-Level Statistics, comparing means often used \(\bar X-\bar Y\). Further Maths keeps the same structure but changes the denominator because the variances are unknown and estimated.

## 8.8 Why paired and two-sample tests are not interchangeable

Paired data has a natural link between values:

\[
(\text{before}_1,\text{after}_1),\quad
(\text{before}_2,\text{after}_2),\quad
\ldots
\]

The differences are meaningful:

\[
d_i=\text{after}_i-\text{before}_i.
\]

Independent two-sample data has no such pairing:

\[
X_1,\ldots,X_{n_x}
\]

and

\[
Y_1,\ldots,Y_{n_y}.
\]

There is no meaningful \(X_i-Y_i\) unless the data are genuinely paired. A paired test eliminates differences between individuals and focuses on change. A non-paired test compares group means.

## 8.9 Summary of the core decision rules

| Situation | Use | Test statistic | Degrees of freedom |
|---|---|---|---|
| One sample, testing \(\mu\), \(\sigma\) known | \(z\)-test, bridge only | \(z=\dfrac{\bar x-\mu_0}{\sigma/\sqrt n}\) | Not \(t\) |
| One sample, testing \(\mu\), \(\sigma\) unknown, small sample, normal variable | One-sample \(t\)-test | \(t=\dfrac{\bar x-\mu_0}{s/\sqrt n}\) | \(\nu=n-1\) |
| Paired measurements | Paired \(t\)-test on differences | \(t=\dfrac{\bar d-\mu_{D,0}}{s_d/\sqrt n}\) | \(\nu=n-1\) |
| Two independent samples, equal unknown variances, normal populations | Pooled two-sample \(t\)-test | \(t=\dfrac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}{s_p\sqrt{1/n_x+1/n_y}}\) | \(\nu=n_x+n_y-2\) |

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22TDistributionMermaid-001 | Source: CCEA FA22-TDIST learning outcomes + lesson evidence | Insert from mermaid/FA22TDistributionMermaid-001.md | Purpose: Help the student decide whether a question needs a one-sample t-test, paired t-test, two-sample pooled t-test or ordinary bridge z-test.]

The visual must show a decision route from a question involving a mean, through known or unknown \(\sigma\), then through one sample, paired sample or two independent samples. It must include the formulas

\[
z=\frac{\bar x-\mu_0}{\sigma/\sqrt n},\qquad
 t=\frac{\bar x-\mu_0}{s/\sqrt n},\qquad
 t=\frac{\bar d-\mu_{D,0}}{s_d/\sqrt n},
\]

and

\[
t=
\frac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}
{s_p\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}}.
\]

[VISUAL PLACEHOLDER: FA22TDistributionSVG-001 | Source: Teacher transcript + Dr Frost t-distribution slides | Insert from svg/FA22TDistributionSVG-001.svg | Purpose: Show why t_nu has fatter tails than N(0,1), especially for small nu.]

The visual must show a central vertical line at \(0\), a standard normal curve labelled \(Z\sim N(0,1)\), at least two \(t\)-curves such as \(t_2\) and \(t_{10}\), fatter tails labelled “extra uncertainty from estimating \(\sigma\) using \(S\)”, and a note \(\nu\uparrow\Rightarrow t_\nu\to N(0,1)\).

[VISUAL PLACEHOLDER: FA22TDistributionSVG-002 | Source: Dr Frost t-table slide + transcript table explanation | Insert from svg/FA22TDistributionSVG-002.svg | Purpose: Teach upper-tail table reading and symmetry.]

The visual must show row \(\nu=2\), column \(0.05\), value \(2.920\), the shaded right tail \(P(T>2.920)=0.05\), the symmetry result \(P(T<-2.920)=0.05\), and \(P(T<2.920)=0.95\).

[VISUAL PLACEHOLDER: FA22TDistributionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22TDistributionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

The visual must show the upgrade

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

becoming

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

It must label \(\sigma\) as population standard deviation and \(S\) as sample standard deviation.

[VISUAL PLACEHOLDER: FA22TDistributionTikZ-001 | Source: Core hypothesis-test method | Insert from tikz/FA22TDistributionTikZ-001.tex | Purpose: Show one-tailed and two-tailed t-test critical regions.]

The TikZ diagram must show left-tailed, right-tailed and two-tailed tests with \(0\), critical values, rejection regions, observed \(t\)-statistic markers and conclusion arrows.

[VISUAL PLACEHOLDER: FA22TDistributionTikZ-002 | Source: Dr Frost paired/non-paired comparison slide + transcript | Insert from tikz/FA22TDistributionTikZ-002.tex | Purpose: Show why paired data becomes a one-sample test on differences.]

The diagram must compare paired data, where each subject has before and after values, with independent samples, where there is no natural one-to-one pairing. It must include

\[
D_i=\text{after}_i-\text{before}_i,
\]

and

\[
t=\frac{\bar d-0}{s_d/\sqrt n}.
\]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22TDistributionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22TDistributionWidget-001.html | Purpose: Let the student practise the complete one-sample t-test workflow.]

Student inputs \(n\), \(\bar x\), \(s\), \(\mu_0\), \(\alpha\), and test direction. The widget displays \(\nu=n-1\) and \(t=\dfrac{\bar x-\mu_0}{s/\sqrt n}\), checks assumptions and gives critical-region feedback.

[INTERACTIVE PLACEHOLDER: FA22TDistributionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22TDistributionWidget-002.html | Purpose: Convert paired data into differences and perform a paired t-test.]

Student inputs before-values, after-values, a difference convention, significance level and test direction. The widget displays \(d_i\), \(\sum d_i\), \(\sum d_i^2\), \(\bar d\), \(s_d^2\), \(s_d\), \(\nu=n-1\), and the observed \(t\)-statistic.

[INTERACTIVE PLACEHOLDER: FA22TDistributionWidget-003 | Source: AI-proposed teaching enhancement based on CCEA FA22-TDIST-LO003 | Insert from widgets/FA22TDistributionWidget-003.html | Purpose: Practise the CCEA pooled-variance two-sample t-test.]

Student inputs \(n_x,n_y,\bar x,\bar y,s_x^2,s_y^2,(\mu_x-\mu_y)_0\), significance level and test direction. The widget displays \(s_p^2\), the pooled two-sample \(t\)-statistic and \(\nu=n_x+n_y-2\). It includes an assumption checklist for independent samples, normal populations and equal unknown variances.

---

# 11. Worked Examples

## Worked Example 1: One-sample \(t\)-test for a class mean

**Evidence source:** Dr Frost t-tests slide on conducting a \(t\)-test for a sample mean.  
**On-spec status:** Core `FA22-TDIST-LO002`.  
**Ordinary Maths idea used:** One-sample \(z\)-test for a mean.  
**Further Maths upgrade:** Use \(s\) and \(t_{n-1}\) because the population standard deviation is unknown and the sample is small.

### Question

The mean height of students in a class is thought to be \(1.5\text{ m}\). The heights of a sample of \(3\) students in that class are recorded as:

\[
1.3\text{ m},\quad 1.35\text{ m},\quad 1.4\text{ m}.
\]

Conduct a \(t\)-test, at the \(1\%\) significance level, to determine if the mean height of the class is less than \(1.5\text{ m}\).

### Solution

Let \(\mu\) be the population mean height. The hypotheses are

\[
H_0:\mu=1.5,
\]

\[
H_1:\mu<1.5.
\]

Calculate the sample mean:

\[
\bar x=\frac{1.3+1.35+1.4}{3}=\frac{4.05}{3}=1.35.
\]

The slide gives

\[
s=0.05.
\]

The \(t\)-statistic is

\[
t=\frac{\bar x-\mu_0}{s/\sqrt n}.
\]

Substitute:

\[
t=\frac{1.35-1.5}{0.05/\sqrt3}.
\]

Work numerator first:

\[
1.35-1.5=-0.15.
\]

So

\[
t=\frac{-0.15}{0.05/\sqrt3}.
\]

Since

\[
\frac{0.05}{\sqrt3}\approx0.0288675,
\]

\[
t\approx\frac{-0.15}{0.0288675}=-5.196.
\]

Degrees of freedom:

\[
\nu=n-1=3-1=2.
\]

For a \(1\%\) left-tailed test with \(\nu=2\), the critical value is

\[
-6.964.
\]

The critical region is

\[
t<-6.964.
\]

The observed value is

\[
t=-5.196.
\]

Compare:

\[
-5.196>-6.964.
\]

Therefore the observed value is not in the critical region. Do not reject \(H_0\). There is insufficient evidence, at the \(1\%\) significance level, that the mean height of students in the class is less than \(1.5\text{ m}\).

### Teaching note

The sample mean \(1.35\) is visibly below \(1.5\), but the sample is tiny and the \(1\%\) test is strict. Statistics asks whether the difference is large enough compared with the uncertainty.

## Worked Example 2: One-sample \(t\)-test for cats on Aoshima

**Evidence source:** Dr Frost test-your-understanding slide.  
**On-spec status:** Core `FA22-TDIST-LO002`.  
**Ordinary Maths idea used:** One-sample hypothesis test.  
**Further Maths upgrade:** Use \(t_3\) because \(n=4\) and \(\sigma\) is unknown.

### Question

The historical mean weight of cats on the island of Aoshima in Japan is \(6.5\text{ kg}\). A sample of \(4\) cats is caught and their weights are recorded:

\[
6\text{ kg},\quad 7\text{ kg},\quad 7.5\text{ kg},\quad 9\text{ kg}.
\]

Conduct a \(t\)-test, at the \(10\%\) significance level, to determine if the mean weight of cats on the island is more than \(6.5\text{ kg}\).

### Solution

Let \(\mu\) be the population mean weight of cats on the island.

\[
H_0:\mu=6.5,
\]

\[
H_1:\mu>6.5.
\]

This is a right-tailed test.

\[
\bar x=\frac{6+7+7.5+9}{4}=\frac{29.5}{4}=7.375.
\]

The slide gives

\[
s=1.25.
\]

\[
t=\frac{7.375-6.5}{1.25/\sqrt4}.
\]

\[
7.375-6.5=0.875,
\]

and

\[
\frac{1.25}{\sqrt4}=\frac{1.25}{2}=0.625.
\]

Therefore

\[
t=\frac{0.875}{0.625}=1.4.
\]

Degrees of freedom:

\[
\nu=n-1=4-1=3.
\]

For a right-tailed \(10\%\) test with \(\nu=3\), the critical value is

\[
1.6377.
\]

The critical region is

\[
t>1.6377.
\]

But

\[
1.4<1.6377.
\]

So the observed value is not in the critical region. Do not reject \(H_0\). There is insufficient evidence, at the \(10\%\) significance level, that the mean weight of cats on Aoshima is more than \(6.5\text{ kg}\).

## Worked Example 3: One-sample \(t\)-test for jars of jam

**Evidence source:** Teacher transcript, one-sample \(t\)-test example.  
**On-spec status:** Core `FA22-TDIST-LO002`.  
**Ordinary Maths idea used:** One-sample \(z\)-test for a mean.  
**Further Maths upgrade:** Use \(s\) and \(t_7\). The transcript emphasises that the standard deviation comes from the observed sample, not from the whole population.

### Question

A shopkeeper sells jars of jam. The weights of the jars of jam are normally distributed with a claimed mean of \(150\text{ g}\). A customer complains that the mean weight of \(8\) jars she bought was only \(147\text{ g}\).

An estimate for the standard deviation of the weights of the \(8\) jars of jam, calculated from the \(8\) observations, was \(2\text{ g}\).

Test, at the \(5\%\) significance level, whether the customer’s belief that the mean weight is less than \(150\text{ g}\) is supported.

### Solution

Let

\[
\mu=\text{the population mean weight of jars of jam in grams}.
\]

\[
H_0:\mu=150,
\]

\[
H_1:\mu<150.
\]

Record the sample information:

\[
n=8,\qquad \bar x=147,\qquad s=2.
\]

The observed \(t\)-statistic is

\[
t=\frac{147-150}{2/\sqrt8}.
\]

\[
147-150=-3.
\]

Since

\[
\sqrt8=2\sqrt2,
\]

\[
\frac{2}{\sqrt8}=\frac{2}{2\sqrt2}=\frac{1}{\sqrt2}.
\]

So

\[
t=\frac{-3}{1/\sqrt2}=-3\sqrt2\approx -4.2426.
\]

Degrees of freedom:

\[
\nu=n-1=8-1=7.
\]

For a \(5\%\) left-tailed test with \(\nu=7\), the critical value is

\[
-1.895.
\]

The critical region is

\[
t<-1.895.
\]

Since

\[
-4.2426<-1.895,
\]

the observed value is in the critical region. Reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, to support the customer’s belief that the mean weight of jars of jam is less than \(150\text{ g}\).

## Worked Example 4: One-sample two-tailed \(t\)-test for concrete strength

**Evidence source:** Teacher transcript, concrete manufacturer example.  
**On-spec status:** Core `FA22-TDIST-LO002`.  
**Ordinary Maths idea used:** Two-tailed hypothesis test.  
**Further Maths upgrade:** Calculate \(s\) from summary statistics and use \(t_{11}\).

### Question

A concrete manufacturer tests cubes of its concrete at regular intervals. Their compressive strengths are determined. The mean value of the strength is required to be \(0.47\). A new supplier of cement offers to supply the firm at a cheaper rate than the present supplier. A trial bag of cement is used to make \(12\) concrete cubes. Upon testing, these cubes are found to have strengths \(x\) such that

\[
\sum x=5.52
\]

and

\[
\sum x^2=2.542.
\]

Assume the strengths are normally distributed. Test, at the \(5\%\) significance level, whether the new cement has altered the mean strength of the concrete. Make a recommendation to the manufacturer.

### Solution

Let

\[
\mu=\text{the population mean compressive strength using the new cement}.
\]

The test asks whether the mean has altered, so this is two-tailed:

\[
H_0:\mu=0.47,
\]

\[
H_1:\mu\ne0.47.
\]

Calculate the sample mean:

\[
\bar x=\frac{\sum x}{n}=\frac{5.52}{12}=0.46.
\]

Use

\[
s^2=\frac{\sum x^2-n\bar x^2}{n-1}.
\]

Substitute:

\[
s^2=\frac{2.542-12(0.46)^2}{12-1}.
\]

\[
0.46^2=0.2116,
\]

\[
12(0.46)^2=12(0.2116)=2.5392.
\]

So

\[
s^2=\frac{2.542-2.5392}{11}=\frac{0.0028}{11}=0.000254545\ldots
\]

Therefore

\[
s=\sqrt{0.000254545\ldots}=0.01595\ldots
\]

The observed \(t\)-statistic is

\[
t=\frac{0.46-0.47}{0.01595\ldots/\sqrt{12}}\approx -2.1712.
\]

Degrees of freedom:

\[
\nu=n-1=12-1=11.
\]

The test is two-tailed at the \(5\%\) significance level, so each tail has \(2.5\%\). Using \(t_{11}\),

\[
t_{\text{critical}}=\pm 2.201.
\]

The critical regions are

\[
t<-2.201\quad \text{or}\quad t>2.201.
\]

Since

\[
-2.1712>-2.201,
\]

the observed value is not in the critical region. Do not reject \(H_0\). There is insufficient evidence, at the \(5\%\) significance level, that the new cement has altered the mean strength of the concrete.

Since there is insufficient evidence that the mean strength has changed, and the new supplier is cheaper, it would be reasonable to consider changing supplier. However, the observed statistic was very close to the critical region, so taking a further sample for testing may be wise.

## Worked Example 5: Paired \(t\)-test for reaction times after alcohol

**Evidence source:** Teacher transcript, paired \(t\)-test example.  
**On-spec status:** Core `FA22-TDIST-LO003`.  
**Ordinary Maths idea used:** Compare before and after.  
**Further Maths upgrade:** Use paired differences and test the population mean difference.

### Question

In an experiment to test the effects of alcohol on reaction times, a group of \(10\) students took part. Students reacted to a light by pushing a switch. After each student had drunk one pint of beer, the experiment was repeated.

Test, at the \(5\%\) significance level, whether the consumption of a pint of beer increased students’ reaction times.

The transcript gives the summary information for the differences:

\[
n=10,\qquad \sum d=1.2,\qquad \sum d^2=0.48.
\]

The teacher defines the differences so that a positive difference means reaction time increased.

### Solution

Let

\[
D=\text{reaction time after beer}-\text{reaction time before beer}.
\]

If beer increases reaction time, then \(\mu_D>0\). Hence

\[
H_0:\mu_D=0,
\]

\[
H_1:\mu_D>0.
\]

Calculate the mean difference:

\[
\bar d=\frac{\sum d}{n}=\frac{1.2}{10}=0.12.
\]

Calculate the sample variance of the differences:

\[
s_d^2=\frac{\sum d^2-n\bar d^2}{n-1}
=\frac{0.48-10(0.12)^2}{10-1}.
\]

\[
0.12^2=0.0144,
\]

\[
10(0.12)^2=0.144.
\]

So

\[
s_d^2=\frac{0.48-0.144}{9}=\frac{0.336}{9}=0.037333\ldots
\]

\[
s_d=\sqrt{0.037333\ldots}=0.1932\ldots
\]

The \(t\)-statistic is

\[
t=\frac{\bar d-0}{s_d/\sqrt n}
=\frac{0.12}{0.1932\ldots/\sqrt{10}}.
\]

Since

\[
\frac{0.1932\ldots}{\sqrt{10}}\approx0.06109,
\]

\[
t\approx\frac{0.12}{0.06109}=1.9640.
\]

Degrees of freedom:

\[
\nu=n-1=10-1=9.
\]

For a right-tailed \(5\%\) test with \(\nu=9\), the critical value is

\[
1.833.
\]

The critical region is

\[
t>1.833.
\]

Since

\[
1.9640>1.833,
\]

the observed value is in the critical region. Reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, that consuming a pint of beer increased the students’ reaction times.

## Worked Example 6: Paired \(t\)-test for two hardness measurement methods

**Evidence source:** Teacher transcript, paired \(t\)-test test-yourself example.  
**On-spec status:** Core `FA22-TDIST-LO003`.  
**Ordinary Maths idea used:** Compare two measurement methods.  
**Further Maths upgrade:** Use paired differences because each metal specimen is measured by both methods.

### Question

Two methods are used to measure the Brinell hardness of metals. Readings are taken using each method for \(8\) different metal specimens. Use a paired \(t\)-test at the \(5\%\) significance level to test whether there is a difference in the readings given by the two methods.

The transcript gives the differences:

\[
2,\ -1,\ 1,\ 3,\ 2,\ 0,\ 1,\ 1.
\]

So

\[
\sum d=9,\qquad \sum d^2=21.
\]

### Solution

Let

\[
D=\text{reading from method 2}-\text{reading from method 1}.
\]

\[
H_0:\mu_D=0,
\]

\[
H_1:\mu_D\ne0.
\]

\[
\bar d=\frac{\sum d}{n}=\frac{9}{8}=1.125.
\]

\[
s_d^2=\frac{\sum d^2-n\bar d^2}{n-1}
=\frac{21-8(1.125)^2}{8-1}.
\]

\[
1.125^2=1.265625,
\]

\[
8(1.125)^2=10.125.
\]

So

\[
s_d^2=\frac{21-10.125}{7}=\frac{10.875}{7}=1.553571\ldots
\]

\[
s_d=\sqrt{1.553571\ldots}=1.2464\ldots
\]

\[
t=\frac{1.125}{1.2464\ldots/\sqrt8}\approx2.5529.
\]

Degrees of freedom:

\[
\nu=8-1=7.
\]

For a two-tailed \(5\%\) test, using \(t_7\),

\[
t_{\text{critical}}=\pm2.365.
\]

Since

\[
2.5529>2.365,
\]

the observed value is in the critical region. Reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, that there is a difference in the readings given by the two methods.

## Worked Example 7: Paired \(t\)-test exam-style question on two papers

**Evidence source:** Teacher transcript, exam-question section.  
**On-spec status:** Core `FA22-TDIST-LO003`.  
**Ordinary Maths idea used:** Paired comparison.  
**Further Maths upgrade:** Test whether the mean difference is zero.

### Question

Alexa believes that students are equally likely to achieve the same percentage score on each of two tests, Paper 1 and Paper 2. She randomly selects \(8\) students and gives each student both papers.

The paired differences are:

\[
-6,\ 6,\ -12,\ -6,\ 4,\ -1,\ -7,\ -14.
\]

Test, at the \(1\%\) significance level, whether or not there is evidence to support Alexa’s belief.

The transcript records:

\[
\sum d=-36,\qquad \sum d^2=514.
\]

### Solution

Let

\[
D=\text{Paper 2 score}-\text{Paper 1 score}.
\]

\[
H_0:\mu_D=0,
\]

\[
H_1:\mu_D\ne0.
\]

\[
\bar d=\frac{-36}{8}=-4.5.
\]

\[
s_d^2=\frac{514-8(-4.5)^2}{8-1}.
\]

Since

\[
(-4.5)^2=20.25,
\]

\[
8(-4.5)^2=162.
\]

So

\[
s_d^2=\frac{514-162}{7}=\frac{352}{7}=50.285714\ldots
\]

\[
s_d=\sqrt{50.285714\ldots}=7.09124\ldots
\]

\[
t=\frac{-4.5}{7.09124\ldots/\sqrt8}\approx -1.7949.
\]

Degrees of freedom:

\[
\nu=8-1=7.
\]

For a two-tailed \(1\%\) test, each tail has \(0.5\%\). Using \(t_7\),

\[
t_{\text{critical}}=\pm3.499.
\]

Since

\[
-1.7949>-3.499,
\]

the observed value is not in the critical region. Do not reject \(H_0\). There is insufficient evidence, at the \(1\%\) significance level, that the mean percentage scores on the two papers are different. Therefore, there is evidence consistent with Alexa’s belief that students are equally likely to achieve the same percentage score on each paper.

## Worked Example 8: Pooled sample variance

**Evidence source:** Teacher transcript, pooled sample variance section.  
**On-spec status:** Supports core `FA22-TDIST-LO003`.  
**Ordinary Maths idea used:** Sample variance.  
**Further Maths upgrade:** Combine two sample variances to estimate a common unknown population variance.

### Question

A sample of size \(15\) from one population gives an unbiased estimate of the population variance of \(9.47\). A second random sample of size \(12\) is taken from a different population that has the same variance. It gives an unbiased estimate of the variance of \(13.84\). Calculate an unbiased estimate of the common population variance using both samples.

### Solution

\[
n_x=15,\qquad s_x^2=9.47,
\]

\[
n_y=12,\qquad s_y^2=13.84.
\]

Use the pooled variance formula:

\[
s_p^2=\frac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}.
\]

Substitute:

\[
s_p^2=\frac{(15-1)(9.47)+(12-1)(13.84)}{15+12-2}.
\]

\[
s_p^2=\frac{14(9.47)+11(13.84)}{25}.
\]

\[
14(9.47)=132.58,
\]

\[
11(13.84)=152.24.
\]

So

\[
s_p^2=\frac{132.58+152.24}{25}=\frac{284.82}{25}=11.3928.
\]

\[
\boxed{s_p^2=11.3928}\qquad \text{or}\qquad \boxed{s_p^2\approx 11.39}.
\]

## Worked Example 9: Two-sample pooled \(t\)-test for class results

**Evidence source:** Teacher transcript, hypothesis testing for difference between means.  
**On-spec status:** Core `FA22-TDIST-LO003`.  
**Ordinary Maths idea used:** Difference of sample means.  
**Further Maths upgrade:** Unknown but equal variances, small samples, pooled variance and \(t_{n_x+n_y-2}\).

### Question

Two groups of students, \(X\) and \(Y\), were taught by different teachers. At the end of the course, a random sample of students from each class was selected and given a test out of \(50\) marks.

Summary statistics:

\[
n_x=9,\qquad \bar x=38.67,\qquad s_x^2=23.0,
\]

\[
n_y=7,\qquad \bar y=40.286,\qquad s_y^2=15.9.
\]

Test, at the \(10\%\) significance level, whether or not there is a significant difference between the population mean test scores.

### Solution

Assume the two samples are independent, the two populations are normally distributed, and the two population variances are equal but unknown.

Let

\[
\mu_x=\text{population mean score for class }X,
\]

\[
\mu_y=\text{population mean score for class }Y.
\]

\[
H_0:\mu_x-\mu_y=0,
\]

\[
H_1:\mu_x-\mu_y\ne0.
\]

Calculate the pooled variance:

\[
s_p^2=\frac{(9-1)(23.0)+(7-1)(15.9)}{9+7-2}.
\]

\[
s_p^2=\frac{8(23.0)+6(15.9)}{14}.
\]

\[
8(23.0)=184.0,
\]

\[
6(15.9)=95.4.
\]

So

\[
s_p^2=\frac{184.0+95.4}{14}=\frac{279.4}{14}=19.95714286\ldots
\]

The two-sample pooled \(t\)-statistic is

\[
t=\frac{(\bar x-\bar y)-0}{\sqrt{s_p^2\left(\frac{1}{n_x}+\frac{1}{n_y}\right)}}.
\]

\[
t=\frac{38.67-40.286}{\sqrt{19.95714286\ldots\left(\frac{1}{9}+\frac{1}{7}\right)}}.
\]

\[
38.67-40.286=-1.616.
\]

\[
\frac{1}{9}+\frac{1}{7}=\frac{7}{63}+\frac{9}{63}=\frac{16}{63}.
\]

So the denominator is

\[
\sqrt{19.95714286\ldots\times\frac{16}{63}}\approx\sqrt{5.06848}\approx2.25133.
\]

Therefore

\[
t\approx\frac{-1.616}{2.25133}=-0.71913.
\]

Degrees of freedom:

\[
\nu=n_x+n_y-2=9+7-2=14.
\]

The test is two-tailed at the \(10\%\) level, so each tail has \(5\%\). Using \(t_{14}\),

\[
t_{\text{critical}}=\pm1.761.
\]

Since

\[
-1.761<-0.71913<1.761,
\]

the observed value is not in the critical region. Do not reject \(H_0\). There is insufficient evidence, at the \(10\%\) significance level, that there is a difference between the population mean test scores of class \(X\) and class \(Y\).

---

# 12. Common Mistakes and Exam Traps

## 12.1 Using a \(z\)-test when \(\sigma\) is unknown

The ordinary Maths habit is

\[
z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}.
\]

That only works when \(\sigma\) is known. For this topic, if the population standard deviation is unknown and the sample is small, use

\[
t=\frac{\bar x-\mu_0}{s/\sqrt n}.
\]

## 12.2 Treating \(S\) as if it were fixed

The sample standard deviation \(S\) is calculated from the sample. For a small sample, it can vary considerably. That is why the \(t\)-distribution is needed. Do not write

\[
\frac{\bar X-\mu}{S/\sqrt n}\sim N(0,1)
\]

for a small sample. The correct model is

\[
\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1},
\]

assuming the conditions hold.

## 12.3 Forgetting the normality condition

For small-sample \(t\)-tests, the source population must be modelled as normally distributed. This condition matters because small samples do not allow you to lean comfortably on the central limit theorem.

## 12.4 Wrong degrees of freedom

For one sample:

\[
\nu=n-1.
\]

For paired data:

\[
\nu=n-1,
\]

where \(n\) is the number of pairs.

For two independent samples with pooled variance:

\[
\nu=n_x+n_y-2.
\]

Do not use \(\nu=n\) or \(\nu=n_x+n_y-1\).

## 12.5 Confusing paired and independent samples

If the same subject or object is measured twice, the data are paired. Use differences:

\[
D_i=\text{second}_i-\text{first}_i.
\]

Do not use a two-sample test if the measurements are naturally paired.

## 12.6 Forgetting to define the difference direction

If you define

\[
D=\text{after}-\text{before},
\]

then an increase means

\[
\mu_D>0.
\]

If you define

\[
D=\text{before}-\text{after},
\]

then an increase after the event means

\[
\mu_D<0.
\]

The arithmetic and the hypothesis must use the same direction.

## 12.7 Splitting the significance level incorrectly

For a two-tailed \(5\%\) test, \(2.5\%\) goes in each tail. For a one-tailed \(5\%\) test, \(5\%\) goes in one tail. A two-tailed test at \(10\%\) uses \(5\%\) in each tail.

## 12.8 Saying “accept \(H_0\)” carelessly

A safer CCEA-style conclusion is:

```text
Do not reject H0.
There is insufficient evidence that ...
```

Do not say:

```text
H0 is definitely true.
```

Hypothesis tests do not prove \(H_0\).

## 12.9 Ignoring context in the final sentence

A final answer like \(t=-0.719\) is not enough. The conclusion must say what this means in the problem context.

## 12.10 Pooling variances without checking assumptions

The pooled two-sample \(t\)-test assumes equal population variances. Use

\[
s_p^2=\frac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}
\]

only when equal variances are assumed or justified.

## 12.11 Treating confidence intervals as core TDIST content without checking the LO

The supplied transcript contains \(t\)-based confidence intervals. They are mathematically connected to \(t\)-methods, but the official `FA22-TDIST` learning outcomes supplied for this lesson focus on when to use \(t\), hypothesis tests for one population mean, and paired and two-sample \(t\)-tests for differences of means. So confidence intervals are logged as enrichment or cross-topic estimation material, not core TDIST teaching.

## 12.12 Calculator trap: tail direction

When using a calculator for \(t\)-probabilities or inverse \(t\), the tail direction must match the hypothesis.

---

# 13. Practice Questions

All questions in this section are **generated practice questions**. They are not claimed to be CCEA past-paper or textbook questions. Use \(t\)-tables or a calculator where needed. Unless otherwise stated, assume any population being sampled is normally distributed.

## 13.1 Basic fluency questions

### Question 1: Choosing the correct distribution

For each situation, state whether the method should use \(Z\) or \(T\). If \(T\), state the degrees of freedom.

**(a)** A sample of \(12\) items is taken from a normally distributed population. The population standard deviation is unknown.

**(b)** A sample of \(40\) items is taken from a population. The population standard deviation is known.

**(c)** A paired before-and-after experiment is carried out on \(9\) people. The differences are assumed to be normally distributed.

**(d)** Two independent small samples are taken from normally distributed populations with equal unknown variances. The sample sizes are \(8\) and \(11\).

### Question 2: Reading the \(t\)-distribution table

Let

\[
T\sim t_5.
\]

Use the following table values:

\[
P(T>2.015)=0.05,
\]

\[
P(T>2.571)=0.025,
\]

\[
P(T>3.365)=0.01.
\]

Find:

**(a)** \(P(T<2.015)\)

**(b)** \(P(T<-2.571)\)

**(c)** \(P(-2.571<T<2.571)\)

**(d)** the positive value \(c\) such that \(P(T>c)=0.01\).

## 13.2 Bridge questions

### Question 3: From \(z\) to \(t\)

In ordinary A-Level Statistics, when \(\sigma\) is known, the test statistic for a population mean is

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
\]

For a small sample from a normal population where \(\sigma\) is unknown, explain why this is changed to

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

Your answer must mention what \(S\) represents, why the distribution is not \(N(0,1)\), and why the tails of the \(t\)-distribution are fatter for small samples.

### Question 4: Why \(n-1\)?

A sample contains \(6\) values. The sample mean is known.

**(a)** Explain why only \(5\) of the \(6\) values can vary freely.

**(b)** State the degrees of freedom for a one-sample \(t\)-test using this sample.

**(c)** Explain the link between this and the sample variance formula \(s^2=\dfrac{\sum(x_i-\bar x)^2}{n-1}\).

## 13.3 Standard exam-style questions

### Question 5: One-sample \(t\)-test from summary statistics

A manufacturer claims that a packet has mean mass \(100\text{ g}\). A random sample of \(9\) packets gives

\[
\bar x=98.6,\qquad s=1.2.
\]

Assuming packet masses are normally distributed, test at the \(5\%\) significance level whether the true mean mass is less than \(100\text{ g}\). Use \(t_{8,0.05}=1.860\), where \(P(T>1.860)=0.05\), \(T\sim t_8\).

### Question 6: One-sample \(t\)-test from \(\sum x\) and \(\sum x^2\)

A filling machine is intended to fill bottles with mean volume \(50\text{ ml}\). A sample of \(10\) bottles gives

\[
\sum x=499.2,
\]

\[
\sum x^2=24921.504.
\]

Assuming bottle volumes are normally distributed, test at the \(5\%\) significance level whether the true mean volume is less than \(50\text{ ml}\). Use \(t_{9,0.05}=1.833\).

### Question 7: Paired \(t\)-test

Six students take a short test before and after a revision session. The improvement scores, calculated as \(D=\text{after score}-\text{before score}\), are

\[
5,\quad 7,\quad 2,\quad 4,\quad 6,\quad 3.
\]

Assuming the differences are normally distributed, test at the \(5\%\) significance level whether the revision session improves the mean score. Use \(t_{5,0.05}=2.015\).

### Question 8: Two-sample pooled \(t\)-test

Two independent random samples are taken from normally distributed populations with equal but unknown variances.

Group \(A\):

\[
n_A=8,\qquad \bar a=42.1,\qquad s_A^2=4.0.
\]

Group \(B\):

\[
n_B=7,\qquad \bar b=39.6,\qquad s_B^2=5.5.
\]

Test, at the \(5\%\) significance level, whether the population mean of group \(A\) is greater than the population mean of group \(B\). Use \(t_{13,0.05}=1.771\).

## 13.4 Harder synthesis question

### Question 9: Which \(t\)-test?

For each situation, choose the correct test and give a reason.

**(a)** The same \(10\) athletes have their sprint times measured before and after a training programme.

**(b)** A sample of \(7\) trees from woodland \(X\) and a separate sample of \(9\) trees from woodland \(Y\) are used to compare mean heights. The populations are normally distributed with equal unknown variances.

**(c)** A sample of \(6\) bolts is used to test whether the mean bolt diameter is less than \(5\text{ mm}\). The population standard deviation is unknown.

**(d)** A sample of \(50\) items is used to test a mean, and the population standard deviation is known.

---

# 14. Worked Solutions

## Solution 1: Choosing the correct distribution

**(a)** Use \(T\), since the sample is small, normal population is stated and \(\sigma\) is unknown. Degrees of freedom:

\[
\nu=12-1=11.
\]

**(b)** Use \(Z\), since \(\sigma\) is known. No \(t\)-degrees of freedom are needed.

**(c)** Use a paired \(t\)-test on the differences. There are \(9\) differences, so

\[
\nu=9-1=8.
\]

**(d)** Use a pooled two-sample \(t\)-test. Degrees of freedom:

\[
\nu=8+11-2=17.
\]

## Solution 2: Reading the \(t\)-distribution table

Given \(T\sim t_5\).

**(a)** Since \(P(T>2.015)=0.05\),

\[
P(T<2.015)=1-0.05=0.95.
\]

**(b)** By symmetry,

\[
P(T<-2.571)=P(T>2.571)=0.025.
\]

**(c)** The probability outside the interval is \(0.025+0.025=0.05\). Therefore

\[
P(-2.571<T<2.571)=1-0.05=0.95.
\]

**(d)** The positive value \(c\) is

\[
c=3.365.
\]

## Solution 3: From \(z\) to \(t\)

When \(\sigma\) is known, the sample mean is standardised using

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
\]

Here, \(\sigma\) is fixed. When \(\sigma\) is unknown, estimate it with the sample standard deviation \(S\), so

\[
T=\frac{\bar X-\mu}{S/\sqrt n}.
\]

The key issue is that \(S\) is calculated from the sample. It is not fixed. Different samples can give different values of \(S\). For small samples, \(S\) may not be close to \(\sigma\). This extra uncertainty means

\[
\frac{\bar X-\mu}{S/\sqrt n}
\]

does not follow \(N(0,1)\). Instead, assuming the population is normally distributed,

\[
T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}.
\]

The \(t\)-distribution has fatter tails for small samples because there is more uncertainty in the estimated standard deviation.

## Solution 4: Why \(n-1\)?

If a sample contains \(6\) values and the sample mean is known, the total must be

\[
x_1+x_2+x_3+x_4+x_5+x_6=6\bar x.
\]

If \(5\) of the values are chosen freely, the sixth value is forced so that the total remains \(6\bar x\). Therefore only \(6-1=5\) values can vary freely.

For a one-sample \(t\)-test,

\[
\nu=n-1=6-1=5.
\]

The sample variance formula is

\[
s^2=\frac{\sum(x_i-\bar x)^2}{n-1}.
\]

The division by \(n-1\) reflects that the sample mean \(\bar x\) has been estimated from the data. Once \(\bar x\) is fixed, only \(n-1\) deviations are free to vary.

## Solution 5: One-sample \(t\)-test from summary statistics

Let \(\mu\) be the true mean mass.

\[
H_0:\mu=100,
\]

\[
H_1:\mu<100.
\]

\[
n=9,\quad \bar x=98.6,\quad s=1.2.
\]

\[
t=\frac{98.6-100}{1.2/\sqrt9}.
\]

\[
98.6-100=-1.4,
\]

and

\[
\frac{1.2}{\sqrt9}=\frac{1.2}{3}=0.4.
\]

Therefore

\[
t=\frac{-1.4}{0.4}=-3.5.
\]

Degrees of freedom:

\[
\nu=9-1=8.
\]

Given \(t_{8,0.05}=1.860\). For a left-tailed test, the critical value is \(-1.860\). The critical region is

\[
t<-1.860.
\]

Since

\[
-3.5<-1.860,
\]

reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, that the true mean packet mass is less than \(100\text{ g}\).

## Solution 6: One-sample \(t\)-test from \(\sum x\) and \(\sum x^2\)

Let \(\mu\) be the true mean bottle volume.

\[
H_0:\mu=50,
\]

\[
H_1:\mu<50.
\]

\[
\bar x=\frac{499.2}{10}=49.92.
\]

Use

\[
s^2=\frac{\sum x^2-n\bar x^2}{n-1}.
\]

\[
s^2=\frac{24921.504-10(49.92)^2}{10-1}.
\]

\[
49.92^2=2492.0064.
\]

\[
10(49.92)^2=24920.064.
\]

So

\[
s^2=\frac{24921.504-24920.064}{9}=\frac{1.44}{9}=0.16.
\]

\[
s=\sqrt{0.16}=0.4.
\]

\[
t=\frac{49.92-50}{0.4/\sqrt{10}}.
\]

\[
49.92-50=-0.08,
\]

and

\[
\frac{0.4}{\sqrt{10}}\approx0.126491.
\]

So

\[
t\approx\frac{-0.08}{0.126491}=-0.6325.
\]

Degrees of freedom:

\[
\nu=10-1=9.
\]

Given \(t_{9,0.05}=1.833\). For a left-tailed test, the critical value is \(-1.833\). Since

\[
-0.6325>-1.833,
\]

do not reject \(H_0\). There is insufficient evidence, at the \(5\%\) significance level, that the true mean bottle volume is less than \(50\text{ ml}\).

## Solution 7: Paired \(t\)-test

The question defines

\[
D=\text{after score}-\text{before score}.
\]

An improvement means \(D>0\), so

\[
H_0:\mu_D=0,
\]

\[
H_1:\mu_D>0.
\]

The differences are \(5,7,2,4,6,3\).

\[
\sum d=5+7+2+4+6+3=27.
\]

\[
\bar d=\frac{27}{6}=4.5.
\]

\[
\sum d^2=5^2+7^2+2^2+4^2+6^2+3^2=25+49+4+16+36+9=139.
\]

\[
s_d^2=\frac{139-6(4.5)^2}{6-1}.
\]

\[
4.5^2=20.25,
\]

\[
6(4.5)^2=121.5.
\]

Therefore

\[
s_d^2=\frac{139-121.5}{5}=\frac{17.5}{5}=3.5.
\]

\[
s_d=\sqrt{3.5}=1.8708\ldots
\]

\[
t=\frac{4.5-0}{1.8708/\sqrt6}.
\]

Since

\[
\frac{1.8708}{\sqrt6}\approx0.7638,
\]

\[
t\approx\frac{4.5}{0.7638}=5.891.
\]

Degrees of freedom:

\[
\nu=6-1=5.
\]

Given \(t_{5,0.05}=2.015\). The critical region is \(t>2.015\). Since

\[
5.891>2.015,
\]

reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, that the revision session improves the mean score.

## Solution 8: Two-sample pooled \(t\)-test

Let \(\mu_A\) and \(\mu_B\) be the two population means.

\[
H_0:\mu_A-\mu_B=0,
\]

\[
H_1:\mu_A-\mu_B>0.
\]

Assume the samples are independent, both populations are normally distributed, and both populations have equal unknown variances.

\[
s_p^2=\frac{(8-1)(4.0)+(7-1)(5.5)}{8+7-2}.
\]

\[
s_p^2=\frac{7(4.0)+6(5.5)}{13}=\frac{28+33}{13}=\frac{61}{13}=4.692307\ldots
\]

\[
s_p=\sqrt{4.692307\ldots}=2.1662\ldots
\]

\[
t=\frac{(42.1-39.6)-0}{2.1662\ldots\sqrt{\frac{1}{8}+\frac{1}{7}}}.
\]

\[
42.1-39.6=2.5.
\]

\[
\frac{1}{8}+\frac{1}{7}=\frac{7}{56}+\frac{8}{56}=\frac{15}{56}.
\]

\[
\sqrt{\frac{15}{56}}\approx0.51755.
\]

Denominator:

\[
2.1662\ldots(0.51755)\approx1.1211.
\]

Therefore

\[
t\approx\frac{2.5}{1.1211}=2.230.
\]

Degrees of freedom:

\[
\nu=8+7-2=13.
\]

Given \(t_{13,0.05}=1.771\). Since

\[
2.230>1.771,
\]

reject \(H_0\). There is sufficient evidence, at the \(5\%\) significance level, that the population mean of group \(A\) is greater than the population mean of group \(B\).

## Solution 9: Which \(t\)-test?

**(a)** Same \(10\) athletes before and after. Use paired \(t\)-test, \(\nu=10-1=9\).

**(b)** Separate samples of \(7\) and \(9\) trees from normal populations with equal unknown variances. Use pooled two-sample \(t\)-test, \(\nu=7+9-2=14\).

**(c)** One small sample of \(6\) bolts, \(\sigma\) unknown. Use one-sample \(t\)-test, \(\nu=6-1=5\).

**(d)** Sample of \(50\), population standard deviation known. Use a \(z\)-test; no \(t\)-degrees of freedom are needed.

---

# 15. Exam Technique Notes

## 15.1 Always identify the parameter

For a one-sample test, use \(\mu\). For a paired test, use \(\mu_D\). For a two-sample test, use \(\mu_x-\mu_y\). The hypothesis-test machinery only makes sense once the parameter is named.

## 15.2 Use hypotheses, not vibes

A sample mean being smaller than a claimed mean does not automatically mean “reject”. You must test \(H_0\) against the relevant alternative.

## 15.3 Match the alternative hypothesis to the tail

| Wording | Alternative hypothesis | Tail |
|---|---|---|
| “less than” | \(H_1:\mu<\mu_0\) | left-tailed |
| “greater than” | \(H_1:\mu>\mu_0\) | right-tailed |
| “has changed” | \(H_1:\mu\ne\mu_0\) | two-tailed |
| “is different from” | \(H_1:\mu\ne\mu_0\) | two-tailed |
| “has increased” with \(D=\text{after}-\text{before}\) | \(H_1:\mu_D>0\) | right-tailed |
| “has decreased” with \(D=\text{after}-\text{before}\) | \(H_1:\mu_D<0\) | left-tailed |

## 15.4 Write the degrees of freedom explicitly

For one-sample and paired tests:

\[
\nu=n-1.
\]

For pooled two-sample tests:

\[
\nu=n_x+n_y-2.
\]

## 15.5 Use \(s\), not \(\sigma\)

In this topic, the population standard deviation is usually unknown. Use \(s/\sqrt n\) for one-sample and paired tests, or \(s_p\sqrt{1/n_x+1/n_y}\) for pooled two-sample tests.

## 15.6 For paired data, calculate differences first

For paired data, do not compare the two original means directly. Define \(D\), calculate all \(d_i\), calculate \(\bar d\), calculate \(s_d\), and carry out a one-sample \(t\)-test on \(D\).

## 15.7 For pooled two-sample tests, state the assumptions

Write:

```text
Assume the two samples are independent and come from normal populations with equal unknown variances.
```

Then proceed with

\[
s_p^2=
\frac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}.
\]

## 15.8 Use contextual conclusions

Weak conclusion:

```text
Reject H0.
```

Better conclusion:

```text
Reject H0. There is sufficient evidence, at the 5% significance level, that the true mean packet mass is less than 100 g.
```

Weak conclusion:

```text
Do not reject H0.
```

Better conclusion:

```text
Do not reject H0. There is insufficient evidence, at the 5% significance level, that the new cement has altered the mean strength.
```

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Official wording | Covered in lesson? | Evidence strength | Notes |
|---|---|---:|---|---|
| `FA22-TDIST-LO001` | demonstrate understanding of when it is appropriate to use the t-distribution | Yes | Strong | Covered through unknown variance, small sample, normality, \(S\) replacing \(\sigma\), fatter tails and degrees of freedom |
| `FA22-TDIST-LO002` | carry out a hypothesis test for the population mean using a small sample drawn from a normally distributed variable | Yes | Strong | Covered through one-sample \(t\)-test theory, worked examples and generated practice |
| `FA22-TDIST-LO003` | formulate a hypothesis and carry out either a two-sample or paired-sample t-test as appropriate for the difference of the sample means, and demonstrate understanding of the conditions for these tests to be valid | Yes | Strong | Covered through paired differences, pooled two-sample tests, assumptions and test choice |

## 16.2 Evidence coverage table

| Evidence item | Covered? | Where used |
|---|---:|---|
| Guinness/Gosset motivation | Yes, contextual only | Big Picture |
| Unknown variance plus large sample comparison | Yes, bridge/boundary warning | Prerequisite Recap, Core Theory, Common Mistakes |
| \(Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\) bridge | Yes | Bridge, Core Theory |
| \(T=\dfrac{\bar X-\mu}{S/\sqrt n}\) | Yes | Definitions, Core Theory, Worked Examples |
| Fatter tails | Yes | Big Picture, Core Theory, Visual Asset Plan |
| Degrees of freedom \(\nu=n-1\) | Yes | Definitions, Core Theory, Practice |
| \(t\)-table upper-tail reading | Yes | Core Theory, Visual Asset Plan, Practice |
| One-sample \(t\)-test examples | Yes | Worked Examples |
| Paired \(t\)-test examples | Yes | Worked Examples |
| Pooled variance | Yes | Core Theory, Worked Examples |
| Two-sample \(t\)-test | Yes | Core Theory, Worked Examples |
| Calculator instructions | Partly | Visual/widget plan and exam technique |
| Confidence intervals using \(t\) | Logged, not core | Off-spec/boundary-risk section |

## 16.3 Bridge coverage table

| Bridge topic | Covered? | How |
|---|---:|---|
| \(z\)-scores | Yes | Recap and bridge question |
| \(z\)-tests | Yes | Compared with \(t\)-tests |
| Normal distribution | Yes | Conditions and model comparison |
| Sample mean distribution | Yes | Used to motivate \(t\)-statistic |
| Sample variance and \(n-1\) | Yes | Degrees of freedom explanation |
| Hypothesis-test decision logic | Yes | All worked examples |
| Difference of means | Yes | Two-sample \(t\)-test |
| Before/after comparisons | Yes | Paired \(t\)-test |

## 16.4 Off-Spec Content Found but Excluded

| Content found | Source | Why excluded from core |
|---|---|---|
| \(t\)-based confidence intervals for one mean | Transcript | Official `FA22-TDIST` LOs supplied for this lesson focus on hypothesis tests and when to use \(t\), not confidence intervals |
| \(t\)-based confidence intervals for difference of means | Transcript | Useful and connected, but treated as FA22 estimation enrichment unless a separate CCEA LO is supplied |
| Non-parametric tests: Wilcoxon, Mann-Whitney | Dr Frost PDF context table | Not part of supplied CCEA `FA22-TDIST` boundary |
| ANOVA | Dr Frost PDF context table | Not part of supplied CCEA `FA22-TDIST` boundary |
| Fixed threshold “small means \(n<30\)” | Transcript | Useful heuristic, but not used as official CCEA wording |
| Dr Frost non-pooled two-sample formula | Dr Frost PDF | CCEA route for this topic is treated as pooled variance where equal unknown variance is assumed |

## 16.5 Optional Enrichment Not Required by CCEA

The following could be added as enrichment pages later, but should not be treated as core `FA22-TDIST` lesson content:

1. derivation of the \(t\)-distribution using a normal variable divided by a chi-squared variable;
2. \(t\)-confidence intervals for a mean;
3. \(t\)-confidence intervals for the difference between means;
4. Welch’s two-sample \(t\)-test for unequal variances;
5. \(p\)-value method using calculator distributions;
6. comparison between \(t\), \(\chi^2\) and \(F\) distributions.

## 16.6 Weak evidence warnings

- The screenshot PDF was image-only. Only visible preview details were used.
- The CCEA formula booklet extract was not supplied, so exact table layout and formula-book wording were not claimed.
- The Dr Frost PDF is not CCEA-specific, so it was used as supporting teaching evidence only.
- The transcript includes cross-topic confidence interval material, which was deliberately not imported as core `FA22-TDIST` content.
- Some teacher transcript wording refers to Edexcel or textbook chapters; those references were not treated as CCEA authority.

## 16.7 Missing evidence log

| Missing evidence | Impact |
|---|---|
| CCEA formula booklet extract | Cannot quote the exact table heading or formula-book layout |
| CCEA past-paper questions | Practice questions are generated, not past-paper questions |
| Topic-specific README and evidence checklist for this exact topic | Used general project maps and checklists instead |
| Full inspected visuals for all 150 screenshot pages | Only visible/readable preview evidence used |

---

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements based on the evidence and the CCEA topic boundary. They are not claimed to be present in the supplied lesson evidence.

## 17.1 Extra diagrams

1. Distribution-choice flowchart.
2. Fatter-tail comparison diagram.
3. Degrees-of-freedom visual.
4. Paired versus independent data map.
5. Pooled variance balance diagram.

## 17.2 Extra examples

1. One-sample \(t\)-test where the conclusion is “do not reject” even though \(\bar x\) is visibly different from \(\mu_0\).
2. Paired \(t\)-test where the sign convention changes the alternative hypothesis.
3. Two-sample pooled \(t\)-test where the hypothesised difference is not zero.
4. Boundary comparison: same data analysed incorrectly with \(z\) to show why \(t\) matters.

## 17.3 Extra widgets

1. One-sample \(t\)-test step checker.
2. Paired-differences table builder.
3. Pooled-variance calculator.
4. Tail-direction quiz.
5. Distribution-choice diagnostic game.

## 17.4 Extra revision cards

1. “When do I use \(t\)?”
2. “What is \(\nu\)?”
3. “Paired or independent?”
4. “What assumptions must I state?”
5. “What does do not reject mean?”

---

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`: authority for `FA22-TDIST`, LO IDs and topic boundary.
- `Further_Maths_README_module_map.md`: project structure and lesson-pack mapping.
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`: evidence handling, missing evidence and boundary-risk logging.
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`: ordinary A-Level Maths bridge context only.
- `CCEA_GCE_Mathematics_Specification_Map.md`: ordinary Mathematics bridge context only.

## 18.2 Lesson-specific evidence used

- `transcripts.md`: teacher explanation of the \(t\)-distribution, unknown variance, small sample behaviour, fatter tails, degrees of freedom, table use, one-sample \(t\)-tests, paired \(t\)-tests, pooled variance and two-sample tests.
- `t-Tests - Lesson.pdf`: slide examples, \(z\)-test recap, sample standard deviation recap, \(t\)-distribution explanation, calculator guidance, one-sample tests, paired tests and contextual test-choice tables.
- `Chapter_7_t-distribution_📈_(Further_Statistics_2)_screenshots.pdf`: visible slide titles and visual details only. No full text could be parsed from the screenshot PDF, so it is logged as partial visual evidence.

## 18.3 Bridge sources used

Ordinary A-Level Maths sources were used only to explain \(z\)-scores, \(z\)-tests, normal-distribution standardisation, sample mean, sample standard deviation and hypothesis-test structure. They were not used to override the Further Maths specification boundary.

## 18.4 Cross-board or non-CCEA source notes

The Dr Frost PDF and teacher transcript are not CCEA specification documents. They were used as supporting teaching evidence because their content matches the CCEA `FA22-TDIST` boundary where it covers \(t\)-distribution use, one-sample \(t\)-tests, paired \(t\)-tests, difference of means, normality and variance assumptions. Any non-CCEA or cross-topic material was logged and excluded from core.

## 18.5 Evidence limitations

- CCEA formula booklet extract was not supplied.
- No CCEA past-paper questions were supplied.
- Screenshot PDF was image-only and not fully parsed.
- Some lesson evidence included confidence interval material, which was not treated as core `FA22-TDIST`.

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

Before attempting exam questions, check that you can:

- [ ] explain what a \(z\)-score measures;
- [ ] standardise a sample mean using \(Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\);
- [ ] write \(H_0\) and \(H_1\) correctly;
- [ ] identify left-tailed, right-tailed and two-tailed tests;
- [ ] calculate a sample mean \(\bar x\);
- [ ] calculate sample variance using \(s^2=\dfrac{\sum x^2-n\bar x^2}{n-1}\);
- [ ] explain why \(n-1\) appears in sample variance.

## 19.2 Further Maths method checklist

You are ready for `FA22-TDIST` if you can:

- [ ] state when the \(t\)-distribution is appropriate;
- [ ] explain why \(S\) replacing \(\sigma\) changes the distribution;
- [ ] calculate \(t=\dfrac{\bar x-\mu_0}{s/\sqrt n}\);
- [ ] use \(\nu=n-1\) for one-sample tests;
- [ ] define paired differences consistently;
- [ ] calculate \(t=\dfrac{\bar d-0}{s_d/\sqrt n}\);
- [ ] calculate pooled variance \(s_p^2=\dfrac{(n_x-1)s_x^2+(n_y-1)s_y^2}{n_x+n_y-2}\);
- [ ] calculate the pooled two-sample statistic \(t=\dfrac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}{s_p\sqrt{1/n_x+1/n_y}}\);
- [ ] use \(\nu=n_x+n_y-2\) for pooled two-sample tests.

## 19.3 Exam technique checklist

In an exam solution, make sure you:

- [ ] define the population parameter;
- [ ] state hypotheses using population parameters;
- [ ] state or use the normality assumption;
- [ ] state independence and equal variance assumptions for pooled two-sample tests;
- [ ] choose the correct tail;
- [ ] split the significance level correctly for two-tailed tests;
- [ ] write the degrees of freedom;
- [ ] calculate the observed \(t\)-statistic;
- [ ] compare with the correct critical value;
- [ ] write “reject \(H_0\)” or “do not reject \(H_0\)”;
- [ ] give a contextual conclusion.

## 19.4 Bridge checklist

| Ordinary A-Level idea | Further Maths upgrade |
|---|---|
| Known \(\sigma\) | Unknown \(\sigma\), estimate with \(S\) |
| \(Z\sim N(0,1)\) | \(T\sim t_\nu\) |
| Fixed standard error \(\sigma/\sqrt n\) | Estimated standard error \(S/\sqrt n\) |
| One distribution \(N(0,1)\) | Family of distributions \(t_\nu\) |
| Standard normal tails | Fatter \(t\)-tails for small \(\nu\) |
| One-sample \(z\)-test | One-sample \(t\)-test |
| Before/after comparison | Paired \(t\)-test on differences |
| Difference of sample means | Pooled two-sample \(t\)-test |

## 19.5 Diagram and visual understanding checklist

You should be able to explain:

- [ ] why the \(t\)-distribution is symmetric;
- [ ] why \(t_\nu\) has fatter tails than \(N(0,1)\);
- [ ] why \(t_\nu\to N(0,1)\) as \(\nu\) increases;
- [ ] how to read an upper-tail \(t\)-table;
- [ ] how to reflect a right-tail probability into a left-tail probability;
- [ ] why paired data should be drawn as linked pairs;
- [ ] why pooled variance is a weighted combination of two sample variances.

## 19.6 Final one-page memory grid

| Test type | Conditions | Statistic | Degrees of freedom |
|---|---|---|---|
| One-sample \(t\)-test | Small sample, normal population, \(\sigma\) unknown | \(\displaystyle t=\frac{\bar x-\mu_0}{s/\sqrt n}\) | \(\nu=n-1\) |
| Paired \(t\)-test | Paired observations, differences normal | \(\displaystyle t=\frac{\bar d-0}{s_d/\sqrt n}\) | \(\nu=n-1\) |
| Pooled two-sample \(t\)-test | Independent samples, normal populations, equal unknown variances | \(\displaystyle t=\frac{(\bar x-\bar y)-(\mu_x-\mu_y)_0}{s_p\sqrt{1/n_x+1/n_y}}\) | \(\nu=n_x+n_y-2\) |
