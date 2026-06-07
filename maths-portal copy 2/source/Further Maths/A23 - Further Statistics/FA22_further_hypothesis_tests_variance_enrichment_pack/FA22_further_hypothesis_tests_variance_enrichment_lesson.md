# Further Hypothesis Tests for Variance

## Off-Spec Enrichment Lesson for FA22 Section C: Statistics

**Date generated:** 2026-06-05  
**Course:** CCEA GCE Further Mathematics  
**Unit:** `FA22`  
**Official unit name:** Further A2 2 Applied Mathematics  
**Applied section:** Section C: Statistics  
**Core CCEA status:** Off-spec enrichment, not required by CCEA unless separate official CCEA evidence is supplied  
**Closest CCEA boundary topic:** Sampling and estimation  
**Closest CCEA LO overlap:** `FA22-EST-LO002`, because it uses  
\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}
\]
as an unbiased estimator of \(\sigma^2\).  
**No exact CCEA LO found for:** variance confidence intervals, \(\chi^2\) tests for variance, \(F\)-distribution, or \(F\)-tests comparing variances.

| Metadata field | Value |
|---|---|
| `unit_code` | `FA22` |
| `topic_code` | `OFFSPEC-ENRICHMENT` |
| `topic_name` | Further Hypothesis Tests for Variance |
| `topic_slug` | `further_hypothesis_tests_variance_enrichment` |
| `topic_pascal` | `FurtherHypothesisTestsVarianceEnrichment` |
| `topic_id` | `FA22FurtherHypothesisTestsVarianceEnrichment` |
| `lesson_file` | `FA22_further_hypothesis_tests_variance_enrichment_lesson.md` |
| `applied_section` | Section C: Statistics |
| `official_LO_IDs` | None found for the full topic |
| `near_boundary_CCEA_LO_IDs` | `FA22-EST-LO002`, `FA22-CHI2-LO002`, `FA22-CHI2-LO003`, `FA22-TDIST-LO003` |
| `bridge_tags` | `#Sampling`, `#Variance`, `#NormalDistribution`, `#HypothesisTesting`, `#ConfidenceIntervals` |
| `topic_tags` | `#OffSpecEnrichment`, `#VarianceInference`, `#ChiSquaredDistribution`, `#FDistribution`, `#FTest`, `#NormalAssumption` |

> **Boundary warning:** This lesson is deliberately marked as **off-spec enrichment**. It is useful for deepening statistical understanding, especially around why sample variance has a non-normal distribution, but it must not be treated as a required CCEA FA22 lesson unless official CCEA evidence is later supplied.

---

# 2. Evidence Map

| Evidence source | Type | What it contributes | Status in this lesson |
|---|---|---|---|
| CCEA Further Mathematics Specification Map | Project source, specification authority | Confirms the closest official CCEA overlap is point estimation of population variance using \(S^2\). No exact CCEA LO found for variance confidence intervals or \(F\)-tests | Boundary authority |
| Further Maths README module map | Project source | Confirms file naming, unit-code rules, lesson phase structure and bridge protocol | Workflow authority |
| Further Maths Evidence Drop Checklist | Project source | Confirms evidence priority and off-spec logging rules | Workflow authority |
| `transcripts.md` | Lesson-specific transcript | Full teacher explanation of Chapter 6: \(\chi^2\) distribution for variance, confidence intervals for variance, hypothesis tests for variance, \(F\)-distribution and \(F\)-tests | Core enrichment evidence |
| Screenshot PDF | Lesson-specific visual evidence | Page 1 visually confirms the lesson split into Chapter 6a \(\chi^2_{n-1}\) distribution for variance and Chapter 6b \(F\)-distribution for differences in variances | Visual evidence, partially inaccessible because no parsed text |
| `Which Hypothesis Test Poster.pdf` | Cross-board / third-party support | Provides general test-selection context: parametric assumptions, sample-number distinction, \(z\)-tests, \(t\)-tests, \(\chi^2\) tests and variance/F-distribution route | Supplementary enrichment only |
| Ordinary A-Level Maths bridge extracts | Bridge source | Sampling, summary statistics, variance, standard deviation, normal distribution and hypothesis testing | Bridge context only |

---

# 3. Specification Alignment

## 3.1 CCEA Boundary Alignment

| CCEA LO ID | Official / project wording summary | Relationship to this lesson | Lesson coverage | Boundary judgement |
|---|---|---|---|---|
| `FA22-EST-LO002` | Calculate point estimates of population mean and variance, including \(S^2=\frac{\sum(X_i-\bar X)^2}{n-1}\) as an unbiased estimator of \(\sigma^2\) | Direct overlap | Used as the starting point for all variance inference | On-spec overlap only |
| `FA22-EST-LO004` | Calculate confidence intervals for the population mean | Conceptual bridge only | This lesson considers confidence intervals for variance, not mean | Off-spec extension |
| `FA22-CHI2-LO002` | Use \(\chi^2\) test for goodness of fit | Same distribution family, different application | This lesson uses \(\chi^2\) for variance of a normal distribution | Boundary risk |
| `FA22-CHI2-LO003` | Use \(\chi^2\) test for independence in a contingency table | Same distribution family, different application | No contingency-table method taught here | Not core |
| `FA22-TDIST-LO003` | Two-sample or paired-sample \(t\)-test for means, with validity conditions | Shares the hypothesis-test framework and normality/variance ideas | This lesson tests variances, not means | Off-spec extension |

## 3.2 Enrichment Objectives

These are lesson-local enrichment objectives, not official CCEA LO IDs.

| Enrichment objective | Student should be able to... | Evidence source |
|---|---|---|
| ENR-OBJ-001 | Explain why \(S^2\) is an unbiased estimator of \(\sigma^2\), but why its distribution is not normal | Transcript |
| ENR-OBJ-002 | Use \(\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}\) for a normal population | Transcript |
| ENR-OBJ-003 | Derive a confidence interval for \(\sigma^2\) using upper-tail \(\chi^2\) critical values | Transcript |
| ENR-OBJ-004 | Carry out a one-sample hypothesis test for a population variance | Transcript |
| ENR-OBJ-005 | Explain the \(F\)-distribution as a ratio of scaled \(\chi^2\) variables | Transcript |
| ENR-OBJ-006 | Carry out an \(F\)-test comparing two population variances | Transcript |
| ENR-OBJ-007 | State and check the normality and independence assumptions | Transcript and poster |

---

# 4. Learning Objectives

## Core enrichment objectives

By the end of this lesson, you should be able to:

1. State that, for a random sample of size \(n\) from a normal population,
   \[
   \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
   \]

2. Explain why the number of degrees of freedom is \(n-1\), not \(n\).

3. Use upper-tail \(\chi^2\) percentage points to construct a confidence interval for the population variance \(\sigma^2\).

4. Carry out a hypothesis test for a single population variance.

5. Define the \(F\)-distribution as
   \[
   F=\frac{U/\nu_1}{V/\nu_2},
   \]
   where
   \[
   U\sim\chi^2_{\nu_1},\qquad V\sim\chi^2_{\nu_2},
   \]
   and \(U,V\) are independent.

6. Use the \(F\)-test statistic
   \[
   F=\frac{S_1^2}{S_2^2}
   \]
   to compare two population variances under the null hypothesis
   \[
   H_0:\sigma_1^2=\sigma_2^2.
   \]

## Bridge objectives

You should connect this lesson to ordinary A-Level Maths by recognising:

1. sample mean \(\bar X\) as an estimator of population mean \(\mu\);
2. sample variance \(S^2\) as an estimator of population variance \(\sigma^2\);
3. normal standardisation:
   \[
   Z=\frac{X-\mu}{\sigma};
   \]
4. hypothesis-test structure: hypotheses, significance level, critical region, test statistic, conclusion in context;
5. confidence interval logic: middle probability region, tail probabilities and interval interpretation.

## Exam technique objectives

Although this is off-spec enrichment for CCEA, the exam-style technique is:

1. always state the normality assumption;
2. use \(S^2\), not the biased variance denominator \(n\);
3. use degrees of freedom carefully;
4. remember that upper-tail \(\chi^2\) and \(F\) tables can make the smaller probability correspond to the larger critical value;
5. reverse inequalities when taking reciprocals;
6. answer in context, especially for standard deviation versus variance.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You should already be comfortable with:

- substitution into formulae;
- rearranging inequalities;
- interpreting square roots and squares;
- calculating mean, variance and standard deviation;
- understanding that variance has squared units.

Example:

If a time is measured in minutes, then a variance is measured in minutes squared:
\[
\text{minutes}^2.
\]

That matters because a question may ask about a standard deviation in minutes but give a variance in minutes squared.

## 5.2 Ordinary A-Level Maths foundations

You should already know:

- random samples;
- sample mean:
  \[
  \bar X=\frac{\sum X_i}{n};
  \]
- sample variance:
  \[
  S^2=\frac{\sum(X_i-\bar X)^2}{n-1};
  \]
- normal distribution:
  \[
  X\sim N(\mu,\sigma^2);
  \]
- standardisation:
  \[
  Z=\frac{X-\mu}{\sigma};
  \]
- hypothesis tests:
  \[
  H_0,\quad H_1,\quad \text{significance level},\quad \text{critical region};
  \]
- confidence intervals for a population mean.

## 5.3 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Sampling | A sample is used to learn about a population | The sample variance \(S^2\) is used as an estimator of the population variance \(\sigma^2\) | A sample statistic varies from sample to sample |
| AS2 Data presentation and interpretation | Variance and standard deviation describe spread | Variance becomes the object being estimated and tested | Do not confuse descriptive calculation with inference |
| A22 Normal distribution | Standardise with \(Z=\frac{X-\mu}{\sigma}\) | Squared standard normal variables lead to \(\chi^2\) variables | Squaring destroys symmetry and creates a right-skewed distribution |
| A22 Hypothesis testing | Use \(H_0\), \(H_1\), critical regions and conclusions | Same test skeleton, but the test statistic follows \(\chi^2\) or \(F\), not normal | Tail direction and degrees of freedom are the trapdoors |
| A22 Confidence intervals | Confidence intervals estimate unknown parameters | Here the unknown parameter is \(\sigma^2\), not \(\mu\) | Reciprocals reverse inequality signs |

In ordinary A-Level Maths, this idea appeared as sampling, variance, standard deviation, normal distribution and hypothesis testing for a mean or proportion.

In Further Statistics enrichment, the same idea becomes inference about **spread itself**. Instead of asking “has the mean changed?”, we ask “has the variance changed?” or “are the two variances different?”

The key upgrade is that \(S^2\) does not behave normally. A transformed version of it,

\[
\frac{(n-1)S^2}{\sigma^2},
\]

has a \(\chi^2\) distribution when the original population is normal.

The danger is that the hypothesis-test skeleton looks familiar, but the distribution, critical values, tail logic and assumptions have all changed. A friendly little stats goblin has swapped the ruler.

---

# 6. Big Picture Explanation

Variance measures spread. Sometimes the mean is not the main issue.

A machine might produce parts with the correct average length but too much variation.  
A mechanic might usually take the expected time to change tyres, but with inconsistent timing.  
Two orchards might produce fruit with the same mean size, but one orchard’s fruit sizes are more uniform.

That is why variance inference exists.

## Mean inference versus variance inference

For means, ordinary A-Level Maths often uses the normal distribution or \(t\)-distribution.

For variance, the sample variance

\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}
\]

is an unbiased estimator of \(\sigma^2\), but \(S^2\) itself is not normally distributed. The teacher transcript states that the distribution is not simple and is not normally distributed.

Instead, for a normal population,

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
\]

That one formula is the enchanted key for:

- confidence intervals for \(\sigma^2\);
- hypothesis tests for one population variance.

For comparing two variances, we use the \(F\)-distribution:

\[
F=\frac{S_1^2}{S_2^2}
\]

under the null hypothesis that the two population variances are equal.

## Modelling assumptions

This lesson is statistical modelling, so assumptions matter.

For \(\chi^2\) variance inference:

1. the data are a random sample;
2. the population is normally distributed;
3. \(S^2\) is calculated using denominator \(n-1\).

For \(F\)-tests:

1. the two samples are independent;
2. each sample is taken from a normal population;
3. \(S_1^2\) and \(S_2^2\) are unbiased sample variances;
4. the order of numerator and denominator is tracked carefully.

---

# 7. Key Definitions and Notation

## Population mean and variance

Let

\[
X\sim N(\mu,\sigma^2).
\]

This means:

- \(X\) is a normally distributed random variable;
- \(\mu\) is the population mean;
- \(\sigma^2\) is the population variance;
- \(\sigma\) is the population standard deviation.

## Random sample

A random sample of size \(n\) is written as

\[
X_1,X_2,\ldots,X_n.
\]

Each \(X_i\) is assumed to come from the same population.

## Sample mean

The sample mean is

\[
\bar X=\frac{\sum_{i=1}^{n}X_i}{n}.
\]

## Sample variance

The unbiased sample variance is

\[
S^2=\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}.
\]

The denominator is \(n-1\), not \(n\), because the sample mean \(\bar X\) has been estimated from the data. One degree of freedom has already been used.

## Standard normal variable

If

\[
X\sim N(\mu,\sigma^2),
\]

then

\[
Z=\frac{X-\mu}{\sigma}
\]

has distribution

\[
Z\sim N(0,1).
\]

## Chi-squared distribution

If

\[
Z_1,Z_2,\ldots,Z_\nu
\]

are independent standard normal variables, then

\[
Q=Z_1^2+Z_2^2+\cdots+Z_\nu^2
\]

has a chi-squared distribution with \(\nu\) degrees of freedom:

\[
Q\sim\chi^2_\nu.
\]

The transcript describes a \(\chi^2\) distribution as the sum of squared standard normal distributions.

## Upper-tail chi-squared critical value

We will write

\[
\chi^2_\nu(p)
\]

for the value such that

\[
P(\chi^2_\nu>\chi^2_\nu(p))=p.
\]

So:

- \(\chi^2_\nu(0.025)\) is a large value, because only \(2.5\%\) is above it;
- \(\chi^2_\nu(0.975)\) is a small value, because \(97.5\%\) is above it.

This is the “probability to the right” convention used in the transcript.

## F-distribution

If

\[
U\sim\chi^2_{\nu_1},\qquad V\sim\chi^2_{\nu_2},
\]

and \(U,V\) are independent, then

\[
F=\frac{U/\nu_1}{V/\nu_2}
\]

has an \(F\)-distribution with \(\nu_1\) and \(\nu_2\) degrees of freedom:

\[
F\sim F_{\nu_1,\nu_2}.
\]

The order matters:

\[
F_{\nu_1,\nu_2}\neq F_{\nu_2,\nu_1}
\]

in general.

---

# 8. Core Theory

## 8.1 Why variance inference needs a new distribution

**Bridge Note:** In ordinary A-Level Maths, you used \(\bar X\) to estimate \(\mu\) and often treated sample means using a normal model. Here, Further Statistics enrichment asks what happens to \(S^2\), the sample variance.

We know that

\[
S^2=\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}
\]

is an unbiased estimator of \(\sigma^2\).

But the distribution of \(S^2\) is not normal. The transcript makes this warning explicit.

So we do not use

\[
S^2\sim N(\text{something},\text{something}).
\]

Instead, if the original population is normal, we use:

\[
\boxed{\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}}.
\]

This is the main formula for one-sample variance inference.

## 8.2 Chi-squared distribution as squared standard normals

Suppose

\[
Z_1,Z_2,\ldots,Z_n
\]

are independent standard normal variables, where

\[
Z_i\sim N(0,1).
\]

Then

\[
Z_1^2+Z_2^2+\cdots+Z_n^2\sim\chi^2_n.
\]

Using sigma notation,

\[
\sum_{i=1}^{n}Z_i^2\sim\chi^2_n.
\]

If

\[
X_i\sim N(\mu,\sigma^2),
\]

then

\[
Z_i=\frac{X_i-\mu}{\sigma}.
\]

Therefore

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2\sim\chi^2_n.
\]

This is the starting cauldron.

## 8.3 Deriving \(\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}\)

This derivation is enrichment. It is not required for CCEA core.

Start with the definition:

\[
S^2=\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}.
\]

Multiply both sides by \(n-1\):

\[
(n-1)S^2=\sum_{i=1}^{n}(X_i-\bar X)^2.
\]

Divide by \(\sigma^2\):

\[
\frac{(n-1)S^2}{\sigma^2}
=
\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{\sigma^2}.
\]

Since \(\sigma^2\) is a constant, this can be written as

\[
\frac{(n-1)S^2}{\sigma^2}
=
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}.
\]

Equivalently,

\[
\frac{(n-1)S^2}{\sigma^2}
=
\sum_{i=1}^{n}\left(\frac{X_i-\bar X}{\sigma}\right)^2.
\]

We want the distribution of this quantity.

Now begin with a related quantity whose distribution is known:

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2\sim\chi^2_n.
\]

Use the algebraic trick from the transcript:

\[
X_i-\mu=(X_i-\bar X)+(\bar X-\mu).
\]

So

\[
\frac{X_i-\mu}{\sigma}
=
\frac{(X_i-\bar X)+(\bar X-\mu)}{\sigma}.
\]

Square it:

\[
\left(\frac{X_i-\mu}{\sigma}\right)^2
=
\left(\frac{(X_i-\bar X)+(\bar X-\mu)}{\sigma}\right)^2.
\]

Using

\[
(a+b)^2=a^2+2ab+b^2,
\]

with

\[
a=X_i-\bar X,\qquad b=\bar X-\mu,
\]

we get

\[
\left(\frac{X_i-\mu}{\sigma}\right)^2
=
\frac{(X_i-\bar X)^2}{\sigma^2}
+
\frac{2(X_i-\bar X)(\bar X-\mu)}{\sigma^2}
+
\frac{(\bar X-\mu)^2}{\sigma^2}.
\]

Now sum from \(i=1\) to \(n\):

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2
=
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}
+
\sum_{i=1}^{n}\frac{2(X_i-\bar X)(\bar X-\mu)}{\sigma^2}
+
\sum_{i=1}^{n}\frac{(\bar X-\mu)^2}{\sigma^2}.
\]

Consider the middle term:

\[
\sum_{i=1}^{n}\frac{2(X_i-\bar X)(\bar X-\mu)}{\sigma^2}.
\]

Since \(2\), \(\bar X-\mu\), and \(\sigma^2\) are constant with respect to \(i\), take them outside the summation:

\[
\sum_{i=1}^{n}\frac{2(X_i-\bar X)(\bar X-\mu)}{\sigma^2}
=
\frac{2(\bar X-\mu)}{\sigma^2}
\sum_{i=1}^{n}(X_i-\bar X).
\]

Now

\[
\sum_{i=1}^{n}(X_i-\bar X)
=
\sum_{i=1}^{n}X_i-\sum_{i=1}^{n}\bar X.
\]

Because \(\bar X\) is constant,

\[
\sum_{i=1}^{n}\bar X=n\bar X.
\]

Also,

\[
\bar X=\frac{\sum_{i=1}^{n}X_i}{n},
\]

so

\[
\sum_{i=1}^{n}X_i=n\bar X.
\]

Therefore

\[
\sum_{i=1}^{n}(X_i-\bar X)
=
n\bar X-n\bar X
=
0.
\]

So the middle term vanishes:

\[
\frac{2(\bar X-\mu)}{\sigma^2}
\sum_{i=1}^{n}(X_i-\bar X)
=
0.
\]

We are left with

\[
\sum_{i=1}^{n}\left(\frac{X_i-\mu}{\sigma}\right)^2
=
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}
+
\sum_{i=1}^{n}\frac{(\bar X-\mu)^2}{\sigma^2}.
\]

The final term is constant across the summation, so

\[
\sum_{i=1}^{n}\frac{(\bar X-\mu)^2}{\sigma^2}
=
\frac{n(\bar X-\mu)^2}{\sigma^2}.
\]

Now rewrite it as

\[
\frac{n(\bar X-\mu)^2}{\sigma^2}
=
\frac{(\bar X-\mu)^2}{\sigma^2/n}.
\]

Since

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right),
\]

we have

\[
\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).
\]

Therefore

\[
\left(\frac{\bar X-\mu}{\sigma/\sqrt n}\right)^2\sim\chi^2_1.
\]

But

\[
\left(\frac{\bar X-\mu}{\sigma/\sqrt n}\right)^2
=
\frac{(\bar X-\mu)^2}{\sigma^2/n}
=
\frac{n(\bar X-\mu)^2}{\sigma^2}.
\]

So we have decomposed a \(\chi^2_n\) variable into:

\[
\chi^2_n
=
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}
+
\chi^2_1.
\]

The remaining part has \(n-1\) degrees of freedom:

\[
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}
\sim\chi^2_{n-1}.
\]

But

\[
\sum_{i=1}^{n}\frac{(X_i-\bar X)^2}{\sigma^2}
=
\frac{(n-1)S^2}{\sigma^2}.
\]

Therefore

\[
\boxed{\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}}.
\]

**Important refinement:** The teacher transcript presents the intuition that one squared normal component is used by \(\bar X\), leaving \(n-1\) degrees of freedom. In a fully rigorous university proof, one also uses the fact that, for a normal sample, the sample mean and sample variance are independent. This is the quiet hinge in the proof door.

## 8.4 Confidence interval for the population variance

**Bridge Note:** In ordinary A-Level Maths, a confidence interval for a mean often comes from putting the estimator in the middle of a probability statement. Here we do the same thing, but the statistic follows \(\chi^2\), and the parameter \(\sigma^2\) is in the denominator.

Let

\[
\nu=n-1.
\]

For a normal population,

\[
\frac{\nu S^2}{\sigma^2}\sim\chi^2_\nu.
\]

For a \(100(1-\alpha)\%\) confidence interval, the middle probability is

\[
1-\alpha.
\]

So the two tails each have probability

\[
\frac{\alpha}{2}.
\]

Using upper-tail notation,

\[
P\left(
\chi^2_\nu(1-\alpha/2)
<
\frac{\nu S^2}{\sigma^2}
<
\chi^2_\nu(\alpha/2)
\right)
=
1-\alpha.
\]

Now solve the inequality for \(\sigma^2\).

Start with

\[
\chi^2_\nu(1-\alpha/2)
<
\frac{\nu S^2}{\sigma^2}
<
\chi^2_\nu(\alpha/2).
\]

Take reciprocals. Since all quantities are positive, the inequality signs reverse:

\[
\frac{1}{\chi^2_\nu(1-\alpha/2)}
>
\frac{\sigma^2}{\nu S^2}
>
\frac{1}{\chi^2_\nu(\alpha/2)}.
\]

Rewrite in increasing order:

\[
\frac{1}{\chi^2_\nu(\alpha/2)}
<
\frac{\sigma^2}{\nu S^2}
<
\frac{1}{\chi^2_\nu(1-\alpha/2)}.
\]

Multiply throughout by \(\nu S^2\):

\[
\frac{\nu S^2}{\chi^2_\nu(\alpha/2)}
<
\sigma^2
<
\frac{\nu S^2}{\chi^2_\nu(1-\alpha/2)}.
\]

So the confidence interval is

\[
\boxed{
\left(
\frac{(n-1)S^2}{\chi^2_{n-1}(\alpha/2)},
\frac{(n-1)S^2}{\chi^2_{n-1}(1-\alpha/2)}
\right)
}.
\]

For a \(95\%\) confidence interval:

\[
\alpha=0.05,
\]

so

\[
\alpha/2=0.025,
\]

and

\[
1-\alpha/2=0.975.
\]

Therefore

\[
\boxed{
\frac{(n-1)S^2}{\chi^2_{n-1}(0.025)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{n-1}(0.975)}
}.
\]

**Warning:** This looks backwards until you remember that \(\chi^2_\nu(0.025)\) is a large upper-tail value and \(\chi^2_\nu(0.975)\) is a small upper-tail value.

## 8.5 Hypothesis test for one population variance

**Bridge Note:** In ordinary A-Level Maths, the hypothesis-test skeleton was: state hypotheses, choose significance level, calculate a test statistic, compare with critical region, conclude in context. Here that skeleton survives, but the test statistic follows \(\chi^2\).

Suppose

\[
X\sim N(\mu,\sigma^2).
\]

We want to test a claim about the population variance.

The null hypothesis is usually

\[
H_0:\sigma^2=\sigma_0^2.
\]

The alternative could be:

\[
H_1:\sigma^2>\sigma_0^2,
\]

or

\[
H_1:\sigma^2<\sigma_0^2,
\]

or

\[
H_1:\sigma^2\neq\sigma_0^2.
\]

Under \(H_0\), assume

\[
\sigma^2=\sigma_0^2.
\]

Then the test statistic is

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Under \(H_0\),

\[
T\sim\chi^2_{n-1}.
\]

### Upper-tailed test

If

\[
H_1:\sigma^2>\sigma_0^2,
\]

large values of \(S^2\) support \(H_1\), so large values of \(T\) support \(H_1\).

The critical region is

\[
T>\chi^2_{n-1}(\alpha).
\]

### Lower-tailed test

If

\[
H_1:\sigma^2<\sigma_0^2,
\]

small values of \(S^2\) support \(H_1\), so small values of \(T\) support \(H_1\).

Using upper-tail notation, the lower critical value is

\[
\chi^2_{n-1}(1-\alpha).
\]

The critical region is

\[
T<\chi^2_{n-1}(1-\alpha).
\]

### Two-tailed test

If

\[
H_1:\sigma^2\neq\sigma_0^2,
\]

split the significance level:

\[
\frac{\alpha}{2}
\]

in each tail.

The critical regions are

\[
T<\chi^2_{n-1}(1-\alpha/2)
\]

or

\[
T>\chi^2_{n-1}(\alpha/2).
\]

## 8.6 F-distribution for comparing two variances

**Bridge Note:** In ordinary A-Level Maths, two-sample tests often compare two means. In this enrichment lesson, we compare two variances.

Suppose there are two independent normal populations:

\[
X\sim N(\mu_X,\sigma_X^2),
\]

and

\[
Y\sim N(\mu_Y,\sigma_Y^2).
\]

Let the sample sizes be:

\[
n_X,\qquad n_Y.
\]

Let the unbiased sample variances be:

\[
S_X^2,\qquad S_Y^2.
\]

For the first population,

\[
\frac{(n_X-1)S_X^2}{\sigma_X^2}\sim\chi^2_{n_X-1}.
\]

For the second population,

\[
\frac{(n_Y-1)S_Y^2}{\sigma_Y^2}\sim\chi^2_{n_Y-1}.
\]

Let

\[
\nu_1=n_X-1,\qquad \nu_2=n_Y-1.
\]

Then

\[
\frac{\frac{(n_X-1)S_X^2}{\sigma_X^2}/(n_X-1)}
{\frac{(n_Y-1)S_Y^2}{\sigma_Y^2}/(n_Y-1)}
\sim F_{\nu_1,\nu_2}.
\]

Simplify the numerator:

\[
\frac{(n_X-1)S_X^2}{\sigma_X^2}\div(n_X-1)
=
\frac{S_X^2}{\sigma_X^2}.
\]

Simplify the denominator:

\[
\frac{(n_Y-1)S_Y^2}{\sigma_Y^2}\div(n_Y-1)
=
\frac{S_Y^2}{\sigma_Y^2}.
\]

So

\[
\frac{S_X^2/\sigma_X^2}{S_Y^2/\sigma_Y^2}
\sim F_{\nu_1,\nu_2}.
\]

For an \(F\)-test, the null hypothesis is

\[
H_0:\sigma_X^2=\sigma_Y^2.
\]

Under \(H_0\), the two population variances are equal, so they cancel in the ratio:

\[
\frac{S_X^2/\sigma_X^2}{S_Y^2/\sigma_Y^2}
=
\frac{S_X^2}{S_Y^2}.
\]

Therefore, under \(H_0\),

\[
\boxed{
\frac{S_X^2}{S_Y^2}\sim F_{n_X-1,n_Y-1}
}.
\]

The transcript states that the \(F\)-distribution is used when comparing the variances of two different normal populations, and that the order of degrees of freedom matters.

## 8.7 Reciprocal rule for \(F\)-values

The order matters:

\[
F_{\nu_1,\nu_2}
\neq
F_{\nu_2,\nu_1}.
\]

If

\[
F=\frac{S_X^2}{S_Y^2},
\]

then the reciprocal is

\[
\frac{1}{F}=\frac{S_Y^2}{S_X^2}.
\]

The degrees of freedom also swap:

\[
F_{\nu_1,\nu_2}
\quad\text{becomes}\quad
F_{\nu_2,\nu_1}.
\]

The transcript gives the memorable “three switches” rule:

1. switch \(\nu_1\) and \(\nu_2\);
2. take the reciprocal of the \(F\)-value;
3. reverse the inequality sign.

So

\[
P(F_{\nu_1,\nu_2}<a)
=
P\left(F_{\nu_2,\nu_1}>\frac{1}{a}\right).
\]

This is why lower-tail \(F\)-critical values can be found from upper-tail tables.

---

# 9. Visual Asset Integration

No files are generated yet. These are placeholders for later phases.

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + enrichment transcript | Insert from svg/FA22FurtherHypothesisTestsVarianceEnrichmentBridgeSVG-001.svg | Purpose: Compare ordinary A-Level mean inference with enrichment variance inference. The visual must show \(\bar X\to\mu\) using normal or \(t\)-methods beside \(S^2\to\sigma^2\) using \(\chi^2\)-methods.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentSVG-001 | Source: Teacher transcript proof of chi-squared variance statistic | Insert from svg/FA22FurtherHypothesisTestsVarianceEnrichmentSVG-001.svg | Purpose: Show the decomposition of total squared standardised variation into sample-spread variation plus sample-mean variation.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentSVG-002 | Source: Teacher transcript confidence interval derivation | Insert from svg/FA22FurtherHypothesisTestsVarianceEnrichmentSVG-002.svg | Purpose: Show a right-skewed \(\chi^2_\nu\) curve with upper-tail values \(\chi^2_\nu(0.975)\) and \(\chi^2_\nu(0.025)\), with the middle \(95\%\) shaded.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentSVG-003 | Source: Teacher transcript one-sample variance hypothesis test | Insert from svg/FA22FurtherHypothesisTestsVarianceEnrichmentSVG-003.svg | Purpose: Show one-tailed and two-tailed \(\chi^2\) critical regions for variance tests.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentSVG-004 | Source: Teacher transcript F-distribution section | Insert from svg/FA22FurtherHypothesisTestsVarianceEnrichmentSVG-004.svg | Purpose: Show two \(F\)-distributions, \(F_{\nu_1,\nu_2}\) and \(F_{\nu_2,\nu_1}\), to make order of degrees of freedom visible.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001 | Source: Lesson synthesis from transcript and bridge context | Insert from mermaid/FA22FurtherHypothesisTestsVarianceEnrichmentMermaid-001.md | Purpose: Decision tree for choosing between \(S^2\) calculation, \(\chi^2\) variance confidence interval, one-variance \(\chi^2\) test and two-variance \(F\)-test.]

[VISUAL PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentTikZ-001 | Source: Teacher transcript confidence interval derivation | Insert from tikz/FA22FurtherHypothesisTestsVarianceEnrichmentTikZ-001.tex | Purpose: Precise mathematical number-line diagram showing reciprocal inequality reversal when solving for \(\sigma^2\).]

---

# 10. Interactive Learning Widgets

No widgets are generated yet. These are placeholders for Phase 5.

[INTERACTIVE PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherHypothesisTestsVarianceEnrichmentWidget-001.html | Purpose: Let the student input \(n\), \(S^2\), \(\sigma_0^2\), significance level and tail type, then display the \(\chi^2\) test statistic and critical-region decision.]

Student inputs:

- \(n\);
- \(S^2\);
- hypothesised variance \(\sigma_0^2\);
- significance level;
- one-tailed or two-tailed alternative.

Widget displays:

- degrees of freedom \(\nu=n-1\);
- test statistic
  \[
  T=\frac{(n-1)S^2}{\sigma_0^2};
  \]
- critical region;
- conclusion scaffold.

Error checks:

- warns if \(S^2\le 0\);
- warns if \(n<2\);
- reminds student that normality is required.

[INTERACTIVE PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherHypothesisTestsVarianceEnrichmentWidget-002.html | Purpose: Let the student build a confidence interval for \(\sigma^2\) and see why \(\chi^2(0.025)\) goes in the lower-bound denominator for a 95% interval.]

Student inputs:

- confidence level;
- \(n\);
- \(S^2\);
- table values \(\chi^2_\nu(\alpha/2)\) and \(\chi^2_\nu(1-\alpha/2)\).

Widget displays:

\[
\frac{(n-1)S^2}{\chi^2_\nu(\alpha/2)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_\nu(1-\alpha/2)}.
\]

Error checks:

- warns if the upper-tail values are swapped;
- highlights reciprocal inequality reversal.

[INTERACTIVE PLACEHOLDER: FA22FurtherHypothesisTestsVarianceEnrichmentWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherHypothesisTestsVarianceEnrichmentWidget-003.html | Purpose: Let the student compare two sample variances using an \(F\)-test, including numerator choice, degrees of freedom and reciprocal rule.]

Student inputs:

- \(n_1,n_2\);
- \(S_1^2,S_2^2\);
- significance level;
- alternative hypothesis.

Widget displays:

\[
F=\frac{S_1^2}{S_2^2},
\qquad
F\sim F_{n_1-1,n_2-1}.
\]

Error checks:

- warns that order matters;
- shows reciprocal if student swaps numerator and denominator;
- requires normality and independence assumptions.

---

# 11. Worked Examples

## Worked Example 1: Confidence interval for variance

### Evidence source

Teacher transcript, Chi-squared Distribution for Variance 2.

### On-spec status

Off-spec enrichment for CCEA. Uses on-spec estimator \(S^2\), then extends beyond CCEA into confidence intervals for \(\sigma^2\).

### Question

Eight marksmen fire a rifle at a target. The distances \(X\), in millimetres, of the eight shots from the centre are:

\[
10,\ 14,\ 12,\ 8,\ 6,\ 11,\ 18,\ 14.
\]

Assume the distances are normally distributed.

Find a \(95\%\) confidence interval for the population variance.

### Solution

The sample size is

\[
n=8.
\]

Therefore the degrees of freedom are

\[
\nu=n-1=7.
\]

First calculate:

\[
\sum X=10+14+12+8+6+11+18+14=93.
\]

Also,

\[
\sum X^2
=
10^2+14^2+12^2+8^2+6^2+11^2+18^2+14^2.
\]

Compute each square:

\[
10^2=100,
\]

\[
14^2=196,
\]

\[
12^2=144,
\]

\[
8^2=64,
\]

\[
6^2=36,
\]

\[
11^2=121,
\]

\[
18^2=324,
\]

\[
14^2=196.
\]

So

\[
\sum X^2
=
100+196+144+64+36+121+324+196.
\]

Add step by step:

\[
100+196=296,
\]

\[
296+144=440,
\]

\[
440+64=504,
\]

\[
504+36=540,
\]

\[
540+121=661,
\]

\[
661+324=985,
\]

\[
985+196=1181.
\]

Thus

\[
\sum X^2=1181.
\]

The sample mean is

\[
\bar X=\frac{\sum X}{n}.
\]

So

\[
\bar X=\frac{93}{8}.
\]

\[
\bar X=11.625.
\]

The unbiased sample variance is

\[
S^2=\frac{\sum X^2-n\bar X^2}{n-1}.
\]

Substitute:

\[
S^2=\frac{1181-8(11.625)^2}{7}.
\]

Calculate the square:

\[
11.625^2=135.140625.
\]

Multiply by \(8\):

\[
8(11.625)^2=8(135.140625)=1081.125.
\]

Subtract:

\[
1181-1081.125=99.875.
\]

Divide by \(7\):

\[
S^2=\frac{99.875}{7}=14.267857142\ldots
\]

So

\[
S^2\approx14.2679.
\]

For a \(95\%\) confidence interval,

\[
\alpha=0.05,
\]

so

\[
\alpha/2=0.025,
\]

and

\[
1-\alpha/2=0.975.
\]

The confidence interval is

\[
\frac{(n-1)S^2}{\chi^2_{n-1}(0.025)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{n-1}(0.975)}.
\]

Here,

\[
n-1=7.
\]

So

\[
\frac{7S^2}{\chi^2_7(0.025)}
<
\sigma^2
<
\frac{7S^2}{\chi^2_7(0.975)}.
\]

Using the transcript’s table values:

\[
\chi^2_7(0.025)=16.13,
\]

and

\[
\chi^2_7(0.975)=1.69.
\]

The lower limit is

\[
\frac{7(14.2679)}{16.13}.
\]

Calculate the numerator:

\[
7(14.2679)=99.8753.
\]

Then

\[
\frac{99.8753}{16.13}=6.1919\ldots
\]

Using the transcript’s rounded working, the lower limit is approximately

\[
6.237.
\]

The upper limit is

\[
\frac{7(14.2679)}{1.69}.
\]

So

\[
\frac{99.8753}{1.69}=59.0978\ldots
\]

Thus the \(95\%\) confidence interval for the population variance is approximately

\[
\boxed{6.237<\sigma^2<59.098}
\]

to three decimal places.

### Teaching note

The denominator with \(0.025\) gives the lower bound because \(\chi^2_7(0.025)\) is the large upper-tail critical value. The big denominator makes the fraction smaller. Tiny table gremlin, huge consequence.

## Worked Example 2: Hypothesis test for one variance

### Evidence source

Teacher transcript, Chi-squared Distribution for Variance 3.

### On-spec status

Off-spec enrichment.

### Question

A random sample of \(12\) observations is taken from a normal distribution with variance \(\sigma^2\). The unbiased estimate of the population variance is

\[
S^2=0.015.
\]

Test at the \(5\%\) level the null hypothesis

\[
H_0:\sigma^2=0.03
\]

against

\[
H_1:\sigma^2\neq0.03.
\]

### Solution

The sample size is

\[
n=12.
\]

So the degrees of freedom are

\[
\nu=n-1=11.
\]

The hypotheses are:

\[
H_0:\sigma^2=0.03,
\]

\[
H_1:\sigma^2\neq0.03.
\]

This is a two-tailed test.

The test statistic is

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Under \(H_0\),

\[
\sigma_0^2=0.03.
\]

Substitute:

\[
T=\frac{11(0.015)}{0.03}.
\]

Calculate the numerator:

\[
11(0.015)=0.165.
\]

Then

\[
T=\frac{0.165}{0.03}=5.5.
\]

So

\[
T=5.5.
\]

At the \(5\%\) level for a two-tailed test, each tail has probability

\[
2.5\%=0.025.
\]

Using \(\chi^2_{11}\) critical values:

\[
\chi^2_{11}(0.975)=3.816,
\]

and

\[
\chi^2_{11}(0.025)=21.92.
\]

The critical regions are:

\[
T<3.816
\]

or

\[
T>21.92.
\]

But

\[
3.816<5.5<21.92.
\]

So \(T=5.5\) is not in the critical region.

Therefore the result is not significant.

There is insufficient evidence to reject \(H_0\).

### Final answer

\[
\boxed{\text{There is insufficient evidence at the }5\%\text{ level to suggest that the variance differs from }0.03.}
\]

The variance is still thought to be

\[
0.03.
\]

## Worked Example 3: Hypothesis test for standard deviation using variance

### Evidence source

Teacher transcript, tyre-change example.

### On-spec status

Off-spec enrichment.

### Question

A mechanic is required to change car tyres. An inspector timed a random sample of \(20\) tyre changes and calculated the unbiased estimate of the population variance to be

\[
S^2=6.25\text{ minutes}^2.
\]

Test at the \(5\%\) significance level whether or not the standard deviation of the population times taken by the mechanic is greater than \(2\) minutes.

State one necessary assumption.

### Solution

The question is about the standard deviation, but the test is easier in terms of variance.

If the standard deviation is \(2\), then the variance is

\[
2^2=4.
\]

So the hypotheses are:

\[
H_0:\sigma^2=4,
\]

\[
H_1:\sigma^2>4.
\]

This is an upper-tailed test because the alternative says the variance is greater.

The sample size is

\[
n=20.
\]

So the degrees of freedom are

\[
\nu=n-1=19.
\]

The test statistic is

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Under \(H_0\),

\[
\sigma_0^2=4.
\]

Substitute:

\[
T=\frac{19(6.25)}{4}.
\]

Calculate:

\[
19(6.25)=118.75.
\]

So

\[
T=\frac{118.75}{4}.
\]

\[
T=29.6875.
\]

At the \(5\%\) significance level, using the upper-tail critical value:

\[
\chi^2_{19}(0.05)=30.144.
\]

The critical region is:

\[
T>30.144.
\]

But

\[
29.6875<30.144.
\]

So \(T\) is not in the critical region.

Therefore the result is not significant.

There is insufficient evidence to reject \(H_0\).

### Final answer

\[
\boxed{\text{There is insufficient evidence at the }5\%\text{ level to suggest that the standard deviation is greater than }2\text{ minutes.}}
\]

### Necessary assumption

The times taken to change tyres are normally distributed.

### Teaching note

The observed sample standard deviation is

\[
\sqrt{6.25}=2.5.
\]

That looks bigger than \(2\), but the statistical test says this sample evidence is not strong enough. The sample puffed itself up a bit, but not enough to convict.

## Worked Example 4: \(F\)-test for two variances

### Evidence source

Teacher transcript, F-distribution and F-test sections.

### On-spec status

Off-spec enrichment.

### Question

Gina receives packages from two companies, A and B. She believes that the variance of the weights of packages from company A is greater than the variance of the weights of packages from company B.

She takes:

\[
n_A=7
\]

packages from company A and

\[
n_B=10
\]

packages from company B.

Suppose the unbiased sample variances are:

\[
S_A^2=24249.333\ldots
\]

and

\[
S_B^2=6262.711\ldots
\]

Assume the package weights are normally distributed.

Test Gina’s belief at the \(5\%\) level.

### Solution

The hypotheses are:

\[
H_0:\sigma_A^2=\sigma_B^2,
\]

\[
H_1:\sigma_A^2>\sigma_B^2.
\]

This is an upper-tailed \(F\)-test.

Use the statistic:

\[
F=\frac{S_A^2}{S_B^2}.
\]

Substitute:

\[
F=\frac{24249.333\ldots}{6262.711\ldots}.
\]

Calculate:

\[
F=3.872\ldots
\]

So

\[
F\approx3.87.
\]

The degrees of freedom are:

\[
\nu_1=n_A-1=7-1=6,
\]

and

\[
\nu_2=n_B-1=10-1=9.
\]

Under \(H_0\),

\[
F\sim F_{6,9}.
\]

At the \(5\%\) significance level, the upper-tail critical value is

\[
F_{6,9}(0.05).
\]

From tables, suppose

\[
F_{6,9}(0.05)\approx3.37.
\]

The critical region is

\[
F>3.37.
\]

Since

\[
3.87>3.37,
\]

the test statistic lies in the critical region.

Therefore the result is significant.

Reject \(H_0\).

### Final answer

\[
\boxed{\text{There is sufficient evidence at the }5\%\text{ level to support Gina’s belief that company A has greater variance in package weights.}}
\]

### Teaching note

The numerator was chosen as \(S_A^2\) because Gina’s belief is

\[
\sigma_A^2>\sigma_B^2.
\]

That makes the alternative line up with an upper-tail test.

---

# 12. Common Mistakes and Exam Traps

| Trap | Why it happens | How to avoid it |
|---|---|---|
| Using \(n\) instead of \(n-1\) | Ordinary variance formula habits | For unbiased sample variance, use \(S^2=\frac{\sum(X_i-\bar X)^2}{n-1}\) |
| Treating \(S^2\) as normally distributed | Mean inference habits | Use \(\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}\) for normal populations |
| Forgetting the normality assumption | The test method feels mechanical | Always state the population is normally distributed |
| Confusing variance with standard deviation | The question asks about \(\sigma\), but the test uses \(\sigma^2\) | Square standard deviations before testing variance |
| Forgetting squared units | Variance has squared units | If time is minutes, variance is minutes squared |
| Misreading upper-tail tables | A small probability gives a large critical value | Remember \(\chi^2_\nu(0.025)\) is large |
| Not reversing inequalities when taking reciprocals | Algebra autopilot | Positive reciprocals reverse order |
| Swapping \(F\) degrees of freedom | \(F_{\nu_1,\nu_2}\) looks symmetrical but is not | Numerator variance gives \(\nu_1\), denominator variance gives \(\nu_2\) |
| Splitting a one-tailed test | Two-tail habits | Only split \(\alpha\) when \(H_1\) says \(\neq\) |
| Not splitting a two-tailed test | One-tail habits | If \(H_1:\sigma^2\neq\sigma_0^2\), use \(\alpha/2\) in each tail |
| Saying “accept \(H_0\)” | Overclaims the test | Say “insufficient evidence to reject \(H_0\)” |
| Ignoring context | Maths done, meaning abandoned | Final sentence must answer the real-world claim |

---

# 13. Practice Questions

These are generated enrichment questions. They are not past-paper or textbook questions.

## Basic fluency

### Question 1

A random sample of size \(9\) is taken from a normal population. Write down the distribution of

\[
\frac{(n-1)S^2}{\sigma^2}.
\]

### Question 2

For a random sample of size \(15\), what are the degrees of freedom used in

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_\nu?
\]

### Question 3

A sample has

\[
n=10,\qquad S^2=4.8.
\]

Calculate

\[
(n-1)S^2.
\]

## Bridge questions

### Question 4

Explain why

\[
\sum_{i=1}^{n}(X_i-\bar X)=0.
\]

### Question 5

A question asks whether the standard deviation is greater than \(3\). Write the equivalent variance hypotheses.

## Standard exam-style questions

### Question 6

A random sample of size \(12\) from a normal population has unbiased sample variance

\[
S^2=18.4.
\]

Find a \(95\%\) confidence interval for the population variance \(\sigma^2\), given:

\[
\chi^2_{11}(0.025)=21.92,
\]

and

\[
\chi^2_{11}(0.975)=3.816.
\]

### Question 7

A random sample of size \(16\) from a normal population has

\[
S^2=7.2.
\]

Test, at the \(5\%\) significance level,

\[
H_0:\sigma^2=5
\]

against

\[
H_1:\sigma^2>5.
\]

Use

\[
\chi^2_{15}(0.05)=24.996.
\]

### Question 8

Two independent random samples are taken from normal populations.

Sample A:

\[
n_A=8,\qquad S_A^2=14.5.
\]

Sample B:

\[
n_B=11,\qquad S_B^2=6.2.
\]

Test at the \(5\%\) level whether the variance of population A is greater than the variance of population B.

Use

\[
F_{7,10}(0.05)=3.14.
\]

## Harder synthesis

### Question 9

A manufacturer claims that the variance of fuse-breaking currents is

\[
0.020.
\]

A random sample of \(10\) fuses from a normal population gives

\[
\sum X=18.9,
\]

and

\[
\sum X^2=36.01.
\]

Test at the \(5\%\) level whether the variance differs from the claimed value.

Use:

\[
\chi^2_9(0.025)=19.02,
\]

\[
\chi^2_9(0.975)=2.70.
\]

---

# 14. Worked Solutions

## Solution 1

Given

\[
n=9.
\]

For a normal population,

\[
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
\]

So

\[
n-1=9-1=8.
\]

Therefore

\[
\boxed{\frac{8S^2}{\sigma^2}\sim\chi^2_8.}
\]

## Solution 2

Given

\[
n=15.
\]

The degrees of freedom are

\[
\nu=n-1.
\]

So

\[
\nu=15-1=14.
\]

\[
\boxed{14}
\]

## Solution 3

Given

\[
n=10,\qquad S^2=4.8.
\]

Calculate:

\[
(n-1)S^2=(10-1)(4.8).
\]

\[
=9(4.8).
\]

\[
=43.2.
\]

\[
\boxed{43.2}
\]

## Solution 4

Start with

\[
\sum_{i=1}^{n}(X_i-\bar X).
\]

Expand the summation:

\[
\sum_{i=1}^{n}(X_i-\bar X)
=
\sum_{i=1}^{n}X_i-\sum_{i=1}^{n}\bar X.
\]

Since \(\bar X\) is constant,

\[
\sum_{i=1}^{n}\bar X=n\bar X.
\]

Also,

\[
\bar X=\frac{\sum_{i=1}^{n}X_i}{n}.
\]

Multiplying by \(n\),

\[
n\bar X=\sum_{i=1}^{n}X_i.
\]

Therefore

\[
\sum_{i=1}^{n}(X_i-\bar X)
=
\sum_{i=1}^{n}X_i-n\bar X.
\]

But

\[
n\bar X=\sum_{i=1}^{n}X_i.
\]

So

\[
\sum_{i=1}^{n}(X_i-\bar X)=0.
\]

\[
\boxed{\sum_{i=1}^{n}(X_i-\bar X)=0}
\]

## Solution 5

The claim is about standard deviation:

\[
\sigma>3.
\]

Square both sides to convert to variance:

\[
\sigma^2>9.
\]

The null hypothesis is equality:

\[
H_0:\sigma^2=9.
\]

The alternative hypothesis is:

\[
H_1:\sigma^2>9.
\]

\[
\boxed{H_0:\sigma^2=9,\qquad H_1:\sigma^2>9}
\]

## Solution 6

Given:

\[
n=12,
\]

\[
S^2=18.4.
\]

Degrees of freedom:

\[
\nu=n-1=11.
\]

For a \(95\%\) confidence interval,

\[
\frac{(n-1)S^2}{\chi^2_{n-1}(0.025)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{n-1}(0.975)}.
\]

Substitute:

\[
\frac{11(18.4)}{21.92}
<
\sigma^2
<
\frac{11(18.4)}{3.816}.
\]

Calculate the numerator:

\[
11(18.4)=202.4.
\]

Lower limit:

\[
\frac{202.4}{21.92}=9.2335\ldots
\]

Upper limit:

\[
\frac{202.4}{3.816}=53.0398\ldots
\]

So the confidence interval is:

\[
\boxed{9.23<\sigma^2<53.04}
\]

to two decimal places.

## Solution 7

Given:

\[
n=16,\qquad S^2=7.2.
\]

The hypotheses are:

\[
H_0:\sigma^2=5,
\]

\[
H_1:\sigma^2>5.
\]

This is an upper-tailed test.

Degrees of freedom:

\[
\nu=n-1=16-1=15.
\]

The test statistic is

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Substitute:

\[
T=\frac{15(7.2)}{5}.
\]

Calculate:

\[
15(7.2)=108.
\]

So

\[
T=\frac{108}{5}=21.6.
\]

Critical value:

\[
\chi^2_{15}(0.05)=24.996.
\]

Critical region:

\[
T>24.996.
\]

But

\[
21.6<24.996.
\]

So \(T\) is not in the critical region.

There is insufficient evidence to reject \(H_0\).

\[
\boxed{\text{There is insufficient evidence at the }5\%\text{ level that the variance is greater than }5.}
\]

## Solution 8

Given:

\[
n_A=8,\qquad S_A^2=14.5,
\]

\[
n_B=11,\qquad S_B^2=6.2.
\]

The hypotheses are:

\[
H_0:\sigma_A^2=\sigma_B^2,
\]

\[
H_1:\sigma_A^2>\sigma_B^2.
\]

Use

\[
F=\frac{S_A^2}{S_B^2}.
\]

Substitute:

\[
F=\frac{14.5}{6.2}.
\]

Calculate:

\[
F=2.3387\ldots
\]

So

\[
F\approx2.34.
\]

Degrees of freedom:

\[
\nu_1=n_A-1=8-1=7,
\]

\[
\nu_2=n_B-1=11-1=10.
\]

Under \(H_0\),

\[
F\sim F_{7,10}.
\]

Critical value:

\[
F_{7,10}(0.05)=3.14.
\]

Critical region:

\[
F>3.14.
\]

But

\[
2.34<3.14.
\]

So \(F\) is not in the critical region.

There is insufficient evidence to reject \(H_0\).

\[
\boxed{\text{There is insufficient evidence at the }5\%\text{ level that population A has greater variance than population B.}}
\]

## Solution 9

Given:

\[
n=10,
\]

\[
\sum X=18.9,
\]

\[
\sum X^2=36.01.
\]

The claim is:

\[
\sigma^2=0.020.
\]

The hypotheses are:

\[
H_0:\sigma^2=0.020,
\]

\[
H_1:\sigma^2\neq0.020.
\]

This is a two-tailed test.

First calculate the sample mean:

\[
\bar X=\frac{\sum X}{n}.
\]

\[
\bar X=\frac{18.9}{10}=1.89.
\]

Calculate the unbiased sample variance:

\[
S^2=\frac{\sum X^2-n\bar X^2}{n-1}.
\]

Substitute:

\[
S^2=\frac{36.01-10(1.89)^2}{9}.
\]

Calculate:

\[
1.89^2=3.5721.
\]

Then

\[
10(1.89)^2=10(3.5721)=35.721.
\]

So

\[
36.01-35.721=0.289.
\]

Therefore

\[
S^2=\frac{0.289}{9}=0.032111\ldots
\]

So

\[
S^2\approx0.03211.
\]

The degrees of freedom are:

\[
\nu=n-1=9.
\]

The test statistic is:

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Substitute:

\[
T=\frac{9(0.032111\ldots)}{0.020}.
\]

But

\[
9(0.032111\ldots)=0.289.
\]

So

\[
T=\frac{0.289}{0.020}=14.45.
\]

At the \(5\%\) level, two-tailed, the critical regions are:

\[
T<\chi^2_9(0.975)
\]

or

\[
T>\chi^2_9(0.025).
\]

Given:

\[
\chi^2_9(0.975)=2.70,
\]

\[
\chi^2_9(0.025)=19.02.
\]

So the critical regions are:

\[
T<2.70
\]

or

\[
T>19.02.
\]

But

\[
2.70<14.45<19.02.
\]

So \(T\) is not in the critical region.

There is insufficient evidence to reject \(H_0\).

\[
\boxed{\text{There is insufficient evidence at the }5\%\text{ level that the variance differs from }0.020.}
\]

---

# 15. Exam Technique Notes

Even though this is off-spec for CCEA, the technique is worth learning because it sharpens your statistics instincts.

## For \(\chi^2\) variance confidence intervals

Use:

\[
\frac{(n-1)S^2}{\chi^2_{n-1}(\alpha/2)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{n-1}(1-\alpha/2)}.
\]

For \(95\%\):

\[
\frac{(n-1)S^2}{\chi^2_{n-1}(0.025)}
<
\sigma^2
<
\frac{(n-1)S^2}{\chi^2_{n-1}(0.975)}.
\]

## For one-variance \(\chi^2\) hypothesis tests

Use:

\[
T=\frac{(n-1)S^2}{\sigma_0^2}.
\]

Then compare with:

\[
\chi^2_{n-1}.
\]

## For \(F\)-tests

Use:

\[
F=\frac{S_1^2}{S_2^2}.
\]

Degrees of freedom:

\[
\nu_1=n_1-1,
\]

\[
\nu_2=n_2-1.
\]

Then:

\[
F\sim F_{\nu_1,\nu_2}.
\]

## Always state assumptions

For variance tests:

\[
\boxed{\text{The population is normally distributed.}}
\]

For \(F\)-tests:

\[
\boxed{\text{The two samples are independent and come from normal populations.}}
\]

## Standard deviation wording

If the question asks about standard deviation, convert to variance before testing.

Example:

\[
\sigma>2
\]

means

\[
\sigma^2>4.
\]

## Conclusion language

Avoid:

\[
\text{“Accept }H_0\text{.”}
\]

Use:

\[
\text{“There is insufficient evidence to reject }H_0\text{.”}
\]

or

\[
\text{“There is sufficient evidence to reject }H_0\text{.”}
\]

---

# 16. Syllabus Gap Check

## LO coverage table

| Item | Covered? | Status |
|---|---:|---|
| `FA22-EST-LO002`: \(S^2\) as unbiased estimator of \(\sigma^2\) | Yes | On-spec overlap |
| \(\chi^2\) distribution for variance | Yes | Off-spec enrichment |
| Confidence interval for \(\sigma^2\) | Yes | Off-spec enrichment |
| Hypothesis test for one variance | Yes | Off-spec enrichment |
| \(F\)-distribution | Yes | Off-spec enrichment |
| \(F\)-test comparing two variances | Yes | Off-spec enrichment |
| CCEA \(\chi^2\) goodness-of-fit | No | Separate CCEA topic |
| CCEA \(\chi^2\) independence test | No | Separate CCEA topic |
| CCEA \(t\)-tests for means | No | Separate CCEA topic |

## Evidence coverage table

| Evidence item | Included? | Notes |
|---|---:|---|
| Chapter split into 6A \(\chi^2\) variance and 6B \(F\)-distribution | Yes | Metadata and big picture |
| \(S^2\) is unbiased for \(\sigma^2\) | Yes | Definitions and theory |
| \(S^2\) not normally distributed | Yes | Big picture |
| \(\chi^2\) as sum of squared standard normals | Yes | Core theory |
| Derivation of \((n-1)S^2/\sigma^2\) | Yes | Core theory |
| Confidence interval derivation | Yes | Core theory |
| One-sample variance tests | Yes | Worked examples |
| \(F\)-distribution theory | Yes | Core theory |
| \(F\)-test examples | Yes | Worked examples |
| DrFrost test-selection context | Partly | Supplementary only |

## Off-Spec Content Found but Excluded from Core CCEA

This entire lesson is excluded from the core CCEA lesson library unless official CCEA evidence is later supplied.

The only core-safe overlap is:

\[
S^2=\frac{\sum(X_i-\bar X)^2}{n-1}.
\]

## Weak evidence warnings

- The screenshot PDF is image-based and has no parsed text.
- Only visible/rendered screenshot details and transcript text were used.
- Some transcript numerical examples refer to textbook/table values without the full textbook extract being supplied.
- The \(F\)-test example table value in this lesson is treated as a representative enrichment value, not an official CCEA requirement.

---

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements, not evidence-backed source content.

1. A dynamic \(\chi^2\) curve showing how degrees of freedom change the shape.
2. A slider showing how \(n\), \(S^2\) and \(\sigma_0^2\) affect
   \[
   T=\frac{(n-1)S^2}{\sigma_0^2}.
   \]
3. A “table value translator” widget for upper-tail \(\chi^2\) notation.
4. A reciprocal-rule animation for \(F\)-distributions:
   \[
   F_{\nu_1,\nu_2}<a
   \quad\Longleftrightarrow\quad
   F_{\nu_2,\nu_1}>\frac{1}{a}.
   \]
5. A comparison table:
   - test for mean;
   - test for variance;
   - test for two variances.
6. A warning card titled “Same hypothesis-test skeleton, different distribution beast.”

---

# 18. Supplementary Sources Used

| Source | Use |
|---|---|
| CCEA Further Mathematics Specification Map | Boundary authority, confirming no exact CCEA LO found for this full topic |
| Further Maths README module map | Project structure and naming rules |
| Further Maths Evidence Drop Checklist | Evidence handling and off-spec logging |
| Ordinary A-Level Maths Bridge Extracts | Bridge context only |
| `transcripts.md` | Main enrichment lesson evidence |
| `Chapter_6_Further_Hypothesis_Tests_📈_(Further_Statistics_2)_screenshots.pdf` | Visual confirmation of chapter topic split |
| `Which Hypothesis Test Poster.pdf` | Supplementary test-selection context |

Ordinary A-Level Maths sources are used as bridge context only. They do not authorise this content as CCEA Further Mathematics core.

Cross-board and third-party material is used only as enrichment.

---

# 19. Final Student Checklist

## Prerequisite confidence checklist

- [ ] I can calculate \(\bar X\).
- [ ] I can calculate \(S^2\) using denominator \(n-1\).
- [ ] I know the difference between variance and standard deviation.
- [ ] I can standardise a normal variable using
  \[
  Z=\frac{X-\mu}{\sigma}.
  \]
- [ ] I can state hypotheses \(H_0\) and \(H_1\).
- [ ] I understand one-tailed and two-tailed tests.

## Variance inference checklist

- [ ] I know that
  \[
  \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
  \]
- [ ] I can explain why \(n-1\) appears.
- [ ] I can use \(\chi^2\) critical values with upper-tail notation.
- [ ] I can construct a confidence interval for \(\sigma^2\).
- [ ] I remember that reciprocals reverse inequality signs.
- [ ] I can test a claim about one population variance.

## F-distribution checklist

- [ ] I know that
  \[
  F=\frac{U/\nu_1}{V/\nu_2}
  \]
  where \(U,V\) are independent \(\chi^2\) variables.
- [ ] I can use
  \[
  F=\frac{S_1^2}{S_2^2}
  \]
  under
  \[
  H_0:\sigma_1^2=\sigma_2^2.
  \]
- [ ] I know that the numerator variance controls \(\nu_1\).
- [ ] I know that the denominator variance controls \(\nu_2\).
- [ ] I remember that order matters:
  \[
  F_{\nu_1,\nu_2}\neq F_{\nu_2,\nu_1}.
  \]
- [ ] I can use the reciprocal rule for lower-tail \(F\)-values.

## Modelling checklist

- [ ] I state that the population is normally distributed for \(\chi^2\) variance inference.
- [ ] I state that both populations are normally distributed for an \(F\)-test.
- [ ] I state that the two samples are independent for an \(F\)-test.
- [ ] I interpret the final conclusion in context.

## CCEA boundary checklist

- [ ] I know this is off-spec enrichment.
- [ ] I know the CCEA-safe overlap is \(S^2\) as an unbiased estimator of \(\sigma^2\).
- [ ] I will not treat variance confidence intervals or \(F\)-tests as required CCEA content unless official CCEA evidence is supplied.
