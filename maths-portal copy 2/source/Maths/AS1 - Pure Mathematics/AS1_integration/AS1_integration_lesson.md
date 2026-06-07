# AS1 Integration

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-INT |
| Topic name | Integration |
| Topic slug | integration |
| Topic Pascal | Integration |
| Topic ID | AS1Integration |
| Lesson file | AS1_integration_lesson.md |
| LO IDs | AS1-INT-LO001, AS1-INT-LO002, AS1-INT-LO003, AS1-INT-LO004 |
| Tags | `#AS1`, `#Integration`, `#Integrate`, `#AreaUnderCurve`, `#ExamTechnique` |

## Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit identity, topic code, LO IDs, syllabus boundaries | Core authority |
| README-Module-Map.txt | Required metadata pattern and file naming | Project control source |
| Source-Evidence-Drop-Checklist.txt | Evidence logging and off-spec logging pattern | Project control source |
| P1-Chp13-Integration.pdf | Main examples, notation, warnings, diagrams and worked examples | Lesson evidence |
| Chapter_13_Integration_🚀_(Pure_Year_1)_Transcript.md | Teacher explanation, method commentary and warnings | Lesson evidence |
| Chapter_13_Integration_🚀_(Pure_Year_1)_Screenshots.pdf | Visual reference for slides and board annotations | Partial visual evidence |

## Specification Alignment

| LO ID | Official requirement | Where covered |
|---|---|---|
| AS1-INT-LO001 | demonstrate understanding of and use indefinite integration as the reverse of differentiation | Sections 1 to 6 |
| AS1-INT-LO002 | integrate \(x^n\) excluding \(n=-1\), and related sums, differences and constant multiples | Sections 2 to 5 |
| AS1-INT-LO003 | evaluate definite integrals | Sections 7 to 8 |
| AS1-INT-LO004 | use a definite integral to find the area defined by a curve and either axis | Sections 9 to 12 |

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain integration as the reverse process of differentiation.
2. Integrate expressions of the form \(kx^n\), where \(n\ne -1\), including rational and negative powers.
3. Use \(+c\) correctly for indefinite integration.
4. Find the constant of integration using a point on a curve.
5. Use correct integral notation, including \(dx\), \(dt\), limits and square brackets.
6. Evaluate definite integrals using upper limit minus lower limit.
7. Use definite integrals to find areas between a curve and the \(x\)-axis.
8. Recognise when a definite integral gives signed area, and split intervals when true area is required.

## Prerequisite Recap

For rational \(n\),

\[
\frac{d}{dx}(x^n)=nx^{n-1}.
\]

For a constant multiple,

\[
\frac{d}{dx}(ax^n)=anx^{n-1}.
\]

Before integrating, rewrite roots and fractions as powers of \(x\):

\[
\sqrt{x}=x^{\frac12},\qquad \frac{1}{x^2}=x^{-2},\qquad \frac{1}{\sqrt{x}}=x^{-\frac12}.
\]

For areas bounded by a curve and the \(x\)-axis, the limits often come from roots found by solving \(y=0\).

## Big Picture Explanation

Differentiation asks for the gradient or rate of change. Integration begins with the reverse question: what function differentiated to give this? This is why integration is also called anti-differentiation.

Integration also finds exact areas under curves. In pure mathematics this appears as area between a curve and the \(x\)-axis; in applied work the same idea later links to areas under velocity-time graphs.

## Key Definitions and Notation

### Indefinite integration

An indefinite integral has no limits and produces a family of functions:

\[
\int f(x)\,dx=F(x)+c.
\]

The \(+c\) is needed because constants disappear when differentiated.

For example,

\[
\frac{d}{dx}(x^3)=3x^2,\qquad
\frac{d}{dx}(x^3+1)=3x^2,\qquad
\frac{d}{dx}(x^3-4)=3x^2.
\]

So, if

\[
\frac{dy}{dx}=3x^2,
\]

then

\[
y=x^3+c.
\]

### Constant of integration

The constant \(c\) is called the constant of integration. It represents the unknown constant that may have been present before differentiation.

### Integral notation

\[
\int 10x\,dx
\]

means integrate \(10x\) with respect to \(x\). The \(dx\) is part of the instruction.

### Definite integration

\[
\int_a^b f(x)\,dx=\left[F(x)\right]_a^b=F(b)-F(a).
\]

There is no \(+c\) in the final definite-integral working because constants cancel when we subtract \(F(a)\) from \(F(b)\).

---

## Core Theory

## 1. Integration as reverse differentiation

Differentiation of powers works by multiplying by the power and reducing the power by \(1\):

\[
\frac{d}{dx}(5x^3)=5\cdot3x^{3-1}=15x^2.
\]

Integration reverses this:

\[
\text{increase the power by }1,\text{ then divide by the new power.}
\]

The general AS1 power rule is:

\[
\int ax^n\,dx=\frac{a}{n+1}x^{n+1}+c,\qquad n\ne -1.
\]

The condition \(n\ne -1\) matters because if \(n=-1\), then \(n+1=0\), so the rule would divide by \(0\). Integrating \(1/x\) is not handled by the AS1 power rule.

[VISUAL PLACEHOLDER: AS1IntegrationMER-001 | Source: P1 Chapter 13 Integration PDF + teacher transcript | Insert from mermaid/AS1IntegrationMER-001.md | Purpose: Flowchart showing differentiation as “multiply by power, reduce power” and integration as “increase power, divide by new power”.]

## 2. Basic indefinite integration examples

### Example 1

Find \(y\) when \(\frac{dy}{dx}=4x^3\).

Increase the power from \(3\) to \(4\), then divide by \(4\):

\[
y=\frac{4}{4}x^4+c=x^4+c.
\]

\[
\boxed{y=x^4+c}
\]

### Example 2

Find \(y\) when \(\frac{dy}{dx}=x^5\).

\[
y=\frac16x^6+c.
\]

\[
\boxed{y=\frac16x^6+c}
\]

### Example 3

Find \(y\) when \(\frac{dy}{dx}=3x^{\frac12}\).

\[
\frac12+1=\frac32.
\]

\[
y=\frac{3x^{\frac32}}{\frac32}+c
=3\cdot\frac23x^{\frac32}+c
=2x^{\frac32}+c.
\]

\[
\boxed{y=2x^{\frac32}+c}
\]

Warning: avoid leaving answers in a messy “dividing by a fraction” form. Use the reciprocal.

## 3. Fractional and negative power examples

### Example 4

\[
\frac{dy}{dx}=\frac{4}{\sqrt{x}}=4x^{-\frac12}.
\]

\[
-\frac12+1=\frac12.
\]

\[
y=4\cdot2x^{\frac12}+c=8x^{\frac12}+c.
\]

\[
\boxed{y=8x^{\frac12}+c}
\]

### Example 5

\[
\frac{dy}{dx}=5x^{-2}.
\]

\[
-2+1=-1.
\]

\[
y=\frac{5}{-1}x^{-1}+c=-5x^{-1}+c.
\]

\[
\boxed{y=-5x^{-1}+c}
\]

### Example 6

\[
\frac{dy}{dx}=4x^{\frac23}.
\]

\[
\frac23+1=\frac53.
\]

\[
y=4\cdot\frac35x^{\frac53}+c=\frac{12}{5}x^{\frac53}+c.
\]

\[
\boxed{y=\frac{12}{5}x^{\frac53}+c}
\]

### Example 7

\[
\frac{dy}{dx}=10x^{-\frac27}.
\]

\[
-\frac27+1=\frac57.
\]

\[
y=10\cdot\frac75x^{\frac57}+c=14x^{\frac57}+c.
\]

\[
\boxed{y=14x^{\frac57}+c}
\]

## 4. Test-your-understanding integration set

### Question A

\[
f'(x)=\frac{2}{x^7}=2x^{-7}.
\]

\[
f(x)=\frac{2}{-6}x^{-6}+c=-\frac13x^{-6}+c.
\]

\[
\boxed{f(x)=-\frac13x^{-6}+c}
\]

### Question B

\[
f'(x)=\sqrt[3]{x}=x^{\frac13}.
\]

\[
f(x)=\frac{1}{\frac43}x^{\frac43}+c=\frac34x^{\frac43}+c.
\]

\[
\boxed{f(x)=\frac34x^{\frac43}+c}
\]

### Question C

\[
f'(x)=33x^{\frac56}.
\]

\[
\frac56+1=\frac{11}{6}.
\]

\[
f(x)=33\cdot\frac6{11}x^{\frac{11}{6}}+c=18x^{\frac{11}{6}}+c.
\]

\[
\boxed{f(x)=18x^{\frac{11}{6}}+c}
\]

### Question D

\[
f'(x)=2x+7.
\]

\[
\boxed{f(x)=x^2+7x+c}
\]

### Question E

\[
f'(x)=x^2-1.
\]

\[
\boxed{f(x)=\frac13x^3-x+c}
\]

## 5. Integral notation and variables

### Example 8

Find

\[
\int \left(x^{-\frac32}+2\right)\,dx.
\]

\[
-\frac32+1=-\frac12.
\]

\[
\int x^{-\frac32}\,dx=-2x^{-\frac12}.
\]

\[
\int2\,dx=2x.
\]

\[
\boxed{\int \left(x^{-\frac32}+2\right)\,dx=-2x^{-\frac12}+2x+c}
\]

Brackets are required when there are multiple terms.

### Example 9

Find

\[
\int(6t^2-1)\,dt.
\]

\[
\int6t^2\,dt=2t^3,\qquad \int-1\,dt=-t.
\]

\[
\boxed{\int(6t^2-1)\,dt=2t^3-t+c}
\]

### Example 10

Find

\[
\int(px^3+q)\,dx,
\]

where \(p\) and \(q\) are constants.

\[
\int px^3\,dx=\frac14px^4,\qquad \int q\,dx=qx.
\]

\[
\boxed{\int(px^3+q)\,dx=\frac14px^4+qx+c}
\]

Important warning: other letters can be treated as constants only when they are constants or variables independent of \(x\).

## 6. Finding the constant of integration

### Method

1. Integrate \(f'(x)\) to find \(f(x)=F(x)+c\).
2. Substitute the given point \((x,y)\).
3. Solve for \(c\).
4. Write the full equation of the curve.

### Example 11

The curve \(y=f(x)\) passes through \((1,3)\). Given \(f'(x)=3x^2\), find the equation of the curve.

\[
f(x)=x^3+c.
\]

Use \((1,3)\):

\[
3=1^3+c.
\]

\[
3=1+c.
\]

\[
c=2.
\]

\[
\boxed{f(x)=x^3+2}
\]

### Example 12

A curve \(y=f(x)\) passes through \((4,25)\). Given

\[
f'(x)=\frac38x^2-10x^{-\frac12}+1,\qquad x>0,
\]

find \(f(x)\), simplifying each term.

\[
\int \frac38x^2\,dx=\frac38\cdot\frac13x^3=\frac18x^3.
\]

\[
\int -10x^{-\frac12}\,dx=-10\cdot2x^{\frac12}=-20x^{\frac12}.
\]

\[
\int1\,dx=x.
\]

\[
f(x)=\frac18x^3-20x^{\frac12}+x+c.
\]

Use \((4,25)\):

\[
25=\frac18(4)^3-20(4)^{\frac12}+4+c.
\]

\[
25=8-40+4+c.
\]

\[
25=-28+c.
\]

\[
c=53.
\]

\[
\boxed{f(x)=\frac18x^3-20x^{\frac12}+x+53}
\]

## 7. Definite integration

\[
\int_a^bf(x)\,dx=\left[F(x)\right]_a^b=F(b)-F(a).
\]

Always write

\[
(\text{upper substitution})-(\text{lower substitution}).
\]

[VISUAL PLACEHOLDER: AS1IntegrationSVG-002 | Source: P1 Chapter 13 Integration PDF page 16 and transcript | Insert from svg/AS1IntegrationSVG-002.svg | Purpose: Show the definite-integral evaluation layout: integrate, bracket, upper substitution minus lower substitution.]

### Example 13

Evaluate

\[
\int_1^54x^3\,dx.
\]

\[
\int4x^3\,dx=x^4.
\]

\[
\int_1^54x^3\,dx=\left[x^4\right]_1^5=5^4-1^4=625-1.
\]

\[
\boxed{624}
\]

### Example 14

Evaluate

\[
\int_{-3}^{3}(x^2+1)\,dx.
\]

\[
\int(x^2+1)\,dx=\frac13x^3+x.
\]

\[
\int_{-3}^{3}(x^2+1)\,dx=\left[\frac13x^3+x\right]_{-3}^{3}.
\]

\[
=\left(\frac13(3)^3+3\right)-\left(\frac13(-3)^3+(-3)\right).
\]

\[
=(9+3)-(-9-3)=12-(-12)=24.
\]

\[
\boxed{24}
\]

### Why there is no \(+c\) in definite integration

\[
\left[x^4+c\right]_1^5=(5^4+c)-(1^4+c)=5^4+c-1^4-c.
\]

The constants cancel, so no \(+c\) is needed.

## 8. Definite integration with a parameter

Given that \(P\) is a constant and

\[
\int_1^5(2Px+7)\,dx=4P^2,
\]

show that there are two possible values for \(P\), and find these values.

\[
\int(2Px+7)\,dx=Px^2+7x.
\]

\[
\int_1^5(2Px+7)\,dx=\left[Px^2+7x\right]_1^5.
\]

\[
=(25P+35)-(P+7)=24P+28.
\]

\[
24P+28=4P^2.
\]

\[
4P^2-24P-28=0.
\]

\[
P^2-6P-7=0.
\]

\[
(P+1)(P-7)=0.
\]

\[
\boxed{P=-1\text{ or }P=7}
\]

## 9. Area under a positive curve

For a positive curve \(y=f(x)\),

\[
\int_a^b f(x)\,dx
\]

gives the area between \(y=f(x)\), the \(x\)-axis, \(x=a\) and \(x=b\).

[VISUAL PLACEHOLDER: AS1IntegrationSVG-001 | Source: P1 Chapter 13 Integration PDF page 20 | Insert from svg/AS1IntegrationSVG-001.svg | Purpose: Show a positive curve \(y=f(x)\), vertical lines \(x=a\), \(x=b\), the \(x\)-axis and the shaded area represented by \(\int_a^b f(x)\,dx\).]

### Example 16

Find the area of the finite region between

\[
y=20-x-x^2
\]

and the \(x\)-axis.

Find roots:

\[
20-x-x^2=0.
\]

\[
x^2+x-20=0.
\]

\[
(x+5)(x-4)=0.
\]

\[
x=-5\quad\text{or}\quad x=4.
\]

The area is:

\[
\int_{-5}^{4}(20-x-x^2)\,dx.
\]

\[
\int(20-x-x^2)\,dx=20x-\frac12x^2-\frac13x^3.
\]

\[
\left[20x-\frac12x^2-\frac13x^3\right]_{-5}^{4}.
\]

Substitute \(4\):

\[
80-8-\frac{64}{3}.
\]

Substitute \(-5\):

\[
-100-\frac{25}{2}+\frac{125}{3}.
\]

Subtract:

\[
\left(80-8-\frac{64}{3}\right)-\left(-100-\frac{25}{2}+\frac{125}{3}\right).
\]

\[
=\frac{152}{3}-\left(-\frac{425}{6}\right)
=\frac{304}{6}+\frac{425}{6}
=\frac{729}{6}
=\frac{243}{2}.
\]

\[
\boxed{\frac{243}{2}}
\]

[VISUAL PLACEHOLDER: AS1IntegrationSVG-003 | Source: P1 Chapter 13 Integration PDF page 20 | Insert from svg/AS1IntegrationSVG-003.svg | Purpose: Show the curve \(y=20-x-x^2\), roots \(x=-5\), \(x=4\), and the finite region above the \(x\)-axis.]

## 10. Why integration gives area

Let \(A(x)\) be the area under \(y=f(x)\) up to \(x\). If \(x\) increases by a very small amount \(h\), the extra thin strip has approximate area \(f(x)h\):

\[
A(x+h)-A(x)\approx f(x)h.
\]

\[
\frac{A(x+h)-A(x)}{h}\approx f(x).
\]

As \(h\to0\), this becomes

\[
A'(x)=f(x).
\]

Therefore \(A(x)\) is an integral of \(f(x)\), and

\[
\int_a^b f(x)\,dx=A(b)-A(a).
\]

[VISUAL PLACEHOLDER: AS1IntegrationSVG-006 | Source: P1 Chapter 13 Integration PDF pages 21-22 | Insert from svg/AS1IntegrationSVG-006.svg | Purpose: Show area function \(A(x)\), a thin strip of width \(h\), and the link \(A'(x)=f(x)\).]

## 11. Signed or negative areas

A definite integral gives signed area. If the graph is above the \(x\)-axis, the area contributes positively. If the graph is below the \(x\)-axis, the area contributes negatively.

Consider

\[
y=x(x-1)(x-2).
\]

\[
x(x-1)(x-2)=x^3-3x^2+2x.
\]

\[
\int_0^2x(x-1)(x-2)\,dx
=
\int_0^2(x^3-3x^2+2x)\,dx.
\]

\[
\int(x^3-3x^2+2x)\,dx=\frac14x^4-x^3+x^2.
\]

\[
\left[\frac14x^4-x^3+x^2\right]_0^2.
\]

\[
F(2)=4-8+4=0,\qquad F(0)=0.
\]

\[
\boxed{0}
\]

The result is \(0\) because the positive part from \(0\) to \(1\) cancels the negative part from \(1\) to \(2\).

[VISUAL PLACEHOLDER: AS1IntegrationSVG-004 | Source: P1 Chapter 13 Integration PDF pages 25-26 + transcript | Insert from svg/AS1IntegrationSVG-004.svg | Purpose: Show \(y=x(x-1)(x-2)\), positive area on \(0<x<1\), negative signed area on \(1<x<2\), and why the integral from 0 to 2 is 0.]

### Total area

Roots are \(x=0,1,2\). Split:

\[
\int_0^1(x^3-3x^2+2x)\,dx=\left[\frac14x^4-x^3+x^2\right]_0^1=\frac14.
\]

\[
\int_1^2(x^3-3x^2+2x)\,dx=\left[\frac14x^4-x^3+x^2\right]_1^2=0-\frac14=-\frac14.
\]

Total area:

\[
\frac14+\left|-\frac14\right|=\frac14+\frac14=\boxed{\frac12}.
\]

## 12. Area involving a line and a curve

CCEA AS1 allows definite integration with areas of trapeziums and triangles. The AS1-safe method is:

1. Use integration for the area under the curve.
2. Use triangle or trapezium formulae for the straight-line region.
3. Subtract the unwanted part.

### Example 17

Determine the area between

\[
y=x(4-x)
\]

and

\[
y=x.
\]

Find intersections:

\[
x(4-x)=x.
\]

\[
4x-x^2=x.
\]

\[
3x-x^2=0.
\]

\[
x(3-x)=0.
\]

\[
x=0\quad\text{or}\quad x=3.
\]

Area under the curve:

\[
\int_0^3(4x-x^2)\,dx.
\]

\[
\int(4x-x^2)\,dx=2x^2-\frac13x^3.
\]

\[
\left[2x^2-\frac13x^3\right]_0^3=18-9=9.
\]

Area under the line \(y=x\) from \(0\) to \(3\) is a triangle:

\[
\frac12\times3\times3=\frac92.
\]

Therefore

\[
9-\frac92=\frac{18}{2}-\frac92=\boxed{\frac92}.
\]

[VISUAL PLACEHOLDER: AS1IntegrationSVG-005 | Source: P1 Chapter 13 Integration PDF page 30 | Insert from svg/AS1IntegrationSVG-005.svg | Purpose: Show \(y=x(4-x)\), \(y=x\), intersections at \(x=0\) and \(x=3\), area under curve, triangle subtraction, and shaded result.]

## Visual Asset Integration

| Asset ID | Type | Lesson section | Purpose |
|---|---|---|---|
| AS1IntegrationMER-001 | Mermaid | Section 1 | Reverse differentiation flowchart |
| AS1IntegrationSVG-001 | SVG | Section 9 | Positive area under curve |
| AS1IntegrationSVG-002 | SVG | Section 7 | Definite integral evaluation layout |
| AS1IntegrationSVG-003 | SVG | Example 16 | \(y=20-x-x^2\) finite area |
| AS1IntegrationSVG-004 | SVG | Section 11 | Signed area and true total area |
| AS1IntegrationSVG-005 | SVG | Example 17 | Line-curve triangle subtraction |
| AS1IntegrationSVG-006 | SVG | Section 10 | Area function and thin strip explanation |
| AS1IntegrationWID-001 | Widget | Practice | Power-rule integration checker |
| AS1IntegrationWID-002 | Widget | Practice | Signed-area explorer |

[INTERACTIVE PLACEHOLDER: AS1IntegrationWID-001 | Source: CCEA AS1 Integration LO002 + lesson evidence | Insert from widgets/AS1IntegrationWID-001.html | Purpose: Let students enter \(ax^n\) and see the AS1 power-rule integration step, with \(n=-1\) blocked as off-spec.]

[INTERACTIVE PLACEHOLDER: AS1IntegrationWID-002 | Source: CCEA AS1 Integration LO004 + negative-area evidence | Insert from widgets/AS1IntegrationWID-002.html | Purpose: Let students compare signed integral and total area by splitting intervals at roots.]

## Guided Practice

1. Find \(y\) when \(\frac{dy}{dx}=6x^5-8x^3+2\).
2. Find \(\int \left(9x^{\frac12}-4x^{-3}\right)\,dx\).
3. A curve satisfies \(f'(x)=12x^2-4x+5\) and passes through \((1,10)\). Find \(f(x)\).
4. Evaluate \(\int_2^4(3x^2-5)\,dx\).
5. Given \(\int_0^3(kx+2)\,dx=30\), find \(k\).
6. Find the area between \(y=x^2-6x+8\) and the \(x\)-axis between its roots.
7. Calculate the total area bounded between \(y=x(x-2)\) and the \(x\)-axis from \(x=0\) to \(x=3\).
8. The curve \(y=x(5-x)\) and the line \(y=x\) meet at \(x=0\) and another point. Find the area between them using the AS1-safe triangle subtraction method.

## Full Worked Solutions to Guided Practice

### Solution 1

\[
y=x^6-2x^4+2x+c.
\]

### Solution 2

\[
\int \left(9x^{\frac12}-4x^{-3}\right)\,dx=6x^{\frac32}+2x^{-2}+c.
\]

### Solution 3

\[
f(x)=4x^3-2x^2+5x+c.
\]

Use \((1,10)\):

\[
10=4-2+5+c=7+c.
\]

\[
c=3.
\]

\[
\boxed{f(x)=4x^3-2x^2+5x+3}
\]

### Solution 4

\[
\int_2^4(3x^2-5)\,dx=\left[x^3-5x\right]_2^4.
\]

\[
=(64-20)-(8-10)=44-(-2)=\boxed{46}.
\]

### Solution 5

\[
\int(kx+2)\,dx=\frac{k}{2}x^2+2x.
\]

\[
\left[\frac{k}{2}x^2+2x\right]_0^3=\frac{9k}{2}+6.
\]

\[
\frac{9k}{2}+6=30.
\]

\[
\frac{9k}{2}=24.
\]

\[
9k=48.
\]

\[
\boxed{k=\frac{16}{3}}
\]

### Solution 6

\[
x^2-6x+8=0.
\]

\[
(x-2)(x-4)=0.
\]

\[
x=2,\quad x=4.
\]

Between \(2\) and \(4\), \(f(3)=-1\), so the curve is below the \(x\)-axis.

\[
\int_2^4(x^2-6x+8)\,dx
=
\left[\frac13x^3-3x^2+8x\right]_2^4.
\]

\[
F(4)=\frac{16}{3},\qquad F(2)=\frac{20}{3}.
\]

\[
\int_2^4(x^2-6x+8)\,dx=-\frac43.
\]

Area:

\[
\boxed{\frac43}
\]

### Solution 7

\[
y=x(x-2)=x^2-2x.
\]

Roots \(x=0,2\). Split:

\[
\left|\int_0^2(x^2-2x)\,dx\right|+\left|\int_2^3(x^2-2x)\,dx\right|.
\]

\[
\int(x^2-2x)\,dx=\frac13x^3-x^2.
\]

First interval:

\[
\left[\frac13x^3-x^2\right]_0^2=-\frac43.
\]

Second interval:

\[
\left[\frac13x^3-x^2\right]_2^3=0-\left(-\frac43\right)=\frac43.
\]

Total area:

\[
\boxed{\frac83}
\]

### Solution 8

\[
x(5-x)=x.
\]

\[
5x-x^2=x.
\]

\[
4x-x^2=0.
\]

\[
x(4-x)=0.
\]

\[
x=0,\quad x=4.
\]

Area under curve:

\[
\int_0^4(5x-x^2)\,dx=\left[\frac52x^2-\frac13x^3\right]_0^4.
\]

\[
=\frac52(16)-\frac{64}{3}
=40-\frac{64}{3}
=\frac{56}{3}.
\]

Area under line:

\[
\frac12\times4\times4=8.
\]

Subtract:

\[
\frac{56}{3}-8=\frac{56}{3}-\frac{24}{3}=\boxed{\frac{32}{3}}.
\]

## Common Mistakes and Exam Traps

- Forgetting \(+c\) for indefinite integration.
- Adding \(+c\) in a definite integral.
- Dividing by the old power instead of the new power.
- Mishandling fractional powers.
- Using the AS1 power rule on \(\int x^{-1}\,dx\).
- Dropping brackets in upper-minus-lower substitution.
- Treating signed integral as total area without checking whether the curve crosses the \(x\)-axis.

## Exam Technique

1. Rewrite roots and fractions as powers first.
2. Show the integrated expression.
3. Use square brackets for definite integrals.
4. Always write upper substitution minus lower substitution.
5. Use calculator integration only to check, not as displayed working.
6. For areas, sketch enough to know whether the curve is above or below the axis.
7. Split signed areas at roots.

## Common CCEA-Style Wording

| Wording | Meaning |
|---|---|
| “Find \(y\), given \(\frac{dy}{dx}\)” | Integrate and include \(+c\); use any point given to find \(c\). |
| “Find \(f(x)\), given \(f'(x)\)” | Same as above, but in function notation. |
| “Evaluate \(\int_a^b f(x)\,dx\)” | Definite integral, no \(+c\), show upper minus lower. |
| “Find the area bounded by the curve and the \(x\)-axis” | Find roots or limits, integrate, check sign. |
| “Total area” | Split at roots if the graph crosses the \(x\)-axis; add magnitudes. |
| “\(P\) is a constant” | Treat \(P\) as a number while integrating with respect to \(x\). |

## Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---|---|
| AS1-INT-LO001 | Yes | Reverse differentiation, \(+c\), finding original functions. |
| AS1-INT-LO002 | Yes | Powers \(x^n\), rational powers, negative powers, constant multiples, sums and differences. |
| AS1-INT-LO003 | Yes | Definite integral notation, limits, evaluation and parameter examples. |
| AS1-INT-LO004 | Yes | Area under curve, finite region, signed areas, true area by splitting. |

### Excluded from core

- \(\int1/x\,dx\): excluded from AS1.
- Surface areas and volumes: excluded from AS1 core.
- MAT/STEP extension questions: excluded from core.
- Direct area between two curves: treated as A21 boundary risk, not core AS1.
- Substitution, integration by parts and partial fractions: excluded.

## Supplementary Sources Used

No external web sources were used. Cross-board lesson evidence was used only where it aligns with CCEA AS1 Integration. Edexcel/MAT/STEP references in the evidence were not treated as CCEA core requirements.

## Final Student Checklist

- [ ] I can explain integration as reverse differentiation.
- [ ] I can use \(\int ax^n\,dx=\frac{a}{n+1}x^{n+1}+c\), with \(n\ne -1\).
- [ ] I know why \(+c\) is needed for indefinite integration.
- [ ] I know why \(+c\) is not used in definite integration.
- [ ] I can rewrite roots and fractions using powers of \(x\).
- [ ] I can integrate sums, differences and constant multiples.
- [ ] I can find \(c\) using a point on the curve.
- [ ] I can evaluate definite integrals using square brackets.
- [ ] I can calculate upper substitution minus lower substitution.
- [ ] I can find areas between a curve and the \(x\)-axis.
- [ ] I can split an area problem when the curve crosses the \(x\)-axis.
- [ ] I know that \(\int1/x\,dx\) is not part of the AS1 power-rule method.
