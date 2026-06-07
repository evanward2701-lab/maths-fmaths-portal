# A21 Parametric Equations

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-CG |
| Official topic area | Co-ordinate geometry in the \((x,y)\) plane |
| Lesson topic | Parametric Equations |
| Topic slug | parametric_equations |
| Topic Pascal | ParametricEquations |
| Topic ID | A21ParametricEquations |
| Lesson file | A21_parametric_equations_lesson.md |
| Learning outcome IDs | A21-CG-LO001, A21-CG-LO002 |
| Tags | #A21 #CoordinateGeometry #ParametricEquations #CartesianForm #Modelling |

---

## Evidence Map

| Evidence | Use in lesson |
|---|---|
| CCEA Mathematics Specification Map | Authority for unit code, topic code, topic area and LO IDs. |
| README-Module-Map.txt | Project naming, folder structure and phase conventions. |
| Source-Evidence-Drop-Checklist.txt | Missing evidence, off-spec logging and placeholder rules. |
| Chapter 8 Parametric Equations transcript | Core explanations, warnings, worked examples and modelling examples. |
| P2-Chp8-ParametricEquations.pptx | Topic sequence, visual planning and worked-example prompts. |
| Screenshot PDF | Visual support only; no uninspected visual detail is claimed. |

---

## Specification Alignment

### A21-CG-LO001

**Official wording:** demonstrate understanding of and use the parametric equations of curves and conversion between Cartesian and parametric forms.

Covered through:

- Cartesian versus parametric representations;
- parameter notation \(x=p(t), y=q(t)\);
- conversion by eliminating the parameter;
- conversion using identities such as \(\sin^2t+\cos^2t=1\);
- domain and range from parameter restrictions;
- sketching parametric curves;
- intersections with axes, lines and Cartesian curves.

### A21-CG-LO002

**Official wording:** use parametric equations in modelling in a variety of contexts.

Covered through:

- time as a parameter;
- two-dimensional motion models;
- plane motion;
- figure-skater motion;
- interpreting limitations of unrestricted domains.

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain the difference between a Cartesian equation and parametric equations.
2. Identify the parameter and explain how it generates \((x,y)\).
3. Convert simple parametric equations to Cartesian form.
4. Use trig identities to eliminate a trig parameter.
5. Find domain and range from the permitted parameter values.
6. Sketch a parametric curve by conversion or by a table of parameter values.
7. Find intersections by solving for the parameter first.
8. Use parametric equations in modelling and comment on realism.

---

## Prerequisite Recap

This lesson uses earlier A-Level content only.

| A-Level skill | Why it matters |
|---|---|
| Algebraic rearrangement | Needed to make \(t\) the subject and substitute. |
| Functions | Needed for domain and range. |
| Trigonometry | Needed for \(\sin\), \(\cos\), \(\tan\), radians and identities. |
| Exponentials/logarithms | Needed for examples involving \(e^x\) and \(\ln x\). |
| Coordinate geometry | Needed for circles, lines, axes and intersections. |
| Modelling language | Needed for time-parameter examples. |

---

## Big Picture Explanation

A Cartesian equation relates \(x\) and \(y\) directly. For example,

\[
x^2-y^2=5
\]

describes all points \((x,y)\) satisfying that one equation.

Parametric equations use a third variable, called a **parameter**, to generate both coordinates. For example,

\[
x=\sin t,\qquad y=t^2.
\]

For each value of \(t\):

\[
t \longrightarrow x(t),
\qquad
t \longrightarrow y(t),
\qquad
t \longrightarrow (x(t),y(t)).
\]

The parameter is the hidden clockwork. You see \((x,y)\) on the graph, but \(t\) is working behind the curtain.

---

## Key Definitions and Notation

### Cartesian equation

A **Cartesian equation** relates \(x\) and \(y\) directly.

Examples:

\[
y=x^2,\qquad x^2+y^2=25,\qquad x^2-y^2=5.
\]

### Parametric equations

A curve is given **parametrically** when

\[
x=p(t),\qquad y=q(t),
\]

where \(t\) is the parameter.

### Parameter

A **parameter** is a variable that generates the coordinates of the point on the curve. It is often \(t\), especially in motion problems, but it may also be \(\theta\).

### Domain and range

If

\[
x=p(t),\qquad y=q(t)
\]

can be written as

\[
y=f(x),
\]

then:

\[
\text{domain of }f=\text{possible values of }x=p(t),
\]

\[
\text{range of }f=\text{possible values of }y=q(t).
\]

---

## Core Theory

### 1. Converting from parametric to Cartesian form

To convert

\[
x=p(t),\qquad y=q(t)
\]

to Cartesian form:

1. choose the easier equation to rearrange;
2. make \(t\) the subject;
3. substitute into the other equation;
4. simplify until only \(x\) and \(y\) remain;
5. use the parameter restriction to state the domain and range.

This is called **eliminating the parameter**.

### 2. Example structure: \(x=2t,\ y=t^2\)

Given

\[
x=2t,
\]

make \(t\) the subject:

\[
t=\frac{x}{2}.
\]

Substitute into

\[
y=t^2:
\]

\[
y=\left(\frac{x}{2}\right)^2
\]

\[
y=\frac{x^2}{4}.
\]

So

\[
y=\frac14x^2.
\]

### 3. Trig-parametric conversion

When equations contain \(\sin t\) and \(\cos t\), use

\[
\sin^2t+\cos^2t=1.
\]

For

\[
x=\sin t+2,\qquad y=\cos t-3,
\]

we get

\[
\sin t=x-2
\]

and

\[
\cos t=y+3.
\]

Substitute into the identity:

\[
(x-2)^2+(y+3)^2=1.
\]

So the curve is a circle with centre

\[
(2,-3)
\]

and radius

\[
1.
\]

### 4. Restricted parameter intervals

If

\[
x=2t,\qquad y=t^2,\qquad -3<t<3,
\]

then the Cartesian equation is

\[
y=\frac14x^2.
\]

But the graph is not the full parabola.

From

\[
-3<t<3,
\]

multiply by \(2\):

\[
-6<2t<6.
\]

Since \(x=2t\),

\[
-6<x<6.
\]

For the range,

\[
y=t^2.
\]

Since \(t=0\) is allowed,

\[
y_{\min}=0.
\]

Since \(t\) approaches but never equals \(\pm3\),

\[
y<9.
\]

Therefore

\[
0\leq y<9.
\]

### 5. Sketching strategy

Use one of two methods.

#### Method A: Convert first

If the Cartesian form is recognisable, sketch that curve and then apply parameter restrictions.

Examples:

\[
y=\frac14x^2
\]

is a parabola, while

\[
(x-2)^2+(y+3)^2=1
\]

is a circle.

#### Method B: Use a table

If Cartesian form is awkward, choose parameter values and calculate points.

For example,

\[
x=\theta\cos\theta,\qquad y=\theta\sin\theta
\]

is better sketched by a table of \(\theta\)-values.

### 6. Intersections

To find an intersection, solve for the parameter first.

- On the \(x\)-axis, set \(y(t)=0\).
- On the \(y\)-axis, set \(x(t)=0\).
- With a line or Cartesian curve, substitute \(x(t)\) and \(y(t)\) into the Cartesian equation.

If

\[
x=t^2,\qquad y=4t
\]

and

\[
x+y+4=0,
\]

then

\[
t^2+4t+4=0.
\]

\[
(t+2)^2=0.
\]

\[
t=-2.
\]

Then

\[
x=(-2)^2=4,
\]

\[
y=4(-2)=-8.
\]

So the point is

\[
(4,-8).
\]

### 7. Modelling

In modelling, \(t\) often represents time. A plane can be modelled by

\[
x=v\cos\theta\,t,
\]

\[
y=v\sin\theta\,t.
\]

Here:

- \(v\) is speed;
- \(\theta\) is the angle of elevation;
- \(x\) is horizontal distance;
- \(y\) is vertical distance;
- \(t\) is time.

The domain of \(t\) must be realistic. A model with \(t>0\) forever may imply the plane climbs forever, which is not realistic.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-001 | Source: Screenshot PDF page 1 + transcript section 1 | Insert from svg/A21ParametricEquationsSVG-001.svg | Purpose: Compare a Cartesian curve with a parametric path.]

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-002 | Source: Transcript section 1 | Insert from svg/A21ParametricEquationsSVG-002.svg | Purpose: Show how \(-3<t<3\) trims \(y=\frac14x^2\).]

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-003 | Source: Transcript section 2 | Insert from svg/A21ParametricEquationsSVG-003.svg | Purpose: Show the circle generated by \(x=\sin t+2,\ y=\cos t-3\).]

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-004 | Source: Transcript section 4 | Insert from svg/A21ParametricEquationsSVG-004.svg | Purpose: Show sketching by parameter table.]

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-005 | Source: Transcript section 5 | Insert from svg/A21ParametricEquationsSVG-005.svg | Purpose: Show intersection by substitution into a line.]

[VISUAL PLACEHOLDER: A21ParametricEquationsSVG-006 | Source: Transcript modelling section | Insert from svg/A21ParametricEquationsSVG-006.svg | Purpose: Show plane motion with time as parameter.]

[INTERACTIVE PLACEHOLDER: A21ParametricEquationsWidget-001 | Source: Transcript sections 1 and 4 | Insert from widgets/A21ParametricEquationsWidget-001.html | Purpose: Slider for \(t\) showing how \(x(t)\) and \(y(t)\) generate a moving point.]

---

## Worked Examples

### Worked Example 1: Simple conversion with domain and range

Given

\[
x=2t,\qquad y=t^2,\qquad -3<t<3,
\]

find the Cartesian equation, domain and range.

\[
x=2t
\]

\[
t=\frac{x}{2}.
\]

Substitute:

\[
y=t^2
\]

\[
y=\left(\frac{x}{2}\right)^2
\]

\[
y=\frac{x^2}{4}.
\]

So

\[
\boxed{y=\frac14x^2}.
\]

Domain:

\[
-3<t<3
\]

\[
-6<2t<6
\]

\[
\boxed{-6<x<6}.
\]

Range:

\[
y=t^2.
\]

The minimum is

\[
0
\]

because \(t=0\) is allowed. The largest possible endpoint value would be

\[
9
\]

but \(t=\pm3\) is not allowed. Therefore

\[
\boxed{0\leq y<9}.
\]

### Worked Example 2: Logarithmic parametric equations

Given

\[
x=\ln(t+3),\qquad y=\frac{1}{t+5},\qquad t>-2,
\]

find the Cartesian equation, domain and range.

\[
x=\ln(t+3)
\]

\[
e^x=t+3
\]

\[
t=e^x-3.
\]

Substitute into \(y\):

\[
y=\frac{1}{t+5}
\]

\[
y=\frac{1}{(e^x-3)+5}
\]

\[
\boxed{y=\frac{1}{e^x+2}}.
\]

At \(t=-2\),

\[
x=\ln(-2+3)=\ln1=0.
\]

Since \(t>-2\),

\[
\boxed{x>0}.
\]

At \(t=-2\),

\[
y=\frac{1}{-2+5}=\frac13.
\]

But \(t=-2\) is excluded. As \(t\to\infty\), \(y\to0\) but never equals \(0\). Therefore

\[
\boxed{0<y<\frac13}.
\]

### Worked Example 3: Circle from trig equations

Given

\[
x=\sin t+2,\qquad y=\cos t-3,\qquad t\in\mathbb R,
\]

find the Cartesian equation.

\[
\sin t=x-2
\]

\[
\cos t=y+3.
\]

Use

\[
\sin^2t+\cos^2t=1.
\]

\[
(x-2)^2+(y+3)^2=1.
\]

So

\[
\boxed{(x-2)^2+(y+3)^2=1}.
\]

The centre is

\[
\boxed{(2,-3)}
\]

and the radius is

\[
\boxed{1}.
\]

### Worked Example 4: Using \(\sin 2t\)

Given

\[
x=\sin t,\qquad y=\sin 2t,\qquad -\frac{\pi}{2}\leq t\leq\frac{\pi}{2},
\]

find \(y=f(x)\), the domain and range.

Use

\[
\sin2t=2\sin t\cos t.
\]

Since \(x=\sin t\),

\[
y=2x\cos t.
\]

Use

\[
\cos^2t=1-\sin^2t.
\]

Since \(x=\sin t\),

\[
\cos^2t=1-x^2.
\]

On

\[
-\frac{\pi}{2}\leq t\leq\frac{\pi}{2},
\]

\[
\cos t\geq0.
\]

So

\[
\cos t=\sqrt{1-x^2}.
\]

Therefore

\[
\boxed{y=2x\sqrt{1-x^2}}.
\]

The domain is

\[
\boxed{-1\leq x\leq1}
\]

and the range is

\[
\boxed{-1\leq y\leq1}.
\]

### Worked Example 5: Double-angle identity producing a quadratic

Given

\[
x=2\sin t,\qquad y=1-\cos2t,
\]

use

\[
\cos2t=1-2\sin^2t.
\]

Then

\[
y=1-(1-2\sin^2t)
\]

\[
y=1-1+2\sin^2t
\]

\[
y=2\sin^2t.
\]

From

\[
x=2\sin t
\]

we get

\[
\sin t=\frac{x}{2}.
\]

So

\[
y=2\left(\frac{x}{2}\right)^2
\]

\[
y=\frac{x^2}{2}.
\]

Thus

\[
\boxed{y=\frac{x^2}{2}}.
\]

If \(-\frac{\pi}{2}\leq t\leq\frac{\pi}{2}\), then

\[
-2\leq x\leq2,
\]

so \(k=2\).

### Worked Example 6: Intersection with a line

A curve is given by

\[
x=t^2,\qquad y=4t.
\]

The line is

\[
x+y+4=0.
\]

Substitute:

\[
t^2+4t+4=0.
\]

\[
(t+2)^2=0.
\]

\[
t=-2.
\]

Then

\[
x=(-2)^2=4
\]

and

\[
y=4(-2)=-8.
\]

Therefore

\[
\boxed{(4,-8)}.
\]

### Worked Example 7: Plane model

A plane is modelled by

\[
x=v\cos\theta\,t,\qquad y=v\sin\theta\,t.
\]

When \(x=600\), \(y=120\):

\[
\frac{y}{x}
=
\frac{v\sin\theta\,t}{v\cos\theta\,t}
=
\tan\theta.
\]

So

\[
\tan\theta=\frac{120}{600}=\frac15.
\]

\[
\theta=\tan^{-1}\left(\frac15\right)\approx11.3^\circ.
\]

If \(v=50\),

\[
x=50\cos(11.3^\circ)t\approx49.03t
\]

and

\[
y=50\sin(11.3^\circ)t\approx9.81t.
\]

After \(10\) seconds:

\[
y\approx9.81(10)=98.1.
\]

To show straight-line motion:

\[
t=\frac{x}{49.03}.
\]

Substitute:

\[
y=9.81\left(\frac{x}{49.03}\right)
\]

\[
y\approx0.2x.
\]

The model is not realistic for all \(t>0\) because it implies the plane keeps climbing forever.

---

## Guided Practice

### Practice Question 1

Convert to Cartesian form and state the domain and range:

\[
x=3t,\qquad y=t^2+1,\qquad -2<t<4.
\]

### Practice Question 2

A curve is given by

\[
x=\ln(t+4),\qquad y=\frac{1}{t+6},\qquad t>-3.
\]

Find a Cartesian equation and state the domain and range.

### Practice Question 3

A curve is given by

\[
x=\cos t+1,\qquad y=\sin t-2,\qquad t\in\mathbb R.
\]

Find the Cartesian equation and identify the centre and radius.

### Practice Question 4

A curve is given by

\[
x=t^2,\qquad y=3t.
\]

Find where it intersects

\[
x+y-10=0.
\]

### Practice Question 5

A moving object is modelled by

\[
x=12t,\qquad y=5t,\qquad t>0.
\]

Show that the motion is a straight line and explain why the model may not be realistic for all \(t>0\).

---

## Common Mistakes and Exam Traps

### 1. Drawing the whole Cartesian curve

After converting to Cartesian form, still use the parameter restriction.

For

\[
x=2t,\quad y=t^2,\quad -3<t<3,
\]

the graph is not the whole of

\[
y=\frac14x^2.
\]

It is only

\[
-6<x<6,\qquad 0\leq y<9.
\]

### 2. Solving for \(t\), then stopping

A value of \(t\) is not a coordinate. Substitute back into both \(x(t)\) and \(y(t)\).

### 3. Converting to Cartesian form when not needed

For intersections, stay parametric where possible.

### 4. Only checking endpoints

For quadratic and trig functions, maxima and minima may occur inside the interval.

### 5. Forgetting radians

Many A2 trig-parametric examples use radians.

### 6. Ignoring model limitations

A model domain such as \(t>0\) may be mathematically tidy but physically unrealistic.

---

## Exam Technique Notes

| Wording | First move |
|---|---|
| Find a Cartesian equation | Eliminate the parameter. |
| State the domain | Find possible \(x=p(t)\) values. |
| State the range | Find possible \(y=q(t)\) values. |
| Sketch the curve | Convert if recognisable; otherwise use a table. |
| Crosses the \(x\)-axis | Set \(y(t)=0\). |
| Crosses the \(y\)-axis | Set \(x(t)=0\). |
| Meets a line or curve | Substitute \(x(t),y(t)\) into the Cartesian equation. |
| Modelling | Solve mathematically, then interpret in context. |

Useful identities:

\[
\sin^2t+\cos^2t=1,
\]

\[
\sin2t=2\sin t\cos t,
\]

\[
\cos2t=1-2\sin^2t,
\]

\[
\cos2t=2\cos^2t-1.
\]

---

## Full Worked Solutions to Guided Practice

### Solution 1

\[
x=3t
\]

\[
t=\frac{x}{3}.
\]

\[
y=t^2+1
\]

\[
y=\left(\frac{x}{3}\right)^2+1
\]

\[
\boxed{y=\frac{x^2}{9}+1}.
\]

Domain:

\[
-2<t<4
\]

\[
-6<3t<12
\]

\[
\boxed{-6<x<12}.
\]

Range:

\[
y=t^2+1.
\]

Since \(t=0\) is included,

\[
y_{\min}=1.
\]

As \(t\to4\),

\[
y\to17,
\]

but \(t=4\) is not included. Therefore

\[
\boxed{1\leq y<17}.
\]

### Solution 2

\[
x=\ln(t+4)
\]

\[
e^x=t+4
\]

\[
t=e^x-4.
\]

\[
y=\frac{1}{t+6}
\]

\[
y=\frac{1}{(e^x-4)+6}
\]

\[
\boxed{y=\frac{1}{e^x+2}}.
\]

At \(t=-3\),

\[
x=\ln1=0,
\]

so

\[
\boxed{x>0}.
\]

At \(t=-3\),

\[
y=\frac13,
\]

but the endpoint is excluded. As \(t\to\infty\), \(y\to0\). Therefore

\[
\boxed{0<y<\frac13}.
\]

### Solution 3

\[
x=\cos t+1
\]

\[
x-1=\cos t.
\]

\[
y=\sin t-2
\]

\[
y+2=\sin t.
\]

Use

\[
\sin^2t+\cos^2t=1.
\]

\[
(y+2)^2+(x-1)^2=1.
\]

So

\[
\boxed{(x-1)^2+(y+2)^2=1}.
\]

Centre:

\[
\boxed{(1,-2)}.
\]

Radius:

\[
\boxed{1}.
\]

### Solution 4

\[
x+y-10=0.
\]

Substitute:

\[
t^2+3t-10=0.
\]

Factorise:

\[
(t+5)(t-2)=0.
\]

So

\[
t=-5
\quad\text{or}\quad
t=2.
\]

For \(t=-5\):

\[
x=25,\qquad y=-15.
\]

For \(t=2\):

\[
x=4,\qquad y=6.
\]

Thus the intersections are

\[
\boxed{(25,-15)\text{ and }(4,6)}.
\]

### Solution 5

\[
x=12t
\]

\[
t=\frac{x}{12}.
\]

Substitute into \(y=5t\):

\[
y=5\left(\frac{x}{12}\right)
\]

\[
\boxed{y=\frac{5}{12}x}.
\]

This is a straight line. The model may not be realistic for all \(t>0\), because it says the object continues forever at the same horizontal and vertical rates.

---

## Syllabus Gap Check

| LO ID | Covered? | Evidence-backed lesson content |
|---|---|---|
| A21-CG-LO001 | Yes | Definitions, conversion, trig identities, domains/ranges, sketching and intersections. |
| A21-CG-LO002 | Yes | Time as a parameter, plane modelling and model limitations. |

Excluded from core:

- parametric differentiation;
- parametric integration;
- full Edexcel/Pearson mark-scheme analysis;
- reciprocal trig examples except as optional extension;
- non-parametric “just for fun” material.

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA specification map | Core authority. |
| Project README/module map | Project structure and metadata conventions. |
| Evidence checklist | Evidence handling, missing log and off-spec log. |
| Teacher transcript | Core lesson evidence where aligned with CCEA LO IDs. |
| DrFrost/Pearson/Edexcel references inside slides/transcript | Cross-board support only. |
| Screenshot PDF | Visual support only. |

---

## Final Student Checklist

- [ ] I can define a parameter.
- [ ] I can distinguish Cartesian and parametric form.
- [ ] I can eliminate \(t\) by substitution.
- [ ] I can use \(\sin^2t+\cos^2t=1\) in trig-parametric questions.
- [ ] I can use double-angle identities when needed.
- [ ] I can find the domain from possible \(x\)-values.
- [ ] I can find the range from possible \(y\)-values.
- [ ] I can avoid drawing the full Cartesian curve when \(t\) is restricted.
- [ ] I can find intersections by solving for \(t\) first.
- [ ] I can substitute back into both \(x(t)\) and \(y(t)\).
- [ ] I can interpret \(t\) as time in modelling questions.
- [ ] I can explain why a model may be unrealistic over an unlimited domain.
