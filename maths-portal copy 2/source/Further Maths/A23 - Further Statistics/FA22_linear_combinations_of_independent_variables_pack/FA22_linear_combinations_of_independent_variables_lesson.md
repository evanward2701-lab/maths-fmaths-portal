# FA22-LINCOMB: Linear Combinations of Independent Variables

| Metadata field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FA22-LINCOMB` |
| Topic name | Linear combinations of independent variables |
| Topic slug | `linear_combinations_of_independent_variables` |
| Topic Pascal | `LinearCombinationsOfIndependentVariables` |
| Topic ID | `FA22LinearCombinationsOfIndependentVariables` |
| Lesson file | `FA22_linear_combinations_of_independent_variables_lesson.md` |
| LO IDs | `FA22-LINCOMB-LO001`; `FA22-LINCOMB-LO002`; `FA22-LINCOMB-LO003` |
| Bridge tags | A22 Normal Distribution; AS2 Statistical Distributions; AS2 Probability |
| Topic tags | `#FA22`, `#LINCOMB`, `#Statistics`, `#NormalDistribution`, `#LinearCombinations`, `#Expectation`, `#Variance`, `#IndependentRandomVariables` |

---

# 2. Evidence Map

| Evidence source | Role in this lesson | Lesson use |
|---|---|---|
| CCEA GCE Further Mathematics Specification Map | Core authority | Topic identity, LO IDs, official learning outcomes, syllabus boundary. |
| Further Maths README module map | Project bridge map | Confirms bridge links to A22 Normal Distribution, AS2 Statistical Distributions, and AS2 Probability. |
| Further Maths Evidence Drop Checklist | Project workflow | Controls missing evidence, off-spec logging, visual placeholders and end-of-phase checks. |
| Ordinary A-Level Maths Bridge Spec Extracts | Bridge source only | Used to explain prior ordinary Maths knowledge. |
| Teacher transcript: Chapter 4 Combinations of Random Variables | Lesson-specific mathematical evidence | Preserves notation explanation, motivation, intuition, formula warnings, worked examples and exam-question strategies. |
| Slide PDF: FS2 Chapter 4 Combining Variables | Lesson-specific slide evidence | Preserves starter tables, formula panels, examples, quickfire prompts and the crate example. |
| Screenshot PDF: Chapter 4 Combinations of Random Variables | Visual evidence | Supports visible slide layout, annotations and image-based teaching visuals where readable. |
| DrFrost/FS2 framing | Cross-board source | Used only when content is confirmed on-spec by CCEA FA22-LINCOMB. |
| Edexcel S3-style questions in evidence | Cross-board enrichment | Logged as boundary-risk. Not labelled as CCEA past-paper content. |

**Visual evidence limitation:** Diagram evidence is partially unclear here. The screenshot PDF is image-based and not parseable as text. The lesson preserves visible/readable details from rendered pages and relies on the transcript and slide PDF for exact mathematical wording. No uninspected visual detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA22-LINCOMB-LO001` | demonstrate understanding of and use the expressions for \(E(aX+bY)\) and \(\operatorname{Var}(aX+bY)\), where \(X\) and \(Y\) are independent random variables | Sections 7 and 8 define expectation and variance formulae; worked examples use \(aX\pm bY\) for independent normal variables. | CCEA map; transcript; slide PDF | Independent variables only; proofs not required | Extends ordinary \(E(X)\), \(\operatorname{Var}(X)\), and \(X\sim N(\mu,\sigma^2)\). |
| `FA22-LINCOMB-LO002` | solve problems involving linear combinations of independent normally distributed variables, including the expressions for the mean and variance of the sum of a number of independent observations from a given population | Sections 8, 11 and 14 solve distribution and probability problems involving sums of independent observations. | CCEA map; transcript; slide PDF | Normal linear combinations; independent observations | Builds on A22 normal probability and inverse normal calculations. |
| `FA22-LINCOMB-LO003` | demonstrate understanding of and use the distribution of a multiple of a single observation from a given population | Sections 8, 11 and 12 compare \(nX\) with \(X_1+\cdots+X_n\). | CCEA map; transcript; slide PDF | Core distinction between scaling and sampling | Extends ordinary transformations \(aX+b\), but the variance distinction is new and examinable. |

---

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Explain the difference between a random variable such as \(X\), a particular observation such as \(x\), a general sample variable such as \(X_i\), and a particular sample value such as \(x_i\).
2. Use
   \[
   E(aX+bY)=aE(X)+bE(Y)
   \]
   for independent random variables \(X\) and \(Y\).
3. Use
   \[
   \operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)
   \]
   when \(X\) and \(Y\) are independent.
4. Know that the variance formula still uses addition when the random variables are subtracted:
   \[
   \operatorname{Var}(aX-bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y).
   \]
5. If
   \[
   X\sim N(\mu_X,\sigma_X^2),\qquad Y\sim N(\mu_Y,\sigma_Y^2),
   \]
   and \(X,Y\) are independent, write
   \[
   aX\pm bY\sim N(a\mu_X\pm b\mu_Y,\ a^2\sigma_X^2+b^2\sigma_Y^2).
   \]
6. For independent observations \(X_1,\ldots,X_n\) from the same population as \(X\), use
   \[
   E(X_1+\cdots+X_n)=nE(X),
   \]
   and
   \[
   \operatorname{Var}(X_1+\cdots+X_n)=n\operatorname{Var}(X).
   \]
7. Distinguish this from a multiple of one observation:
   \[
   E(nX)=nE(X),\qquad \operatorname{Var}(nX)=n^2\operatorname{Var}(X).
   \]

## 4.2 Bridge objectives

You should connect this topic to ordinary A-Level Maths by recognising that ordinary normal-distribution work gave you probability tools once a distribution was known; Further Maths often asks you to build the distribution first; ordinary transformations such as \(aX+b\) are extended into combinations such as \(aX\pm bY\); and probability statements such as \(P(X>Y)\) often need translating into \(P(X-Y>0)\).

## 4.3 Exam technique objectives

You should be able to state independence when using the variance formula; keep variance and standard deviation separate; convert a worded comparison into a linear combination, for example \(W>2X\Longleftrightarrow W-2X>0\); use \(\sigma=\sqrt{\operatorname{Var}(X)}\) when entering a normal calculation on a calculator; and interpret final probabilities or thresholds in context.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You should already be confident with substitution into formulae, rearranging inequalities, interpreting tables, using square roots and squares correctly, and reading probability statements such as “between”, “greater than”, and “less than”.

## 5.2 Ordinary AS/A2 Mathematics foundations

For a normal distribution,

\[
X\sim N(\mu,\sigma^2)
\]

means \(X\) is the random variable, \(\mu=E(X)\) is the mean, \(\sigma^2=\operatorname{Var}(X)\) is the variance, and \(\sigma\) is the standard deviation.

This notation is the first little statistics trapdoor in the floorboards: the distribution is usually written using the **variance**, but the calculator often asks for the **standard deviation**.

So if

\[
X\sim N(25,16),
\]

then

\[
E(X)=25,\qquad \operatorname{Var}(X)=16,\qquad \sigma=4.
\]

## 5.3 Previous Further Mathematics foundations

This topic assumes that you can work with discrete and continuous random variables; expectation and variance; probability distributions; normal-distribution calculations; independent events or independent random variables; and algebraic notation such as \(X_1,X_2,\ldots,X_n\).

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Statistical Distributions | A random variable \(X\), its probability distribution, \(E(X)\), \(\operatorname{Var}(X)\), and standard deviation | Random variables are combined algebraically, for example \(X+Y\), \(X-Y\), \(3X-Y\), \(X_1+\cdots+X_n\) | Do not treat \(X+Y\) as just two numbers. It is a new random variable with its own distribution. |
| A22 Normal Distribution | If \(X\sim N(\mu,\sigma^2)\), use standardisation or calculator methods to find probabilities | First build a new normal distribution, then calculate probabilities from it | Do not enter variance as \(\sigma\) on the calculator. Use \(\sigma=\sqrt{\text{variance}}\). |
| AS2 Probability | Independence lets probabilities multiply in suitable contexts | Independence lets variances add in this topic | The variance rule used here depends on independence. |
| Ordinary transformation work | Multiplying a variable by \(a\) scales its mean by \(a\) | Multiplying a random variable by \(a\) scales its variance by \(a^2\) | Negative signs affect the mean but not the sign of the variance contribution. |
| Ordinary sampling language | A sample contains observations from a population | \(X_1,\ldots,X_n\) are random variables before the data are observed; \(x_1,\ldots,x_n\) are observed values | Confusing \(4X\) with \(X_1+X_2+X_3+X_4\) gives the wrong variance. |

In ordinary A-Level Maths, this idea appeared as: “Here is a distribution. Use it to calculate a probability.”

In Further Maths, the same idea becomes: “Here are several distributions. Build a new distribution from them, then calculate a probability.”

The key upgrade is that expectation behaves like ordinary algebra, but variance has its own rulebook. Means can add or subtract. Variances add under independence, and any scaling is squared.

The danger is treating the random variables like fixed numbers. A fixed number has no spread. A random variable carries uncertainty around with it, like a little statistical weather system.

---

# 6. Big Picture Explanation

The reason this topic exists is simple: real measurements often arrive in packs.

A full egg box is not just “an egg” and not just “a box”. It is:

\[
\text{full box}=\text{egg}_1+\text{egg}_2+\cdots+\text{egg}_6+\text{empty box}.
\]

A full crate of bottled water is not one bottle multiplied by \(12\). It is:

\[
\text{full crate}=B_1+B_2+\cdots+B_{12}+C,
\]

where \(B_1,\ldots,B_{12}\) are the weights of separate bottles, and \(C\) is the empty crate weight.

The new problem is: how do we find the distribution of the total?

Once we know the mean and variance of the total, normal distribution methods wake up again and do their familiar work.

The big lesson is:

\[
\boxed{\text{Mean follows the signs. Variance adds the uncertainty.}}
\]

So:

\[
E(X-Y)=E(X)-E(Y),
\]

but, when \(X\) and \(Y\) are independent,

\[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).
\]

---

# 7. Key Definitions and Notation

## 7.1 Random variable and observation

A **random variable** is a variable whose value is determined by chance.

- \(X\) is a random variable with its own distribution;
- \(x\) is a particular observation from that random variable;
- \(x_1,x_2,\ldots,x_n\) is a particular sample of \(n\) observed values from \(X\);
- \(X_1,X_2,\ldots,X_n\) is a sample of \(n\) random variables from \(X\), before the actual values are known.

So:

\[
X=\text{the whole random mechanism},\qquad x=\text{one value actually observed}.
\]

Example:

\[
X\sim B(100,0.3)
\]

could represent the number of games won out of \(100\), when the probability of winning each game is \(0.3\). If one trial gives \(25\) wins, then \(x=25\). If three repeats produce \(32,38,24\), then \(x_1=32\), \(x_2=38\), \(x_3=24\). Before those repeats happen, write \(X_1,X_2,X_3\).

## 7.2 Expected value

\[
E(X)
\]

is the mean of \(X\). If \(X\sim N(62,3^2)\), then \(E(X)=62\) and \(\operatorname{Var}(X)=3^2=9\).

## 7.3 Variance

If \(X\sim N(\mu,\sigma^2)\), then:

\[
E(X)=\mu,\qquad \operatorname{Var}(X)=\sigma^2,\qquad \sigma=\sqrt{\operatorname{Var}(X)}.
\]

## 7.4 Independent random variables

Random variables \(X\) and \(Y\) are **independent** when knowing the value of one does not change the distribution of the other. In this lesson, independence is a load-bearing wall.

## 7.5 Linear combination

A **linear combination** of random variables is an expression such as \(aX+bY\) or \(aX-bY\), where \(a\) and \(b\) are constants.

## 7.6 Independent observations from the same population

If \(X_1,X_2,\ldots,X_n\) are independent observations from the same population as \(X\), then each \(X_i\) has the same distribution as \(X\), but their actual observed values may be different.

## 7.7 Multiple of one observation versus sum of many observations

\[
4X
\]

means one random observation \(X\), multiplied by \(4\). But

\[
X_1+X_2+X_3+X_4
\]

means four independent observations from the same distribution, added.

They have the same expected value:

\[
E(4X)=4E(X),\qquad E(X_1+X_2+X_3+X_4)=4E(X).
\]

But they do not have the same variance:

\[
\operatorname{Var}(4X)=16\operatorname{Var}(X),
\]

whereas

\[
\operatorname{Var}(X_1+X_2+X_3+X_4)=4\operatorname{Var}(X).
\]

---

# 8. Core Theory

## 8.1 The two master formulae

Let \(X\) and \(Y\) be independent random variables.

\[
\boxed{E(aX\pm bY)=aE(X)\pm bE(Y)}
\]

\[
\boxed{\operatorname{Var}(aX\pm bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)}
\]

The first formula keeps the sign. The second formula uses addition, even when the random variables are subtracted.

**Bridge Note:** In ordinary A-Level Maths, you learned to transform a single normal random variable and calculate probabilities. Here, Further Maths extends this by combining two or more independent random variables before using the normal distribution.

## 8.2 Why expectation behaves like ordinary algebra

If \(X\) has mean \(6\), and \(Y\) has mean \(2\), then:

\[
E(X+Y)=E(X)+E(Y)=6+2=8,
\]

and:

\[
E(X-Y)=E(X)-E(Y)=6-2=4.
\]

## 8.3 Why variance adds even when variables are subtracted

For \(X+Y\), both variables vary. For \(X-Y\), both variables still vary. The mean subtracts, but the spread still increases. Under independence:

\[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).
\]

Not:

\[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y).
\]

Never let that false formula sneak into your working wearing a fake moustache.

**Bridge Note:** In ordinary probability, subtracting numbers makes a smaller number. In Further Statistics, subtracting a random variable still brings in its uncertainty, so the variance contribution is positive.

## 8.4 Scaling a random variable

For constant \(a\):

\[
\boxed{E(aX)=aE(X)}
\]

\[
\boxed{\operatorname{Var}(aX)=a^2\operatorname{Var}(X)}
\]

Example: if \(Y\sim N(2,1)\), then \(3Y\sim N(6,9)\). If \(-2Y\) is used, then \(E(-2Y)=-4\) but \(\operatorname{Var}(-2Y)=4\). The mean moves left. The variance does not become negative.

## 8.5 Linear combinations of independent normal variables

Suppose

\[
X\sim N(\mu_X,\sigma_X^2),\qquad Y\sim N(\mu_Y,\sigma_Y^2),
\]

where \(X\) and \(Y\) are independent. Then:

\[
\boxed{aX\pm bY\sim N(a\mu_X\pm b\mu_Y,\ a^2\sigma_X^2+b^2\sigma_Y^2)}.
\]

## 8.6 Example pattern: \(X-Y\) as a translation trick

A common question asks for \(P(X>Y)\). Move everything to one side:

\[
X>Y\quad\Longleftrightarrow\quad X-Y>0.
\]

So:

\[
P(X>Y)=P(X-Y>0).
\]

Now \(X-Y\) is a new random variable. Find its normal distribution, then use ordinary normal-distribution methods.

## 8.7 Sums of independent observations

Suppose \(X\sim N(\mu,\sigma^2)\), and \(X_1,X_2,\ldots,X_n\) are independent observations from the same population.

Let

\[
S=X_1+X_2+\cdots+X_n.
\]

Then:

\[
E(S)=n\mu,
\]

and:

\[
\operatorname{Var}(S)=n\sigma^2.
\]

Thus:

\[
\boxed{X_1+\cdots+X_n\sim N(n\mu,n\sigma^2)}.
\]

## 8.8 Multiple of a single observation

For \(T=nX\):

\[
E(T)=n\mu,
\]

but:

\[
\operatorname{Var}(T)=n^2\sigma^2.
\]

Thus:

\[
\boxed{nX\sim N(n\mu,n^2\sigma^2)}.
\]

Same mean as the sum of \(n\) observations. Different variance. That is the little dragon guarding this chapter.

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesMermaid-001 | Source: CCEA FA22-LINCOMB specification boundary + teacher transcript | Insert from mermaid/FA22LinearCombinationsOfIndependentVariablesMermaid-001.md | Purpose: Show the full solution workflow for a linear-combination problem: identify random variables, check independence, form the linear combination, calculate expectation, calculate variance, write the new distribution, then answer the probability or inverse-normal question.]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesSVG-001 | Source: Teacher transcript notation clarification | Insert from svg/FA22LinearCombinationsOfIndependentVariablesSVG-001.svg | Purpose: Preserve and clarify the uppercase/lowercase notation distinction between \(X\), \(x\), \(X_i\), and \(x_i\).]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesSVG-002 | Source: FS2-Chp4-CombiningVars.pdf page 4 starter | Insert from svg/FA22LinearCombinationsOfIndependentVariablesSVG-002.svg | Purpose: Preserve the starter idea that \(X+Y\) and \(X-Y\) are new random variables, using two fair six-sided dice.]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesTikZ-001 | Source: Teacher transcript intuition for adding and subtracting variables | Insert from tikz/FA22LinearCombinationsOfIndependentVariablesTikZ-001.tex | Purpose: Show why means add/subtract but spread increases for both \(X+Y\) and \(X-Y\).]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesTikZ-002 | Source: Teacher transcript scaling section | Insert from tikz/FA22LinearCombinationsOfIndependentVariablesTikZ-002.tex | Purpose: Show how multiplying a random variable by \(3\) or by \(-2\) changes the mean and spread.]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesSVG-003 | Source: FS2-Chp4-CombiningVars.pdf page 7 + teacher transcript | Insert from svg/FA22LinearCombinationsOfIndependentVariablesSVG-003.svg | Purpose: Show why \(4X\) and \(X_1+X_2+X_3+X_4\) have the same expected value but different variances.]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesTikZ-003 | Source: Mineral-water crate worked example from transcript and slide PDF | Insert from tikz/FA22LinearCombinationsOfIndependentVariablesTikZ-003.tex | Purpose: Show \(P(26<W<27)\) after deriving \(W\sim N(26.5,0.12)\).]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesTikZ-004 | Source: Mineral-water crate label worked example from transcript and slide PDF | Insert from tikz/FA22LinearCombinationsOfIndependentVariablesTikZ-004.tex | Purpose: Show the inverse-normal setup for the label weight \(M\) where \(P(W>M)=0.01\).]

[VISUAL PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22LinearCombinationsOfIndependentVariablesBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths normal-distribution methods with the Further Maths extension to linear combinations.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FA22-LINCOMB and lesson evidence | Insert from widgets/FA22LinearCombinationsOfIndependentVariablesWidget-001.html | Purpose: Let students enter two independent normal variables and a linear combination \(aX\pm bY\), then see the resulting mean, variance and normal distribution.]

[INTERACTIVE PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesWidget-002 | Source: AI-proposed teaching enhancement based on CCEA FA22-LINCOMB and teacher transcript | Insert from widgets/FA22LinearCombinationsOfIndependentVariablesWidget-002.html | Purpose: Reinforce the difference between scaling one observation and summing independent observations.]

[INTERACTIVE PLACEHOLDER: FA22LinearCombinationsOfIndependentVariablesWidget-003 | Source: AI-proposed teaching enhancement based on mineral-water crate example and A22 normal-distribution bridge | Insert from widgets/FA22LinearCombinationsOfIndependentVariablesWidget-003.html | Purpose: Practise the second stage of these problems after the new distribution has been found.]

---

# 11. Worked Examples

## Worked Example 1: Notation and the difference between \(X\), \(x\), \(X_i\), and \(x_i\)

Let \(X\sim B(100,0.3)\), where \(X\) represents how many games out of \(100\) are won. \(X\) is the random variable. If one repeat gives \(25\), then \(x=25\). If three repeats give \(32,38,24\), then \(x_1=32\), \(x_2=38\), \(x_3=24\). Before the repeats happen, \(X_1,X_2,X_3\) are random variables with values not yet known.

**Final exam-style answer:** \(X\) is the random variable; \(x\) is a specific observation; \(x_1,x_2,x_3\) are specific observed values; \(X_1,X_2,X_3\) are random observations before values are known.

## Worked Example 2: Egg-box motivation

Suppose egg weights in grams are \(E\sim N(62,3^2)\), empty box weights are \(B\sim N(25,1.9^2)\), and an egg box contains \(6\) eggs. Assume independence. Let \(F\) be the weight of a full egg box.

Use separate egg observations:

\[
F=E_1+E_2+E_3+E_4+E_5+E_6+B.
\]

Mean:

\[
E(F)=6(62)+25=372+25=397.
\]

Variance:

\[
\operatorname{Var}(F)=6(3^2)+1.9^2=54+3.61=57.61.
\]

Therefore:

\[
\boxed{F\sim N(397,57.61).}
\]

## Worked Example 3: Dice starter, \(X+Y\) and \(X-Y\)

Let \(X\) and \(Y\) be independent fair die throws. The evidence gives \(E(X)=3.5\) and \(\operatorname{Var}(X)=35/12\).

\[
E(X+Y)=3.5+3.5=7.
\]

\[
\operatorname{Var}(X+Y)=\frac{35}{12}+\frac{35}{12}=\frac{70}{12}=5.8333\ldots.
\]

\[
E(X-Y)=3.5-3.5=0.
\]

\[
\operatorname{Var}(X-Y)=\frac{35}{12}+\frac{35}{12}=\frac{70}{12}=5.8333\ldots.
\]

## Worked Example 4: Basic linear combination of independent normal variables

Let \(X\sim N(5,2^2)\), \(Y\sim N(10,3^2)\), independent. Find \(A=X+Y\).

\[
E(A)=5+10=15.
\]

\[
\operatorname{Var}(A)=2^2+3^2=4+9=13.
\]

\[
\boxed{A\sim N(15,13).}
\]

## Worked Example 5: Coefficients and subtraction

Let \(X\sim N(5,2^2)\), \(Y\sim N(10,3^2)\), independent. Find \(B=9X-2Y\).

\[
E(B)=9E(X)-2E(Y)=9(5)-2(10)=45-20=25.
\]

\[
\operatorname{Var}(B)=9^2\operatorname{Var}(X)+2^2\operatorname{Var}(Y)=9^2(4)+2^2(9)=324+36=360.
\]

\[
\boxed{B\sim N(25,360).}
\]

## Worked Example 6: Sum of four independent observations

Let \(X\sim N(5,2^2)\), and let \(X_1,X_2,X_3,X_4\) be independent observations from the same distribution as \(X\). Find \(C=\sum_{i=1}^{4}X_i\).

\[
C=X_1+X_2+X_3+X_4.
\]

\[
E(C)=4E(X)=4(5)=20.
\]

\[
\operatorname{Var}(C)=4\operatorname{Var}(X)=4(2^2)=4(4)=16.
\]

\[
\boxed{C\sim N(20,16).}
\]

## Worked Example 7: Mixed scaled variable and sum of observations

Let \(X\sim N(5,2^2)\), \(Y\sim N(10,3^2)\). Let \(Y_1,\ldots,Y_5\) be independent observations from \(Y\), and suppose all variables are independent. Find:

\[
D=3X+\sum_{i=1}^{5}Y_i.
\]

Expand:

\[
D=3X+Y_1+Y_2+Y_3+Y_4+Y_5.
\]

Mean:

\[
E(D)=3E(X)+5E(Y)=3(5)+5(10)=15+50=65.
\]

Variance:

\[
\operatorname{Var}(D)=3^2\operatorname{Var}(X)+5\operatorname{Var}(Y)=3^2(4)+5(9)=36+45=81.
\]

\[
\boxed{D\sim N(65,81).}
\]

## Worked Example 8: Turning \(P(X>Y)\) into a linear-combination problem

Let \(X\sim N(25,6)\), \(Y\sim N(22,10)\), independent. Find \(P(X>Y)\).

\[
P(X>Y)=P(X-Y>0).
\]

\[
E(X-Y)=25-22=3.
\]

\[
\operatorname{Var}(X-Y)=6+10=16.
\]

So:

\[
X-Y\sim N(3,16).
\]

Using \(\mu=3\), \(\sigma=\sqrt{16}=4\):

\[
P(X-Y>0)=0.7734\ldots.
\]

\[
\boxed{P(X>Y)=0.7734\text{ to 4 d.p.}}
\]

## Worked Example 9: Mineral-water crate worded problem

Bottles have weights \(B_i\sim N(2,0.05^2)\). Empty crate weight \(C\sim N(2.5,0.3^2)\). A crate contains \(12\) bottles. Assume independence. Let:

\[
W=B_1+B_2+\cdots+B_{12}+C.
\]

Mean:

\[
E(W)=12(2)+2.5=24+2.5=26.5.
\]

Variance:

\[
\operatorname{Var}(W)=12(0.05^2)+0.3^2=12(0.0025)+0.09=0.03+0.09=0.12.
\]

So:

\[
W\sim N(26.5,0.12).
\]

Part (a):

\[
P(26<W<27)=0.8511\text{ to 4 d.p.}
\]

using \(\mu=26.5\) and \(\sigma=\sqrt{0.12}\).

Part (b): For two bottles:

\[
D=B_1-B_2.
\]

\[
E(D)=2-2=0.
\]

\[
\operatorname{Var}(D)=0.05^2+0.05^2=0.005.
\]

So \(D\sim N(0,0.005)\). We need:

\[
P(|D|>0.1)=2P(D>0.1)=0.1573\text{ to 4 d.p.}
\]

Part (c): Need \(P(W>M)=0.01\). This is a right-tail inverse-normal calculation:

\[
M=27.3\text{ kg to 3 s.f.}
\]

## Worked Example 10: Cross-board enrichment, \(A=4X-3Y\) and \(B=\sum_{i=1}^{4}Y_i\)

This example is cross-board enrichment, not CCEA past-paper evidence.

Let \(A=4X-3Y\), where \(X\sim N(30,3^2)\), \(Y\sim N(20,2^2)\), independent.

\[
E(A)=4(30)-3(20)=120-60=60.
\]

\[
\operatorname{Var}(A)=4^2(3^2)+3^2(2^2)=16(9)+9(4)=144+36=180.
\]

Let \(B=Y_1+Y_2+Y_3+Y_4\), where each \(Y_i\sim N(20,2^2)\).

\[
E(B)=4(20)=80,
\]

\[
\operatorname{Var}(B)=4(2^2)=16.
\]

Now:

\[
P(B>A)=P(B-A>0).
\]

\[
E(B-A)=80-60=20.
\]

\[
\operatorname{Var}(B-A)=16+180=196.
\]

So:

\[
B-A\sim N(20,196).
\]

\[
P(B-A>0)=P\left(Z>\frac{0-20}{14}\right)=P(Z>-1.428571\ldots)=0.923\ldots.
\]

\[
\boxed{P(B>A)=0.923\text{ to 3 s.f.}}
\]

---

# 12. Common Mistakes and Exam Traps

1. **Subtracting variances.** Wrong: \(\operatorname{Var}(X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)\). Correct under independence: \(\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\).
2. **Forgetting to square coefficients.** Correct: \(\operatorname{Var}(3X-2Y)=3^2\operatorname{Var}(X)+2^2\operatorname{Var}(Y)\).
3. **Confusing standard deviation with variance.** If \(W\sim N(26.5,0.12)\), calculator input is \(\sigma=\sqrt{0.12}\).
4. **Treating \(nX\) as the same as \(X_1+\cdots+X_n\).** Same mean, different variance.
5. **Writing a worded total as a scaled single observation.** Twelve bottles means \(B_1+\cdots+B_{12}\), not \(12B\).
6. **Missing independence.** The simple variance rule depends on independence.
7. **Wrong tail in inverse-normal problems.** \(P(W>M)=0.01\) is a right-tail condition.
8. **Forgetting context.** Interpret probabilities and thresholds with units and wording.

---

# 13. Practice Questions

These questions are generated for this lesson. They are **not** past-paper questions and should not be labelled as CCEA past-paper evidence.

## 13.1 Basic fluency questions

1. Let \(X\sim N(12,5)\) and \(Y\sim N(8,3)\), independent. Find the distribution of \(X+Y\).
2. Let \(X\sim N(20,4^2)\) and \(Y\sim N(15,2^2)\), independent. Find the distribution of \(X-Y\).
3. Let \(X\sim N(6,2)\) and \(Y\sim N(10,5)\), independent. Find the distribution of \(3X+2Y\).
4. Let \(X\sim N(5,3^2)\) and \(Y\sim N(4,2^2)\), independent. Find the distribution of \(2X-3Y\).

## 13.2 Bridge questions

5. Let \(X\sim N(30,16)\). Find the distribution of \(4X\). Then state the standard deviation of \(4X\).
6. Let \(X\sim N(30,16)\). Let \(X_1,X_2,X_3,X_4\) be independent observations from the same distribution as \(X\). Find the distribution of \(X_1+X_2+X_3+X_4\). Compare with Question 5.
7. A student writes \(\operatorname{Var}(X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)\). Explain why this is wrong and write the correct formula.

## 13.3 Standard exam-style questions

8. Let \(X\sim N(100,12^2)\) and \(Y\sim N(92,9^2)\), independent. Find \(P(X>Y)\).
9. The weight of a packet of rice, in kg, is \(R\sim N(1.02,0.03^2)\). A box contains \(10\) independently selected packets. The empty box weight, in kg, is \(B\sim N(0.35,0.04^2)\). Let \(T\) be the weight of a full box. Find the distribution of \(T\), then find \(P(T>10.7)\).
10. A rod length is \(L\sim N(50,0.4^2)\). Four rods are independently selected and placed end-to-end. Let \(S\) be their total length. Find the distribution of \(S\), then find \(P(199<S<201)\).

## 13.4 Harder synthesis questions

11. Let \(X\sim N(40,5^2)\), \(Y\sim N(35,4^2)\), all observations independent. Let \(A=2X-Y\). Let \(Y_1,Y_2,Y_3\) be independent observations from \(Y\), and define \(B=Y_1+Y_2+Y_3\). Find \(P(B>A)\).
12. The mass of a chocolate bar, in grams, is \(C\sim N(52,1.5^2)\). A multipack contains \(6\) independently selected bars. Packaging mass is \(P\sim N(18,2^2)\). Find the distribution of the total mass \(M\), then find \(m\) such that only \(5\%\) of multipacks have mass greater than \(m\).

---

# 14. Worked Solutions

## Solution 1

\[
E(X+Y)=12+8=20,
\]

\[
\operatorname{Var}(X+Y)=5+3=8.
\]

\[
\boxed{X+Y\sim N(20,8).}
\]

## Solution 2

\[
E(X-Y)=20-15=5.
\]

\[
\operatorname{Var}(X-Y)=4^2+2^2=16+4=20.
\]

\[
\boxed{X-Y\sim N(5,20).}
\]

## Solution 3

\[
E(3X+2Y)=3(6)+2(10)=18+20=38.
\]

\[
\operatorname{Var}(3X+2Y)=3^2(2)+2^2(5)=18+20=38.
\]

\[
\boxed{3X+2Y\sim N(38,38).}
\]

## Solution 4

\[
E(2X-3Y)=2(5)-3(4)=10-12=-2.
\]

\[
\operatorname{Var}(2X-3Y)=2^2(9)+3^2(4)=36+36=72.
\]

\[
\boxed{2X-3Y\sim N(-2,72).}
\]

## Solution 5

\[
E(4X)=4(30)=120.
\]

\[
\operatorname{Var}(4X)=4^2(16)=256.
\]

\[
\boxed{4X\sim N(120,256)},\qquad \boxed{\sigma=16}.
\]

## Solution 6

\[
E(X_1+X_2+X_3+X_4)=4(30)=120.
\]

\[
\operatorname{Var}(X_1+X_2+X_3+X_4)=4(16)=64.
\]

\[
\boxed{X_1+X_2+X_3+X_4\sim N(120,64).}
\]

Compare: \(4X\sim N(120,256)\). Same mean, different variance.

## Solution 7

The formula is wrong because subtracting an independent random variable still contributes uncertainty. Correct:

\[
\boxed{\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)}.
\]

More generally:

\[
\boxed{\operatorname{Var}(aX-bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y).}
\]

## Solution 8

\[
P(X>Y)=P(X-Y>0).
\]

\[
E(X-Y)=100-92=8.
\]

\[
\operatorname{Var}(X-Y)=12^2+9^2=144+81=225.
\]

So \(X-Y\sim N(8,225)\), with \(\sigma=15\).

\[
P(X-Y>0)=P\left(Z>\frac{0-8}{15}\right)=P(Z>-0.5333\ldots)=0.7031\ldots.
\]

\[
\boxed{P(X>Y)=0.7031\text{ to 4 d.p.}}
\]

## Solution 9

\[
T=R_1+R_2+\cdots+R_{10}+B.
\]

\[
E(T)=10(1.02)+0.35=10.55.
\]

\[
\operatorname{Var}(T)=10(0.03^2)+0.04^2=0.009+0.0016=0.0106.
\]

\[
\boxed{T\sim N(10.55,0.0106).}
\]

\[
P(T>10.7)=P\left(Z>\frac{10.7-10.55}{\sqrt{0.0106}}\right)=P(Z>1.4569\ldots)=0.0726\ldots.
\]

\[
\boxed{P(T>10.7)=0.0726\text{ to 4 d.p.}}
\]

## Solution 10

\[
S=L_1+L_2+L_3+L_4.
\]

\[
E(S)=4(50)=200.
\]

\[
\operatorname{Var}(S)=4(0.4^2)=4(0.16)=0.64.
\]

\[
\boxed{S\sim N(200,0.64).}
\]

\[
P(199<S<201)=P\left(\frac{199-200}{0.8}<Z<\frac{201-200}{0.8}\right)=P(-1.25<Z<1.25)=0.7887\ldots.
\]

\[
\boxed{P(199<S<201)=0.7887\text{ to 4 d.p.}}
\]

## Solution 11

\[
A=2X-Y.
\]

\[
E(A)=2(40)-35=45.
\]

\[
\operatorname{Var}(A)=2^2(25)+16=100+16=116.
\]

So \(A\sim N(45,116)\).

\[
B=Y_1+Y_2+Y_3.
\]

\[
E(B)=3(35)=105,
\]

\[
\operatorname{Var}(B)=3(16)=48.
\]

So \(B\sim N(105,48)\).

\[
P(B>A)=P(B-A>0).
\]

\[
E(B-A)=105-45=60,
\]

\[
\operatorname{Var}(B-A)=48+116=164.
\]

\[
B-A\sim N(60,164).
\]

\[
P(B-A>0)=P\left(Z>\frac{0-60}{\sqrt{164}}\right)=P(Z>-4.6855\ldots)=0.9999986\ldots.
\]

\[
\boxed{P(B>A)=0.999999\text{ approximately}.}
\]

## Solution 12

\[
M=C_1+C_2+C_3+C_4+C_5+C_6+P.
\]

\[
E(M)=6(52)+18=312+18=330.
\]

\[
\operatorname{Var}(M)=6(1.5^2)+2^2=6(2.25)+4=13.5+4=17.5.
\]

\[
\boxed{M\sim N(330,17.5).}
\]

Need \(P(M>m)=0.05\), so \(P(M\le m)=0.95\). With \(z=1.64485\):

\[
m=330+1.64485\sqrt{17.5}=336.8804\ldots.
\]

\[
\boxed{m=337\text{ g to 3 s.f.}}
\]

---

# 15. Exam Technique Notes

1. Start by defining the random variable you need: totals often need \(T=X_1+\cdots+X_n+B\); comparisons often need \(D=X-Y\).
2. State independence before using the variance rule.
3. Mean follows signs, variance adds uncertainty.
4. Do not mix up \(\sigma\) and \(\sigma^2\).
5. For sums of observations, use subscripts.
6. For “differ by more than” questions, use absolute value.
7. For inverse-normal label questions, translate the wording: \(P(W>M)=0.01\) is a right-tail area of \(0.01\), or a left-tail area of \(0.99\).
8. Interpret final answers in context.

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Required content | Covered? | Evidence strength | Notes |
|---|---|---:|---|---|
| `FA22-LINCOMB-LO001` | Use \(E(aX+bY)\) and \(\operatorname{Var}(aX+bY)\) for independent random variables | Yes | Strong | Formulae, worked examples and warnings included. |
| `FA22-LINCOMB-LO002` | Solve problems involving linear combinations of independent normally distributed variables, including sums of independent observations | Yes | Strong | Crate, comparison, rod, rice-box and multipack examples included. |
| `FA22-LINCOMB-LO003` | Understand and use distribution of a multiple of a single observation | Yes | Strong | \(nX\) versus \(X_1+\cdots+X_n\) explained repeatedly. |

## 16.2 Evidence coverage table

| Evidence item | Used? | Where used |
|---|---:|---|
| Notation clarification \(X,x,X_i,x_i\) | Yes | Sections 5, 7, 9, 11 |
| Egg-box motivation | Yes | Sections 6, 8, 11 |
| Dice starter \(X+Y\), \(X-Y\) | Yes | Sections 6, 9, 11 |
| Formulae \(E(X\pm Y)\), \(\operatorname{Var}(X\pm Y)\) | Yes | Sections 7, 8, 11, 14 |
| Formulae \(E(aX\pm bY)\), \(\operatorname{Var}(aX\pm bY)\) | Yes | Sections 8, 11, 14 |
| Scaling intuition | Yes | Sections 8, 9, 12 |
| \(4X\) versus \(X_1+\cdots+X_4\) | Yes | Sections 8, 9, 12, 14 |
| Mineral-water crate example | Yes | Sections 9, 11 |
| Edexcel/S3-style comparison example | Yes, marked cross-board | Section 11 enrichment |
| Proof slides | Not core | Section 16 off-spec |
| DrFrost resource/promotional slides | Not used as lesson content | Section 16 off-spec |

## 16.3 Bridge coverage table

| Bridge area | Covered? | Lesson location |
|---|---:|---|
| Ordinary normal distribution \(X\sim N(\mu,\sigma^2)\) | Yes | Sections 5, 7, 8, 14 |
| Normal probabilities after distribution is formed | Yes | Sections 11, 14, 15 |
| Inverse-normal calculations | Yes | Sections 11, 14, 15 |
| Random-variable notation | Yes | Sections 5, 7, 11 |
| Independence | Yes | Sections 5, 7, 8, 12, 15 |
| Variance versus standard deviation | Yes | Sections 5, 7, 12, 15 |

## 16.4 Off-Spec Content Found but Excluded

| Off-spec / boundary-risk item | Reason excluded from core |
|---|---|
| Formal proofs of the expectation and variance formulae | CCEA elaboration says proofs are not required for this topic. |
| Covariance formulae for non-independent variables | Topic boundary states independent variables. |
| Moment-generating functions | Not in supplied CCEA FA22-LINCOMB boundary. |
| Convolution methods | Not in supplied CCEA FA22-LINCOMB boundary. |
| DrFrost registration/resource promotional slides | Not mathematical content. |
| UKMT and extension references | Not required by CCEA FA22-LINCOMB. |
| Edexcel/S3 exam labels | Cross-board. Used only as enrichment where the mathematics matches CCEA. |

## 16.5 Optional Enrichment Not Required by CCEA

Formal proof of variance addition under independence, non-independent cases, covariance, and deeper derivations of normality of linear combinations are useful enrichment but excluded from the core lesson.

## 16.6 Weak evidence warnings

- The 150-page screenshot PDF is image-based and not fully text-parseable.
- The supplied DrFrost-style PDF is cross-board style and includes Edexcel/S3 labels.
- No CCEA-specific past-paper mark scheme was supplied.
- The parsed text for the mineral-water crate example appears to distort the part (b) threshold as \(0.01\) in one place, but the question wording and final probability \(0.1573\) match \(0.1\text{ kg}\).

## 16.7 Missing Evidence Log

| Missing evidence | Effect |
|---|---|
| CCEA FA22-LINCOMB past-paper examples | Practice questions are generated and clearly labelled as generated. |
| CCEA mark scheme for linear combinations | Exam-technique notes are based on specification and supplied teaching evidence, not mark-scheme quotation. |
| Complete parseable screenshot PDF text | Visual details are preserved only where visible or supported by transcript/PDF text. |
| Full ordinary Maths lesson extracts | Bridge uses available project bridge extract and known ordinary Maths concepts only. |

---

# 17. Recommended Enhancements Not in the Evidence

These enhancements are proposed for teaching value. They are **not** claimed as evidence-backed source content.

- Side-by-side “mean path versus variance path” diagram for \(aX-bY\).
- Variance contribution meter showing that each independent component adds spread.
- Calculator conversion card: \(N(\mu,\sigma^2)\to\) calculator uses \(\mu,\sigma\).
- Comparison diagram for \(P(X>Y)\) becoming \(P(X-Y>0)\).
- Animation of one random variable sliding and stretching under \(aX\).
- Widget asking whether a worded situation is \(nX\) or \(X_1+\cdots+X_n\).

---

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- Ordinary A-Level Maths Bridge Spec Extracts.
- CCEA GCE Mathematics Specification Map, bridge context only.

## 18.2 Lesson-specific evidence used

- Teacher transcript file: Chapter 4, Combinations of Random Variables.
- Slide PDF: FS2 :: Chapter 4 – Combining Variables.
- Screenshot PDF: Chapter 4 Combinations of Random Variables, visual evidence only where visible/readable.

## 18.3 Ordinary A-Level Maths bridge sources used

Bridge content was used only to connect this Further Maths topic to ordinary normal-distribution calculations; expectation and variance; probability notation; independent random variables; and inverse-normal calculations.

Ordinary A-Level Maths sources do not override the CCEA Further Mathematics specification.

## 18.4 Cross-board source notes

The supplied lesson materials use FS2/DrFrost/Edexcel S3-style labels. Their mathematics is included only where it matches the CCEA FA22-LINCOMB topic boundary.

Cross-board exam labels are not treated as CCEA evidence.

## 18.5 Evidence limitations

- Visual evidence from the screenshot PDF was not fully machine-readable.
- Some parsed text from PDFs lost mathematical symbols or distorted thresholds.
- No CCEA-specific mark scheme was supplied.

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

- [ ] Explain what \(X\sim N(\mu,\sigma^2)\) means.
- [ ] Identify \(\mu\), \(\sigma^2\), and \(\sigma\).
- [ ] Calculate normal probabilities using a calculator.
- [ ] Use inverse normal for percentile and tail questions.
- [ ] Understand independence in probability/statistics language.
- [ ] Distinguish uppercase random variables from lowercase observed values.

## 19.2 Further Maths method checklist

- [ ] Write \(E(aX+bY)=aE(X)+bE(Y)\).
- [ ] Write \(E(aX-bY)=aE(X)-bE(Y)\).
- [ ] Write \(\operatorname{Var}(aX\pm bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)\).
- [ ] Remember that variances add even when variables are subtracted.
- [ ] Find the distribution of \(aX\pm bY\).
- [ ] Find the distribution of \(X_1+\cdots+X_n\).
- [ ] Find the distribution of \(nX\).
- [ ] Explain why \(nX\neq X_1+\cdots+X_n\) in general.
- [ ] Convert \(P(X>Y)\) into \(P(X-Y>0)\).
- [ ] Convert “differ by more than” into an absolute-value probability.

## 19.3 Exam technique checklist

- [ ] Define your new random variable clearly.
- [ ] State independence before adding variances.
- [ ] Square coefficients in variance calculations.
- [ ] Use separate observations \(X_1,\ldots,X_n\) for totals.
- [ ] Use \(\sigma=\sqrt{\text{variance}}\) in calculator work.
- [ ] Round probabilities sensibly.
- [ ] Keep units in final contextual answers.
- [ ] Label cross-board examples as practice, not CCEA past papers.

## 19.4 Bridge checklist

- [ ] Ordinary Maths gave me normal probability tools.
- [ ] Further Maths makes me build the normal distribution first.
- [ ] Ordinary transformations scale means.
- [ ] Further Maths makes me square scaling factors for variance.
- [ ] Independence is essential for the simple variance-addition formula.

## 19.5 Diagram and visual understanding checklist

- [ ] Explain why dice tables show \(X+Y\) and \(X-Y\) are new random variables.
- [ ] Explain why subtracting random variables still increases spread.
- [ ] Explain why \(4X\) has larger variance than \(X_1+X_2+X_3+X_4\).
- [ ] Explain why a total crate or box weight must use separate observations.
- [ ] Explain how a right-tail inverse-normal sketch matches wording such as “only \(1\%\) weigh more than \(M\)”.
