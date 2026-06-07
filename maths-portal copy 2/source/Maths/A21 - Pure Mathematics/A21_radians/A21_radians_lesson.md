# A21 Radians
## A2 1 Pure Mathematics, Trigonometry

## 1. Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A21: A2 1 Pure Mathematics |
| Topic code | A21-TRIG |
| Lesson title | Radians |
| Topic slug | radians |
| Topic Pascal | Radians |
| Topic ID | A21Radians |
| Lesson file | A21_radians_lesson.md |
| Primary LO | A21-TRIG-LO001 |
| Supporting LOs | A21-TRIG-LO008, A21-TRIG-LO009 |
| Tags | `#A21`, `#Trigonometry`, `#Radians`, `#ArcLength`, `#SectorArea`, `#TrigEquations`, `#SmallAngleBoundaryRisk` |

## 2. Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic and LO identity | Core authority |
| README-Module-Map.txt | File naming and lesson structure rules | Project metadata source |
| Source-Evidence-Drop-Checklist.txt | Missing evidence and boundary-risk logging rules | Project control source |
| Chapter_5_Radians_💡_(Pure_Year_2)_Transcript.md | Definitions, explanations, warnings, worked examples | Core lesson evidence |
| P2-Chp5-Radians_RevealBlocksRemoved.pdf | Slide text, overview, formulae, examples | Core lesson evidence where on-spec |
| Chapter_5_Radians_💡_(Pure_Year_2)_Screenshots.pdf | Visual confirmation only | No parsed text available; no uninspected detail invented |

The slide overview gives four lesson strands: converting between degrees and radians, arc length and sector area, trigonometric equations in radians, and small angle approximations. The transcript confirms the same structure and introduces radians as a different way of measuring angles.

## 3. Specification Alignment

The core CCEA alignment is:

- **A21-TRIG-LO001:** work with radian measure, including use for arc length and area of sector.

Supporting alignments:

- **A21-TRIG-LO008:** construct proofs involving trigonometric functions and identities.
- **A21-TRIG-LO009:** use trigonometric functions to solve problems in context.

This lesson directly teaches radian measure, conversion, arc length and sector area. Contextual sector, arc, segment and trigonometric equation examples support wider A21 trigonometry fluency.

## 4. Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain what one radian means geometrically.
2. Convert between degrees and radians using
   \[
   180^\circ=\pi,\qquad 360^\circ=2\pi.
   \]
3. Use common radian values without constantly converting back to degrees.
4. Sketch or interpret sine and cosine graphs with radian-labelled axes.
5. Evaluate common trig values in radians.
6. Solve trigonometric equations in radian intervals.
7. Derive and use the arc length formula
   \[
   l=r\theta.
   \]
8. Derive and use the sector area formula
   \[
   A=\frac12r^2\theta.
   \]
9. Use sector and segment methods in multi-step geometry problems.
10. Use small angle approximations carefully, while noting their CCEA boundary-risk status.

## 5. Prerequisite Recap, A-Level Evidence Only

This lesson relies on earlier A-Level trigonometry and algebra rather than external GCSE sources.

| Needed skill | Why it matters here |
|---|---|
| Sine, cosine and tangent graphs | Radian axes replace degree axes. |
| Exact trig values | Values like \(\sin \frac{\pi}{6}\), \(\cos \frac{4\pi}{3}\) appear. |
| Trig identities | Used when solving equations such as \(2\cos^2x+1=5\sin x\). |
| Triangle area formula \(\frac12ab\sin C\) | Needed for segment area. |
| Sine rule, cosine rule and right-angle trig | Used in sector and arc context problems. |
| Algebraic rearranging | Needed when solving \(p=2r+r\theta\), \(l=r\theta\), and trig quadratics. |

## 6. Big Picture Explanation

Degrees are useful because \(360\) splits neatly into many factors. This makes degrees friendly for measuring, drawing and sharing a circle into common pieces.

Radians are different. A radian is not based on chopping a full turn into \(360\) pieces. It is based on the circle itself.

One radian is the angle made at the centre of a circle when the arc length is equal to the radius. The lesson evidence describes this as the movement of one radius' worth around the circumference of the circle.

Radians become the natural angle language for higher mathematics because trigonometry and calculus work cleanly only when angles are measured in radians. The evidence notes that \(\sin x\) differentiates to \(\cos x\) only if \(x\) is in radians.

## 7. Key Definitions and Notation

### 7.1 Radian

A **radian** is the angle subtended at the centre of a circle by an arc whose length is equal to the radius.

If the radius is \(r\), and the arc length is also \(r\), then the angle at the centre is

\[
1\text{ radian}.
\]

### 7.2 Subtend

In this lesson, an arc **subtends** an angle at the centre when that angle stands opposite the arc.

### 7.3 Core symbols

| Symbol | Meaning |
|---|---|
| \(r\) | Radius of a circle or sector |
| \(\theta\) | Angle, usually in radians unless stated otherwise |
| \(l\) | Arc length |
| \(A\) | Area |
| \(P\), \(p\) | Perimeter |
| \(O\) | Centre of a circle |
| rad | Optional written unit for radians |

Important unit convention:

\[
45^\circ
\]

must include the degree sign, but radians usually do not need a written unit. If a radians unit is written, use `rad`.

## 8. Core Theory

## 8.1 Why \(180^\circ=\pi\)

For a circle of radius \(r\), the full circumference is

\[
2\pi r.
\]

A full turn corresponds to the full circumference, so

\[
360^\circ=2\pi\text{ radians}.
\]

Divide both sides by \(2\):

\[
180^\circ=\pi\text{ radians}.
\]

A half-turn is therefore

\[
\pi.
\]

A full turn is

\[
2\pi.
\]

The core memory anchor is:

\[
\boxed{180^\circ=\pi}.
\]

## 8.2 Converting between degrees and radians

The conversion core is

\[
180^\circ=\pi.
\]

### Degrees to radians

To convert degrees to radians:

\[
\text{radians}=\frac{\text{degrees}}{180}\pi.
\]

Example:

\[
45^\circ=\frac{45}{180}\pi
\]

\[
45^\circ=\frac14\pi
\]

\[
45^\circ=\frac{\pi}{4}.
\]

### Radians to degrees

To convert radians to degrees:

\[
\text{degrees}=\frac{\text{radians}}{\pi}\times180^\circ.
\]

Example:

\[
\frac{5\pi}{6}=\frac{5\pi}{6}\div\pi\times180^\circ
\]

\[
=\frac56\times180^\circ
\]

\[
=150^\circ.
\]

### Common conversions

| Degrees | Radians |
|---:|---:|
| \(30^\circ\) | \(\frac{\pi}{6}\) |
| \(45^\circ\) | \(\frac{\pi}{4}\) |
| \(60^\circ\) | \(\frac{\pi}{3}\) |
| \(90^\circ\) | \(\frac{\pi}{2}\) |
| \(120^\circ\) | \(\frac{2\pi}{3}\) |
| \(135^\circ\) | \(\frac{3\pi}{4}\) |
| \(150^\circ\) | \(\frac{5\pi}{6}\) |
| \(180^\circ\) | \(\pi\) |
| \(270^\circ\) | \(\frac{3\pi}{2}\) |
| \(360^\circ\) | \(2\pi\) |

## 8.3 Radian graphs

The sine and cosine graphs keep the same shape, but the \(x\)-axis labels change:

\[
90^\circ,\ 180^\circ,\ 270^\circ,\ 360^\circ
\]

become

\[
\frac{\pi}{2},\ \pi,\ \frac{3\pi}{2},\ 2\pi.
\]

### Example: sketching \(y=\cos\left(x+\frac{\pi}{2}\right)\)

The base graph is

\[
y=\cos x.
\]

The transformation is

\[
x\mapsto x+\frac{\pi}{2}.
\]

A plus inside the bracket shifts the graph left:

\[
\text{translation left by }\frac{\pi}{2}.
\]

The interval

\[
0\leq x<2\pi
\]

is the radian version of one full \(0^\circ\) to \(360^\circ\) cycle.

## 8.4 Trig values in radians

The same trig symmetry laws apply, but written in radians.

Degree form:

\[
\sin x=\sin(180^\circ-x)
\]

\[
\cos x=\cos(360^\circ-x)
\]

Radian form:

\[
\sin x=\sin(\pi-x)
\]

\[
\cos x=\cos(2\pi-x)
\]

Sine and cosine repeat every

\[
2\pi.
\]

Tangent repeats every

\[
\pi.
\]

### Example: evaluate \(\cos\frac{4\pi}{3}\)

Convert first, if helpful:

\[
\frac{4\pi}{3}=\frac43\times180^\circ
\]

\[
=240^\circ.
\]

Then

\[
\cos 240^\circ=\cos(360^\circ-240^\circ)
\]

\[
=\cos120^\circ.
\]

Since \(120^\circ\) is in quadrant II, cosine is negative:

\[
\cos120^\circ=-\cos60^\circ
\]

\[
=-\frac12.
\]

Therefore

\[
\cos\frac{4\pi}{3}=-\frac12.
\]

Calculator warning: to find trig functions directly in radians, the calculator must be in radians mode.

## 8.5 Arc length

The old degree formula is

\[
l=\frac{\theta}{360}\times2\pi r.
\]

For radians, a full turn is \(2\pi\), so the fraction of the circle is

\[
\frac{\theta}{2\pi}.
\]

Therefore

\[
l=\frac{\theta}{2\pi}\times2\pi r.
\]

Cancel \(2\pi\):

\[
l=\theta r.
\]

So

\[
\boxed{l=r\theta}
\]

where \(\theta\) must be in radians.

## 8.6 Sector area

The old degree formula is

\[
A=\frac{\theta}{360}\times\pi r^2.
\]

In radians, replace the fraction of the circle by

\[
\frac{\theta}{2\pi}.
\]

So

\[
A=\frac{\theta}{2\pi}\times\pi r^2.
\]

Cancel \(\pi\):

\[
A=\frac{\theta r^2}{2}.
\]

Therefore

\[
\boxed{A=\frac12r^2\theta}
\]

where \(\theta\) must be in radians.

## 8.7 Segment area

A segment is the region between a chord and the circumference. A segment is a sector with a triangle cut out.

For a sector of radius \(r\) and angle \(\theta\), the sector area is

\[
\frac12r^2\theta.
\]

The triangle inside the sector has sides \(r\) and \(r\) with included angle \(\theta\), so its area is

\[
\frac12r^2\sin\theta.
\]

Therefore

\[
\text{segment area}=\text{sector area}-\text{triangle area}
\]

\[
=\frac12r^2\theta-\frac12r^2\sin\theta
\]

\[
=\boxed{\frac12r^2(\theta-\sin\theta)}.
\]

## 8.8 Solving trig equations in radians

Solving trig equations in radians is almost the same as solving them in degrees, except:

1. The calculator must be in radians mode.
2. Use \(\pi-\theta\), \(2\pi-\theta\), and period \(2\pi\), rather than \(180^\circ-\theta\), \(360^\circ-\theta\), and \(360^\circ\).

For equations such as \(\sin(3\theta)=\frac{\sqrt3}{2}\), adjust the interval first, find all the values of \(3\theta\), and only then divide by \(3\).

## 8.9 Small angle approximations, boundary-risk section

The lesson evidence gives the small angle approximations:

\[
\sin\theta\approx\theta
\]

\[
\tan\theta\approx\theta
\]

\[
\cos\theta\approx1-\frac{\theta^2}{2}
\]

when \(\theta\) is small and measured in radians.

Important warning: these approximations require radians. This section is included because it appears in the supplied A-Level lesson evidence. It is not explicitly listed in the supplied CCEA A21-TRIG LO table, so it should be treated as evidence-backed support unless separately confirmed in the official CCEA specification.

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: A21RadiansSVG-001 | Source: Chapter 5 Radians slides and transcript | Insert from svg/A21RadiansSVG-001.svg | Purpose: Show one radian as an arc length equal to one radius.]

[VISUAL PLACEHOLDER: A21RadiansSVG-002 | Source: Chapter 5 Radians slides | Insert from svg/A21RadiansSVG-002.svg | Purpose: Radian conversion circle showing common radian angles.]

[VISUAL PLACEHOLDER: A21RadiansSVG-003 | Source: P2-Chp5-Radians PDF | Insert from svg/A21RadiansSVG-003.svg | Purpose: Sine and cosine graphs with radian-labelled axes.]

[VISUAL PLACEHOLDER: A21RadiansSVG-004 | Source: P2-Chp5-Radians PDF and transcript | Insert from svg/A21RadiansSVG-004.svg | Purpose: Sector diagram labelled \(r,\theta,l\), supporting \(l=r\theta\) and \(A=\frac12r^2\theta\).]

[VISUAL PLACEHOLDER: A21RadiansSVG-005 | Source: P2-Chp5-Radians PDF and transcript | Insert from svg/A21RadiansSVG-005.svg | Purpose: Segment as sector minus triangle, supporting \(\frac12r^2(\theta-\sin\theta)\).]

[INTERACTIVE PLACEHOLDER: A21RadiansWidget-001 | Source: Lesson evidence | Insert from widgets/A21RadiansWidget-001.html | Purpose: Drag a radius around a circle to see arc length and radian measure change together.]

[INTERACTIVE PLACEHOLDER: A21RadiansWidget-002 | Source: Lesson evidence | Insert from widgets/A21RadiansWidget-002.html | Purpose: Compare \(\sin x\), \(x\), \(\cos x\), \(1-\frac{x^2}{2}\), \(\tan x\) near zero.]

## 10. Worked Examples

### Example 1: Convert \(45^\circ\) to radians

\[
45^\circ=\frac{45}{180}\pi
\]

\[
=\frac14\pi
\]

\[
=\boxed{\frac{\pi}{4}}.
\]

### Example 2: Convert \(72^\circ\) to radians

\[
72^\circ=\frac{72}{180}\pi
\]

Simplify the fraction:

\[
\frac{72}{180}=\frac25.
\]

So:

\[
72^\circ=\boxed{\frac{2\pi}{5}}.
\]

### Example 3: Convert \(\frac{5\pi}{6}\) to degrees

\[
\frac{5\pi}{6}=\frac{5\pi}{6}\div\pi\times180^\circ
\]

\[
=\frac56\times180^\circ
\]

\[
=5\times30^\circ
\]

\[
=\boxed{150^\circ}.
\]

### Example 4: Arc length with known radius and angle

Find the length of the arc of a circle of radius \(5.2\text{ cm}\), given that the arc subtends an angle of \(0.8\) radians at the centre.

Use:

\[
l=r\theta.
\]

Substitute:

\[
l=5.2\times0.8.
\]

Calculate:

\[
l=4.16.
\]

Therefore:

\[
\boxed{l=4.16\text{ cm}}.
\]

### Example 5: Find the angle from arc length

An arc of a circle with radius \(7\text{ cm}\) has length \(2.45\text{ cm}\). Find the angle subtended at the centre.

Use:

\[
l=r\theta.
\]

Substitute:

\[
2.45=7\theta.
\]

Divide by \(7\):

\[
\theta=\frac{2.45}{7}.
\]

\[
\theta=0.35.
\]

Therefore:

\[
\boxed{\theta=0.35\text{ radians}}.
\]

### Example 6: Rearranging sector perimeter

An arc \(AB\) of a circle has centre \(O\), radius \(r\), and angle \(\theta\) radians. The perimeter of sector \(AOB\) is \(p\). Express \(r\) in terms of \(p\) and \(\theta\).

The sector perimeter is:

\[
p=r+r+l.
\]

Since:

\[
l=r\theta,
\]

we get:

\[
p=r+r+r\theta.
\]

\[
p=2r+r\theta.
\]

Factorise \(r\):

\[
p=r(2+\theta).
\]

Divide by \(2+\theta\):

\[
\boxed{r=\frac{p}{2+\theta}}.
\]

### Example 7: Pond arc length

A garden pond has a straight edge of length \(2.4\text{ m}\). The curved part is an arc of a circle with centre \(O\) and radius \(2\text{ m}\). Find the length of the curved arc.

Split the isosceles triangle into two right-angled triangles.

Half of the straight edge is:

\[
\frac{2.4}{2}=1.2.
\]

The radius is:

\[
2.
\]

Let the small angle in one right triangle be \(\alpha\). Then:

\[
\sin\alpha=\frac{1.2}{2}.
\]

\[
\alpha=\sin^{-1}\left(\frac{1.2}{2}\right).
\]

\[
\alpha=0.6435\ldots
\]

The minor central angle is:

\[
2\alpha=2(0.6435\ldots).
\]

The major central angle is:

\[
\theta=2\pi-2\alpha.
\]

\[
\theta=2\pi-2(0.6435\ldots).
\]

\[
\theta=4.9961\ldots
\]

The arc length is:

\[
l=r\theta.
\]

\[
l=2(4.9961\ldots).
\]

\[
l=9.9922\ldots
\]

To 3 significant figures:

\[
\boxed{l=9.99\text{ m}}.
\]

### Example 8: Sector area from radius and angle

A minor sector has area \(28.9\text{ cm}^2\) and angle \(0.8\) radians. Find the radius.

Use:

\[
A=\frac12r^2\theta.
\]

Substitute:

\[
28.9=\frac12r^2(0.8).
\]

\[
28.9=0.4r^2.
\]

Divide by \(0.4\):

\[
r^2=\frac{28.9}{0.4}.
\]

\[
r^2=72.25.
\]

Square root:

\[
r=\sqrt{72.25}.
\]

\[
\boxed{r=8.5\text{ cm}}.
\]

### Example 9: Fenced sector plot

A plot of land is a sector of a circle with radius \(55\text{ m}\). The fencing around the plot is \(176\text{ m}\). Find the area.

The perimeter consists of two radii and the arc:

\[
176=55+55+l.
\]

\[
l=176-55-55.
\]

\[
l=66.
\]

Use:

\[
l=r\theta.
\]

\[
66=55\theta.
\]

\[
\theta=\frac{66}{55}.
\]

\[
\theta=1.2.
\]

Now use sector area:

\[
A=\frac12r^2\theta.
\]

\[
A=\frac12(55)^2(1.2).
\]

\[
A=\frac12(3025)(1.2).
\]

\[
A=1815.
\]

Therefore:

\[
\boxed{1815\text{ m}^2}.
\]

### Example 10: Segment area with chord \(5\) and radius \(4\)

A sector has radius \(4\text{ m}\) and chord \(5\text{ m}\). Find the shaded segment.

First find the central angle \(\theta\) using the cosine rule.

\[
5^2=4^2+4^2-2(4)(4)\cos\theta.
\]

\[
25=16+16-32\cos\theta.
\]

\[
25=32-32\cos\theta.
\]

Subtract \(32\):

\[
-7=-32\cos\theta.
\]

Divide by \(-32\):

\[
\cos\theta=\frac{7}{32}.
\]

\[
\theta=\cos^{-1}\left(\frac{7}{32}\right).
\]

Now use the segment formula:

\[
A_{\text{segment}}=\frac12r^2(\theta-\sin\theta).
\]

Substitute \(r=4\):

\[
A_{\text{segment}}=\frac12(4)^2(\theta-\sin\theta).
\]

\[
A_{\text{segment}}=8(\theta-\sin\theta).
\]

With:

\[
\theta=\cos^{-1}\left(\frac{7}{32}\right),
\]

\[
A_{\text{segment}}=8\left[\cos^{-1}\left(\frac{7}{32}\right)-\sin\left(\cos^{-1}\left(\frac{7}{32}\right)\right)\right].
\]

Numerically:

\[
\theta=1.350263\ldots
\]

\[
A_{\text{segment}}=2.995857\ldots
\]

So:

\[
\boxed{A_{\text{segment}}\approx3.00\text{ m}^2}.
\]

### Example 11: Solve \(\sin(3\theta)=\frac{\sqrt3}{2}\), \(0\leq\theta\leq2\pi\)

First adjust the interval.

\[
0\leq\theta\leq2\pi.
\]

Multiply all parts by \(3\):

\[
0\leq3\theta\leq6\pi.
\]

Solve:

\[
\sin(3\theta)=\frac{\sqrt3}{2}.
\]

In one \(2\pi\) cycle:

\[
3\theta=\frac{\pi}{3},\quad \frac{2\pi}{3}.
\]

Add \(2\pi\) to each:

\[
3\theta=\frac{\pi}{3},\quad \frac{2\pi}{3},\quad \frac{7\pi}{3},\quad \frac{8\pi}{3},\quad \frac{13\pi}{3},\quad \frac{14\pi}{3}.
\]

Now divide by \(3\):

\[
\theta=\frac{\pi}{9},\quad \frac{2\pi}{9},\quad \frac{7\pi}{9},\quad \frac{8\pi}{9},\quad \frac{13\pi}{9},\quad \frac{14\pi}{9}.
\]

Therefore:

\[
\boxed{\theta=\frac{\pi}{9},\frac{2\pi}{9},\frac{7\pi}{9},\frac{8\pi}{9},\frac{13\pi}{9},\frac{14\pi}{9}}.
\]

### Example 12: Solve \(2\cos^2x+1=5\sin x\), \(0\leq x<2\pi\)

Use:

\[
\cos^2x=1-\sin^2x.
\]

Substitute:

\[
2(1-\sin^2x)+1=5\sin x.
\]

Expand:

\[
2-2\sin^2x+1=5\sin x.
\]

\[
3-2\sin^2x=5\sin x.
\]

Bring all terms to one side:

\[
2\sin^2x+5\sin x-3=0.
\]

Factorise:

\[
(2\sin x-1)(\sin x+3)=0.
\]

So:

\[
2\sin x-1=0
\]

or

\[
\sin x+3=0.
\]

First equation:

\[
2\sin x=1.
\]

\[
\sin x=\frac12.
\]

Second equation:

\[
\sin x=-3.
\]

This is impossible because:

\[
-1\leq\sin x\leq1.
\]

So solve:

\[
\sin x=\frac12.
\]

In \(0\leq x<2\pi\):

\[
x=\frac{\pi}{6},\quad x=\frac{5\pi}{6}.
\]

Therefore:

\[
\boxed{x=\frac{\pi}{6},\frac{5\pi}{6}}.
\]

### Example 13: Small angle approximation substitution

Given that \(\theta\) is small and measured in radians, approximate:

\[
12\tan\theta-3\sin^2\left(\frac{\theta}{2}\right)+2\cos\left(\frac{\theta}{2}\right)
\]

in the form:

\[
a+b\theta+c\theta^2.
\]

Use:

\[
\tan\theta\approx\theta,
\]

\[
\sin u\approx u,
\]

\[
\cos u\approx1-\frac{u^2}{2}.
\]

Start:

\[
12\tan\theta-3\sin^2\left(\frac{\theta}{2}\right)+2\cos\left(\frac{\theta}{2}\right)
\]

Approximate each part:

\[
\approx12\theta-3\left(\frac{\theta}{2}\right)^2+2\left(1-\frac{\left(\frac{\theta}{2}\right)^2}{2}\right).
\]

Now simplify:

\[
=12\theta-3\left(\frac{\theta^2}{4}\right)+2\left(1-\frac{\theta^2}{8}\right).
\]

\[
=12\theta-\frac{3\theta^2}{4}+2-\frac{2\theta^2}{8}.
\]

\[
=12\theta-\frac{3\theta^2}{4}+2-\frac{\theta^2}{4}.
\]

Group terms:

\[
=2+12\theta-\left(\frac{3\theta^2}{4}+\frac{\theta^2}{4}\right).
\]

\[
=2+12\theta-\frac{4\theta^2}{4}.
\]

\[
=2+12\theta-\theta^2.
\]

Therefore:

\[
\boxed{a=2,\quad b=12,\quad c=-1}.
\]

## 11. Guided Practice

### Practice 1: Conversions

Convert each angle.

1. \(30^\circ\) to radians
2. \(120^\circ\) to radians
3. \(\frac{7\pi}{6}\) to degrees
4. \(\frac{11\pi}{6}\) to degrees

### Practice 2: Arc length

A sector has radius \(9\text{ cm}\) and angle \(1.4\) radians. Find the arc length.

### Practice 3: Sector area

A sector has radius \(6\text{ m}\) and angle \(2.1\) radians. Find the area.

### Practice 4: Rearranging arc length

An arc has length \(12\text{ cm}\) and angle \(0.75\) radians. Find the radius.

### Practice 5: Segment area

A sector has radius \(10\text{ cm}\) and angle \(1.2\) radians. Find the area of the minor segment.

### Practice 6: Trig equation

Solve:

\[
\sin x=\frac12
\]

for:

\[
0\leq x<2\pi.
\]

### Practice 7: Multiple-angle trig equation

Solve:

\[
\cos(2x)=\frac12
\]

for:

\[
0\leq x<2\pi.
\]

### Practice 8: Small angle approximation

For small \(\theta\), approximate:

\[
5\sin(2\theta)+3\tan\theta-4\cos\theta
\]

in the form:

\[
a+b\theta+c\theta^2.
\]

## 12. Common Mistakes and Exam Traps

| Mistake | Why it matters | Fix |
|---|---|---|
| Using degree mode for \(\sin,\cos,\tan\) with radian inputs | Calculator output becomes wrong | Put calculator in radians mode before trig calculations. |
| Converting radians back to degrees for every question | Slows the method and increases error risk | Learn to think directly in radians. |
| Using \(l=\frac{\theta}{360}\times2\pi r\) when \(\theta\) is in radians | Wrong unless \(\theta\) is degrees | Use \(l=r\theta\). |
| Forgetting \(\theta\) must be in radians for \(l=r\theta\) and \(A=\frac12r^2\theta\) | Formula misuse | Convert angle first if it is given in degrees. |
| Dividing by \(3\) too early in \(\sin(3x)\) equations | Loses solutions | Adjust interval for \(3x\), find all values, then divide. |
| Treating \(\sin x=-3\) as solvable | Impossible because sine is between \(-1\) and \(1\) | Reject impossible trig values. |
| Using segment formula without radians | \(\frac12r^2(\theta-\sin\theta)\) assumes radian \(\theta\) | Check calculator is in radians mode. |
| Using small angle approximations for large \(\theta\) | Approximation becomes poor | Use only when \(\theta\) is small and in radians. |

## 13. Exam Technique Notes

1. Write degree signs only for degrees. If there is no degree sign, expect radians.
2. Memorise:
   \[
   180^\circ=\pi,\qquad 360^\circ=2\pi.
   \]
3. Memorise:
   \[
   l=r\theta,\qquad A=\frac12r^2\theta.
   \]
4. For sector perimeter:
   \[
   P=2r+r\theta.
   \]
5. For segment area:
   \[
   A=\frac12r^2(\theta-\sin\theta).
   \]
6. For trig equations in radians, rewrite the interval first if the angle is \(2x\), \(3x\), etc.
7. Calculator radians mode matters when using trig functions, not for multiplication such as \(5.2\times0.8\).

## 14. Full Worked Solutions to Guided Practice

### Solution 1

1.
\[
30^\circ=\frac{30}{180}\pi=\frac{\pi}{6}.
\]

2.
\[
120^\circ=\frac{120}{180}\pi=\frac{2\pi}{3}.
\]

3.
\[
\frac{7\pi}{6}=\frac76\times180^\circ=210^\circ.
\]

4.
\[
\frac{11\pi}{6}=\frac{11}{6}\times180^\circ=330^\circ.
\]

### Solution 2

\[
l=r\theta.
\]

\[
l=9(1.4).
\]

\[
l=12.6.
\]

\[
\boxed{12.6\text{ cm}}.
\]

### Solution 3

\[
A=\frac12r^2\theta.
\]

\[
A=\frac12(6)^2(2.1).
\]

\[
A=\frac12(36)(2.1).
\]

\[
A=18(2.1).
\]

\[
A=37.8.
\]

\[
\boxed{37.8\text{ m}^2}.
\]

### Solution 4

\[
l=r\theta.
\]

\[
12=0.75r.
\]

\[
r=\frac{12}{0.75}.
\]

\[
r=16.
\]

\[
\boxed{16\text{ cm}}.
\]

### Solution 5

\[
A_{\text{segment}}=\frac12r^2(\theta-\sin\theta).
\]

\[
A_{\text{segment}}=\frac12(10)^2(1.2-\sin1.2).
\]

\[
A_{\text{segment}}=50(1.2-\sin1.2).
\]

Using radians:

\[
\sin1.2=0.9320\ldots
\]

\[
A_{\text{segment}}=50(1.2-0.9320\ldots).
\]

\[
A_{\text{segment}}=50(0.2679\ldots).
\]

\[
A_{\text{segment}}=13.397\ldots
\]

\[
\boxed{13.4\text{ cm}^2}.
\]

### Solution 6

\[
\sin x=\frac12.
\]

In one full radian cycle:

\[
x=\frac{\pi}{6},\quad x=\frac{5\pi}{6}.
\]

Both are in:

\[
0\leq x<2\pi.
\]

So:

\[
\boxed{x=\frac{\pi}{6},\frac{5\pi}{6}}.
\]

### Solution 7

\[
\cos(2x)=\frac12.
\]

First adjust the interval:

\[
0\leq x<2\pi.
\]

Multiply by \(2\):

\[
0\leq2x<4\pi.
\]

Solve:

\[
\cos(2x)=\frac12.
\]

In \(0\leq2x<2\pi\):

\[
2x=\frac{\pi}{3},\quad \frac{5\pi}{3}.
\]

In the next cycle:

\[
2x=\frac{\pi}{3}+2\pi,\quad \frac{5\pi}{3}+2\pi.
\]

\[
2x=\frac{\pi}{3},\quad \frac{5\pi}{3},\quad \frac{7\pi}{3},\quad \frac{11\pi}{3}.
\]

Now divide by \(2\):

\[
x=\frac{\pi}{6},\quad \frac{5\pi}{6},\quad \frac{7\pi}{6},\quad \frac{11\pi}{6}.
\]

\[
\boxed{x=\frac{\pi}{6},\frac{5\pi}{6},\frac{7\pi}{6},\frac{11\pi}{6}}.
\]

### Solution 8

Use:

\[
\sin\theta\approx\theta,\qquad \tan\theta\approx\theta,\qquad \cos\theta\approx1-\frac{\theta^2}{2}.
\]

Start:

\[
5\sin(2\theta)+3\tan\theta-4\cos\theta.
\]

Approximate:

\[
\sin(2\theta)\approx2\theta,
\]

\[
\tan\theta\approx\theta,
\]

\[
\cos\theta\approx1-\frac{\theta^2}{2}.
\]

So:

\[
5\sin(2\theta)+3\tan\theta-4\cos\theta
\approx
5(2\theta)+3\theta-4\left(1-\frac{\theta^2}{2}\right).
\]

Expand:

\[
=10\theta+3\theta-4+2\theta^2.
\]

Collect terms:

\[
= -4+13\theta+2\theta^2.
\]

Therefore:

\[
\boxed{a=-4,\quad b=13,\quad c=2}.
\]

## 15. Common CCEA-Style Wording

| Wording | Meaning |
|---|---|
| “subtends an angle at the centre” | The arc creates that central angle. |
| “in terms of \(\pi\)” | Give exact radian answers, not decimals. |
| “giving each solution in the interval” | Only list solutions inside the stated interval. |
| “sector” | Region enclosed by two radii and an arc. |
| “segment” | Region enclosed by a chord and an arc. |
| “minor arc” | Shorter arc between two points. |
| “major arc” | Longer arc between two points. |

## 16. Syllabus Gap Check

| Content | Covered? | Notes |
|---|---|---|
| Radian measure | Yes | Definition, \(180^\circ=\pi\), common conversions. |
| Arc length | Yes | Formula derived and used. |
| Sector area | Yes | Formula derived and used. |
| Contextual trig/radian problems | Yes | Pond, fencing, sector and trig equations. |
| Proof/derivation style | Yes | Arc length, sector area, segment area. |
| Small angle approximations | Included with caution | Evidence-backed but not explicit in supplied CCEA LO table. |
| Full visual asset files | Yes | Produced in Mermaid, SVG, TikZ and widget phases. |
| Complex screenshot-only diagrams | Partially logged | No invented details. |

## 17. Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A21RadiansMermaid-001 to 007 | Mermaid | Lesson flow, formula choice, conversion and trig-equation workflows |
| A21RadiansSVG-001 | SVG | One-radian definition diagram |
| A21RadiansSVG-002 | SVG | Radian conversion circle |
| A21RadiansSVG-003 | SVG | Sine and cosine graphs in radians |
| A21RadiansSVG-004 | SVG | Sector diagram for \(l=r\theta\), \(A=\frac12r^2\theta\) |
| A21RadiansSVG-005 | SVG | Segment equals sector minus triangle |
| A21RadiansTikZ-001 to 007 | TikZ | Printable mathematical diagrams |
| A21RadiansWidget-001 | HTML widget | Dynamic radian measure and arc length |
| A21RadiansWidget-002 | HTML widget | Small angle approximation comparison |

## 18. Supplementary Sources Used

| Source | Status |
|---|---|
| Dr Frost / P2 Chapter 5 Radians slide PDF | Lesson evidence, cross-board style, used only where CCEA-aligned |
| Pearson Pure Mathematics Year 2/AS exercise references | Mentioned in evidence, not independently used |
| Edexcel past-paper style questions | Used only for on-spec radian methods |
| MAT extension material | Excluded from core lesson |

## 19. Final Student Checklist

Tick these when ready:

- [ ] I know that \(180^\circ=\pi\) and \(360^\circ=2\pi\).
- [ ] I can convert between degrees and radians.
- [ ] I know common values such as \(\frac{\pi}{6},\frac{\pi}{4},\frac{\pi}{3},\frac{\pi}{2}\).
- [ ] I can label trig graphs using radians.
- [ ] I can evaluate common trig values in radians.
- [ ] I can solve trig equations on radian intervals.
- [ ] I can derive and use \(l=r\theta\).
- [ ] I can derive and use \(A=\frac12r^2\theta\).
- [ ] I can solve sector perimeter problems.
- [ ] I can find segment areas using sector minus triangle.
- [ ] I know when calculator radians mode matters.
- [ ] I know small angle approximations require \(\theta\) to be small and in radians.
- [ ] I understand that small angle approximations are included here as evidence-backed boundary-risk content unless confirmed directly in CCEA materials.
