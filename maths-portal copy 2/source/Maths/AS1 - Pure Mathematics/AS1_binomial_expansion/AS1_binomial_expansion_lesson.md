# AS1 Binomial Expansion

## 1. Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-SS |
| Topic name | Sequences and series |
| Lesson focus | Binomial Expansion |
| Topic slug | binomial_expansion |
| Topic Pascal | BinomialExpansion |
| Topic ID | AS1BinomialExpansion |
| Lesson file | AS1_binomial_expansion_lesson.md |
| LO IDs | AS1-SS-LO001, AS1-SS-LO002 |
| Date drafted | 2026-06-06 |

## 2. Evidence Map

| Evidence source | How it is used |
|---|---|
| CCEA Mathematics Specification Map | Defines AS1, topic code AS1-SS, LO IDs and syllabus boundary |
| README Module Map | Confirms metadata fields, file naming, phase structure and placeholder rules |
| Source Evidence Drop Checklist | Confirms missing evidence, visual evidence and off-spec logging rules |
| Dr Frost Maths P1 Chapter 8 PDF | Main slide content, examples, definitions, warnings and visual sequence |
| Chapter 8 Binomial Expansion transcript | Detailed teacher explanation and additional worked examples |
| Screenshots PDF | Visual evidence for annotated slide sequence and planned diagram placeholders |

## 3. Specification Alignment

| LO ID | Requirement | Lesson sections |
|---|---|---|
| AS1-SS-LO001 | Use the binomial expansion of $(a+bx)^n$ for positive integer $n$ | Core Theory 8.1 to 8.10, Worked Examples 1 to 11 |
| AS1-SS-LO002 | Use $n!$ and ${}^nC_r$ notation | Core Theory 8.5 to 8.7, Worked Examples 5 to 7 |

## 4. Learning Objectives

By the end of this lesson, the student should be able to:

1. Recognise a binomial expression and expand small positive integer powers using Pascal’s triangle.
2. Explain the pattern of coefficients and powers in $(a+b)^n$.
3. Use factorial notation $n!$.
4. Use choose notation:
   $$
   {}^nC_r=\binom nr=\frac{n!}{r!(n-r)!}.
   $$
5. Use the binomial expansion formula:
   $$
   (a+b)^n=a^n+\binom n1a^{n-1}b+\binom n2a^{n-2}b^2+\cdots+\binom nr a^{n-r}b^r+\cdots+b^n.
   $$
6. Find a single term or coefficient without expanding everything.
7. Use a truncated binomial expansion to estimate a power when the substituted value is small.
8. Avoid common sign, bracket and indexing traps.

## 5. Prerequisite Recap

No GCSE source is used as lesson evidence. The lesson assumes only the following algebraic readiness skills:

| Skill | Needed because |
|---|---|
| Expanding brackets | Binomial expansion generalises repeated bracket expansion |
| Collecting like terms | Coefficients are attached to powers of $x$ |
| Index laws | Powers such as $(3x)^2=9x^2$ must be simplified correctly |
| Negative numbers and powers | Terms such as $(-2x)^3$ carry signs |
| Fractions | Terms such as $\left(-\frac13x\right)^2$ appear |
| Calculator use | $n!$ and $nCr$ may be evaluated efficiently |

## 6. Big Picture Explanation

A binomial is an expression with two terms, such as:

$$
a+b,\qquad 2+3x,\qquad 1-\frac13x.
$$

A binomial expansion is what happens when we raise a binomial to a positive integer power and expand it:

$$
(a+b)^4=(a+b)(a+b)(a+b)(a+b).
$$

Doing this by brute-force multiplication works for small powers, but becomes slow for powers like $10$, $20$, or $75$. Binomial expansion gives a map through the algebra: coefficients come from Pascal’s triangle or from $\binom nr$, and powers move in a predictable pattern.

## 7. Key Definitions and Notation

### 7.1 Binomial

A **binomial** has two terms.

Examples:

$$
a+b,\qquad 2+3x,\qquad 1-2x.
$$

### 7.2 Expansion

An **expansion** removes brackets by multiplying out.

For example:

$$
(a+b)^2=(a+b)(a+b)=a^2+2ab+b^2.
$$

### 7.3 Coefficient

The **coefficient** of a term is the multiplier attached to the variable part.

In

$$
16+96x+216x^2,
$$

the coefficient of $x$ is $96$, and the coefficient of $x^2$ is $216$.

### 7.4 Ascending powers of $x$

Ascending powers of $x$ means the powers go upward:

$$
x^0,\ x^1,\ x^2,\ x^3,\ldots
$$

For example:

$$
1+30x+405x^2+3240x^3+\cdots
$$

is written in ascending powers of $x$.

### 7.5 Factorial notation

For positive integer $n$,

$$
n!=n(n-1)(n-2)\cdots 2\cdot 1.
$$

Example:

$$
5!=5\times4\times3\times2\times1=120.
$$

The evidence also uses:

$$
0!=1.
$$

### 7.6 Choose notation

The notation

$$
{}^nC_r=\binom nr
$$

is read as “$n$ choose $r$”.

It means the number of ways of choosing $r$ things from $n$, where order does not matter.

$$
{}^nC_r=\binom nr=\frac{n!}{r!(n-r)!}.
$$

Example:

$$
\binom{10}{4}
=\frac{10!}{4!6!}
=210.
$$

These numbers are also called **binomial coefficients**.

## 8. Core Theory

## 8.1 The pattern in $(a+b)^n$

Start with small powers.

$$
(a+b)^0=1
$$

$$
(a+b)^1=a+b
$$

$$
(a+b)^2=a^2+2ab+b^2
$$

$$
(a+b)^3=a^3+3a^2b+3ab^2+b^3
$$

$$
(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4
$$

The coefficients form Pascal’s triangle:

$$
\begin{array}{ccccccccc}
&&&&1\\
&&&1&&1\\
&&1&&2&&1\\
&1&&3&&3&&1\\
1&&4&&6&&4&&1
\end{array}
$$

The powers follow a second pattern.

In

$$
(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4,
$$

the power of $a$ decreases:

$$
4,\ 3,\ 2,\ 1,\ 0,
$$

and the power of $b$ increases:

$$
0,\ 1,\ 2,\ 3,\ 4.
$$

Every term has powers adding to $4$:

$$
a^4b^0,\quad a^3b^1,\quad a^2b^2,\quad a^1b^3,\quad a^0b^4.
$$

## 8.2 Pascal’s triangle

Pascal’s triangle begins:

$$
\begin{array}{ccccccccccc}
&&&&&1\\
&&&&1&&1\\
&&&1&&2&&1\\
&&1&&3&&3&&1\\
&1&&4&&6&&4&&1\\
1&&5&&10&&10&&5&&1
\end{array}
$$

Each non-edge entry is the sum of the two entries above it.

For example:

$$
6=3+3,
$$

and

$$
10=4+6.
$$

The transcript notes a typo in the slide row for the fifth power: the correct row is

$$
1,\ 5,\ 10,\ 10,\ 5,\ 1.
$$

The row used for $(a+b)^n$ is the row indexed by $n$, if the top row is called row $0$.

So:

$$
(a+b)^4
$$

uses

$$
1,\ 4,\ 6,\ 4,\ 1.
$$

## 8.3 Expanding with Pascal’s triangle

For small powers, use this structure:

$$
(a+b)^n
$$

has coefficients from Pascal’s triangle, with powers:

$$
a^n,\quad a^{n-1}b,\quad a^{n-2}b^2,\quad \ldots,\quad b^n.
$$

For example, for power $4$:

$$
(a+b)^4
=
1a^4+4a^3b+6a^2b^2+4ab^3+1b^4.
$$

When substituting expressions such as $2$ and $3x$, keep the whole term in brackets when raising to a power:

$$
(3x)^2=9x^2,
$$

not

$$
3x^2.
$$

## 8.4 Negative terms

If the binomial contains a negative term, rewrite it as adding a negative term.

$$
1-2x=1+(-2x).
$$

Then expand using $(-2x)$ as the second term.

Signs often alternate:

$$
+,\ -,\ +,\ -,\ldots
$$

because powers of a negative term alternate depending on whether the power is odd or even.

## 8.5 Factorials

Factorial notation is:

$$
n!=n(n-1)(n-2)\cdots2\cdot1.
$$

Example:

$$
5!=5\times4\times3\times2\times1=120.
$$

For arranging three letters $A,B,C$, there are:

$$
3\times2\times1=3!=6
$$

arrangements:

$$
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
$$

The evidence accepts and justifies:

$$
0!=1.
$$

One way to see this is:

$$
\binom{20}{0}
=
\frac{20!}{0!20!}
=
1.
$$

For this to be true,

$$
0!=1.
$$

## 8.6 Choose notation and binomial coefficients

The choose function is:

$$
{}^nC_r=\binom nr=\frac{n!}{r!(n-r)!}.
$$

Example:

$$
\binom53
=
\frac{5!}{3!2!}
$$

$$
=
\frac{120}{6\times2}
$$

$$
=
10.
$$

Example:

$$
\binom{20}{1}
=
\frac{20!}{1!19!}
=
20.
$$

So, in general:

$$
\binom n1=n.
$$

Example:

$$
\binom{20}{2}
=
\frac{20!}{2!18!}
$$

$$
=
\frac{20\times19\times18\times17\times\cdots\times1}{2!\times18\times17\times\cdots\times1}
$$

$$
=
\frac{20\times19}{2!}
$$

$$
=190.
$$

So, in general:

$$
\binom n2=\frac{n(n-1)}2.
$$

Also:

$$
\binom{20}{18}
=
\frac{20!}{18!2!}
=
\binom{20}{2}
=
190.
$$

This symmetry appears in Pascal’s triangle:

$$
\binom41=\binom43.
$$

## 8.7 Why Pascal’s triangle and $\binom nr$ are linked

Consider:

$$
(a+b)^5=(a+b)(a+b)(a+b)(a+b)(a+b).
$$

Each term in the expansion is made by choosing one term from each bracket.

To get

$$
a^3b^2,
$$

we must choose $a$ from 3 of the 5 brackets, and $b$ from the other 2 brackets.

The number of ways to choose the 3 brackets that contribute $a$ is:

$$
\binom53.
$$

Therefore the coefficient of $a^3b^2$ in $(a+b)^5$ is:

$$
\binom53=10.
$$

That is why the row

$$
1,\ 5,\ 10,\ 10,\ 5,\ 1
$$

can also be written as:

$$
\binom50,\ \binom51,\ \binom52,\ \binom53,\ \binom54,\ \binom55.
$$

## 8.8 The binomial expansion formula

For positive integer $n$,

$$
(a+b)^n
=
a^n
+\binom n1a^{n-1}b
+\binom n2a^{n-2}b^2
+\cdots
+\binom nr a^{n-r}b^r
+\cdots
+b^n.
$$

The general term is:

$$
\binom nr a^{n-r}b^r.
$$

Important boundary:

$$
n\in\mathbb N,
$$

so this AS1 formula is for positive integer powers only.

Fractional or negative powers are not core content for this AS1 lesson.

## 8.9 Extracting a single term

For

$$
(a+b)^n,
$$

the term containing $b^r$ is:

$$
\binom nr a^{n-r}b^r.
$$

The two powers always add to $n$:

$$
(n-r)+r=n.
$$

So if you want the $x^4$ term in

$$
(1+qx)^{10},
$$

use $r=4$:

$$
\binom{10}{4}(1)^6(qx)^4.
$$

You do not need the full expansion.

## 8.10 Estimating powers

A truncated binomial expansion can estimate powers when the omitted terms are very small.

For example:

$$
\left(1+\frac x4\right)^8
=
1+2x+\frac74x^2+\frac78x^3+\cdots.
$$

To estimate:

$$
1.025^8,
$$

match:

$$
1+\frac x4=1.025.
$$

Then:

$$
\frac x4=0.025
$$

$$
x=0.1.
$$

Substitute $x=0.1$:

$$
1+2(0.1)+\frac74(0.1)^2+\frac78(0.1)^3
$$

$$
=1+0.2+\frac74(0.01)+\frac78(0.001)
$$

$$
=1+0.2+0.0175+0.000875
$$

$$
=1.218375.
$$

So:

$$
1.025^8\approx1.2184
$$

to 4 decimal places.

The reason this is reasonable is that powers such as

$$
0.1^4,\ 0.1^5,\ldots
$$

become very small.

## 9. Visual Asset Integration

No diagrams, TikZ or widgets are generated inside this Markdown lesson file. The generated assets are linked as placeholders below.

[VISUAL PLACEHOLDER: AS1BinomialExpansionSVG-001 | Source: Dr Frost slide PDF pages 4-5 and screenshots visual evidence | Insert from svg/AS1BinomialExpansionSVG-001.svg | Purpose: Show $(a+b)^0$ to $(a+b)^4$, highlighting Pascal coefficients and increasing/decreasing powers.]

[VISUAL PLACEHOLDER: AS1BinomialExpansionSVG-002 | Source: Dr Frost slide PDF pages 5 and 13 | Insert from svg/AS1BinomialExpansionSVG-002.svg | Purpose: Display Pascal’s triangle with row indexing from row 0 and entries as $\binom nr$.]

[VISUAL PLACEHOLDER: AS1BinomialExpansionSVG-003 | Source: Dr Frost slide PDF page 16 | Insert from svg/AS1BinomialExpansionSVG-003.svg | Purpose: Explain why $\binom53$ counts the number of ways to obtain $a^3b^2$ from $(a+b)^5$.]

[VISUAL PLACEHOLDER: AS1BinomialExpansionTIKZ-001 | Source: Lesson evidence and CCEA specification boundary | Insert from tikz/AS1BinomialExpansionTIKZ-001.tex | Purpose: Create a clean coefficient table for the general term $\binom nr a^{n-r}b^r$.]

[INTERACTIVE PLACEHOLDER: AS1BinomialExpansionWIDGET-001 | Source: Lesson evidence and CCEA AS1-SS-LO001 | Insert from widgets/AS1BinomialExpansionWIDGET-001.html | Purpose: Let the student choose $n$, $a$, and $b$, then see powers and coefficients generated term by term.]

[VISUAL PLACEHOLDER: AS1BinomialExpansionMMD-001 | Source: Lesson evidence and CCEA AS1-SS boundary | Insert from mermaid/AS1BinomialExpansionMMD-001.md | Purpose: Method decision flowchart for expansion, coefficient extraction and estimation.]

## 10. Worked Examples

## Example 1: Expand $(2+3x)^4$

Use row $4$ of Pascal’s triangle:

$$
1,\ 4,\ 6,\ 4,\ 1.
$$

Set up the terms:

$$
(2+3x)^4
=
1(2^4)
+4(2^3)(3x)
+6(2^2)(3x)^2
+4(2^1)(3x)^3
+1(3x)^4.
$$

Now simplify each term.

First term:

$$
1(2^4)=16.
$$

Second term:

$$
4(2^3)(3x)
=
4(8)(3x)
$$

$$
=32(3x)
$$

$$
=96x.
$$

Third term:

$$
6(2^2)(3x)^2
=
6(4)(9x^2)
$$

$$
=24(9x^2)
$$

$$
=216x^2.
$$

Fourth term:

$$
4(2)(3x)^3
=
8(27x^3)
$$

$$
=216x^3.
$$

Fifth term:

$$
(3x)^4=81x^4.
$$

Therefore:

$$
(2+3x)^4
=
16+96x+216x^2+216x^3+81x^4.
$$

## Example 2: Expand $(1-2x)^3$

Rewrite:

$$
1-2x=1+(-2x).
$$

Use row $3$ of Pascal’s triangle:

$$
1,\ 3,\ 3,\ 1.
$$

$$
(1-2x)^3
=
1(1^3)
+3(1^2)(-2x)
+3(1)(-2x)^2
+1(-2x)^3.
$$

First term:

$$
1(1^3)=1.
$$

Second term:

$$
3(1^2)(-2x)=3(-2x)=-6x.
$$

Third term:

$$
3(1)(-2x)^2
=
3(4x^2)
=
12x^2.
$$

Fourth term:

$$
(-2x)^3=-8x^3.
$$

Therefore:

$$
(1-2x)^3=1-6x+12x^2-8x^3.
$$

Notice the alternating signs:

$$
+,\ -,\ +,\ -.
$$

## Example 3: Find $c$ from a coefficient

The coefficient of $x^2$ in the expansion of

$$
(2-cx)^5
$$

is $720$. Find the possible values of $c$.

Use row $5$:

$$
1,\ 5,\ 10,\ 10,\ 5,\ 1.
$$

We want the $x^2$ term, so the $(-cx)$ part must have power $2$.

Because the total power is $5$, the $2$ part must have power $3$.

So the required term is:

$$
10(2^3)(-cx)^2.
$$

Now simplify:

$$
10(2^3)(-cx)^2
=
10(8)(c^2x^2)
$$

$$
=80c^2x^2.
$$

The coefficient of $x^2$ is therefore:

$$
80c^2.
$$

Given:

$$
80c^2=720.
$$

Divide by $80$:

$$
c^2=9.
$$

Square root:

$$
c=\pm3.
$$

Therefore:

$$
\boxed{c=\pm3}.
$$

## Example 4: First three terms of $(2+kx)^7$, then find $k$

Find the first three terms in ascending powers of $x$ of

$$
(2+kx)^7.
$$

Use the first three coefficients from row $7$:

$$
1,\ 7,\ 21.
$$

$$
(2+kx)^7
=
1(2^7)
+7(2^6)(kx)
+21(2^5)(kx)^2+\cdots.
$$

First term:

$$
2^7=128.
$$

Second term:

$$
7(2^6)(kx)
=
7(64)kx
=
448kx.
$$

Third term:

$$
21(2^5)(kx)^2
=
21(32)k^2x^2
=
672k^2x^2.
$$

So:

$$
(2+kx)^7
=
128+448kx+672k^2x^2+\cdots.
$$

Now suppose the coefficient of $x^2$ is six times the coefficient of $x$.

Coefficient of $x$:

$$
448k.
$$

Coefficient of $x^2$:

$$
672k^2.
$$

So:

$$
672k^2=6(448k).
$$

Simplify the right-hand side:

$$
6(448k)=2688k.
$$

So:

$$
672k^2=2688k.
$$

Assuming the non-zero value relevant to the expansion comparison, divide by $k$:

$$
672k=2688.
$$

Divide by $672$:

$$
k=4.
$$

Therefore:

$$
\boxed{k=4}.
$$

## Example 5: Factorial and choose values

### Part a

$$
5!=5\times4\times3\times2\times1=120.
$$

### Part b

$$
\binom53
=
\frac{5!}{3!2!}
$$

$$
=
\frac{120}{6\times2}
$$

$$
=
\frac{120}{12}
$$

$$
=10.
$$

### Part c

$$
0!=1.
$$

### Part d

$$
\binom{20}{1}
=
\frac{20!}{1!19!}
$$

$$
=
20.
$$

### Part e

$$
\binom{20}{0}
=
\frac{20!}{0!20!}
=
1.
$$

This supports:

$$
0!=1.
$$

### Part f

$$
\binom{20}{2}
=
\frac{20!}{2!18!}
$$

$$
=
\frac{20\times19\times18\times\cdots\times1}{2!\times18\times17\times\cdots\times1}
$$

$$
=
\frac{20\times19}{2}
$$

$$
=190.
$$

### Part g

$$
\binom{20}{18}
=
\frac{20!}{18!2!}
$$

$$
=
\binom{20}{2}
$$

$$
=190.
$$

## Example 6: Expand $(3x+1)^{10}$ for the first four terms

Find the first four terms in ascending powers of $x$.

Because we want ascending powers of $x$, use powers of $3x$ increasing:

$$
(3x)^0,\ (3x)^1,\ (3x)^2,\ (3x)^3.
$$

The coefficients are:

$$
\binom{10}{0},\ \binom{10}{1},\ \binom{10}{2},\ \binom{10}{3}.
$$

Calculate:

$$
\binom{10}{0}=1,
$$

$$
\binom{10}{1}=10,
$$

$$
\binom{10}{2}=45,
$$

$$
\binom{10}{3}=120.
$$

So:

$$
(3x+1)^{10}
=
\binom{10}{0}(1^{10})
+\binom{10}{1}(1^9)(3x)
+\binom{10}{2}(1^8)(3x)^2
+\binom{10}{3}(1^7)(3x)^3
+\cdots.
$$

Simplify:

$$
=1+10(3x)+45(9x^2)+120(27x^3)+\cdots
$$

$$
=1+30x+405x^2+3240x^3+\cdots.
$$

Therefore:

$$
\boxed{(3x+1)^{10}=1+30x+405x^2+3240x^3+\cdots}.
$$

## Example 7: Expand $\left(2-\frac13x\right)^7$ for the first three terms

$$
\left(2-\frac13x\right)^7
=
\binom70(2^7)
+
\binom71(2^6)\left(-\frac13x\right)
+
\binom72(2^5)\left(-\frac13x\right)^2
+\cdots.
$$

First term:

$$
\binom70(2^7)=1(128)=128.
$$

Second term:

$$
\binom71(2^6)\left(-\frac13x\right)
=
7(64)\left(-\frac13x\right)
$$

$$
=
448\left(-\frac13x\right)
$$

$$
=-\frac{448}{3}x.
$$

Third term:

$$
\binom72(2^5)\left(-\frac13x\right)^2
=
21(32)\left(\frac19x^2\right)
$$

$$
=
672\left(\frac19x^2\right)
$$

$$
=\frac{672}{9}x^2
$$

$$
=\frac{224}{3}x^2.
$$

Therefore:

$$
\boxed{
\left(2-\frac13x\right)^7
=
128-\frac{448}{3}x+\frac{224}{3}x^2+\cdots
}.
$$

## Example 8: Find $q$ from $(1+qx)^{10}$

The coefficient of $x^4$ in

$$
(1+qx)^{10}
$$

is $3360$. Find $q$.

The $x^4$ term is:

$$
\binom{10}{4}(1)^6(qx)^4.
$$

Calculate:

$$
\binom{10}{4}=210.
$$

So:

$$
\binom{10}{4}(1)^6(qx)^4
=
210q^4x^4.
$$

The coefficient is:

$$
210q^4.
$$

Given:

$$
210q^4=3360.
$$

Divide by $210$:

$$
q^4=16.
$$

So:

$$
q=\pm2.
$$

Therefore:

$$
\boxed{q=\pm2}.
$$

## Example 9: Coefficient comparison in $(1+ax)^{10}$

In the expansion of

$$
(1+ax)^{10},
$$

where $a$ is non-zero, the coefficient of $x^3$ is double the coefficient of $x^2$. Find $a$.

The $x^2$ term is:

$$
\binom{10}{2}(1)^8(ax)^2.
$$

$$
\binom{10}{2}=45.
$$

So:

$$
x^2\text{ term}=45a^2x^2.
$$

The coefficient of $x^2$ is:

$$
45a^2.
$$

The $x^3$ term is:

$$
\binom{10}{3}(1)^7(ax)^3.
$$

$$
\binom{10}{3}=120.
$$

So:

$$
x^3\text{ term}=120a^3x^3.
$$

The coefficient of $x^3$ is:

$$
120a^3.
$$

The coefficient of $x^3$ is double the coefficient of $x^2$:

$$
120a^3=2(45a^2).
$$

$$
120a^3=90a^2.
$$

Bring all terms to one side:

$$
120a^3-90a^2=0.
$$

Factor:

$$
30a^2(4a-3)=0.
$$

So:

$$
a=0
$$

or

$$
4a-3=0.
$$

But $a$ is non-zero, so reject $a=0$.

$$
4a=3.
$$

$$
a=\frac34.
$$

Therefore:

$$
\boxed{a=\frac34}.
$$

## Example 10: Estimating $1.025^8$

First expand:

$$
\left(1+\frac x4\right)^8.
$$

The first four terms are:

$$
\binom80(1)^8
+
\binom81(1)^7\left(\frac x4\right)
+
\binom82(1)^6\left(\frac x4\right)^2
+
\binom83(1)^5\left(\frac x4\right)^3.
$$

Calculate the coefficients:

$$
\binom80=1,\qquad \binom81=8,\qquad \binom82=28,\qquad \binom83=56.
$$

So:

$$
\left(1+\frac x4\right)^8
=
1+8\left(\frac x4\right)+28\left(\frac x4\right)^2+56\left(\frac x4\right)^3+\cdots.
$$

Simplify:

$$
8\left(\frac x4\right)=2x.
$$

$$
28\left(\frac x4\right)^2
=
28\left(\frac{x^2}{16}\right)
=
\frac{28}{16}x^2
=
\frac74x^2.
$$

$$
56\left(\frac x4\right)^3
=
56\left(\frac{x^3}{64}\right)
=
\frac{56}{64}x^3
=
\frac78x^3.
$$

Therefore:

$$
\left(1+\frac x4\right)^8
=
1+2x+\frac74x^2+\frac78x^3+\cdots.
$$

Now match:

$$
1+\frac x4=1.025.
$$

$$
\frac x4=0.025.
$$

$$
x=0.1.
$$

Substitute:

$$
1.025^8
\approx
1+2(0.1)+\frac74(0.1)^2+\frac78(0.1)^3.
$$

$$
=
1+0.2+\frac74(0.01)+\frac78(0.001).
$$

$$
=
1+0.2+0.0175+0.000875.
$$

$$
=
1.218375.
$$

So:

$$
\boxed{1.025^8\approx1.2184}
$$

to 4 decimal places.

## Example 11: Product with a binomial expansion

Find the coefficient of $x$ in:

$$
\left(3+\frac1{x^3}\right)(2+x)^7.
$$

We do not need the whole expansion of $(2+x)^7$. We only need the terms that can become $x$ after multiplication.

From the $3$ part:

$$
3\times(\text{$x$ term of }(2+x)^7)
$$

will give an $x$ term.

From the $\frac1{x^3}$ part:

$$
\frac1{x^3}\times(\text{$x^4$ term of }(2+x)^7)
$$

will also give an $x$ term.

Find the $x$ term of $(2+x)^7$:

$$
\binom71(2^6)x
=
7(64)x
=
448x.
$$

Find the $x^4$ term of $(2+x)^7$:

$$
\binom74(2^3)x^4.
$$

$$
\binom74=35.
$$

So:

$$
35(8)x^4=280x^4.
$$

Now multiply by the outside bracket:

$$
3(448x)+\frac1{x^3}(280x^4)
$$

$$
=
1344x+280x
$$

$$
=
1624x.
$$

Therefore the coefficient of $x$ is:

$$
\boxed{1624}.
$$

## 11. Guided Practice

### Question 1

Expand:

$$
(4+5x)^{10}
$$

up to and including the $x^3$ term, in ascending powers of $x$.

### Question 2

Given that:

$$
\binom83=\frac{8!}{3!a!},
$$

find $a$.

### Question 3

Find the coefficient of $x^4$ in:

$$
(3+2ax)^{10}.
$$

Then, given that this coefficient is:

$$
\frac{1120}{3},
$$

find $a$, assuming $a>0$.

### Question 4

Find the first three terms in ascending powers of $x$ of:

$$
\left(2-\frac x2\right)^7.
$$

Then explain how to use your expansion to estimate:

$$
1.995^7.
$$

### Question 5

Find the constant term in:

$$
\left(3+\frac1{x^3}\right)(2+x)^7.
$$

## 12. Common Mistakes and Exam Traps

| Trap | What goes wrong | Correct approach |
|---|---|---|
| Forgetting brackets | Writing $(3x)^2=3x^2$ | $(3x)^2=9x^2$ |
| Squaring only the variable | Treating $(-2x)^2$ as $-4x^2$ | $(-2x)^2=4x^2$ |
| Wrong sign pattern | Two negative terms appear in a row when signs should alternate | Track powers of the negative term |
| Wrong Pascal row | Using row 5 for power 4 | Row indexing starts at 0 |
| Expanding everything unnecessarily | Time lost finding one coefficient | Use $\binom nr a^{n-r}b^r$ |
| Misreading “six times” | Setting the smaller coefficient equal to six times the larger one | Translate the sentence carefully |
| Dividing by a variable that could be zero | Losing possible solutions or failing to reject invalid ones | Check whether the question says non-zero |
| Using AS1 formula for non-integer powers | Applying finite expansion where it does not apply | AS1 formula here is positive integer $n$ only |
| Ignoring dots $\cdots$ | Treating a truncated expansion as exact | Use $\cdots$ when terms are omitted |

## 13. Exam Technique

### 13.1 When asked for the first few terms

Use this table method:

| Column | Meaning |
|---|---|
| Coefficient | $\binom n0,\binom n1,\binom n2,\ldots$ |
| First binomial term | Powers decrease |
| Second binomial term | Powers increase |
| Multiply down | Each column gives one term |

### 13.2 When asked for a coefficient

Do not expand everything. Use:

$$
\binom nr a^{n-r}b^r.
$$

Choose $r$ by matching the required power of $x$.

### 13.3 When a binomial contains a negative term

Use brackets:

$$
(2-3x)^7=(2+(-3x))^7.
$$

Then terms involving odd powers of $(-3x)$ will be negative.

### 13.4 When using estimation

Match the bracket exactly.

For example:

$$
1+\frac x4=1.025
$$

must be solved before substituting into the expansion.

Also explain why the approximation is good:

$$
x=0.1
$$

is small, so higher powers such as $x^4$ are very small.

## 14. Full Worked Solutions to Guided Practice

## Solution 1

Expand:

$$
(4+5x)^{10}
$$

up to and including the $x^3$ term.

Use:

$$
(a+b)^n
=
\sum_{r=0}^{n}\binom nr a^{n-r}b^r.
$$

Here:

$$
a=4,\qquad b=5x,\qquad n=10.
$$

The first four terms are:

$$
\binom{10}{0}4^{10}
+
\binom{10}{1}4^9(5x)
+
\binom{10}{2}4^8(5x)^2
+
\binom{10}{3}4^7(5x)^3.
$$

Term 1:

$$
\binom{10}{0}4^{10}=1(4^{10}).
$$

$$
4^{10}=1048576.
$$

Term 2:

$$
\binom{10}{1}4^9(5x)
=
10(4^9)(5x).
$$

$$
4^9=262144.
$$

$$
10(262144)(5x)=13107200x.
$$

Term 3:

$$
\binom{10}{2}4^8(5x)^2
=
45(4^8)(25x^2).
$$

$$
4^8=65536.
$$

$$
45(65536)(25x^2)
=
73728000x^2.
$$

Term 4:

$$
\binom{10}{3}4^7(5x)^3
=
120(4^7)(125x^3).
$$

$$
4^7=16384.
$$

$$
120(16384)(125x^3)
=
245760000x^3.
$$

Therefore:

$$
\boxed{
(4+5x)^{10}
=
1048576+13107200x+73728000x^2+245760000x^3+\cdots
}.
$$

## Solution 2

Given:

$$
\binom83=\frac{8!}{3!a!}.
$$

But the choose formula says:

$$
\binom83=\frac{8!}{3!(8-3)!}.
$$

$$
8-3=5.
$$

So:

$$
\binom83=\frac{8!}{3!5!}.
$$

Compare:

$$
\frac{8!}{3!a!}=\frac{8!}{3!5!}.
$$

Therefore:

$$
a!=5!.
$$

So:

$$
\boxed{a=5}.
$$

## Solution 3

Find the coefficient of $x^4$ in:

$$
(3+2ax)^{10}.
$$

The $x^4$ term is:

$$
\binom{10}{4}3^6(2ax)^4.
$$

Now simplify.

$$
\binom{10}{4}=210.
$$

$$
(2ax)^4=2^4a^4x^4=16a^4x^4.
$$

$$
3^6=729.
$$

So the term is:

$$
210(729)(16a^4x^4).
$$

$$
210\times729\times16=2449440.
$$

Therefore the $x^4$ term is:

$$
2449440a^4x^4.
$$

The coefficient is:

$$
2449440a^4.
$$

Given:

$$
2449440a^4=\frac{1120}{3}.
$$

Divide:

$$
a^4=\frac{\frac{1120}{3}}{2449440}.
$$

$$
a^4=\frac1{6561}.
$$

Take the fourth root:

$$
a=\sqrt[4]{\frac1{6561}}.
$$

Since:

$$
6561=9^4,
$$

$$
\sqrt[4]{6561}=9.
$$

So:

$$
a=\frac19.
$$

Therefore:

$$
\boxed{a=\frac19}.
$$

## Solution 4

Find the first three terms of:

$$
\left(2-\frac x2\right)^7.
$$

Use:

$$
\binom70(2^7)
+
\binom71(2^6)\left(-\frac x2\right)
+
\binom72(2^5)\left(-\frac x2\right)^2
+\cdots.
$$

First term:

$$
\binom70(2^7)=128.
$$

Second term:

$$
\binom71(2^6)\left(-\frac x2\right)
=
7(64)\left(-\frac x2\right)
$$

$$
=
448\left(-\frac x2\right)
$$

$$
=-224x.
$$

Third term:

$$
\binom72(2^5)\left(-\frac x2\right)^2
=
21(32)\left(\frac{x^2}{4}\right)
$$

$$
=
672\left(\frac{x^2}{4}\right)
$$

$$
=168x^2.
$$

Therefore:

$$
\boxed{
\left(2-\frac x2\right)^7
=
128-224x+168x^2+\cdots
}.
$$

To estimate:

$$
1.995^7,
$$

match:

$$
2-\frac x2=1.995.
$$

Subtract $1.995$ from $2$:

$$
\frac x2=2-1.995.
$$

$$
\frac x2=0.005.
$$

Multiply by $2$:

$$
x=0.01.
$$

So substitute:

$$
x=0.01
$$

into:

$$
128-224x+168x^2+\cdots.
$$

That gives an estimate for:

$$
1.995^7.
$$

## Solution 5

Find the constant term in:

$$
\left(3+\frac1{x^3}\right)(2+x)^7.
$$

A constant term can come from:

$$
3\times(\text{constant term of }(2+x)^7)
$$

or from:

$$
\frac1{x^3}\times(\text{$x^3$ term of }(2+x)^7).
$$

First find the constant term of $(2+x)^7$:

$$
2^7=128.
$$

So the contribution from $3$ is:

$$
3(128)=384.
$$

Now find the $x^3$ term of $(2+x)^7$:

$$
\binom73(2^4)x^3.
$$

$$
\binom73=35.
$$

$$
2^4=16.
$$

So:

$$
35(16)x^3=560x^3.
$$

Multiply by:

$$
\frac1{x^3}.
$$

$$
\frac1{x^3}(560x^3)=560.
$$

Total constant term:

$$
384+560=944.
$$

Therefore:

$$
\boxed{944}.
$$

## 15. Syllabus Gap Check

| LO ID | Covered? | Evidence-backed content included |
|---|---|---|
| AS1-SS-LO001 | Yes | Positive integer binomial expansion, Pascal’s triangle, binomial coefficients, first terms, single terms, coefficient comparison, estimation |
| AS1-SS-LO002 | Yes | $n!$, $0!$, ${}^nC_r$, $\binom nr$, formula and calculator notation |

### Off-spec material excluded from required core

- Pascal’s Rule proof.
- STEP/MAT/AEA extension questions.
- Fractional and negative binomial powers.
- Generalised binomial theorem for non-integer $n$.
- Any cross-board exam branding as required CCEA evidence.

## 16. Visual and Interactive Asset Plan

| Asset ID | Type | Purpose | Phase |
|---|---|---|---|
| AS1BinomialExpansionSVG-001 | SVG | Pattern from $(a+b)^0$ to $(a+b)^4$ | Phase 3 |
| AS1BinomialExpansionSVG-002 | SVG | Pascal’s triangle with row $0$ indexing | Phase 3 |
| AS1BinomialExpansionSVG-003 | SVG | Choosing terms from five brackets to get $a^3b^2$ | Phase 3 |
| AS1BinomialExpansionTIKZ-001 | TikZ | General term coefficient table | Phase 4 |
| AS1BinomialExpansionWIDGET-001 | HTML widget | Interactive expansion builder | Phase 5 |
| AS1BinomialExpansionMMD-001 | Mermaid | Method decision flowchart | Phase 2 |

## 17. Supplementary Sources Used

No external web sources were used.

Cross-board evidence appears in the supplied lesson materials, especially Edexcel C2 examples and Pearson exercise references. These were only used where the mathematical content matched the CCEA AS1-SS boundary. Extension material from MAT, STEP and AEA was logged but not treated as required core content.

## 18. Final Student Checklist

Before moving on, the student should be able to say “yes” to each item:

| Checklist item | Yes/Not yet |
|---|---|
| I can write the first rows of Pascal’s triangle correctly. |  |
| I know that row $n$ is used for $(a+b)^n$. |  |
| I can explain why powers in each term add to $n$. |  |
| I can expand small powers using Pascal’s triangle. |  |
| I can use $n!$. |  |
| I can use $\binom nr=\frac{n!}{r!(n-r)!}$. |  |
| I can find the first few terms of $(a+bx)^n$. |  |
| I can find a single coefficient without expanding everything. |  |
| I remember to put terms like $(-2x)$ and $(3x)$ in brackets before raising powers. |  |
| I know that the AS1 finite binomial formula here is for positive integer $n$. |  |
| I can use a small $x$ value in a truncated expansion to estimate a power. |  |
