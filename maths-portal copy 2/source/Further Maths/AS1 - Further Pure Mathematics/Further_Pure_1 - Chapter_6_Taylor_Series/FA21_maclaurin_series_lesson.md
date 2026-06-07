# 1. Lesson Title and Metadata

# FA21 Further A2 1 Pure Mathematics: Maclaurin Series

| Field | Value |
|---|---|
| Date generated | 2026-06-03 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA21` - Further A2 1 Pure Mathematics |
| Applied section | Pure |
| Topic code | `FA21-FAF` |
| Topic name | Further algebra and functions - Maclaurin series |
| Topic slug | `maclaurin_series` |
| Topic Pascal | `MaclaurinSeries` |
| Topic ID | `FA21MaclaurinSeries` |
| Lesson file name | `FA21_maclaurin_series_lesson.md` |
| Core LO IDs | `FA21-FAF-LO004`, `FA21-FAF-LO005`, `FA21-FAF-LO006`, `FA21-FAF-LO007` |
| Bridge tags | differentiation, gradients, higher derivatives, factorials, trig exact values, radians, logarithms, binomial expansion, sequences and series |
| Topic tags | Maclaurin series, power series, standard series, range of validity, compound functions, small-angle approximations |

## Boundary Notice

The supplied chapter evidence is titled **Taylor Series** and includes Taylor expansions about \(x=a\), limits using series, and series solutions of differential equations. The CCEA Further Mathematics topic boundary identified for this lesson is **Maclaurin series** within `FA21-FAF`. Therefore:

- Maclaurin series and standard Maclaurin expansions are core.
- Simple compound expansions are core.
- Small-angle approximations in radians are core.
- Taylor series about arbitrary \(x=a\), limits using Taylor expansions and series solutions of differential equations are logged as optional enrichment or excluded from the core lesson.

This is not a downgrade of the mathematics. It is a syllabus boundary guardrail, the little golden fence around the garden.

---

# 2. Evidence Map

| Source | Evidence used in this lesson | Core or boundary role |
|---|---|---|
| CCEA Further Mathematics specification map | Confirms `FA21-FAF` and LO IDs `FA21-FAF-LO004` to `FA21-FAF-LO007`. | Core authority |
| Further Maths module map | Confirms naming, metadata conventions and bridge workflow. | Workflow authority |
| Further Maths evidence checklist | Confirms evidence hierarchy and missing-evidence logging. | Workflow authority |
| Ordinary A-Level Maths bridge extracts | Supports prerequisites: derivatives, trig, radians, factorials, logs and binomial expansion. | Bridge only |
| DrFrost/Pearson PDF `FP1-Chp6-TaylorSeries.pdf` | Gives Maclaurin recap, derivative matching, \(\sin x\) expansion, Maclaurin formula, Taylor material, limits and differential-equation extensions. | Core only where CCEA supports it; otherwise boundary log |
| Teacher transcript `transcripts.md` | Gives teacher explanation of Maclaurin versus Taylor, approximation near the expansion point, repeated differentiation, radians and cross-board exam notes. | Core only where CCEA supports it; otherwise boundary log |
| Screenshot PDF `Chapter_6_Taylor_Series_🧩_(Further_Pure_1)_screenshots.pdf` | Confirms visual slide sequence and graph/slide evidence. | Visual evidence, partially inspected |

The PDF evidence states that in an earlier Core Pure chapter, functions such as trigonometric functions were written as power series, meaning infinitely long polynomials, and that such polynomials only necessarily match the exact shape around \(x=0\). The same evidence shows the Maclaurin idea as matching successive derivatives at \(x=0\): first the value, then the gradient, then the second derivative, then the third derivative. The evidence also gives the Maclaurin formula and the sine expansion, including the note that “entire function” is not syllabus vocabulary.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA21-FAF-LO004` | find the Maclaurin series of a function, including the general term | Derive \(a_r=\frac{f^{(r)}(0)}{r!}\), then use it to form Maclaurin series. | CCEA spec map; DrFrost derivative-matching recap | Core | Differentiation, repeated derivatives, factorial notation |
| `FA21-FAF-LO005` | recognise and use the Maclaurin series for \(e^x\), \(\ln(1+x)\), \(\sin x\), \(\cos x\) and \((1+x)^n\), and be aware of the range of values of \(x\) for which they are valid | State, derive or use each standard expansion. Include range warnings. | CCEA spec map; DrFrost \(\sin x\) and \(\ln(1+x)\) discussion | Core | Exponentials, logarithms, trig, binomial expansion, series notation |
| `FA21-FAF-LO006` | derive the series expansions of simple compound functions | Substitute simple expressions into standard series and simplify carefully. | CCEA spec map | Core | Function composition, algebraic expansion, powers and brackets |
| `FA21-FAF-LO007` | demonstrate understanding of and use the standard small angle approximations \(\sin x\approx x\), \(\cos x\approx1-x^2/2\) and \(\tan x\approx x\), where \(x\) is in radians | Derive approximations from the first non-zero Maclaurin terms and use them in simple estimates. | CCEA spec map | Core | Radians, trig graphs, approximation language |

---

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Explain why a Maclaurin series is a power series centred at \(x=0\).
2. Derive the Maclaurin coefficient formula
   \[
   a_r=\frac{f^{(r)}(0)}{r!}.
   \]
3. Write and use
   \[
   f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots+\frac{f^{(r)}(0)}{r!}x^r+\cdots.
   \]
4. Recognise and use the standard Maclaurin series for
   \[
   e^x,\qquad \ln(1+x),\qquad \sin x,\qquad \cos x,\qquad (1+x)^n.
   \]
5. State and use the relevant ranges of validity.
6. Derive simple compound expansions by substitution and simplification.
7. Derive and use the small-angle approximations
   \[
   \sin x\approx x,\qquad
   \cos x\approx 1-\frac{x^2}{2},\qquad
   \tan x\approx x,
   \]
   where \(x\) is in radians.

## Bridge objectives

You should connect this lesson to ordinary A-Level Maths by recognising that:

1. A tangent approximation uses one derivative.
2. A Maclaurin polynomial uses many derivatives.
3. Factorials appear because repeated differentiation of powers creates products such as \(3\times2\times1\).
4. Radians are not decoration. They are required for the trig approximations.
5. The domain of \(\ln(1+x)\) controls the possible range of a series.

## Exam technique objectives

You should be able to:

1. Show enough derivative working for coefficient marks.
2. Use exact values rather than decimal approximations unless requested.
3. Keep factorials until simplification is safe.
4. State the range of validity when a standard series requires it.
5. Distinguish between an exact infinite series and a truncated approximation.
6. Label \(x\) in radians when using small-angle approximations.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You need to be comfortable with expanding brackets, collecting like powers of \(x\), substituting \(x=0\), working with exact fractions, recognising powers such as \(x^2\), \(x^3\), \(x^4\), and reading simple graphs.

## 5.2 Ordinary AS/A2 Mathematics foundations

You need differentiation:
\[
\frac{d}{dx}(x^n)=nx^{n-1}.
\]

You need higher derivatives:
\[
f'(x),\qquad f''(x),\qquad f'''(x),\qquad f^{(r)}(x).
\]

You need exact values:
\[
\sin0=0,
\qquad \cos0=1,
\qquad \tan0=0,
\qquad e^0=1,
\qquad \ln1=0.
\]

You need factorials:
\[
0!=1,
\quad 1!=1,
\quad 2!=2,
\quad 3!=6,
\quad 4!=24.
\]

You also need radian measure.

## 5.3 Previous Further Mathematics foundations

This lesson sits inside `FA21-FAF`, where series tools also include sums of powers and method of differences. Those are neighbouring ideas, not prerequisites for every Maclaurin calculation. The central prerequisite is fluency with repeated differentiation.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary AS differentiation | \(f'(x)\) gives the gradient of the curve. | The Maclaurin series uses \(f'(0)\), \(f''(0)\), \(f'''(0)\), and higher derivatives to build a polynomial. | A tangent line is only the first rung of the ladder. It does not contain enough information for a higher-order series. |
| Ordinary A2 differentiation | Product, quotient, chain and implicit differentiation. | Complicated Maclaurin questions may require repeated use of these rules to find several derivatives. | One algebra slip early on spreads through the whole series. |
| Ordinary trigonometry | Exact values, trig identities and radians. | The standard series for \(\sin x\), \(\cos x\) and \(\tan x\) become approximation engines near \(x=0\). | Small-angle approximations require radians. Degrees will sabotage the calculation quietly. |
| Ordinary exponentials and logarithms | \(e^x\), \(\ln x\), log laws and domains. | Further Maths uses \(e^x\) and \(\ln(1+x)\) as standard Maclaurin series. | \(\ln x\) is not defined at \(x=0\), so it cannot have a Maclaurin expansion about \(0\). |
| Ordinary binomial expansion | Expanding simple powers such as \((1+x)^2\), \((1+x)^3\). | Further Maths uses the general expansion of \((1+x)^n\), including non-integer powers. | For non-integer \(n\), the series is infinite and has a validity range. |
| Ordinary sequences and series | Summation notation and patterns in sequences. | Maclaurin series are infinite polynomial-like objects with terms arranged by powers of \(x\). | A finite truncation is an approximation, not automatically the whole function. |

In ordinary A-Level Maths, this idea appeared as using derivatives to describe local behaviour: value, gradient, curvature and rate of change.
In Further Maths, the same idea becomes a machine for replacing a function by a polynomial whose coefficients are chosen using derivatives at \(x=0\).
The key upgrade is that instead of matching just the tangent, we match as many derivatives as the question requires.
The danger is that old habits such as “just use the tangent” or “just substitute a decimal” become too blunt. Maclaurin work is exact, derivative-heavy and quietly fussy about notation.

---

# 6. Big Picture Explanation

A Maclaurin series is a way of turning a function into an infinite polynomial centred at \(x=0\).

That sounds like alchemy, but the mechanism is humble: make a polynomial and force it to agree with the original function at \(x=0\). First match the value. Then match the gradient. Then match the curvature. Then keep matching higher derivatives. Each derivative match tightens the approximation around \(x=0\), like focusing a mathematical lens.

Suppose we want a polynomial
\[
P(x)=a_0+a_1x+a_2x^2+a_3x^3+\cdots
\]
to imitate a function \(f(x)\) near \(x=0\).

At \(x=0\), all terms involving \(x\) disappear:
\[
P(0)=a_0.
\]
So if we want \(P(0)=f(0)\), we must choose
\[
a_0=f(0).
\]

Differentiate:
\[
P'(x)=a_1+2a_2x+3a_3x^2+4a_4x^3+\cdots.
\]
Again, at \(x=0\), most terms vanish:
\[
P'(0)=a_1.
\]
So if \(P'(0)=f'(0)\), choose
\[
a_1=f'(0).
\]

The same trick repeats. Each time we differentiate, the coefficient we want is exposed at \(x=0\), but multiplied by a factorial. That is why the Maclaurin formula is full of \(2!\), \(3!\), \(4!\), and so on.

For CCEA, this becomes a toolkit:

- find Maclaurin series;
- know the standard Maclaurin series;
- understand their ranges of validity;
- expand simple compound functions;
- use small-angle approximations.

---

# 7. Key Definitions and Notation

## 7.1 Power series

A **power series in \(x\)** is an expression of the form
\[
a_0+a_1x+a_2x^2+a_3x^3+\cdots+a_rx^r+\cdots,
\]
where \(a_0,a_1,a_2,a_3,\ldots\) are constants called **coefficients**.

## 7.2 Maclaurin series

The **Maclaurin series** of a function \(f(x)\) is the power series about \(x=0\):
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots+\frac{f^{(r)}(0)}{r!}x^r+\cdots.
\]

## 7.3 Factorial notation

For a positive integer \(r\),
\[
r!=r(r-1)(r-2)\cdots3\cdot2\cdot1.
\]
Also,
\[
0!=1.
\]
This is needed because the constant term may be viewed as
\[
\frac{f^{(0)}(0)}{0!}x^0=f(0).
\]

## 7.4 General coefficient

If
\[
f(x)=a_0+a_1x+a_2x^2+\cdots+a_rx^r+\cdots,
\]
then the Maclaurin coefficient of \(x^r\) is
\[
a_r=\frac{f^{(r)}(0)}{r!}.
\]

## 7.5 Standard Maclaurin series required by CCEA

### Exponential series

\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots+\frac{x^r}{r!}+\cdots.
\]
Valid for all real \(x\).

### Sine series

\[
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots.
\]
Valid for all real \(x\).

### Cosine series

\[
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots.
\]
Valid for all real \(x\).

### Logarithm series

\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\frac{x^5}{5}-\cdots.
\]
For CCEA purposes, record the standard range:
\[
-1<x\leq1.
\]

### Binomial series

\[
(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots.
\]
If \(n\) is a non-negative integer, the expansion terminates and is valid for all real \(x\).
If \(n\) is not a non-negative integer, the expansion is usually used with
\[
|x|<1,
\]
with endpoint behaviour depending on \(n\).

## 7.6 Small-angle approximations

For small \(x\), where \(x\) is measured in radians,
\[
\sin x\approx x,
\]
\[
\cos x\approx1-\frac{x^2}{2},
\]
\[
\tan x\approx x.
\]
The symbol \(\approx\) means “is approximately equal to”.

## 7.7 Truncation

An infinite Maclaurin series has infinitely many terms. In an exam, you are often asked to work “up to and including the term in \(x^3\)” or similar.
For example,
\[
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots.
\]
Up to and including the term in \(x^3\),
\[
\sin x\approx x-\frac{x^3}{3!}.
\]
This is a **truncated series**.

## 7.8 Boundary-only vocabulary: Taylor series

A **Taylor series about \(x=a\)** is a series centred at a value other than \(0\). The uploaded evidence explains that Taylor series let us shift the focus from \(0\) to another value \(a\). This lesson does not teach Taylor series as CCEA core content because the relevant CCEA LO boundary is Maclaurin. Taylor series are optional enrichment, not required content.

---

# 8. Core Theory

## 8.1 Deriving the Maclaurin formula by matching derivatives

Let
\[
P(x)=a_0+a_1x+a_2x^2+a_3x^3+a_4x^4+\cdots.
\]
We want \(P(x)\) to match \(f(x)\) as closely as possible near \(x=0\).

### Step 1: Match the function value

Substitute \(x=0\):
\[
P(0)=a_0+a_1(0)+a_2(0)^2+a_3(0)^3+a_4(0)^4+\cdots.
\]
Since every positive power of \(0\) is \(0\),
\[
P(0)=a_0.
\]
To match \(f(0)\), set
\[
P(0)=f(0),
\]
so
\[
a_0=f(0).
\]

**Bridge Note:** In ordinary A-Level Maths, substituting \(x=0\) simply found an intercept or a value. Here, substitution at \(0\) is used strategically because all powers of \(x\) disappear except the constant term.

### Step 2: Match the first derivative

Differentiate term by term:
\[
P'(x)=a_1+2a_2x+3a_3x^2+4a_4x^3+\cdots.
\]
Substitute \(x=0\):
\[
P'(0)=a_1.
\]
To match \(f'(0)\), set
\[
P'(0)=f'(0),
\]
so
\[
a_1=f'(0).
\]

**Bridge Note:** In ordinary A-Level Maths, \(f'(0)\) is the gradient of the curve at \(x=0\). Here, it becomes the coefficient of \(x\) in the Maclaurin series.

### Step 3: Match the second derivative

Differentiate again:
\[
P''(x)=2a_2+6a_3x+12a_4x^2+20a_5x^3+\cdots.
\]
Substitute \(x=0\):
\[
P''(0)=2a_2=2!a_2.
\]
To match \(f''(0)\), set
\[
2!a_2=f''(0).
\]
Therefore
\[
a_2=\frac{f''(0)}{2!}.
\]

**Bridge Note:** In ordinary A-Level Maths, the second derivative helped describe curvature or stationary-point type. Here, it becomes the coefficient of \(x^2\), after dividing by \(2!\).

### Step 4: Match the third derivative

Differentiate again:
\[
P'''(x)=6a_3+24a_4x+60a_5x^2+\cdots.
\]
Substitute \(x=0\):
\[
P'''(0)=6a_3=3!a_3.
\]
To match \(f'''(0)\), set
\[
3!a_3=f'''(0).
\]
Therefore
\[
a_3=\frac{f'''(0)}{3!}.
\]

### Step 5: General pattern

The pattern is
\[
a_0=f(0),
\]
\[
a_1=f'(0),
\]
\[
a_2=\frac{f''(0)}{2!},
\]
\[
a_3=\frac{f'''(0)}{3!}.
\]
In general,
\[
a_r=\frac{f^{(r)}(0)}{r!}.
\]
Therefore
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots+\frac{f^{(r)}(0)}{r!}x^r+\cdots.
\]

## 8.2 Deriving the Maclaurin series for \(\sin x\)

Let
\[
f(x)=\sin x.
\]
We need derivatives at \(x=0\):
\[
f(x)=\sin x,
\]
\[
f'(x)=\cos x,
\]
\[
f''(x)=-\sin x,
\]
\[
f'''(x)=-\cos x,
\]
\[
f^{(4)}(x)=\sin x,
\]
\[
f^{(5)}(x)=\cos x.
\]
Substitute \(x=0\):
\[
f(0)=0,
\quad f'(0)=1,
\quad f''(0)=0,
\quad f'''(0)=-1,
\quad f^{(4)}(0)=0,
\quad f^{(5)}(0)=1.
\]
Substitute into the Maclaurin formula:
\[
\sin x=0+1x+\frac{0}{2!}x^2+\frac{-1}{3!}x^3+\frac{0}{4!}x^4+\frac{1}{5!}x^5+\cdots.
\]
So
\[
\boxed{\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!}-\cdots.}
\]

**Bridge Note:** In ordinary A-Level Maths, you learned the derivative cycle
\[
\sin x\to\cos x\to-\sin x\to-\cos x\to\sin x.
\]
In Further Maths, that same cycle becomes the coefficient pattern of the whole series.

## 8.3 Deriving the Maclaurin series for \(\cos x\)

Let
\[
f(x)=\cos x.
\]
Then
\[
f(0)=\cos0=1.
\]
Differentiate:
\[
f'(x)=-\sin x,
\quad f'(0)=0.
\]
Differentiate again:
\[
f''(x)=-\cos x,
\quad f''(0)=-1.
\]
Differentiate again:
\[
f'''(x)=\sin x,
\quad f'''(0)=0.
\]
Differentiate again:
\[
f^{(4)}(x)=\cos x,
\quad f^{(4)}(0)=1.
\]
Substitute:
\[
\cos x=1+0x+\frac{-1}{2!}x^2+\frac{0}{3!}x^3+\frac{1}{4!}x^4+\cdots.
\]
Therefore
\[
\boxed{\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots.}
\]

**Bridge Note:** In ordinary A-Level Maths, \(\cos0=1\) and \(\sin0=0\) were exact trig values. Here, those exact values decide which powers survive in the series.

## 8.4 Standard Maclaurin Series and Range of Validity

The CCEA specification requires you to recognise and use the Maclaurin series for
\[
e^x,\qquad \ln(1+x),\qquad \sin x,\qquad \cos x,\qquad (1+x)^n,
\]
and to be aware of the range of values of \(x\) for which they are valid.

### 8.4.1 The Maclaurin series for \(e^x\)

Let
\[
f(x)=e^x.
\]
Differentiate repeatedly:
\[
f(x)=e^x,
\quad f'(x)=e^x,
\quad f''(x)=e^x,
\quad f'''(x)=e^x,
\]
and in general
\[
f^{(r)}(x)=e^x.
\]
Substitute \(x=0\):
\[
f^{(r)}(0)=e^0=1.
\]
Therefore
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots+\frac{x^r}{r!}+\cdots,
\]
or
\[
\boxed{e^x=\sum_{r=0}^{\infty}\frac{x^r}{r!}.}
\]
This is valid for all real \(x\).

**Bridge Note:** In ordinary A-Level Maths, \(e^x\) was special because it differentiates to itself. Here that same fact becomes a series where every derivative value at \(0\) is \(1\), so the only changing part is the factorial denominator.

### 8.4.2 The Maclaurin series for \(\ln(1+x)\)

Let
\[
f(x)=\ln(1+x).
\]
This is the correct logarithm for a Maclaurin expansion because
\[
f(0)=\ln(1+0)=\ln1=0.
\]
By contrast, \(\ln x\) itself cannot have a Maclaurin expansion about \(x=0\), because \(\ln0\) is not defined.

Differentiate:
\[
f'(x)=\frac{1}{1+x}=(1+x)^{-1},
\]
so
\[
f'(0)=1.
\]
Differentiate again:
\[
f''(x)=-(1+x)^{-2},
\quad f''(0)=-1.
\]
Differentiate again:
\[
f'''(x)=2(1+x)^{-3},
\quad f'''(0)=2=2!.
\]
Differentiate again:
\[
f^{(4)}(x)=-6(1+x)^{-4},
\quad f^{(4)}(0)=-6=-3!.
\]
Substitute into the Maclaurin formula:
\[
\ln(1+x)=0+1x+\frac{-1}{2!}x^2+\frac{2!}{3!}x^3+\frac{-3!}{4!}x^4+\cdots.
\]
Simplify:
\[
\boxed{\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\frac{x^5}{5}-\cdots.}
\]
The general term is
\[
\boxed{\ln(1+x)=\sum_{r=1}^{\infty}(-1)^{r+1}\frac{x^r}{r}.}
\]
For CCEA, record the range of validity as
\[
\boxed{-1<x\leq1.}
\]

**Bridge Note:** In ordinary A-Level Maths, logarithms came with domain restrictions. Here, that old domain instinct grows sharper: a series can have its own validity range, even when the original function exists beyond that interval.

### 8.4.3 The Maclaurin series for \((1+x)^n\)

Let
\[
f(x)=(1+x)^n.
\]
Then
\[
f(0)=1.
\]
Differentiate:
\[
f'(x)=n(1+x)^{n-1},
\quad f'(0)=n.
\]
Differentiate again:
\[
f''(x)=n(n-1)(1+x)^{n-2},
\quad f''(0)=n(n-1).
\]
Differentiate again:
\[
f'''(x)=n(n-1)(n-2)(1+x)^{n-3},
\quad f'''(0)=n(n-1)(n-2).
\]
In general,
\[
f^{(r)}(0)=n(n-1)(n-2)\cdots(n-r+1).
\]
Therefore
\[
\boxed{(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots.}
\]
The general term is
\[
\boxed{\frac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r.}
\]
Using binomial notation,
\[
\boxed{(1+x)^n=\sum_{r=0}^{\infty}\binom nr x^r,}
\]
where
\[
\binom nr=\frac{n(n-1)(n-2)\cdots(n-r+1)}{r!}.
\]

If \(n\) is a non-negative integer, the series terminates. If \(n\) is not a non-negative integer, the series is usually infinite, and the standard range is
\[
\boxed{|x|<1.}
\]

**Bridge Note:** In ordinary A-Level Maths, binomial expansion often meant finite algebra. In Further Maths, the same algebra becomes a potentially infinite series. The old habit “expand until it stops” is only safe when \(n\) is a non-negative integer.

### 8.4.4 Summary table of required standard series

| Function | Maclaurin series | Standard validity range |
|---|---|---|
| \(e^x\) | \(\displaystyle 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots+\frac{x^r}{r!}+\cdots\) | all real \(x\) |
| \(\sin x\) | \(\displaystyle x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots\) | all real \(x\) |
| \(\cos x\) | \(\displaystyle 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots\) | all real \(x\) |
| \(\ln(1+x)\) | \(\displaystyle x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots\) | \(-1<x\leq1\) |
| \((1+x)^n\) | \(\displaystyle 1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots\) | all real \(x\) if \(n\in\mathbb{Z}_{\geq0}\); usually \(|x|<1\) otherwise |

## 8.5 Finding a Maclaurin Series from Derivatives

For a function \(f(x)\):

1. Find \(f(0)\).
2. Find \(f'(x)\), then \(f'(0)\).
3. Find \(f''(x)\), then \(f''(0)\).
4. Continue until you have enough terms.
5. Substitute into
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots.
\]
6. Simplify carefully.

### Example 8.5.1: Find the Maclaurin series of \(f(x)=\frac{1}{1-x}\)

Find the Maclaurin series for
\[
f(x)=\frac{1}{1-x}
\]
up to and including \(x^4\).

Rewrite:
\[
f(x)=(1-x)^{-1}.
\]
Then
\[
f(0)=1.
\]
Using the chain rule:
\[
f'(x)=(1-x)^{-2},
\quad f'(0)=1.
\]
Differentiate again:
\[
f''(x)=2(1-x)^{-3},
\quad f''(0)=2.
\]
Differentiate again:
\[
f'''(x)=6(1-x)^{-4},
\quad f'''(0)=6.
\]
Differentiate again:
\[
f^{(4)}(x)=24(1-x)^{-5},
\quad f^{(4)}(0)=24.
\]
Substitute:
\[
\frac{1}{1-x}=1+1x+\frac{2}{2!}x^2+\frac{6}{3!}x^3+\frac{24}{4!}x^4+\cdots.
\]
Since
\[
\frac{2}{2!}=1,
\quad \frac{6}{3!}=1,
\quad \frac{24}{4!}=1,
\]
we get
\[
\boxed{\frac{1}{1-x}=1+x+x^2+x^3+x^4+\cdots.}
\]
The range of validity is
\[
\boxed{|x|<1.}
\]

### Example 8.5.2: Find the Maclaurin series of \(f(x)=\tan x\) up to \(x^3\)

Let
\[
f(x)=\tan x.
\]
Then
\[
f(0)=0.
\]
Differentiate:
\[
f'(x)=\sec^2x,
\quad f'(0)=1.
\]
Differentiate again:
\[
f''(x)=2\sec^2x\tan x,
\quad f''(0)=0.
\]
For the third derivative,
\[
f''(x)=2\sec^2x\tan x.
\]
Use the product rule:
\[
\frac{d}{dx}\left(\sec^2x\tan x\right)=\sec^2x\sec^2x+\tan x\cdot2\sec^2x\tan x.
\]
So
\[
f'''(x)=2\sec^4x+4\sec^2x\tan^2x.
\]
At \(x=0\), \(\sec0=1\) and \(\tan0=0\), so
\[
f'''(0)=2(1)^4+4(1)^2(0)^2=2.
\]
Substitute:
\[
\tan x=0+1x+\frac{0}{2!}x^2+\frac{2}{3!}x^3+\cdots.
\]
Since \(3!=6\),
\[
\boxed{\tan x=x+\frac{x^3}{3}+\cdots.}
\]
So
\[
\boxed{\tan x\approx x}
\]
for small \(x\), where \(x\) is in radians.

## 8.6 Using Standard Series to Expand Simple Compound Functions

`FA21-FAF-LO006` requires you to derive the series expansions of simple compound functions.

The key idea is substitution. If
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots,
\]
then replacing \(x\) by \(2x\) gives
\[
e^{2x}=1+2x+\frac{(2x)^2}{2!}+\frac{(2x)^3}{3!}+\cdots.
\]
The substitution is simple, but the simplification is where the gremlins keep their teacups. Powers must apply to the whole substituted expression.

### 8.6.1 Example: Expand \(e^{3x}\) up to \(x^3\)

Use
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.
\]
Replace \(x\) by \(3x\):
\[
e^{3x}=1+(3x)+\frac{(3x)^2}{2!}+\frac{(3x)^3}{3!}+\cdots.
\]
Simplify:
\[
(3x)^2=9x^2,
\quad 2!=2,
\]
so
\[
\frac{(3x)^2}{2!}=\frac{9x^2}{2}.
\]
Also,
\[
(3x)^3=27x^3,
\quad 3!=6,
\]
so
\[
\frac{(3x)^3}{3!}=\frac{27x^3}{6}=\frac{9x^3}{2}.
\]
Therefore
\[
\boxed{e^{3x}=1+3x+\frac{9x^2}{2}+\frac{9x^3}{2}+\cdots.}
\]

**Bridge Note:** In ordinary A-Level Maths, substituting \(3x\) into a function was composition. Here, the same composition must be applied to every power in the infinite series.

### 8.6.2 Example: Expand \(\sin(2x)\) up to \(x^5\)

Use
\[
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots.
\]
Replace \(x\) by \(2x\):
\[
\sin(2x)=2x-\frac{(2x)^3}{3!}+\frac{(2x)^5}{5!}-\cdots.
\]
Now
\[
(2x)^3=8x^3,
\quad 3!=6,
\]
so
\[
-\frac{(2x)^3}{3!}=-\frac{8x^3}{6}=-\frac{4x^3}{3}.
\]
Also,
\[
(2x)^5=32x^5,
\quad 5!=120,
\]
so
\[
\frac{(2x)^5}{5!}=\frac{32x^5}{120}=\frac{4x^5}{15}.
\]
Therefore
\[
\boxed{\sin(2x)=2x-\frac{4x^3}{3}+\frac{4x^5}{15}-\cdots.}
\]

### 8.6.3 Example: Expand \(\ln(1-2x)\) up to \(x^4\)

Use
\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots.
\]
Replace \(x\) by \(-2x\):
\[
\ln(1-2x)=(-2x)-\frac{(-2x)^2}{2}+\frac{(-2x)^3}{3}-\frac{(-2x)^4}{4}+\cdots.
\]
Simplify:
\[
\boxed{\ln(1-2x)=-2x-2x^2-\frac{8x^3}{3}-4x^4+\cdots.}
\]

For the range, the standard series is valid for
\[
-1<u\leq1.
\]
Here \(u=-2x\), so
\[
-1<-2x\leq1.
\]
Solving carefully:
\[
-1<-2x \quad\Rightarrow\quad x<\frac12,
\]
and
\[
-2x\leq1 \quad\Rightarrow\quad x\geq-\frac12.
\]
Therefore
\[
\boxed{-\frac12\leq x<\frac12.}
\]

### 8.6.4 Example: Expand \((1+4x)^{-1/2}\) up to \(x^3\)

Use the binomial series with \(n=-\frac12\) and replace \(x\) by \(4x\):
\[
(1+4x)^{-1/2}=1+\left(-\frac12\right)(4x)+\frac{\left(-\frac12\right)\left(-\frac32\right)}{2!}(4x)^2+\frac{\left(-\frac12\right)\left(-\frac32\right)\left(-\frac52\right)}{3!}(4x)^3+\cdots.
\]
The first-order term is
\[
-2x.
\]
The second-order coefficient is
\[
\frac{\left(-\frac12\right)\left(-\frac32\right)}{2!}=\frac{3/4}{2}=\frac38.
\]
Since \((4x)^2=16x^2\), the \(x^2\) term is
\[
\frac38\cdot16x^2=6x^2.
\]
The third-order coefficient is
\[
\frac{\left(-\frac12\right)\left(-\frac32\right)\left(-\frac52\right)}{3!}=\frac{-15/8}{6}=-\frac{5}{16}.
\]
Since \((4x)^3=64x^3\), the \(x^3\) term is
\[
-\frac{5}{16}\cdot64x^3=-20x^3.
\]
Therefore
\[
\boxed{(1+4x)^{-1/2}=1-2x+6x^2-20x^3+\cdots.}
\]
The range is
\[
|4x|<1,
\]
so
\[
\boxed{|x|<\frac14.}
\]

## 8.7 Combining Series

Sometimes a question asks for the expansion of an expression made from several functions, for example \(e^x\cos x\) or \(\frac{\ln(1+x)}{x}\). Expand each part only as far as needed, then multiply, divide or simplify.

### 8.7.1 Example: Expand \(e^x\cos x\) up to \(x^3\)

We need
\[
e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots,
\]
and, up to \(x^3\),
\[
\cos x=1-\frac{x^2}{2}+\cdots.
\]
Multiply:
\[
e^x\cos x=\left(1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots\right)\left(1-\frac{x^2}{2}+\cdots\right).
\]
Keep terms up to \(x^3\):
\[
1\left(1-\frac{x^2}{2}\right)=1-\frac{x^2}{2},
\]
\[
x\left(1-\frac{x^2}{2}\right)=x-\frac{x^3}{2},
\]
\[
\frac{x^2}{2}\left(1-\frac{x^2}{2}\right)=\frac{x^2}{2}+\text{terms beyond }x^3,
\]
\[
\frac{x^3}{6}\left(1-\frac{x^2}{2}\right)=\frac{x^3}{6}+\text{terms beyond }x^3.
\]
Collect:
\[
e^x\cos x=1+x+\left(-\frac{x^2}{2}+\frac{x^2}{2}\right)+\left(-\frac{x^3}{2}+\frac{x^3}{6}\right)+\cdots.
\]
The \(x^2\) terms cancel, and
\[
-\frac{x^3}{2}+\frac{x^3}{6}=-\frac{x^3}{3}.
\]
Therefore
\[
\boxed{e^x\cos x=1+x-\frac{x^3}{3}+\cdots.}
\]

### 8.7.2 Example: Expand \(\dfrac{\ln(1+x)}{x}\) up to \(x^3\)

Start with
\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots.
\]
Divide every term by \(x\):
\[
\frac{\ln(1+x)}{x}=\frac{x}{x}-\frac{x^2}{2x}+\frac{x^3}{3x}-\frac{x^4}{4x}+\cdots.
\]
Therefore
\[
\boxed{\frac{\ln(1+x)}{x}=1-\frac{x}{2}+\frac{x^2}{3}-\frac{x^3}{4}+\cdots.}
\]
The validity comes from \(\ln(1+x)\):
\[
\boxed{-1<x\leq1.}
\]

## 8.8 Small-Angle Approximations

`FA21-FAF-LO007` requires:
\[
\sin x\approx x,
\]
\[
\cos x\approx1-\frac{x^2}{2},
\]
\[
\tan x\approx x,
\]
where \(x\) is in radians.

### 8.8.1 Deriving \(\sin x\approx x\)

The Maclaurin series is
\[
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots.
\]
For small \(x\), powers such as \(x^3\), \(x^5\), \(x^7\) are much smaller than \(x\). So
\[
\boxed{\sin x\approx x.}
\]
A slightly better approximation is
\[
\boxed{\sin x\approx x-\frac{x^3}{6}.}
\]

### 8.8.2 Deriving \(\cos x\approx1-\frac{x^2}{2}\)

The Maclaurin series is
\[
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots.
\]
For small \(x\), keep the first two non-zero terms:
\[
\boxed{\cos x\approx1-\frac{x^2}{2}.}
\]

### 8.8.3 Deriving \(\tan x\approx x\)

We derived
\[
\tan x=x+\frac{x^3}{3}+\cdots.
\]
For small \(x\),
\[
\boxed{\tan x\approx x.}
\]
Alternatively,
\[
\tan x=\frac{\sin x}{\cos x}\approx\frac{x}{1}=x.
\]

### 8.8.4 Why radians are required

In radians,
\[
\frac{d}{dx}\sin x=\cos x,
\]
and
\[
\frac{d}{dx}\cos x=-\sin x.
\]
These derivative facts build the Maclaurin series. If \(x\) is measured in degrees, these derivative formulae acquire extra conversion factors, so \(\sin x\approx x\) and \(\tan x\approx x\) do not work with \(x\) in degrees.

For example,
\[
5^\circ=\frac{5\pi}{180}=\frac{\pi}{36},
\]
so
\[
\sin5^\circ\approx\frac{\pi}{36},
\]
not \(5\).

### 8.8.5 Example: Approximate \(\sin0.04\)

Use
\[
\sin x\approx x-\frac{x^3}{6}.
\]
With \(x=0.04\),
\[
\sin0.04\approx0.04-\frac{(0.04)^3}{6}.
\]
Now
\[
(0.04)^2=0.0016,
\]
\[
(0.04)^3=0.000064.
\]
Therefore
\[
\sin0.04\approx0.04-\frac{0.000064}{6}=0.039989333\ldots.
\]
So
\[
\boxed{\sin0.04\approx0.0399893.}
\]

### 8.8.6 Example: Approximate \(1-\cos0.1\)

Use
\[
\cos x\approx1-\frac{x^2}{2}.
\]
Then
\[
1-\cos x\approx1-\left(1-\frac{x^2}{2}\right)=\frac{x^2}{2}.
\]
For \(x=0.1\),
\[
1-\cos0.1\approx\frac{(0.1)^2}{2}=\frac{0.01}{2}=0.005.
\]
Therefore
\[
\boxed{1-\cos0.1\approx0.005.}
\]

## 8.9 General Terms

`FA21-FAF-LO004` includes finding the Maclaurin series of a function including the general term.

### 8.9.1 General term for \(e^x\)

\[
\boxed{e^x=\sum_{r=0}^{\infty}\frac{x^r}{r!}.}
\]

### 8.9.2 General term for \(\sin x\)

Only odd powers appear:
\[
x^{2r+1},\qquad r=0,1,2,\ldots.
\]
The signs alternate with \((-1)^r\), so
\[
\boxed{\sin x=\sum_{r=0}^{\infty}(-1)^r\frac{x^{2r+1}}{(2r+1)!}.}
\]

### 8.9.3 General term for \(\cos x\)

Only even powers appear:
\[
x^{2r},\qquad r=0,1,2,\ldots.
\]
The signs alternate with \((-1)^r\), so
\[
\boxed{\cos x=\sum_{r=0}^{\infty}(-1)^r\frac{x^{2r}}{(2r)!}.}
\]

### 8.9.4 General term for \(\ln(1+x)\)

The powers are \(x^1,x^2,x^3,\ldots\), the denominator matches the power, and the signs alternate:
\[
\boxed{\ln(1+x)=\sum_{r=1}^{\infty}(-1)^{r+1}\frac{x^r}{r}.}
\]

### 8.9.5 General term for \((1+x)^n\)

\[
\boxed{(1+x)^n=\sum_{r=0}^{\infty}\binom nr x^r,}
\]
where
\[
\boxed{\binom nr=\frac{n(n-1)(n-2)\cdots(n-r+1)}{r!}.}
\]

## 8.10 Equality, Approximation and Omitted Terms

There are two different ideas:

1. An **infinite series** may equal the function inside its range of validity.
2. A **truncated series** approximates the function.

For example,
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
\]
is an infinite series. But
\[
e^x\approx1+x+\frac{x^2}{2}
\]
is a truncated approximation.

If you include ellipses,
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots,
\]
you indicate that the infinite series continues.
If you stop after a term without ellipses, write an approximation:
\[
e^x\approx1+x+\frac{x^2}{2!}.
\]
Big-\(O\) notation is not necessary for this lesson unless a question uses it.

## 8.11 CCEA Boundary Note: Maclaurin versus Taylor

The uploaded chapter is titled **Taylor Series**, and the slides show Taylor expansions about \(x=a\), including formulae such as
\[
f(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots.
\]
For this CCEA lesson, Taylor expansions about arbitrary \(a\) are **not core**, because the identified CCEA LO set is specifically about Maclaurin series.

It is useful to know the relationship:
\[
\text{Maclaurin series}=\text{Taylor series centred at }0.
\]
So the Maclaurin series is the special case \(a=0\). This lesson therefore teaches
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots
\]
as core CCEA content. Taylor series about \(x=a\) are optional enrichment, not required CCEA content.

---

# 9. Visual Asset Integration

The following placeholders are inserted for planned assets.

## 9.1 Mermaid learning path

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesMermaid-001 | Source: CCEA `FA21-FAF` LO map + lesson boundary | Insert from mermaid/FA21MaclaurinSeriesMermaid-001.md | Purpose: Show the learning route from ordinary derivatives to Maclaurin coefficients, standard series, compound expansions and small-angle approximations. The diagram must show the chain `derivatives at x=0 → coefficients → standard series → substitutions → approximations`, with `FA21-FAF-LO004` to `FA21-FAF-LO007` attached to the relevant nodes.]

## 9.2 SVG graph of \(\sin x\) and successive Maclaurin approximations

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesSVG-001 | Source: DrFrost/Pearson Maclaurin recap graph and CCEA Maclaurin LO boundary | Insert from svg/FA21MaclaurinSeriesSVG-001.svg | Purpose: Show \(y=\sin x\) and the successive approximations \(y=x\), \(y=x-\frac{x^3}{3!}\), \(y=x-\frac{x^3}{3!}+\frac{x^5}{5!}\), highlighting that the approximations match best near \(x=0\). The visual must preserve the evidence idea of successive curves matching more derivatives near \(x=0\).]

## 9.3 SVG derivative-matching coefficient visual

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesSVG-002 | Source: DrFrost/Pearson derivative-matching slides | Insert from svg/FA21MaclaurinSeriesSVG-002.svg | Purpose: Show how substituting \(x=0\) into \(P(x)\), \(P'(x)\), \(P''(x)\), \(P'''(x)\) exposes \(a_0\), \(a_1\), \(2!a_2\), \(3!a_3\). The visual must include the equations \(P(0)=a_0\), \(P'(0)=a_1\), \(P''(0)=2!a_2\), \(P'''(0)=3!a_3\), leading to \(a_r=\frac{f^{(r)}(0)}{r!}\).]

## 9.4 Bridge SVG: tangent line versus Maclaurin polynomial

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA21MaclaurinSeriesBridgeSVG-001.svg | Purpose: Compare ordinary A-Level tangent-line approximation with Further Maths Maclaurin polynomial approximation. The visual must show a curve near \(x=0\), a tangent line matching value and gradient, and a higher-order polynomial matching value, gradient and curvature.]

## 9.5 TikZ precise graph sketch

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesTikZ-001 | Source: CCEA Maclaurin LO + DrFrost/Pearson graph idea | Insert from tikz/FA21MaclaurinSeriesTikZ-001.tex | Purpose: Provide a precise mathematical graph sketch of \(y=\sin x\), \(y=x\), \(y=x-\frac{x^3}{3!}\), and \(y=x-\frac{x^3}{3!}+\frac{x^5}{5!}\). The graph must include axes, origin label, and a highlighted neighbourhood around \(x=0\).]

## 9.6 Optional enrichment SVG: Maclaurin versus Taylor centre

[VISUAL PLACEHOLDER: FA21MaclaurinSeriesEnrichmentSVG-001 | Source: Cross-board Taylor evidence from uploaded DrFrost/Pearson chapter | Insert from svg/FA21MaclaurinSeriesEnrichmentSVG-001.svg | Purpose: Optional enrichment only. Compare a Maclaurin approximation centred at \(0\) with a Taylor approximation centred at \(a\), using the evidence idea that Taylor series shift the focus of the function to other values of \(x\). This visual must be clearly labelled as not required by CCEA core for this lesson.]

---

# 10. Interactive Learning Widgets

## 10.1 Widget 001: Maclaurin coefficient builder

[INTERACTIVE PLACEHOLDER: FA21MaclaurinSeriesWidget-001 | Source: AI-proposed teaching enhancement based on CCEA `FA21-FAF-LO004` and derivative-matching evidence | Insert from widgets/FA21MaclaurinSeriesWidget-001.html | Purpose: Help students build a Maclaurin polynomial from derivative values at \(x=0\).]

The student inputs:
\[
f(0),\quad f'(0),\quad f''(0),\quad f'''(0),\quad f^{(4)}(0).
\]
The widget displays:
\[
f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\frac{f^{(4)}(0)}{4!}x^4.
\]
It reinforces derivative values at \(0\), factorial denominators, coefficient calculation and exact fractions. It checks errors such as forgetting \(2!\), putting \(f''(0)\) directly as the coefficient of \(x^2\), using \(3\) instead of \(3!=6\), and missing zero derivative terms.

## 10.2 Widget 002: Standard-series selector and range checker

[INTERACTIVE PLACEHOLDER: FA21MaclaurinSeriesWidget-002 | Source: AI-proposed teaching enhancement based on CCEA `FA21-FAF-LO005` | Insert from widgets/FA21MaclaurinSeriesWidget-002.html | Purpose: Let students choose a standard function and see its Maclaurin series, general term and validity range.]

The student selects one of
\[
e^x,\qquad \sin x,\qquad \cos x,\qquad \ln(1+x),\qquad (1+x)^n.
\]
The widget displays the standard expansion, the general term where suitable, the validity range, and a warning if a proposed \(x\)-value is outside the range.

## 10.3 Widget 003: Small-angle approximation checker

[INTERACTIVE PLACEHOLDER: FA21MaclaurinSeriesWidget-003 | Source: AI-proposed teaching enhancement based on CCEA `FA21-FAF-LO007` | Insert from widgets/FA21MaclaurinSeriesWidget-003.html | Purpose: Let students enter a small angle and compare \(\sin x\), \(\cos x\), \(\tan x\) with their small-angle approximations.]

The student inputs a value of \(x\) and whether it is in radians or degrees. The widget displays
\[
\sin x\approx x,
\]
\[
\cos x\approx1-\frac{x^2}{2},
\]
\[
\tan x\approx x.
\]
It reinforces radians, approximation size and the difference between first-term and higher-term approximations.

---

# 11. Worked Examples

## 11.1 Evidence-backed worked example: Derive the Maclaurin series for \(\sin x\)

| Required item | Details |
|---|---|
| Evidence source | DrFrost/Pearson recap slides and transcript |
| On-spec status | Core CCEA content for `FA21-FAF-LO004` and `FA21-FAF-LO005` |
| Ordinary Maths idea used | Repeated differentiation of \(\sin x\) |
| Further Maths upgrade | Use derivative values at \(x=0\) to build a whole power series |
| Question | Find the Maclaurin series for \(\sin x\), including the pattern of the terms. |

Let
\[
f(x)=\sin x.
\]
The Maclaurin formula is
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\frac{f^{(4)}(0)}{4!}x^4+\frac{f^{(5)}(0)}{5!}x^5+\cdots.
\]
Differentiate:
\[
f'(x)=\cos x,
\]
\[
f''(x)=-\sin x,
\]
\[
f'''(x)=-\cos x,
\]
\[
f^{(4)}(x)=\sin x,
\]
\[
f^{(5)}(x)=\cos x,
\]
\[
f^{(6)}(x)=-\sin x,
\]
\[
f^{(7)}(x)=-\cos x.
\]
At \(x=0\),
\[
f(0)=0,
\quad f'(0)=1,
\quad f''(0)=0,
\quad f'''(0)=-1,
\quad f^{(4)}(0)=0,
\quad f^{(5)}(0)=1,
\quad f^{(6)}(0)=0,
\quad f^{(7)}(0)=-1.
\]
Substitute:
\[
\sin x=0+1x+\frac{0}{2!}x^2+\frac{-1}{3!}x^3+\frac{0}{4!}x^4+\frac{1}{5!}x^5+\frac{0}{6!}x^6+\frac{-1}{7!}x^7+\cdots.
\]
Simplify:
\[
\boxed{\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots.}
\]
Using general-term notation,
\[
\boxed{\sin x=\sum_{r=0}^{\infty}(-1)^r\frac{x^{2r+1}}{(2r+1)!}.}
\]

### Teaching note

Only odd powers appear because all even derivatives of \(\sin x\) evaluate to \(0\) at \(x=0\). The signs alternate because the non-zero derivative values cycle through \(1,-1,1,-1,\ldots\) for the odd derivatives.

## 11.2 Generated on-spec worked example: Derive the Maclaurin series for \(e^{-2x}\)

Expand \(e^{-2x}\) up to and including the term in \(x^4\).

The standard series is
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots.
\]
Replace \(x\) by \(-2x\):
\[
e^{-2x}=1+(-2x)+\frac{(-2x)^2}{2!}+\frac{(-2x)^3}{3!}+\frac{(-2x)^4}{4!}+\cdots.
\]
Simplify term by term:
\[
(-2x)^2=4x^2,
\quad \frac{4x^2}{2!}=2x^2,
\]
\[
(-2x)^3=-8x^3,
\quad \frac{-8x^3}{3!}=-\frac{8x^3}{6}=-\frac{4x^3}{3},
\]
\[
(-2x)^4=16x^4,
\quad \frac{16x^4}{4!}=\frac{16x^4}{24}=\frac{2x^4}{3}.
\]
Therefore
\[
\boxed{e^{-2x}=1-2x+2x^2-\frac{4x^3}{3}+\frac{2x^4}{3}+\cdots.}
\]
Valid for all real \(x\).

## 11.3 Generated on-spec worked example: Expand \(\ln(1+3x)\) and state the range

The standard series is
\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots,
\]
valid for
\[
-1<x\leq1.
\]
Replace \(x\) by \(3x\):
\[
\ln(1+3x)=3x-\frac{(3x)^2}{2}+\frac{(3x)^3}{3}-\frac{(3x)^4}{4}+\cdots.
\]
Simplify:
\[
\boxed{\ln(1+3x)=3x-\frac{9x^2}{2}+9x^3-\frac{81x^4}{4}+\cdots.}
\]
For the range, set \(u=3x\):
\[
-1<3x\leq1.
\]
Divide by \(3\):
\[
\boxed{-\frac13<x\leq\frac13.}
\]

## 11.4 Generated on-spec worked example: Binomial expansion of \((1-3x)^{1/2}\)

Use
\[
(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots.
\]
For \((1-3x)^{1/2}\), take \(n=\frac12\) and replace \(x\) by \(-3x\):
\[
(1-3x)^{1/2}=1+\left(\frac12\right)(-3x)+\frac{\left(\frac12\right)\left(-\frac12\right)}{2!}(-3x)^2+\frac{\left(\frac12\right)\left(-\frac12\right)\left(-\frac32\right)}{3!}(-3x)^3+\cdots.
\]
Simplify:
\[
\left(\frac12\right)(-3x)=-\frac{3x}{2},
\]
\[
\frac{\left(\frac12\right)\left(-\frac12\right)}{2!}=-\frac18,
\quad -\frac18(9x^2)=-\frac{9x^2}{8},
\]
\[
\frac{\left(\frac12\right)\left(-\frac12\right)\left(-\frac32\right)}{3!}=\frac{1}{16},
\quad \frac{1}{16}(-27x^3)=-\frac{27x^3}{16}.
\]
Therefore
\[
\boxed{(1-3x)^{1/2}=1-\frac{3x}{2}-\frac{9x^2}{8}-\frac{27x^3}{16}+\cdots.}
\]
The range is
\[
|-3x|<1,
\]
so
\[
\boxed{|x|<\frac13.}
\]

## 11.5 Generated on-spec worked example: Multiply two standard series

Find the expansion of \(e^x\sin x\) up to and including the term in \(x^4\).

Use
\[
e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots,
\]
and
\[
\sin x=x-\frac{x^3}{6}+\cdots.
\]
Then
\[
e^x\sin x=\left(1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots\right)\left(x-\frac{x^3}{6}+\cdots\right).
\]
Keep terms up to \(x^4\):
\[
1\left(x-\frac{x^3}{6}\right)=x-\frac{x^3}{6},
\]
\[
x\left(x-\frac{x^3}{6}\right)=x^2-\frac{x^4}{6},
\]
\[
\frac{x^2}{2}\left(x-\frac{x^3}{6}\right)=\frac{x^3}{2}+\text{terms beyond }x^4,
\]
\[
\frac{x^3}{6}\left(x-\frac{x^3}{6}\right)=\frac{x^4}{6}+\text{terms beyond }x^4.
\]
Collect:
\[
e^x\sin x=x+x^2+\left(-\frac{x^3}{6}+\frac{x^3}{2}\right)+\left(-\frac{x^4}{6}+\frac{x^4}{6}\right)+\cdots.
\]
So
\[
\boxed{e^x\sin x=x+x^2+\frac{x^3}{3}+0x^4+\cdots.}
\]
Usually this is written
\[
\boxed{e^x\sin x=x+x^2+\frac{x^3}{3}+\cdots.}
\]

## 11.6 Generated on-spec worked example: Small-angle approximation

For small \(x\), simplify
\[
\frac{\sin3x}{\tan2x}.
\]
For small \(x\) in radians,
\[
\sin u\approx u,
\qquad \tan u\approx u.
\]
Therefore
\[
\sin3x\approx3x,
\]
and
\[
\tan2x\approx2x.
\]
Thus
\[
\frac{\sin3x}{\tan2x}\approx\frac{3x}{2x}=\frac32.
\]
So
\[
\boxed{\frac{\sin3x}{\tan2x}\approx\frac32.}
\]

## 11.7 Evidence found but excluded from core worked examples

The uploaded evidence includes substantial Taylor-series examples, such as expanding \(e^x\) in powers of \((x-4)\), expressing \(\tan(x+\frac{\pi}{4})\) in powers of \(x\), using Taylor or Maclaurin series for limits, and using Taylor methods for differential-equation series solutions.

They are **not taught as CCEA core examples in this lesson** because the identified CCEA `FA21-FAF` lesson boundary is Maclaurin series, recognised standard Maclaurin expansions, simple compound expansions and small-angle approximations. Taylor expansions about arbitrary \(x=a\), limits using series and differential-equation series solutions remain boundary-risk or optional enrichment content.

---

# 12. Common Mistakes and Exam Traps

## 12.1 Forgetting that Maclaurin means centred at \(x=0\)

A Maclaurin series uses derivative values at \(0\):
\[
f(0),\quad f'(0),\quad f''(0),\quad f'''(0),\ldots
\]
So the formula is
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots.
\]
A Taylor series about \(x=a\) uses derivative values at \(a\). That is not this CCEA core lesson.

## 12.2 Forgetting factorial denominators

The coefficient of \(x^r\) is not usually \(f^{(r)}(0)\). It is
\[
\frac{f^{(r)}(0)}{r!}.
\]
If \(f'''(0)=12\), then the \(x^3\) term is
\[
\frac{12}{3!}x^3=\frac{12}{6}x^3=2x^3.
\]

## 12.3 Treating \(3!\) as \(3\)

Remember:
\[
3!=3\cdot2\cdot1=6,
\]
\[
4!=4\cdot3\cdot2\cdot1=24,
\]
\[
5!=5\cdot4\cdot3\cdot2\cdot1=120.
\]
So
\[
\frac{x^3}{3!}=\frac{x^3}{6},
\]
not \(\frac{x^3}{3}\).

## 12.4 Losing brackets in compound functions

If
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots,
\]
then
\[
e^{3x}=1+3x+\frac{(3x)^2}{2!}+\frac{(3x)^3}{3!}+\cdots.
\]
Always substitute the whole expression:
\[
(3x)^r=3^rx^r.
\]

## 12.5 Getting signs wrong in \(\ln(1+x)\)

The standard series is
\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots.
\]
The signs alternate. The positive-sign series
\[
x+\frac{x^2}{2}+\frac{x^3}{3}+\cdots
\]
belongs to \(-\ln(1-x)\), not \(\ln(1+x)\).

## 12.6 Forgetting range of validity

\[
e^x,
\quad \sin x,
\quad \cos x
\]
are valid for all real \(x\).

\[
\ln(1+x)
\]
is valid for
\[
-1<x\leq1.
\]
For non-terminating binomial expansions,
\[
(1+x)^n
\]
usually requires
\[
|x|<1.
\]

For \(\ln(1+4x)\), do not write the range as \(-1<x\leq1\). Let \(u=4x\), so
\[
-1<4x\leq1,
\]
which gives
\[
-\frac14<x\leq\frac14.
\]

## 12.7 Reversing inequalities incorrectly

When dividing an inequality by a negative number, reverse the inequality sign. For \(\ln(1-2x)\), the substitution is \(u=-2x\). The validity condition is
\[
-1<-2x\leq1.
\]
Solving gives
\[
-\frac12\leq x<\frac12.
\]

## 12.8 Using degrees in small-angle approximations

The small-angle approximations require radians:
\[
\sin x\approx x,
\quad \cos x\approx1-\frac{x^2}{2},
\quad \tan x\approx x.
\]
For example,
\[
\sin5^\circ\approx\frac{\pi}{36},
\]
not \(5\).

## 12.9 Confusing exact infinite series with truncated approximations

The infinite series
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
\]
is exact within its range. The finite expression
\[
1+x+\frac{x^2}{2}
\]
is only a truncation, so write
\[
e^x\approx1+x+\frac{x^2}{2}
\]
or
\[
e^x=1+x+\frac{x^2}{2}+\cdots.
\]

## 12.10 Expanding \(\ln x\) as a Maclaurin series

A Maclaurin series is centred at \(x=0\), so it needs \(f(0)\). For \(f(x)=\ln x\), this would need \(\ln0\), which is undefined. Use \(\ln(1+x)\) when the standard Maclaurin series is required.

## 12.11 Treating off-spec Taylor material as CCEA core

The uploaded evidence contains a full Taylor-series chapter. It is mathematically useful, but this lesson’s CCEA boundary is Maclaurin-focused. For this lesson, core CCEA content is Maclaurin series centred at \(0\). Taylor expansions about \(x=a\) are optional enrichment unless a CCEA topic boundary explicitly requires them.

---

# 13. Practice Questions

These questions are **AI-generated on-spec practice questions**. They are not past-paper questions and are not textbook questions.

## 13.1 Basic fluency questions

### Question 1: Coefficients from derivatives

A function \(f\) has
\[
f(0)=3,
\qquad f'(0)=-2,
\qquad f''(0)=10,
\qquad f'''(0)=-24.
\]
Write the Maclaurin expansion of \(f(x)\) up to and including the term in \(x^3\).

### Question 2: Derive \(e^x\)

Use the Maclaurin formula to show that
\[
e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots.
\]
State the general term.

### Question 3: Recognise the standard series

Write down the Maclaurin series for each of the following, giving terms up to and including the first non-zero term after \(x^3\), where applicable.

1. \(\sin x\)
2. \(\cos x\)
3. \(\ln(1+x)\)
4. \((1+x)^n\)

For \(\ln(1+x)\), state the standard range of validity.

## 13.2 Bridge questions

### Question 4: Tangent line versus Maclaurin polynomial

For
\[
f(x)=\cos x,
\]
find:

1. the tangent-line approximation at \(x=0\);
2. the Maclaurin expansion up to and including the term in \(x^4\).

Explain why the Maclaurin polynomial contains more local information than the tangent line.

### Question 5: Degree trap

Use a small-angle approximation to estimate
\[
\sin3^\circ.
\]
Give your answer exactly in terms of \(\pi\).

## 13.3 Standard exam-style questions

### Question 6: Compound exponential

Find the expansion of
\[
e^{4x}
\]
up to and including the term in \(x^4\).

### Question 7: Compound logarithm and range

Find the expansion of
\[
\ln(1-5x)
\]
up to and including the term in \(x^4\). State the range of validity.

### Question 8: Binomial expansion and range

Find the expansion of
\[
(1+2x)^{-3/2}
\]
up to and including the term in \(x^3\). State the range of validity.

### Question 9: Product of standard series

Find the expansion of
\[
e^{2x}\cos x
\]
up to and including the term in \(x^3\).

### Question 10: Small-angle simplification

For small \(x\), where \(x\) is in radians, simplify
\[
\frac{1-
\cos2x}{x^2}.
\]
Use the standard small-angle approximation for \(\cos x\).

## 13.4 Harder synthesis questions

### Question 11: Mixed standard series

Find the expansion of
\[
e^x\ln(1+x)
\]
up to and including the term in \(x^4\). State the range of validity inherited from the logarithm series.

### Question 12: General term and substitution

Using the standard series for \(\sin x\), write down a general term for the Maclaurin series of
\[
\sin(3x).
\]
Then write the expansion up to and including the term in \(x^7\).

---

# 14. Worked Solutions

These are **generated practice solutions** for the AI-generated questions in Section 13. They are not past-paper solutions and are not textbook solutions.

## 14.1 Solution to Question 1: Coefficients from derivatives

The Maclaurin formula is
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots.
\]
Substitute:
\[
f(x)=3+(-2)x+\frac{10}{2!}x^2+\frac{-24}{3!}x^3+\cdots.
\]
Since \(2!=2\) and \(3!=6\),
\[
\frac{10}{2!}x^2=5x^2,
\]
and
\[
\frac{-24}{3!}x^3=-4x^3.
\]
Therefore
\[
\boxed{f(x)=3-2x+5x^2-4x^3+\cdots.}
\]

## 14.2 Solution to Question 2: Derive \(e^x\)

Let \(f(x)=e^x\). Then
\[
f^{(r)}(x)=e^x
\]
for every non-negative integer \(r\), so
\[
f^{(r)}(0)=e^0=1.
\]
The Maclaurin formula gives
\[
e^x=1+1x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+\frac{1}{4!}x^4+\cdots.
\]
Thus
\[
\boxed{e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots.}
\]
The general term is
\[
\boxed{\frac{x^r}{r!}},
\]
so
\[
\boxed{e^x=\sum_{r=0}^{\infty}\frac{x^r}{r!}.}
\]

## 14.3 Solution to Question 3: Recognise the standard series

\[
\boxed{\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots}
\]

\[
\boxed{\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+\cdots}
\]

\[
\boxed{\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots,
\qquad -1<x\leq1.}
\]

\[
\boxed{(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\frac{n(n-1)(n-2)(n-3)}{4!}x^4+\cdots.}
\]

## 14.4 Solution to Question 4: Tangent line versus Maclaurin polynomial

For \(f(x)=\cos x\),
\[
f(0)=1,
\]
and
\[
f'(x)=-\sin x,
\quad f'(0)=0.
\]
The tangent-line approximation at \(x=0\) is
\[
y=f(0)+f'(0)x=1+0x=1.
\]
So
\[
\boxed{y=1.}
\]

For the Maclaurin expansion,
\[
f''(x)=-\cos x,
\quad f''(0)=-1,
\]
\[
f'''(x)=\sin x,
\quad f'''(0)=0,
\]
\[
f^{(4)}(x)=\cos x,
\quad f^{(4)}(0)=1.
\]
Thus
\[
\cos x=1+0x+\frac{-1}{2!}x^2+\frac{0}{3!}x^3+\frac{1}{4!}x^4+\cdots,
\]
so
\[
\boxed{\cos x=1-\frac{x^2}{2}+\frac{x^4}{24}+\cdots.}
\]

The tangent line matches only value and gradient. The Maclaurin polynomial also includes higher-derivative information, so it captures more of the local shape near \(x=0\).

## 14.5 Solution to Question 5: Degree trap

Convert \(3^\circ\) to radians:
\[
3^\circ=3\cdot\frac{\pi}{180}=\frac{\pi}{60}.
\]
Use \(\sin x\approx x\) for small \(x\) in radians:
\[
\boxed{\sin3^\circ\approx\frac{\pi}{60}.}
\]

## 14.6 Solution to Question 6: Compound exponential

Replace \(x\) by \(4x\) in the series for \(e^x\):
\[
e^{4x}=1+(4x)+\frac{(4x)^2}{2!}+\frac{(4x)^3}{3!}+\frac{(4x)^4}{4!}+\cdots.
\]
Simplify:
\[
(4x)^2=16x^2,
\quad \frac{16x^2}{2}=8x^2,
\]
\[
(4x)^3=64x^3,
\quad \frac{64x^3}{6}=\frac{32x^3}{3},
\]
\[
(4x)^4=256x^4,
\quad \frac{256x^4}{24}=\frac{32x^4}{3}.
\]
Therefore
\[
\boxed{e^{4x}=1+4x+8x^2+\frac{32}{3}x^3+\frac{32}{3}x^4+\cdots.}
\]

## 14.7 Solution to Question 7: Compound logarithm and range

Replace \(x\) by \(-5x\) in \(\ln(1+x)\):
\[
\ln(1-5x)=(-5x)-\frac{(-5x)^2}{2}+\frac{(-5x)^3}{3}-\frac{(-5x)^4}{4}+\cdots.
\]
Simplify:
\[
\boxed{\ln(1-5x)=-5x-\frac{25}{2}x^2-\frac{125}{3}x^3-\frac{625}{4}x^4+\cdots.}
\]
For the range, let \(u=-5x\). Then
\[
-1<u\leq1
\]
becomes
\[
-1<-5x\leq1.
\]
Solving:
\[
x<\frac15,
\qquad x\geq-\frac15.
\]
Therefore
\[
\boxed{-\frac15\leq x<\frac15.}
\]

## 14.8 Solution to Question 8: Binomial expansion and range

For
\[
(1+2x)^{-3/2},
\]
use \(n=-\frac32\) and replace \(x\) by \(2x\):
\[
(1+2x)^{-3/2}=1+\left(-\frac32\right)(2x)+\frac{\left(-\frac32\right)\left(-\frac52\right)}{2!}(2x)^2+\frac{\left(-\frac32\right)\left(-\frac52\right)\left(-\frac72\right)}{3!}(2x)^3+\cdots.
\]
The \(x\) term is
\[
-3x.
\]
The \(x^2\) term is
\[
\frac{15/4}{2}(4x^2)=\frac{15}{8}\cdot4x^2=\frac{15}{2}x^2.
\]
The \(x^3\) term is
\[
\frac{-105/8}{6}(8x^3)=-\frac{35}{16}\cdot8x^3=-\frac{35}{2}x^3.
\]
Therefore
\[
\boxed{(1+2x)^{-3/2}=1-3x+\frac{15}{2}x^2-\frac{35}{2}x^3+\cdots.}
\]
The range is
\[
|2x|<1,
\]
so
\[
\boxed{|x|<\frac12.}
\]

## 14.9 Solution to Question 9: Product of standard series

Use
\[
e^{2x}=1+2x+2x^2+\frac{4x^3}{3}+\cdots,
\]
and
\[
\cos x=1-\frac{x^2}{2}+\cdots.
\]
Multiply:
\[
e^{2x}\cos x=\left(1+2x+2x^2+\frac{4x^3}{3}+\cdots\right)\left(1-\frac{x^2}{2}+\cdots\right).
\]
Keep terms up to \(x^3\):
\[
1\left(1-\frac{x^2}{2}\right)=1-\frac{x^2}{2},
\]
\[
2x\left(1-\frac{x^2}{2}\right)=2x-x^3,
\]
\[
2x^2\left(1-\frac{x^2}{2}\right)=2x^2+\text{terms beyond }x^3,
\]
\[
\frac{4x^3}{3}\left(1-\frac{x^2}{2}\right)=\frac{4x^3}{3}+\text{terms beyond }x^3.
\]
Collect:
\[
e^{2x}\cos x=1+2x+\left(-\frac{x^2}{2}+2x^2\right)+\left(-x^3+\frac{4x^3}{3}\right)+\cdots.
\]
Therefore
\[
\boxed{e^{2x}\cos x=1+2x+\frac{3}{2}x^2+\frac{1}{3}x^3+\cdots.}
\]

## 14.10 Solution to Question 10: Small-angle simplification

Use
\[
\cos u\approx1-\frac{u^2}{2}.
\]
With \(u=2x\),
\[
\cos2x\approx1-\frac{(2x)^2}{2}=1-2x^2.
\]
Therefore
\[
1-\cos2x\approx1-(1-2x^2)=2x^2.
\]
So
\[
\frac{1-\cos2x}{x^2}\approx\frac{2x^2}{x^2}=2.
\]
Thus
\[
\boxed{2.}
\]

## 14.11 Solution to Question 11: Mixed standard series

Use
\[
e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots,
\]
and
\[
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots.
\]
Multiply:
\[
e^x\ln(1+x)=\left(1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots\right)\left(x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots\right).
\]
Keep terms up to \(x^4\):
\[
1\cdot\left(x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}\right)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4},
\]
\[
x\cdot\left(x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}\right)=x^2-\frac{x^3}{2}+\frac{x^4}{3}+\text{terms beyond }x^4,
\]
\[
\frac{x^2}{2}\cdot\left(x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}\right)=\frac{x^3}{2}-\frac{x^4}{4}+\text{terms beyond }x^4,
\]
\[
\frac{x^3}{6}\cdot\left(x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}\right)=\frac{x^4}{6}+\text{terms beyond }x^4.
\]
Collect:
\[
x+rac{x^2}{2}+\frac{x^3}{3}+\left(-\frac{x^4}{4}+\frac{x^4}{3}-\frac{x^4}{4}+\frac{x^4}{6}\right)+\cdots.
\]
Use common denominator \(12\):
\[
-\frac{3}{12}+\frac{4}{12}-\frac{3}{12}+\frac{2}{12}=0.
\]
Therefore
\[
\boxed{e^x\ln(1+x)=x+\frac{x^2}{2}+\frac{x^3}{3}+0x^4+\cdots.}
\]
The inherited range is
\[
\boxed{-1<x\leq1.}
\]

## 14.12 Solution to Question 12: General term and substitution

The standard series is
\[
\sin x=\sum_{r=0}^{\infty}(-1)^r\frac{x^{2r+1}}{(2r+1)!}.
\]
Replace \(x\) by \(3x\):
\[
\sin(3x)=\sum_{r=0}^{\infty}(-1)^r\frac{(3x)^{2r+1}}{(2r+1)!}.
\]
Since
\[
(3x)^{2r+1}=3^{2r+1}x^{2r+1},
\]
the general term is
\[
\boxed{(-1)^r\frac{3^{2r+1}x^{2r+1}}{(2r+1)!}.}
\]
Now expand:
\[
\sin(3x)=3x-\frac{(3x)^3}{3!}+\frac{(3x)^5}{5!}-\frac{(3x)^7}{7!}+\cdots.
\]
Simplify:
\[
-\frac{(3x)^3}{3!}=-\frac{27x^3}{6}=-\frac{9x^3}{2},
\]
\[
\frac{(3x)^5}{5!}=\frac{243x^5}{120}=\frac{81x^5}{40},
\]
\[
-\frac{(3x)^7}{7!}=-\frac{2187x^7}{5040}=-\frac{243x^7}{560}.
\]
Therefore
\[
\boxed{\sin(3x)=3x-\frac{9}{2}x^3+\frac{81}{40}x^5-\frac{243}{560}x^7+\cdots.}
\]

---

# 15. Exam Technique Notes

## 15.1 Always begin with the correct centre

For this CCEA lesson, **Maclaurin** means expansion about \(x=0\). The derivative values are
\[
f(0),\qquad f'(0),\qquad f''(0),\qquad f'''(0),\ldots
\]
The core formula is
\[
\boxed{f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots.}
\]

## 15.2 Write the Maclaurin skeleton before simplifying

Write
\[
f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\frac{f^{(4)}(0)}{4!}x^4+\cdots.
\]
This prevents the most common coefficient error:
\[
\text{coefficient of }x^r\neq f^{(r)}(0)
\]
in general. The coefficient is
\[
\boxed{\frac{f^{(r)}(0)}{r!}.}
\]

## 15.3 Keep factorials visible until the final simplification

For example, \(\frac{x^5}{5!}\) should not be simplified too soon if the factorial structure helps reveal the pattern. When giving a final polynomial approximation, simplify if the question asks for a polynomial:
\[
5!=120,
\qquad \frac{x^5}{5!}=\frac{x^5}{120}.
\]

## 15.4 Use exact values, not unnecessary decimals

Prefer \(\frac{9x^2}{2}\) over \(4.5x^2\), and prefer \(\frac{\pi}{60}\) over a decimal unless the question explicitly asks for one.

## 15.5 State range of validity when required

Remember:
\[
e^x,
\quad \sin x,
\quad \cos x
\]
are valid for all real \(x\).

\[
\ln(1+x)
\]
is valid for
\[
\boxed{-1<x\leq1.}
\]
For non-terminating binomial expansions,
\[
(1+x)^n
\]
usually requires
\[
\boxed{|x|<1.}
\]

## 15.6 Watch inequality reversal

When dividing by a negative number, reverse the inequality sign. This is essential for ranges such as \(\ln(1-5x)\), where
\[
-1<-5x\leq1
\]
gives
\[
\boxed{-\frac15\leq x<\frac15.}
\]

## 15.7 Use brackets for compound functions

If expanding \(e^{4x}\), write
\[
e^{4x}=1+(4x)+\frac{(4x)^2}{2!}+\frac{(4x)^3}{3!}+\cdots.
\]
Do not write
\[
1+4x+\frac{4x^2}{2!}+\frac{4x^3}{3!}+\cdots.
\]

## 15.8 Know when to use substitution versus direct differentiation

For standard functions and simple compounds, substitution is usually fastest:
\[
e^{3x},
\quad \sin(2x),
\quad \ln(1-4x),
\quad (1+5x)^{-1/2}.
\]
Use direct differentiation when the function is not a standard listed series, the question asks you to derive from first principles, or the coefficient pattern is not obvious.

## 15.9 For products, keep only enough terms

If expanding \(e^x\cos x\) up to \(x^3\), use
\[
e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots,
\]
and
\[
\cos x=1-\frac{x^2}{2}+\cdots.
\]
The \(x^4\) term in \(\cos x\) is not needed for a product up to \(x^3\).

## 15.10 Small-angle approximations require radians

For small \(x\) in radians,
\[
\sin x\approx x,
\quad \cos x\approx1-\frac{x^2}{2},
\quad \tan x\approx x.
\]
If the angle is in degrees, convert it first.

## 15.11 Be clear about equality versus approximation

Write either
\[
e^x=1+x+\frac{x^2}{2}+\cdots
\]
or
\[
e^x\approx1+x+\frac{x^2}{2}.
\]
Do not write
\[
e^x=1+x+\frac{x^2}{2}
\]
as though this finite polynomial were exact.

## 15.12 CCEA-style caution about cross-board evidence

The supplied DrFrost/Pearson chapter includes Edexcel-style comments about Taylor formulae being given inside exam questions and a chapter path through Taylor series, limits and differential equations. This is useful context, but not CCEA authority. The CCEA core for this lesson remains Maclaurin series, standard expansions, compound expansions and small-angle approximations.

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Official CCEA wording | Covered in lesson? | Coverage notes |
|---|---|---:|---|
| `FA21-FAF-LO004` | find the Maclaurin series of a function, including the general term | Yes | Covered through derivative matching, coefficient formula, direct examples, and general terms. |
| `FA21-FAF-LO005` | recognise and use the Maclaurin series for \(e^x\), \(\ln(1+x)\), \(\sin x\), \(\cos x\) and \((1+x)^n\), and be aware of the range of values of \(x\) for which they are valid | Yes | All five standard series stated, derived or used. Range of validity included. |
| `FA21-FAF-LO006` | derive the series expansions of simple compound functions | Yes | Covered through substitution and product examples. |
| `FA21-FAF-LO007` | demonstrate understanding of and use the standard small angle approximations \(\sin x\approx x\), \(\cos x\approx1-x^2/2\) and \(\tan x\approx x\), where \(x\) is in radians | Yes | Covered through derivation, radian warnings and examples. |

## 16.2 Evidence coverage table

| Evidence item | Lesson use | Status |
|---|---|---|
| Maclaurin series as power series around \(x=0\) | Used in Sections 6, 7 and 8 | Covered |
| Matching values at \(x=0\) | Used to derive \(a_0=f(0)\) | Covered |
| Matching gradients at \(x=0\) | Used to derive \(a_1=f'(0)\) | Covered |
| Matching second and third derivatives | Used to derive factorial denominators | Covered |
| \(\sin x\) expansion | Fully derived and used | Covered |
| General Maclaurin formula | Stated, derived and applied | Covered |
| \(\ln(1+x)\) limited range | Included and applied to compound logarithms | Covered |
| Visual idea: approximations best near \(x=0\) | Included in big picture and visual placeholders | Covered |
| “Entire function” note | Logged as not syllabus vocabulary | Excluded from core |
| Taylor series about \(x=a\) | Mentioned only as optional enrichment and boundary context | Excluded from core |
| Limits using series | Logged as off-spec for this CCEA lesson | Excluded from core |
| Differential-equation series solutions | Logged as off-spec for this CCEA lesson | Excluded from core |

## 16.3 Bridge coverage table

| Bridge topic | Covered? | Where |
|---|---:|---|
| Ordinary differentiation | Yes | Sections 5, 8, 11, 14 |
| Higher derivatives | Yes | Sections 7, 8, 11 |
| Tangent-line approximation | Yes | Sections 5 and 14.4 |
| Factorial notation | Yes | Sections 7, 8, 12, 14 |
| Trig exact values | Yes | Sections 8, 11, 14 |
| Radian measure | Yes | Sections 8.8, 12, 14.5, 15 |
| Logarithm domain | Yes | Sections 7, 8.4, 12, 14.7 |
| Binomial expansion | Yes | Sections 8.4, 8.6, 14.8 |
| Series notation | Yes | Sections 7, 8.9, 14.12 |

## 16.4 Off-Spec Content Found but Excluded

| Content | Evidence source | Why excluded from core | Treatment |
|---|---|---|---|
| Taylor series about \(x=a\) | Uploaded DrFrost/Pearson PDF, transcript and screenshots | The identified CCEA LO boundary for this lesson is Maclaurin series, not Taylor series about arbitrary centres. | Mentioned only as optional enrichment and relationship note. |
| Limits using Taylor/Maclaurin series | Uploaded PDF and transcript | Not part of `FA21-FAF-LO004` to `FA21-FAF-LO007`. | Excluded from core. |
| Indeterminate forms such as \(0/0\), \(\infty/\infty\), \(0\times\infty\) | Uploaded PDF and transcript | Not part of the identified Maclaurin LO set. | Excluded from core. |
| Series solutions to differential equations | Uploaded PDF and transcript | Not part of the identified Maclaurin LO set. | Excluded from core. |
| Edexcel-specific exam comments | Teacher transcript | Cross-board exam guidance cannot be treated as CCEA exam guidance. | Logged but not used for CCEA exam technique. |
| “Entire function” vocabulary | Uploaded PDF | The evidence itself notes this word is not in the syllabus. | Not taught as core vocabulary. |

## 16.5 Optional Enrichment Not Required by CCEA

Students may optionally read the following as enrichment after mastering the CCEA Maclaurin content:

1. A Taylor series about \(x=a\) is a shifted version of the Maclaurin idea.
2. A Maclaurin series is the special case of a Taylor series with \(a=0\).
3. Taylor series can improve approximation away from \(x=0\).
4. Series can sometimes be used to evaluate limits.
5. Series can sometimes be used to solve differential equations.

These are mathematical relatives, not invited guests at the CCEA core dinner for this lesson.

## 16.6 Weak evidence warnings

| Issue | Warning |
|---|---|
| Uploaded lesson evidence is cross-board FP1 | It contains valid mathematical exposition, but the CCEA specification boundary controls the lesson. |
| Screenshot PDF is image-heavy | Only visible/readable details are preserved. No uninspected visual detail is claimed. |
| Direct CCEA textbook examples not supplied | Generated practice questions are labelled as AI-generated and not past-paper/textbook questions. |
| Direct CCEA past-paper examples not supplied | Exam-style guidance is syllabus-aware but not claimed as past-paper-specific. |
| Topic-specific checklist for this exact sublesson not separately supplied | Global project checklist and specification map used instead. |

## 16.7 Missing evidence log

| Missing evidence | Impact | Lesson action |
|---|---|---|
| Direct CCEA textbook extract for Maclaurin series | Medium | No textbook questions are claimed. |
| Direct CCEA past-paper questions for `FA21-FAF-LO004` to `FA21-FAF-LO007` | Medium | Practice questions are generated and labelled as such. |
| Topic-specific FA21-FAF Maclaurin checklist | Low | Global evidence checklist used. |
| Full inspection of every screenshot page | Medium | Visual claims restricted to inspected/readable details. |
| CCEA mark scheme guidance for Maclaurin questions | Medium | Exam technique remains general and syllabus-aware, not mark-scheme-specific. |

---

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements for the lesson pack. They are not evidence-backed source material, but they are designed to support the CCEA Maclaurin learning objectives.

## 17.1 Recommended diagrams

| Enhancement | Purpose | Related placeholder |
|---|---|---|
| Derivative-matching ladder diagram | Show \(P(0)=a_0\), \(P'(0)=a_1\), \(P''(0)=2!a_2\), \(P'''(0)=3!a_3\). | `FA21MaclaurinSeriesSVG-002` |
| Tangent line versus Maclaurin polynomial | Compare ordinary A-Level tangent approximation with Further Maths higher-order approximation. | `FA21MaclaurinSeriesBridgeSVG-001` |
| Successive \(\sin x\) approximation graph | Show \(x\), \(x-\frac{x^3}{3!}\), \(x-\frac{x^3}{3!}+\frac{x^5}{5!}\). | `FA21MaclaurinSeriesSVG-001`, `FA21MaclaurinSeriesTikZ-001` |
| Standard series memory map | Connect \(e^x\), \(\sin x\), \(\cos x\), \(\ln(1+x)\), \((1+x)^n\) to patterns. | `FA21MaclaurinSeriesMermaid-001` |
| Optional Maclaurin versus Taylor centre visual | Show \(x=0\) versus \(x=a\) as expansion centres. | `FA21MaclaurinSeriesEnrichmentSVG-001` |

## 17.2 Recommended animations

| Animation | Student action | Mathematical purpose |
|---|---|---|
| Add one derivative at a time | Slider increases from value match to first, second, third and fourth derivative matches. | Shows why each new term improves the approximation near \(x=0\). |
| Series truncation slider | Student increases highest power of \(x\). | Shows difference between exact infinite series and truncated approximation. |
| Range-of-validity warning animation | Student tries values inside/outside \(-1<x\leq1\) for \(\ln(1+x)\). | Prevents blind substitution outside valid ranges. |
| Radian trap toggle | Student toggles degree/radian mode for small angles. | Shows why \(\sin x\approx x\) requires radians. |

## 17.3 Recommended widgets

| Widget ID | Enhancement |
|---|---|
| `FA21MaclaurinSeriesWidget-001` | Maclaurin coefficient builder from derivative values. |
| `FA21MaclaurinSeriesWidget-002` | Standard-series selector and range checker. |
| `FA21MaclaurinSeriesWidget-003` | Small-angle approximation checker with radians warning. |

## 17.4 Recommended extra examples

Add further generated examples in a later revision bank:

1. Expand \(\cos(3x)\) up to \(x^6\).
2. Expand \(e^{-x}\sin x\) up to \(x^4\).
3. Expand \(\ln(1+2x)-\ln(1-x)\) up to \(x^3\), with range.
4. Expand \((1-4x)^{-2}\) and explain why the expansion is infinite.
5. Use small-angle approximations to simplify \(\frac{\tan5x}{\sin2x}\) for small \(x\) in radians.

---

# 18. Supplementary Sources Used

## 18.1 Project Sources used

| Source | Role |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Controlled the CCEA unit, topic and LO boundary. |
| `Further_Maths_README_module_map.md` | Supported project naming, metadata and workflow conventions. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Supported evidence hierarchy, missing evidence and boundary-risk logging. |
| `Further Maths Portal Build – Knowledge Evidence.txt` | Supported portal lesson-pack workflow. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Used only for ordinary A-Level Maths bridge context. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Used only for ordinary Maths bridge context. |

Ordinary A-Level Mathematics sources are bridge context only. They do not override the CCEA Further Mathematics specification boundary.

## 18.2 Lesson-specific evidence used

| Source | Role |
|---|---|
| `FP1-Chp6-TaylorSeries.pdf` | Used for Maclaurin recap, derivative matching, \(\sin x\) expansion, visual approximation idea and off-spec Taylor/limits/DE logging. |
| `transcripts.md` | Used for teacher phrasing on Maclaurin/Taylor relationship, warnings and cross-board boundary notes. |
| `Chapter_6_Taylor_Series_🧩_(Further_Pure_1)_screenshots.pdf` | Used for visual evidence, especially the opening Taylor/Maclaurin comparison slide and graph-based explanation. |

## 18.3 Cross-board source notes

The supplied lesson-specific evidence is labelled **Further Pure 1 Chapter 6: Taylor Series** and appears to follow a Pearson/DrFrost FP1 route. It contains Taylor expansions about arbitrary \(x=a\), limits using Taylor/Maclaurin series, indeterminate forms, differential-equation series solutions and Edexcel-style exam comments. These are mathematically useful but not treated as CCEA core unless the CCEA `FA21-FAF` LO boundary supports the content.

## 18.4 Evidence limitations

| Limitation | Handling |
|---|---|
| Screenshot PDF is image-heavy and long | Only inspected/readable visual details are claimed. |
| Direct CCEA textbook examples unavailable | Generated examples are clearly labelled as AI-generated. |
| Direct CCEA past-paper examples unavailable | Practice questions are not labelled as past-paper. |
| Cross-board Taylor chapter does not match CCEA Maclaurin boundary exactly | Lesson core is controlled by the CCEA specification map. |
| Some visual slide details may be unreadable or truncated | Visual placeholders include proposed teaching visuals rather than claiming unsupported source detail. |

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

| Check | Yes / Not yet |
|---|---|
| I can differentiate powers of \(x\). |  |
| I can find first, second, third and fourth derivatives. |  |
| I know \(\sin0=0\), \(\cos0=1\), \(\tan0=0\). |  |
| I know \(e^0=1\) and \(\ln1=0\). |  |
| I understand factorial notation, including \(0!=1\). |  |
| I can expand and simplify brackets such as \((3x)^4\). |  |
| I can solve inequalities and remember to reverse the sign when dividing by a negative. |  |
| I can convert degrees to radians. |  |

## 19.2 Further Maths method checklist

| Skill | Yes / Not yet |
|---|---|
| I can explain what a Maclaurin series is. |  |
| I know that Maclaurin series are centred at \(x=0\). |  |
| I can derive \(a_r=\frac{f^{(r)}(0)}{r!}\). |  |
| I can write the Maclaurin formula correctly. |  |
| I can find a Maclaurin expansion by direct differentiation. |  |
| I can write the standard series for \(e^x\). |  |
| I can write the standard series for \(\sin x\). |  |
| I can write the standard series for \(\cos x\). |  |
| I can write the standard series for \(\ln(1+x)\). |  |
| I can write the standard binomial series for \((1+x)^n\). |  |
| I can state the validity range for \(\ln(1+x)\). |  |
| I can state the usual validity range for a non-terminating binomial series. |  |
| I can expand simple compound functions by substitution. |  |
| I can multiply two truncated series and collect terms. |  |
| I can identify a general term. |  |

## 19.3 Small-angle checklist

| Skill | Yes / Not yet |
|---|---|
| I know \(\sin x\approx x\) for small \(x\) in radians. |  |
| I know \(\cos x\approx1-\frac{x^2}{2}\) for small \(x\) in radians. |  |
| I know \(\tan x\approx x\) for small \(x\) in radians. |  |
| I can derive these approximations from Maclaurin series. |  |
| I remember to convert degrees to radians first. |  |
| I can simplify expressions such as \(\frac{1-\cos2x}{x^2}\) using small-angle approximations. |  |

## 19.4 Exam technique checklist

| Technique | Yes / Not yet |
|---|---|
| I write the Maclaurin skeleton before substituting values. |  |
| I include factorial denominators. |  |
| I keep exact fractions rather than unnecessary decimals. |  |
| I use brackets when substituting compound expressions such as \(3x\) or \(-2x\). |  |
| I state validity ranges when asked or when using \(\ln(1+x)\) or binomial series. |  |
| I distinguish between exact infinite series and truncated approximations. |  |
| I label small-angle approximations as radian-based. |  |
| I do not treat Taylor-series-about-\(a\) material as CCEA core unless explicitly required by the specification. |  |

## 19.5 Bridge checklist

| Ordinary A-Level idea | Further Maths upgrade | Secure? |
|---|---|---|
| Tangent line uses \(f(0)\) and \(f'(0)\). | Maclaurin uses all higher derivatives too. |  |
| Repeated differentiation gives new functions. | Derivative values become coefficients. |  |
| Factorials are arithmetic notation. | Factorials appear naturally in power-series coefficients. |  |
| Trig values at \(0\) are exact. | They determine which terms survive in \(\sin x\) and \(\cos x\). |  |
| Logarithms have domains. | Series also have validity ranges. |  |
| Binomial expansion can be finite. | Non-integer binomial expansions are usually infinite. |  |
| Radians are used in calculus. | Radians are essential for small-angle approximations. |  |

## 19.6 Visual understanding checklist

| Visual idea | Secure? |
|---|---|
| I understand why substituting \(x=0\) into a power series exposes \(a_0\). |  |
| I understand why differentiating first exposes \(a_1\). |  |
| I understand why differentiating twice gives \(2!a_2\). |  |
| I understand why differentiating three times gives \(3!a_3\). |  |
| I understand why more terms usually improve the approximation near \(x=0\). |  |
| I understand why a Maclaurin approximation may be poor far from \(x=0\). |  |
| I can explain visually why \(\sin x\approx x\) near \(x=0\). |  |
