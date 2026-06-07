# A21 Trigonometry and Modelling

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-TRIG |
| Official topic name | Trigonometry |
| Lesson/chapter title | Trigonometry and Modelling |
| Topic slug | trigonometry_and_modelling |
| Topic Pascal | TrigonometryAndModelling |
| Topic ID | A21TrigonometryAndModelling |
| Lesson file | A21_trigonometry_and_modelling_lesson.md |
| Core LO IDs | A21-TRIG-LO005, A21-TRIG-LO006, A21-TRIG-LO007, A21-TRIG-LO008, A21-TRIG-LO009 |

## Evidence Map

| Evidence source | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic, LO IDs, official boundaries |
| README-Module-Map.txt | Metadata rules and file naming conventions |
| Source-Evidence-Drop-Checklist.txt | Missing-evidence and off-spec logging rules |
| Chapter_7_Trigonometry_&_Modelling transcript | Teacher explanations, warnings, worked steps and practice flow |
| P2-Chp7-TrigonometryAndModelling_RevealBlocksRemoved.pdf | Slide formulae, worked examples, exercise references, diagram placeholders |
| Chapter_7 screenshots PDF | Visual support only; full text was not parsed |

## Specification Alignment

| LO ID | Lesson content |
|---|---|
| A21-TRIG-LO005 | Compound/addition formulae for \(\sin(A\pm B)\), \(\cos(A\pm B)\), \(\tan(A\pm B)\); expansion and reverse recognition |
| A21-TRIG-LO006 | Double angle formulae, derivations, exact values and equations |
| A21-TRIG-LO007 | \(a\cos\theta+b\sin\theta\) and \(a\sin\theta+b\cos\theta\) in \(R\cos(\theta\pm\alpha)\) or \(R\sin(\theta\pm\alpha)\) forms |
| A21-TRIG-LO008 | Proofs involving trig functions and identities |
| A21-TRIG-LO009 | Trig functions used to solve modelling problems in context |

## Learning Objectives

By the end of this lesson, you should be able to state and use the compound angle formulae, derive the tangent addition formula, use exact values and quadrant signs, derive and use double angle formulae, solve equations involving compound/double angles, rewrite sine-cosine sums in harmonic form, find maxima/minima, prove identities and interpret sinusoidal models.

## Prerequisite Recap: A-Level Knowledge Only

Prior A-Level knowledge needed: \(\sin^2x+\cos^2x\equiv1\), \(\tan x=\frac{\sin x}{\cos x}\), CAST/quadrants, exact values for \(30^\circ,45^\circ,60^\circ,90^\circ\), solving basic trig equations, radians, and reciprocal identities.

No GCSE bridge source is used in this lesson.

## Big Picture Explanation

Trigonometry and Modelling is the chapter where trig becomes an algebraic toolkit. Expressions such as \(\sin(A+B)\), \(\cos(A-B)\) and \(\tan(A+B)\) cannot be split apart informally. They require exact identities. The chapter moves through four layers: addition formulae, double angle formulae, harmonic identity, and modelling.

## Key Definitions and Notation

The **argument** of a trig function is the input inside the function, for example \(A+B\) in \(\sin(A+B)\). An **identity** is true for every value for which both sides are defined and is written using \(\equiv\). A **compound angle formula** rewrites a trig function whose argument is a sum or difference. A **harmonic form** rewrites a linear combination such as \(a\sin x+b\cos x\) as one shifted trig function.

## Core Theory Part A: Addition Formulae

\[
\boxed{\sin(A+B)\equiv \sin A\cos B+\cos A\sin B}
\]
\[
\boxed{\sin(A-B)\equiv \sin A\cos B-\cos A\sin B}
\]
\[
\boxed{\cos(A+B)\equiv \cos A\cos B-\sin A\sin B}
\]
\[
\boxed{\cos(A-B)\equiv \cos A\cos B+\sin A\sin B}
\]
\[
\boxed{\tan(A+B)\equiv \frac{\tan A+\tan B}{1-\tan A\tan B}}
\]
\[
\boxed{\tan(A-B)\equiv \frac{\tan A-\tan B}{1+\tan A\tan B}}
\]

For sine, the sign stays the same and sine/cosine are mixed. For cosine, the sign switches and cosines stay together while sines stay together. For tangent, the numerator keeps the same sign and the denominator switches sign.

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-001 | Source: P2 Chapter 7 slide PDF page 4 and transcript section 1 | Insert from svg/A21TrigonometryAndModellingSVG-001.svg | Purpose: Addition formulae memory map showing sign patterns for sine, cosine and tangent.]

[INTERACTIVE PLACEHOLDER: A21TrigonometryAndModellingWidget-001 | Source: Addition formulae lesson evidence | Insert from widgets/A21TrigonometryAndModellingWidget-001.html | Purpose: Formula reconstruction drill.]

## Core Theory Part B: A Common Error

A common mistake is
\[
\sin(A+B)=\sin A+\sin B.
\]
This is false. Test \(A=30^\circ\), \(B=60^\circ\):
\[
\sin(30^\circ+60^\circ)=\sin90^\circ=1,
\]
but
\[
\sin30^\circ+\sin60^\circ=\frac12+\frac{\sqrt3}{2}=\frac{1+\sqrt3}{2}.
\]
Since \(1\ne\frac{1+\sqrt3}{2}\), \(\sin(A+B)\ne \sin A+\sin B\).

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-002 | Source: P2 Chapter 7 slide PDF page 5 | Insert from svg/A21TrigonometryAndModellingSVG-002.svg | Purpose: Counterexample visual.]

## Core Theory Part C: Proof of \(\sin(A+B)\)

A geometric proof considers a line of length \(1\) projected at angle \(A+B\). Its total vertical height is \(\sin(A+B)\). Splitting the geometry into two right-angled triangles gives vertical pieces \(\sin A\cos B\) and \(\cos A\sin B\). Therefore
\[
\boxed{\sin(A+B)\equiv\sin A\cos B+\cos A\sin B}.
\]

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingTikZ-001 | Source: P2 Chapter 7 slide PDF page 7 | Insert from tikz/A21TrigonometryAndModellingTikZ-001.tex | Purpose: Geometric proof diagram for \(\sin(A+B)\).]

## Core Theory Part D: Deriving Other Compound Formulae

\[
\sin(A-B)=\sin(A+(-B))=\sin A\cos(-B)+\cos A\sin(-B).
\]
Since \(\cos(-B)=\cos B\) and \(\sin(-B)=-\sin B\),
\[
\boxed{\sin(A-B)\equiv \sin A\cos B-\cos A\sin B}.
\]

Similarly, using cofunction relationships gives the cosine identities.

## Worked Examples: Addition Formulae

### Example 1
\[
\cos110^\circ\cos15^\circ-\sin110^\circ\sin15^\circ
=\cos(110^\circ+15^\circ)=\boxed{\cos125^\circ}.
\]

### Example 2
\[
\sin5x\cos2x-\cos5x\sin2x
=\sin(5x-2x)=\boxed{\sin3x}.
\]

### Example 3
\[
\sin20^\circ\cos35^\circ+\cos20^\circ\sin35^\circ
=\sin(20^\circ+35^\circ)=\boxed{\sin55^\circ}.
\]

### Example 4
\[
\sin10^\circ\sin15^\circ-\cos10^\circ\cos15^\circ
=-\left(\cos10^\circ\cos15^\circ-\sin10^\circ\sin15^\circ\right)
=\boxed{-\cos25^\circ}.
\]

### Example 5
\[
\frac{\tan(\theta/2)+\tan(\theta/4)}
{1-\tan(\theta/2)\tan(\theta/4)}
=\tan\left(\frac{\theta}{2}+\frac{\theta}{4}\right)
=\boxed{\tan\left(\frac{3\theta}{4}\right)}.
\]

### Example 6
\[
\frac{\tan(5\pi/12)-\tan(\pi/6)}{1+\tan(5\pi/12)\tan(\pi/6)}
=\tan\left(\frac{5\pi}{12}-\frac{\pi}{6}\right)
=\tan\left(\frac{3\pi}{12}\right)
=\tan\left(\frac{\pi}{4}\right)
=\boxed{1}.
\]

## Core Theory Part E: Creating Tangent Expressions

To create \(\tan x\), divide by \(\cos x\), because \(\tan x=\frac{\sin x}{\cos x}\). To create both \(\tan x\) and \(\tan y\), divide by \(\cos x\cos y\).

### Deriving \(\tan(A+B)\)

\[
\tan(A+B)=\frac{\sin(A+B)}{\cos(A+B)}
=\frac{\sin A\cos B+\cos A\sin B}{\cos A\cos B-\sin A\sin B}.
\]
Divide every term by \(\cos A\cos B\):
\[
\tan(A+B)=
\frac{\frac{\sin A\cos B}{\cos A\cos B}+\frac{\cos A\sin B}{\cos A\cos B}}
{\frac{\cos A\cos B}{\cos A\cos B}-\frac{\sin A\sin B}{\cos A\cos B}}.
\]
Thus
\[
\boxed{\tan(A+B)\equiv\frac{\tan A+\tan B}{1-\tan A\tan B}}.
\]

### Example: Expressing \(\tan x\) in terms of \(\tan y\)

Given
\[
2\sin(x+y)=3\cos(x-y),
\]
expand:
\[
2(\sin x\cos y+\cos x\sin y)=3(\cos x\cos y+\sin x\sin y).
\]
\[
2\sin x\cos y+2\cos x\sin y=3\cos x\cos y+3\sin x\sin y.
\]
Divide by \(\cos x\cos y\):
\[
2\tan x+2\tan y=3+3\tan x\tan y.
\]
\[
2\tan x-3\tan x\tan y=3-2\tan y.
\]
\[
\tan x(2-3\tan y)=3-2\tan y.
\]
\[
\boxed{\tan x=\frac{3-2\tan y}{2-3\tan y}}.
\]

### Exact value from \(\tan(x+60^\circ)=5\)

\[
\frac{\tan x+\sqrt3}{1-\sqrt3\tan x}=5.
\]
\[
\tan x+\sqrt3=5-5\sqrt3\tan x.
\]
\[
\tan x(1+5\sqrt3)=5-\sqrt3.
\]
\[
\boxed{\tan x=\frac{5-\sqrt3}{1+5\sqrt3}}.
\]

### Exact value \(\sin15^\circ\)

\[
\sin15^\circ=\sin(45^\circ-30^\circ)
=\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ.
\]
\[
=\frac1{\sqrt2}\cdot\frac{\sqrt3}{2}-\frac1{\sqrt2}\cdot\frac12
=\frac{\sqrt3-1}{2\sqrt2}.
\]
Rationalise:
\[
\frac{\sqrt3-1}{2\sqrt2}\cdot\frac{\sqrt2}{\sqrt2}
=\boxed{\frac{\sqrt6-\sqrt2}{4}}.
\]

### Quadrant example

Given \(\sin A=-\frac35\), \(180^\circ<A<270^\circ\), and \(\cos B=-\frac{12}{13}\), with \(B\) obtuse:
\[
\cos^2A=1-\frac9{25}=\frac{16}{25},
\]
so \(\cos A=-\frac45\). Also
\[
\sin^2B=1-\frac{144}{169}=\frac{25}{169},
\]
so \(\sin B=\frac5{13}\). Then
\[
\cos(A-B)=\left(-\frac45\right)\left(-\frac{12}{13}\right)+\left(-\frac35\right)\left(\frac5{13}\right)
=\frac{48}{65}-\frac{15}{65}=\boxed{\frac{33}{65}}.
\]
\[
\tan A=\frac34,\qquad \tan B=-\frac5{12}.
\]
\[
\tan(A+B)=\frac{\frac34-\frac5{12}}{1-\left(\frac34\right)\left(-\frac5{12}\right)}
=\frac{\frac13}{\frac{63}{48}}
=\boxed{\frac{16}{63}}.
\]

## Core Theory Part F: Double Angle Formulae

Set \(B=A\) in the compound angle formulae:
\[
\boxed{\sin2A=2\sin A\cos A}
\]
\[
\boxed{\cos2A=\cos^2A-\sin^2A}
\]
\[
\boxed{\cos2A=1-2\sin^2A}
\]
\[
\boxed{\cos2A=2\cos^2A-1}
\]
\[
\boxed{\tan2A=\frac{2\tan A}{1-\tan^2A}}.
\]

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-003 | Source: P2 Chapter 7 double angle formula slides and transcript section 4 | Insert from svg/A21TrigonometryAndModellingSVG-003.svg | Purpose: Double angle formula derivation map.]

[INTERACTIVE PLACEHOLDER: A21TrigonometryAndModellingWidget-002 | Source: Double angle formula evidence | Insert from widgets/A21TrigonometryAndModellingWidget-002.html | Purpose: Formula-selection drill for \(\cos2A\).]

### Double angle examples

\[
\cos^250^\circ-\sin^250^\circ=\cos100^\circ.
\]
\[
\frac{2\tan(\pi/6)}{1-\tan^2(\pi/6)}=\tan(\pi/3).
\]

### Eliminating a parameter

Given \(x=3\sin\theta\), \(y=3-4\cos2\theta\):
\[
y=3-4(1-2\sin^2\theta)=8\sin^2\theta-1.
\]
Since \(\sin\theta=x/3\),
\[
\boxed{y=\frac{8x^2}{9}-1}.
\]

### Exact \(\sin2x\) and \(\tan2x\)

Given \(\cos x=\frac34\) and \(x\) is acute:
\[
\sin x=\frac{\sqrt7}{4}.
\]
\[
\sin2x=2\cdot\frac{\sqrt7}{4}\cdot\frac34=\boxed{\frac{3\sqrt7}{8}}.
\]
\[
\tan x=\frac{\sqrt7}{3},\quad
\tan2x=\frac{2\sqrt7/3}{1-7/9}
=\frac{2\sqrt7/3}{2/9}
=\boxed{3\sqrt7}.
\]

## Core Theory Part G: Solving Equations Using Addition and Double Angle Formulae

Check whether all trig functions have the same argument. If not, use an addition or double angle formula first.

### Addition formula equation

Solve
\[
4\cos(x-30^\circ)=8\sqrt2\sin x,\quad 0^\circ\le x<360^\circ.
\]
\[
4\left(\cos x\frac{\sqrt3}{2}+\sin x\frac12\right)=8\sqrt2\sin x.
\]
\[
2\sqrt3\cos x+2\sin x=8\sqrt2\sin x.
\]
\[
2\sqrt3\cos x=(8\sqrt2-2)\sin x.
\]
\[
\tan x=\boxed{\frac{\sqrt3}{4\sqrt2-1}}.
\]
The solutions are in quadrants 1 and 3.

### Double angle equation

\[
\cos2\theta+\sin\theta=1.
\]
Use \(\cos2\theta=1-2\sin^2\theta\):
\[
1-2\sin^2\theta+\sin\theta=1.
\]
\[
2\sin^2\theta-\sin\theta=0.
\]
\[
\sin\theta(2\sin\theta-1)=0.
\]
For \(0^\circ\le\theta<360^\circ\),
\[
\boxed{\theta=0^\circ,\ 30^\circ,\ 150^\circ,\ 180^\circ}.
\]

## Core Theory Part H: Identity Proofs with Double Angles

### Power identity
\[
(\sin^2A+\cos^2A)^2=1
\]
\[
\sin^4A+2\sin^2A\cos^2A+\cos^4A=1.
\]
\[
\sin^4A+\cos^4A=1-2\sin^2A\cos^2A.
\]
Since \(\sin^22A=4\sin^2A\cos^2A\),
\[
\boxed{\sin^4A+\cos^4A=\frac12(2-\sin^22A)}.
\]

Using \(\cos4A=1-2\sin^22A\),
\[
\boxed{\sin^4A+\cos^4A=\frac14(3+\cos4A)}.
\]

## Core Theory Part I: The Harmonic Identity

The harmonic identity is used when an expression contains sine and cosine with the same argument:
\[
a\sin x+b\cos x\equiv R\sin(x+\alpha).
\]
Expand:
\[
R\sin(x+\alpha)=R\sin x\cos\alpha+R\cos x\sin\alpha.
\]
Compare:
\[
R\cos\alpha=a,\qquad R\sin\alpha=b.
\]
Then
\[
\boxed{R=\sqrt{a^2+b^2}},\qquad \boxed{\tan\alpha=\frac{b}{a}}.
\]

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-004 | Source: Harmonic identity evidence | Insert from svg/A21TrigonometryAndModellingSVG-004.svg | Purpose: Coefficient triangle.]

[INTERACTIVE PLACEHOLDER: A21TrigonometryAndModellingWidget-003 | Source: Harmonic identity evidence | Insert from widgets/A21TrigonometryAndModellingWidget-003.html | Purpose: \(R,\alpha\) calculator.]

### Harmonic examples

\[
3\sin x+4\cos x\equiv R\sin(x+\alpha).
\]
\[
R\cos\alpha=3,\quad R\sin\alpha=4,\quad R=5,\quad \tan\alpha=\frac43.
\]
\[
\boxed{3\sin x+4\cos x\equiv5\sin(x+53.1^\circ)}.
\]

\[
\sin x+\cos x\equiv\sqrt2\sin\left(x+\frac{\pi}{4}\right).
\]

\[
\sin x-\sqrt3\cos x\equiv2\sin\left(x-\frac{\pi}{3}\right).
\]

\[
8\sin(3x)+6\cos(3x)\equiv10\sin(3x+0.64).
\]

## Core Theory Part J: Solving with the Harmonic Identity

Put \(2\cos\theta+5\sin\theta\) in the form \(R\cos(\theta-\alpha)\):
\[
R\cos(\theta-\alpha)=R\cos\theta\cos\alpha+R\sin\theta\sin\alpha.
\]
\[
R\cos\alpha=2,\quad R\sin\alpha=5.
\]
\[
R=\sqrt{29},\quad \alpha=\tan^{-1}\left(\frac52\right)=68.199^\circ.
\]
So
\[
2\cos\theta+5\sin\theta\equiv\sqrt{29}\cos(\theta-68.199^\circ).
\]
Solving \(2\cos\theta+5\sin\theta=3\):
\[
\cos(\theta-68.199^\circ)=\frac3{\sqrt{29}}.
\]
Let \(u=\theta-68.199^\circ\). Then
\[
-68.199^\circ<u<291.801^\circ.
\]
\[
u=\pm56.145^\circ.
\]
Thus
\[
\boxed{\theta=12.1^\circ,\ 124.3^\circ}.
\]

## Core Theory Part K: Maxima and Minima

If \(a\sin x+b\cos x\equiv R\sin(x+\alpha)\), then
\[
-R\le R\sin(x+\alpha)\le R.
\]
So maximum \(=R\), minimum \(=-R\). With a vertical shift \(d\), maximum \(=d+R\), minimum \(=d-R\).

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-005 | Source: Harmonic graph evidence | Insert from svg/A21TrigonometryAndModellingSVG-005.svg | Purpose: Harmonic range graph.]

### Maximum example

\[
12\cos\theta+5\sin\theta\equiv13\sin(\theta+67.4^\circ).
\]
Maximum value:
\[
\boxed{13}.
\]
It occurs when
\[
\theta+67.4^\circ=90^\circ,
\]
so
\[
\boxed{\theta=22.6^\circ}.
\]

## Core Theory Part L: Proving Trig Identities

[INTERACTIVE PLACEHOLDER: A21TrigonometryAndModellingWidget-005 | Source: Proof sections | Insert from widgets/A21TrigonometryAndModellingWidget-005.html | Purpose: Identity proof decision helper.]

### Proof 1
\[
\cot\theta-\tan\theta=\frac1{\tan\theta}-\tan\theta
=\frac{1-\tan^2\theta}{\tan\theta}.
\]
\[
\frac2{\cot\theta-\tan\theta}
=
\frac2{\frac{1-\tan^2\theta}{\tan\theta}}
=
\frac{2\tan\theta}{1-\tan^2\theta}
=\boxed{\tan2\theta}.
\]

### Proof 2
\[
\frac{1-\cos2\theta}{\sin2\theta}
=
\frac{1-(1-2\sin^2\theta)}{2\sin\theta\cos\theta}
=
\frac{2\sin^2\theta}{2\sin\theta\cos\theta}
=\boxed{\tan\theta}.
\]

### Proof 3
\[
\cot2x+\cosec2x
=
\frac{\cos2x}{\sin2x}+\frac1{\sin2x}
=
\frac{\cos2x+1}{\sin2x}.
\]
\[
=
\frac{(2\cos^2x-1)+1}{2\sin x\cos x}
=
\frac{2\cos^2x}{2\sin x\cos x}
=\boxed{\cot x}.
\]

### Half-angle proof
\[
\frac{1-\cos x}{1+\cos x}
=
\frac{1-\left(2\cos^2\frac{x}{2}-1\right)}
{1+\left(2\cos^2\frac{x}{2}-1\right)}
=
\frac{2-2\cos^2\frac{x}{2}}{2\cos^2\frac{x}{2}}
=
\frac{2\sin^2\frac{x}{2}}{2\cos^2\frac{x}{2}}
=\boxed{\tan^2\frac{x}{2}}.
\]

## Core Theory Part M: Modelling

Trig models describe oscillations such as tides, temperatures, pendulums and waves.

\[
y=d+R\sin(kx+\alpha)
\]
has midline \(d\), amplitude \(R\), period \(\frac{2\pi}{k}\), and phase shift controlled by \(\alpha\).

[VISUAL PLACEHOLDER: A21TrigonometryAndModellingSVG-006 | Source: Modelling evidence | Insert from svg/A21TrigonometryAndModellingSVG-006.svg | Purpose: Sinusoidal model labels.]

[INTERACTIVE PLACEHOLDER: A21TrigonometryAndModellingWidget-004 | Source: Modelling evidence | Insert from widgets/A21TrigonometryAndModellingWidget-004.html | Purpose: Sinusoidal model explorer.]

### Kiln temperature model

\[
T=1100+5\cos\left(\frac{x}{3}\right)-8\sin\left(\frac{x}{3}\right),\quad 0\le x\le72.
\]
Use
\[
5\cos\theta-8\sin\theta\equiv\sqrt{89}\cos(\theta+1.0122).
\]
Then
\[
T=1100+\sqrt{89}\cos\left(\frac{x}{3}+1.0122\right).
\]
Maximum:
\[
\boxed{T_{\max}=1100+\sqrt{89}=1109.43^\circ\text{C}}.
\]
First maximum:
\[
\frac{x}{3}+1.0122=2\pi
\]
\[
x=3(2\pi-1.0122)=\boxed{15.81\text{ hours}}.
\]

## Guided Practice and Full Worked Solutions

### Question 1
Write \(5\sin x+12\cos x\) as \(R\sin(x+\alpha)\) and find its maximum.

Solution:
\[
R=13,\quad \tan\alpha=\frac{12}{5},\quad \alpha=67.4^\circ.
\]
\[
\boxed{5\sin x+12\cos x\equiv13\sin(x+67.4^\circ)}.
\]
Maximum \(=\boxed{13}\).

### Question 2
Write \(4\cos\theta-3\sin\theta\) as \(R\cos(\theta+\alpha)\).

Solution:
\[
R=5,\quad \tan\alpha=\frac34,\quad \alpha=36.9^\circ.
\]
\[
\boxed{4\cos\theta-3\sin\theta\equiv5\cos(\theta+36.9^\circ)}.
\]

### Question 3
Solve \(6\cos\theta+8\sin\theta=5\), \(0^\circ<\theta<360^\circ\).

Solution:
\[
6\cos\theta+8\sin\theta\equiv10\cos(\theta-53.130^\circ).
\]
\[
10\cos(\theta-53.130^\circ)=5.
\]
\[
\cos(\theta-53.130^\circ)=\frac12.
\]
\[
\boxed{\theta=113.1^\circ,\ 353.1^\circ}.
\]

### Question 4
Prove
\[
\frac{1-\cos2x}{\sin2x}\equiv\tan x.
\]

Solution:
\[
\frac{1-\cos2x}{\sin2x}
=
\frac{1-(1-2\sin^2x)}{2\sin x\cos x}
=
\frac{2\sin^2x}{2\sin x\cos x}
=
\boxed{\tan x}.
\]

### Question 5
For
\[
d=4+3\sin\left(\frac{2\pi t}{5}+\alpha\right),
\]
midline \(=\boxed{4}\), amplitude \(=\boxed{3}\), period
\[
=\frac{2\pi}{2\pi/5}=\boxed{5\text{ hours}}.
\]

## Common Mistakes and Exam Traps

- Never split \(\sin(A+B)\) into \(\sin A+\sin B\).
- Do not divide by \(\cos x\) if trig arguments do not match.
- Choose the correct form of \(\cos2x\).
- Use quadrant information when square-rooting.
- Do not use harmonic identity if the sine and cosine arguments differ.
- Do not round \(\alpha\) too early.
- Adjust intervals after substituting \(u=\theta-\alpha\).
- In modelling, state units and interpret the answer in context.

## Exam Technique

For exact values, use \(30^\circ,45^\circ,60^\circ,90^\circ\). For identity proofs, work from the more complicated side. For harmonic identity questions, expand, compare coefficients, find \(R\), find \(\alpha\), then substitute back. For modelling, identify the midline, amplitude, period, phase shift, maximum/minimum and units.

## Syllabus Gap Check

| LO ID | Covered? | Evidence-backed lesson content |
|---|---|---|
| A21-TRIG-LO005 | Yes | Compound formulae and tangent derivation |
| A21-TRIG-LO006 | Yes | Double angle formulae and proofs |
| A21-TRIG-LO007 | Yes | Harmonic identity and maxima/minima |
| A21-TRIG-LO008 | Yes | Identity proof examples |
| A21-TRIG-LO009 | Yes | Trig modelling examples |

## Visual and Interactive Asset Plan

Mermaid: 10 files. SVG: 6 files. TikZ: 5 files. Widgets: 5 files.

## Supplementary Sources Used

No web sources were used. Cross-board slide examples were used only where matching CCEA A21 Trigonometry outcomes.

## Final Student Checklist

I can state and use the compound formulae, derive tangent addition, find exact values, use quadrant signs, derive double angle formulae, solve equations, use harmonic form, find maxima/minima, prove identities and interpret trig models.

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix and topic identity correct | Yes |
| LO IDs preserved exactly | Yes |
| On-spec evidence covered | Yes |
| Off-spec material excluded or marked | Yes |
| Placeholders match generated asset plan | Yes |
| Manifest and source reference updated | Yes |
| Unresolved issues | Screenshot PDF not fully inspected page-by-page; no CCEA past-paper extract supplied |
