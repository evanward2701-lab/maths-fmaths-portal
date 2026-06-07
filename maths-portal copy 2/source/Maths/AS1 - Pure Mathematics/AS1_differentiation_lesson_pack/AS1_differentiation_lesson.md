# AS1 Differentiation

- Course: CCEA GCE Mathematics
- Unit code: AS1
- Unit name: AS 1 Pure Mathematics
- Topic code: AS1-DIFF
- Topic name: Differentiation
- Topic slug: differentiation
- Topic Pascal: Differentiation
- Topic ID: AS1Differentiation
- Lesson file: AS1_differentiation_lesson.md
- Learning outcome IDs:
  - AS1-DIFF-LO001
  - AS1-DIFF-LO002
  - AS1-DIFF-LO003
  - AS1-DIFF-LO004
  - AS1-DIFF-LO005
  - AS1-DIFF-LO006
  - AS1-DIFF-LO007
  - AS1-DIFF-LO008

---

## Evidence Map

| Evidence | Role in this lesson |
|---|---|
| CCEA GCE Mathematics Specification Map | Authority for unit, topic, LO IDs and syllabus boundary. |
| README Module Map | Confirms topic identity and file conventions. |
| Evidence Drop Checklist | Controls missing evidence, off-spec logging and visual placeholders. |
| `P1-Chp12-Differentiation_RevealBlocksRemoved.pdf` | Main slide/PDF evidence for definitions, examples, warnings and diagrams. |
| `Chapter_12_Differentiation_🤖_(Pure_Year_1)_Transcript.md` | Teacher explanations, method details and warnings. |
| `Chapter_12_Differentiation_🤖_(Pure_Year_1)_Screenshots.pdf` | Visual support only; no parsed text was available. |

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| AS1-DIFF-LO001 | Derivative as the gradient function of \(y=f(x)\). |
| AS1-DIFF-LO002 | Secant-to-tangent limit idea and first principles formula. |
| AS1-DIFF-LO003 | Gradient as rate of change, including \(\frac{dV}{dt}\). |
| AS1-DIFF-LO004 | Finding \(\frac{d^2y}{dx^2}\) and \(f''(x)\). |
| AS1-DIFF-LO005 | Interpreting the second derivative as rate of change of gradient. |
| AS1-DIFF-LO006 | Differentiating \(x^n\) for rational \(n\), including roots, fractions, sums and differences. |
| AS1-DIFF-LO007 | Gradients, tangents, normals, stationary points, maxima, minima and optimisation. |
| AS1-DIFF-LO008 | Increasing and decreasing functions using the sign of \(f'(x)\). |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain why a curve needs a gradient function, not just one gradient.
2. Understand the derivative as a limit of gradients between nearby points.
3. Use first principles:
   \[
   f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
   \]
4. Differentiate powers of \(x\):
   \[
   \frac{d}{dx}(ax^n)=anx^{n-1}.
   \]
5. Rewrite roots, fractions and brackets into differentiable power form.
6. Find gradients at points on curves.
7. Find equations of tangents and normals.
8. Use \(f'(x)\) to identify stationary points and increasing/decreasing intervals.
9. Use \(f''(x)\) to classify stationary points where possible.
10. Apply differentiation to simple rate-of-change and optimisation problems.

---

## Prerequisite Recap

You should already be able to:

- find the gradient of a straight line;
- use \(y-y_1=m(x-x_1)\);
- expand brackets;
- simplify powers using index laws;
- rewrite roots as fractional powers;
- rewrite reciprocals as negative powers;
- solve linear and quadratic equations;
- solve simultaneous equations involving a line and a curve;
- substitute values into functions.

---

## Big Picture Explanation

Differentiation is one half of calculus. Its central question is:

> How steep is a curve at a point?

For a straight line such as

\[
y=3x+2,
\]

the gradient is always

\[
m=3.
\]

A straight line has one constant gradient.

For a curve such as

\[
y=x^2,
\]

the gradient varies. At \(x=-3\), \(x=-2\), \(x=-1\), \(x=0\), \(x=1\), \(x=2\), \(x=3\), the gradient values are:

\[
\begin{array}{c|rrrrrrr}
x & -3 & -2 & -1 & 0 & 1 & 2 & 3\\
\hline
\text{Gradient} & -6 & -4 & -2 & 0 & 2 & 4 & 6
\end{array}
\]

The pattern is:

\[
\text{Gradient}=2x.
\]

So the gradient function of \(y=x^2\) is:

\[
\frac{dy}{dx}=2x.
\]

---

## Key Definitions and Notation

### Gradient function

The gradient function gives the gradient of a curve at a general point.

For

\[
y=f(x),
\]

the gradient function is written as:

\[
f'(x)
\]

or

\[
\frac{dy}{dx}.
\]

### Derivative

The derivative is another name for the gradient function.

\[
\text{Derivative}=\text{gradient function}.
\]

### First principles formula

\[
\boxed{f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}}
\]

This means:

- take a point at \(x\);
- take another point very close to it at \(x+h\);
- find the gradient between them;
- let \(h\) tend towards \(0\), so the secant becomes the tangent.

### Leibniz notation

If the function is written as

\[
y=x^2,
\]

then the derivative is usually written as:

\[
\frac{dy}{dx}=2x.
\]

### Lagrange notation

If the function is written as

\[
f(x)=x^2,
\]

then the derivative is usually written as:

\[
f'(x)=2x.
\]

### Second derivative

The second derivative is the derivative of the derivative:

\[
\frac{d^2y}{dx^2}
\]

or

\[
f''(x).
\]

---

## Core Theory

### 1. Why curves need a gradient function

For a straight line:

\[
y=3x+2,
\]

the gradient is constant:

\[
m=3.
\]

For a curve:

\[
y=x^2,
\]

the gradient varies.

At several points on the curve:

\[
\begin{array}{c|rrrrrrr}
x & -3 & -2 & -1 & 0 & 1 & 2 & 3\\
\hline
\text{Gradient} & -6 & -4 & -2 & 0 & 2 & 4 & 6
\end{array}
\]

So:

\[
\frac{dy}{dx}=2x.
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-001 | Source: Chapter 12 Differentiation PDF p.3 and transcript video 1 | Insert from svg/AS1DifferentiationSVG-001.svg | Purpose: Show \(y=x^2\) with tangent gradients and the table leading to \(2x\).]

---

### 2. Approximating the gradient of a curve

To approximate the gradient of

\[
y=x^2
\]

when

\[
x=5,
\]

choose:

\[
(5,25).
\]

A nearby point is:

\[
(6,36).
\]

The gradient between them is:

\[
m=\frac{\Delta y}{\Delta x}
\]

\[
m=\frac{36-25}{6-5}
\]

\[
m=\frac{11}{1}
\]

\[
m=11.
\]

But the actual gradient is:

\[
2(5)=10.
\]

So \(11\) is only an approximation.

Using a closer point:

\[
(5.01,25.1001),
\]

\[
m=\frac{25.1001-25}{5.01-5}
\]

\[
m=\frac{0.1001}{0.01}
\]

\[
m=10.01.
\]

This is closer to the true tangent gradient \(10\).

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-002 | Source: Chapter 12 Differentiation PDF pp.4–5 | Insert from svg/AS1DifferentiationSVG-002.svg | Purpose: Show a secant line from \((5,25)\) to \((6,36)\), then a closer secant from \((5,25)\) to \((5.01,25.1001)\).]

[INTERACTIVE PLACEHOLDER: AS1DifferentiationWidget-002 | Source: Chapter 12 Differentiation PDF pp.4–6 | Insert from widgets/AS1DifferentiationWidget-002.html | Purpose: Let the student vary \(h\) and watch the secant gradient approach \(10\).]

---

### 3. Deriving the gradient function of \(y=x^2\) from first principles

For the curve:

\[
y=x^2,
\]

take a point:

\[
(x,x^2).
\]

Move \(h\) to the right:

\[
x+h.
\]

The second point is:

\[
(x+h,(x+h)^2).
\]

The gradient between the two points is:

\[
m=\frac{(x+h)^2-x^2}{(x+h)-x}.
\]

Since

\[
(x+h)-x=h,
\]

\[
m=\frac{(x+h)^2-x^2}{h}.
\]

The true gradient is the limit:

\[
\frac{dy}{dx}
=
\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.
\]

Expand:

\[
(x+h)^2=x^2+2xh+h^2.
\]

So:

\[
\frac{dy}{dx}
=
\lim_{h\to0}\frac{x^2+2xh+h^2-x^2}{h}.
\]

Cancel:

\[
x^2-x^2=0.
\]

\[
\frac{dy}{dx}
=
\lim_{h\to0}\frac{2xh+h^2}{h}.
\]

Factorise:

\[
2xh+h^2=h(2x+h).
\]

\[
\frac{dy}{dx}
=
\lim_{h\to0}\frac{h(2x+h)}{h}.
\]

Cancel \(h\):

\[
\frac{dy}{dx}
=
\lim_{h\to0}(2x+h).
\]

Now let \(h\to0\):

\[
\frac{dy}{dx}=2x.
\]

So:

\[
\boxed{\frac{dy}{dx}=2x.}
\]

---

### 4. Why not put \(h=0\) immediately?

In

\[
\lim_{h\to0}\frac{(x+h)^2-x^2}{h},
\]

if you immediately substitute \(h=0\):

\[
\frac{(x+0)^2-x^2}{0}
=
\frac{x^2-x^2}{0}
=
\frac00.
\]

The expression

\[
\frac00
\]

is indeterminate. It does not give a usable value.

Correct route:

\[
\text{expand} \rightarrow \text{simplify} \rightarrow \text{cancel }h \rightarrow \text{then take the limit}.
\]

---

### 5. First principles at a fixed point

The point \(A(4,16)\) lies on \(y=x^2\). Find the gradient at \(A\) using first principles.

Let:

\[
f(x)=x^2.
\]

At \(x=4\):

\[
g=\lim_{h\to0}\frac{f(4+h)-f(4)}{h}.
\]

\[
g=\lim_{h\to0}\frac{(4+h)^2-4^2}{h}.
\]

Expand:

\[
(4+h)^2=16+8h+h^2.
\]

\[
g=\lim_{h\to0}\frac{16+8h+h^2-16}{h}.
\]

\[
g=\lim_{h\to0}\frac{8h+h^2}{h}.
\]

Factorise:

\[
8h+h^2=h(8+h).
\]

\[
g=\lim_{h\to0}\frac{h(8+h)}{h}.
\]

Cancel:

\[
g=\lim_{h\to0}(8+h).
\]

Let \(h\to0\):

\[
\boxed{g=8.}
\]

---

### 6. First principles proof: derivative of \(x^4\)

Prove from first principles that the derivative of:

\[
x^4
\]

is:

\[
4x^3.
\]

Let:

\[
f(x)=x^4.
\]

\[
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
\]

\[
f'(x)=\lim_{h\to0}\frac{(x+h)^4-x^4}{h}.
\]

Using Pascal's triangle row \(1,4,6,4,1\):

\[
(x+h)^4=x^4+4x^3h+6x^2h^2+4xh^3+h^4.
\]

Substitute:

\[
f'(x)=\lim_{h\to0}
\frac{x^4+4x^3h+6x^2h^2+4xh^3+h^4-x^4}{h}.
\]

Cancel:

\[
x^4-x^4=0.
\]

\[
f'(x)=\lim_{h\to0}
\frac{4x^3h+6x^2h^2+4xh^3+h^4}{h}.
\]

Divide each term by \(h\):

\[
f'(x)=\lim_{h\to0}
\left(4x^3+6x^2h+4xh^2+h^3\right).
\]

As \(h\to0\):

\[
6x^2h\to0,
\qquad
4xh^2\to0,
\qquad
h^3\to0.
\]

Therefore:

\[
\boxed{f'(x)=4x^3.}
\]

---

### 7. The power rule

If

\[
y=ax^n,
\]

where \(a\) and \(n\) are constants, then:

\[
\boxed{\frac{dy}{dx}=anx^{n-1}.}
\]

In words:

1. multiply by the power;
2. reduce the power by \(1\).

Examples:

\[
y=x^5
\quad\Rightarrow\quad
\frac{dy}{dx}=5x^4.
\]

\[
y=2x^6
\quad\Rightarrow\quad
\frac{dy}{dx}=12x^5.
\]

\[
f(x)=x^{1/2}
\quad\Rightarrow\quad
f'(x)=\frac12x^{-1/2}.
\]

\[
f(x)=\frac{x}{x^4}=x^{-3}
\quad\Rightarrow\quad
f'(x)=-3x^{-4}.
\]

---

### 8. Differentiating multiple terms

If

\[
y=f(x)+g(x),
\]

then:

\[
\frac{dy}{dx}=f'(x)+g'(x).
\]

If

\[
y=f(x)-g(x),
\]

then:

\[
\frac{dy}{dx}=f'(x)-g'(x).
\]

Example:

\[
y=x^2+4x+3.
\]

Differentiate term by term:

\[
\frac{d}{dx}(x^2)=2x,
\]

\[
\frac{d}{dx}(4x)=4,
\]

\[
\frac{d}{dx}(3)=0.
\]

So:

\[
\frac{dy}{dx}=2x+4.
\]

A constant disappears because its graph is horizontal, so its gradient is zero.

---

### 9. Quickfire differentiation

\[
y=2x^2-3x
\quad\Rightarrow\quad
\frac{dy}{dx}=4x-3.
\]

\[
y=4-9x^3
\quad\Rightarrow\quad
\frac{dy}{dx}=-27x^2.
\]

\[
y=5x+1
\quad\Rightarrow\quad
\frac{dy}{dx}=5.
\]

\[
y=ax
\quad\Rightarrow\quad
\frac{dy}{dx}=a,
\]

where \(a\) is constant.

\[
y=6x-3+px^2
\quad\Rightarrow\quad
\frac{dy}{dx}=6+2px,
\]

where \(p\) is constant.

---

### 10. Using the gradient function at a point

Let:

\[
f(x)=4x^2-8x+3.
\]

Find the gradient at:

\[
\left(\frac12,0\right).
\]

Differentiate:

\[
f'(x)=8x-8.
\]

At:

\[
x=\frac12,
\]

\[
f'\left(\frac12\right)=8\left(\frac12\right)-8=4-8=-4.
\]

So the gradient is:

\[
\boxed{-4.}
\]

---

### 11. Find the point where the gradient is given

Let:

\[
f(x)=4x^2-8x+3.
\]

Find the coordinates of the point where the gradient is \(8\).

\[
f'(x)=8x-8.
\]

Set:

\[
f'(x)=8.
\]

\[
8x-8=8.
\]

\[
8x=16.
\]

\[
x=2.
\]

Now use the original function:

\[
y=f(2)=4(2)^2-8(2)+3=16-16+3=3.
\]

The point is:

\[
\boxed{(2,3).}
\]

Exam warning: use the original function \(f(x)\) to find \(y\), not \(f'(x)\).

---

### 12. Gradient where a curve meets a line

Let:

\[
f(x)=4x^2-8x+3.
\]

Find the gradient of \(y=f(x)\) at the points where it meets:

\[
y=4x-5.
\]

Set the equations equal:

\[
4x^2-8x+3=4x-5.
\]

\[
4x^2-12x+8=0.
\]

Divide by \(4\):

\[
x^2-3x+2=0.
\]

\[
(x-1)(x-2)=0.
\]

So:

\[
x=1
\quad\text{or}\quad
x=2.
\]

Use:

\[
f'(x)=8x-8.
\]

When \(x=1\):

\[
f'(1)=8(1)-8=0.
\]

When \(x=2\):

\[
f'(2)=8(2)-8=8.
\]

So the gradients are:

\[
\boxed{0\text{ and }8.}
\]

---

### 13. Differentiating harder expressions

If an expression is not already a sum of \(x^n\) terms, manipulate it until it is.

#### Roots into powers

\[
\sqrt{x}=x^{1/2}.
\]

\[
\frac{1}{\sqrt[3]{x}}=x^{-1/3}.
\]

So:

\[
y=x^{-1/3}
\quad\Rightarrow\quad
\frac{dy}{dx}
=
-\frac13x^{-4/3}.
\]

#### Split numerator fractions

\[
y=\frac{x^2+3}{\sqrt{x}}
=
\frac{x^2}{x^{1/2}}+\frac{3}{x^{1/2}}
=
x^{3/2}+3x^{-1/2}.
\]

Differentiate:

\[
\frac{dy}{dx}
=
\frac32x^{1/2}-\frac32x^{-3/2}.
\]

#### Expand brackets first

\[
y=x^2(x-3)=x^3-3x^2.
\]

\[
\frac{dy}{dx}=3x^2-6x.
\]

#### Beware numbers in denominators

Wrong:

\[
\frac1{3x}=3x^{-1}.
\]

Correct:

\[
\frac1{3x}=\frac13x^{-1}.
\]

Differentiate:

\[
\frac{d}{dx}\left(\frac13x^{-1}\right)
=
-\frac13x^{-2}.
\]

---

### 14. Tangents

A tangent is a straight line that touches a curve at a point and has the same gradient as the curve at that point.

To find a tangent:

1. differentiate to find the gradient function;
2. substitute the \(x\)-value to find the gradient;
3. substitute into the original function to find the point;
4. use \(y-y_1=m(x-x_1)\).

Example: find the tangent to:

\[
y=x^2
\]

when \(x=3\).

\[
\frac{dy}{dx}=2x.
\]

At \(x=3\):

\[
m=2(3)=6.
\]

Point:

\[
y=3^2=9,
\]

so:

\[
(3,9).
\]

\[
y-9=6(x-3).
\]

Expanded:

\[
y=6x-9.
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-003 | Source: Chapter 12 Differentiation PDF p.21 | Insert from svg/AS1DifferentiationSVG-003.svg | Purpose: Show \(y=x^2\), point \((3,9)\) and the tangent line.]

---

### 15. Normals

A normal is perpendicular to the tangent.

If the tangent gradient is:

\[
m_t,
\]

then the normal gradient is:

\[
m_n=-\frac1{m_t}.
\]

Example: find the normal to:

\[
y=x^2
\]

when \(x=3\).

From the tangent example:

\[
m_t=6.
\]

So:

\[
m_n=-\frac16.
\]

Point:

\[
(3,9).
\]

Normal equation:

\[
y-9=-\frac16(x-3).
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-004 | Source: Chapter 12 Differentiation PDF p.22 | Insert from svg/AS1DifferentiationSVG-004.svg | Purpose: Show tangent and normal at \((3,9)\), including negative reciprocal gradients.]

[INTERACTIVE PLACEHOLDER: AS1DifferentiationWidget-003 | Source: Chapter 12 Differentiation PDF pp.21–23 | Insert from widgets/AS1DifferentiationWidget-003.html | Purpose: Let the student choose a point on \(y=x^2\) and compare tangent and normal gradients.]

---

### 16. Normal to \(y=x+3\sqrt{x}\)

Find the equation of the normal to:

\[
y=x+3\sqrt{x}
\]

when:

\[
x=9.
\]

Rewrite:

\[
y=x+3x^{1/2}.
\]

Differentiate:

\[
\frac{dy}{dx}=1+3\left(\frac12\right)x^{-1/2}
=
1+\frac32x^{-1/2}.
\]

At \(x=9\):

\[
\frac{dy}{dx}
=
1+\frac32(9^{-1/2}).
\]

\[
9^{-1/2}=\frac1{\sqrt9}=\frac13.
\]

\[
\frac{dy}{dx}=1+\frac32\cdot\frac13
=
1+\frac12
=
\frac32.
\]

This is the tangent gradient:

\[
m_t=\frac32.
\]

The normal gradient is:

\[
m_n=-\frac23.
\]

Point:

\[
y=9+3\sqrt9=9+9=18.
\]

So:

\[
(9,18).
\]

Equation:

\[
\boxed{y-18=-\frac23(x-9).}
\]

---

### 17. Increasing and decreasing functions

A function is increasing where:

\[
f'(x)>0.
\]

A function is decreasing where:

\[
f'(x)<0.
\]

Stationary points occur where:

\[
f'(x)=0.
\]

Example: find where:

\[
f(x)=x^3-x
\]

is increasing.

\[
f'(x)=3x^2-1.
\]

For increasing:

\[
3x^2-1>0.
\]

\[
3x^2>1.
\]

\[
x^2>\frac13.
\]

So:

\[
x<-\sqrt{\frac13}
\quad\text{or}\quad
x>\sqrt{\frac13}.
\]

\[
\boxed{x<-\frac{\sqrt3}{3}\quad\text{or}\quad x>\frac{\sqrt3}{3}.}
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-005 | Source: CCEA AS1-DIFF-LO008 + Chapter 12 overview | Insert from svg/AS1DifferentiationSVG-005.svg | Purpose: Show a sign chart for \(f'(x)=3x^2-1\).]

---

### 18. Second derivatives

The first derivative tells you the gradient:

\[
\frac{dy}{dx}.
\]

The second derivative tells you how the gradient is changing:

\[
\frac{d^2y}{dx^2}.
\]

Example:

\[
y=x^4-3x^2.
\]

First derivative:

\[
\frac{dy}{dx}=4x^3-6x.
\]

Second derivative:

\[
\frac{d^2y}{dx^2}=12x^2-6.
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-006 | Source: CCEA AS1-DIFF-LO004 and LO005 + Chapter 12 overview | Insert from svg/AS1DifferentiationSVG-006.svg | Purpose: Show \(y \to \frac{dy}{dx} \to \frac{d^2y}{dx^2}\).]

---

### 19. Stationary points

A stationary point occurs where:

\[
f'(x)=0.
\]

Stationary points can be:

1. local maximum points;
2. local minimum points;
3. stationary points of inflexion.

A local maximum has gradient pattern:

\[
+\to0\to-.
\]

A local minimum has gradient pattern:

\[
-\to0\to+.
\]

A stationary point of inflexion may have:

\[
+\to0\to+
\]

or

\[
-\to0\to-.
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-007 | Source: Chapter 12 Differentiation PDF stationary point sections | Insert from svg/AS1DifferentiationSVG-007.svg | Purpose: Compare local maximum, local minimum and stationary point of inflexion.]

[INTERACTIVE PLACEHOLDER: AS1DifferentiationWidget-004 | Source: Chapter 12 Differentiation PDF pp.26–40 | Insert from widgets/AS1DifferentiationWidget-004.html | Purpose: Explore \(f'(x)\), \(f''(x)\), increasing/decreasing behaviour and stationary-point classification.]

---

### 20. Classifying stationary points using the second derivative

At a stationary point:

\[
f'(x)=0.
\]

If:

\[
f''(x)>0,
\]

then the point is a local minimum.

If:

\[
f''(x)<0,
\]

then the point is a local maximum.

If:

\[
f''(x)=0,
\]

the test is inconclusive. More investigation is needed.

---

### 21. Worked example: stationary points of \(y=x^3-x\)

Find the stationary points of:

\[
y=x^3-x
\]

and determine their nature.

Differentiate:

\[
\frac{dy}{dx}=3x^2-1.
\]

Set equal to zero:

\[
3x^2-1=0.
\]

\[
3x^2=1.
\]

\[
x^2=\frac13.
\]

\[
x=\pm\frac1{\sqrt3}.
\]

Find \(y\)-values.

At \(x=\frac1{\sqrt3}\):

\[
y=\left(\frac1{\sqrt3}\right)^3-\frac1{\sqrt3}
=
\frac1{3\sqrt3}-\frac1{\sqrt3}
=
\frac1{3\sqrt3}-\frac3{3\sqrt3}
=
-\frac2{3\sqrt3}.
\]

At \(x=-\frac1{\sqrt3}\):

\[
y=-\frac1{3\sqrt3}+\frac1{\sqrt3}
=
-\frac1{3\sqrt3}+\frac3{3\sqrt3}
=
\frac2{3\sqrt3}.
\]

Second derivative:

\[
\frac{d^2y}{dx^2}=6x.
\]

At \(x=\frac1{\sqrt3}\):

\[
6\left(\frac1{\sqrt3}\right)>0,
\]

so it is a local minimum.

At \(x=-\frac1{\sqrt3}\):

\[
6\left(-\frac1{\sqrt3}\right)<0,
\]

so it is a local maximum.

---

### 22. Least value of a quadratic

Find the least value of:

\[
f(x)=x^2-4x+9.
\]

Differentiate:

\[
f'(x)=2x-4.
\]

Set equal to zero:

\[
2x-4=0.
\]

\[
2x=4.
\]

\[
x=2.
\]

Now:

\[
f(2)=2^2-4(2)+9=4-8+9=5.
\]

So the least value is:

\[
\boxed{5.}
\]

Completing the square confirms this:

\[
f(x)=x^2-4x+9=(x-2)^2+5.
\]

Since:

\[
(x-2)^2\ge0,
\]

the least value is:

\[
5.
\]

---

### 23. Rate of change

A derivative can represent a real rate of change.

If \(V\) is volume and \(t\) is time, then:

\[
\frac{dV}{dt}
\]

means the rate at which volume changes with respect to time.

If a container fills at:

\[
20\text{ cm}^3\text{/s},
\]

then:

\[
\boxed{\frac{dV}{dt}=20.}
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-008 | Source: Chapter 12 Differentiation PDF rate-of-change evidence | Insert from svg/AS1DifferentiationSVG-008.svg | Purpose: Show \(V\) increasing with time and connect \(\frac{dV}{dt}\) to a real rate of change.]

---

### 24. Optimisation problems

Optimisation means using differentiation to maximise or minimise something.

General method:

1. Identify the quantity to maximise or minimise.
2. Identify the constraint.
3. Use the constraint to write the target quantity in terms of one variable.
4. Differentiate.
5. Set the derivative equal to zero.
6. Solve for the variable.
7. Substitute back to find the required value.
8. Confirm maximum/minimum using a second derivative or sign change.

---

### 25. Optimisation tank example

A large open-top cuboid tank is made from:

\[
54\text{ m}^2
\]

of sheet metal.

Height is \(x\) metres. Two opposite vertical faces are squares.

The volume is shown to be:

\[
V=18x-\frac23x^3.
\]

Differentiate:

\[
\frac{dV}{dx}=18-2x^2.
\]

Set equal to zero:

\[
18-2x^2=0.
\]

\[
18=2x^2.
\]

\[
x^2=9.
\]

Since \(x\) is a length:

\[
x=3.
\]

Volume:

\[
V=18(3)-\frac23(3)^3.
\]

\[
=54-\frac23(27).
\]

\[
=54-18.
\]

\[
=36.
\]

Second derivative:

\[
\frac{d^2V}{dx^2}=-4x.
\]

At \(x=3\):

\[
\frac{d^2V}{dx^2}=-12<0,
\]

so this is a maximum.

Maximum volume:

\[
\boxed{36\text{ m}^3.}
\]

[VISUAL PLACEHOLDER: AS1DifferentiationSVG-009 | Source: Chapter 12 Differentiation PDF optimisation tank evidence | Insert from svg/AS1DifferentiationSVG-009.svg | Purpose: Show open-top cuboid tank with dimensions \(x\) and \(y\).]

[INTERACTIVE PLACEHOLDER: AS1DifferentiationWidget-001 | Source: Chapter 12 Differentiation PDF optimisation tank example | Insert from widgets/AS1DifferentiationWidget-001.html | Purpose: Vary \(x\), view \(V=18x-\frac23x^3\), and observe the maximum at \(x=3\).]

---

## Worked Examples

### Worked Example 1: Differentiate a polynomial

Differentiate:

\[
y=3x^2+\sqrt{x}.
\]

Rewrite:

\[
y=3x^2+x^{1/2}.
\]

Differentiate:

\[
\frac{dy}{dx}=6x+\frac12x^{-1/2}.
\]

Equivalently:

\[
\frac{dy}{dx}=6x+\frac1{2\sqrt{x}}.
\]

---

### Worked Example 2: First principles at a point

The point \(A(4,16)\) lies on \(y=x^2\). Find the gradient at \(A\) using first principles.

\[
g=\lim_{h\to0}\frac{(4+h)^2-4^2}{h}
\]

\[
=\lim_{h\to0}\frac{16+8h+h^2-16}{h}
\]

\[
=\lim_{h\to0}\frac{8h+h^2}{h}
\]

\[
=\lim_{h\to0}(8+h)
\]

\[
=8.
\]

---

### Worked Example 3: Gradient at a point

Let:

\[
f(x)=4x^2-8x+3.
\]

Find the gradient at:

\[
\left(\frac12,0\right).
\]

\[
f'(x)=8x-8.
\]

\[
f'\left(\frac12\right)=8\left(\frac12\right)-8=-4.
\]

---

### Worked Example 4: Point where gradient is given

Let:

\[
f(x)=4x^2-8x+3.
\]

Find the coordinates where the gradient is \(8\).

\[
f'(x)=8x-8.
\]

\[
8x-8=8.
\]

\[
x=2.
\]

\[
y=f(2)=4(2)^2-8(2)+3=3.
\]

Point:

\[
\boxed{(2,3).}
\]

---

### Worked Example 5: Tangent to a curve

Find the tangent to \(y=x^2\) when \(x=3\).

\[
\frac{dy}{dx}=2x.
\]

At \(x=3\):

\[
m=6.
\]

Point:

\[
(3,9).
\]

Equation:

\[
\boxed{y-9=6(x-3).}
\]

---

### Worked Example 6: Normal to a curve

Find the normal to \(y=x^2\) when \(x=3\).

Tangent gradient:

\[
m_t=6.
\]

Normal gradient:

\[
m_n=-\frac16.
\]

Point:

\[
(3,9).
\]

Equation:

\[
\boxed{y-9=-\frac16(x-3).}
\]

---

### Worked Example 7: Increasing intervals

Find where:

\[
f(x)=x^3-x
\]

is increasing.

\[
f'(x)=3x^2-1.
\]

Increasing means:

\[
3x^2-1>0.
\]

\[
x^2>\frac13.
\]

\[
\boxed{x<-\frac{\sqrt3}{3}\quad\text{or}\quad x>\frac{\sqrt3}{3}.}
\]

---

### Worked Example 8: Second derivative

Find:

\[
\frac{d^2y}{dx^2}
\]

if:

\[
y=x^4-3x^2.
\]

\[
\frac{dy}{dx}=4x^3-6x.
\]

\[
\boxed{\frac{d^2y}{dx^2}=12x^2-6.}
\]

---

## Guided Practice

### Practice Question 1

Differentiate:

\[
y=7x^4-5x^2+9x-11.
\]

### Practice Question 2

Differentiate:

\[
y=3\sqrt{x}+\frac4{x^2}.
\]

### Practice Question 3

Differentiate:

\[
y=\frac{x^3+2x}{\sqrt{x}}.
\]

### Practice Question 4

Let:

\[
f(x)=2x^2-3x+5.
\]

Find the gradient at:

\[
x=4.
\]

### Practice Question 5

Let:

\[
f(x)=x^2-6x+4.
\]

Find the coordinates of the point where the gradient is \(8\).

### Practice Question 6

Find the tangent to:

\[
y=x^2+2x
\]

at:

\[
x=1.
\]

### Practice Question 7

Find the normal to:

\[
y=x^2+2x
\]

at:

\[
x=1.
\]

### Practice Question 8

Find the values of \(x\) for which:

\[
f(x)=x^3-12x
\]

is increasing.

### Practice Question 9

Find the stationary points of:

\[
y=x^3-3x^2-9x+2
\]

and determine their nature.

### Practice Question 10

A function is given by:

\[
A(x)=12x-x^2.
\]

Find the maximum value of \(A(x)\).

---

## Common Mistakes and Exam Traps

### Trap 1: Substituting \(h=0\) too early

Do not go straight from:

\[
\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
\]

to \(h=0\). It often creates:

\[
\frac00.
\]

Expand, simplify, cancel and then take the limit.

### Trap 2: Forgetting the limit notation

Keep writing:

\[
\lim_{h\to0}
\]

until the expression is simplified enough to take the limit.

### Trap 3: Differentiating before rewriting

At AS1, rewrite expressions into sums/differences of \(ax^n\) terms first.

### Trap 4: Moving denominator numbers incorrectly

Wrong:

\[
\frac1{3x}=3x^{-1}.
\]

Correct:

\[
\frac1{3x}=\frac13x^{-1}.
\]

### Trap 5: Using the derivative to find \(y\)

Use \(f'(x)\) to find gradients. Use \(f(x)\) to find \(y\)-coordinates.

### Trap 6: Tangent versus normal

A tangent uses:

\[
m_t=f'(x).
\]

A normal uses:

\[
m_n=-\frac1{m_t}.
\]

### Trap 7: Assuming every stationary point is a maximum or minimum

A stationary point may be a maximum, minimum or stationary point of inflexion.

### Trap 8: \(f''(x)=0\) does not prove inflexion

If \(f''(x)=0\), the second derivative test is inconclusive.

### Trap 9: Forgetting interval notation

For increasing/decreasing questions, give intervals, not just boundary points.

---

## Exam Technique Notes

### Differentiate questions

Use:

\[
\text{rewrite} \rightarrow \text{differentiate} \rightarrow \text{simplify}.
\]

### Gradient at a point

Differentiate first, then substitute the \(x\)-value.

### Tangents

\[
\text{differentiate} \rightarrow \text{find }m \rightarrow \text{find point} \rightarrow y-y_1=m(x-x_1).
\]

### Normals

Find \(m_t\), then:

\[
m_n=-\frac1{m_t}.
\]

### Stationary points

Solve:

\[
f'(x)=0.
\]

Then find \(y\)-values using the original function.

### Increasing/decreasing

Increasing:

\[
f'(x)>0.
\]

Decreasing:

\[
f'(x)<0.
\]

### Optimisation

\[
\text{constraint} \rightarrow \text{one-variable formula} \rightarrow \text{differentiate} \rightarrow f'(x)=0 \rightarrow \text{check maximum/minimum}.
\]

---

## Full Worked Solutions

### Solution 1

\[
y=7x^4-5x^2+9x-11.
\]

\[
\frac{dy}{dx}=28x^3-10x+9.
\]

### Solution 2

\[
y=3\sqrt{x}+\frac4{x^2}=3x^{1/2}+4x^{-2}.
\]

\[
\frac{dy}{dx}=\frac32x^{-1/2}-8x^{-3}.
\]

### Solution 3

\[
y=\frac{x^3+2x}{\sqrt{x}}
=
\frac{x^3}{x^{1/2}}+\frac{2x}{x^{1/2}}
=
x^{5/2}+2x^{1/2}.
\]

\[
\frac{dy}{dx}
=
\frac52x^{3/2}+x^{-1/2}.
\]

### Solution 4

\[
f(x)=2x^2-3x+5.
\]

\[
f'(x)=4x-3.
\]

\[
f'(4)=16-3=13.
\]

### Solution 5

\[
f(x)=x^2-6x+4.
\]

\[
f'(x)=2x-6.
\]

\[
2x-6=8.
\]

\[
x=7.
\]

\[
y=f(7)=49-42+4=11.
\]

Point:

\[
(7,11).
\]

### Solution 6

\[
y=x^2+2x.
\]

\[
\frac{dy}{dx}=2x+2.
\]

At \(x=1\):

\[
m=4.
\]

Point:

\[
(1,3).
\]

Tangent:

\[
y-3=4(x-1).
\]

Expanded:

\[
y=4x-1.
\]

### Solution 7

Tangent gradient:

\[
m_t=4.
\]

Normal gradient:

\[
m_n=-\frac14.
\]

Point:

\[
(1,3).
\]

Normal:

\[
y-3=-\frac14(x-1).
\]

Expanded:

\[
y=-\frac14x+\frac{13}{4}.
\]

### Solution 8

\[
f(x)=x^3-12x.
\]

\[
f'(x)=3x^2-12.
\]

Increasing:

\[
3x^2-12>0.
\]

\[
x^2>4.
\]

\[
\boxed{x<-2\quad\text{or}\quad x>2.}
\]

### Solution 9

\[
y=x^3-3x^2-9x+2.
\]

\[
\frac{dy}{dx}=3x^2-6x-9.
\]

Set equal to zero:

\[
3x^2-6x-9=0.
\]

Divide by \(3\):

\[
x^2-2x-3=0.
\]

\[
(x-3)(x+1)=0.
\]

\[
x=3
\quad\text{or}\quad
x=-1.
\]

At \(x=3\):

\[
y=27-27-27+2=-25.
\]

At \(x=-1\):

\[
y=-1-3+9+2=7.
\]

Second derivative:

\[
\frac{d^2y}{dx^2}=6x-6.
\]

At \(x=3\):

\[
6(3)-6=12>0,
\]

so \((3,-25)\) is a local minimum.

At \(x=-1\):

\[
6(-1)-6=-12<0,
\]

so \((-1,7)\) is a local maximum.

### Solution 10

\[
A(x)=12x-x^2.
\]

\[
A'(x)=12-2x.
\]

\[
12-2x=0.
\]

\[
x=6.
\]

\[
A(6)=72-36=36.
\]

Second derivative:

\[
A''(x)=-2<0.
\]

So the maximum value is:

\[
\boxed{36.}
\]

---

## Common CCEA-Style Wording

| Command phrase | What to do |
|---|---|
| Differentiate | Find \(\frac{dy}{dx}\) or \(f'(x)\). |
| Find the gradient at | Differentiate, then substitute the \(x\)-value. |
| Find the equation of the tangent | Find point and tangent gradient, then use \(y-y_1=m(x-x_1)\). |
| Find the equation of the normal | Find tangent gradient, take negative reciprocal, then use \(y-y_1=m(x-x_1)\). |
| Find stationary points | Solve \(f'(x)=0\), then find corresponding \(y\)-values. |
| Determine the nature | Use \(f''(x)\) or sign changes in \(f'(x)\). |
| Find where the function is increasing | Solve \(f'(x)>0\). |
| Find where the function is decreasing | Solve \(f'(x)<0\). |
| Use first principles | Use \(\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\). |
| Interpret the rate of change | State what the derivative means in context and include units. |

---

## Syllabus Gap Check

| LO ID | Coverage status | Evidence-backed coverage |
|---|---|---|
| AS1-DIFF-LO001 | Covered | Derivative as gradient function of \(y=f(x)\). |
| AS1-DIFF-LO002 | Covered | First principles and limit of secant gradients. |
| AS1-DIFF-LO003 | Covered | Rate of change examples using \(\frac{dV}{dt}\). |
| AS1-DIFF-LO004 | Covered | Second derivative calculation examples. |
| AS1-DIFF-LO005 | Covered | Second derivative as rate of change of gradient and classification support. |
| AS1-DIFF-LO006 | Covered | Power rule for rational powers, sums, differences and constants. |
| AS1-DIFF-LO007 | Covered | Gradients, tangents, normals, maxima, minima, stationary points and optimisation. |
| AS1-DIFF-LO008 | Covered | Increasing/decreasing functions using \(f'(x)>0\) and \(f'(x)<0\). |

---

## Off-Spec Content Found but Excluded

| Evidence item | Decision | Reason |
|---|---|---|
| Newton dot notation | Excluded from core | Evidence notes it is not used at A Level. |
| Product rule | Excluded from core | Belongs to later differentiation, not AS1-DIFF. |
| Quotient rule | Excluded from core | AS1 uses algebraic rewriting instead. |
| Chain rule | Excluded from core | Not part of this AS1 lesson boundary. |
| Implicit differentiation | Excluded from core | Year 2/A2 method. |
| Partial differentiation | Excluded from core | Not standard CCEA A-Level Mathematics AS1 content. |
| STEP/MAT extension problems | Optional enrichment only | Cross-board/extension level; not treated as required CCEA core. |
| Trig derivative sketching beyond gradient intuition | Excluded from core | Differentiating trig functions is not AS1-DIFF core. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Folder | Purpose |
|---|---|---|---|
| AS1DifferentiationMERMAID-001 | Mermaid | mermaid/ | Why a curve needs a gradient function. |
| AS1DifferentiationMERMAID-002 | Mermaid | mermaid/ | Secant-to-tangent first-principles idea. |
| AS1DifferentiationMERMAID-003 | Mermaid | mermaid/ | First-principles route and \(0/0\) warning. |
| AS1DifferentiationMERMAID-004 | Mermaid | mermaid/ | Rewriting expressions before differentiating. |
| AS1DifferentiationMERMAID-005 | Mermaid | mermaid/ | Tangent/normal method comparison. |
| AS1DifferentiationMERMAID-006 | Mermaid | mermaid/ | Stationary-point workflow. |
| AS1DifferentiationMERMAID-007 | Mermaid | mermaid/ | Increasing/decreasing sign process. |
| AS1DifferentiationMERMAID-008 | Mermaid | mermaid/ | Optimisation workflow. |
| AS1DifferentiationMERMAID-009 | Mermaid | mermaid/ | AS1 boundary: avoid later A2 rules. |
| AS1DifferentiationSVG-001 | SVG | svg/ | Gradient function for \(y=x^2\). |
| AS1DifferentiationSVG-002 | SVG | svg/ | Secants approaching tangent. |
| AS1DifferentiationSVG-003 | SVG | svg/ | Tangent to \(y=x^2\) at \((3,9)\). |
| AS1DifferentiationSVG-004 | SVG | svg/ | Normal to \(y=x^2\) at \((3,9)\). |
| AS1DifferentiationSVG-005 | SVG | svg/ | Sign chart for increasing/decreasing intervals. |
| AS1DifferentiationSVG-006 | SVG | svg/ | First derivative to second derivative chain. |
| AS1DifferentiationSVG-007 | SVG | svg/ | Maximum/minimum/stationary inflexion comparison. |
| AS1DifferentiationSVG-008 | SVG | svg/ | Rate-of-change interpretation. |
| AS1DifferentiationSVG-009 | SVG | svg/ | Optimisation tank diagram. |
| AS1DifferentiationTIKZ-001 to 009 | TikZ | tikz/ | Mathematical diagram equivalents. |
| AS1DifferentiationWidget-001 | HTML | widgets/ | Optimisation tank explorer. |
| AS1DifferentiationWidget-002 | HTML | widgets/ | Secant-to-tangent explorer. |
| AS1DifferentiationWidget-003 | HTML | widgets/ | Tangent/normal explorer. |
| AS1DifferentiationWidget-004 | HTML | widgets/ | Stationary point explorer. |

---

## Supplementary Sources Used

No external web sources were used.

Core sources used:

- CCEA GCE Mathematics Specification Map
- README Module Map
- Evidence Drop Checklist
- Chapter 12 Differentiation PDF
- Chapter 12 Differentiation Transcript
- Chapter 12 Screenshots PDF as visual support only

---

## Final Student Checklist

### Understanding

- [ ] I can explain why curves need gradient functions.
- [ ] I can explain what the derivative means.
- [ ] I can explain why tangent gradient is found using a limit.
- [ ] I can explain why \(\frac00\) appears if \(h=0\) is substituted too early.
- [ ] I can explain the difference between \(f(x)\), \(f'(x)\) and \(f''(x)\).

### First Principles

- [ ] I can use:
  \[
  f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
  \]
- [ ] I can expand, simplify and cancel before taking the limit.
- [ ] I can prove:
  \[
  \frac{d}{dx}(x^2)=2x
  \]
  and:
  \[
  \frac{d}{dx}(x^4)=4x^3.
  \]

### Differentiation Rules

- [ ] I can differentiate \(ax^n\).
- [ ] I can differentiate sums and differences.
- [ ] I can rewrite roots as powers.
- [ ] I can rewrite reciprocals as negative powers.
- [ ] I can split fractions by the numerator where valid.
- [ ] I can expand brackets before differentiating.
- [ ] I know not to turn \(\frac1{3x}\) into \(3x^{-1}\).

### Applications

- [ ] I can find the gradient at a point.
- [ ] I can find a point where the gradient is given.
- [ ] I can find tangent equations.
- [ ] I can find normal equations.
- [ ] I can solve \(f'(x)>0\) for increasing intervals.
- [ ] I can solve \(f'(x)<0\) for decreasing intervals.
- [ ] I can find stationary points by solving \(f'(x)=0\).
- [ ] I can classify stationary points using \(f''(x)\).
- [ ] I can apply differentiation to simple optimisation problems.

### Exam Readiness

- [ ] I write \(\frac{dy}{dx}\) or \(f'(x)\) correctly.
- [ ] I use the original function, not the derivative, to find \(y\)-coordinates.
- [ ] I clearly distinguish tangent gradients from normal gradients.
- [ ] I include exact values where possible.
- [ ] I give interval answers for increasing/decreasing questions.
- [ ] I check whether a stationary point is maximum or minimum when asked.
- [ ] I can explain rates of change in context and include units.
