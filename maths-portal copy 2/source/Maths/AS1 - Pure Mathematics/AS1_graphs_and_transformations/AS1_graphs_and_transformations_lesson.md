# AS1 Graphs and Transformations

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `AS1` |
| Unit name | `AS 1 Pure Mathematics` |
| Topic code | `AS1-AF` |
| Specification topic | Algebra and functions |
| Lesson title | Graphs and Transformations |
| Topic slug | `graphs_and_transformations` |
| Topic Pascal | `GraphsAndTransformations` |
| Topic ID | `AS1GraphsAndTransformations` |
| Lesson file | `AS1_graphs_and_transformations_lesson.md` |
| Core LO IDs | `AS1-AF-LO012`, `AS1-AF-LO013`, `AS1-AF-LO014`, `AS1-AF-LO015`, `AS1-AF-LO016` |
| Supporting LO IDs | `AS1-AF-LO010`, `AS1-AF-LO011` |
| Evidence status | Specification map, module map, checklist, PDF slides, transcript and screenshot PDF available |
| Asset status | Mermaid, SVG, TikZ and widget files included in pack |

---

## Evidence Map

This lesson is built from the CCEA AS1 Algebra and functions outcomes and the uploaded Chapter 4 evidence. The DrFrost chapter overview lists cubic graphs, quartic graphs, reciprocal graphs, points of intersection and graph transformations. The CCEA boundary retains cubics, reciprocal graphs, intersections and transformations as core, but not quartic polynomial sketching.

| Evidence source | Status | Used for |
|---|---:|---|
| CCEA GCE Mathematics Specification Map | Available | Unit, topic code, LO IDs, syllabus boundary |
| README Module Map | Available | Naming conventions, phase structure, metadata fields |
| Source Evidence Drop Checklist | Available | Missing evidence log, off-spec log, visual placeholder rules |
| `P1-Chp4-GraphsAndTransformations.pdf` | Available | Slide content: polynomial sketches, reciprocal graphs, intersections, transformations |
| Teacher transcript for Chapter 4 | Available | Teacher explanations, warnings, method language, Desmos/calculator checking advice |
| Screenshots PDF | Available, visual-only | Visual reference for early slides; no extra uninspected mathematical claims |
| Textbook extract | Partial only through slide references | Pearson exercise/page references appear in slides, but full textbook pages are not supplied |

---

## Specification Alignment

| LO ID | Where it appears in this lesson |
|---|---|
| `AS1-AF-LO010` | Expanding factorised expressions, collecting like terms, using factorised forms to identify roots |
| `AS1-AF-LO011` | Factorised cubic expressions and solving cubic equations through factors |
| `AS1-AF-LO012` | Sketching cubic curves from shape, roots and `y`-intercept |
| `AS1-AF-LO013` | Sketching `y=a/x`, `y=a/x^2`, and transformed reciprocal graphs with asymptotes |
| `AS1-AF-LO014` | Reading algebraic equation solutions from sketches |
| `AS1-AF-LO015` | Using graph intersections to solve equations or count real solutions |
| `AS1-AF-LO016` | Translating, stretching and reflecting graphs of `y=f(x)` |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Sketch cubic graphs from factorised equations by identifying shape, roots and `y`-intercept.
2. Explain what happens at simple, repeated and triple repeated roots, without treating “point of inflection” as required CCEA vocabulary.
3. Sketch reciprocal graphs of the forms `y=a/x` and `y=a/x^2`, including asymptotes.
4. Use intersections of graphs to solve equations or state the number of real solutions.
5. Apply graph transformations of the forms `y=af(x)`, `y=f(x)+a`, `y=f(x+a)`, and `y=f(ax)`.
6. Track the movement of roots, intercepts and specific points under transformations.

---

## Prerequisite Recap

You need these earlier A-Level algebra skills:

| Skill | Why it matters here |
|---|---|
| Expanding brackets | Used when converting a factorised curve equation into polynomial form |
| Factorising quadratics and cubics | Used to identify roots and intersection points |
| Discriminant `b^2-4ac` | Used to prove a quadratic has no further real roots |
| Quadratic graph shape | Used as the starting comparison for cubic and reciprocal sketches |
| Function notation `f(x)` | Used throughout transformations |
| Simultaneous equations | Graph intersections are simultaneous equations in disguise |

No external GCSE sources are used in this lesson.

---

## Big Picture Explanation

This chapter is a graph-reading and graph-drawing engine room. The uploaded transcript says the chapter begins by moving beyond straight lines and quadratics into “more interesting kinds of graphs”, including cubic graphs, reciprocal graphs and transformations.

At AS1, a sketch is not an art competition. It is a mathematical map. A good sketch shows the features that matter:

\[
\text{shape},\qquad \text{roots},\qquad y\text{-intercept},\qquad \text{asymptotes where relevant}.
\]

The exam does not need a graph with museum-quality curves. It needs a curve that tells the truth.

---

## Key Definitions and Notation

### Polynomial

A polynomial expression is built from powers of `x` with constant coefficients:

\[
a+bx+cx^2+dx^3+ex^4+\cdots
\]

where

\[
a,b,c,d,e,\ldots
\]

are constants, and some of them may be `0`. The evidence PDF contains a printing issue where the fourth-power term is shown incorrectly in one place; the transcript explicitly corrects this to `ex^4`.

### Order or degree of a polynomial

The order, or degree, is the highest power of `x`.

| Degree | Name | Example |
|---:|---|---|
| 0 | Constant | `4` |
| 1 | Linear | `2x-1` |
| 2 | Quadratic | `x^2+3` |
| 3 | Cubic | `x^3-3x^2+7` |
| 4 | Quartic | `x^4+...`, enrichment only for this CCEA lesson |
| 5 | Quintic | enrichment only |

For CCEA AS1 core polynomial sketching in this lesson, stop at degree `3`.

### Root

A root is an `x`-value where

\[
y=0.
\]

Graphically, it is where the curve meets the `x`-axis.

### `y`-intercept

The `y`-intercept is found by setting

\[
x=0.
\]

### Asymptote

An asymptote is a line that a graph approaches but never reaches. For the standard reciprocal graphs in this lesson, the axes are usually asymptotes unless the graph has been transformed.

### Transformation

A transformation changes the position or shape of a graph. For CCEA AS1, the required forms are:

\[
y=af(x),\qquad y=f(x)+a,\qquad y=f(x+a),\qquad y=f(ax).
\]

Reflections are included as the special cases where `a=-1`.

---

## Core Theory

## 1. Polynomial Graph Shape

For graph sketching, the highest power controls the end behaviour.

### Cubic shape

A cubic has the general form

\[
y=ax^3+bx^2+cx+d.
\]

If `a>0`, then:

\[
x\to\infty \implies y\to\infty,
\]

and

\[
x\to-\infty \implies y\to-\infty.
\]

So the curve goes “uphill” from left to right.

If `a<0`, then:

\[
x\to\infty \implies y\to-\infty,
\]

and

\[
x\to-\infty \implies y\to\infty.
\]

So the curve goes “downhill” from left to right.

The evidence summary says that for odd degree with positive leading coefficient, the graph goes uphill; for even degree with positive leading coefficient, the tails go upwards, with the opposite behaviour when the leading coefficient is negative.

---

## 2. The Three-Feature Sketching Routine

For a cubic sketch, always identify:

\[
\boxed{\text{Shape}}\qquad
\boxed{\text{Roots}}\qquad
\boxed{y\text{-intercept}}
\]

The teacher transcript states that a sketch does not need accurate scale or perfect drawing; it needs to show the key features: shape, roots and `y`-intercept.

### Feature 1: Shape

Look at the sign of the `x^3` term.

For

\[
y=(x-2)(1-x)(1+x),
\]

the leading `x`-terms multiply as

\[
x\cdot(-x)\cdot x=-x^3.
\]

So the cubic is negative and goes downhill.

### Feature 2: Roots

Set each factor equal to zero.

\[
x-2=0 \implies x=2,
\]

\[
1-x=0 \implies x=1,
\]

\[
1+x=0 \implies x=-1.
\]

### Feature 3: `y`-intercept

Set `x=0`:

\[
y=(0-2)(1-0)(1+0),
\]

\[
y=(-2)(1)(1),
\]

\[
y=-2.
\]

So the curve crosses the `y`-axis at

\[
(0,-2).
\]

---

## 3. Repeated Roots

Consider

\[
y=x^2(x-1).
\]

### Shape

The leading term is

\[
x^2\cdot x=x^3,
\]

so this is a positive cubic.

### Roots

\[
x^2=0 \implies x=0,
\]

\[
x-1=0 \implies x=1.
\]

But `x=0` is repeated because the factor `x` appears twice.

### Behaviour at the root

At `x=0`, the graph touches the `x`-axis and turns back.

At `x=1`, the graph crosses the `x`-axis.

The evidence describes this as the curve crossing at `0`, then immediately crossing at `0` again, so it comes back on itself.

---

## 4. Triple Repeated Roots

Consider

\[
y=(x-4)^3.
\]

### Shape

The leading term is positive:

\[
(x-4)^3=x^3+\cdots
\]

so the curve is uphill.

### Root

\[
x-4=0 \implies x=4.
\]

This is a triple repeated root.

### `y`-intercept

Set `x=0`:

\[
y=(0-4)^3,
\]

\[
y=(-4)^3,
\]

\[
y=-64.
\]

So the curve passes through

\[
(0,-64).
\]

### Shape at `x=4`

The curve crosses the `x`-axis but becomes momentarily flat at the crossing. The evidence uses the phrase “point of inflection”, but also notes that this term has been removed from the new A Level syllabus, so it should not be treated as required CCEA vocabulary.

Use this safe CCEA wording:

> At the triple repeated root, the curve crosses the `x`-axis and is momentarily flat.

---

## 5. Cubics with Limited Real Roots

Consider

\[
y=(x+1)(x^2+x+1).
\]

### Shape

The leading term is

\[
x\cdot x^2=x^3,
\]

so the curve is a positive cubic.

### Roots

Set each factor equal to zero:

\[
x+1=0 \implies x=-1.
\]

Now test

\[
x^2+x+1=0.
\]

The discriminant is

\[
b^2-4ac.
\]

Here,

\[
a=1,\qquad b=1,\qquad c=1.
\]

So

\[
b^2-4ac=1^2-4(1)(1),
\]

\[
=1-4,
\]

\[
=-3.
\]

Since

\[
-3<0,
\]

the quadratic has no real roots.

Therefore the only real root is

\[
x=-1.
\]

The evidence notes that without differentiation, we do not have enough information to determine every turning-point detail exactly.

---

## 6. Finding the Equation from a Cubic Graph

If a graph crosses the `x`-axis at `x=-1`, it has a factor

\[
x+1.
\]

If it touches the `x`-axis at `x=2`, it has a repeated factor

\[
(x-2)^2.
\]

So a suitable cubic is

\[
y=(x-2)^2(x+1).
\]

Now expand carefully:

\[
y=(x-2)^2(x+1),
\]

\[
y=(x^2-4x+4)(x+1),
\]

\[
y=x^2(x+1)-4x(x+1)+4(x+1),
\]

\[
y=x^3+x^2-4x^2-4x+4x+4,
\]

\[
y=x^3-3x^2+0x+4,
\]

\[
y=x^3-3x^2+4.
\]

So if the question writes

\[
y=x^3+ax^2+bx+c,
\]

then

\[
a=-3,\qquad b=0,\qquad c=4.
\]

This worked example appears in the slide evidence as Edexcel C1 May 2013(R) Q9; it is cross-board, but the algebraic method is on-spec for CCEA AS1.

---

## 7. Reciprocal Graphs

## 7.1 The graph `y=1/x`

The graph

\[
y=\frac{1}{x}
\]

has two branches:

- one in the first quadrant;
- one in the third quadrant.

It has asymptotes:

\[
x=0,\qquad y=0.
\]

The graph approaches both axes but never touches them.

## 7.2 The graph `y=-3/x`

The graph

\[
y=-\frac{3}{x}
\]

has two branches:

- one in the second quadrant;
- one in the fourth quadrant.

It has the same asymptotes:

\[
x=0,\qquad y=0.
\]

The evidence notes that the scaling caused by `3` is not very visible if the graph is shown alone without scale, but it matters when comparing multiple graphs on the same axes.

## 7.3 The graph `y=a/x^2`

Because

\[
x^2>0
\]

for all

\[
x\ne 0,
\]

the sign of

\[
\frac{a}{x^2}
\]

is controlled by the sign of `a`.

If `a>0`, then

\[
y=\frac{a}{x^2}
\]

has two branches above the `x`-axis.

If `a<0`, then

\[
y=\frac{a}{x^2}
\]

has two branches below the `x`-axis.

The asymptotes are still:

\[
x=0,\qquad y=0.
\]

---

## 8. Points of Intersection

If

\[
y=f(x)
\]

and

\[
y=g(x),
\]

then the `x`-values of their points of intersection are found by solving

\[
f(x)=g(x).
\]

Graph intersections are simultaneous equations in disguise.

---

## 9. Transformations of Graphs

The transformation summary from the evidence is:

| Transformation | Effect |
|---|---|
| `y=f(x)+a` | Translation by `\begin{pmatrix}0\\a\end{pmatrix}` |
| `y=f(x+a)` | Translation by `\begin{pmatrix}-a\\0\end{pmatrix}` |
| `y=af(x)` | Stretch in the `y`-direction, scale factor `a` |
| `y=f(ax)` | Stretch in the `x`-direction, scale factor `1/a` |

The teacher transcript gives the key memory rule: outside the function affects `y`-coordinates and behaves as expected; inside the function affects `x`-coordinates and does the “opposite” of what many students expect.

### Reflections

\[
y=-f(x)
\]

negates all `y`-coordinates, so it is a reflection in the `x`-axis.

\[
y=f(-x)
\]

negates all `x`-coordinates, so it is a reflection in the `y`-axis.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1GraphsTransformationsSVG-001 | Source: CCEA specification map + DrFrost Chapter 4 PDF pages 3–6 | Insert from svg/AS1GraphsTransformationsSVG-001.svg | Purpose: Show the cubic sketching routine: shape, roots and `y`-intercept.]

[VISUAL PLACEHOLDER: AS1GraphsTransformationsSVG-002 | Source: DrFrost Chapter 4 PDF pages 6–8 | Insert from svg/AS1GraphsTransformationsSVG-002.svg | Purpose: Compare simple, repeated and triple repeated roots on the `x`-axis.]

[VISUAL PLACEHOLDER: AS1GraphsTransformationsSVG-003 | Source: DrFrost Chapter 4 PDF pages 17–19 | Insert from svg/AS1GraphsTransformationsSVG-003.svg | Purpose: Show `y=a/x`, `y=-a/x`, `y=a/x^2`, `y=-a/x^2` with asymptotes.]

[VISUAL PLACEHOLDER: AS1GraphsTransformationsSVG-004 | Source: DrFrost Chapter 4 PDF pages 21–23 | Insert from svg/AS1GraphsTransformationsSVG-004.svg | Purpose: Show intersections of `y=x(x-3)` and `y=x^2(1-x)` as graphical solutions.]

[VISUAL PLACEHOLDER: AS1GraphsTransformationsSVG-005 | Source: DrFrost Chapter 4 PDF pages 25–32 + teacher transcript | Insert from svg/AS1GraphsTransformationsSVG-005.svg | Purpose: Summarise inside/outside function transformations and coordinate effects.]

[INTERACTIVE PLACEHOLDER: AS1GraphsTransformationsWidget-001 | Source: CCEA AS1-AF-LO016 + DrFrost transformation evidence | Insert from widgets/AS1GraphsTransformationsWidget-001.html | Purpose: Slider widget for `y=af(x)`, `y=f(x)+a`, `y=f(x+a)`, `y=f(ax)`.]

---

## Worked Examples

## Worked Example 1 – Sketching a Cubic with Three Simple Roots

Sketch

\[
y=(x-2)(1-x)(1+x).
\]

### Step 1: Shape

Look only at the leading terms:

\[
x,\qquad -x,\qquad x.
\]

Multiply:

\[
x(-x)(x)=-x^3.
\]

So the graph is a negative cubic.

It goes downhill from left to right.

### Step 2: Roots

Set each factor equal to zero:

\[
x-2=0 \implies x=2,
\]

\[
1-x=0 \implies x=1,
\]

\[
1+x=0 \implies x=-1.
\]

So the roots are:

\[
x=-1,\qquad x=1,\qquad x=2.
\]

### Step 3: `y`-intercept

Set `x=0`:

\[
y=(0-2)(1-0)(1+0),
\]

\[
y=(-2)(1)(1),
\]

\[
y=-2.
\]

So the `y`-intercept is:

\[
(0,-2).
\]

### Sketch instructions

The sketch must:

- cross the `x`-axis at `-1`, `1`, and `2`;
- cross the `y`-axis at `-2`;
- have negative cubic shape.

---

## Worked Example 2 – Sketching a Cubic with a Repeated Root

Sketch

\[
y=x^2(x-1).
\]

### Step 1: Shape

\[
x^2(x-1)=x^3-x^2.
\]

The leading term is positive:

\[
x^3.
\]

So the graph is a positive cubic.

### Step 2: Roots

\[
x^2=0 \implies x=0,
\]

\[
x-1=0 \implies x=1.
\]

The root `x=0` is repeated because `x^2` means:

\[
x^2=x\cdot x.
\]

### Step 3: `y`-intercept

Set `x=0`:

\[
y=0^2(0-1),
\]

\[
y=0(-1),
\]

\[
y=0.
\]

### Sketch instructions

The sketch must:

- touch the `x`-axis at `x=0`;
- cross the `x`-axis at `x=1`;
- pass through the origin;
- have positive cubic shape.

---

## Worked Example 3 – Sketching a Cubic with a Triple Repeated Root

Sketch

\[
y=(x-4)^3.
\]

### Step 1: Shape

The leading term is

\[
x^3,
\]

so the graph is a positive cubic.

### Step 2: Root

\[
x-4=0,
\]

\[
x=4.
\]

The factor is cubed, so `x=4` is a triple repeated root.

### Step 3: `y`-intercept

Set `x=0`:

\[
y=(0-4)^3,
\]

\[
y=(-4)^3,
\]

\[
y=-64.
\]

### Sketch instructions

The sketch must:

- cross the `x`-axis at `x=4`;
- be momentarily flat at `x=4`;
- cross the `y`-axis at `-64`;
- have positive cubic shape.

---

## Worked Example 4 – A Cubic with Only One Real Root

Sketch

\[
y=(x+1)(x^2+x+1).
\]

### Step 1: Shape

The leading term is:

\[
x\cdot x^2=x^3.
\]

So the graph is a positive cubic.

### Step 2: Roots

First factor:

\[
x+1=0,
\]

\[
x=-1.
\]

Second factor:

\[
x^2+x+1=0.
\]

Use the discriminant:

\[
b^2-4ac=1^2-4(1)(1),
\]

\[
=1-4,
\]

\[
=-3.
\]

Since

\[
-3<0,
\]

there are no real roots from the quadratic factor.

### Step 3: `y`-intercept

Set `x=0`:

\[
y=(0+1)(0^2+0+1),
\]

\[
y=(1)(1),
\]

\[
y=1.
\]

### Sketch instructions

The sketch must:

- cross the `x`-axis at `x=-1`;
- cross the `y`-axis at `1`;
- have positive cubic shape;
- not invent extra real roots.

---

## Worked Example 5 – Finding the Equation from a Cubic Sketch

A curve crosses the `x`-axis at

\[
(-1,0)
\]

and touches the `x`-axis at

\[
(2,0).
\]

The curve has equation

\[
y=x^3+ax^2+bx+c.
\]

Find `a`, `b`, and `c`.

### Step 1: Convert graph features into factors

Crosses at `x=-1`:

\[
x=-1 \implies x+1=0,
\]

so the factor is

\[
x+1.
\]

Touches at `x=2`:

\[
x=2 \implies x-2=0.
\]

Touching means repeated root, so the factor is:

\[
(x-2)^2.
\]

Thus:

\[
y=(x-2)^2(x+1).
\]

### Step 2: Expand

\[
y=(x-2)^2(x+1),
\]

\[
y=(x^2-4x+4)(x+1),
\]

\[
y=x^2(x+1)-4x(x+1)+4(x+1),
\]

\[
y=x^3+x^2-4x^2-4x+4x+4,
\]

\[
y=x^3-3x^2+4.
\]

### Step 3: Compare coefficients

\[
x^3+ax^2+bx+c=x^3-3x^2+0x+4.
\]

Therefore:

\[
a=-3,\qquad b=0,\qquad c=4.
\]

---

## Worked Example 6 – Reciprocal Graphs

Sketch

\[
y=-\frac{3}{x^2}.
\]

### Step 1: Identify the family

This is of the form

\[
y=\frac{a}{x^2}
\]

with

\[
a=-3.
\]

### Step 2: Use the sign

Since

\[
x^2>0
\]

for every

\[
x\ne0,
\]

the denominator is always positive.

So

\[
-\frac{3}{x^2}<0.
\]

The graph lies below the `x`-axis.

### Step 3: Asymptotes

The graph has vertical asymptote:

\[
x=0,
\]

and horizontal asymptote:

\[
y=0.
\]

### Sketch instructions

The sketch must show:

- two branches below the `x`-axis;
- symmetry about the `y`-axis;
- dotted asymptotes `x=0` and `y=0`.

---

## Worked Example 7 – Points of Intersection

On the same diagram sketch:

\[
y=x(x-3)
\]

and

\[
y=x^2(1-x).
\]

Find their points of intersection.

### Step 1: Equate the two expressions

\[
x(x-3)=x^2(1-x).
\]

### Step 2: Expand both sides

Left-hand side:

\[
x(x-3)=x^2-3x.
\]

Right-hand side:

\[
x^2(1-x)=x^2-x^3.
\]

So:

\[
x^2-3x=x^2-x^3.
\]

### Step 3: Rearrange to zero

Subtract `x^2` from both sides:

\[
-3x=-x^3.
\]

Add `x^3` to both sides:

\[
x^3-3x=0.
\]

### Step 4: Factorise

\[
x^3-3x=x(x^2-3).
\]

So:

\[
x(x^2-3)=0.
\]

### Step 5: Solve

\[
x=0
\]

or

\[
x^2-3=0.
\]

So:

\[
x^2=3,
\]

\[
x=\pm\sqrt3.
\]

### Step 6: Substitute to find `y`-coordinates

Use

\[
y=x(x-3).
\]

For `x=0`:

\[
y=0(0-3)=0.
\]

Point:

\[
(0,0).
\]

For `x=\sqrt3`:

\[
y=\sqrt3(\sqrt3-3),
\]

\[
y=3-3\sqrt3.
\]

Point:

\[
(\sqrt3,\;3-3\sqrt3).
\]

For `x=-\sqrt3`:

\[
y=(-\sqrt3)(-\sqrt3-3),
\]

\[
y=(-\sqrt3)(-\sqrt3)+(-\sqrt3)(-3),
\]

\[
y=3+3\sqrt3.
\]

Point:

\[
(-\sqrt3,\;3+3\sqrt3).
\]

### Final answer

\[
\boxed{(-\sqrt3,\;3+3\sqrt3),\quad (0,0),\quad (\sqrt3,\;3-3\sqrt3)}
\]

The slide warns not to divide by `x`, because that would lose the solution `x=0`.

---

## Worked Example 8 – Showing There Are No Further Intersections

On the same diagram sketch:

\[
y=x(x-4)
\]

and

\[
y=x(x-2)^2.
\]

Find the coordinates of any points of intersection.

### Step 1: Equate the two equations

\[
x(x-2)^2=x(x-4).
\]

### Step 2: Expand the squared bracket

\[
(x-2)^2=x^2-4x+4.
\]

So:

\[
x(x^2-4x+4)=x(x-4).
\]

### Step 3: Expand both sides

Left-hand side:

\[
x(x^2-4x+4)=x^3-4x^2+4x.
\]

Right-hand side:

\[
x(x-4)=x^2-4x.
\]

So:

\[
x^3-4x^2+4x=x^2-4x.
\]

### Step 4: Rearrange to zero

Subtract `x^2` from both sides:

\[
x^3-5x^2+4x=-4x.
\]

Add `4x` to both sides:

\[
x^3-5x^2+8x=0.
\]

### Step 5: Factorise

\[
x(x^2-5x+8)=0.
\]

So:

\[
x=0
\]

or

\[
x^2-5x+8=0.
\]

### Step 6: Use the discriminant

For

\[
x^2-5x+8=0,
\]

we have:

\[
a=1,\qquad b=-5,\qquad c=8.
\]

The discriminant is:

\[
b^2-4ac=(-5)^2-4(1)(8),
\]

\[
=25-32,
\]

\[
=-7.
\]

Since

\[
-7<0,
\]

there are no real roots from the quadratic.

Therefore the only intersection is from

\[
x=0.
\]

Substitute into either graph:

\[
y=0(0-4)=0.
\]

### Final answer

\[
\boxed{(0,0)}
\]

---

## Worked Example 9 – Transformation: `y=f(x+2)`

Suppose

\[
f(x)=x^2.
\]

Then

\[
f(x+2)=(x+2)^2.
\]

The graph

\[
y=x^2
\]

has its turning point at

\[
(0,0).
\]

The graph

\[
y=(x+2)^2
\]

has its turning point at

\[
(-2,0).
\]

So:

\[
y=f(x+2)
\]

is a translation by

\[
\begin{pmatrix}-2\\0\end{pmatrix}.
\]

This is the classic inside-the-function reversal: `+2` inside means move left `2`.

---

## Worked Example 10 – Transformation: `y=x^2+3`

Sketch

\[
y=x^2+3.
\]

Think of

\[
f(x)=x^2.
\]

Then:

\[
y=f(x)+3.
\]

The `+3` is outside the function, so it affects `y`-coordinates as expected.

Translation:

\[
\begin{pmatrix}0\\3\end{pmatrix}.
\]

The turning point moves from:

\[
(0,0)
\]

to

\[
(0,3).
\]

The graph has no real roots because

\[
x^2+3=0
\]

would require

\[
x^2=-3,
\]

which has no real solutions.

---

## Worked Example 11 – Transformation of a Reciprocal Graph

Sketch

\[
y=\frac{2}{x+1}.
\]

Start with

\[
y=\frac{2}{x}.
\]

The `+1` is inside the denominator, so the graph moves left by `1`.

### Vertical asymptote

Originally:

\[
x=0.
\]

After moving left `1`:

\[
x=-1.
\]

### Horizontal asymptote

The horizontal asymptote remains:

\[
y=0.
\]

### `x`-intercept

Solve:

\[
\frac{2}{x+1}=0.
\]

There is no value of `x` that makes the numerator `2` become `0`, so there is no `x`-intercept.

### `y`-intercept

Set `x=0`:

\[
y=\frac{2}{0+1},
\]

\[
y=2.
\]

So the `y`-intercept is:

\[
(0,2).
\]

### Sketch instructions

The sketch must show:

- vertical asymptote `x=-1`;
- horizontal asymptote `y=0`;
- `y`-intercept `(0,2)`;
- no `x`-intercept.

The evidence warns that transformations can create new intercepts or roots, so you must still check intercepts after transforming.

---

## Worked Example 12 – Effects on Specific Points

Suppose a graph

\[
y=f(x)
\]

contains the points:

\[
(4,3),\qquad (1,0),\qquad (6,-4).
\]

Find where these points go under each transformation.

### 1. `y=f(x+1)`

Inside `+1` means subtract `1` from each `x`-coordinate.

\[
(4,3)\to(3,3),
\]

\[
(1,0)\to(0,0),
\]

\[
(6,-4)\to(5,-4).
\]

### 2. `y=f(2x)`

Inside multiplying by `2` means multiply `x`-coordinates by `1/2`.

\[
(4,3)\to(2,3),
\]

\[
(1,0)\to\left(\frac12,0\right),
\]

\[
(6,-4)\to(3,-4).
\]

### 3. `y=3f(x)`

Outside multiplying by `3` means multiply `y`-coordinates by `3`.

\[
(4,3)\to(4,9),
\]

\[
(1,0)\to(1,0),
\]

\[
(6,-4)\to(6,-12).
\]

### 4. `y=f(x)-1`

Outside subtracting `1` means subtract `1` from each `y`-coordinate.

\[
(4,3)\to(4,2),
\]

\[
(1,0)\to(1,-1),
\]

\[
(6,-4)\to(6,-5).
\]

### 5. `y=f(x/4)`

Inside multiplying `x` by `1/4` means multiply `x`-coordinates by `4`.

\[
(4,3)\to(16,3),
\]

\[
(1,0)\to(4,0),
\]

\[
(6,-4)\to(24,-4).
\]

### 6. `y=f(-x)`

Inside negating `x` means negate each `x`-coordinate.

\[
(4,3)\to(-4,3),
\]

\[
(1,0)\to(-1,0),
\]

\[
(6,-4)\to(-6,-4).
\]

### 7. `y=-f(x)`

Outside negating the function means negate each `y`-coordinate.

\[
(4,3)\to(4,-3),
\]

\[
(1,0)\to(1,0),
\]

\[
(6,-4)\to(6,4).
\]

---

## Guided Practice

### Question 1

Sketch

\[
y=x(x-3)^2.
\]

Show the shape, roots and `y`-intercept.

### Question 2

Sketch

\[
y=-(x+2)^3.
\]

Show the root and `y`-intercept.

### Question 3

Sketch

\[
y=\frac{2}{x+1},
\]

showing asymptotes and intercepts.

### Question 4

Find the points of intersection of

\[
y=x(x-3)
\]

and

\[
y=x^2(1-x).
\]

### Question 5

A graph

\[
y=f(x)
\]

passes through

\[
(4,3),\qquad (1,0),\qquad (6,-4).
\]

Find the images of these points under:

\[
y=f(2x),\qquad y=3f(x),\qquad y=f(-x),\qquad y=-f(x).
\]

### Question 6

A cubic crosses the `x`-axis at `x=-2` and touches the `x`-axis at `x=3`. Give a suitable equation for the graph.

---

## Common Mistakes and Exam Traps

| Trap | Why it is dangerous | Safer habit |
|---|---|---|
| Forgetting an intercept | The evidence explicitly warns this is easy to do | Always run the three-feature checklist |
| Expanding when unnecessary | It wastes time and invites sign errors | Use factorised form to get roots |
| Dividing by `x` in an equation | You may lose `x=0` as a solution | Factorise instead |
| Saying “doesn’t factorise” to prove no real roots | Not enough for a proof | Use the discriminant |
| Treating `f(x+a)` as moving right | It moves left by `a` | Inside changes affect `x`-coordinates in the opposite way |
| Forgetting asymptotes on reciprocal sketches | Asymptotes are required in CCEA LO013 | Draw dotted lines and label them |
| Treating quartics as core CCEA AS1 polynomial sketching | Supplied CCEA boundary says degree `x<=3` | Log quartics as enrichment only |
| Using “point of inflection” as required vocabulary | Evidence says term removed from new A Level syllabus | Describe the shape instead |

---

## Exam Technique

A reliable graph-sketching routine:

\[
\boxed{1.\ \text{Identify family}}
\]

Is it cubic, reciprocal, transformed quadratic, or another known graph?

\[
\boxed{2.\ \text{Find shape}}
\]

For cubics, inspect the leading term.

\[
\boxed{3.\ \text{Find roots}}
\]

Set `y=0`, usually by setting factors equal to zero.

\[
\boxed{4.\ \text{Find } y\text{-intercept}}
\]

Set `x=0`.

\[
\boxed{5.\ \text{Find asymptotes if reciprocal}}
\]

For reciprocal graphs, label the asymptotes.

\[
\boxed{6.\ \text{Check transformation effects}}
\]

Outside `f`: `y`-coordinates.  
Inside `f`: `x`-coordinates, often opposite.

\[
\boxed{7.\ \text{For intersections, equate}}
\]

If the graphs are

\[
y=f(x),\qquad y=g(x),
\]

solve

\[
f(x)=g(x).
\]

---

## Full Worked Solutions

## Solution 1

Sketch

\[
y=x(x-3)^2.
\]

### Shape

The leading term is:

\[
x\cdot x^2=x^3.
\]

So this is a positive cubic.

### Roots

\[
x=0
\]

and

\[
x-3=0 \implies x=3.
\]

The factor `(x-3)^2` is repeated, so the graph touches the `x`-axis at `x=3`.

### `y`-intercept

Set `x=0`:

\[
y=0(0-3)^2,
\]

\[
y=0.
\]

### Final sketch description

The curve:

- crosses at `x=0`;
- touches at `x=3`;
- passes through `(0,0)`;
- has positive cubic shape.

---

## Solution 2

Sketch

\[
y=-(x+2)^3.
\]

### Shape

The leading term is:

\[
-x^3.
\]

So the curve is a negative cubic.

### Root

\[
x+2=0,
\]

\[
x=-2.
\]

This is a triple repeated root.

### `y`-intercept

Set `x=0`:

\[
y=-(0+2)^3,
\]

\[
y=-(2)^3,
\]

\[
y=-8.
\]

### Final sketch description

The curve:

- crosses the `x`-axis at `x=-2`;
- is momentarily flat at `x=-2`;
- crosses the `y`-axis at `-8`;
- has negative cubic shape.

---

## Solution 3

Sketch

\[
y=\frac{2}{x+1}.
\]

### Family

This is a transformed reciprocal graph.

Start from:

\[
y=\frac{2}{x}.
\]

### Transformation

The `+1` is inside the denominator, so the graph moves left by `1`.

### Asymptotes

Vertical asymptote:

\[
x=-1.
\]

Horizontal asymptote:

\[
y=0.
\]

### `x`-intercept

\[
\frac{2}{x+1}=0
\]

has no solution, since `2 != 0`.

### `y`-intercept

Set `x=0`:

\[
y=\frac{2}{0+1},
\]

\[
y=2.
\]

So:

\[
(0,2).
\]

### Final sketch description

The graph has:

- vertical asymptote `x=-1`;
- horizontal asymptote `y=0`;
- `y`-intercept `(0,2)`;
- no `x`-intercept.

---

## Solution 4

Find the intersections of

\[
y=x(x-3)
\]

and

\[
y=x^2(1-x).
\]

Equate:

\[
x(x-3)=x^2(1-x).
\]

Expand:

\[
x^2-3x=x^2-x^3.
\]

Subtract `x^2`:

\[
-3x=-x^3.
\]

Add `x^3`:

\[
x^3-3x=0.
\]

Factorise:

\[
x(x^2-3)=0.
\]

So:

\[
x=0
\]

or

\[
x^2-3=0.
\]

Thus:

\[
x=\pm\sqrt3.
\]

Now substitute into

\[
y=x(x-3).
\]

For `x=0`:

\[
y=0.
\]

For `x=\sqrt3`:

\[
y=\sqrt3(\sqrt3-3),
\]

\[
y=3-3\sqrt3.
\]

For `x=-\sqrt3`:

\[
y=(-\sqrt3)(-\sqrt3-3),
\]

\[
y=3+3\sqrt3.
\]

Final answer:

\[
\boxed{(-\sqrt3,\;3+3\sqrt3),\quad (0,0),\quad (\sqrt3,\;3-3\sqrt3)}
\]

---

## Solution 5

Original points:

\[
(4,3),\qquad (1,0),\qquad (6,-4).
\]

### Under `y=f(2x)`

Multiply `x`-coordinates by `1/2`:

\[
(4,3)\to(2,3),
\]

\[
(1,0)\to\left(\frac12,0\right),
\]

\[
(6,-4)\to(3,-4).
\]

### Under `y=3f(x)`

Multiply `y`-coordinates by `3`:

\[
(4,3)\to(4,9),
\]

\[
(1,0)\to(1,0),
\]

\[
(6,-4)\to(6,-12).
\]

### Under `y=f(-x)`

Negate `x`-coordinates:

\[
(4,3)\to(-4,3),
\]

\[
(1,0)\to(-1,0),
\]

\[
(6,-4)\to(-6,-4).
\]

### Under `y=-f(x)`

Negate `y`-coordinates:

\[
(4,3)\to(4,-3),
\]

\[
(1,0)\to(1,0),
\]

\[
(6,-4)\to(6,4).
\]

---

## Solution 6

A cubic crosses at `x=-2` and touches at `x=3`.

Crossing at `x=-2` gives factor:

\[
x+2.
\]

Touching at `x=3` gives repeated factor:

\[
(x-3)^2.
\]

A suitable equation is:

\[
\boxed{y=(x+2)(x-3)^2}.
\]

---

## Common CCEA-Style Wording

You should be ready for prompts like:

- “Sketch the curve with equation...”
- “Indicate any intercepts with the axes.”
- “State, with a reason, the number of real solutions...”
- “Use your sketch to explain...”
- “Find the coordinates of the points of intersection.”
- “Sketch the graph of `y=f(x+a)`.”
- “Describe the transformation from `y=f(x)` to...”

The phrase “with a reason” usually means the answer is not just a number. You need to say why the graph intersections, roots, asymptotes or discriminant support your conclusion.

---

## Syllabus Gap Check

| Area | Status |
|---|---|
| Cubic graph sketches | Covered |
| Reciprocal graphs `y=a/x` | Covered |
| Reciprocal graphs `y=a/x^2` | Covered |
| Asymptotes | Covered |
| Graph intersections | Covered |
| Algebraic interpretation of intersections | Covered |
| Transformations `y=af(x)` | Covered |
| Transformations `y=f(x)+a` | Covered |
| Transformations `y=f(x+a)` | Covered |
| Transformations `y=f(ax)` | Covered |
| Reflections as `a=-1` transformations | Covered |
| Quartic polynomial sketches | Excluded from core; evidence contains them, but supplied CCEA AS1 boundary says polynomial degree `x<=3` |
| Quintic/higher polynomial sketches | Excluded from core; evidence treats them as extension |
| Full Pearson exercise pages | Not supplied; not reproduced |

---

## Visual/Interactive Asset Plan

| Asset ID | Type | Purpose | File |
|---|---|---|---|
| `AS1GraphsTransformationsSVG-001` | SVG | Cubic sketching routine | `svg/AS1GraphsTransformationsSVG-001.svg` |
| `AS1GraphsTransformationsSVG-002` | SVG | Root multiplicity behaviour | `svg/AS1GraphsTransformationsSVG-002.svg` |
| `AS1GraphsTransformationsSVG-003` | SVG | Reciprocal graphs and asymptotes | `svg/AS1GraphsTransformationsSVG-003.svg` |
| `AS1GraphsTransformationsSVG-004` | SVG | Graph intersections | `svg/AS1GraphsTransformationsSVG-004.svg` |
| `AS1GraphsTransformationsSVG-005` | SVG | Transformation summary map | `svg/AS1GraphsTransformationsSVG-005.svg` |
| `AS1GraphsTransformationsTikZ-001` | TikZ | Clean printable cubic graph | `tikz/AS1GraphsTransformationsTikZ-001.tex` |
| `AS1GraphsTransformationsWidget-001` | HTML widget | Transformation slider/checker | `widgets/AS1GraphsTransformationsWidget-001.html` |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| DrFrost Chapter 4 PDF | Core lesson evidence, controlled by CCEA boundary |
| Teacher transcript | Core explanation evidence, controlled by CCEA boundary |
| Screenshot PDF | Visual reference only |
| Pearson exercise references in slides | Not reproduced unless visible in slides |
| Edexcel/MAT/STEP examples shown in slides | Cross-board; used only where on-spec and labelled as extension/support |
| External GCSE sources | Not used |

---

## Final Student Checklist

Before moving on, check that you can:

- [ ] Identify whether a cubic is positive or negative from its leading term.
- [ ] Find roots from factorised form.
- [ ] Find the `y`-intercept by setting `x=0`.
- [ ] Explain the difference between crossing, touching and triple repeated roots.
- [ ] Sketch `y=a/x` with asymptotes.
- [ ] Sketch `y=a/x^2` with asymptotes.
- [ ] Solve graph intersections by setting `f(x)=g(x)`.
- [ ] Avoid dividing by a variable when it might lose a solution.
- [ ] Use the discriminant to prove no further real roots.
- [ ] Apply `y=f(x)+a`, `y=f(x+a)`, `y=af(x)`, and `y=f(ax)`.
- [ ] Transform specific points correctly.
- [ ] Label asymptotes and intercepts clearly on sketches.
- [ ] Keep quartic sketches as enrichment, not CCEA AS1 core for this lesson.
