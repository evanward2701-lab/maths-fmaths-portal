# Central Limit Theorem

## 1. Lesson Title and Metadata

| Metadata field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FA22-EST` |
| CCEA topic area | Sampling and estimation |
| Lesson topic | Central Limit Theorem |
| Topic slug | `central_limit_theorem` |
| Topic Pascal | `CentralLimitTheorem` |
| Topic ID | `FA22CentralLimitTheorem` |
| Lesson file name | `FA22_central_limit_theorem_lesson.md` |
| Core LO IDs | `FA22-EST-LO001` |
| Connected LO IDs | `FA22-EST-LO003`, `FA22-LINCOMB-LO002` |
| Prerequisite Further Maths LO IDs | `FAS2-DIST-LO002`, `FAS2-DIST-LO003`, `FAS2-DIST-LO008` |
| Bridge tags | `#Sampling`, `#NormalDistribution`, `#Standardisation`, `#Variance`, `#StandardDeviation`, `#BinomialDistribution`, `#HypothesisTesting` |
| Topic tags | `#FA22`, `#EST`, `#Statistics`, `#CentralLimitTheorem`, `#SampleMean`, `#StandardError`, `#NormalApproximation`, `#CalculatorCDF`, `#InverseNormal` |

This lesson is a Further Maths sampling-distribution lesson. The main object is not a single observation \(X\), but the sample mean \(\bar X\). The governing CCEA boundary is: use the central limit theorem for samples of 30 or more observations.

---

## 2. Evidence Map

| Evidence source | Lesson use |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Establishes `FA22-EST`, Section C Statistics, and core LO `FA22-EST-LO001`. |
| `Further_Maths_README_module_map.md` | Confirms applied/statistics structure and bridge dependencies. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Supplies evidence-intake, off-spec logging and missing-evidence protocol. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge context only: sampling, normal distribution, variance, standardisation and hypothesis testing. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary A-Level bridge context only. |
| `transcripts.md` | Teacher transcript for Chapter 5 Central Limit Theorem; used for intuition, warnings, notation, calculator guidance and minimum sample-size methods. |
| `FS1-Chp5-CentralLimitTheorem.pdf` | DrFrost/Pearson Further Statistics 1 slide PDF; used for theorem statement, spinner diagrams and worked examples. |
| `Chapter_5_Central_Limit_Theorem_📊_(Further_Statistics_1)_screenshots.pdf` | Screenshot PDF; used as visual evidence only because parsed text was unavailable. |

---

## 3. Specification Alignment

| CCEA LO ID | Official wording | Lesson coverage | Syllabus boundary | Bridge |
|---|---|---|---|---|
| `FA22-EST-LO001` | Demonstrate understanding of and use the central limit theorem for samples of 30 or more observations. | Core theorem, interpretation, probability calculations, standardisation and minimum sample-size questions. | Core. Use \(n\ge 30\) for CLT unless the original population is normal. | A22 normal distribution and standardisation. |
| `FA22-EST-LO003` | Demonstrate understanding of and use the standard error of the mean. | Define \(\operatorname{SD}(\bar X)=\sigma/\sqrt n\); connect to calculator input. | Supporting. | Ordinary standard deviation and normal calculator use. |
| `FA22-LINCOMB-LO002` | Solve problems involving linear combinations of independent normally distributed variables, including sums of observations from a population. | Explains why \(\bar X\) is normal if \(X\) is already normal. | Connected support. | A22 normal distribution. |

---

## 4. Learning Objectives

### Core Further Maths objectives

1. State the Central Limit Theorem:
   \[
   \bar X \approx N\left(\mu,\frac{\sigma^2}{n}\right).
   \]
2. Explain that \(X\) is one observation, while \(\bar X\) is the mean of a sample.
3. Use \(E(X)=\mu\) and \(\operatorname{Var}(X)=\sigma^2\) to build the sampling distribution of \(\bar X\).
4. Calculate probabilities involving \(\bar X\).
5. Use the standard error \(\sigma/\sqrt n\) as the calculator standard deviation.
6. Solve inverse-normal and minimum-sample-size CLT questions.

### Bridge objectives

Recall population, sample and sample mean; use variance and standard deviation correctly; standardise using \(Z=(X-\mu)/\sigma\); recognise normal CDF and inverse-normal methods.

### Exam technique objectives

Spot “mean” or “average” as a CLT clue, write the distribution of \(\bar X\) before calculating, avoid typing variance into the calculator, and round minimum sample sizes according to the inequality.

---

## 5. Explicit Prerequisite Recap

### GCSE foundations

Means, probability tables, fractions/decimals, inequality language, square roots and rearranging inequalities.

### Ordinary AS/A2 Mathematics foundations

\[
X\sim N(\mu,\sigma^2),\qquad Z=\frac{X-\mu}{\sigma}.
\]

### Previous Further Mathematics foundations

| Further Maths prerequisite | Needed here because |
|---|---|
| Discrete probability distributions | Some CLT examples start from a table. |
| \(E(X)\) and \(\operatorname{Var}(X)\) | These become \(\mu\) and \(\sigma^2\). |
| Mean and variance of binomial, geometric and Poisson distributions | These allow CLT without a full probability table. |
| Linear combinations of independent variables | Helps explain sums and sample means. |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary AS2 Sampling | Population and sample. | We study the distribution of a statistic, especially \(\bar X\). | A sample mean is not automatically equal to \(\mu\). |
| Ordinary AS2 Data presentation | Mean, variance and standard deviation. | \(\mu\) and \(\sigma^2\) become population inputs for the sampling distribution. | Do not mix up \(\sigma^2\) and \(\sigma\). |
| Ordinary A22 Normal distribution | Use \(N(\mu,\sigma^2)\), standardisation and normal CDF/inverse normal. | Even when \(X\) is not normal, \(\bar X\) may be approximately normal for large \(n\). | Calculator uses standard deviation, so enter \(\sqrt{\sigma^2/n}\). |
| Ordinary A22 Hypothesis testing | A sample mean can be compared with a hypothesised mean. | CLT explains why sampling distributions of means can be used more generally. | Do not run a tail calculation before writing the \(\bar X\) distribution. |
| Ordinary AS2 Binomial distribution | Binomial probabilities, mean and variance. | Binomial, Poisson and geometric models can feed into CLT. | The binomial trial count is not necessarily the CLT sample size. |

In ordinary A-Level Maths, the object was often one random variable \(X\). In Further Maths, the object is often
\[
\bar X=\frac{X_1+X_2+\cdots+X_n}{n}.
\]
The key upgrade is modelling the mean of a sample. The danger is entering \(\sigma^2/n\) into the calculator instead of \(\sigma/\sqrt n\).

---

## 6. Big Picture Explanation

The Central Limit Theorem says that if you repeatedly take random samples of the same size, then the sample means form an approximately normal distribution when the sample size is large. You may start with a skewed, discrete or uneven population, but the averages gather into a bell-shaped distribution.

If \(X\) is one observation and
\[
E(X)=\mu,\qquad \operatorname{Var}(X)=\sigma^2,
\]
then for large \(n\),
\[
\bar X \approx N\left(\mu,\frac{\sigma^2}{n}\right).
\]
The mean stays \(\mu\). The variance shrinks to \(\sigma^2/n\). For CCEA, use the CLT approximation for \(n\ge 30\), unless the population is already normal.

---

## 7. Key Definitions and Notation

The population distribution is the distribution from which individual observations are taken. A single observation is \(X\). A random sample of size \(n\) is
\[
X_1,X_2,\ldots,X_n.
\]
The sample mean is
\[
\bar X=\frac{X_1+X_2+\cdots+X_n}{n}.
\]
The population mean and variance are
\[
\mu=E(X),\qquad \sigma^2=\operatorname{Var}(X).
\]
By CLT,
\[
\bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right).
\]
The standard error is
\[
\operatorname{SD}(\bar X)=\sqrt{\frac{\sigma^2}{n}}=\frac{\sigma}{\sqrt n}.
\]
Notation warning: \(\bar X\) is a random variable; \(\bar x\) is an observed value.

---

## 8. Core Theory

### 8.1 Formal statement

Let \(X_1,\ldots,X_n\) be a random sample from a population with mean \(\mu\) and variance \(\sigma^2\). Then, for large \(n\),
\[
\boxed{\bar X \approx N\left(\mu,\frac{\sigma^2}{n}\right).}
\]
For CCEA FA22, the safe large-sample boundary is \(n\ge 30\).

**Bridge Note:** In ordinary A-Level Maths, normal work usually modelled \(X\). Here, Further Maths models \(\bar X\).

### 8.2 Why the mean stays the same

\[
E(\bar X)=E\left(\frac{X_1+\cdots+X_n}{n}\right)=\frac1n(E(X_1)+\cdots+E(X_n)).
\]
Since every \(X_i\) has mean \(\mu\),
\[
E(\bar X)=\frac1n(n\mu)=\mu.
\]

### 8.3 Why the variance is divided by \(n\)

\[
\operatorname{Var}(\bar X)=\operatorname{Var}\left(\frac{X_1+\cdots+X_n}{n}\right)=\frac1{n^2}\operatorname{Var}(X_1+\cdots+X_n).
\]
For independent observations, variances add:
\[
\operatorname{Var}(X_1+\cdots+X_n)=n\sigma^2.
\]
Therefore
\[
\operatorname{Var}(\bar X)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}.
\]

### 8.4 Standard error and calculator input

\[
\operatorname{SE}(\bar X)=\sqrt{\frac{\sigma^2}{n}}=\frac{\sigma}{\sqrt n}.
\]
The calculator wants the standard deviation, not the variance.

### 8.5 Method checklist

1. Identify \(X\).
2. Find \(\mu=E(X)\).
3. Find \(\sigma^2=\operatorname{Var}(X)\).
4. Identify the CLT sample size \(n\).
5. Write \(\bar X\approx N(\mu,\sigma^2/n)\).
6. Use normal CDF, inverse normal or standardisation.
7. Interpret the result.

### 8.6 What \(\bar X\) means for different distributions

| Original distribution | What \(X\) measures | What \(\bar X\) measures |
|---|---|---|
| Normal | One measurement | Mean of \(n\) measurements |
| Tabulated discrete | One score | Mean score from \(n\) repeats |
| Poisson | Events in one interval | Mean events across \(n\) intervals |
| Binomial | Successes in one set of trials | Mean successes across \(n\) repeated sets |
| Geometric | Attempts until first success | Mean attempts across \(n\) repeated experiments |
| Negative binomial | Attempts until \(r\) successes | Mean attempts across \(n\) repeated experiments |

### 8.7 When CLT applies

If \(n\ge 30\), then CLT gives an approximate normal model for \(\bar X\). If \(X\) is already normal, then \(\bar X\) is normal even for smaller \(n\). If \(n=1\), then \(\bar X=X\).

### 8.8 Standardising \(\bar X\)

\[
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}.
\]
So
\[
P(\bar X>a)=P\left(Z>\frac{a-\mu}{\sigma/\sqrt n}\right).
\]

### 8.9 Inverse normal and minimum \(n\)

For threshold questions, use inverse normal with mean \(\mu\) and standard deviation \(\sigma/\sqrt n\). For minimum sample size, standardise first and solve the inequality in \(n\).

Example:
\[
\bar X\approx N\left(50,\frac{25}{n}\right),\qquad P(\bar X>52)<0.05.
\]
Then
\[
P\left(Z>\frac{52-50}{5/\sqrt n}\right)<0.05,
\]
so
\[
P\left(Z>\frac{2\sqrt n}{5}\right)<0.05.
\]
Since \(P(Z>1.64485)=0.05\), require
\[
\frac{2\sqrt n}{5}>1.64485.
\]
Hence
\[
\sqrt n>4.112125,
\]
\[
n>16.909\ldots,
\]
and
\[
\boxed{n_{\min}=17.}
\]

---

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremSVG-001 | Source: Screenshot PDF pages showing multiple small source distributions feeding by yellow arrows into a bell curve; DrFrost/Pearson CLT slides | Insert from svg/FA22CentralLimitTheoremSVG-001.svg | Purpose: Show the core CLT idea that many possible original population shapes can produce an approximately normal distribution of sample means.]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremSVG-002 | Source: FS1-Chp5-CentralLimitTheorem.pdf pages 3-4 | Insert from svg/FA22CentralLimitTheoremSVG-002.svg | Purpose: Rebuild the spinner example showing how adding repeated independent spinner outcomes produces a distribution that begins to resemble a normal distribution.]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremSVG-003 | Source: Teacher transcript explanation of \(\sigma^2/n\) and standard error | Insert from svg/FA22CentralLimitTheoremSVG-003.svg | Purpose: Show that increasing sample size narrows the sampling distribution of \(\bar X\).]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22CentralLimitTheoremBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremTikZ-001 | Source: CLT theorem + worked examples in transcript and slide PDF | Insert from tikz/FA22CentralLimitTheoremTikZ-001.tex | Purpose: Show how a sample-mean probability becomes a normal tail probability.]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremTikZ-002 | Source: Teacher transcript minimum sample-size method | Insert from tikz/FA22CentralLimitTheoremTikZ-002.tex | Purpose: Show why a strict tail-probability inequality becomes an inequality for \(n\).]

[VISUAL PLACEHOLDER: FA22CentralLimitTheoremMermaid-001 | Source: CCEA Further Maths specification + transcript method checklist | Insert from mermaid/FA22CentralLimitTheoremMermaid-001.md | Purpose: Give students an exam workflow for deciding when and how to use CLT.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22CentralLimitTheoremWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentralLimitTheoremWidget-001.html | Purpose: Let students build the sampling distribution of \(\bar X\) from \(\mu\), \(\sigma^2\), and \(n\).]

[INTERACTIVE PLACEHOLDER: FA22CentralLimitTheoremWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentralLimitTheoremWidget-002.html | Purpose: Prevent the common calculator error of typing \(\sigma^2/n\) instead of \(\sqrt{\sigma^2/n}\).]

[INTERACTIVE PLACEHOLDER: FA22CentralLimitTheoremWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentralLimitTheoremWidget-003.html | Purpose: Help students solve inverse-normal CLT questions involving an unknown \(n\).]

---

## 11. Worked Examples

### Worked Example 1: Normally distributed population, small sample size

A sample of size \(9\) is taken from \(N(10,2^2)\). Find \(P(\bar X>11)\).

\[
\bar X\sim N\left(10,\frac{2^2}{9}\right)=N\left(10,\left(\frac23\right)^2\right).
\]
Using normal CDF with \(\mu=10\) and \(\sigma=2/3\),
\[
\boxed{P(\bar X>11)=0.0668.}
\]

### Worked Example 2: Relabelled dice

A six-sided dice has three faces marked \(1\), two marked \(3\), and one marked \(6\). It is rolled \(40\) times.

| \(x\) | \(1\) | \(3\) | \(6\) |
|---|---:|---:|---:|
| \(P(X=x)\) | \(\frac12\) | \(\frac13\) | \(\frac16\) |

\[
E(X)=1\cdot\frac12+3\cdot\frac13+6\cdot\frac16=2.5.
\]
\[
E(X^2)=1^2\cdot\frac12+3^2\cdot\frac13+6^2\cdot\frac16=9.5.
\]
\[
\operatorname{Var}(X)=9.5-(2.5)^2=3.25=\frac{13}{4}.
\]
With \(n=40\),
\[
\boxed{\bar X\approx N\left(2.5,\frac{13}{160}\right).}
\]
Use \(\sigma=\sqrt{13/160}\):
\[
\boxed{P(\bar X>3)\approx 0.0397.}
\]
Evidence discrepancy: the slide value \(0.0401\) conflicts with the transcript/calculation value \(0.0397\); this is logged rather than hidden.

### Worked Example 3: Poisson arrivals

If \(X\sim\operatorname{Po}(20)\) is customers per minute, then \(E(X)=20\) and \(\operatorname{Var}(X)=20\). For \(60\) minutes,
\[
\bar X\approx N\left(20,\frac{20}{60}\right)=N\left(20,\frac13\right).
\]
For a total of \(1150\), the average is
\[
\frac{1150}{60}=19.1666\ldots.
\]
Thus
\[
P(T\le 1150)\approx P\left(\bar X\le \frac{1150}{60}\right)\approx 0.0744.
\]
This is close to the direct Poisson value \(0.07589\).

### Worked Example 4: Binomial teapots

If \(X\sim B(25,0.24)\), then
\[
E(X)=25(0.24)=6,
\]
\[
\operatorname{Var}(X)=25(0.24)(0.76)=4.56.
\]
For \(30\) samples,
\[
\bar X\approx N\left(6,\frac{4.56}{30}\right).
\]
Then
\[
\boxed{P(\bar X>5.5)=0.9002.}
\]
For \(P(\bar X<K)=0.90\), inverse normal gives
\[
\boxed{K=6.500.}
\]

### Worked Example 5: Minimum sample size

For \(\mu=50\), \(\sigma^2=25\), and \(P(\bar X>52)<0.05\),
\[
\bar X\approx N\left(50,\frac{25}{n}\right),
\]
\[
P\left(Z>\frac{52-50}{5/\sqrt n}\right)<0.05,
\]
\[
P\left(Z>\frac{2\sqrt n}{5}\right)<0.05.
\]
Since \(P(Z>1.64485)=0.05\),
\[
\frac{2\sqrt n}{5}>1.64485.
\]
Therefore
\[
n>16.909\ldots,
\]
so
\[
\boxed{n_{\min}=17.}
\]

### Worked Example 6: Two-sided minimum sample size

If \(\mu=0.4\), \(\sigma^2=0.3\), and we require \(P(0.35<\bar X<0.45)\ge 0.95\), each tail has probability \(0.025\). Using the upper tail,
\[
P\left(Z>\frac{0.45-0.4}{\sqrt{0.3}/\sqrt n}\right)\le 0.025.
\]
Since \(P(Z>1.95996)=0.025\),
\[
\frac{0.05\sqrt n}{\sqrt{0.3}}>1.95996.
\]
Thus
\[
n>460.97\ldots,
\]
so
\[
\boxed{n_{\min}=461.}
\]

### Worked Example 7: Fair die inverse-normal question

For a fair die,
\[
E(S)=\frac{1+2+3+4+5+6}{6}=3.5.
\]
\[
E(S^2)=\frac{1+4+9+16+25+36}{6}=\frac{91}{6}.
\]
\[
\operatorname{Var}(S)=\frac{91}{6}-(3.5)^2=\frac{35}{12}.
\]
For \(45\) rolls,
\[
\bar S\approx N\left(3.5,\frac{35/12}{45}\right)=N\left(3.5,\frac{7}{108}\right).
\]
For \(P(\bar S<K)=0.05\), inverse normal gives
\[
\boxed{K=3.08.}
\]

### Worked Example 8: Optional boundary-risk negative binomial example

If \(X\sim\operatorname{NegativeBinomial}(10,2/3)\), then
\[
E(X)=\frac{10}{2/3}=15,
\]
\[
\operatorname{Var}(X)=\frac{10(1/3)}{(2/3)^2}=7.5.
\]
For \(25\) matches,
\[
\bar X\approx N\left(15,\frac{7.5}{25}\right)=N(15,0.3).
\]
Using \(\sigma=\sqrt{0.3}\),
\[
\boxed{P(\bar X<15.5)=0.8193.}
\]
This remains optional boundary-risk content unless negative binomial is confirmed in the CCEA route.

---

## 12. Common Mistakes and Exam Traps

1. Treating \(X\) and \(\bar X\) as the same thing.
2. Entering \(\sigma^2/n\) into the calculator instead of \(\sqrt{\sigma^2/n}\).
3. Writing \(\operatorname{SD}(\bar X)=\sigma/n\) instead of \(\sigma/\sqrt n\).
4. Using CLT for small non-normal samples without justification.
5. Confusing binomial trials with the CLT sample size.
6. Forgetting to calculate \(E(X)\) and \(\operatorname{Var}(X)\) first.
7. Rounding minimum sample sizes incorrectly.
8. Losing the inequality direction in inverse-normal questions.
9. Failing to explain that CLT is relevant because the sample size is large and \(\bar X\) is approximately normal.
10. Treating enrichment such as the 3Blue1Brown video as core CCEA content.

---

## 13. Practice Questions

1. A population has \(\mu=80\), \(\sigma^2=36\), and \(n=64\). Find the distribution of \(\bar X\) and \(P(\bar X>81.5)\).
2. For \(X\) with values \(0,1,4\) and probabilities \(0.2,0.5,0.3\), find \(E(X)\), \(\operatorname{Var}(X)\), the distribution of \(\bar X\) for \(n=50\), and \(P(2<\bar X<2.8)\).
3. If \(X\sim N(50,16)\) and \(n=16\), find the distribution of \(\bar X\), calculate \(P(49<\bar X<51)\), and explain why large-sample CLT is not needed.
4. If \(E(X)=12\), \(\operatorname{Var}(X)=9\), find the minimum \(n\) such that \(P(\bar X>13)<0.01\).
5. Emails arrive according to \(\operatorname{Po}(3.2)\) per hour. For \(40\) hours, estimate \(P(\bar X<3)\).
6. If \(X\sim B(20,0.08)\), and \(35\) boxes are inspected, estimate \(P(\bar X>2)\).
7. A population has mean \(100\), variance \(25\), and \(n=36\). Find \(k\) such that \(P(\bar X<k)=0.95\).
8. A game score has values \(1,5,10\) with probabilities \(0.6,0.3,0.1\). For \(75\) plays, estimate \(P(3<\bar X<3.6)\).

---

## 14. Worked Solutions

1. \(\bar X\approx N(80,36/64)=N(80,9/16)\). Standard deviation \(=3/4\). \(P(\bar X>81.5)=P(Z>2)=0.0228\).
2. \(E(X)=1.7\). \(E(X^2)=5.3\). \(\operatorname{Var}(X)=5.3-1.7^2=2.41\). \(\bar X\approx N(1.7,2.41/50)=N(1.7,0.0482)\). \(P(2<\bar X<2.8)\approx0.0859\).
3. \(\bar X\sim N(50,16/16)=N(50,1)\). \(P(49<\bar X<51)=P(-1<Z<1)=0.6827\). Large-sample CLT is not needed because \(X\) is already normal.
4. \(\bar X\approx N(12,9/n)\). Need \(P(Z>\sqrt n/3)<0.01\). Since \(z=2.3263\), \(\sqrt n>6.9789\), so \(n>48.705\), hence \(n_{\min}=49\).
5. \(\bar X\approx N(3.2,3.2/40)=N(3.2,0.08)\). \(Z=(3-3.2)/\sqrt{0.08}=-0.7071\). Probability \(\approx0.2398\).
6. \(E(X)=20(0.08)=1.6\). \(\operatorname{Var}(X)=20(0.08)(0.92)=1.472\). \(\bar X\approx N(1.6,1.472/35)\). \(P(\bar X>2)\approx0.0256\).
7. \(\bar X\approx N(100,25/36)\), standard deviation \(5/6\). \(k=100+1.64485(5/6)=101.3707\), so \(k=101\) to 3 s.f.
8. \(E(X)=3.1\). \(E(X^2)=18.1\). \(\operatorname{Var}(X)=18.1-3.1^2=8.49\). \(\bar X\approx N(3.1,8.49/75)\). \(P(3<\bar X<3.6)\approx0.548\).

---

## 15. Exam Technique Notes

Write \(\bar X\)'s distribution before calculating. Use exact fractions where clean, for example \(13/160\). Interpret final probabilities in context. For inverse-normal thresholds, sketch first. For minimum sample size, round up to the smallest integer satisfying the inequality. Explain CLT in words when asked: since the sample size is large, the sample mean is approximately normally distributed.

---

## 16. Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---|---|
| `FA22-EST-LO001` | Yes | Core CLT formula, use and interpretation included. |
| `FA22-EST-LO003` | Yes | Standard error \(\sigma/\sqrt n\) included. |
| `FA22-LINCOMB-LO002` | Partial support | Used for normal-population contrast. |
| `FAS2-DIST-LO002` | Prerequisite only | Discrete distribution examples used. |
| `FAS2-DIST-LO003` | Prerequisite only | \(E(X)\) and \(\operatorname{Var}(X)\) used. |
| `FAS2-DIST-LO008` | Prerequisite only | Binomial and Poisson used as inputs. |

### Off-Spec Content Found but Excluded

- CLT for sums as the main object: enrichment only; core object is \(\bar X\).
- 3Blue1Brown video: optional enrichment only.
- Negative binomial as core: boundary-risk; included only as optional cross-board support.
- Pearson exercise page references: not treated as official CCEA evidence.
- Continuity correction for direct Poisson/binomial approximations: comparison only.

### Missing Evidence Log

- Official CCEA past-paper CLT questions were not supplied.
- CCEA formula booklet extract was not supplied.
- Full Pearson textbook pages 78-82 were not supplied.
- Fully parsed screenshot PDF was unavailable.
- Confirmation of negative binomial in CCEA FA22 route was not supplied.

---

## 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include a CLT variance shrink diagram, a population-versus-sample-mean diagram, a calculator trap panel, an inverse-normal minimum-sample-size diagram, a simulation of repeated samples from a skewed distribution, and widgets for distribution recognition and minimum \(n\) verification.

---

## 18. Supplementary Sources Used

### Project Sources used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

### Lesson-specific evidence used

- `transcripts.md`
- `FS1-Chp5-CentralLimitTheorem.pdf`
- `Chapter_5_Central_Limit_Theorem_📊_(Further_Statistics_1)_screenshots.pdf`

Ordinary A-Level Maths sources were used only as bridge context and do not override the Further Maths specification. The screenshot PDF could not be parsed as text, so it was used only as visual evidence where readable.

---

## 19. Final Student Checklist

### Prerequisite confidence

- [ ] I can calculate \(E(X)\) and \(\operatorname{Var}(X)\).
- [ ] I can use \(X\sim N(\mu,\sigma^2)\).
- [ ] I can standardise using \(Z=(X-\mu)/\sigma\).
- [ ] I can use normal CDF and inverse normal.
- [ ] I can distinguish variance from standard deviation.

### Further Maths method

- [ ] I can identify questions about \(\bar X\).
- [ ] I can write \(\bar X=(X_1+\cdots+X_n)/n\).
- [ ] I can state \(\bar X\approx N(\mu,\sigma^2/n)\).
- [ ] I can use \(\operatorname{SE}(\bar X)=\sigma/\sqrt n\).
- [ ] I can solve inverse-normal and minimum sample-size questions.

### Exam technique

- [ ] I write \(\bar X\)'s distribution before calculating.
- [ ] I use calculator standard deviation \(\sqrt{\sigma^2/n}\).
- [ ] I recognise \(n\ge30\) for the CCEA CLT approximation unless the population is normal.
- [ ] I round minimum sample sizes up according to the inequality.
- [ ] I interpret probability answers in context.

### Bridge and visual understanding

- [ ] I understand the difference between modelling \(X\) and modelling \(\bar X\).
- [ ] I understand why increasing \(n\) narrows the sampling distribution.
- [ ] I can explain how a standard normal tail value such as \(1.64485\) leads to a minimum sample size.
