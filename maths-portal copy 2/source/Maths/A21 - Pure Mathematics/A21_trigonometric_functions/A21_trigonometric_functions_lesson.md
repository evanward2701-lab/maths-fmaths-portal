# A21 Trigonometric Functions

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A2 1 Pure Mathematics |
| Unit code | A21 |
| Topic code | A21-TRIG |
| Official topic area | Trigonometry |
| Lesson title | Trigonometric Functions |
| Topic slug | trigonometric_functions |
| Topic Pascal | TrigonometricFunctions |
| Topic ID | A21TrigonometricFunctions |
| Lesson file | A21_trigonometric_functions_lesson.md |
| Core LO IDs | A21-TRIG-LO002, A21-TRIG-LO003, A21-TRIG-LO004, A21-TRIG-LO008 |
| Supporting LO IDs | A21-TRIG-LO001, AS1-TRIG-LO005, AS1-TRIG-LO006, AS1-TRIG-LO007 |
| Tags | `#A21`, `#Trigonometry`, `#ReciprocalTrig`, `#InverseTrig`, `#TrigIdentities`, `#SolveTrigEquation`, `#Proof` |

## Evidence Map

| Evidence | What it contributes |
|---|---|
| CCEA GCE Mathematics Specification Map | Confirms A21-TRIG topic and official LO boundary. |
| Chapter 6 Trigonometric Functions Transcript | Definitions, teaching explanations, worked examples, teacher warnings and solving/proof methods. |
| P2 Chapter 6 Trigonometric Functions PDF | Slide structure, reciprocal graphs, inverse trig graphs, worked examples and visual structure. |
| Chapter 6 Screenshot PDF | Visual backup for slide sequence. Text was not parsed automatically, so no uninspected detail is claimed. |
| Project README / Module Map | Metadata, folder conventions, phase workflow and placeholder rules. |
| Project Evidence Drop Checklist | Missing evidence, off-spec logging and visual placeholder rules. |

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| A21-TRIG-LO002 | Define $\sec$, $\cosec$, $\cot$, $\arcsin$, $\arccos$, $\arctan$; distinguish reciprocal notation from inverse notation; connect each function to sine, cosine and tangent. |
| A21-TRIG-LO003 | Sketch and interpret graphs of $\sec x$, $\cosec x$, $\cot x$, $\arcsin x$, $\arccos x$, $\arctan x$; state domains, ranges and restrictions. |
| A21-TRIG-LO004 | Derive and use $1+\tan^2x=\sec^2x$ and $1+\cot^2x=\cosec^2x$. |
| A21-TRIG-LO008 | Prove identities involving reciprocal trig functions, using logical chains of equalities and correct algebra. |

## Learning Objectives

By the end of this lesson, the student should be able to:

1. State and use

   $$
   \sec x=\frac{1}{\cos x},\qquad
   \cosec x=\frac{1}{\sin x},\qquad
   \cot x=\frac{1}{\tan x}=\frac{\cos x}{\sin x}.
   $$

2. Explain why $\cos^{-1}x$ means $\arccos x$, not $\dfrac{1}{\cos x}$.

3. Evaluate exact reciprocal trig values such as $\sec\frac{\pi}{4}$ and $\cosec\frac{5\pi}{6}$.

4. Sketch and interpret the graphs of $y=\sec x$, $y=\cosec x$ and $y=\cot x$, including asymptotes, domains and ranges.

5. Solve equations involving $\sec$, $\cosec$ and $\cot$ by converting them into equations involving $\sin$, $\cos$ or $\tan$.

6. Prove identities involving reciprocal trig functions by converting to sine/cosine, combining algebraic fractions and using known identities.

7. Derive and use

   $$
   1+\tan^2x=\sec^2x,\qquad
   1+\cot^2x=\cosec^2x.
   $$

8. Understand how the graphs of $\arcsin x$, $\arccos x$ and $\arctan x$ arise by reflecting restricted trig graphs in the line $y=x$.

## Prerequisite Recap

This lesson assumes earlier A-Level knowledge, not external GCSE sources.

| Prior knowledge | Needed here because |
|---|---|
| $\tan x=\dfrac{\sin x}{\cos x}$ | Used to show $\cot x=\dfrac{\cos x}{\sin x}$. |
| $\sin^2x+\cos^2x=1$ | Used to prove new identities and simplify expressions. |
| Trig graphs of $\sin x$, $\cos x$, $\tan x$ | Reciprocal graphs are built by reciprocating their $y$-values. |
| Exact values | Needed for values at $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$, etc. |
| Solving trig equations in intervals | Used for equations such as $\cosec 3\theta=2$. |
| Algebraic fractions | Used heavily in proof questions. |
| Difference of two squares | Used in identities such as $\cosec^4\theta-\cot^4\theta$. |

GCSE bridge topics are logged only as background and are not used as independent sources: basic sine/cosine/tangent, graph sketching, fractions, factorising and solving quadratics.

## Big Picture Explanation

Chapter 6 adds three reciprocal trigonometric functions:

$$
\sec x,\qquad \cosec x,\qquad \cot x.
$$

They are not mysterious new machines. They are reciprocal versions of familiar functions. The newness is mostly notation, graph behaviour and algebraic fluency.

The chapter has four main strands:

1. understand $\sec$, $\cosec$, $\cot$ and draw their graphs;
2. solve equations involving reciprocal trig functions;
3. prove identities involving reciprocal trig functions;
4. understand inverse trig functions and their domains/ranges.

A useful mental picture: sine, cosine and tangent are the old trig instruments. Secant, cosecant and cotangent are the mirrors that flip their outputs into reciprocals. Sometimes that mirror turns a gentle graph into something with vertical asymptotes, so this chapter has graph-theatre energy.

## Key Definitions and Notation

### 1. Squared trig notation

The notation

$$
\cos^2x
$$

means

$$
(\cos x)^2.
$$

So

$$
\cos^2x=(\cos x)^2.
$$

This is not the same kind of notation as $\cos^{-1}x$.

### 2. Inverse trig notation

The notation

$$
\cos^{-1}x
$$

means

$$
\arccos x.
$$

It means “the angle whose cosine is $x$”. It does **not** mean

$$
\frac{1}{\cos x}.
$$

The $-1$ in inverse trig notation does not mean “power of $-1$”; it means the inverse function.

### 3. Reciprocal trig notation

The reciprocal of $\cos x$ is called $\sec x$:

$$
\sec x=\frac{1}{\cos x}.
$$

The reciprocal of $\sin x$ is called $\cosec x$:

$$
\cosec x=\frac{1}{\sin x}.
$$

The reciprocal of $\tan x$ is called $\cot x$:

$$
\cot x=\frac{1}{\tan x}.
$$

Since

$$
\tan x=\frac{\sin x}{\cos x},
$$

we also have

$$
\cot x=\frac{1}{\tan x}
      =\frac{1}{\frac{\sin x}{\cos x}}
      =\frac{\cos x}{\sin x}.
$$

For proof questions it is usually more useful to use

$$
\cot x=\frac{\cos x}{\sin x}
$$

rather than

$$
\cot x=\frac{1}{\tan x}.
$$

### 4. Reciprocal of the reciprocal

Because reciprocating twice returns to the original function:

$$
\frac{1}{\sec x}=\cos x,
$$

$$
\frac{1}{\cosec x}=\sin x,
$$

$$
\frac{1}{\cot x}=\tan x.
$$

This matters in equations. If $\sec x$ is in a denominator, it can be moved to the numerator as $\cos x$.

## Core Theory

### A. Exact reciprocal trig values

When evaluating reciprocal trig functions, first rewrite them using sine, cosine or tangent.

#### Example 1: Evaluate $\cot\frac{\pi}{4}$

$$
\cot\frac{\pi}{4}
=
\frac{1}{\tan\frac{\pi}{4}}.
$$

Since

$$
\tan\frac{\pi}{4}=1,
$$

we get

$$
\cot\frac{\pi}{4}
=
\frac{1}{1}
=
1.
$$

#### Example 2: Evaluate $\sec\frac{\pi}{4}$

$$
\sec\frac{\pi}{4}
=
\frac{1}{\cos\frac{\pi}{4}}.
$$

Since

$$
\cos\frac{\pi}{4}
=
\frac{1}{\sqrt2},
$$

we get

$$
\sec\frac{\pi}{4}
=
\frac{1}{\frac{1}{\sqrt2}}
=
\sqrt2.
$$

To see the fraction-within-a-fraction clearly:

$$
\frac{1}{\frac{1}{\sqrt2}}
=
1\div \frac{1}{\sqrt2}
=
1\times \sqrt2
=
\sqrt2.
$$

#### Example 3: Evaluate $\cosec\frac{\pi}{3}$

$$
\cosec\frac{\pi}{3}
=
\frac{1}{\sin\frac{\pi}{3}}.
$$

Since

$$
\sin\frac{\pi}{3}
=
\frac{\sqrt3}{2},
$$

we get

$$
\cosec\frac{\pi}{3}
=
\frac{1}{\frac{\sqrt3}{2}}
=
\frac{2}{\sqrt3}.
$$

This may be left as $\frac{2}{\sqrt3}$ unless rationalised form is requested.

#### Example 4: Evaluate $\cot\frac{\pi}{6}$

$$
\cot\frac{\pi}{6}
=
\frac{1}{\tan\frac{\pi}{6}}.
$$

Since

$$
\tan\frac{\pi}{6}
=
\frac{1}{\sqrt3},
$$

we get

$$
\cot\frac{\pi}{6}
=
\frac{1}{\frac{1}{\sqrt3}}
=
\sqrt3.
$$

Equivalently, using $\tan\frac{\pi}{6}=\frac{\sqrt3}{3}$:

$$
\cot\frac{\pi}{6}
=
\frac{1}{\frac{\sqrt3}{3}}
=
\frac{3}{\sqrt3}
=
\sqrt3.
$$

#### Example 5: Evaluate $\cosec\frac{5\pi}{6}$

$$
\cosec\frac{5\pi}{6}
=
\frac{1}{\sin\frac{5\pi}{6}}.
$$

Using the symmetry

$$
\sin(\pi-\theta)=\sin\theta,
$$

we have

$$
\sin\frac{5\pi}{6}
=
\sin\frac{\pi}{6}
=
\frac12.
$$

Therefore

$$
\cosec\frac{5\pi}{6}
=
\frac{1}{\frac12}
=
2.
$$

#### Example 6: Evaluate $\sec\frac{5\pi}{3}$

$$
\sec\frac{5\pi}{3}
=
\frac{1}{\cos\frac{5\pi}{3}}.
$$

Using cosine symmetry,

$$
\cos\frac{5\pi}{3}
=
\cos\frac{\pi}{3}
=
\frac12.
$$

Therefore

$$
\sec\frac{5\pi}{3}
=
\frac{1}{\frac12}
=
2.
$$

### B. Graphs of reciprocal trig functions

The core idea is:

$$
y=\cosec x
$$

comes from

$$
y=\sin x
$$

by reciprocating each $y$-value:

$$
y=\frac{1}{\sin x}.
$$

Likewise,

$$
y=\sec x=\frac{1}{\cos x},
$$

and

$$
y=\cot x=\frac{1}{\tan x}.
$$

#### What reciprocating does

If the original $y$-value is $1$, the reciprocal is still $1$:

$$
\frac{1}{1}=1.
$$

If the original $y$-value is $-1$, the reciprocal is still $-1$:

$$
\frac{1}{-1}=-1.
$$

If the original $y$-value is a small positive number, the reciprocal is a large positive number:

$$
\frac{1}{0.001}=1000.
$$

If the original $y$-value is a small negative number, the reciprocal is a large negative number:

$$
\frac{1}{-0.001}=-1000.
$$

If the original $y$-value is $0$, the reciprocal is undefined:

$$
\frac{1}{0}\quad \text{is undefined}.
$$

That creates vertical asymptotes.

#### Domain and range of $y=\cosec x$

Since

$$
\cosec x=\frac{1}{\sin x},
$$

we cannot allow

$$
\sin x=0.
$$

This happens when

$$
x=n\pi,\qquad n\in\mathbb Z.
$$

So the domain is

$$
x\in\mathbb R,\qquad x\ne n\pi,\quad n\in\mathbb Z.
$$

The range is

$$
y\le -1
\quad\text{or}\quad
y\ge 1.
$$

There are no values between $-1$ and $1$.

#### Domain and range of $y=\sec x$

Since

$$
\sec x=\frac{1}{\cos x},
$$

we cannot allow

$$
\cos x=0.
$$

This happens when

$$
x=\frac{\pi}{2}+n\pi,\qquad n\in\mathbb Z.
$$

So the domain is

$$
x\in\mathbb R,\qquad x\ne \frac{\pi}{2}+n\pi,\quad n\in\mathbb Z.
$$

The range is

$$
y\le -1
\quad\text{or}\quad
y\ge 1.
$$

#### Domain and range of $y=\cot x$

Since

$$
\cot x=\frac{\cos x}{\sin x},
$$

we cannot allow

$$
\sin x=0.
$$

So the domain is

$$
x\in\mathbb R,\qquad x\ne n\pi,\quad n\in\mathbb Z.
$$

The range is

$$
y\in\mathbb R.
$$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-001 | Source: Chapter 6 PDF pages 10-12 + transcript graph explanation | Insert from svg/A21TrigonometricFunctionsSVG-001.svg | Purpose: Show how $y=\sin x$, $y=\cos x$, $y=\tan x$ generate $y=\cosec x$, $y=\sec x$, $y=\cot x$ by reciprocating $y$-values.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-006 | Source: Chapter 6 reciprocal graph explanation | Insert from mermaid/A21TrigonometricFunctionsMermaid-006.md | Purpose: Show how original y-values determine reciprocal graph behaviour.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-003 | Source: Chapter 6 reciprocal graph explanation | Insert from tikz/A21TrigonometricFunctionsTikZ-003.tex | Purpose: Explain $y=\frac1{f(x)}$ behaviour for reciprocal graphs.]

[INTERACTIVE PLACEHOLDER: A21TrigonometricFunctionsWidget-001 | Source: Chapter 6 PDF pages 10-12 | Insert from widgets/A21TrigonometricFunctionsWidget-001.html | Purpose: Let the student toggle $f(x)$ and $\frac1{f(x)}$ to see asymptotes and ranges form.]

### C. Two proof tips for reciprocal trig identities

#### Tip 1: Convert everything into sine and cosine first

Use:

$$
\sec x=\frac{1}{\cos x},
$$

$$
\cosec x=\frac{1}{\sin x},
$$

$$
\cot x=\frac{\cos x}{\sin x}.
$$

This is often better than using

$$
\cot x=\frac{1}{\tan x},
$$

because proof questions usually simplify more cleanly in sine and cosine.

#### Tip 2: Combine algebraic fractions

If you see fractions being added or subtracted, combine them into one fraction.

For example,

$$
\frac{1}{\cos\theta}+\frac{1}{\sin\theta}
$$

has common denominator

$$
\sin\theta\cos\theta.
$$

So

$$
\frac{1}{\cos\theta}+\frac{1}{\sin\theta}
=
\frac{\sin\theta}{\sin\theta\cos\theta}
+
\frac{\cos\theta}{\sin\theta\cos\theta}
=
\frac{\sin\theta+\cos\theta}{\sin\theta\cos\theta}.
$$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-002 | Source: Chapter 6 transcript/PDF + CCEA A21-TRIG-LO008 | Insert from mermaid/A21TrigonometricFunctionsMermaid-002.md | Purpose: Show a proof strategy for reciprocal trig identities.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-005 | Source: Chapter 6 proof examples | Insert from tikz/A21TrigonometricFunctionsTikZ-005.tex | Purpose: Summarise the reciprocal trig identity proof route.]

### D. New reciprocal Pythagorean identities

Start from the familiar identity:

$$
\sin^2x+\cos^2x=1.
$$

#### Derive $1+\tan^2x=\sec^2x$

Divide every term by $\cos^2x$:

$$
\frac{\sin^2x}{\cos^2x}
+
\frac{\cos^2x}{\cos^2x}
=
\frac{1}{\cos^2x}.
$$

Now simplify each term:

$$
\frac{\sin^2x}{\cos^2x}=\tan^2x,
$$

$$
\frac{\cos^2x}{\cos^2x}=1,
$$

$$
\frac{1}{\cos^2x}=\sec^2x.
$$

Therefore

$$
\tan^2x+1=\sec^2x.
$$

Usually written as

$$
1+\tan^2x=\sec^2x.
$$

#### Derive $1+\cot^2x=\cosec^2x$

Start again:

$$
\sin^2x+\cos^2x=1.
$$

Divide every term by $\sin^2x$:

$$
\frac{\sin^2x}{\sin^2x}
+
\frac{\cos^2x}{\sin^2x}
=
\frac{1}{\sin^2x}.
$$

Now simplify each term:

$$
\frac{\sin^2x}{\sin^2x}=1,
$$

$$
\frac{\cos^2x}{\sin^2x}=\cot^2x,
$$

$$
\frac{1}{\sin^2x}=\cosec^2x.
$$

Therefore

$$
1+\cot^2x=\cosec^2x.
$$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-001 | Source: Chapter 6 PDF page 21 + transcript section 7 | Insert from mermaid/A21TrigonometricFunctionsMermaid-001.md | Purpose: Flowchart deriving the two new identities from $\sin^2x+\cos^2x=1$.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-001 | Source: Chapter 6 PDF page 21 | Insert from tikz/A21TrigonometricFunctionsTikZ-001.tex | Purpose: Derive $1+\tan^2x=\sec^2x$ and $1+\cot^2x=\cosec^2x$ from $\sin^2x+\cos^2x=1$.]

## Visual Asset Integration

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-001 | Source: Chapter 6 PDF pages 10-12 | Insert from svg/A21TrigonometricFunctionsSVG-001.svg | Purpose: Reciprocal graph comparison for $\sin/\cosec$, $\cos/\sec$, $\tan/\cot$.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-002 | Source: Chapter 6 PDF pages 25-26 | Insert from svg/A21TrigonometricFunctionsSVG-002.svg | Purpose: Show inverse trig graphs as reflections in $y=x$ with restricted domains/ranges.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-003 | Source: Chapter 6 notation warning | Insert from svg/A21TrigonometricFunctionsSVG-003.svg | Purpose: Summarise the notation distinction between $\cos^2x$, $\cos^{-1}x$ and $\sec x$.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-001 | Source: Chapter 6 reciprocal identity derivation | Insert from mermaid/A21TrigonometricFunctionsMermaid-001.md | Purpose: Derive reciprocal Pythagorean identities.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-002 | Source: Chapter 6 proof-method evidence | Insert from mermaid/A21TrigonometricFunctionsMermaid-002.md | Purpose: Give a decision flow for proving identities.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-003 | Source: Chapter 6 reciprocal-trig equation examples | Insert from mermaid/A21TrigonometricFunctionsMermaid-003.md | Purpose: Show the solving process for sec, cosec and cot equations.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-004 | Source: Chapter 6 inverse trig functions evidence | Insert from mermaid/A21TrigonometricFunctionsMermaid-004.md | Purpose: Explain why inverse trig graphs require restricted original domains.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-005 | Source: Chapter 6 notation warning | Insert from mermaid/A21TrigonometricFunctionsMermaid-005.md | Purpose: Prevent confusion between inverse trig notation and reciprocal trig notation.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-006 | Source: Chapter 6 reciprocal graph explanation | Insert from mermaid/A21TrigonometricFunctionsMermaid-006.md | Purpose: Show how original y-values determine reciprocal graph behaviour.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-001 | Source: Chapter 6 identity derivation | Insert from tikz/A21TrigonometricFunctionsTikZ-001.tex | Purpose: Derive reciprocal Pythagorean identities.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-002 | Source: Chapter 6 notation warning | Insert from tikz/A21TrigonometricFunctionsTikZ-002.tex | Purpose: Distinguish squared trig, inverse trig and reciprocal trig notation.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-003 | Source: Chapter 6 reciprocal graph explanation | Insert from tikz/A21TrigonometricFunctionsTikZ-003.tex | Purpose: Explain $y=\frac1{f(x)}$ behaviour for reciprocal graphs.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-004 | Source: Chapter 6 inverse trig evidence | Insert from tikz/A21TrigonometricFunctionsTikZ-004.tex | Purpose: Show domain/range swapping for inverse trig functions.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-005 | Source: Chapter 6 proof examples | Insert from tikz/A21TrigonometricFunctionsTikZ-005.tex | Purpose: Summarise the reciprocal trig identity proof route.]

[INTERACTIVE PLACEHOLDER: A21TrigonometricFunctionsWidget-001 | Source: Chapter 6 reciprocal graph evidence | Insert from widgets/A21TrigonometricFunctionsWidget-001.html | Purpose: Toggle original and reciprocal trig graphs.]

[INTERACTIVE PLACEHOLDER: A21TrigonometricFunctionsWidget-002 | Source: Chapter 6 inverse trig evidence | Insert from widgets/A21TrigonometricFunctionsWidget-002.html | Purpose: Explore inverse trig restrictions and reflections.]

## Worked Examples

### Worked Example 1: Simplify $\sin\theta\cot\theta\sec\theta$

Start with

$$
\sin\theta\cot\theta\sec\theta.
$$

Convert to sine and cosine:

$$
\sin\theta
\cdot
\frac{\cos\theta}{\sin\theta}
\cdot
\frac{1}{\cos\theta}.
$$

Cancel $\sin\theta$:

$$
\sin\theta
\cdot
\frac{1}{\sin\theta}
=
1.
$$

Cancel $\cos\theta$:

$$
\cos\theta
\cdot
\frac{1}{\cos\theta}
=
1.
$$

So

$$
\sin\theta\cot\theta\sec\theta
=
1.
$$

### Worked Example 2: Simplify $\sin\theta\cos\theta(\sec\theta+\cosec\theta)$

Start with

$$
\sin\theta\cos\theta(\sec\theta+\cosec\theta).
$$

Convert reciprocal trig functions:

$$
=
\sin\theta\cos\theta
\left(
\frac{1}{\cos\theta}
+
\frac{1}{\sin\theta}
\right).
$$

Combine the fractions inside the bracket:

$$
\frac{1}{\cos\theta}
+
\frac{1}{\sin\theta}
=
\frac{\sin\theta}{\sin\theta\cos\theta}
+
\frac{\cos\theta}{\sin\theta\cos\theta}.
$$

So

$$
\frac{1}{\cos\theta}
+
\frac{1}{\sin\theta}
=
\frac{\sin\theta+\cos\theta}{\sin\theta\cos\theta}.
$$

Substitute:

$$
\sin\theta\cos\theta
\left(
\frac{\sin\theta+\cos\theta}{\sin\theta\cos\theta}
\right).
$$

Cancel:

$$
=
\sin\theta+\cos\theta.
$$

Therefore

$$
\sin\theta\cos\theta(\sec\theta+\cosec\theta)
=
\sin\theta+\cos\theta.
$$

### Worked Example 3: Prove

$$
\frac{\cot\theta\cosec\theta}{\sec^2\theta+\cosec^2\theta}
\equiv
\cos^3\theta.
$$

Start with the left-hand side:

$$
\text{LHS}
=
\frac{\cot\theta\cosec\theta}{\sec^2\theta+\cosec^2\theta}.
$$

Convert everything to sine and cosine:

$$
=
\frac{
\frac{\cos\theta}{\sin\theta}\cdot \frac{1}{\sin\theta}
}{
\frac{1}{\cos^2\theta}+\frac{1}{\sin^2\theta}
}.
$$

Simplify the numerator:

$$
\frac{\cos\theta}{\sin\theta}\cdot \frac{1}{\sin\theta}
=
\frac{\cos\theta}{\sin^2\theta}.
$$

So

$$
\text{LHS}
=
\frac{
\frac{\cos\theta}{\sin^2\theta}
}{
\frac{1}{\cos^2\theta}+\frac{1}{\sin^2\theta}
}.
$$

Combine the fractions in the denominator:

$$
\frac{1}{\cos^2\theta}+\frac{1}{\sin^2\theta}
=
\frac{\sin^2\theta}{\sin^2\theta\cos^2\theta}
+
\frac{\cos^2\theta}{\sin^2\theta\cos^2\theta}.
$$

So

$$
\frac{1}{\cos^2\theta}+\frac{1}{\sin^2\theta}
=
\frac{\sin^2\theta+\cos^2\theta}{\sin^2\theta\cos^2\theta}.
$$

Use

$$
\sin^2\theta+\cos^2\theta=1.
$$

Therefore

$$
\frac{1}{\cos^2\theta}+\frac{1}{\sin^2\theta}
=
\frac{1}{\sin^2\theta\cos^2\theta}.
$$

Now substitute:

$$
\text{LHS}
=
\frac{
\frac{\cos\theta}{\sin^2\theta}
}{
\frac{1}{\sin^2\theta\cos^2\theta}
}.
$$

Dividing by a fraction means multiplying by its reciprocal:

$$
=
\frac{\cos\theta}{\sin^2\theta}
\cdot
\sin^2\theta\cos^2\theta.
$$

Cancel $\sin^2\theta$:

$$
=
\cos\theta\cos^2\theta.
$$

So

$$
=
\cos^3\theta.
$$

Hence

$$
\frac{\cot\theta\cosec\theta}{\sec^2\theta+\cosec^2\theta}
\equiv
\cos^3\theta.
$$

### Worked Example 4: Prove

$$
\sec x-\cos x\equiv \sin x\tan x.
$$

Start from the left-hand side:

$$
\text{LHS}
=
\sec x-\cos x.
$$

Convert $\sec x$:

$$
=
\frac{1}{\cos x}-\cos x.
$$

Write $\cos x$ as a fraction with denominator $\cos x$:

$$
\cos x
=
\frac{\cos^2x}{\cos x}.
$$

So

$$
\text{LHS}
=
\frac{1}{\cos x}
-
\frac{\cos^2x}{\cos x}.
$$

Combine:

$$
=
\frac{1-\cos^2x}{\cos x}.
$$

Use

$$
1-\cos^2x=\sin^2x.
$$

So

$$
=
\frac{\sin^2x}{\cos x}.
$$

Split one factor of $\sin x$:

$$
=
\sin x\cdot \frac{\sin x}{\cos x}.
$$

Use

$$
\tan x=\frac{\sin x}{\cos x}.
$$

Therefore

$$
=
\sin x\tan x.
$$

Hence

$$
\sec x-\cos x\equiv \sin x\tan x.
$$

### Worked Example 5: Solve

$$
\sec\theta=-2.5,\qquad 0^\circ\le \theta\le 360^\circ.
$$

Use

$$
\sec\theta=\frac{1}{\cos\theta}.
$$

So

$$
\frac{1}{\cos\theta}=-2.5.
$$

Take reciprocals:

$$
\cos\theta=\frac{1}{-2.5}.
$$

Since

$$
-2.5=-\frac52,
$$

we have

$$
\frac{1}{-2.5}
=
-\frac25.
$$

So

$$
\cos\theta=-\frac25.
$$

Now solve:

$$
\theta=\cos^{-1}\left(-\frac25\right).
$$

Calculator gives

$$
\theta=113.6^\circ \quad \text{to 1 d.p.}
$$

Cosine is negative in quadrants II and III. The second solution is

$$
360^\circ-113.6^\circ=246.4^\circ.
$$

Therefore

$$
\theta=113.6^\circ,\ 246.4^\circ.
$$

### Worked Example 6: Solve

$$
\cot 2\theta=0.6,\qquad 0^\circ\le \theta\le 360^\circ.
$$

Use the reciprocal relationship:

$$
\frac{1}{\cot 2\theta}=\tan 2\theta.
$$

Take reciprocals:

$$
\tan 2\theta=\frac{1}{0.6}.
$$

Since

$$
0.6=\frac35,
$$

we have

$$
\frac{1}{0.6}
=
\frac{1}{\frac35}
=
\frac53.
$$

So

$$
\tan 2\theta=\frac53.
$$

Change the interval. Since

$$
0^\circ\le \theta\le 360^\circ,
$$

then

$$
0^\circ\le 2\theta\le 720^\circ.
$$

Now solve:

$$
2\theta=\tan^{-1}\left(\frac53\right).
$$

Calculator gives

$$
2\theta=59.0^\circ \quad \text{to 3 s.f.}
$$

For tangent, add $180^\circ$ repeatedly:

$$
2\theta=59.0^\circ,\ 239.0^\circ,\ 419.0^\circ,\ 599.0^\circ.
$$

The next would be

$$
779.0^\circ,
$$

which is outside

$$
0^\circ\le 2\theta\le 720^\circ.
$$

Now halve all values:

$$
\theta=29.5^\circ,\ 119.5^\circ,\ 209.5^\circ,\ 299.5^\circ.
$$

### Worked Example 7: Solve

$$
\cot\theta=0,\qquad 0\le \theta\le 2\pi.
$$

This is a special case.

If we try to take reciprocals:

$$
\frac{1}{\cot\theta}=\tan\theta,
$$

but

$$
\frac{1}{0}
$$

is undefined.

So $\tan\theta$ must be undefined.

The tangent graph is undefined at its vertical asymptotes:

$$
\theta=\frac{\pi}{2},\ \frac{3\pi}{2}
$$

inside

$$
0\le \theta\le 2\pi.
$$

Therefore

$$
\theta=\frac{\pi}{2},\ \frac{3\pi}{2}.
$$

### Worked Example 8: Solve

$$
\cosec 3\theta=2,\qquad 0^\circ\le \theta<360^\circ.
$$

Convert the interval:

$$
0^\circ\le 3\theta<1080^\circ.
$$

Use

$$
\cosec 3\theta=\frac{1}{\sin 3\theta}.
$$

So

$$
\frac{1}{\sin 3\theta}=2.
$$

Take reciprocals:

$$
\sin 3\theta=\frac12.
$$

First solutions:

$$
3\theta=30^\circ,\ 150^\circ.
$$

Add $360^\circ$ to each until reaching the interval limit:

$$
3\theta=30^\circ,\ 390^\circ,\ 750^\circ,
$$

and

$$
3\theta=150^\circ,\ 510^\circ,\ 870^\circ.
$$

Now divide every value by $3$:

$$
\theta=10^\circ,\ 130^\circ,\ 250^\circ,
$$

and

$$
\theta=50^\circ,\ 170^\circ,\ 290^\circ.
$$

Therefore

$$
\theta=10^\circ,\ 50^\circ,\ 130^\circ,\ 170^\circ,\ 250^\circ,\ 290^\circ.
$$

### Worked Example 9: Prove

$$
\cosec^4\theta-\cot^4\theta
\equiv
\frac{1+\cos^2\theta}{1-\cos^2\theta}.
$$

Start with the left-hand side:

$$
\text{LHS}
=
\cosec^4\theta-\cot^4\theta.
$$

Use difference of two squares:

$$
a^2-b^2=(a+b)(a-b).
$$

Here,

$$
a=\cosec^2\theta,\qquad b=\cot^2\theta.
$$

So

$$
\cosec^4\theta-\cot^4\theta
=
(\cosec^2\theta+\cot^2\theta)
(\cosec^2\theta-\cot^2\theta).
$$

Use

$$
1+\cot^2\theta=\cosec^2\theta.
$$

Rearrange:

$$
\cosec^2\theta-\cot^2\theta=1.
$$

Therefore

$$
\text{LHS}
=
(\cosec^2\theta+\cot^2\theta)(1).
$$

So

$$
\text{LHS}
=
\cosec^2\theta+\cot^2\theta.
$$

Convert to sine and cosine:

$$
=
\frac{1}{\sin^2\theta}
+
\frac{\cos^2\theta}{\sin^2\theta}.
$$

Combine:

$$
=
\frac{1+\cos^2\theta}{\sin^2\theta}.
$$

Use

$$
\sin^2\theta=1-\cos^2\theta.
$$

Therefore

$$
=
\frac{1+\cos^2\theta}{1-\cos^2\theta}.
$$

Hence

$$
\cosec^4\theta-\cot^4\theta
\equiv
\frac{1+\cos^2\theta}{1-\cos^2\theta}.
$$

### Worked Example 10: Solve

$$
4\cosec^2\theta-9=\cot\theta,\qquad 0^\circ\le \theta\le 360^\circ.
$$

Use

$$
\cosec^2\theta=1+\cot^2\theta.
$$

Substitute:

$$
4(1+\cot^2\theta)-9=\cot\theta.
$$

Expand:

$$
4+4\cot^2\theta-9=\cot\theta.
$$

Simplify:

$$
4\cot^2\theta-5=\cot\theta.
$$

Bring all terms to one side:

$$
4\cot^2\theta-\cot\theta-5=0.
$$

Factorise:

$$
(4\cot\theta-5)(\cot\theta+1)=0.
$$

So

$$
4\cot\theta-5=0
$$

or

$$
\cot\theta+1=0.
$$

First branch:

$$
4\cot\theta=5,
$$

$$
\cot\theta=\frac54.
$$

Take reciprocals:

$$
\tan\theta=\frac45.
$$

So

$$
\theta=\tan^{-1}\left(\frac45\right)
=
38.7^\circ.
$$

Add $180^\circ$:

$$
\theta=38.7^\circ,\ 218.7^\circ.
$$

Second branch:

$$
\cot\theta=-1.
$$

Take reciprocals:

$$
\tan\theta=-1.
$$

The reference angle is

$$
45^\circ.
$$

Tangent is negative in quadrants II and IV:

$$
\theta=135^\circ,\ 315^\circ.
$$

Therefore

$$
\theta=38.7^\circ,\ 135^\circ,\ 218.7^\circ,\ 315^\circ.
$$

### Worked Example 11: Solve

$$
2\cosec^2x+\cot x=5,\qquad 0\le x<2\pi.
$$

Use

$$
\cosec^2x=1+\cot^2x.
$$

Substitute:

$$
2(1+\cot^2x)+\cot x=5.
$$

Expand:

$$
2+2\cot^2x+\cot x=5.
$$

Bring all terms to one side:

$$
2\cot^2x+\cot x-3=0.
$$

Factorise:

$$
(2\cot x+3)(\cot x-1)=0.
$$

So

$$
2\cot x+3=0
$$

or

$$
\cot x-1=0.
$$

First branch:

$$
2\cot x=-3,
$$

$$
\cot x=-\frac32.
$$

Take reciprocals:

$$
\tan x=-\frac23.
$$

For

$$
0\le x<2\pi,
$$

solutions are in quadrants II and IV:

$$
x=2.55,\ 5.70
$$

to 3 significant figures.

Second branch:

$$
\cot x=1.
$$

Take reciprocals:

$$
\tan x=1.
$$

So

$$
x=\frac{\pi}{4},\ \frac{5\pi}{4}.
$$

To 3 significant figures:

$$
x=0.785,\ 3.93.
$$

Therefore

$$
x=0.785,\ 2.55,\ 3.93,\ 5.70
$$

to 3 significant figures, listed in ascending order.

## Inverse Trig Functions

### Why restrictions are needed

To find an inverse function, the original function must be one-to-one on the chosen domain.

The graph of

$$
y=\sin x
$$

is not one-to-one over all real $x$, so it must be restricted before forming

$$
y=\arcsin x.
$$

### Standard inverse trig domains and ranges

| Function | Domain | Range |
|---|---|---|
| $y=\arcsin x$ | $-1\le x\le 1$ | $-\frac{\pi}{2}\le y\le \frac{\pi}{2}$ |
| $y=\arccos x$ | $-1\le x\le 1$ | $0\le y\le \pi$ |
| $y=\arctan x$ | $x\in\mathbb R$ | $-\frac{\pi}{2}<y<\frac{\pi}{2}$ |

The graph of $y=\arctan x$ has horizontal asymptotes:

$$
y=\frac{\pi}{2}
\quad\text{and}\quad
y=-\frac{\pi}{2}.
$$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-002 | Source: Chapter 6 PDF pages 25-26 | Insert from svg/A21TrigonometricFunctionsSVG-002.svg | Purpose: Show inverse trig graphs as reflections in $y=x$ with restricted domains/ranges.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-004 | Source: Chapter 6 inverse trig functions evidence | Insert from mermaid/A21TrigonometricFunctionsMermaid-004.md | Purpose: Explain why inverse trig graphs require restricted original domains.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-004 | Source: Chapter 6 inverse trig evidence | Insert from tikz/A21TrigonometricFunctionsTikZ-004.tex | Purpose: Show domain/range swapping for inverse trig functions.]

[INTERACTIVE PLACEHOLDER: A21TrigonometricFunctionsWidget-002 | Source: Chapter 6 inverse trig evidence | Insert from widgets/A21TrigonometricFunctionsWidget-002.html | Purpose: Explore inverse trig restrictions and reflections.]

### Evaluating inverse trig functions

#### Example: Evaluate $\arcsin\left(-\frac{\sqrt2}{2}\right)$

We need the angle in the arcsin range

$$
-\frac{\pi}{2}\le y\le \frac{\pi}{2}
$$

whose sine is

$$
-\frac{\sqrt2}{2}.
$$

That angle is

$$
-\frac{\pi}{4}.
$$

So

$$
\arcsin\left(-\frac{\sqrt2}{2}\right)
=
-\frac{\pi}{4}.
$$

#### Example: Evaluate $\arccos(-1)$

We need the angle in

$$
0\le y\le \pi
$$

whose cosine is $-1$.

That angle is

$$
\pi.
$$

So

$$
\arccos(-1)=\pi.
$$

#### Example: Evaluate $\arctan(\sqrt3)$

We need the angle in

$$
-\frac{\pi}{2}<y<\frac{\pi}{2}
$$

whose tangent is $\sqrt3$.

That angle is

$$
\frac{\pi}{3}.
$$

So

$$
\arctan(\sqrt3)=\frac{\pi}{3}.
$$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsSVG-003 | Source: Chapter 6 notation warning | Insert from svg/A21TrigonometricFunctionsSVG-003.svg | Purpose: Summarise the notation distinction between $\cos^2x$, $\cos^{-1}x$ and $\sec x$.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-005 | Source: Chapter 6 notation warning | Insert from mermaid/A21TrigonometricFunctionsMermaid-005.md | Purpose: Prevent confusion between inverse trig notation and reciprocal trig notation.]

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsTikZ-002 | Source: Chapter 6 notation warning | Insert from tikz/A21TrigonometricFunctionsTikZ-002.tex | Purpose: Distinguish squared trig, inverse trig and reciprocal trig notation.]

## Guided Practice

### Practice Question 1

Simplify

$$
\cos\theta\sin\theta(\cot\theta+\tan\theta).
$$

### Practice Question 2

Simplify

$$
\sec a-\sec a\sin^2a.
$$

### Practice Question 3

Prove

$$
(1+\cos x)(\cosec x-\cot x)\equiv \sin x.
$$

### Practice Question 4

Solve

$$
\cosec 3\theta=2,\qquad 0^\circ\le \theta<360^\circ.
$$

### Practice Question 5

Solve

$$
2\cosec^2x+\cot x=5,\qquad 0\le x<2\pi,
$$

giving your answers to 3 significant figures.

### Practice Question 6

Prove

$$
\frac{\sin x}{1-\cos x}
+
\frac{1-\cos x}{\sin x}
\equiv
2\cosec x.
$$

## Common Mistakes and Exam Traps

### Mistake 1: Thinking $\cos^{-1}x=\dfrac{1}{\cos x}$

Wrong:

$$
\cos^{-1}x=\frac{1}{\cos x}.
$$

Correct:

$$
\cos^{-1}x=\arccos x.
$$

Correct reciprocal notation:

$$
\sec x=\frac{1}{\cos x}.
$$

### Mistake 2: Cancelling across addition

You may cancel factors only when they multiply the whole numerator and denominator.

Allowed:

$$
\frac{4\times 5}{3\times 5}
=
\frac43.
$$

Not allowed:

$$
\frac{4+5}{4\times 5}
\ne
\frac{1+1}{1\times 1}.
$$

### Mistake 3: Forgetting to change the interval for $2\theta$ or $3\theta$

If

$$
0^\circ\le \theta<360^\circ,
$$

then

$$
0^\circ\le 3\theta<1080^\circ.
$$

Solve for $3\theta$ first, then divide answers by $3$.

### Mistake 4: Reciprocating zero

You cannot do

$$
\frac{1}{0}.
$$

So for

$$
\cot\theta=0,
$$

do not write

$$
\tan\theta=\frac{1}{0}
$$

as a normal number. Instead, interpret it as tangent being undefined, which occurs at the tangent graph’s asymptotes.

### Mistake 5: Misremembering the new identities

Correct:

$$
1+\tan^2x=\sec^2x.
$$

Correct:

$$
1+\cot^2x=\cosec^2x.
$$

Wrong:

$$
1+\sec^2x=\tan^2x.
$$

## Exam Technique Notes

1. For a proof, usually start with the messier side and work toward the neater side.
2. Convert $\sec$, $\cosec$ and $\cot$ into sine and cosine unless a new identity is clearly waiting to be used.
3. If a question has algebraic fractions, combine them into one fraction before trying to simplify.
4. Write a clear chain of equalities. Avoid arrows scattered around the page.
5. In solving questions, convert reciprocal trig equations into ordinary $\sin$, $\cos$ or $\tan$ equations.
6. If the equation contains $2\theta$ or $3\theta$, change the interval before solving.
7. In final answers, list solutions in increasing order.
8. Check whether the question asks for degrees, radians, exact values or decimal values.
9. For inverse trig graphs, remember: restrict the original trig graph, then reflect in

   $$
   y=x.
   $$

[VISUAL PLACEHOLDER: A21TrigonometricFunctionsMermaid-003 | Source: Chapter 6 reciprocal-trig equation examples | Insert from mermaid/A21TrigonometricFunctionsMermaid-003.md | Purpose: Show the solving process for sec, cosec and cot equations.]

## Full Worked Solutions to Guided Practice

### Solution 1

Simplify

$$
\cos\theta\sin\theta(\cot\theta+\tan\theta).
$$

Convert:

$$
\cot\theta=\frac{\cos\theta}{\sin\theta},
$$

$$
\tan\theta=\frac{\sin\theta}{\cos\theta}.
$$

So

$$
\cos\theta\sin\theta(\cot\theta+\tan\theta)
=
\cos\theta\sin\theta
\left(
\frac{\cos\theta}{\sin\theta}
+
\frac{\sin\theta}{\cos\theta}
\right).
$$

Combine:

$$
\frac{\cos\theta}{\sin\theta}
+
\frac{\sin\theta}{\cos\theta}
=
\frac{\cos^2\theta+\sin^2\theta}{\sin\theta\cos\theta}.
$$

Substitute:

$$
=
\cos\theta\sin\theta
\left(
\frac{\cos^2\theta+\sin^2\theta}{\sin\theta\cos\theta}
\right).
$$

Cancel:

$$
=
\cos^2\theta+\sin^2\theta.
$$

Use

$$
\sin^2\theta+\cos^2\theta=1.
$$

So

$$
\cos\theta\sin\theta(\cot\theta+\tan\theta)=1.
$$

### Solution 2

Simplify

$$
\sec a-\sec a\sin^2a.
$$

Convert $\sec a$:

$$
=
\frac{1}{\cos a}
-
\frac{\sin^2a}{\cos a}.
$$

Combine:

$$
=
\frac{1-\sin^2a}{\cos a}.
$$

Use

$$
1-\sin^2a=\cos^2a.
$$

So

$$
=
\frac{\cos^2a}{\cos a}.
$$

Cancel:

$$
=
\cos a.
$$

### Solution 3

Prove

$$
(1+\cos x)(\cosec x-\cot x)\equiv \sin x.
$$

Start with the left-hand side:

$$
\text{LHS}
=
(1+\cos x)(\cosec x-\cot x).
$$

Expand:

$$
=
\cosec x-\cot x+\cos x\cosec x-\cos x\cot x.
$$

Convert terms:

$$
\cosec x=\frac{1}{\sin x},
$$

$$
\cot x=\frac{\cos x}{\sin x},
$$

$$
\cos x\cosec x=\cos x\cdot \frac{1}{\sin x}
=
\frac{\cos x}{\sin x}
=
\cot x,
$$

$$
\cos x\cot x
=
\cos x\cdot \frac{\cos x}{\sin x}
=
\frac{\cos^2x}{\sin x}.
$$

So

$$
\text{LHS}
=
\frac{1}{\sin x}
-
\cot x
+
\cot x
-
\frac{\cos^2x}{\sin x}.
$$

Cancel $-\cot x+\cot x$:

$$
=
\frac{1}{\sin x}
-
\frac{\cos^2x}{\sin x}.
$$

Combine:

$$
=
\frac{1-\cos^2x}{\sin x}.
$$

Use

$$
1-\cos^2x=\sin^2x.
$$

So

$$
=
\frac{\sin^2x}{\sin x}
=
\sin x.
$$

Hence

$$
(1+\cos x)(\cosec x-\cot x)\equiv \sin x.
$$

### Solution 4

This is Worked Example 8:

$$
\theta=10^\circ,\ 50^\circ,\ 130^\circ,\ 170^\circ,\ 250^\circ,\ 290^\circ.
$$

### Solution 5

This is Worked Example 11:

$$
x=0.785,\ 2.55,\ 3.93,\ 5.70
$$

to 3 significant figures.

### Solution 6

Prove

$$
\frac{\sin x}{1-\cos x}
+
\frac{1-\cos x}{\sin x}
\equiv
2\cosec x.
$$

Start with the left-hand side:

$$
\text{LHS}
=
\frac{\sin x}{1-\cos x}
+
\frac{1-\cos x}{\sin x}.
$$

Common denominator:

$$
\sin x(1-\cos x).
$$

So

$$
\text{LHS}
=
\frac{\sin x\cdot \sin x+(1-\cos x)(1-\cos x)}
{\sin x(1-\cos x)}.
$$

That is

$$
=
\frac{\sin^2x+(1-\cos x)^2}
{\sin x(1-\cos x)}.
$$

Expand:

$$
(1-\cos x)^2
=
1-2\cos x+\cos^2x.
$$

So

$$
=
\frac{\sin^2x+1-2\cos x+\cos^2x}
{\sin x(1-\cos x)}.
$$

Group:

$$
=
\frac{\sin^2x+\cos^2x+1-2\cos x}
{\sin x(1-\cos x)}.
$$

Use

$$
\sin^2x+\cos^2x=1.
$$

So

$$
=
\frac{1+1-2\cos x}
{\sin x(1-\cos x)}.
$$

Simplify:

$$
=
\frac{2-2\cos x}
{\sin x(1-\cos x)}.
$$

Factorise the numerator:

$$
=
\frac{2(1-\cos x)}
{\sin x(1-\cos x)}.
$$

Cancel $1-\cos x$:

$$
=
\frac{2}{\sin x}.
$$

Use

$$
\cosec x=\frac{1}{\sin x}.
$$

Therefore

$$
=
2\cosec x.
$$

Hence

$$
\frac{\sin x}{1-\cos x}
+
\frac{1-\cos x}{\sin x}
\equiv
2\cosec x.
$$

## Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “Prove that …” | Start from one side, usually the messier side, and transform it into the other. |
| “Solve for $0\le x<2\pi$ …” | Work in radians, find all values in the interval and list in increasing order. |
| “Giving your solutions to 3 s.f.” | Use decimals and round final answers to 3 significant figures. |
| “State the number of solutions” | Use graph intersections or range arguments. |
| “Hence explain why …” | Use the result from the previous part. Do not start from scratch unless necessary. |
| “Sketch” | Show key asymptotes, intercepts/turning points, domain restrictions and shape. |

## Syllabus Gap Check

| Item | Status |
|---|---|
| Reciprocal trig definitions | Covered |
| Reciprocal/inverse notation warning | Covered |
| Exact reciprocal trig values | Covered |
| Graphs of $\sec$, $\cosec$, $\cot$ | Covered with placeholders |
| Domains and ranges | Covered |
| Solving reciprocal trig equations | Covered |
| New identities $1+\tan^2x=\sec^2x$ and $1+\cot^2x=\cosec^2x$ | Covered |
| Proofs involving reciprocal trig functions | Covered |
| Inverse trig functions and restricted domains | Covered |
| CCEA contextual trig problem solving | Not covered because no evidence supplied |
| Compound/double-angle formulae | Not covered, belongs elsewhere in A21-TRIG |
| Small-angle approximation | Excluded from core, boundary risk logged |

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A21TrigonometricFunctionsSVG-001 | SVG | Reciprocal graph comparison: $\sin/\cosec$, $\cos/\sec$, $\tan/\cot$. |
| A21TrigonometricFunctionsSVG-002 | SVG | Inverse trig graphs from reflection in $y=x$. |
| A21TrigonometricFunctionsSVG-003 | SVG | Notation warning: squared, inverse and reciprocal trig notation. |
| A21TrigonometricFunctionsTikZ-001 | TikZ | Derivation of reciprocal Pythagorean identities. |
| A21TrigonometricFunctionsTikZ-002 | TikZ | Notation warning. |
| A21TrigonometricFunctionsTikZ-003 | TikZ | Reciprocal graph behaviour from $y=f(x)$ to $y=\frac1{f(x)}$. |
| A21TrigonometricFunctionsTikZ-004 | TikZ | Domain/range swap for inverse trig functions. |
| A21TrigonometricFunctionsTikZ-005 | TikZ | Reciprocal trig identity proof route. |
| A21TrigonometricFunctionsMermaid-001 | Mermaid | Identity derivation flowchart. |
| A21TrigonometricFunctionsMermaid-002 | Mermaid | Proof strategy flowchart. |
| A21TrigonometricFunctionsMermaid-003 | Mermaid | Solving reciprocal trig equations. |
| A21TrigonometricFunctionsMermaid-004 | Mermaid | Inverse trig restriction logic. |
| A21TrigonometricFunctionsMermaid-005 | Mermaid | Notation trap flowchart. |
| A21TrigonometricFunctionsMermaid-006 | Mermaid | Reciprocal graph behaviour. |
| A21TrigonometricFunctionsWidget-001 | HTML widget | Toggle original trig graph and reciprocal graph. |
| A21TrigonometricFunctionsWidget-002 | HTML widget | Explore inverse trig graph restrictions and reflections. |

## Supplementary Sources Used

| Source | Status |
|---|---|
| DrFrost/Pearson-style Chapter 6 PDF | Cross-board/third-party support; used only where matching CCEA A21-TRIG. |
| Edexcel C3 examples inside slide deck | Cross-board examples; used only for on-spec reciprocal trig methods. |
| Pearson exercise references | Logged as source labels only; no unseen textbook content is claimed. |
| Screenshot PDF | Visual backup only; no unparsed detail is invented. |

## Final Student Checklist

Before moving on, the student should be able to tick every item:

- [ ] I know that $\sec x=\dfrac1{\cos x}$.
- [ ] I know that $\cosec x=\dfrac1{\sin x}$.
- [ ] I know that $\cot x=\dfrac1{\tan x}=\dfrac{\cos x}{\sin x}$.
- [ ] I do not confuse $\cos^{-1}x$ with $\dfrac1{\cos x}$.
- [ ] I can evaluate exact values such as $\sec\frac{\pi}{4}$ and $\cosec\frac{5\pi}{6}$.
- [ ] I can explain why reciprocal trig graphs have asymptotes.
- [ ] I know the domains and ranges of $\sec x$, $\cosec x$ and $\cot x$.
- [ ] I can solve equations involving $\sec$, $\cosec$ and $\cot$.
- [ ] I can derive $1+\tan^2x=\sec^2x$.
- [ ] I can derive $1+\cot^2x=\cosec^2x$.
- [ ] I can prove reciprocal trig identities using sine/cosine conversion and algebraic fractions.
- [ ] I can explain why inverse trig functions need restricted domains.
- [ ] I can evaluate simple inverse trig values in radians.
