# FAS2 Statistical Distributions: Poisson and Geometric Probability Decisions, with Hypothesis-Testing Bridge Warnings

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Topic name | Statistical distributions |
| Topic slug | `statistical_distributions` |
| Topic Pascal | `StatisticalDistributions` |
| Topic ID | `FAS2StatisticalDistributions` |
| Lesson file name | `FAS2_statistical_distributions_lesson.md` |
| Core LO IDs | `FAS2-DIST-LO001`, `FAS2-DIST-LO002`, `FAS2-DIST-LO003`, `FAS2-DIST-LO007`, `FAS2-DIST-LO008` |
| Bridge tags | `#A22HypothesisTestingBridge`, `#BinomialDistributionBridge`, `#TailProbabilityBridge`, `#CriticalRegionBridge` |
| Topic tags | `#FAS2`, `#DIST`, `#Statistics`, `#DiscreteDistributions`, `#Poisson`, `#Geometric`, `#Probability`, `#MeanVariance`, `#BoundaryRisk` |
| Core boundary note | CCEA FAS2-DIST supports Poisson and geometric probability modelling. Poisson/geometric hypothesis testing from the uploaded evidence is preserved only as optional enrichment and bridge warning. |

This lesson is a compass lesson. The uploaded evidence is full of hypothesis-testing machinery, which is mathematically useful, but the CCEA Further Maths map gives us a different anchor: **use the Poisson and geometric distributions as models, calculate probabilities, and understand their parameters**. So the core lesson teaches the CCEA-safe probability engine. The hypothesis-test material is kept in a clearly labelled **enrichment** zone.

## 2. Evidence Map

| Evidence source | Used for | Core status |
|---|---|---|
| CCEA GCE Further Mathematics Specification Map | Official FAS2-DIST LOs and boundary | Core authority |
| Further Maths README module map | Topic placement and module identity | Core authority |
| Further Maths evidence checklist | Missing evidence and source-control logging | Control source |
| Ordinary CCEA A-Level Maths bridge extracts | Hypothesis-testing language, binomial distribution bridge | Bridge only |
| `screenshots.pdf` | Visual evidence of annotated Poisson test examples, calculator/table use, critical regions | Partially inspected; enrichment |
| Poisson transcript | Poisson examples, tail probabilities, rate conversions, critical regions and contextual wording | Enrichment and bridge warning |
| Geometric transcript | Geometric first-success examples, reversed inequality warning, logarithmic critical-region enrichment | Enrichment and bridge warning |
| Dr Frost `FS1-Chp4-HypothesisTesting.pdf` | Cross-board enrichment source for Poisson/geometric hypothesis testing and critical regions | Enrichment only |

**Evidence limitation statement:** Diagram evidence is partially unclear here. The screenshot PDF contains 150 pages and no parsed text. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

## 3. Specification Alignment

| CCEA LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-DIST-LO001` | demonstrate understanding of and use the geometric distribution as a model, including the calculation of probabilities using the geometric distribution | Define `X`, identify first-success contexts, calculate `P(X≤x)`, `P(X≥x)`, and exact probabilities | CCEA spec map; geometric transcript as enrichment | Core: geometric probability modelling only | Ordinary binomial probability uses fixed number of trials; geometric uses trials until first success |
| `FAS2-DIST-LO002` | demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Treat `X` as a discrete random variable; use probability functions and cumulative probabilities | CCEA spec map | Core | Ordinary probability notation and binomial model |
| `FAS2-DIST-LO003` | calculate probabilities such as `P(a≤X≤b)`, `E(X)` and `Var(X)` for simple cases of a discrete random variable `X` | Calculate lower-tail, upper-tail and interval probabilities | CCEA spec map; uploaded probability examples | Core | Tail probabilities from binomial hypothesis testing |
| `FAS2-DIST-LO007` | demonstrate understanding of and use the Poisson distribution as a model, including the calculation of probabilities using the Poisson distribution | Define Poisson rate `λ`, scale `λ` to new time intervals, calculate `P(X≤x)`, `P(X≥x)` | CCEA spec map; Poisson transcript/PDF as enrichment | Core: Poisson probability modelling only | Ordinary binomial and normal distribution probability calculations |
| `FAS2-DIST-LO008` | use the expressions for the mean and variance of the binomial, geometric and Poisson distributions | Compare `E(X)` and `Var(X)` across binomial, geometric and Poisson | CCEA spec map | Core support | Ordinary binomial mean and variance |

The uploaded transcript and PDF repeatedly use hypothesis-testing vocabulary: `H_0`, `H_1`, significance level, critical region and actual significance level. That is useful context, but it is not the CCEA FAS2-DIST core boundary found in the project map. Therefore this lesson teaches the probability model first, then keeps hypothesis-testing examples in a labelled enrichment zone.

## 4. Learning Objectives

### Core Further Maths objectives

By the end of the CCEA-safe core lesson, you should be able to:

1. Recognise when a situation is modelled by a Poisson distribution.
2. Recognise when a situation is modelled by a geometric distribution.
3. Define the random variable `X` clearly before calculating probabilities.
4. Use `λ` correctly as the mean rate in a Poisson distribution.
5. Scale a Poisson mean rate to a new time interval, for example `X~Po(λ)` for one interval gives `Y~Po(kλ)` for `k` identical intervals.
6. Use `p` correctly as the probability of success in a geometric distribution.
7. Calculate exact, lower-tail, upper-tail and interval probabilities.
8. Use the expressions for mean and variance of the binomial, geometric and Poisson distributions.

### Bridge objectives

You should be able to explain how ordinary binomial hypothesis-testing language uses tail probabilities, why the uploaded evidence talks about “observed value or more extreme”, why a Poisson upper-tail probability such as `P(X≥25)` is still a valid probability calculation even if the hypothesis-test framing is enrichment, and why geometric “first success” questions behave differently from fixed-trial binomial questions.

### Exam technique objectives

You should be able to state `X =` “number of ... in ...” or “number of trials until ...” precisely, convert rates into the interval used by the random variable, use exact probability notation before calculating, avoid premature decimals, interpret final probabilities in context, and distinguish between CCEA core probability modelling and optional hypothesis-testing language.

## 5. Explicit Prerequisite Recap

### GCSE foundations

You need fractions, decimals and percentages, index laws, inequalities and calculator accuracy. Geometric probabilities often start from percentages or ratios such as `1 in 8`, `0.2%`, or `4%`. Poisson and geometric tails require inequalities such as `X≤16`, `X≥25`, and `a<X<b`.

### Ordinary AS/A2 Mathematics foundations

You need random variables, the binomial distribution, binomial hypothesis testing, tail probabilities and contextual conclusions.

### Previous Further Mathematics foundations

This lesson assumes discrete probability distributions, probability functions, cumulative probabilities, and mean/variance.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary A-Level Mathematics, binomial distribution | `X~B(n,p)`, fixed number of trials, fixed success probability | Further Maths adds geometric `X~Geo(p)`, where the number of trials is random and stops at first success | Do not treat geometric as binomial with a hidden `n`. There is no fixed number of trials. |
| Ordinary A-Level Mathematics, hypothesis testing | Use `H_0`, `H_1`, significance level, test statistic, critical region and `p`-value | Uploaded evidence applies the same language to Poisson and geometric distributions | This is enrichment unless CCEA explicitly asks for it. Keep it out of the core syllabus lane. |
| Ordinary A-Level Mathematics, binomial hypothesis tests | For `H_1:p>p_0`, use an upper-tail probability; for `H_1:p<p_0`, use a lower-tail probability | Poisson enrichment tests behave similarly with `λ`: higher `λ` means larger values of `X` become more likely | For geometric enrichment tests, the direction reverses because smaller `p` means waiting longer for first success. |
| Ordinary A-Level Mathematics, cumulative probabilities | `P(X≤x)`, `P(X≥x)`, complements such as `1-P(X≤x-1)` | Further Maths uses these on Poisson and geometric models | Be careful with inclusive integer endpoints: `P(X≥25)=1-P(X≤24)`. |

In ordinary A-Level Maths, this idea appeared as binomial probability and hypothesis-testing language. You learned to compare an observed value with a distribution under an assumed model. In Further Maths, the same probability machinery becomes richer because the distribution itself changes: Poisson models counts over time or space, while geometric models the number of trials until the first success. The key upgrade is choosing the correct model and the correct tail. The danger is importing hypothesis-test procedures into CCEA FAS2-DIST as if they were automatically core, when the confirmed CCEA boundary is probability modelling.

## 6. Big Picture Explanation

A probability distribution is a machine for assigning probabilities to possible values of a random variable.

The ordinary binomial distribution answers: how many successes occur in a fixed number of trials?

Further Maths adds two new engines: Poisson and geometric.

### Poisson: counting events in an interval

A Poisson distribution is used when we count events occurring at an average rate. Typical wording includes accidents per month, calls per minute, patients per hour, coins collected per hour, faulty parts per day, or website visits per minute.

If `X` is the number of events in a fixed interval and the mean number in that interval is `λ`, then:

```math
X \sim \operatorname{Po}(\lambda).
```

For CCEA core, the important lesson from the video-game coins evidence is:

```math
X\sim\operatorname{Po}(20),\qquad P(X\geq25)=1-P(X\leq24).
```

The hypothesis-test conclusion is enrichment.

### Geometric: waiting until the first success

A geometric distribution is used when we count how many trials are needed until the first success. Typical wording includes “until he finds a prize ticket”, “until a defective component is found”, or “until a spinner shows 1”.

If `X` is the number of trials up to and including the first success, and the success probability on each trial is `p`, then:

```math
X\sim \operatorname{Geo}(p).
```

For CCEA core, the important part is:

```math
X\sim \operatorname{Geo}\left(\frac18\right),\qquad P(X\geq24)=\left(\frac78\right)^{23}.
```

Again, the hypothesis-test conclusion is enrichment.

## 7. Key Definitions and Notation

### Discrete random variable

A discrete random variable takes separate countable values. A Poisson variable usually starts at `0`, because zero events can occur. A geometric variable usually starts at `1`, because the first success could occur on the first trial.

### Poisson distribution

If `X` is the number of events occurring in a fixed interval, and the mean number of events in that interval is `λ`, then:

```math
X\sim \operatorname{Po}(\lambda).
```

For the Poisson distribution:

```math
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!},\qquad x=0,1,2,\ldots
```

The mean and variance are:

```math
E(X)=\lambda,\qquad \operatorname{Var}(X)=\lambda.
```

### Geometric distribution

In this lesson, `X~Geo(p)` means:

```math
X=\text{the number of trials up to and including the first success}.
```

Then:

```math
P(X=x)=(1-p)^{x-1}p,\qquad x=1,2,3,\ldots
```

The useful cumulative formulae are:

```math
P(X\leq x)=1-(1-p)^x,
```

and:

```math
P(X\geq x)=(1-p)^{x-1}.
```

The mean and variance are:

```math
E(X)=\frac{1}{p},\qquad \operatorname{Var}(X)=\frac{1-p}{p^2}.
```

### Binomial bridge

If `X~B(n,p)`, then `X` counts the number of successes in `n` fixed trials. The mean and variance are:

```math
E(X)=np,\qquad \operatorname{Var}(X)=np(1-p).
```

When `n` is large and `p` is small, a binomial distribution may sometimes be approximated by a Poisson distribution:

```math
B(n,p)\approx \operatorname{Po}(np).
```

### Tail probability

A lower-tail probability has the form `P(X≤a)`. An upper-tail probability has the form `P(X≥a)`. For integer-valued random variables:

```math
P(X\geq a)=1-P(X\leq a-1).
```

Example:

```math
P(X\geq25)=1-P(X\leq24).
```

## 8. Core Theory

### 8.1 Choosing the correct distribution

The first decision is not “what formula do I use?” The first decision is:

```math
\text{What is }X?
```

Only after defining `X` can we decide which distribution model fits.

| Situation | Random variable | Distribution |
|---|---|---|
| Fixed number of trials, count successes | `X=` number of successes in `n` trials | `X~B(n,p)` |
| Count events in a fixed interval | `X=` number of events in the interval | `X~Po(λ)` |
| Count trials until first success | `X=` number of trials up to and including first success | `X~Geo(p)` |

**Bridge Note:** In ordinary A-Level Maths, binomial questions often told you `n` and `p`, then asked for `P(X≤x)` or `P(X≥x)`. Here, Further Maths extends the menu: sometimes there is no fixed `n`, and sometimes the parameter is a rate `λ`, not a probability `p`.

### 8.2 Poisson model: recognising rate language

A Poisson distribution is suggested by rate language:

```math
\text{average of }20\text{ coins per hour},\quad 12\text{ patients per half hour},\quad 6\text{ accidents per month}.
```

The random variable must use the same interval as `λ`.

Suppose a hospital admits on average `12` emergency patients per half hour. If `X` is the number of patients in one hour, then:

```math
\lambda=2\times12=24,
```

so:

```math
X\sim \operatorname{Po}(24).
```

General Poisson scaling rule: if `X~Po(λ)` for one unit of time, then over `k` identical units of time:

```math
Y\sim \operatorname{Po}(k\lambda).
```

### 8.3 Poisson lower-tail probabilities

If `X~Po(24)`, then:

```math
P(X\leq16)=\sum_{x=0}^{16}\frac{e^{-24}24^x}{x!}.
```

From the uploaded hospital example, the probability used is:

```math
P(X\leq16)=0.0563.
```

Core CCEA interpretation: `0.0563` is the probability that a Poisson random variable with mean `24` takes a value of `16` or less. Boundary-enrichment interpretation: comparing this with a significance level is hypothesis-testing language.

### 8.4 Poisson upper-tail probabilities

If `X~Po(20)`, then:

```math
P(X\geq25)=1-P(X\leq24)=1-\sum_{x=0}^{24}\frac{e^{-20}20^x}{x!}.
```

From the uploaded video-game coins example:

```math
P(X\geq25)=0.1568.
```

Exam warning:

```math
P(X\geq25)\neq 1-P(X\leq25).
```

The correct complement is:

```math
P(X\geq25)=1-P(X\leq24).
```

### 8.5 Two-sided probability thinking for a Poisson model

Sometimes an observed value is lower than the mean, but the wording says the rate has **changed**, not decreased. In the uploaded traffic example:

```math
\lambda=6,\quad X=\text{number of accidents in one month},\quad X=3.
```

Since `3<6`, the relevant lower-side probability is:

```math
P(X\leq3)=0.1512.
```

In a two-sided hypothesis-test enrichment context, a `5%` significance level is halved to `2.5%` in each tail. Core CCEA interpretation: `P(X≤3)=0.1512` is a lower-tail probability for `X~Po(6)`.

### 8.6 Binomial-to-Poisson approximation as a probability model

A binomial model has:

```math
X\sim B(n,p).
```

When `n` is large and `p` is small, and `np` is of moderate size:

```math
X\sim B(n,p)\approx \operatorname{Po}(np).
```

In the influenza example:

```math
X\sim B(250,0.04),\qquad \lambda=250(0.04)=10,
```

so:

```math
X\approx\operatorname{Po}(10).
```

For the observed number `17`:

```math
P(X\geq17)=1-P(X\leq16)=0.0270.
```

### 8.7 Critiquing a probability model

The uploaded transcript gives an important modelling criticism for the influenza factory example: employees may not be independent, because they could be family members, friends, or people who spend time together, so one infection may make another more likely.

The binomial model assumes a fixed number of trials, two outcomes, constant probability and independence. If independence is doubtful, then the binomial model is weaker. Since the Poisson approximation inherits the binomial setup, the Poisson approximation is also weaker.

### 8.8 Geometric model: recognising first-success language

A geometric distribution is suggested by language such as “until the first success”. If:

```math
X=\text{number of trials up to and including the first success},
```

and the probability of success on each trial is `p`, then:

```math
X\sim\operatorname{Geo}(p).
```

The probability of first success on trial `x` is:

```math
P(X=x)=(1-p)^{x-1}p.
```

Why? The first `x-1` trials must fail, and the `x`th trial must succeed.

### 8.9 Geometric lower-tail probability

The event `X≤x` means the first success occurs on or before trial `x`. The complement is no success in the first `x` trials:

```math
P(X\leq x)=1-(1-p)^x.
```

### 8.10 Geometric upper-tail probability

The event `X≥x` means the first success occurs on trial `x` or later. For this to happen, the first `x-1` trials must all fail:

```math
P(X\geq x)=(1-p)^{x-1}.
```

For the fast food prize ticket example:

```math
X\sim\operatorname{Geo}\left(\frac18\right),\qquad P(X\geq24)=\left(\frac78\right)^{23}=0.04636\ldots
```

### 8.11 Why geometric inequality direction can feel backwards

For Poisson, larger `λ` usually means larger `X`; smaller `λ` usually means smaller `X`.

For geometric, larger `p` means success is more likely on each trial, so the first success tends to occur sooner:

```math
p\uparrow\Rightarrow X\downarrow,\qquad p\downarrow\Rightarrow X\uparrow.
```

This is the most important warning from the geometric evidence.

### 8.12 Mean and variance comparison

| Distribution | Model | Mean | Variance |
|---|---|---:|---:|
| Binomial | `X~B(n,p)` | `np` | `np(1-p)` |
| Poisson | `X~Po(λ)` | `λ` | `λ` |
| Geometric | `X~Geo(p)` | `1/p` | `(1-p)/p²` |

For example, if:

```math
X\sim\operatorname{Geo}\left(\frac18\right),
```

then:

```math
E(X)=\frac{1}{1/8}=8,
```

and:

```math
\operatorname{Var}(X)=\frac{1-1/8}{(1/8)^2}=\frac{7/8}{1/64}=56.
```

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsMermaid-001 | Source: CCEA FAS2-DIST specification boundary + lesson evidence | Insert from mermaid/FAS2StatisticalDistributionsMermaid-001.md | Purpose: Help the student choose between binomial, geometric and Poisson models before calculating. Description: A decision tree beginning with “What is being counted?” and branching to fixed number of trials, events in an interval, and trials until first success.]

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsSVG-001 | Source: CCEA FAS2-DIST specification boundary | Insert from svg/FAS2StatisticalDistributionsSVG-001.svg | Purpose: Compare the roles of `n`, `p`, `λ`, `E(X)` and `Var(X)` for binomial, geometric and Poisson distributions. Description: Three-column comparison grid with formulas and model cues.]

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsSVG-002 | Source: Poisson transcript + Dr Frost PDF enrichment; CCEA-safe use is probability modelling only | Insert from svg/FAS2StatisticalDistributionsSVG-002.svg | Purpose: Show why `P(X≥25)=1-P(X≤24)` for a discrete Poisson variable. Description: Number-line or bar-style tail diagram for `X~Po(20)`, with bars `0` to `24` shaded as complement and `25,26,...` marked as the upper tail.]

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsSVG-003 | Source: Geometric transcript + Dr Frost PDF enrichment; CCEA-safe use is geometric probability direction | Insert from svg/FAS2StatisticalDistributionsSVG-003.svg | Purpose: Show that smaller `p` makes first success take longer, so upper tails matter when success is rarer. Description: Two horizontal waiting-time number lines comparing high `p` and low `p`, with the low-`p` line stretched to the right.]

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2StatisticalDistributionsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: A bridge diagram showing ordinary binomial tail probability language flowing into Further Maths Poisson/geometric probability calculations, with a boundary marker saying “hypothesis-test conclusion is enrichment unless CCEA asks”.]

[VISUAL PLACEHOLDER: FAS2StatisticalDistributionsTikZ-001 | Source: CCEA FAS2-DIST + uploaded Poisson/geometric probability evidence | Insert from tikz/FAS2StatisticalDistributionsTikZ-001.tex | Purpose: Give a precise discrete number-line diagram for inclusive endpoints. Description: A clean number line showing `X≤a`, `X≥a`, `P(X≥a)=1-P(X≤a-1)`, and why the endpoint moves by one.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2StatisticalDistributionsWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FAS2-DIST lesson evidence | Insert from widgets/FAS2StatisticalDistributionsWidget-001.html | Purpose: Help students choose the correct distribution and calculate core CCEA-safe probabilities.]

The widget asks what is being counted, what the parameters are, and what probability is required. It displays the selected distribution, formula used, exact expression where possible, decimal answer, and endpoint warnings.

[INTERACTIVE PLACEHOLDER: FAS2StatisticalDistributionsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence and bridge/enrichment warnings | Insert from widgets/FAS2StatisticalDistributionsWidget-002.html | Purpose: Train students to choose upper-tail and lower-tail probabilities for Poisson and geometric scenarios without drifting into unsupported hypothesis-test conclusions.]

The widget displays a number-line tail, the chosen probability statement, a warning if the wrong tail is used, and a badge saying either “Core probability calculation” or “Hypothesis-test wording: enrichment unless CCEA asks.”

## 11. Worked Examples

### Worked Example 1: Poisson upper-tail probability from the video-game coins example

**Evidence source:** Poisson transcript and visible screenshot preview.  
**On-spec status:** Core probability calculation; hypothesis-test decision is enrichment only.  
**Ordinary Maths idea used:** Tail probability and complement.  
**Further Maths upgrade:** Use `X~Po(λ)` instead of `X~B(n,p)`.

Suppose a player collects an average of `20` coins per hour. In a one-hour window, the player collects `25` coins. Let:

```math
X=\text{number of coins collected in one hour}.
```

Assume:

```math
X\sim\operatorname{Po}(20).
```

Find:

```math
P(X\geq25).
```

Because `X` is discrete:

```math
P(X\geq25)=1-P(X\leq24).
```

Using the Poisson cumulative probability:

```math
P(X\geq25)=1-\sum_{x=0}^{24}\frac{e^{-20}20^x}{x!}.
```

From the evidence:

```math
P(X\geq25)=0.1568.
```

Final answer:

```math
\boxed{P(X\geq25)=0.1568}
```

### Worked Example 2: Poisson rate conversion for hospital arrivals

A hospital A&E department admits on average `12` emergency patients per half hour. During a one-hour window, `16` people arrive.

Let:

```math
X=\text{number of patients arriving in one hour}.
```

The rate is `12` patients per half hour. One hour contains two half-hour intervals, so:

```math
\lambda=2\times12=24.
```

Therefore:

```math
X\sim\operatorname{Po}(24).
```

Then:

```math
P(X\leq16)=\sum_{x=0}^{16}\frac{e^{-24}24^x}{x!}=0.0563.
```

Final answer:

```math
\boxed{X\sim\operatorname{Po}(24)},\qquad \boxed{P(X\leq16)=0.0563}.
```

### Worked Example 3: Poisson lower-tail probability for accidents

There has been an average of `6` car accidents at a road junction over a one-month period. In the following month, there are `3` accidents.

Let:

```math
X=\text{number of accidents in one month},\qquad X\sim\operatorname{Po}(6).
```

Calculate:

```math
P(X\leq3).
```

Using the probability function:

```math
P(X\leq3)=\frac{e^{-6}6^0}{0!}+\frac{e^{-6}6^1}{1!}+\frac{e^{-6}6^2}{2!}+\frac{e^{-6}6^3}{3!}.
```

Factor out `e^{-6}`:

```math
P(X\leq3)=e^{-6}\left(1+6+18+36\right)=61e^{-6}=0.1512\ldots
```

Final answer:

```math
\boxed{P(X\leq3)=0.1512}
```

### Worked Example 4: Binomial-to-Poisson approximation for influenza absences

During an influenza epidemic, `4%` of a large city were affected on a given day. A factory employs `250` people. The manager finds that `17` employees are absent, claiming to be suffering from influenza.

Let:

```math
X=\text{number of employees out of 250 suffering from influenza}.
```

The original model is:

```math
X\sim B(250,0.04).
```

A Poisson approximation uses:

```math
\lambda=np=250(0.04)=10.
```

Therefore:

```math
X\approx\operatorname{Po}(10).
```

We need:

```math
P(X\geq17)=1-P(X\leq16)=0.0270.
```

Final answer:

```math
\boxed{X\sim B(250,0.04)\approx\operatorname{Po}(10)},\qquad \boxed{P(X\geq17)=0.0270}.
```

### Worked Example 5: Geometric upper-tail probability for first prize ticket

A fast food chain claims that one in eight portions of fries reveals a prize ticket. Harry buys one portion each day until he finds a prize ticket. He finds a prize ticket for the first time on the `24`th day.

Let:

```math
X=\text{number of days until the first prize ticket},\qquad X\sim\operatorname{Geo}\left(\frac18\right).
```

Calculate:

```math
P(X\geq24).
```

For a geometric distribution:

```math
P(X\geq x)=(1-p)^{x-1}.
```

So:

```math
P(X\geq24)=\left(1-\frac18\right)^{23}=\left(\frac78\right)^{23}=0.04636\ldots
```

Final answer:

```math
\boxed{P(X\geq24)=\left(\frac78\right)^{23}=0.0464\text{ approximately}}
```

### Worked Example 6: Geometric lower-tail probability for early defective component

An electronics company claims that the percentage of defective components is `0.05%`. A retailer tests components until finding the first defective one. The first defective component is found on the `90`th component tested.

Convert the percentage:

```math
0.05\%=\frac{0.05}{100}=0.0005.
```

Let:

```math
X=\text{number of components tested until finding a defective one},\qquad X\sim\operatorname{Geo}(0.0005).
```

Calculate:

```math
P(X\leq90)=1-(1-0.0005)^{90}=1-(0.9995)^{90}=0.0440\ldots
```

Final answer:

```math
\boxed{P(X\leq90)=0.0440}
```

### Worked Example 7: Poisson critical region as enrichment, estate-agent sales

**On-spec status:** Boundary-risk enrichment only.

An estate agent has been selling houses at a rate of `9` per month. He believes the rate of sales will decrease in the next month. Let:

```math
X=\text{number of houses sold per month},\qquad X\sim\operatorname{Po}(9).
```

A decrease means unusually small values of `X`, so look for:

```math
P(X\leq a)<0.05.
```

From the evidence tables:

```math
P(X\leq3)=0.0212,
```

and:

```math
P(X\leq4)=0.0550.
```

Since:

```math
0.0212<0.05,\qquad 0.0550>0.05,
```

we get:

```math
\boxed{\text{Critical region: }X\leq3},\qquad \boxed{\text{Actual significance level: }0.0212}.
```

### Worked Example 8: Geometric critical region using logarithms, spinner example

**On-spec status:** Boundary-risk enrichment only.

A five-sided spinner numbered `1` to `5` is spun until it shows `1`. Under fairness:

```math
p=\frac15.
```

Let:

```math
X=\text{number of spins until a 1 is scored},\qquad X\sim\operatorname{Geo}\left(\frac15\right).
```

If `p` is less than `1/5`, then success is rarer, so `X` tends to be larger. We need:

```math
P(X\geq a)<0.05.
```

For a geometric distribution:

```math
P(X\geq a)=(1-p)^{a-1}=0.8^{a-1}.
```

So:

```math
0.8^{a-1}<0.05.
```

Take logarithms:

```math
(a-1)\log(0.8)<\log(0.05).
```

Since `log(0.8)<0`, dividing reverses the inequality:

```math
a-1>\frac{\log(0.05)}{\log(0.8)}.
```

Therefore:

```math
a>1+\frac{\log(0.05)}{\log(0.8)}=14.43\ldots
```

The smallest integer satisfying this is:

```math
a=15.
```

Thus:

```math
\boxed{\text{Critical region: }X\geq15}.
```

The actual significance level is:

```math
P(X\geq15)=0.8^{14}=0.04398\ldots
```

## 12. Common Mistakes and Exam Traps

1. Treating hypothesis-testing enrichment as core CCEA content.
2. Forgetting to define `X`.
3. Not matching the interval to `λ`.
4. Writing `P(X≥25)=1-P(X≤25)` instead of `P(X≥25)=1-P(X≤24)`.
5. Writing “accept `H_0`” in enrichment test language.
6. Forgetting that geometric `X` starts at `1`, not `0`.
7. Missing the geometric direction trap: `p↑⇒X↓`, while `p↓⇒X↑`.
8. Confusing `0.05%` with `0.05`.
9. Ignoring model assumptions such as independence.
10. Letting the calculator replace a written probability statement.

## 13. Practice Questions

These are AI-generated practice questions, not past-paper questions and not textbook questions.

### Question 1: Choosing the model

For each situation, choose the most appropriate distribution from `B(n,p)`, `Po(λ)`, `Geo(p)`, and define `X`.

a. A website receives visits at an average rate of `7` visits per minute. Count the number of visits in one minute.

b. A spinner has probability `1/5` of landing on `1`. Count the number of spins up to and including the first `1`.

c. A factory checks `40` components, each with probability `0.03` of being defective. Count the number of defective components.

d. A call centre receives calls at an average rate of `0.325` calls per minute. Count the number of calls in a `20`-minute interval.

### Question 2: Poisson rate conversion

A machine produces faults at an average rate of `0.8` faults per hour. Let `X` be the number of faults in `5` hours.

a. State the distribution of `X`.

b. Calculate `P(X=3)`.

c. Calculate `P(X≤3)`.

d. Calculate `P(X≥4)`.

### Question 3: Geometric exact probability

A game has probability `0.2` of giving a rare item on each attempt. Attempts are independent. Let `X` be the number of attempts up to and including the first rare item.

a. State the distribution of `X`.

b. Calculate `P(X=4)`.

c. Calculate `P(X≤4)`.

d. Calculate `P(X≥4)`.

### Question 4: Binomial-to-Poisson approximation

A large batch contains items that independently have probability `0.02` of being faulty. A sample of `200` items is inspected. Let `X` be the number of faulty items in the sample.

a. State the exact binomial model for `X`.

b. Use a Poisson approximation to model `X`.

c. Using the Poisson approximation, calculate `P(X≥7)`.

### Question 5: Comparing mean and variance

Find `E(X)` and `Var(X)` for:

a. `X~B(50,0.1)`

b. `X~Po(6.5)`

c. `X~Geo(1/4)`

### Question 6: Poisson model with contextual interpretation

A café receives online orders at an average rate of `3.2` orders per hour. Let `X` be the number of online orders received in `2` hours.

a. State the distribution of `X`.

b. Calculate `P(X≤4)`.

c. Calculate `P(5≤X≤8)`.

d. Interpret your answer to part c.

### Question 7: Geometric model with waiting-time interpretation

A password-reset code has probability `0.15` of being entered correctly on any one independent attempt. Let `X` be the number of attempts up to and including the first correct entry.

a. State the distribution of `X`.

b. Calculate `P(X=1)`.

c. Calculate `P(X>5)`.

d. Calculate `P(3≤X≤6)`.

### Question 8: Model choice and model criticism

During a flu outbreak, `3%` of people in a large town are absent from work on a particular day. A company has `300` employees. Let `X` be the number of employees absent from work due to flu on that day.

a. State a binomial model for `X`.

b. Use a Poisson approximation for `X`.

c. Using the Poisson approximation, calculate `P(X≥15)`.

d. State one reason why the binomial model, and therefore the Poisson approximation, might be questionable.

### Question 9: Poisson interval probability with exact setup

Calls arrive at a helpdesk at an average rate of `0.4` calls per minute. Let `X` be the number of calls arriving in `15` minutes.

a. State the distribution of `X`.

b. Calculate `P(4≤X≤9)`.

c. Calculate `P(X<4 or X>9)`.

### Question 10: Geometric expectation and probability

A student practises a skill. On each independent attempt, the probability of success is `0.12`. Let `X` be the number of attempts up to and including the first success.

a. Find `E(X)`.

b. Find `Var(X)`.

c. Calculate `P(X≤10)`.

d. Explain what `P(X≤10)` means in context.

### Enrichment Question 11: Poisson tail decision

A process normally produces events at rate `10` per hour. In one hour, `17` events are observed. Assuming `X~Po(10)`, calculate `P(X≥17)` and compare it with `0.05`, labelling this comparison as enrichment.

### Enrichment Question 12: Geometric tail direction

A game claims that the probability of success on each attempt is `1/5`. A player records the first success on the `18`th attempt. Assuming `X~Geo(1/5)`, calculate `P(X≥18)`. Explain why a long waiting time would support the idea that the success probability is lower, not higher.

## 14. Worked Solutions

### Solution 1

a. `X=` number of visits in one minute. `X~Po(7)`.

b. `X=` number of spins up to and including the first `1`. `X~Geo(1/5)`.

c. `X=` number of defective components among the `40` checked. `X~B(40,0.03)`.

d. `X=` number of calls in `20` minutes. `λ=0.325×20=6.5`, so `X~Po(6.5)`.

### Solution 2

The rate is `0.8` faults per hour. For `5` hours:

```math
\lambda=5(0.8)=4.
```

So `X~Po(4)`.

```math
P(X=3)=\frac{e^{-4}4^3}{3!}=\frac{32}{3}e^{-4}=0.1954\ldots
```

```math
P(X\leq3)=e^{-4}\left(1+4+8+\frac{32}{3}\right)=\frac{71}{3}e^{-4}=0.4335\ldots
```

```math
P(X\geq4)=1-P(X\leq3)=0.5665\ldots
```

### Solution 3

`X~Geo(0.2)`.

```math
P(X=4)=(1-0.2)^3(0.2)=0.8^3(0.2)=0.1024.
```

```math
P(X\leq4)=1-0.8^4=0.5904.
```

```math
P(X\geq4)=0.8^3=0.512.
```

### Solution 4

Exact model:

```math
X\sim B(200,0.02).
```

Poisson approximation:

```math
\lambda=np=200(0.02)=4,\qquad X\approx\operatorname{Po}(4).
```

```math
P(X\geq7)=1-P(X\leq6)=0.1107\ldots
```

### Solution 5

For `X~B(50,0.1)`:

```math
E(X)=50(0.1)=5,
```

```math
\operatorname{Var}(X)=50(0.1)(0.9)=4.5.
```

For `X~Po(6.5)`:

```math
E(X)=6.5,\qquad \operatorname{Var}(X)=6.5.
```

For `X~Geo(1/4)`:

```math
E(X)=4,
```

```math
\operatorname{Var}(X)=\frac{1-1/4}{(1/4)^2}=12.
```

### Solution 6

For `2` hours:

```math
\lambda=2(3.2)=6.4,
```

so `X~Po(6.4)`.

```math
P(X\leq4)=0.2228\ldots
```

```math
P(5\leq X\leq8)=P(X\leq8)-P(X\leq4)=0.5758\ldots
```

The probability that the café receives between `5` and `8` online orders inclusive in a `2`-hour period is about `0.5758`.

### Solution 7

`X~Geo(0.15)`.

```math
P(X=1)=0.15.
```

```math
P(X>5)=(1-0.15)^5=0.85^5=0.4437\ldots
```

```math
P(3\leq X\leq6)=P(X\leq6)-P(X\leq2)=(1-0.85^6)-(1-0.85^2)=0.3454\ldots
```

### Solution 8

```math
X\sim B(300,0.03).
```

```math
\lambda=300(0.03)=9,
```

so:

```math
X\approx\operatorname{Po}(9).
```

```math
P(X\geq15)=1-P(X\leq14)=0.0415\ldots
```

One reason the model may be questionable is that employees may not be independent. If employees work near one another, socialise, travel together, or infect each other, one person being absent due to flu may make another absence more likely.

### Solution 9

```math
\lambda=15(0.4)=6,
```

so `X~Po(6)`.

```math
P(4\leq X\leq9)=P(X\leq9)-P(X\leq3)=0.7649\ldots
```

```math
P(X<4\text{ or }X>9)=1-P(4\leq X\leq9)=0.2351\ldots
```

### Solution 10

For `p=0.12=3/25`:

```math
E(X)=\frac{1}{0.12}=\frac{25}{3}.
```

```math
\operatorname{Var}(X)=\frac{1-p}{p^2}=\frac{22/25}{9/625}=\frac{550}{9}.
```

```math
P(X\leq10)=1-(1-0.12)^{10}=1-0.88^{10}=0.7215\ldots
```

`P(X≤10)` means the probability that the student gets their first success on or before the `10`th attempt.

### Solution 11: Optional enrichment

```math
P(X\geq17)=1-P(X\leq16)=0.0270\ldots
```

Since `0.0270<0.05`, the observation is unusual at the `5%` level in a hypothesis-test style interpretation. Core-safe interpretation: this is the probability of observing `17` or more events if `X~Po(10)`.

### Solution 12: Optional enrichment

```math
P(X\geq18)=\left(1-\frac15\right)^{17}=\left(\frac45\right)^{17}=0.0225\ldots
```

If the success probability `p` is lower than claimed, success is rarer. If success is rarer, the first success tends to happen later. Therefore a long waiting time supports the idea that `p` may be lower, not higher.

## 15. Exam Technique Notes

1. Always define `X` first.
2. Match the interval to the parameter `λ`.
3. Write the probability statement before using a calculator.
4. Use the correct endpoint in complements: `P(X≥a)=1-P(X≤a-1)`.
5. For intervals, subtract cumulative probabilities carefully: `P(4≤X≤9)=P(X≤9)-P(X≤3)`.
6. For geometric exact probabilities, use `P(X=x)=(1-p)^{x-1}p`.
7. For geometric cumulative probabilities, use `P(X≤x)=1-(1-p)^x`.
8. For geometric upper tails, use `P(X≥x)=(1-p)^{x-1}`.
9. Keep exact forms where useful, then give decimals if required.
10. Check model assumptions, especially independence.
11. Use hypothesis-test vocabulary only if the question explicitly asks for a hypothesis test.

## 16. Syllabus Gap Check

| LO ID | Covered? | Evidence basis | Notes |
|---|---:|---|---|
| `FAS2-DIST-LO001` | Yes | CCEA spec + geometric examples | Core lesson includes geometric model, exact, lower-tail and upper-tail probabilities |
| `FAS2-DIST-LO002` | Yes | CCEA spec | Core lesson defines discrete random variables and probability functions |
| `FAS2-DIST-LO003` | Yes | CCEA spec | Practice includes `P(a≤X≤b)`, `E(X)`, `Var(X)` |
| `FAS2-DIST-LO007` | Yes | CCEA spec + Poisson examples | Core lesson includes Poisson model, rate scaling, cumulative and tail probabilities |
| `FAS2-DIST-LO008` | Yes | CCEA spec | Mean/variance comparison table and worked questions included |

### Off-Spec Content Found but Excluded

| Off-spec or boundary-risk item | Treatment |
|---|---|
| Poisson hypothesis tests on `λ` | Not taught as core; used only as optional enrichment |
| Geometric hypothesis tests on `p` | Not taught as core; used only as optional enrichment |
| Critical regions for Poisson/geometric hypothesis tests | Not taught as core; included as enrichment examples |
| Actual significance level for Poisson/geometric tests | Enrichment only |
| Cross-board Pearson/Edexcel exercise references | Not used as CCEA authority |

### Weak evidence warnings

- `screenshots.pdf` had no parsed text; only visible preview details are claimed.
- Hypothesis testing is not confirmed in the CCEA FAS2-DIST LO list used for this lesson.
- Cross-board PDF and Pearson/Edexcel-style evidence are enrichment, not CCEA authority.

## 17. Recommended Enhancements Not in the Evidence

AI-proposed teaching enhancements include distribution chooser decision tree, Poisson rate-scaling diagram, geometric waiting-time number line, inclusive endpoint complement diagram, binomial-to-Poisson approximation bridge, Poisson bars growing as `λ` changes, geometric waiting-time simulation, complement tail animation, and distribution/tail-direction widgets. These are proposed enhancements, not evidence-backed content unless supported by the cited lesson evidence or CCEA boundary.

## 18. Supplementary Sources Used

| Source | Role |
|---|---|
| CCEA GCE Further Mathematics Specification Map | Official syllabus boundary and LO IDs |
| Further Maths README module map | Topic placement in FAS2 Section C Statistics |
| Further Maths Evidence Drop Checklist | Evidence completeness and limitation logging |
| Ordinary A-Level Maths Bridge Spec Extracts | Bridge context only |
| CCEA GCE Mathematics Specification Map | Ordinary Maths background only |
| `screenshots.pdf` | Partial visual evidence; visible pages showed annotated Poisson examples, critical regions, tables and calculator overlays |
| Poisson transcript | Poisson examples, tail probabilities, rate conversions, critical regions and contextual wording |
| Geometric transcript | Geometric first-success examples, reversed inequality warning, logarithmic critical-region enrichment |
| `FS1-Chp4-HypothesisTesting.pdf` | Cross-board enrichment source for Poisson/geometric hypothesis testing and critical regions |

Ordinary A-Level Maths sources are used only to explain what the student already knows. They do not override the CCEA Further Maths specification boundary.

## 19. Final Student Checklist

### Prerequisite confidence checklist

- [ ] I can define a random variable `X`.
- [ ] I understand `P(X=x)`, `P(X≤x)`, `P(X≥x)`.
- [ ] I can use complements correctly.
- [ ] I know the binomial model `X~B(n,p)`.
- [ ] I know that a percentage such as `0.05%` must be divided by `100`.
- [ ] I can use powers such as `(1-p)^x`.

### Further Maths method checklist

For Poisson:

- [ ] I can recognise rate language.
- [ ] I can define `X` as a count in a fixed interval.
- [ ] I can scale `λ` to match the interval.
- [ ] I can write `X~Po(λ)`.
- [ ] I can calculate exact, lower-tail and upper-tail probabilities.
- [ ] I can use `P(X≥a)=1-P(X≤a-1)`.

For geometric:

- [ ] I can recognise “until the first success” language.
- [ ] I can define `X` as the number of trials up to and including the first success.
- [ ] I can write `X~Geo(p)`.
- [ ] I can use `P(X=x)=(1-p)^{x-1}p`.
- [ ] I can use `P(X≤x)=1-(1-p)^x`.
- [ ] I can use `P(X≥x)=(1-p)^{x-1}`.
- [ ] I remember that geometric `X` starts at `1`, not `0`.

### Mean and variance checklist

- [ ] For `X~B(n,p)`, I know `E(X)=np` and `Var(X)=np(1-p)`.
- [ ] For `X~Po(λ)`, I know `E(X)=λ` and `Var(X)=λ`.
- [ ] For `X~Geo(p)`, I know `E(X)=1/p` and `Var(X)=(1-p)/p²`.

### Exam technique checklist

- [ ] I write the distribution before calculating probabilities.
- [ ] I define `X` in words.
- [ ] I match the interval to `λ`.
- [ ] I keep exact values where appropriate.
- [ ] I round only at the end.
- [ ] I interpret probabilities in context.
- [ ] I state model assumptions when asked.
- [ ] I do not claim a hypothesis-test conclusion unless the question asks for a hypothesis test.

### Bridge checklist

- [ ] I understand that ordinary binomial hypothesis testing uses tail probabilities.
- [ ] I understand that Poisson and geometric examples in the uploaded evidence use similar tail logic.
- [ ] I know that geometric tail direction can feel reversed because lower `p` means longer waiting time.
- [ ] I can separate a core probability calculation from an enrichment hypothesis-test conclusion.
- [ ] I know that “not enough evidence to reject” does not prove the null hypothesis.
