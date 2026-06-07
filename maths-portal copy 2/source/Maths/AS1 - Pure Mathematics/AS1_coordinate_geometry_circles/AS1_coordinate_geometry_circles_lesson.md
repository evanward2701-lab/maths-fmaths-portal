# AS1 Coordinate Geometry: Circles

## Lesson Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-CG |
| Topic name | Co-ordinate geometry in the \(x,y\) plane |
| Lesson focus | Circles |
| Topic slug | coordinate_geometry_circles |
| Topic Pascal | CoordinateGeometryCircles |
| Topic ID | AS1CoordinateGeometryCircles |
| Lesson file | AS1_coordinate_geometry_circles_lesson.md |
| Core LO IDs | AS1-CG-LO001, AS1-CG-LO002, AS1-CG-LO003, AS1-CG-LO005, AS1-CG-LO006, AS1-CG-LO007, AS1-CG-LO008 |
| Supporting LO IDs | AS1-AF-LO004, AS1-AF-LO005, AS1-AF-LO006, AS1-AF-LO007 |
| Status | Complete packaged lesson pack. |

---

## Evidence Map

| Evidence | Use |
|---|---|
| CCEA GCE Mathematics Specification Map | Defines AS1-CG learning outcomes and syllabus boundary. |
| README-Module-Map | Confirms lesson-pack structure, metadata and placeholder rules. |
| Source-Evidence-Drop-Checklist | Used for evidence and off-spec logs. |
| Dr Frost/Pearson-style Chapter 6 Circles PDF | Main lesson sequence, examples and slide-visible algebra. |
| Chapter 6 Circles transcript | Teacher explanations, warnings, method commentary and exam technique. |
| Screenshots PDF | Visual planning only. No extra mathematical details are claimed from unparsed images. |

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| AS1-CG-LO001 | Straight line forms \(y-y_1=m(x-x_1)\) and \(ax+by+c=0\) are used for perpendicular bisectors and tangents. |
| AS1-CG-LO002 | Midpoints and distances are used to find centres and radii. |
| AS1-CG-LO003 | Negative reciprocal gradients are used for perpendicular lines. |
| AS1-CG-LO005 | Circle equations are written and interpreted in centre-radius form and general expanded form. |
| AS1-CG-LO006 | Completing the square is used to find centre and radius. |
| AS1-CG-LO007 | Tangent-radius perpendicularity, chord bisector and angle in a semicircle are used. |
| AS1-CG-LO008 | Tangent equations are found through points on the circumference. |
| AS1-AF-LO004 | The discriminant decides whether a line has \(0\), \(1\) or \(2\) intersections with a circle. |
| AS1-AF-LO005 | Completing the square is used as an algebraic tool for circle equations. |
| AS1-AF-LO006 | Quadratics are solved after substitution. |
| AS1-AF-LO007 | Linear and circle equations are solved simultaneously. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Find the midpoint and length of a line segment.
2. Find the equation of a perpendicular bisector.
3. Write the equation of a circle from its centre and radius.
4. Find the equation of a circle when a diameter is given.
5. Convert a circle equation into centre-radius form by completing the square.
6. Use substitution to find intersections of a line and a circle.
7. Use the discriminant to decide whether a line is a secant, tangent or non-intersecting line.
8. Use the fact that a tangent is perpendicular to the radius at the point of contact.
9. Use the fact that the perpendicular bisector of a chord passes through the centre.
10. Use angle-in-a-semicircle reasoning and perpendicular bisectors to work with circumcircles.

---

## Prerequisite Recap

No external GCSE source is used here. These are prerequisite mathematical skills needed for the A-Level lesson.

### 1. Midpoint

For points

\[
A(x_1,y_1), \qquad B(x_2,y_2),
\]

the midpoint is

\[
M\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right).
\]

The idea is simple: take the mean of the \(x\)-coordinates and the mean of the \(y\)-coordinates.

### 2. Gradient

For two points

\[
A(x_1,y_1), \qquad B(x_2,y_2),
\]

the gradient of \(AB\) is

\[
m_{AB}=\frac{y_2-y_1}{x_2-x_1}.
\]

### 3. Perpendicular gradients

If two non-vertical lines are perpendicular, their gradients multiply to \(-1\):

\[
m_1m_2=-1.
\]

Equivalently, one gradient is the negative reciprocal of the other.

For example, if

\[
m_1=\frac{1}{2},
\]

then

\[
m_2=-2.
\]

### 4. Point-gradient form of a line

A line with gradient \(m\) through \((x_1,y_1)\) has equation

\[
y-y_1=m(x-x_1).
\]

This form is especially useful in this chapter. It is usually cleaner than trying to force everything into \(y=mx+c\) immediately.

---

## Big Picture Explanation

Circles in coordinate geometry are where algebra and geometry shake hands.

At first, a circle equation looks like a formula:

\[
(x-a)^2+(y-b)^2=r^2.
\]

But it is really a distance statement. It says:

> Every point \((x,y)\) on the circle is exactly \(r\) units from the centre \((a,b)\).

The chapter then builds a toolkit:

- **Midpoints** help locate centres when a diameter is known.
- **Perpendicular gradients** help build perpendicular bisectors and tangents.
- **Completing the square** uncovers the hidden centre and radius.
- **Substitution and discriminants** decide whether a line cuts, touches or misses a circle.
- **Circle properties** turn geometry facts into algebraic equations.

---

## Key Definitions and Notation

### Circle

A circle is the set of all points that are a fixed distance from a fixed centre.

### Centre

The fixed point from which every point on the circle is the same distance.

If the centre is

\[
(a,b),
\]

then the standard circle equation uses \(x-a\) and \(y-b\).

### Radius

The fixed distance from the centre to any point on the circumference.

### Diameter

A line segment passing through the centre with endpoints on the circle.

The centre is the midpoint of any diameter.

### Chord

A chord is a line segment joining two points on the circle.

A diameter is a special chord that passes through the centre.

### Tangent

A tangent is a line that touches a circle at exactly one point.

At the point of contact, the tangent is perpendicular to the radius.

### Secant

A secant is a line that cuts a circle at two distinct points.

### Perpendicular bisector

The perpendicular bisector of a line segment:

1. passes through the midpoint of the segment;
2. is perpendicular to the segment.

For a chord of a circle, the perpendicular bisector passes through the centre.

### Circumcircle

A circle that passes through all three vertices of a triangle.

### Circumcentre

The centre of the circumcircle.

---

## Core Theory

### 1. Perpendicular bisectors

Suppose

\[
A(2,5), \qquad B(6,7).
\]

First find the midpoint:

\[
M\left(\frac{2+6}{2},\frac{5+7}{2}\right)
=
M\left(\frac{8}{2},\frac{12}{2}\right)
=
M(4,6).
\]

Now find the gradient of \(AB\):

\[
m_{AB}
=
\frac{7-5}{6-2}
=
\frac{2}{4}
=
\frac{1}{2}.
\]

The perpendicular gradient is the negative reciprocal:

\[
m_{\perp}=-2.
\]

Use point-gradient form through \(M(4,6)\):

\[
y-6=-2(x-4).
\]

Expand if needed:

\[
y-6=-2x+8,
\]

\[
y=-2x+14.
\]

So the perpendicular bisector is

\[
\boxed{y-6=-2(x-4)}
\]

or

\[
\boxed{y=-2x+14}.
\]

### 2. Equation of a circle centred at the origin

For a circle centred at \((0,0)\) with radius \(r\), take a point \((x,y)\) on the circle.

The horizontal distance is \(x\).

The vertical distance is \(y\).

By Pythagoras,

\[
x^2+y^2=r^2.
\]

So the equation is

\[
\boxed{x^2+y^2=r^2}.
\]

### 3. Equation of a circle centred at \((a,b)\)

Now shift the centre to \((a,b)\).

For a point \((x,y)\) on the circle:

- horizontal distance from centre to point is \(x-a\);
- vertical distance from centre to point is \(y-b\);
- radius is \(r\).

By Pythagoras,

\[
(x-a)^2+(y-b)^2=r^2.
\]

So the equation of a circle with centre \((a,b)\) and radius \(r\) is

\[
\boxed{(x-a)^2+(y-b)^2=r^2}.
\]

### 4. Reading the centre and radius

From

\[
(x-a)^2+(y-b)^2=r^2,
\]

the centre is

\[
(a,b),
\]

and the radius is

\[
r.
\]

Be careful with signs.

For example,

\[
(x+3)^2+(y-5)^2=1
\]

means

\[
(x-(-3))^2+(y-5)^2=1,
\]

so the centre is

\[
(-3,5),
\]

and the radius is

\[
1.
\]

### 5. Completing the square for circle equations

A circle may be given in expanded form, such as

\[
x^2+y^2-6x+2y-6=0.
\]

Group the \(x\)-terms and \(y\)-terms:

\[
x^2-6x+y^2+2y-6=0.
\]

Complete the square for the \(x\)-terms:

\[
x^2-6x=(x-3)^2-9.
\]

Complete the square for the \(y\)-terms:

\[
y^2+2y=(y+1)^2-1.
\]

Substitute:

\[
(x-3)^2-9+(y+1)^2-1-6=0.
\]

Collect constants:

\[
(x-3)^2+(y+1)^2-16=0.
\]

Move the constant:

\[
(x-3)^2+(y+1)^2=16.
\]

Therefore,

\[
\text{centre}=(3,-1),
\]

and

\[
r=\sqrt{16}=4.
\]

### 6. Line-circle intersections

To find intersections between a line and a circle:

1. Substitute the line equation into the circle equation.
2. Simplify to a quadratic.
3. Solve the quadratic.
4. Substitute each \(x\)-value back into the line to find the matching \(y\)-value.

The discriminant tells you the number of intersections:

| Discriminant | Meaning | Geometry |
|---|---|---|
| \(b^2-4ac>0\) | Two real roots | Secant, two intersections |
| \(b^2-4ac=0\) | One repeated root | Tangent, one point of contact |
| \(b^2-4ac<0\) | No real roots | Line misses circle |

### 7. Tangent-radius theorem

If a tangent touches a circle at \(P\), then the radius to \(P\) is perpendicular to the tangent.

So if you know:

- the centre of the circle;
- the point of contact;

then you can:

1. find the gradient of the radius;
2. take the negative reciprocal to get the tangent gradient;
3. use point-gradient form through the point of contact.

### 8. Perpendicular bisector of a chord

The perpendicular bisector of any chord passes through the centre of the circle.

This is powerful because if you know two chords, you can:

1. find the perpendicular bisector of chord 1;
2. find the perpendicular bisector of chord 2;
3. solve the two bisector equations simultaneously;
4. the intersection is the centre.

### 9. Angle in a semicircle

If \(AC\) is the diameter of the circumcircle of triangle \(ABC\), then

\[
\angle ABC=90^\circ.
\]

Therefore,

\[
AB^2+BC^2=AC^2.
\]

This can be used in reverse:

If

\[
AB^2+BC^2=AC^2,
\]

then \(\angle ABC=90^\circ\), so \(AC\) is the diameter of the circumcircle.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-001 | Source: Chapter 6 Circles PDF page 3 and screenshots PDF pages 6-20 | Insert from svg/AS1CoordinateGeometryCirclesSVG-001.svg | Purpose: Show a chord, its midpoint, and its perpendicular bisector passing through the circle centre.]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-002 | Source: Chapter 6 Circles PDF page 6 | Insert from svg/AS1CoordinateGeometryCirclesSVG-002.svg | Purpose: Derive \(x^2+y^2=r^2\) using a right-angled triangle inside a circle centred at the origin.]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-003 | Source: Chapter 6 Circles PDF page 7 | Insert from svg/AS1CoordinateGeometryCirclesSVG-003.svg | Purpose: Show why a shifted centre \((a,b)\) gives side lengths \(x-a\) and \(y-b\).]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-004 | Source: Chapter 6 Circles PDF pages 14-15 | Insert from svg/AS1CoordinateGeometryCirclesSVG-004.svg | Purpose: Compare secant, tangent and non-intersecting line cases using the discriminant.]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-005 | Source: Chapter 6 Circles PDF pages 17-18 | Insert from svg/AS1CoordinateGeometryCirclesSVG-005.svg | Purpose: Show tangent perpendicular to radius at the point of contact.]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-006 | Source: Chapter 6 Circles PDF pages 19-20 | Insert from svg/AS1CoordinateGeometryCirclesSVG-006.svg | Purpose: Show how a chord’s perpendicular bisector locates the centre.]

[VISUAL PLACEHOLDER: AS1CoordinateGeometryCirclesSVG-007 | Source: Chapter 6 Circles PDF pages 24-26 | Insert from svg/AS1CoordinateGeometryCirclesSVG-007.svg | Purpose: Show a triangle inscribed in a circle and the angle-in-a-semicircle property.]

[INTERACTIVE PLACEHOLDER: AS1CoordinateGeometryCirclesWidget-001 | Source: CCEA AS1-CG-LO005 plus Chapter 6 circle equation evidence | Insert from widgets/AS1CoordinateGeometryCirclesWidget-001.html | Purpose: Let students move the centre and radius and see the equation update.]

[INTERACTIVE PLACEHOLDER: AS1CoordinateGeometryCirclesWidget-002 | Source: CCEA AS1-AF-LO004 and Chapter 6 line-circle intersection evidence | Insert from widgets/AS1CoordinateGeometryCirclesWidget-002.html | Purpose: Let students alter a line and watch the discriminant change between secant, tangent and no intersection.]

[INTERACTIVE PLACEHOLDER: AS1CoordinateGeometryCirclesWidget-003 | Source: CCEA AS1-CG tangent outcomes and Chapter 6 tangent evidence | Insert from widgets/AS1CoordinateGeometryCirclesWidget-003.html | Purpose: Let students choose a centre and point of contact, then see radius gradient, tangent gradient and tangent equation.]

---

## Worked Examples

### Worked Example 1: Perpendicular bisector of a line segment

Find the perpendicular bisector of \(AB\), where

\[
A(4,7), \qquad B(10,17).
\]

First find the midpoint:

\[
M\left(\frac{4+10}{2},\frac{7+17}{2}\right)
=
M\left(\frac{14}{2},\frac{24}{2}\right)
=
M(7,12).
\]

Find the gradient of \(AB\):

\[
m_{AB}
=
\frac{17-7}{10-4}
=
\frac{10}{6}
=
\frac{5}{3}.
\]

The perpendicular gradient is

\[
m_{\perp}=-\frac{3}{5}.
\]

Use point-gradient form through \(M(7,12)\):

\[
y-12=-\frac{3}{5}(x-7).
\]

So the perpendicular bisector is

\[
\boxed{y-12=-\frac{3}{5}(x-7)}.
\]

If expanded:

\[
y-12=-\frac{3}{5}x+\frac{21}{5},
\]

\[
y=-\frac{3}{5}x+\frac{21}{5}+12,
\]

\[
y=-\frac{3}{5}x+\frac{21}{5}+\frac{60}{5},
\]

\[
\boxed{y=-\frac{3}{5}x+\frac{81}{5}}.
\]

---

### Worked Example 2: Finding the other end of a diameter

A line segment \(AB\) is the diameter of a circle with centre

\[
M(5,-4).
\]

If

\[
A(1,-2),
\]

find \(B\).

From \(A\) to \(M\):

\[
x: 1 \to 5
\]

is an increase of \(4\).

Continue the same movement:

\[
5+4=9.
\]

For the \(y\)-coordinate:

\[
-2 \to -4
\]

is a decrease of \(2\).

Continue the same movement:

\[
-4-2=-6.
\]

So

\[
\boxed{B(9,-6)}.
\]

Using midpoint algebra:

\[
\frac{1+x_B}{2}=5,
\]

\[
1+x_B=10,
\]

\[
x_B=9.
\]

And

\[
\frac{-2+y_B}{2}=-4,
\]

\[
-2+y_B=-8,
\]

\[
y_B=-6.
\]

Therefore,

\[
\boxed{B(9,-6)}.
\]

---

### Worked Example 3: Equation of a circle from a diameter

A line segment \(AB\) is the diameter of a circle, where

\[
A(5,8), \qquad B(-7,4).
\]

Find the equation of the circle.

The centre is the midpoint of \(AB\):

\[
C\left(\frac{5+(-7)}{2},\frac{8+4}{2}\right)
=
C\left(\frac{-2}{2},\frac{12}{2}\right)
=
C(-1,6).
\]

Use \(B(-7,4)\) and \(C(-1,6)\) to find the radius:

\[
r=\sqrt{(-7-(-1))^2+(4-6)^2}.
\]

\[
r=\sqrt{(-6)^2+(-2)^2}.
\]

\[
r=\sqrt{36+4}.
\]

\[
r=\sqrt{40}.
\]

The circle equation is

\[
(x-a)^2+(y-b)^2=r^2.
\]

Here

\[
a=-1, \qquad b=6, \qquad r^2=40.
\]

So

\[
(x-(-1))^2+(y-6)^2=40.
\]

Therefore,

\[
\boxed{(x+1)^2+(y-6)^2=40}.
\]

---

### Worked Example 4: Completing the square to find centre and radius

Find the centre and radius of

\[
x^2+y^2-6x+2y-6=0.
\]

Group \(x\)-terms and \(y\)-terms:

\[
x^2-6x+y^2+2y-6=0.
\]

Complete the square:

\[
x^2-6x=(x-3)^2-9,
\]

\[
y^2+2y=(y+1)^2-1.
\]

Substitute:

\[
(x-3)^2-9+(y+1)^2-1-6=0.
\]

Collect constants:

\[
-9-1-6=-16.
\]

So

\[
(x-3)^2+(y+1)^2-16=0.
\]

Move \(16\) to the other side:

\[
(x-3)^2+(y+1)^2=16.
\]

Hence

\[
\boxed{\text{centre }(3,-1)}
\]

and

\[
\boxed{r=4}.
\]

---

### Worked Example 5: Completing the square with larger coefficients

The circle \(C\) has equation

\[
x^2-20x+y^2-16y+139=0.
\]

Find the centre and show that \(r=5\).

Complete the square for the \(x\)-terms:

\[
x^2-20x=(x-10)^2-100.
\]

Complete the square for the \(y\)-terms:

\[
y^2-16y=(y-8)^2-64.
\]

Substitute:

\[
(x-10)^2-100+(y-8)^2-64+139=0.
\]

Collect constants:

\[
-100-64+139=-25.
\]

So

\[
(x-10)^2+(y-8)^2-25=0.
\]

Therefore,

\[
(x-10)^2+(y-8)^2=25.
\]

The centre is

\[
\boxed{(10,8)}.
\]

The radius is

\[
r=\sqrt{25}=5.
\]

Therefore,

\[
\boxed{r=5}.
\]

---

### Worked Example 6: Restriction on a constant in a circle equation

A circle has equation

\[
x^2-4x+y^2+10y=k.
\]

Find its centre and state the range of possible values of \(k\).

Complete the square:

\[
x^2-4x=(x-2)^2-4,
\]

\[
y^2+10y=(y+5)^2-25.
\]

So

\[
(x-2)^2-4+(y+5)^2-25=k.
\]

\[
(x-2)^2+(y+5)^2-29=k.
\]

\[
(x-2)^2+(y+5)^2=k+29.
\]

The centre is

\[
\boxed{(2,-5)}.
\]

For this to be a genuine circle, the right-hand side must be positive:

\[
k+29>0.
\]

So

\[
\boxed{k>-29}.
\]

---

### Worked Example 7: Showing a line does not meet a circle

Show that the line

\[
y=x+3
\]

does not meet the circle

\[
x^2+y^2=1.
\]

Substitute

\[
y=x+3
\]

into the circle:

\[
x^2+(x+3)^2=1.
\]

Expand:

\[
x^2+x^2+6x+9=1.
\]

\[
2x^2+6x+8=0.
\]

Divide by \(2\):

\[
x^2+3x+4=0.
\]

Use the discriminant:

\[
a=1,\qquad b=3,\qquad c=4.
\]

\[
b^2-4ac=3^2-4(1)(4).
\]

\[
b^2-4ac=9-16.
\]

\[
b^2-4ac=-7.
\]

Since

\[
-7<0,
\]

there are no real solutions. Therefore, the line does not meet the circle.

\[
\boxed{\text{No intersection.}}
\]

---

### Worked Example 8: Finding points of intersection

Find the points of intersection where the line

\[
y=x+6
\]

meets

\[
x^2+(y-3)^2=29.
\]

Substitute

\[
y=x+6.
\]

Then

\[
y-3=x+6-3=x+3.
\]

So

\[
x^2+(x+3)^2=29.
\]

Expand:

\[
x^2+x^2+6x+9=29.
\]

\[
2x^2+6x+9=29.
\]

\[
2x^2+6x-20=0.
\]

Divide by \(2\):

\[
x^2+3x-10=0.
\]

Factorise:

\[
(x+5)(x-2)=0.
\]

So

\[
x=-5 \quad \text{or} \quad x=2.
\]

Use

\[
y=x+6.
\]

If

\[
x=-5,
\]

then

\[
y=-5+6=1.
\]

So one point is

\[
(-5,1).
\]

If

\[
x=2,
\]

then

\[
y=2+6=8.
\]

So the other point is

\[
(2,8).
\]

Therefore,

\[
\boxed{(-5,1),\ (2,8)}.
\]

---

### Worked Example 9: Finding \(k\) so a line is tangent to a circle

Find \(k\) such that

\[
y=x+k
\]

touches the circle

\[
x^2+y^2=1.
\]

If a line touches a circle, there is exactly one point of intersection.

That means the resulting quadratic has discriminant \(0\).

Substitute

\[
y=x+k
\]

into the circle:

\[
x^2+(x+k)^2=1.
\]

Expand:

\[
x^2+x^2+2kx+k^2=1.
\]

\[
2x^2+2kx+k^2-1=0.
\]

This is a quadratic in \(x\), with

\[
a=2,\qquad b=2k,\qquad c=k^2-1.
\]

For tangency,

\[
b^2-4ac=0.
\]

So

\[
(2k)^2-4(2)(k^2-1)=0.
\]

\[
4k^2-8(k^2-1)=0.
\]

\[
4k^2-8k^2+8=0.
\]

\[
-4k^2+8=0.
\]

\[
8=4k^2.
\]

\[
k^2=2.
\]

\[
k=\pm \sqrt{2}.
\]

Therefore,

\[
\boxed{k=\pm\sqrt{2}}.
\]

---

### Worked Example 10: Tangent at a given point

The circle \(C\) has equation

\[
(x-3)^2+(y-7)^2=100.
\]

1. Verify that \(P(11,1)\) lies on \(C\).
2. Find an equation of the tangent to \(C\) at \(P\), giving your answer in the form

\[
ax+by+c=0.
\]

#### Part 1: Verify the point

Substitute \(x=11\), \(y=1\):

\[
(11-3)^2+(1-7)^2.
\]

\[
=8^2+(-6)^2.
\]

\[
=64+36.
\]

\[
=100.
\]

This equals the right-hand side of the circle equation, so

\[
\boxed{P(11,1)\text{ lies on }C.}
\]

#### Part 2: Find the tangent

The centre is

\[
(3,7).
\]

Find the gradient of the radius from \((3,7)\) to \(P(11,1)\):

\[
m_r=\frac{1-7}{11-3}.
\]

\[
m_r=\frac{-6}{8}.
\]

\[
m_r=-\frac{3}{4}.
\]

The tangent is perpendicular to the radius, so

\[
m_t=\frac{4}{3}.
\]

Use point-gradient form through \(P(11,1)\):

\[
y-1=\frac{4}{3}(x-11).
\]

Multiply by \(3\):

\[
3y-3=4(x-11).
\]

Expand:

\[
3y-3=4x-44.
\]

Rearrange into \(ax+by+c=0\):

\[
0=4x-44-3y+3.
\]

\[
0=4x-3y-41.
\]

So

\[
\boxed{4x-3y-41=0}.
\]

---

### Worked Example 11: Tangents with a given gradient

A circle \(C\) has equation

\[
(x-4)^2+(y+4)^2=10.
\]

The line \(l\) is a tangent to the circle and has gradient \(-3\). Find the two possible equations for \(l\), giving answers in the form

\[
y=mx+c.
\]

The centre is

\[
(4,-4).
\]

A tangent with gradient \(-3\) is perpendicular to the radius at the point of contact.

So the radius has gradient

\[
m_r=\frac{1}{3}.
\]

The radius through the centre has equation

\[
y+4=\frac{1}{3}(x-4).
\]

So

\[
y=\frac{1}{3}(x-4)-4.
\]

\[
y=\frac{1}{3}x-\frac{4}{3}-4.
\]

\[
y=\frac{1}{3}x-\frac{4}{3}-\frac{12}{3}.
\]

\[
y=\frac{1}{3}x-\frac{16}{3}.
\]

Now intersect this radius line with the circle:

\[
(x-4)^2+(y+4)^2=10.
\]

From the radius line,

\[
y+4=\frac{1}{3}(x-4).
\]

So

\[
(x-4)^2+\left(\frac{1}{3}(x-4)\right)^2=10.
\]

Let

\[
u=x-4.
\]

Then

\[
u^2+\left(\frac{u}{3}\right)^2=10.
\]

\[
u^2+\frac{u^2}{9}=10.
\]

\[
\frac{9u^2}{9}+\frac{u^2}{9}=10.
\]

\[
\frac{10u^2}{9}=10.
\]

Multiply by \(9\):

\[
10u^2=90.
\]

Divide by \(10\):

\[
u^2=9.
\]

So

\[
u=\pm 3.
\]

Since

\[
u=x-4,
\]

we have

\[
x-4=3 \quad \text{or} \quad x-4=-3.
\]

So

\[
x=7 \quad \text{or} \quad x=1.
\]

Find the matching \(y\)-values using

\[
y=\frac{1}{3}x-\frac{16}{3}.
\]

If

\[
x=7,
\]

then

\[
y=\frac{7}{3}-\frac{16}{3}=-\frac{9}{3}=-3.
\]

So one point of contact is

\[
(7,-3).
\]

If

\[
x=1,
\]

then

\[
y=\frac{1}{3}-\frac{16}{3}=-\frac{15}{3}=-5.
\]

So the other point of contact is

\[
(1,-5).
\]

Now form the tangent equations with gradient \(-3\).

Through \((7,-3)\):

\[
y+3=-3(x-7).
\]

\[
y+3=-3x+21.
\]

\[
y=-3x+18.
\]

Through \((1,-5)\):

\[
y+5=-3(x-1).
\]

\[
y+5=-3x+3.
\]

\[
y=-3x-2.
\]

Therefore,

\[
\boxed{y=-3x+18}
\]

and

\[
\boxed{y=-3x-2}.
\]

---

## Guided Practice

### Question 1

Find the perpendicular bisector of the line segment joining

\[
A(2,5), \qquad B(6,7).
\]

### Question 2

A circle has centre

\[
C(3,5)
\]

and passes through

\[
P(6,9).
\]

Find the equation of the tangent at \(P\), giving your answer in the form

\[
ax+by+c=0.
\]

### Question 3

A circle passes through

\[
A(0,0), \qquad B(4,2).
\]

The centre of the circle has \(x\)-coordinate \(-1\). Determine the equation of the circle.

### Question 4

The points

\[
A(-8,1), \qquad B(4,5), \qquad C(-4,9)
\]

lie on a circle.

1. Show that \(AB\) is a diameter of the circle.
2. Hence find the equation of the circle.

### Question 5

The points

\[
A(0,2), \qquad B(2,0), \qquad C(8,18)
\]

lie on the circumference of a circle. Determine the equation of the circle.

---

## Common Mistakes and Exam Traps

### Mistake 1: Reading the signs wrongly

From

\[
(x+5)^2+(y-2)^2=49,
\]

the centre is

\[
(-5,2),
\]

not

\[
(5,-2).
\]

The bracket hides a subtraction:

\[
x+5=x-(-5).
\]

### Mistake 2: Forgetting to square the radius

If

\[
r=\sqrt{40},
\]

then the equation uses

\[
r^2=40.
\]

Do not write

\[
(x+1)^2+(y-6)^2=\sqrt{40}.
\]

### Mistake 3: Using \(y=mx+c\) too early

For a line through a known point, use

\[
y-y_1=m(x-x_1).
\]

This avoids unnecessary algebra and reduces sign errors.

### Mistake 4: Confusing lowercase \(m\) with capital \(M\)

Use:

\[
m
\]

for gradient, and

\[
M
\]

for midpoint.

The transcript specifically warns that subscripts are useful. For example,

\[
m_r
\]

can mean radius gradient, while

\[
m_t
\]

can mean tangent gradient.

### Mistake 5: Only finding \(x\)-values for intersections

If solving a line-circle intersection gives

\[
x=-5,\quad x=2,
\]

you must substitute back into the line to get the full coordinates.

The answer should be written as points:

\[
(-5,1),\quad (2,8).
\]

### Mistake 6: Saying “tangent” but not using the discriminant

If a line just touches a circle, the resulting quadratic must have

\[
b^2-4ac=0.
\]

This is the algebraic fingerprint of tangency.

---

## Exam Technique Notes

1. **Start with a sketch.** It does not need to be perfect. It only needs to show what is centre, radius, chord, tangent or diameter.
2. **For circle equations, always ask: “Do I know the centre and radius?”**
3. **For tangents at a point, find the radius gradient first.**
4. **For unknown centres involving chords, use perpendicular bisectors.**
5. **For line-circle intersections, substitution creates the quadratic.**
6. **Use the discriminant to explain geometry.**
7. **If no particular form is requested, point-gradient form is acceptable for a line.**
8. **If \(ax+by+c=0\) is requested, rearrange fully and keep integer coefficients if possible.**
9. **Use exact forms.** Do not decimalise \(\sqrt{2}\), \(\sqrt{40}\), or fractions unless the question asks for decimals.

---

## Full Worked Solutions to Guided Practice

### Solution 1

Given

\[
A(2,5), \qquad B(6,7).
\]

Midpoint:

\[
M\left(\frac{2+6}{2},\frac{5+7}{2}\right)
=
M(4,6).
\]

Gradient:

\[
m_{AB}=\frac{7-5}{6-2}
=
\frac{2}{4}
=
\frac{1}{2}.
\]

Perpendicular gradient:

\[
m_{\perp}=-2.
\]

Equation:

\[
y-6=-2(x-4).
\]

So

\[
\boxed{y-6=-2(x-4)}.
\]

---

### Solution 2

Centre:

\[
C(3,5).
\]

Point of contact:

\[
P(6,9).
\]

Gradient of radius:

\[
m_r=\frac{9-5}{6-3}
=
\frac{4}{3}.
\]

Tangent gradient:

\[
m_t=-\frac{3}{4}.
\]

Tangent through \(P(6,9)\):

\[
y-9=-\frac{3}{4}(x-6).
\]

Multiply by \(4\):

\[
4y-36=-3(x-6).
\]

Expand:

\[
4y-36=-3x+18.
\]

Rearrange:

\[
3x+4y-54=0.
\]

Therefore,

\[
\boxed{3x+4y-54=0}.
\]

---

### Solution 3

Given

\[
A(0,0), \qquad B(4,2).
\]

The centre has \(x=-1\).

Find the perpendicular bisector of chord \(AB\).

Gradient:

\[
m_{AB}=\frac{2-0}{4-0}=\frac{2}{4}=\frac{1}{2}.
\]

Perpendicular gradient:

\[
m_{\perp}=-2.
\]

Midpoint:

\[
M\left(\frac{0+4}{2},\frac{0+2}{2}\right)
=
M(2,1).
\]

Equation of perpendicular bisector:

\[
y-1=-2(x-2).
\]

Since the centre has \(x=-1\), substitute \(x=-1\):

\[
y-1=-2(-1-2).
\]

\[
y-1=-2(-3).
\]

\[
y-1=6.
\]

\[
y=7.
\]

So the centre is

\[
C(-1,7).
\]

Find the radius using \(A(0,0)\):

\[
r=\sqrt{(0-(-1))^2+(0-7)^2}.
\]

\[
r=\sqrt{1^2+(-7)^2}.
\]

\[
r=\sqrt{1+49}.
\]

\[
r=\sqrt{50}.
\]

Therefore,

\[
r^2=50.
\]

The circle equation is

\[
\boxed{(x+1)^2+(y-7)^2=50}.
\]

---

### Solution 4

Given

\[
A(-8,1), \qquad B(4,5), \qquad C(-4,9).
\]

#### Part 1: Show \(AB\) is a diameter

Use distances.

\[
AC^2=(-4-(-8))^2+(9-1)^2.
\]

\[
AC^2=4^2+8^2.
\]

\[
AC^2=16+64=80.
\]

\[
BC^2=(-4-4)^2+(9-5)^2.
\]

\[
BC^2=(-8)^2+4^2.
\]

\[
BC^2=64+16=80.
\]

\[
AB^2=(4-(-8))^2+(5-1)^2.
\]

\[
AB^2=12^2+4^2.
\]

\[
AB^2=144+16=160.
\]

Now

\[
AC^2+BC^2=80+80=160.
\]

And

\[
AB^2=160.
\]

So

\[
AC^2+BC^2=AB^2.
\]

Therefore, by the angle-in-a-semicircle relationship, \(AB\) is the diameter of the circle.

#### Part 2: Find the equation

The centre is the midpoint of \(AB\):

\[
M\left(\frac{-8+4}{2},\frac{1+5}{2}\right)
=
M\left(\frac{-4}{2},\frac{6}{2}\right)
=
M(-2,3).
\]

Find radius using \(A(-8,1)\):

\[
r=\sqrt{(-8-(-2))^2+(1-3)^2}.
\]

\[
r=\sqrt{(-6)^2+(-2)^2}.
\]

\[
r=\sqrt{36+4}.
\]

\[
r=\sqrt{40}.
\]

So

\[
r^2=40.
\]

Therefore,

\[
\boxed{(x+2)^2+(y-3)^2=40}.
\]

---

### Solution 5

Given

\[
A(0,2), \qquad B(2,0), \qquad C(8,18).
\]

Find two perpendicular bisectors.

For \(AB\), the midpoint is

\[
M_{AB}\left(\frac{0+2}{2},\frac{2+0}{2}\right)
=
M_{AB}(1,1).
\]

Gradient of \(AB\):

\[
m_{AB}=\frac{0-2}{2-0}=-1.
\]

The perpendicular gradient is

\[
m_{\perp}=1.
\]

Through \((1,1)\):

\[
y-1=1(x-1).
\]

\[
y-1=x-1.
\]

\[
y=x.
\]

So the perpendicular bisector of \(AB\) is

\[
y=x.
\]

For \(AC\), midpoint:

\[
M_{AC}\left(\frac{0+8}{2},\frac{2+18}{2}\right)
=
M_{AC}(4,10).
\]

Gradient of \(AC\):

\[
m_{AC}=\frac{18-2}{8-0}
=
\frac{16}{8}
=
2.
\]

Perpendicular gradient:

\[
m_{\perp}=-\frac{1}{2}.
\]

Through \((4,10)\):

\[
y-10=-\frac{1}{2}(x-4).
\]

Now solve with

\[
y=x.
\]

Substitute \(y=x\):

\[
x-10=-\frac{1}{2}(x-4).
\]

Multiply by \(2\):

\[
2x-20=-(x-4).
\]

\[
2x-20=-x+4.
\]

\[
3x=24.
\]

\[
x=8.
\]

Since

\[
y=x,
\]

\[
y=8.
\]

So the centre is

\[
(8,8).
\]

Find radius using \(A(0,2)\):

\[
r=\sqrt{(0-8)^2+(2-8)^2}.
\]

\[
r=\sqrt{(-8)^2+(-6)^2}.
\]

\[
r=\sqrt{64+36}.
\]

\[
r=\sqrt{100}=10.
\]

So

\[
r^2=100.
\]

Therefore,

\[
\boxed{(x-8)^2+(y-8)^2=100}.
\]

---

## Syllabus Gap Check

| Requirement | Covered? | Evidence notes |
|---|---:|---|
| Straight line equations | Yes | Used in perpendicular bisectors and tangents. |
| Midpoints and lengths | Yes | Used in diameter and radius examples. |
| Perpendicular gradients | Yes | Used throughout. |
| Circle equation centre-radius form | Yes | Derived and used. |
| Circle equation expanded form | Yes | Completed-square examples included. |
| Completing the square | Yes | Several worked examples included. |
| Standard circle properties | Yes | Tangent-radius, chord bisector and angle in semicircle included. |
| Tangent through a point on circumference | Yes | Worked Example 10 and Guided Practice 2. |
| Line-circle intersections | Yes | Worked Examples 7 to 9. |
| MAT/STEP/AEA extension material | Not core | Logged as enrichment or excluded. |
| Incircle material | Excluded | Not part of supplied CCEA AS1-CG boundary. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| AS1CoordinateGeometryCirclesSVG-001 | SVG | Chord and perpendicular bisector. |
| AS1CoordinateGeometryCirclesSVG-002 | SVG | Origin-centred circle derivation. |
| AS1CoordinateGeometryCirclesSVG-003 | SVG | Shifted circle derivation. |
| AS1CoordinateGeometryCirclesSVG-004 | SVG | Secant, tangent, no intersection. |
| AS1CoordinateGeometryCirclesSVG-005 | SVG | Radius perpendicular to tangent. |
| AS1CoordinateGeometryCirclesSVG-006 | SVG | Perpendicular bisectors finding centre. |
| AS1CoordinateGeometryCirclesSVG-007 | SVG | Angle in semicircle and circumcircle. |
| AS1CoordinateGeometryCirclesWidget-001 | HTML widget | Circle equation explorer. |
| AS1CoordinateGeometryCirclesWidget-002 | HTML widget | Line-circle discriminant explorer. |
| AS1CoordinateGeometryCirclesWidget-003 | HTML widget | Tangent-gradient checker. |

---

## Supplementary Sources Used

No external sources beyond the uploaded/pre-loaded project evidence were used.

Cross-board or non-CCEA examples appearing inside the provided evidence:

| Source type | Status |
|---|---|
| Edexcel C2 examples | Used as on-spec support because the methods match CCEA AS1 coordinate geometry and algebra outcomes. |
| Pearson Pure Mathematics Year 1/AS references | Slide-visible references only. Unseen textbook pages were not used. |
| MAT/STEP/AEA extension questions | Excluded from core lesson. Optional enrichment only. |

---

## Final Student Checklist

Before moving on, make sure you can:

- [ ] find a midpoint from two coordinates;
- [ ] find the gradient of a line segment;
- [ ] find the negative reciprocal gradient;
- [ ] form a perpendicular bisector;
- [ ] write \((x-a)^2+(y-b)^2=r^2\) from centre and radius;
- [ ] identify centre and radius from a circle equation;
- [ ] complete the square in both \(x\) and \(y\);
- [ ] substitute a line equation into a circle equation;
- [ ] use \(b^2-4ac\) to identify \(0\), \(1\) or \(2\) intersections;
- [ ] find the equation of a tangent at a point;
- [ ] use perpendicular bisectors of chords to locate a centre;
- [ ] use angle-in-a-semicircle reasoning for a circumcircle problem;
- [ ] write final answers in the requested form.
