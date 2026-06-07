# Off-Spec Enrichment Pack: Numerical Methods

> **Boundary label:** This is an **off-spec enrichment pack** for the CCEA Further Mathematics portal. It is not claimed as CCEA GCE Further Mathematics core content, and it does not satisfy any official CCEA Further Mathematics LO ID unless a later official source confirms otherwise.

---

# 1. Lesson Title and Metadata

| Field | Entry |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics portal, enrichment layer |
| Core specification status | Off-spec enrichment |
| Official CCEA unit | Not assigned |
| Official CCEA topic code | Not assigned |
| Official CCEA Further LO IDs | None assigned |
| Enrichment topic code | `OFFSPEC-NM` |
| Topic name | Numerical Methods |
| Topic slug | `offspec_numerical_methods` |
| Topic Pascal | `OffSpecNumericalMethods` |
| Topic ID | `OffSpecNumericalMethods` |
| Lesson file name | `offspec_numerical_methods_enrichment_lesson.md` |
| Enrichment objective IDs | `ENR-NM-001` to `ENR-NM-010`, non-official |
| Bridge tags | differentiation, gradient, integration, trapezium rule, differential equations, modelling |
| Topic tags | Euler method, midpoint method, second-order finite difference, Simpson rule, vector field, numerical approximation |

## Enrichment Objectives

| Enrichment objective ID | Objective |
|---|---|
| `ENR-NM-001` | Explain why numerical methods are useful when a differential equation or integral cannot be solved analytically. |
| `ENR-NM-002` | Interpret a vector field, tangent field or compass point diagram as a display of local gradients. |
| `ENR-NM-003` | Use Euler’s method to estimate values of a first-order differential equation solution. |
| `ENR-NM-004` | Organise Euler calculations using a table of \(n\), \(x_n\), \(y_n\), and derivative values. |
| `ENR-NM-005` | Use the midpoint method, remembering that an Euler step is usually needed first. |
| `ENR-NM-006` | Use the second-order finite-difference approximation for \(\frac{d^2y}{dx^2}\). |
| `ENR-NM-007` | Distinguish second-order Type A questions from Type B questions. |
| `ENR-NM-008` | Use simultaneous equations when midpoint and second-order formulae must both be satisfied. |
| `ENR-NM-009` | Apply Simpson’s rule to estimate definite integrals from tabulated values. |
| `ENR-NM-010` | Identify common numerical-method traps: step size, units, radians, variable changes, rounding and method display. |

---

# 2. Evidence Map

| Source | Type | Role in this enrichment pack | Boundary status |
|---|---|---|---|
| `FP1-Chp8-NumericalMethods.pdf` | Cross-board Further Pure 1 PDF | Main mathematical enrichment source for Euler, midpoint, second-order methods and Simpson’s rule | Off-spec for inspected CCEA Further core |
| `Chapter_8_Numerical_Methods_🧩_(Further_Pure_1)_screenshots.pdf` | Screenshot PDF | Visual evidence for chapter layout, diagrams, annotations and worked examples | Off-spec for inspected CCEA Further core |
| `transcripts.md` | Teacher transcript | Pedagogical wording, warnings, examples and method sequencing | Off-spec for inspected CCEA Further core |
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Project source | Boundary authority | No matching CCEA Further numerical-methods topic found |
| `Further_Maths_README_module_map.md` | Project source | Workflow authority | Requires exact CCEA topic codes and LO IDs for core lessons |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Project source | Boundary-control authority | Requires off-spec logging and honest missing-evidence logging |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Project source | Bridge context only | Ordinary Maths bridge, not Further Maths authority |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Project source | Bridge context only | Ordinary Maths bridge, not Further Maths authority |

---

# 3. Specification Alignment

## CCEA Further Mathematics Core Alignment

No official CCEA Further Mathematics LO ID was found for the numerical-methods content in the inspected CCEA Further Mathematics specification map.

| Official CCEA Further LO ID | Official wording | Coverage in this enrichment pack | Status |
|---|---|---|---|
| None found | None found | No official CCEA Further Maths LO is claimed | No core alignment |

## Related, but Not Authorising, Neighbour Topics

| Related area | Relationship | Boundary warning |
|---|---|---|
| Differential equations | This pack approximates solutions to differential equations numerically. | Inspected CCEA Further differential equations focus on analytical methods, not Euler/midpoint numerical stepping. |
| Modelling | Context examples use differential equations to model populations or quantities. | A modelling overlap does not authorise these numerical methods as CCEA Further core. |
| Integration | Simpson’s rule estimates definite integrals numerically. | Simpson’s rule was not found as CCEA Further core in the inspected map. |

---

# 4. Learning Objectives

## Core Enrichment Objectives

By the end of this enrichment lesson, the student should be able to:

1. Explain the difference between solving a differential equation analytically and approximating its solution numerically.
2. Interpret a vector field as a picture of local gradients.
3. Use Euler’s method to move from \((x_n,y_n)\) to \((x_{n+1},y_{n+1})\).
4. Rearrange the Euler approximation formula into an iterative formula.
5. Use tables to organise numerical iteration.
6. Use the midpoint method, remembering that an Euler step is usually needed first.
7. Use the second-order finite-difference approximation.
8. Decide whether a second-order question is Type A or Type B.
9. Solve Type B second-order questions using simultaneous equations.
10. Apply Simpson’s rule to approximate a definite integral.

## Bridge Objectives

The student should connect this pack to ordinary A-Level Mathematics by recognising that:

- \(\frac{dy}{dx}\) is a gradient or rate of change;
- a tangent gives a local straight-line approximation to a curve;
- integration can solve some differential equations exactly;
- numerical methods are used when exact algebra is unavailable, impractical or not required;
- trapezium rule approximates area using straight edges, while Simpson’s rule approximates using quadratic arcs.

---

# 5. Explicit Prerequisite Recap

## GCSE Foundations

The student should already be comfortable with substituting values into formulae, working with fractions and decimals, rounding to requested accuracy, using coordinates, and recognising gradients from rise over run.

\[
\text{gradient}=\frac{\text{change in }y}{\text{change in }x}=\frac{y_2-y_1}{x_2-x_1}.
\]

This ordinary gradient formula becomes the small engine inside Euler’s method and the midpoint method.

## Ordinary A-Level Maths Foundations

The student should already know differentiation as rate of change, \(\frac{dy}{dx}\) as gradient of a curve, integration as reverse differentiation, simple differential equations solved by direct integration, numerical approximation and the trapezium rule.

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Differentiation | \(\frac{dy}{dx}\) gives the gradient of a curve at a point. | In this enrichment topic, the gradient becomes a direction for stepping from one approximate point to the next. | A local tangent is only locally accurate. The approximation drifts from the true curve. |
| Integration | Some differential equations can be solved by integrating both sides. | Numerical methods are used when an exact solution is unavailable or awkward. | Do not assume every differential equation can be integrated neatly. |
| Trapezium rule | Definite integrals can be approximated by straight-edged strips. | Simpson’s rule uses quadratic arcs rather than straight-line trapezia. | Simpson’s rule needs an even number of intervals. |
| Numerical methods | Iteration and approximation require careful rounding and stopping rules. | The iteration now follows derivatives and differential equations. | Rounding too early can spoil later values. |
| Modelling | Variables may represent real quantities such as time, population or value. | Differential equations can model changing systems, then numerical methods estimate future values. | Units matter. If \(t\) is in years, four months is \(\frac13\), not \(4\). |

In ordinary A-Level Maths, this idea appeared as gradient, integration and numerical approximation. In this enrichment pack, the same idea becomes a way of walking along a solution curve one small step at a time. The key upgrade is that \(\frac{dy}{dx}\) is no longer just something to calculate; it becomes a local instruction: from here, move in this direction. The danger is that a local instruction is not the whole curve. Every step is a tiny guess, and the guesses can accumulate into visible error.

---

# 6. Big Picture Explanation

A differential equation tells us how a quantity changes. For example,

\[
\frac{dy}{dx}=2x
\]

does not directly say what \(y\) is. It says how \(y\) changes as \(x\) changes. In this simple case, we can solve analytically:

\[
y=\int 2x\,dx=x^2+c.
\]

But an equation such as

\[
\frac{dy}{dx}=x^2+y^3
\]

does not usually give a neat school-level explicit expression \(y=f(x)\). Numerical methods still let us estimate values of the solution.

| Analytical solution | Numerical solution |
|---|---|
| Gives an exact equation such as \(y=x^2+c\). | Gives approximate points such as \(y(4)\approx -2.16\). |
| May be impossible or too difficult. | Often possible with repeated arithmetic. |
| Describes the whole solution curve. | Describes selected points on a particular solution curve. |
| Usually elegant. | Usually tabular, repetitive and calculator-heavy. |

A vector field, tangent field or compass point diagram draws many little line segments, each one showing the local gradient at that point. These small direction marks are like mathematical weather vanes: each tells you which way the curve wants to move at that coordinate.

---

# 7. Key Definitions and Notation

## Differential Equation

A **differential equation** is an equation involving a derivative, for example:

\[
\frac{dy}{dx}=2x,\qquad \frac{dy}{dx}=x^2+y^3,\qquad \frac{d^2y}{dx^2}=x^2+y^2+\frac{dy}{dx}.
\]

## Analytical Solution

An **analytical solution** gives a direct relationship between variables, usually an equation such as \(y=f(x)\) or \(F(x,y)=0\).

## Numerical Solution

A **numerical solution** gives approximate values, often using repeated calculations:

\[
(x_0,y_0),\quad (x_1,y_1),\quad (x_2,y_2),\ldots
\]

## Step Size

The **step size** is usually denoted by \(h\). It is the change in the independent variable between consecutive points.

If \(x_0=3\), \(x_1=3.5\), and \(x_2=4\), then

\[
h=3.5-3=0.5.
\]

## Subscript Notation

\(x_n\) and \(y_n\) mean the \(x\)-value and \(y\)-value at the \(n\)th step. The notation

\[
\left(\frac{dy}{dx}\right)_n
\]

means the derivative evaluated at \((x_n,y_n)\).

## Euler’s Method

Euler’s method uses

\[
\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_n}{h}.
\]

Rearranging:

\[
y_{n+1}\approx y_n+h\left(\frac{dy}{dx}\right)_n.
\]

The corresponding \(x\)-value is

\[
x_{n+1}=x_n+h.
\]

## Midpoint Method

The midpoint method uses

\[
\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_{n-1}}{2h}.
\]

Rearranging:

\[
y_{n+1}\approx y_{n-1}+2h\left(\frac{dy}{dx}\right)_n.
\]

## Second-Order Numerical Formula

For second-order differential equations,

\[
\left(\frac{d^2y}{dx^2}\right)_n\approx \frac{y_{n+1}-2y_n+y_{n-1}}{h^2}.
\]

Rearranging:

\[
y_{n+1}\approx 2y_n-y_{n-1}+h^2\left(\frac{d^2y}{dx^2}\right)_n.
\]

## Simpson’s Rule

For an even number of intervals,

\[
\int_a^b f(x)\,dx\approx \frac{h}{3}\left[(\text{endpoints})+4(\text{odd values})+2(\text{even values})\right].
\]

More explicitly, if the values are \(y_0,y_1,\ldots,y_N\), where \(N\) is even, then

\[
\int_a^b f(x)\,dx\approx \frac{h}{3}\left[y_0+y_N+4(y_1+y_3+\cdots+y_{N-1})+2(y_2+y_4+\cdots+y_{N-2})\right].
\]

---

# 8. Core Theory

## 8.1 Analytical versus Numerical Differential Equations

Suppose

\[
\frac{dy}{dx}=2x.
\]

Integrating both sides gives

\[
y=\int 2x\,dx=x^2+c.
\]

This gives the general solution. If a point is given, such as \((1,3)\), then

\[
3=1^2+c,
\]

so

\[
c=2.
\]

The particular solution is

\[
y=x^2+2.
\]

**Bridge Note:** In ordinary A-Level Maths, integration reversed differentiation. Here, the same idea explains what “solving a differential equation” means before numerical approximation begins.

Now consider

\[
\frac{dy}{dx}=x^2+y^3.
\]

This does not lead neatly to a school-level explicit expression \(y=f(x)\). Instead, we estimate points:

1. Start at a known point.
2. Use the differential equation to calculate the gradient there.
3. Move a small distance \(h\) in the \(x\)-direction.
4. Move vertically according to the gradient.
5. Repeat.

## 8.2 Vector Field Intuition

For

\[
\frac{dy}{dx}=2x,
\]

the gradient depends only on \(x\). At \(x=0\), \(\frac{dy}{dx}=0\), so tangent marks are horizontal. At \(x=1\), \(\frac{dy}{dx}=2\), so the tangent slopes upwards. Following the little tangent marks traces particular solution curves. Since the exact solution is \(y=x^2+c\), the curves are parabolas.

**Important enrichment warning:** Vector fields are used here for intuition only. Numerical-method questions usually require formulae and tables, not field sketches.

## 8.3 Numerically Getting the Next Point

Suppose

\[
\frac{dy}{dx}=x^2+y^3
\]

and start at \((1,0.5)\), with \(h=0.1\).

First calculate the gradient:

\[
\frac{dy}{dx}=1^2+(0.5)^3=1+0.125=1.125.
\]

The estimated change in \(y\) is

\[
0.1(1.125)=0.1125.
\]

So

\[
y_1=0.5+0.1125=0.6125,
\]

and

\[
x_1=1+0.1=1.1.
\]

The new estimated point is

\[
(1.1,0.6125).
\]

### Evidence Ambiguity Note

One parsed page from the supplied PDF appears to state \(y_1=0.5+0.1\times 1.125=0.6125\) but then gives the new point as \((1.1,0.625)\). The calculation supports \((1.1,0.6125)\), so this lesson preserves the ambiguity and uses the calculated value.

## 8.4 Deriving Euler’s Method

Start with

\[
\frac{dy}{dx}\approx \frac{\Delta y}{\Delta x}.
\]

Between nearby points \((x_n,y_n)\) and \((x_{n+1},y_{n+1})\),

\[
\Delta y=y_{n+1}-y_n,
\]

and

\[
\Delta x=x_{n+1}-x_n=h.
\]

Therefore

\[
\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_n}{h}.
\]

Multiply by \(h\):

\[
h\left(\frac{dy}{dx}\right)_n\approx y_{n+1}-y_n.
\]

Add \(y_n\):

\[
y_{n+1}\approx y_n+h\left(\frac{dy}{dx}\right)_n.
\]

This says:

> New \(y\)-value = old \(y\)-value + step size \(\times\) gradient at the old point.

**Bridge Note:** In ordinary A-Level Maths, tangent gradient tells you the slope at a point. Here, that slope becomes a short straight-line prediction for the next point on the curve.

## 8.5 Why Euler’s Method Has Error

Euler’s method uses the tangent direction at the current point. But a curve bends, so the tangent line and the curve separate as you move away from the starting point. Reducing \(h\) usually helps because each tangent step is shorter, but smaller \(h\) usually means more arithmetic.

## 8.6 Euler’s Method Table Layout

For \(\frac{dy}{dx}=F(x,y)\), a useful table is:

| \(n\) | \(x_n\) | \(y_n\) | \(\left(\frac{dy}{dx}\right)_n\) |
|---:|---:|---:|---:|
| 0 | \(x_0\) | \(y_0\) | \(F(x_0,y_0)\) |
| 1 | \(x_1\) | \(y_1\) | \(F(x_1,y_1)\) |
| 2 | \(x_2\) | \(y_2\) | \(F(x_2,y_2)\) |

The method is:

\[
\left(\frac{dy}{dx}\right)_0=F(x_0,y_0),
\]

\[
y_1=y_0+h\left(\frac{dy}{dx}\right)_0,
\]

\[
x_1=x_0+h,
\]

then repeat.

## 8.7 Euler Worked Example: Pure Form

Let \(y=f(x)\) satisfy

\[
\frac{dy}{dx}=\frac{x^2+y}{y^2-x},\qquad f(3)=-1.
\]

Use two iterations of Euler’s method to estimate \(f(4)\), giving the answer to 2 decimal places.

The starting condition gives

\[
x_0=3,\qquad y_0=-1.
\]

Two iterations to reach \(x=4\) give

\[
x_0=3,\quad x_1=3.5,\quad x_2=4,
\]

so

\[
h=0.5.
\]

First gradient:

\[
\left(\frac{dy}{dx}\right)_0=\frac{3^2+(-1)}{(-1)^2-3}=\frac{9-1}{1-3}=\frac{8}{-2}=-4.
\]

First Euler step:

\[
y_1=-1+0.5(-4)=-1-2=-3.
\]

Second gradient:

\[
\left(\frac{dy}{dx}\right)_1=\frac{3.5^2+(-3)}{(-3)^2-3.5}=\frac{12.25-3}{9-3.5}=\frac{9.25}{5.5}.
\]

Write as fractions:

\[
9.25=\frac{37}{4},\qquad 5.5=\frac{11}{2}.
\]

Therefore

\[
\left(\frac{dy}{dx}\right)_1=\frac{\frac{37}{4}}{\frac{11}{2}}=\frac{37}{4}\cdot \frac{2}{11}=\frac{37}{22}.
\]

Second Euler step:

\[
y_2=-3+0.5\left(\frac{37}{22}\right)=-3+\frac{37}{44}=-\frac{132}{44}+\frac{37}{44}=-\frac{95}{44}.
\]

As a decimal,

\[
-\frac{95}{44}=-2.159090\ldots
\]

so

\[
\boxed{f(4)\approx -2.16}.
\]

## 8.8 Euler’s Method in Context: Setup Traps

If a question uses \(R\) and \(t\), rewrite the Euler approximation as

\[
\left(\frac{dR}{dt}\right)_n\approx \frac{R_{n+1}-R_n}{h},
\]

so

\[
R_{n+1}\approx R_n+h\left(\frac{dR}{dt}\right)_n.
\]

If \(t\) is measured in years and the question asks for four months,

\[
4\text{ months}=\frac{4}{12}=\frac13\text{ years}.
\]

If two iterations are required from \(0\) to \(\frac13\), the step size is

\[
h=\frac{1/3}{2}=\frac16.
\]

If a trigonometric function appears in a calculus model, use radians unless the question explicitly says otherwise.

## 8.9 Midpoint Method

Euler’s method predicts using the tangent at the current point. The midpoint method tries to reduce this error by using the gradient at a middle point and looking one step backward and one step forward.

For equally spaced \(x\)-values \(x_{n-1}\), \(x_n\), \(x_{n+1}\), the total horizontal distance from \(x_{n-1}\) to \(x_{n+1}\) is \(2h\). So

\[
\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_{n-1}}{2h}.
\]

Rearranging:

\[
y_{n+1}\approx y_{n-1}+2h\left(\frac{dy}{dx}\right)_n.
\]

To use the midpoint method from the start, you usually need an Euler step first to estimate \(y_1\). Then the midpoint formula can estimate \(y_2\).

## 8.10 Midpoint Worked Example

Use the midpoint formula with \(h=0.25\) to estimate the value at \(x=0.5\) of the particular solution to

\[
\frac{dy}{dx}=\frac{xy+y}{y^2+x^2},
\]

which passes through \((0,2)\). Give the answer to 4 decimal places.

Known values:

\[
x_0=0,\quad y_0=2,
\]

\[
x_1=0.25,
\quad x_2=0.5.
\]

First use Euler:

\[
\left(\frac{dy}{dx}\right)_0=\frac{0\cdot2+2}{2^2+0^2}=\frac{2}{4}=\frac12.
\]

\[
y_1=2+0.25\left(\frac12\right)=2+0.125=2.125.
\]

Now calculate the gradient at \((0.25,2.125)\):

\[
\left(\frac{dy}{dx}\right)_1=\frac{0.25(2.125)+2.125}{(2.125)^2+(0.25)^2}.
\]

Using fractions,

\[
0.25=\frac14,\qquad 2.125=\frac{17}{8}.
\]

Numerator:

\[
\frac14\cdot\frac{17}{8}+\frac{17}{8}=\frac{17}{32}+\frac{68}{32}=\frac{85}{32}.
\]

Denominator:

\[
\left(\frac{17}{8}\right)^2+\left(\frac14\right)^2=\frac{289}{64}+\frac{4}{64}=\frac{293}{64}.
\]

So

\[
\left(\frac{dy}{dx}\right)_1=\frac{\frac{85}{32}}{\frac{293}{64}}=\frac{85}{32}\cdot\frac{64}{293}=\frac{170}{293}.
\]

Midpoint formula:

\[
y_2=y_0+2h\left(\frac{dy}{dx}\right)_1.
\]

\[
y_2=2+2(0.25)\left(\frac{170}{293}\right)=2+\frac12\cdot\frac{170}{293}=2+\frac{85}{293}.
\]

\[
y_2=\frac{586}{293}+\frac{85}{293}=\frac{671}{293}=2.290102\ldots
\]

Thus

\[
\boxed{y(0.5)\approx 2.2901}.
\]

## 8.11 Second-Order Numerical Formula

The second derivative measures the rate of change of gradient. Adjacent gradients are approximately

\[
\frac{y_1-y_0}{h}
\]

and

\[
\frac{y_0-y_{-1}}{h}.
\]

The change in gradient, divided by \(h\), gives

\[
\left(\frac{d^2y}{dx^2}\right)_0\approx \frac{\frac{y_1-y_0}{h}-\frac{y_0-y_{-1}}{h}}{h}.
\]

Simplify:

\[
\left(\frac{d^2y}{dx^2}\right)_0\approx \frac{y_1-2y_0+y_{-1}}{h^2}.
\]

In general,

\[
\left(\frac{d^2y}{dx^2}\right)_n\approx \frac{y_{n+1}-2y_n+y_{n-1}}{h^2}.
\]

Rearranged:

\[
y_{n+1}\approx 2y_n-y_{n-1}+h^2\left(\frac{d^2y}{dx^2}\right)_n.
\]

### Type A

If

\[
\frac{d^2y}{dx^2}=F(x,y),
\]

and no \(\frac{dy}{dx}\) appears on the right, use Euler first if needed, then the second-order formula.

### Type B

If

\[
\frac{d^2y}{dx^2}=F\left(x,y,\frac{dy}{dx}\right),
\]

then use the midpoint formula and the second-order formula together, often producing simultaneous equations.

## 8.12 Second-Order Type A Example

Suppose

\[
\frac{d^2x}{dt^2}=\sin(x+t),
\]

with

\[
t_0=0,\quad x_0=-1,\quad \left(\frac{dx}{dt}\right)_0=3,
\]

and \(h=0.1\).

Euler first:

\[
x_1=x_0+h\left(\frac{dx}{dt}\right)_0=-1+0.1(3)=-0.7.
\]

At \(t_1=0.1\),

\[
\left(\frac{d^2x}{dt^2}\right)_1=\sin(x_1+t_1)=\sin(-0.7+0.1)=\sin(-0.6).
\]

Using radians,

\[
\sin(-0.6)=-0.564642\ldots
\]

Then

\[
x_2=2x_1-x_0+h^2\left(\frac{d^2x}{dt^2}\right)_1.
\]

\[
x_2=2(-0.7)-(-1)+(0.1)^2(-0.564642\ldots).
\]

\[
x_2=-1.4+1-0.00564642\ldots=-0.40564642\ldots
\]

So

\[
\boxed{x(0.1)\approx -0.7000},\qquad \boxed{x(0.2)\approx -0.4056}.
\]

## 8.13 Second-Order Type B Example

Let

\[
\frac{d^2y}{dx^2}=x^2+y^2+\frac{dy}{dx}.
\]

At \(x_0=1\), suppose

\[
y_0=4,\qquad \left(\frac{dy}{dx}\right)_0=3,
\]

with \(h=0.2\). Estimate \(y\) when \(x=1.2\).

First,

\[
\left(\frac{d^2y}{dx^2}\right)_0=1^2+4^2+3=1+16+3=20.
\]

Midpoint formula:

\[
3=\frac{y_1-y_{-1}}{2(0.2)}=\frac{y_1-y_{-1}}{0.4}.
\]

So

\[
y_1-y_{-1}=1.2.\tag{1}
\]

Second-order formula:

\[
20=\frac{y_1-2(4)+y_{-1}}{(0.2)^2}=\frac{y_1-8+y_{-1}}{0.04}.
\]

Thus

\[
0.8=y_1-8+y_{-1},
\]

so

\[
y_1+y_{-1}=8.8.\tag{2}
\]

Add (1) and (2):

\[
2y_1=10,
\]

so

\[
y_1=5.
\]

Therefore

\[
\boxed{y(1.2)\approx 5}.
\]

## 8.14 Simpson’s Rule

The trapezium rule estimates area under a curve using straight-line strips. Simpson’s rule estimates area using quadratic arcs. For an even number of intervals,

\[
\int_a^b f(x)\,dx\approx \frac{h}{3}\left[y_0+y_N+4(y_1+y_3+\cdots+y_{N-1})+2(y_2+y_4+\cdots+y_{N-2})\right].
\]

Simpson’s rule needs an even number of intervals.

“Odd values” means odd subscripts \(y_1,y_3,y_5,\ldots\). “Even values” means internal even subscripts \(y_2,y_4,\ldots,y_{N-2}\). The endpoints \(y_0\) and \(y_N\) are not included in the even-values group.

## 8.15 Simpson’s Rule Example

Use Simpson’s rule with \(h=0.5\) to estimate

\[
\int_0^2 \left(e^{x^2}+\cos x+1\right)\,dx.
\]

Use the values:

| \(x\) | \(y=e^{x^2}+\cos x+1\) |
|---:|---:|
| 0 | 3 |
| 0.5 | 3.16161 |
| 1.0 | 4.25858 |
| 1.5 | 10.55847 |
| 2.0 | 55.18200 |

So

\[
y_0=3,\quad y_1=3.16161,\quad y_2=4.25858,\quad y_3=10.55847,\quad y_4=55.18200.
\]

With four intervals,

\[
\int_0^2 \left(e^{x^2}+\cos x+1\right)\,dx\approx \frac{0.5}{3}\left[y_0+y_4+4(y_1+y_3)+2y_2\right].
\]

Substitute:

\[
\approx \frac{0.5}{3}\left[3+55.18200+4(3.16161+10.55847)+2(4.25858)\right].
\]

Inside the bracket:

\[
3+55.18200=58.18200,
\]

\[
3.16161+10.55847=13.72008,
\]

\[
4(13.72008)=54.88032,
\]

\[
2(4.25858)=8.51716.
\]

Total:

\[
58.18200+54.88032+8.51716=121.57948.
\]

Thus

\[
\frac{0.5}{3}(121.57948)=20.263246\ldots
\]

So, to 3 significant figures,

\[
\boxed{20.3}.
\]

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsMermaid-001 | Source: AI-proposed teaching enhancement based on supplied FP1 Numerical Methods evidence | Insert from mermaid/OffSpecNumericalMethodsMermaid-001.md | Purpose: Show when a student should solve analytically and when a numerical method becomes useful. Brief description: A flowchart begins with “Can the differential equation or integral be solved exactly?” and branches to analytical solution, Euler/midpoint/second-order approximation, or Simpson’s rule.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsMermaid-002 | Source: AI-proposed teaching enhancement based on supplied transcript method sequence | Insert from mermaid/OffSpecNumericalMethodsMermaid-002.md | Purpose: Help students select the right enrichment method. Brief description: A method-choice flowchart separates first-order differential equations, second-order differential equations with no first-derivative term, second-order differential equations containing a first-derivative term, and numerical integration.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + supplied FP1 Numerical Methods enrichment evidence | Insert from svg/OffSpecNumericalMethodsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with the enrichment method. Brief description: Four columns show ordinary gradient, tangent approximation, trapezium rule, and direct integration, then connect them to Euler’s method, midpoint method, Simpson’s rule, and numerical differential-equation approximation.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsSVG-001 | Source: Supplied FP1 Numerical Methods PDF and screenshot evidence | Insert from svg/OffSpecNumericalMethodsSVG-001.svg | Purpose: Show how a differential equation defines local gradient directions. Brief description: The visual must show axes labelled \(x\) and \(y\), small blue tangent marks across the plane for \(\frac{dy}{dx}=2x\), a highlighted starting point, and several parabolic solution curves corresponding to different values of \(c\) in \(y=x^2+c\).]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsSVG-002 | Source: Supplied FP1 Numerical Methods PDF, screenshot evidence and transcript | Insert from svg/OffSpecNumericalMethodsSVG-002.svg | Purpose: Show the geometry of Euler’s method and why it introduces error. Brief description: The visual must show a curve, a starting point labelled \(y_0\), a step \(h\) in the \(x\)-direction, a vertical rise \(h(\frac{dy}{dx})_0\), a predicted point labelled \(y_1\), an actual point on the curve, and an error gap.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsSVG-003 | Source: Supplied FP1 Numerical Methods PDF and transcript | Insert from svg/OffSpecNumericalMethodsSVG-003.svg | Purpose: Explain why the midpoint method can reduce Euler’s error. Brief description: The visual must show three points \(P_{n-1}\), \(P_n\), \(P_{n+1}\), two intervals \(h\) and \(h\), total width \(2h\), a tangent at the middle point, and a predicted point closer to the curve than Euler’s predicted point.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsSVG-004 | Source: Supplied FP1 Numerical Methods PDF and transcript | Insert from svg/OffSpecNumericalMethodsSVG-004.svg | Purpose: Show the central-difference formula for the second derivative. Brief description: The visual must show three equally spaced points \(y_{n-1}\), \(y_n\), \(y_{n+1}\), with horizontal spacing \(h\), gradients on adjacent intervals, and the second derivative as the rate of change of gradient.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsSVG-005 | Source: Supplied FP1 Numerical Methods PDF and transcript | Insert from svg/OffSpecNumericalMethodsSVG-005.svg | Purpose: Compare trapezium rule with Simpson’s rule. Brief description: The visual must show a curve over \([a,b]\), straight trapezium approximation on one side, quadratic/parabolic arc approximation on the other, and labelled values \(y_0,y_1,y_2,y_3,y_4\).]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsTikZ-001 | Source: AI-proposed printable reconstruction of Euler diagram from supplied evidence | Insert from tikz/OffSpecNumericalMethodsTikZ-001.tex | Purpose: Provide a clean printable Euler method diagram. Brief description: A smooth increasing curve, a tangent line at \(P_0=(x_0,y_0)\), a horizontal step \(h\), a vertical step \(h(\frac{dy}{dx})_0\), and labels \(P_1^{\text{predicted}}\), \(P_1^{\text{actual}}\), and error.]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsTikZ-002 | Source: AI-proposed printable reconstruction of midpoint diagram from supplied evidence | Insert from tikz/OffSpecNumericalMethodsTikZ-002.tex | Purpose: Provide a precise midpoint-method diagram. Brief description: A curve with \(P_{n-1}\), \(P_n\), \(P_{n+1}\), a secant line from \(P_{n-1}\) to predicted \(P_{n+1}\), tangent at \(P_n\), and labels \(h\), \(h\), \(2h\).]

[VISUAL PLACEHOLDER: OffSpecNumericalMethodsTikZ-003 | Source: AI-proposed Simpson’s rule labelling diagram based on supplied evidence | Insert from tikz/OffSpecNumericalMethodsTikZ-003.tex | Purpose: Show endpoints, odd values and even values for Simpson’s rule. Brief description: An \(x\)-axis partitioned into equal intervals with ordinates \(y_0,y_1,y_2,y_3,y_4,y_5,y_6\), highlighting endpoints, odd-indexed values and internal even-indexed values.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: OffSpecNumericalMethodsWidget-001 | Source: AI-proposed teaching enhancement based on supplied Euler’s method evidence | Insert from widgets/OffSpecNumericalMethodsWidget-001.html | Purpose: Build an Euler iteration table and show how each row is calculated.]

[INTERACTIVE PLACEHOLDER: OffSpecNumericalMethodsWidget-002 | Source: AI-proposed teaching enhancement based on supplied midpoint method evidence | Insert from widgets/OffSpecNumericalMethodsWidget-002.html | Purpose: Show why midpoint method usually needs Euler’s method first.]

[INTERACTIVE PLACEHOLDER: OffSpecNumericalMethodsWidget-003 | Source: AI-proposed teaching enhancement based on supplied second-order method evidence | Insert from widgets/OffSpecNumericalMethodsWidget-003.html | Purpose: Help the student decide between Type A and Type B second-order numerical methods.]

[INTERACTIVE PLACEHOLDER: OffSpecNumericalMethodsWidget-004 | Source: AI-proposed teaching enhancement based on supplied Simpson’s rule evidence | Insert from widgets/OffSpecNumericalMethodsWidget-004.html | Purpose: Sort values into endpoints, odd values and even values, then apply Simpson’s rule.]

[INTERACTIVE PLACEHOLDER: OffSpecNumericalMethodsWidget-005 | Source: AI-proposed teaching enhancement based on supplied transcript warnings | Insert from widgets/OffSpecNumericalMethodsWidget-005.html | Purpose: Check common numerical-method setup errors before calculation.]

---

# 11. Worked Examples

The major evidence-backed worked examples are integrated into Section 8 so that each method is taught immediately before it is used. This section indexes them for revision.

| Worked example ID | Topic | Status | Full solution location |
|---|---|---|---|
| `WE-001` | Euler’s method, pure form | Off-spec enrichment | Section 8.7 |
| `WE-002` | Midpoint method | Off-spec enrichment | Section 8.10 |
| `WE-003` | Second-order Type A | Off-spec enrichment | Section 8.12 |
| `WE-004` | Second-order Type B | Off-spec enrichment | Section 8.13 |
| `WE-005` | Simpson’s rule | Off-spec enrichment | Section 8.15 |

## Additional Worked Example: Euler Extra Practice

Use Euler’s method to estimate the value at \(x=6\) of the particular solution to

\[
\frac{dy}{dx}=x^2-y^2,
\]

which passes through \((5,2)\), using \(h=0.5\).

Initial values:

\[
x_0=5,\quad y_0=2,\quad x_1=5.5,\quad x_2=6.
\]

First gradient:

\[
\left(\frac{dy}{dx}\right)_0=5^2-2^2=25-4=21.
\]

First Euler step:

\[
y_1=2+0.5(21)=2+10.5=12.5.
\]

Second gradient:

\[
\left(\frac{dy}{dx}\right)_1=(5.5)^2-(12.5)^2=30.25-156.25=-126.
\]

Second Euler step:

\[
y_2=12.5+0.5(-126)=12.5-63=-50.5.
\]

Therefore

\[
\boxed{y(6)\approx -50.5}.
\]

---

# 12. Common Mistakes and Exam Traps

## Boundary Trap

This lesson is off-spec enrichment. Do not list Euler’s method, midpoint method, second-order numerical methods or Simpson’s rule as official CCEA Further Maths content unless an official CCEA source later confirms it.

## Euler Formula Trap

Printed form:

\[
\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_n}{h}.
\]

Useful form:

\[
y_{n+1}\approx y_n+h\left(\frac{dy}{dx}\right)_n.
\]

## Wrong Gradient Point

Euler’s method uses the gradient at the current point, so use \(x_n,y_n\), not \(x_{n+1},y_{n+1}\), inside \(F\).

## Step Size Trap

If the target movement is from \(x=3\) to \(x=4\) in two steps, then

\[
h=\frac{4-3}{2}=\frac12.
\]

## Unit Trap

If \(t\) is measured in years:

\[
4\text{ months}=\frac13,
\quad
6\text{ months}=\frac12,
\quad
10\text{ months}=\frac56.
\]

## Radian Trap

If trigonometric functions appear in calculus contexts, use radians unless the question states otherwise.

## Midpoint Trap

Midpoint uses \(2h\):

\[
y_{n+1}\approx y_{n-1}+2h\left(\frac{dy}{dx}\right)_n.
\]

It often requires Euler first to create \(y_1\).

## Second-Order Sign Trap

The formula is

\[
\left(\frac{d^2y}{dx^2}\right)_n\approx \frac{y_{n+1}-2y_n+y_{n-1}}{h^2}.
\]

The middle term is \(-2y_n\), not \(+2y_n\).

## Simpson’s Rule Trap

Simpson’s rule uses

\[
\frac{h}{3}\left[(\text{endpoints})+4(\text{odd})+2(\text{internal even})\right].
\]

It needs an even number of intervals, and endpoints are not internal even values.

---

# 13. Practice Questions

All questions are AI-generated enrichment practice. They are not past-paper or textbook questions.

## Basic Fluency

1. The function \(y=f(x)\) satisfies \(\frac{dy}{dx}=x+y\). Given \(f(1)=2\), use one Euler step with \(h=0.2\) to estimate \(f(1.2)\).
2. The function \(y=f(x)\) satisfies \(\frac{dy}{dx}=x^2-y\). Given \(f(0)=3\), use two Euler steps with \(h=0.5\) to estimate \(f(1)\).
3. A question asks for two Euler iterations to estimate \(P\) when \(t=8\) months. The variable \(t\) is measured in years and starts at \(t=0\). Find \(h\).

## Bridge Questions

4. The differential equation \(\frac{dy}{dx}=4x^3\) can be solved analytically. Find the general solution and explain why Euler’s method is unnecessary unless requested.
5. A table has \(y_0,y_1,y_2,y_3,y_4\). Write the Simpson’s rule grouping and explain why \(y_0\) and \(y_4\) are not included in the even-values group.

## Standard Exam-Style Enrichment

6. The function \(y=f(x)\) satisfies \(\frac{dy}{dx}=\frac{x+y}{y}\). Given \(f(0)=2\), use the midpoint method with \(h=0.25\) to estimate \(f(0.5)\). Give your answer to 4 decimal places.
7. The function \(y=f(x)\) satisfies \(\frac{d^2y}{dx^2}=x+y\). At \(x=0\), \(y=1\) and \(\frac{dy}{dx}=2\). Use \(h=0.1\) to estimate \(y\) when \(x=0.1\) and \(x=0.2\).
8. The function \(y=f(x)\) satisfies \(\frac{d^2y}{dx^2}=x+y+\frac{dy}{dx}\). At \(x=2\), \(y=5\) and \(\frac{dy}{dx}=4\). Use \(h=0.5\) to estimate \(y\) when \(x=2.5\).

## Harder Synthesis

9. The value \(V\), in thousand pounds, of an asset satisfies \(\frac{dV}{dt}=0.4V+2t\). Initially \(V=15\) at \(t=0\). Use two Euler iterations to estimate \(V\) after six months. Interpret the answer.
10. Use Simpson’s rule with four intervals to estimate \(\int_0^2(x^3+2x+1)\,dx\). Show the table of values and give your answer exactly.
11. A student wants to use Simpson’s rule with values at \(x=0,1,2,3,4,5\). Explain whether Simpson’s rule can be applied directly over the whole interval.
12. Choose the method: Euler, midpoint, second-order Type A, second-order Type B, or Simpson’s rule, for each task described in the lesson.

---

# 14. Worked Solutions

## Solution 1

\[
\left(\frac{dy}{dx}\right)_0=x_0+y_0=1+2=3.
\]

\[
y_1=2+0.2(3)=2.6.
\]

\[
\boxed{f(1.2)\approx 2.6}
\]

## Solution 2

\[
\left(\frac{dy}{dx}\right)_0=0^2-3=-3.
\]

\[
y_1=3+0.5(-3)=1.5.
\]

\[
\left(\frac{dy}{dx}\right)_1=(0.5)^2-1.5=0.25-1.5=-1.25.
\]

\[
y_2=1.5+0.5(-1.25)=1.5-0.625=0.875.
\]

\[
\boxed{f(1)\approx 0.875}
\]

## Solution 3

\[
8\text{ months}=\frac{8}{12}=\frac23\text{ years}.
\]

Two iterations:

\[
h=\frac{2/3}{2}=\frac13.
\]

\[
\boxed{h=\frac13}
\]

## Solution 4

\[
y=\int 4x^3\,dx=4\cdot \frac{x^4}{4}+c=x^4+c.
\]

\[
\boxed{y=x^4+c}
\]

Euler’s method is unnecessary because the exact analytical solution is straightforward, unless the question specifically asks for numerical approximation.

## Solution 5

\[
\boxed{\frac{h}{3}\left[y_0+y_4+4(y_1+y_3)+2y_2\right]}.
\]

\(y_0\) and \(y_4\) are endpoints, so they are not part of the internal even-values group.

## Solution 6

\[
\left(\frac{dy}{dx}\right)_0=\frac{0+2}{2}=1.
\]

Euler first:

\[
y_1=2+0.25(1)=2.25.
\]

Midpoint gradient:

\[
\left(\frac{dy}{dx}\right)_1=\frac{0.25+2.25}{2.25}=\frac{2.5}{2.25}=\frac{10}{9}.
\]

Midpoint step:

\[
y_2=2+2(0.25)\left(\frac{10}{9}\right)=2+\frac{5}{9}=\frac{23}{9}=2.5555\ldots
\]

\[
\boxed{f(0.5)\approx 2.5556}
\]

## Solution 7

Euler first:

\[
y_1=1+0.1(2)=1.2.
\]

Second derivative at \(x_1=0.1,y_1=1.2\):

\[
\left(\frac{d^2y}{dx^2}\right)_1=0.1+1.2=1.3.
\]

Second-order step:

\[
y_2=2(1.2)-1+(0.1)^2(1.3)=2.4-1+0.013=1.413.
\]

\[
\boxed{y(0.1)\approx 1.2000},\qquad \boxed{y(0.2)\approx 1.4130}.
\]

## Solution 8

Second derivative at \(n=0\):

\[
\left(\frac{d^2y}{dx^2}\right)_0=2+5+4=11.
\]

Midpoint formula:

\[
4=\frac{y_1-y_{-1}}{2(0.5)}=y_1-y_{-1}.
\]

So

\[
y_1-y_{-1}=4.\tag{1}
\]

Second-order formula:

\[
11=\frac{y_1-2(5)+y_{-1}}{(0.5)^2}=\frac{y_1-10+y_{-1}}{0.25}.
\]

\[
2.75=y_1-10+y_{-1},
\]

so

\[
y_1+y_{-1}=12.75.\tag{2}
\]

Add (1) and (2):

\[
2y_1=16.75,
\]

\[
y_1=8.375.
\]

\[
\boxed{y(2.5)\approx 8.375}
\]

## Solution 9

Six months is \(\frac12\) year. Two iterations give \(h=\frac14\).

\[
\left(\frac{dV}{dt}\right)_0=0.4(15)+2(0)=6.
\]

\[
V_1=15+\frac14(6)=16.5.
\]

At \(t_1=\frac14\),

\[
\left(\frac{dV}{dt}\right)_1=0.4(16.5)+2\left(\frac14\right)=6.6+0.5=7.1.
\]

\[
V_2=16.5+\frac14(7.1)=16.5+1.775=18.275.
\]

\[
\boxed{V\approx 18.28\text{ thousand pounds, or about }£18{,}280.}
\]

## Solution 10

Four intervals on \([0,2]\) give \(h=\frac12\). Values:

| \(i\) | \(x_i\) | \(y_i=x_i^3+2x_i+1\) |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 0.5 | \(\frac{17}{8}\) |
| 2 | 1 | 4 |
| 3 | 1.5 | \(\frac{59}{8}\) |
| 4 | 2 | 13 |

Simpson’s rule:

\[
\frac{1/2}{3}\left[1+13+4\left(\frac{17}{8}+\frac{59}{8}\right)+2(4)\right].
\]

\[
=\frac16\left[14+4\left(\frac{76}{8}\right)+8\right]
=\frac16\left[14+38+8\right]
=\frac16(60)=10.
\]

\[
\boxed{10}
\]

## Solution 11

The values at \(0,1,2,3,4,5\) create five intervals. Simpson’s rule needs an even number of intervals, so it cannot be applied directly over the whole interval.

\[
\boxed{\text{No. There are 5 intervals, and Simpson’s rule needs an even number of intervals.}}
\]

## Solution 12

1. First-order differential equation: Euler’s method unless midpoint is requested.
2. Second-order with no \(\frac{dy}{dx}\) on the right: Type A, Euler first then second-order formula.
3. Second-order with \(\frac{dy}{dx}\) on the right: Type B, midpoint plus second-order plus simultaneous equations.
4. Integral from equal intervals with an even number of intervals: Simpson’s rule.

---

# 15. Exam Technique Notes

## Method Selection

| Task wording | Likely method |
|---|---|
| “Use two iterations of the approximation formula” with \(\frac{dy}{dx}\) | Euler’s method |
| “Use the midpoint formula” | Euler first, then midpoint |
| Second-order DE without \(\frac{dy}{dx}\) on the right | Euler first, then second-order formula |
| Second-order DE with \(\frac{dy}{dx}\) on the right | midpoint + second-order + simultaneous equations |
| Estimate an integral from a table | Simpson’s rule |

Always find \(h\) before calculating. Rewrite formulae in the question’s variables. Use radians when calculus and trigonometry appear together. Show substitution lines. Avoid premature rounding. Interpret final answers in context.

---

# 16. Syllabus Gap Check

## Official CCEA Further Maths LO Coverage

| Official CCEA Further LO ID | Covered? | Reason |
|---|---:|---|
| None | No | No official CCEA Further Maths LO for this numerical-methods pack was found in the inspected specification map. |

## Enrichment Objective Coverage

| Enrichment objective ID | Covered? | Evidence strength |
|---|---:|---|
| `ENR-NM-001` | Yes | Strong |
| `ENR-NM-002` | Yes | Strong |
| `ENR-NM-003` | Yes | Strong |
| `ENR-NM-004` | Yes | Strong |
| `ENR-NM-005` | Yes | Strong |
| `ENR-NM-006` | Yes | Strong |
| `ENR-NM-007` | Yes | Strong |
| `ENR-NM-008` | Yes | Strong |
| `ENR-NM-009` | Yes | Strong |
| `ENR-NM-010` | Yes | Strong |

## Off-Spec Content Found but Excluded From CCEA Core

| Content | Included in enrichment? | Included as CCEA core? | Boundary reason |
|---|---:|---:|---|
| Euler’s method | Yes | No | Not found in inspected CCEA Further Maths map. |
| Midpoint method | Yes | No | Not found in inspected CCEA Further Maths map. |
| Second-order numerical method | Yes | No | CCEA Further second-order DE topic inspected is analytical, not numerical. |
| Simpson’s rule | Yes | No | Not found in inspected CCEA Further Maths map. |
| Vector/tangent fields | Yes | No | Used as enrichment intuition only. |

## Weak Evidence Warnings

| Issue | Warning |
|---|---|
| Screenshot PDF is image-only | Visual details were preserved only where readable from images or parsed PDF/transcript. |
| Some transcript text is speech-to-text and imperfect | Ambiguous numerical examples were flagged rather than silently repaired. |
| Deer context example model ambiguity | The transcript’s reported derivative values do not match the equation as reconstructed, so that example was flagged in the chat build and not relied on as a final core worked solution. |
| CCEA Further topic code missing | No official CCEA Further topic code or LO ID is assigned. |

---

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements for the portal:

1. Euler error magnifier showing tangent prediction versus true curve.
2. Step-size comparison for \(h=0.5\), \(h=0.25\) and \(h=0.1\).
3. Method-choice decision tree.
4. Simpson grouping strip for \(y_0\) to \(y_8\).
5. Radian warning card: calculus + trig = radians.
6. Widgets for Euler tables, midpoint method, second-order selection, Simpson grouping and exam traps.

These are proposed teaching enhancements, not evidence-backed CCEA requirements.

---

# 18. Supplementary Sources Used

| Source | Use |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Boundary authority. No matching CCEA Further Numerical Methods topic found. |
| `Further_Maths_README_module_map.md` | Workflow and naming rules. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Off-spec logging and missing-evidence control. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge context only. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary A-Level bridge context only. |
| `FP1-Chp8-NumericalMethods.pdf` | Main mathematical enrichment source. |
| `Chapter_8_Numerical_Methods_🧩_(Further_Pure_1)_screenshots.pdf` | Visual evidence for diagrams and annotations. |
| `transcripts.md` | Teacher explanations, warnings, examples and method sequence. |

Final boundary statement: this lesson pack teaches numerical methods from the supplied FP1 evidence but does not claim CCEA Further Mathematics specification coverage.

---

# 19. Final Student Checklist

## Prerequisite Confidence

- [ ] I can calculate gradients using rise over run.
- [ ] I can interpret \(\frac{dy}{dx}\) as a gradient or rate of change.
- [ ] I can integrate simple expressions such as \(2x\).
- [ ] I understand that \(y=x^2+c\) represents a family of curves.
- [ ] I can substitute coordinates into formulae.
- [ ] I can convert months into years when needed.
- [ ] I can use radians for calculus with trigonometric functions.

## Euler’s Method

- [ ] I can identify \(x_0\), \(y_0\), and \(h\).
- [ ] I can calculate \(\left(\frac{dy}{dx}\right)_0\).
- [ ] I can use \(y_{n+1}\approx y_n+h\left(\frac{dy}{dx}\right)_n\).
- [ ] I can fill a table of \(n\), \(x_n\), \(y_n\), and derivative values.
- [ ] I can interpret a final context answer.

## Midpoint Method

- [ ] I can write \(\left(\frac{dy}{dx}\right)_n\approx \frac{y_{n+1}-y_{n-1}}{2h}\).
- [ ] I can use \(y_{n+1}\approx y_{n-1}+2h\left(\frac{dy}{dx}\right)_n\).
- [ ] I remember that Euler often comes first.

## Second-Order Method

- [ ] I can write \(\left(\frac{d^2y}{dx^2}\right)_n\approx \frac{y_{n+1}-2y_n+y_{n-1}}{h^2}\).
- [ ] I can identify Type A and Type B questions.
- [ ] I can solve Type B simultaneous equations.

## Simpson’s Rule

- [ ] I can check that the number of intervals is even.
- [ ] I can calculate \(h=\frac{b-a}{\text{number of intervals}}\).
- [ ] I can identify endpoints, odd values and internal even values.
- [ ] I can apply Simpson’s rule without confusing it with trapezium rule.

## Off-Spec Awareness

- [ ] I can state clearly that this is enrichment, not inspected CCEA Further Maths core.
