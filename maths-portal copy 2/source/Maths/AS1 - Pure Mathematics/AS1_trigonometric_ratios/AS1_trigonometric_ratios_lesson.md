# AS1 Trigonometric Ratios

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Official topic area | Trigonometry |
| Lesson title | Trigonometric Ratios |
| Topic code | AS1-TRIG |
| Topic slug | trigonometric_ratios |
| Topic Pascal | TrigonometricRatios |
| Topic ID | AS1TrigonometricRatios |
| Lesson file | AS1_trigonometric_ratios_lesson.md |
| Core LO IDs | AS1-TRIG-LO001, AS1-TRIG-LO002, AS1-TRIG-LO003, AS1-TRIG-LO004 |
| Partial bridge LO ID | AS1-TRIG-LO007 |
| Logged gaps | AS1-TRIG-LO005, AS1-TRIG-LO006 |

---

## Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Official unit, topic and LO boundaries | Core authority |
| README-Module-Map.txt | Metadata conventions and file naming | Project authority |
| Source-Evidence-Drop-Checklist.txt | Required logs and visual placeholder rules | Project authority |
| P1-Chp9-TrigonometricRatios.pdf | Slide content, examples, formulas, graph features and derivations | Lesson evidence |
| Chapter 9 Trigonometric Ratios transcript | Teacher explanations, warnings, rearrangement advice and transformation clarifications | Lesson evidence |
| Chapter 9 screenshots PDF | Visual confirmation of slide layout and handwritten working | Visual evidence |

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| AS1-TRIG-LO001 | Defines and uses sine, cosine and tangent as ratios and functions. |
| AS1-TRIG-LO002 | Teaches sine rule, cosine rule and the ambiguous case of the sine rule. |
| AS1-TRIG-LO003 | Teaches the area formula \(\frac12ab\sin C\). |
| AS1-TRIG-LO004 | Teaches sine, cosine and tangent graphs, symmetries, periodicity and simple transformations. |
| AS1-TRIG-LO007 | Partially prepared through graph symmetry and multiple possible sine values. Full trig equations belong in a later lesson. |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain sine, cosine and tangent as trigonometric ratios.
2. Choose between right-angled trigonometry, sine rule, cosine rule and the area formula.
3. Use the cosine rule to find missing sides and angles.
4. Use the sine rule to find missing sides and angles.
5. Recognise the ambiguous sine-rule case.
6. Use \(\frac12ab\sin C\) for non-right-angled triangle areas.
7. Combine triangle rules in multi-step context problems.
8. Sketch and interpret \(y=\sin x\), \(y=\cos x\), and \(y=\tan x\).
9. Apply simple transformations to trig graphs.

---

## Prerequisite Recap

For a right-angled triangle with angle \(\theta\):

\[
\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}},\qquad
\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}},\qquad
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}.
\]

A ratio means relative size. Since \(\sin\), \(\cos\) and \(\tan\) compare side lengths, they are called trigonometric ratios.

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-001 | Source: P1-Chp9-TrigonometricRatios.pdf p.4 + screenshots PDF | Insert from svg/AS1TrigonometricRatiosSVG-001.svg | Purpose: Label opposite, adjacent and hypotenuse for a right-angled triangle.]

### Example: finding a side

\[
\cos20^\circ=\frac{4}{x}
\]

\[
x=\frac{4}{\cos20^\circ}=4.26\text{ cm } \quad \text{to 3 significant figures.}
\]

### Example: finding an angle

\[
\tan\theta=\frac{5}{3}
\]

\[
\theta=\tan^{-1}\left(\frac{5}{3}\right)=59.0^\circ.
\]

The notation \(\tan^{-1}\) means inverse tangent, not \(1/\tan\theta\).

---

## Big Picture Explanation

Right-angled trigonometry works directly only when there is a right angle. When triangles are not right-angled, the chapter evidence says we must use the sine and cosine rules. The chapter then moves from triangle calculation to trig graphs, because graph symmetry explains why one trig value can correspond to more than one angle.

---

## Key Definitions and Notation

### Complementary sine and cosine

If two acute angles in a right-angled triangle are \(50^\circ\) and \(40^\circ\), and the relevant sides are \(x\) and \(z\), then:

\[
\cos50^\circ=\frac{x}{z},\qquad \sin40^\circ=\frac{x}{z}.
\]

Therefore:

\[
\cos50^\circ=\sin40^\circ.
\]

In general:

\[
\cos\theta=\sin(90^\circ-\theta),\qquad \sin\theta=\cos(90^\circ-\theta).
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosTIKZ-010 | Source: P1-Chp9-TrigonometricRatios.pdf p.5 | Insert from tikz/AS1TrigonometricRatiosTIKZ-010.tex | Purpose: Show complementary sine and cosine in a right-angled triangle.]

---

## Core Theory

## 1. Choosing the Correct Rule

| You have | You want | Use |
|---|---|---|
| Two angle-side opposite pairs | Missing angle or side in one pair | Sine rule |
| Two sides and the included angle, or three sides involved | Missing side or angle | Cosine rule |
| Two sides and the included angle, with area required | Area | \(\frac12ab\sin C\) |
| Two sides known and missing side not opposite the known angle | Remaining side | Sine rule twice |

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosMER-001 | Source: P1-Chp9-TrigonometricRatios.pdf p.6 | Insert from mermaid/AS1TrigonometricRatiosMER-001.md | Purpose: Decision flowchart for sine rule, cosine rule, area formula and sine rule twice.]

[INTERACTIVE PLACEHOLDER: AS1TrigonometricRatiosWidget-001 | Source: P1-Chp9-TrigonometricRatios.pdf p.6 + transcript | Insert from widgets/AS1TrigonometricRatiosWidget-001.html | Purpose: Interactive method selector.]

---

## 2. The Cosine Rule

For a triangle labelled in the standard way:

\[
a^2=b^2+c^2-2bc\cos A.
\]

The side \(a\) is opposite the angle \(A\). The other two sides \(b\) and \(c\) can be swapped.

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-003 | Source: P1-Chp9-TrigonometricRatios.pdf p.7 | Insert from svg/AS1TrigonometricRatiosSVG-003.svg | Purpose: Show \(A\) opposite \(a\), \(B\) opposite \(b\), and \(C\) opposite \(c\).]

### Missing side example

\[
x^2=15^2+12^2-2\times15\times12\times\cos115^\circ
\]

\[
x^2=225+144-360\cos115^\circ
\]

\[
x^2=521.14257\ldots
\]

\[
x=\sqrt{521.14257\ldots}=22.83.
\]

### Missing angle example

\[
4^2=7^2+9^2-2\times7\times9\cos\alpha
\]

\[
16=49+81-126\cos\alpha
\]

\[
16=130-126\cos\alpha
\]

\[
126\cos\alpha=130-16=114
\]

\[
\cos\alpha=\frac{114}{126}
\]

\[
\alpha=\cos^{-1}\left(\frac{114}{126}\right)=25.2^\circ.
\]

### Evidence-backed warning: BIDMAS trap

Do not simplify

\[
7^2+9^2-2\times7\times9\cos\alpha
\]

as though the whole expression becomes one multiplication. The correct simplification is:

\[
16=130-126\cos\alpha.
\]

---

## 3. Harder Cosine Rule Example: Algebraic Side Lengths

Determine \(x\) in the triangle where the sides around a \(60^\circ\) angle are \(x\) and \(x+8\), and the opposite side is \(2x-1\).

\[
(2x-1)^2=x^2+(x+8)^2-2x(x+8)\cos60^\circ
\]

Since \(\cos60^\circ=\frac12\):

\[
(2x-1)^2=x^2+(x+8)^2-x(x+8)
\]

\[
4x^2-4x+1=x^2+x^2+16x+64-x^2-8x
\]

\[
4x^2-4x+1=x^2+8x+64
\]

\[
3x^2-12x-63=0
\]

\[
x^2-4x-21=0
\]

\[
(x+3)(x-7)=0
\]

\[
x=-3\quad\text{or}\quad x=7.
\]

Since a length cannot be negative:

\[
x=7.
\]

---

## 4. Bearings Context

A coastguard station \(B\) is \(8\text{ km}\) on a bearing of \(060^\circ\) from station \(A\). A ship \(C\) is \(4.8\text{ km}\) on a bearing of \(018^\circ\) from \(A\). Find \(CB\).

\[
60^\circ-18^\circ=42^\circ
\]

\[
a^2=4.8^2+8^2-2\times4.8\times8\cos42^\circ
\]

\[
a=5.47\text{ km}\quad\text{to 3 significant figures.}
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-004 | Source: P1-Chp9-TrigonometricRatios.pdf p.9 | Insert from svg/AS1TrigonometricRatiosSVG-004.svg | Purpose: Bearing diagram showing \(060^\circ\), \(018^\circ\), the included \(42^\circ\), and triangle \(ABC\).]

---

## 5. The Sine Rule

\[
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}.
\]

Use the sine rule when you have two opposite angle-side pairs.

For missing angles, it is often cleaner to use the reciprocal form:

\[
\frac{\sin A}{a}=\frac{\sin B}{b}.
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-005 | Source: P1-Chp9-TrigonometricRatios.pdf p.13 | Insert from svg/AS1TrigonometricRatiosSVG-005.svg | Purpose: Triangle diagram showing opposite pairs \(a,A\), \(b,B\), \(c,C\).]

### Missing side examples

\[
\frac{x}{\sin85^\circ}=\frac{8}{\sin45^\circ}
\]

\[
x=\frac{8\sin85^\circ}{\sin45^\circ}=11.27.
\]

\[
\frac{x}{\sin100^\circ}=\frac{8}{\sin30^\circ}
\]

\[
x=\frac{8\sin100^\circ}{\sin30^\circ}=15.76.
\]

### Missing angle examples

\[
\frac{\sin\theta}{5}=\frac{\sin85^\circ}{6}
\]

\[
\sin\theta=\frac{5\sin85^\circ}{6}
\]

\[
\theta=\sin^{-1}\left(\frac{5\sin85^\circ}{6}\right)=56.11^\circ.
\]

\[
\frac{\sin\theta}{8}=\frac{\sin126^\circ}{10}
\]

\[
\sin\theta=\frac{8\sin126^\circ}{10}
\]

\[
\theta=\sin^{-1}\left(\frac{8\sin126^\circ}{10}\right)=40.33^\circ.
\]

---

## 6. The Ambiguous Case of the Sine Rule

Suppose:

\[
AB=4,\quad AC=3,\quad \angle ABC=44^\circ.
\]

Using the sine rule:

\[
\frac{\sin C}{4}=\frac{\sin44^\circ}{3}
\]

\[
\sin C=\frac{4\sin44^\circ}{3}=0.9262\ldots
\]

The calculator gives:

\[
C=\sin^{-1}(0.9262\ldots)=67.9^\circ.
\]

But:

\[
\sin\theta=\sin(180^\circ-	heta).
\]

So the second possible angle is:

\[
180^\circ-67.9^\circ=112.1^\circ.
\]

Therefore:

\[
C=67.9^\circ\quad\text{or}\quad C=112.1^\circ.
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-006 | Source: P1-Chp9-TrigonometricRatios.pdf p.17 | Insert from svg/AS1TrigonometricRatiosSVG-006.svg | Purpose: Ambiguous sine rule diagram showing two possible positions of \(C\) and sine graph symmetry.]

[INTERACTIVE PLACEHOLDER: AS1TrigonometricRatiosWidget-002 | Source: P1-Chp9-TrigonometricRatios.pdf pp.17-18 | Insert from widgets/AS1TrigonometricRatiosWidget-002.html | Purpose: Interactive ambiguous sine-rule explorer.]

### Ambiguous case worked example

\[
\frac{\sin\theta}{10}=\frac{\sin20^\circ}{5}
\]

\[
\sin\theta=\frac{10\sin20^\circ}{5}
\]

\[
\sin^{-1}\left(\frac{10\sin20^\circ}{5}\right)=43.1602^\circ.
\]

Given \(\theta\) is obtuse:

\[
\theta=180^\circ-43.1602^\circ=136.8398^\circ.
\]

Remaining angle:

\[
180^\circ-136.8398^\circ-20^\circ=23.1602^\circ.
\]

Using sine rule again:

\[
\frac{x}{\sin23.1602^\circ}=\frac{5}{\sin20^\circ}
\]

\[
x=\frac{5\sin23.1602^\circ}{\sin20^\circ}=5.75\quad\text{to 3 significant figures.}
\]

---

## 7. Area of a Non-Right-Angled Triangle

\[
\text{Area}=\frac12ab\sin C.
\]

Here \(C\) is the included angle between sides \(a\) and \(b\).

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-007 | Source: P1-Chp9-TrigonometricRatios.pdf p.20 | Insert from svg/AS1TrigonometricRatiosSVG-007.svg | Purpose: Triangle with two sides \(a,b\) and included angle \(C\) highlighted.]

Example:

\[
\text{Area}=\frac12\times3\times7\times\sin59^\circ=9.00\text{ cm}^2.
\]

### Area formula producing a quadratic

\[
\frac12x(x+3)\sin30^\circ=10
\]

\[
\frac12x(x+3)\times\frac12=10
\]

\[
\frac14x(x+3)=10
\]

\[
x(x+3)=40
\]

\[
x^2+3x-40=0
\]

\[
(x+8)(x-5)=0
\]

\[
x=-8\quad\text{or}\quad x=5.
\]

Since \(x>0\):

\[
x=5.
\]

### Area formula with an obtuse angle

\[
\frac12\times5\times6\times\sin\theta=10
\]

\[
15\sin\theta=10
\]

\[
\sin\theta=\frac{2}{3}
\]

\[
\theta=\sin^{-1}\left(\frac23\right)=41.8^\circ.
\]

Given \(\theta\) is obtuse:

\[
\theta=180^\circ-41.8^\circ=138.2^\circ.
\]

---

## 8. Sine Rule Twice

When two sides and one angle are known, but the missing side is not opposite the known angle, sine rule twice may be cleaner than cosine rule.

\[
\frac{\sin A}{4}=\frac{\sin32^\circ}{3}
\]

\[
\sin A=\frac{4\sin32^\circ}{3}
\]

\[
A=44.9556^\circ.
\]

Remaining angle:

\[
180^\circ-32^\circ-44.9556^\circ=103.0444^\circ.
\]

Use sine rule again:

\[
\frac{x}{\sin103.0444^\circ}=\frac{3}{\sin32^\circ}
\]

\[
x=\frac{3\sin103.0444^\circ}{\sin32^\circ}=5.52\quad\text{to 3 significant figures.}
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosTIKZ-009 | Source: P1-Chp9-TrigonometricRatios.pdf pp.23-24 | Insert from tikz/AS1TrigonometricRatiosTIKZ-009.tex | Purpose: Show the sine-rule-twice situation.]

---

## 9. Multi-Step Problem Solving with Sine and Cosine Rule

The supplied evidence gives a mobile phone mast context. The method is:

1. Use cosine rule in \(\triangle BCD\) to find \(BD\):

\[
BD^2=75^2+80^2-2\times75\times80\cos55^\circ.
\]

\[
BD=71.708\ldots
\]

2. Use sine rule to find \(\angle BDC\):

\[
\frac{\sin\angle BDC}{75}=\frac{\sin55^\circ}{71.708\ldots}
\]

\[
\angle BDC=58.954^\circ.
\]

3. Find:

\[
\angle BDA=140^\circ-58.954^\circ=81.045\ldots^\circ.
\]

4. Use cosine rule in \(\triangle ABD\):

\[
AB^2=70^2+71.708^2-2\times70\times71.708\cos81.045^\circ.
\]

\[
AB=92.1\text{ m}\quad\text{to 3 significant figures.}
\]

5. The evidence gives:

\[
\angle BAD=50.3^\circ
\]

and:

\[
\text{Area }ABCD=4940\text{ m}^2\quad\text{to 3 significant figures.}
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-008 | Source: P1-Chp9-TrigonometricRatios.pdf p.27 | Insert from svg/AS1TrigonometricRatiosSVG-008.svg | Purpose: Four-mast problem diagram showing triangles \(BCD\) and \(ABD\).]

---

## 10. Sine, Cosine and Tangent Graphs

### Sine graph

The graph of \(y=\sin x\):

- repeats every \(360^\circ\);
- has maximum value \(1\);
- has minimum value \(-1\);
- has roots at \(0^\circ,180^\circ,360^\circ,\ldots\);
- has range \(-1\leq\sin x\leq1\).

If \(\sin30^\circ=0.5\), then:

\[
\sin150^\circ=0.5,\quad \sin(-30^\circ)=-0.5,\quad \sin210^\circ=-0.5.
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-009 | Source: P1-Chp9-TrigonometricRatios.pdf pp.31-32 | Insert from svg/AS1TrigonometricRatiosSVG-009.svg | Purpose: Sine graph from \(-360^\circ\) to \(360^\circ\) with symmetry values labelled.]

### Cosine graph

The graph of \(y=\cos x\):

- repeats every \(360^\circ\);
- has maximum value \(1\);
- has minimum value \(-1\);
- starts at \(1\) when \(x=0^\circ\);
- has range \(-1\leq\cos x\leq1\).

If \(\cos60^\circ=0.5\), then:

\[
\cos120^\circ=-0.5,
\quad \cos(-60^\circ)=0.5,
\quad \cos240^\circ=-0.5.
\]

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-010 | Source: P1-Chp9-TrigonometricRatios.pdf pp.33-34 | Insert from svg/AS1TrigonometricRatiosSVG-010.svg | Purpose: Cosine graph from \(-360^\circ\) to \(360^\circ\) with symmetry values labelled.]

### Tangent graph

The graph of \(y=\tan x\):

- repeats every \(180^\circ\);
- has roots at \(0^\circ,180^\circ,-180^\circ,\ldots\);
- has range \(\tan x\in\mathbb R\);
- has asymptotes at \(x=\pm90^\circ,\pm270^\circ,\ldots\).

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-011 | Source: P1-Chp9-TrigonometricRatios.pdf pp.35-36 | Insert from svg/AS1TrigonometricRatiosSVG-011.svg | Purpose: Tangent graph showing roots, period and vertical asymptotes.]

---

## 11. Transforming Trigonometric Graphs

The evidence says to use graph transformation knowledge and decide whether the transformation is inside or outside the function.

### \(y=4\sin x\)

The output values are multiplied by \(4\). The maximum becomes \(4\), the minimum becomes \(-4\), and the period stays \(360^\circ\).

### \(y=\cos(x+45^\circ)\)

The transcript clarifies that the intended example is:

\[
y=\cos(x+45^\circ)
\]

not:

\[
y=\cos x+45^\circ.
\]

The graph shifts \(45^\circ\) left.

### \(y=-\tan x\)

The graph reflects in the \(x\)-axis. Roots and asymptotes stay at the same \(x\)-values.

### \(y=\sin\left(\frac{x}{2}\right)\)

The graph stretches horizontally by scale factor \(2\). Its period becomes \(720^\circ\).

[VISUAL PLACEHOLDER: AS1TrigonometricRatiosSVG-012 | Source: P1-Chp9-TrigonometricRatios.pdf pp.37-38 + transcript clarification | Insert from svg/AS1TrigonometricRatiosSVG-012.svg | Purpose: Four trig transformation sketches.]

[INTERACTIVE PLACEHOLDER: AS1TrigonometricRatiosWidget-003 | Source: P1-Chp9-TrigonometricRatios.pdf pp.31-38 | Insert from widgets/AS1TrigonometricRatiosWidget-003.html | Purpose: Interactive trig graph transformer.]

---

## Guided Practice

1. A triangle has sides \(8\), \(3\), and \(10\). The angle \(\theta\) is opposite the side of length \(10\). Find \(\theta\).
2. A triangle has two sides \(6\) and \(5\), with included angle \(70^\circ\). Find the third side \(x\).
3. A triangle has an angle of \(20^\circ\), opposite side \(5\), and another side \(10\) opposite angle \(\theta\). Given \(\theta\) is obtuse, find \(\theta\).
4. The area of a triangle is \(10\). Two sides are \(x\) and \(x+3\), with included angle \(30^\circ\). Find \(x\).
5. Sketch \(y=\sin x\) for \(0^\circ\leq x\leq360^\circ\). Label roots, maximum and minimum.
6. Sketch \(y=-\tan x\) for \(0^\circ\leq x\leq360^\circ\). Label roots and asymptotes.

---

## Common Mistakes and Exam Traps

1. Using SOHCAHTOA on a non-right-angled triangle.
2. Forgetting to square root after calculating \(a^2\) with cosine rule.
3. Simplifying the cosine rule incorrectly through BIDMAS errors.
4. Ignoring the second sine-rule angle \(180^\circ-\theta\).
5. Using the wrong included angle in \(\frac12ab\sin C\).
6. Treating \(\cos(x+45^\circ)\) as \(\cos x+45^\circ\).
7. Drawing tangent graphs without vertical asymptotes.

---

## Exam Technique Notes

1. Mark opposite pairs before using sine rule.
2. For cosine rule, label the target angle \(A\) and the opposite side \(a\).
3. For missing angles with sine rule, ask whether an obtuse answer is possible.
4. For area, find the included angle.
5. Redraw messy context diagrams.
6. Keep calculator accuracy until the final answer.
7. Use graph symmetry to prepare for trig equations.

---

## Full Worked Solutions to Guided Practice

### Solution 1

\[
10^2=8^2+3^2-2\times8\times3\cos\theta
\]

\[
100=73-48\cos\theta
\]

\[
48\cos\theta=73-100=-27
\]

\[
\cos\theta=-\frac{27}{48}
\]

\[
\theta=\cos^{-1}\left(-\frac{27}{48}\right)=124.2^\circ.
\]

### Solution 2

\[
x^2=6^2+5^2-2\times6\times5\cos70^\circ
\]

\[
x^2=61-60\cos70^\circ
\]

\[
x=\sqrt{61-60\cos70^\circ}=6.36.
\]

### Solution 3

\[
\frac{\sin\theta}{10}=\frac{\sin20^\circ}{5}
\]

\[
\theta=\sin^{-1}\left(\frac{10\sin20^\circ}{5}\right)=43.1602^\circ.
\]

Since \(\theta\) is obtuse:

\[
\theta=180^\circ-43.1602^\circ=136.8398^\circ=136.8^\circ.
\]

### Solution 4

\[
\frac12x(x+3)\sin30^\circ=10
\]

\[
\frac14x(x+3)=10
\]

\[
x^2+3x-40=0
\]

\[
(x+8)(x-5)=0
\]

\[
x=5.
\]

### Solution 5

Key points for \(y=\sin x\):

\[
(0^\circ,0),\;(90^\circ,1),\;(180^\circ,0),\;(270^\circ,-1),\;(360^\circ,0).
\]

### Solution 6

For \(y=-\tan x\), roots are:

\[
0^\circ,\;180^\circ,\;360^\circ.
\]

Asymptotes are:

\[
x=90^\circ,\quad x=270^\circ.
\]

---

## Syllabus Gap Check

| LO ID | Status | Comment |
|---|---|---|
| AS1-TRIG-LO001 | Covered | Sine, cosine, tangent definitions and graph behaviour covered. |
| AS1-TRIG-LO002 | Covered | Sine rule, cosine rule and ambiguous case covered. |
| AS1-TRIG-LO003 | Covered | \(\frac12ab\sin C\) covered. |
| AS1-TRIG-LO004 | Covered | Sine/cos/tan graphs and simple transformations covered. |
| AS1-TRIG-LO005 | Not covered | \(\tan\theta=\frac{\sin\theta}{\cos\theta}\) belongs in a trig identities lesson. |
| AS1-TRIG-LO006 | Not covered | \(\sin^2\theta+\cos^2\theta=1\) belongs in a trig identities lesson. |
| AS1-TRIG-LO007 | Partially prepared | Graph symmetry and ambiguous sine case prepare for trig equations. |

---

## Supplementary Sources Used

The DrFrost/Pearson material is treated as cross-board lesson evidence. It is used only where the CCEA specification confirms the content is on-spec.

Excluded or enrichment-only content:

- DrFrost site/practice registration slide;
- Edexcel practice references as CCEA evidence;
- MAT/STEP/AEA questions;
- tetrahedron/FM extension.

---

## Final Student Checklist

- [ ] I can define sine, cosine and tangent as ratios/functions.
- [ ] I can choose sine rule from opposite angle-side pairs.
- [ ] I can choose cosine rule when three sides are involved.
- [ ] I can use cosine rule for missing sides and angles.
- [ ] I can use sine rule for missing sides and angles.
- [ ] I can recognise and handle the ambiguous sine-rule case.
- [ ] I can use \(\frac12ab\sin C\) and identify the included angle.
- [ ] I can sketch \(y=\sin x\), \(y=\cos x\), and \(y=\tan x\).
- [ ] I can state periods, ranges, roots and asymptotes.
- [ ] I can transform simple trig graphs.
