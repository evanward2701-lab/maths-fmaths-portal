# A21 Numerical Methods

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-NUM |
| Topic name | Numerical methods |
| Topic slug | numerical_methods |
| Topic Pascal | NumericalMethods |
| Topic ID | A21NumericalMethods |
| Lesson file | A21_numerical_methods_lesson.md |
| Date generated | 2026-06-06 |

## Learning Outcome IDs

- A21-NUM-LO001
- A21-NUM-LO002
- A21-NUM-LO003
- A21-NUM-LO004

## Evidence Map

| Evidence | Used for | Role |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic, LO IDs and boundary | Authority |
| README Module Map | Topic identity and file conventions | Supporting metadata |
| Evidence Drop Checklist | Missing evidence and visual rules | Workflow authority |
| Chapter 10 Numerical Methods Transcript | Roots, iteration, Newton-Raphson, modelling | Core lesson evidence where on-spec |
| P2 Chapter 10 Numerical Methods PDF/slides | Visual planning and worked-example support | Core visual/text evidence where on-spec |
| Screenshots PDF | Visual support only | No parsed text available |
| Pearson/Edexcel-labelled examples in evidence | Worked examples and practice models | Cross-board support only where matching CCEA |

## Specification Alignment

| LO ID | Official learning outcome | Lesson coverage |
|---|---|---|
| A21-NUM-LO001 | Locate roots of \(f(x)=0\) by considering changes of sign of \(f(x)\) in an interval of \(x\) in which \(f(x)\) is continuous. | Covered through sign-change tests, continuity warnings and accuracy intervals. |
| A21-NUM-LO002 | Solve equations approximately using simple iterative methods, for example the Newton-Raphson method. | Covered through \(x=g(x)\), iteration, convergence, staircase/cobweb diagrams and Newton-Raphson. |
| A21-NUM-LO003 | Demonstrate understanding of and use numerical integration of functions via the trapezium rule, including finding the approximate area under a curve. | Required by CCEA, but lesson evidence missing. Logged as a gap with placeholder-only assets. |
| A21-NUM-LO004 | Use numerical methods to solve problems in context. | Partly covered through contextual modelling and model criticism. |

## Learning Objectives

By the end of this lesson the student should be able to:

1. Explain that a root of \(f(x)\) is a solution of \(f(x)=0\).
2. Prove that a root lies in an interval using a sign change and continuity.
3. Prove that a root is correct to a required number of decimal places.
4. Interpret roots graphically as \(x\)-axis crossings and intersections of graphs.
5. Rearrange \(f(x)=0\) into \(x=g(x)\).
6. Generate terms using \(x_{n+1}=g(x_n)\).
7. Recognise convergence, divergence, oscillation and non-convergence.
8. Interpret staircase and cobweb diagrams.
9. Apply \(x_{n+1}=x_n-rac{f(x_n)}{f'(x_n)}\).
10. Explain Newton-Raphson using tangents.
11. Recognise failure cases such as \(f'(x_n)=0\).
12. Apply numerical methods in a contextual model and criticise the model.
13. State that the trapezium rule is required by CCEA but remains evidence-pending in this pack.

## Prerequisite Recap

This pack does not use GCSE sources. Required prior A-Level/general skills are function notation, solving equations, graph interpretation, logarithms, exponentials, differentiation, straight-line equations and calculator fluency.

## Big Picture Explanation

Numerical methods are used when exact algebra is ugly, inefficient or impossible. A root of \(f(x)\) is an input such that

\[
f(x)=0.
\]

For some equations, such as

\[
x-\cos x=0,
\]

there is no ordinary exact algebraic expression for the solution. Numerical methods build increasingly accurate approximations instead.

The core methods in this evidence are sign-change location, iteration, staircase/cobweb diagrams, Newton-Raphson and contextual modelling. CCEA also requires trapezium rule, but the uploaded evidence did not teach it fully.

## Key Definitions and Notation

### Root

A root of \(f(x)\) is a value of \(x\) such that

\[
f(x)=0.
\]

Graphically, this is where \(y=f(x)\) meets the \(x\)-axis.

### Continuous function

A function is continuous over an interval if the graph does not jump or break over that interval. For this topic, the key point is that sign-change arguments only guarantee a root when the function is continuous on the interval.

### Sign change

There is a change in sign between \(x=a\) and \(x=b\) if \(f(a)\) and \(f(b)\) have opposite signs. If \(f\) is continuous on \([a,b]\), a sign change guarantees at least one root in the interval.

### Iteration

If an equation is rearranged into

\[
x=g(x),
\]

then an iterative formula is

\[
x_{n+1}=g(x_n).
\]

### Newton-Raphson

Newton-Raphson uses

\[
x_{n+1}=x_n-rac{f(x_n)}{f'(x_n)}.
\]

It uses the tangent at the current point to generate the next approximation.

---

# Core Theory

## 1. Locating roots by sign change

To show that \(f(x)=0\) has a root between \(x=a\) and \(x=b\):

1. Calculate \(f(a)\).
2. Calculate \(f(b)\).
3. Show they have opposite signs.
4. State that \(f(x)\) is continuous.
5. Conclude that a root lies in the interval.

Exam-safe conclusion:

\[
oxed{	ext{There is a change in sign and }f(x)	ext{ is continuous, so a root lies in the interval.}}
\]

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-001 | Source: Chapter 10 evidence | Insert from svg/A21NumericalMethodsSVG-001.svg | Purpose: Show continuous graph crossing the \(x\)-axis between endpoints.]

## 2. Worked sign-change example

Show that

\[
f(x)=e^x+2x-3
\]

has a root between \(x=0.5\) and \(x=0.6\).

\[
f(0.5)=e^{0.5}+2(0.5)-3.
\]

\[
2(0.5)=1.
\]

\[
f(0.5)=e^{0.5}+1-3=e^{0.5}-2.
\]

\[
f(0.5)=-0.35127\ldots<0.
\]

\[
f(0.6)=e^{0.6}+2(0.6)-3.
\]

\[
2(0.6)=1.2.
\]

\[
f(0.6)=e^{0.6}+1.2-3=e^{0.6}-1.8.
\]

\[
f(0.6)=0.02211\ldots>0.
\]

There is a change in sign. Since \(f(x)=e^x+2x-3\) is continuous, there is a root between \(0.5\) and \(0.6\).

## 3. Why continuity is required

For

\[
f(x)=rac1x,
\]

\[
f(-1)=-1,\qquad f(1)=1.
\]

There is a sign change, but no root in \([-1,1]\), because \(f(x)=1/x\) is not continuous at \(x=0\). It has a vertical asymptote and jumps from negative to positive without crossing zero.

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-002 | Source: Chapter 10 continuity warning | Insert from svg/A21NumericalMethodsSVG-002.svg | Purpose: Show \(1/x\) sign-change trap.]

## 4. No sign change does not mean no root

If \(f(a)\) and \(f(b)\) have the same sign, there may still be roots inside the interval. An even number of roots can be hidden between the endpoints.

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-003 | Source: Chapter 10 warning | Insert from svg/A21NumericalMethodsSVG-003.svg | Purpose: Show two hidden roots with matching endpoint signs.]

## 5. Proving a root to a given accuracy

To prove that \(lpha=2.307\) correct to 3 d.p., use

\[
2.3065<lpha<2.3075.
\]

For

\[
g(x)=e^{x-1}+x-6,
\]

\[
g(2.3065)=e^{2.3065-1}+2.3065-6=e^{1.3065}+2.3065-6.
\]

\[
g(2.3065)=-2.75\ldots	imes10^{-4}<0.
\]

\[
g(2.3075)=e^{2.3075-1}+2.3075-6=e^{1.3075}+2.3075-6.
\]

\[
g(2.3075)=4.419\ldots	imes10^{-3}>0.
\]

There is a change in sign in \((2.3065,2.3075)\). Since \(g(x)\) is continuous,

\[
2.3065<lpha<2.3075.
\]

Therefore

\[
oxed{lpha=2.307	ext{ correct to 3 decimal places}.}
\]

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-004 | Source: Chapter 10 accuracy example | Insert from svg/A21NumericalMethodsSVG-004.svg | Purpose: Show rounding interval.]

## 6. Roots as intersections

For

\[
f(x)=\ln x-rac1x,
\]

a root satisfies

\[
\ln x-rac1x=0.
\]

Add \(rac1x\):

\[
\ln x=rac1x.
\]

So the root corresponds to the intersection of \(y=\ln x\) and \(y=rac1x\).

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-005 | Source: Chapter 10 graph-intersection example | Insert from svg/A21NumericalMethodsSVG-005.svg | Purpose: Show \(\ln x=1/x\) as graph intersection.]

## 7. Iteration

To solve \(f(x)=0\) by iteration, rearrange into

\[
x=g(x)
\]

and use

\[
x_{n+1}=g(x_n).
\]

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-006 | Source: Chapter 10 iteration explanation | Insert from svg/A21NumericalMethodsSVG-006.svg | Purpose: Show iteration machine.]

## 8. Rearranging into iterative form

For

\[
g(x)=e^{x-1}+x-6,
\]

start with

\[
e^{x-1}+x-6=0.
\]

Move \(x-6\) to the other side:

\[
e^{x-1}=6-x.
\]

Take natural logarithms:

\[
\ln(e^{x-1})=\ln(6-x).
\]

\[
x-1=\ln(6-x).
\]

Add 1:

\[
x=\ln(6-x)+1.
\]

So

\[
oxed{x_{n+1}=\ln(6-x_n)+1.}
\]

## 9. Using an iterative formula

Given

\[
x_{n+1}=\ln(6-x_n)+1,\qquad x_0=2,
\]

\[
x_1=\ln(6-x_0)+1=\ln(6-2)+1=\ln4+1=2.3863\ldots
\]

\[
x_1=2.3863.
\]

Using the unrounded calculator value:

\[
x_2=2.2847,\qquad x_3=2.3125,\qquad x_4=2.3050.
\]

The values are getting closer together, so the iteration appears to converge.

## 10. Convergence, divergence and non-convergence

If \(x_0,x_1,x_2,\ldots\) get closer to one value, the iteration is convergent. If they move further apart, it is divergent. If they bounce between values or do not settle, it is oscillating, periodic or non-convergent.

## 11. Staircase and cobweb diagrams

For \(x_{n+1}=g(x_n)\), compare \(y=g(x)\) with \(y=x\). The construction rule is:

\[
oxed{	ext{curve, line, curve, line}.}
\]

Moving towards the intersection means convergence. Moving away means divergence.

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-007 | Source: Chapter 10 staircase/cobweb explanation | Insert from svg/A21NumericalMethodsSVG-007.svg | Purpose: Show construction process.]

## 12. Newton-Raphson method

Newton-Raphson uses tangents. Starting from \(x_n\), draw the tangent at \((x_n,f(x_n))\). The tangent’s \(x\)-axis crossing gives \(x_{n+1}\).

\[
oxed{x_{n+1}=x_n-rac{f(x_n)}{f'(x_n)}.}
\]

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-008 | Source: Chapter 10 Newton-Raphson evidence | Insert from svg/A21NumericalMethodsSVG-008.svg | Purpose: Show tangent method.]

## 13. Deriving Newton-Raphson

At \(x=x_n\), the point is

\[
(x_n,f(x_n)).
\]

The tangent gradient is

\[
f'(x_n).
\]

Using

\[
y-y_1=m(x-x_1),
\]

the tangent is

\[
y-f(x_n)=f'(x_n)(x-x_n).
\]

At the tangent’s \(x\)-axis crossing,

\[
y=0,\qquad x=x_{n+1}.
\]

Substitute:

\[
0-f(x_n)=f'(x_n)(x_{n+1}-x_n).
\]

\[
-f(x_n)=f'(x_n)(x_{n+1}-x_n).
\]

Divide by \(f'(x_n)\):

\[
-rac{f(x_n)}{f'(x_n)}=x_{n+1}-x_n.
\]

Add \(x_n\):

\[
x_{n+1}=x_n-rac{f(x_n)}{f'(x_n)}.
\]

## 14. Newton-Raphson failure

If

\[
f'(x_n)=0,
\]

then Newton-Raphson requires division by zero:

\[
x_{n+1}=x_n-rac{f(x_n)}{0}.
\]

Graphically, the tangent is horizontal and may not give a usable next approximation.

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-009 | Source: Chapter 10 failure examples | Insert from svg/A21NumericalMethodsSVG-009.svg | Purpose: Show horizontal tangent failure.]

## 15. Trapezium-rule syllabus gap

A21-NUM-LO003 requires the trapezium rule. The uploaded evidence did not fully teach it, so this pack includes placeholder-only assets and logs the strand as incomplete.

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-010 | Source: CCEA specification only | Insert from svg/A21NumericalMethodsSVG-010.svg | Purpose: Evidence-pending trapezium rule visual.]

[INTERACTIVE PLACEHOLDER: A21NumericalMethodsWidget-001 | Source: CCEA specification only | Insert from widgets/A21NumericalMethodsWidget-001.html | Purpose: Evidence-pending trapezium rule widget scaffold.]

---

# Worked Examples

## Worked Example 1: \(\ln x-rac1x\)

For

\[
f(x)=\ln x-rac1x,
\]

show the root lies in \(1.7<x<1.8\) and equals \(1.763\) correct to 3 d.p.

\[
f(1.7)=\ln(1.7)-rac1{1.7}=-0.0576\ldots<0.
\]

\[
f(1.8)=\ln(1.8)-rac1{1.8}=0.0322\ldots>0.
\]

There is a change in sign. Since \(f(x)\) is continuous for \(x>0\), the root lies in \(1.7<x<1.8\).

For 3 d.p. bounds:

\[
f(1.7625)=\ln(1.7625)-rac1{1.7625}=-6.4\ldots	imes10^{-4}<0.
\]

\[
f(1.7635)=\ln(1.7635)-rac1{1.7635}=2.46\ldots	imes10^{-4}>0.
\]

So

\[
1.7625<lpha<1.7635
\]

and

\[
oxed{lpha=1.763	ext{ correct to 3 decimal places}.}
\]

## Worked Example 2: Harder rearrangement

Show that

\[
x^3+3x^2+4x-12=0
\]

can be rearranged as

\[
x=\sqrt{rac{4(3-x)}{3+x}}.
\]

\[
x^3+3x^2+4x-12=0
\]

\[
x^3+3x^2=12-4x
\]

\[
x^2(x+3)=4(3-x)
\]

\[
x^2=rac{4(3-x)}{x+3}
\]

\[
x^2=rac{4(3-x)}{3+x}
\]

\[
oxed{x=\sqrt{rac{4(3-x)}{3+x}}.}
\]

## Worked Example 3: Newton-Raphson for \(x-\cos x=0\)

Let

\[
f(x)=x-\cos x.
\]

Then

\[
f'(x)=1+\sin x.
\]

Newton-Raphson gives

\[
x_{n+1}=x_n-rac{x_n-\cos x_n}{1+\sin x_n}.
\]

Starting with \(x_0=0.5\):

\[
x_1=0.5-rac{0.5-\cos(0.5)}{1+\sin(0.5)}=0.7552\ldots
\]

\[
x_2=0.7391\ldots
\]

So the root is approximately

\[
oxed{x=0.7391}.
\]

Use radians.

## Worked Example 4: Newton-Raphson recurrence

For

\[
f(x)=2x^3+x^2-1,
\]

\[
f'(x)=6x^2+2x.
\]

\[
x_{n+1}=x_n-rac{2x_n^3+x_n^2-1}{6x_n^2+2x_n}.
\]

Put over a common denominator:

\[
x_n=rac{x_n(6x_n^2+2x_n)}{6x_n^2+2x_n}.
\]

\[
x_{n+1}=rac{x_n(6x_n^2+2x_n)-(2x_n^3+x_n^2-1)}{6x_n^2+2x_n}.
\]

\[
x_{n+1}=rac{6x_n^3+2x_n^2-2x_n^3-x_n^2+1}{6x_n^2+2x_n}.
\]

\[
oxed{x_{n+1}=rac{4x_n^3+x_n^2+1}{6x_n^2+2x_n}.}
\]

If \(x_n=0\),

\[
f'(0)=6(0)^2+2(0)=0.
\]

Newton-Raphson cannot be used because it would divide by zero.

## Worked Example 5: Contextual car-value model

The price of a car, in pounds, \(x\) years after purchase is modelled by

\[
f(x)=15000(0.85)^x-1000\sin x.
\]

Value after 10 years:

\[
f(10)=15000(0.85)^{10}-1000\sin(10)=3497\ldots
\]

So

\[
oxed{f(10)pprox £3500}
\]

to the nearest hundred pounds.

Root between 19 and 20:

\[
f(19)=15000(0.85)^{19}-1000\sin(19)=534.11\ldots>0.
\]

\[
f(20)=15000(0.85)^{20}-1000\sin(20)=-331.55\ldots<0.
\]

There is a change in sign and \(f(x)\) is continuous, so a root lies between 19 and 20.

Derivative:

\[
f'(x)=15000(0.85)^x\ln(0.85)-1000\cos x.
\]

Newton-Raphson from \(x_0=19.5\):

\[
x_1=19.5-rac{15000(0.85)^{19.5}-1000\sin(19.5)}{15000(0.85)^{19.5}\ln(0.85)-1000\cos(19.5)}.
\]

\[
x_1=19.528\ldots
\]

The model predicts negative value near \(x=20\), which is unrealistic. Therefore the model is not valid for all large \(x\).

[VISUAL PLACEHOLDER: A21NumericalMethodsSVG-011 | Source: CCEA A21-NUM-LO004 + contextual example | Insert from svg/A21NumericalMethodsSVG-011.svg | Purpose: Show modelling cycle.]

---

# Guided Practice

1. Show that \(f(x)=x^3-4x^2+3x+1\) has a root between \(x=1.4\) and \(x=1.5\).
2. Given \(f(3.245)<0\) and \(f(3.255)>0\), explain why the root is \(3.25\) correct to 2 d.p.
3. Use \(x_{n+1}=\sqrt{x_n+1}\), \(x_0=1\), to find \(x_1,x_2,x_3\) to 4 d.p.
4. For \(f(x)=x^2\sin x+x-3\), find the Newton-Raphson recurrence relation.
5. For \(f(x)=3x^2-rac{11}{x^2}\), use Newton-Raphson once from \(x_0=1.4\).
6. Explain why Newton-Raphson fails if \(f'(x_n)=0\).

---

# Full Worked Solutions to Guided Practice

## Solution 1

\[
f(1.4)=(1.4)^3-4(1.4)^2+3(1.4)+1.
\]

\[
(1.4)^3=2.744,\quad (1.4)^2=1.96,\quad -4(1.96)=-7.84,\quad 3(1.4)=4.2.
\]

\[
f(1.4)=2.744-7.84+4.2+1=0.104>0.
\]

\[
f(1.5)=(1.5)^3-4(1.5)^2+3(1.5)+1.
\]

\[
(1.5)^3=3.375,\quad (1.5)^2=2.25,\quad -4(2.25)=-9,\quad 3(1.5)=4.5.
\]

\[
f(1.5)=3.375-9+4.5+1=-0.125<0.
\]

There is a change in sign. Since \(f(x)\) is continuous, a root lies in \((1.4,1.5)\).

## Solution 2

Since

\[
f(3.245)<0,\qquad f(3.255)>0,
\]

there is a change in sign in \((3.245,3.255)\). Since \(f(x)\) is continuous,

\[
3.245<lpha<3.255.
\]

Every value in this interval rounds to \(3.25\) to 2 d.p. Therefore

\[
oxed{lpha=3.25	ext{ correct to 2 d.p.}}
\]

## Solution 3

\[
x_1=\sqrt{1+1}=\sqrt2=1.414213\ldots
\]

\[
x_1=1.4142.
\]

\[
x_2=\sqrt{x_1+1}=1.553773\ldots=1.5538.
\]

\[
x_3=\sqrt{x_2+1}=1.598053\ldots=1.5981.
\]

## Solution 4

\[
f(x)=x^2\sin x+x-3.
\]

Using the product rule,

\[
rac{d}{dx}(x^2\sin x)=x^2\cos x+2x\sin x.
\]

So

\[
f'(x)=x^2\cos x+2x\sin x+1.
\]

Newton-Raphson:

\[
oxed{x_{n+1}=x_n-rac{x_n^2\sin x_n+x_n-3}{x_n^2\cos x_n+2x_n\sin x_n+1}.}
\]

## Solution 5

\[
f(x)=3x^2-rac{11}{x^2}=3x^2-11x^{-2}.
\]

\[
f'(x)=6x+22x^{-3}.
\]

\[
x_1=1.4-rac{3(1.4)^2-11(1.4)^{-2}}{6(1.4)+22(1.4)^{-3}}.
\]

\[
oxed{x_1=1.384}
\]

to 3 d.p.

## Solution 6

Newton-Raphson uses

\[
x_{n+1}=x_n-rac{f(x_n)}{f'(x_n)}.
\]

If

\[
f'(x_n)=0,
\]

then the formula divides by zero. Graphically, the tangent is horizontal and does not give a usable next approximation.

---

# Common Mistakes and Exam Traps

- Forgetting to say \(f(x)\) is continuous.
- Claiming no sign change means no root.
- Testing the wrong function when intersections are involved.
- Rounding too early during iteration.
- Confusing \(x_0\) and \(x_1\).
- Using degrees instead of radians.
- Applying Newton-Raphson when \(f'(x_n)=0\).
- Assuming Newton-Raphson always converges to the intended root.

# Exam Technique

Use these sentence skeletons:

- “There is a change in sign and \(f(x)\) is continuous, so a root lies in the interval.”
- “Since the root lies between the lower and upper rounding bounds, it is equal to the stated value correct to the required accuracy.”
- “The values get closer together, so the iteration converges to the root.”
- “The method cannot be used because \(f'(x_n)=0\), causing division by zero.”

# Syllabus Gap Check

| LO ID | Status | Notes |
|---|---|---|
| A21-NUM-LO001 | Covered | Sign-change and continuity covered. |
| A21-NUM-LO002 | Covered | Iteration and Newton-Raphson covered. |
| A21-NUM-LO003 | Evidence gap | Trapezium rule required by CCEA, but lesson evidence missing. |
| A21-NUM-LO004 | Partly covered | Contextual modelling example included. |

# Visual and Interactive Asset Plan

Mermaid, SVG and TikZ assets are included in subfolders. The widget folder includes one evidence-locked trapezium-rule scaffold.

# Supplementary Sources Used

Cross-board Pearson/Edexcel-labelled examples embedded in the uploaded evidence were used only where they match the CCEA A21 Numerical Methods boundary.

# Final Student Checklist

- I can define a root as a solution of \(f(x)=0\).
- I can prove a root lies in an interval using signs and continuity.
- I can prove a root correct to a stated number of decimal places.
- I can rearrange an equation into \(x=g(x)\).
- I can use \(x_{n+1}=g(x_n)\).
- I can describe convergence and non-convergence.
- I can interpret staircase/cobweb diagrams.
- I can apply Newton-Raphson.
- I can explain why \(f'(x_n)=0\) causes failure.
- I can criticise a contextual model.
- I know trapezium rule is required but not complete in this evidence-backed pack.

# Progress Manifest

| Item | Status |
|---|---|
| Phase 0 | Completed |
| Phase 1 | Completed and written |
| Phase 2 | Completed and written |
| Phase 3 | Completed and written |
| Phase 4 | Completed and written |
| Phase 5 | Completed and written |
| Phase 6 | Completed and written |
| Final generation status | FILES_WRITTEN_AND_ZIPPED |
