# The t-formulae: Tangent Half-Angle Substitution as Optional Further Pure Enrichment

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA21: Further A2 1 Pure Mathematics, nearest available CCEA anchor only |
| Applied section | Pure |
| Topic code | FA21-FCALC, nearest CCEA anchor only |
| Topic name | Further calculus: optional t-formulae boundary enrichment |
| Topic slug | `t_formulae_boundary_enrichment` |
| Topic Pascal | `TFormulaeBoundaryEnrichment` |
| Topic ID | `FA21TFormulaeBoundaryEnrichment` |
| Lesson file name | `FA21_t_formulae_boundary_enrichment_lesson.md` |
| Direct CCEA LO IDs | None found for t-formulae in supplied CCEA Further Maths sources |
| Nearest anchor LO ID | `FA21-FCALC-LO004`, not claimed as covered |
| Related background LO ID | `FA21-CN-LO001`, related only through multiple-angle formulae |
| Boundary status | Boundary-controlled optional Further Pure enrichment |

### Boundary notice

This lesson is built from the supplied FP1 t-formulae PDF, screenshot evidence and transcript. In the available CCEA Further Mathematics project sources, no exact CCEA Further Mathematics learning outcome for “the t-formulae” was found. Therefore the lesson is preserved as **optional Further Pure enrichment**, not as confirmed CCEA core content.

The mathematical heart of the topic is

$$
t=\tan\frac{\theta}{2},\qquad
\sin\theta=\frac{2t}{1+t^2},\qquad
\cos\theta=\frac{1-t^2}{1+t^2},\qquad
\tan\theta=\frac{2t}{1-t^2}.
$$

## 2. Evidence Map

| Evidence source | Type | How used |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | CCEA authority | No exact t-formulae LO found; nearest anchor logged as FA21-FCALC. |
| `Further_Maths_README_module_map.md` | Project map | Used for lesson-pack structure and phase workflow. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence rules | Used for off-spec logging, missing evidence and visual preservation. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary Maths bridge | Used only for bridge context. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary Maths bridge | Used only for ordinary AS/A2 Mathematics background. |
| `FP1-Chp5-tFormulae.pdf` | Lesson-specific evidence | Formulae, derivations, textbook examples, identities, equations and modelling. |
| `transcripts.md` | Lesson-specific transcript | Teacher explanations, warnings, method choices and exact working. |
| `Chapter_5_The_t-formulae_🧩_(Further_Pure_1)_screenshots.pdf` | Visual evidence | Opening graph, chapter menu, memory triangle, alternative proof triangle and formula annotations. |

### Visual evidence limitation

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed. The screenshot PDF is long, so only the visible early derivation pages and relevant evidence-supported diagrams are used in this pack.

## 3. Specification Alignment

| CCEA LO ID | Official relationship | Lesson coverage | Boundary judgement |
|---|---|---|---|
| `FA21-FCALC-LO004` | Nearest anchor: Further Calculus and trigonometric substitution/integration ideas | The lesson supports substitution fluency but does not teach the official specified integration forms as core. | Nearest anchor only. |
| `FA21-CN-LO001` | Related background through multiple-angle formulae | The lesson uses ordinary double-angle formulae but not De Moivre’s theorem. | Related background only. |
| No direct LO found | No exact CCEA t-formulae LO found | t-formulae are taught as enrichment only. | Do not invent LO IDs. |

## 4. Learning Objectives

### Enrichment mathematical objectives

By the end of this lesson, you should be able to:

1. Define $t=\tan(\theta/2)$.
2. Derive $\tan\theta=\dfrac{2t}{1-t^2}$ from the tangent double-angle formula.
3. Use the memory triangle to derive $\sin\theta=\dfrac{2t}{1+t^2}$ and $\cos\theta=\dfrac{1-t^2}{1+t^2}$.
4. Use t-formulae to prove identities.
5. Use t-formulae to solve trigonometric equations by translating into algebraic equations in $t$.
6. Undo the substitution carefully, including half-angle range checks.
7. Understand the optional modelling/differentiation route where differentiating first is usually cleaner than substituting first.

### Boundary objective

You should also be able to explain that this is useful Further Pure enrichment but not confirmed CCEA core content from the supplied CCEA map.

## 5. Explicit Prerequisite Recap

### GCSE and ordinary A-Level foundations

| Prior skill | Why it matters here |
|---|---|
| Pythagoras | Finds the hypotenuse $1+t^2$ from sides $2t$ and $1-t^2$. |
| Algebraic fractions | Required for simplifying t-formula substitutions. |
| Quadratics | Trig equations often become quadratics in $t$. |
| Exact surds | Some examples require exact manipulation such as $\sqrt{12}=2\sqrt3$. |
| $\sin^2\theta+\cos^2\theta=1$ | Used to find missing trig values and signs. |
| Double-angle formulae | The t-formulae grow from double-angle formulae. |
| Trig equation solving | Used after solving for $t$. |
| Radians and degrees | Calculator mode and angle range depend on the unit. |
| Differentiation | Optional modelling examples use $v=ds/dx$. |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS/A2 trigonometry | Exact values, identities, trig graphs and reciprocal functions | Rewrite $\sin\theta$, $\cos\theta$ and $\tan\theta$ as rational functions of $t$ | A wrong quadrant sign corrupts the whole answer. |
| A2 double-angle formulae | $\tan2A=\dfrac{2\tan A}{1-\tan^2A}$ | Put $A=\theta/2$ and set $t=\tan(\theta/2)$ | Match the angle ladder: $\theta/2\to\theta$ or $\theta\to2\theta$. |
| Algebra | Fractions, factorising, quadratics | Trig equations become algebraic equations in $t$ | Clearing denominators can hide excluded values. |
| Trig equations | Inverse trig and ranges | Solve $\tan(\theta/2)=t$ before doubling | Do not report $\theta/2$ as $\theta$. |
| Calculus | Chain rule and stationary points | Optional model differentiates first, then substitutes | $t$ is not time; in the model, $x$ is time. |

In ordinary A-Level Maths, this idea appeared as double-angle trigonometry, trig equation solving and algebraic fractions. In Further Pure enrichment, the same idea becomes a substitution machine: trig is translated into algebra, worked on there, then translated back. The key upgrade is that complicated trig expressions can become rational algebraic expressions in $t$. The danger is that range, sign, denominator and angle-doubling checks still matter.

## 6. Big Picture Explanation

The t-formulae are a trig-to-algebra translator. They take expressions involving $\sin\theta$, $\cos\theta$ and $\tan\theta$ and rewrite them using

$$
t=\tan\frac{\theta}{2}.
$$

Once this is done, a trigonometric equation can become an algebraic equation in $t$. After solving for $t$, the final step is to undo the substitution:

$$
t=\tan\frac{\theta}{2}.
$$

The angle relationship is the hinge. If $t=\tan(\theta/2)$, the formulae give trig functions of $\theta$. If $t=\tan\theta$, the formulae give trig functions of $2\theta$. If $t=\tan x$, the formulae give trig functions of $2x$.

## 7. Key Definitions and Notation

### Main substitution

$$
\boxed{t=\tan\frac{\theta}{2}}
$$

### The three t-formulae

$$
\boxed{\sin\theta=\frac{2t}{1+t^2}},\qquad
\boxed{\cos\theta=\frac{1-t^2}{1+t^2}},\qquad
\boxed{\tan\theta=\frac{2t}{1-t^2}}.
$$

### Reciprocal forms

$$
\cosec\theta=\frac{1+t^2}{2t},\qquad t\ne0.
$$

$$
\sec\theta=\frac{1+t^2}{1-t^2},\qquad t\ne\pm1.
$$

$$
\cot\theta=\frac{1-t^2}{2t},\qquad t\ne0.
$$

### General doubled-angle version

If $t=\tan u$, then

$$
\sin2u=\frac{2t}{1+t^2},\qquad
\cos2u=\frac{1-t^2}{1+t^2},\qquad
\tan2u=\frac{2t}{1-t^2}.
$$

## 8. Core Theory

### 8.1 Deriving $\tan\theta$

Start with the ordinary double-angle formula

$$
\tan2A=\frac{2\tan A}{1-\tan^2A}.
$$

Let

$$
A=\frac{\theta}{2}.
$$

Then

$$
2A=\theta.
$$

So

$$
\tan\theta=\frac{2\tan(\theta/2)}{1-\tan^2(\theta/2)}.
$$

Since

$$
t=\tan\frac{\theta}{2},
$$

we get

$$
\boxed{\tan\theta=\frac{2t}{1-t^2}}.
$$

**Bridge Note:** In ordinary A-Level Maths, the tangent double-angle formula was a formula to use. Here it becomes the generator of a substitution method.

### 8.2 Memory triangle derivation

From

$$
\tan\theta=\frac{2t}{1-t^2},
$$

read

$$
\text{opposite}=2t,\qquad \text{adjacent}=1-t^2.
$$

By Pythagoras,

$$
h^2=(2t)^2+(1-t^2)^2.
$$

Expand:

$$
(2t)^2=4t^2,
$$

$$
(1-t^2)^2=1-2t^2+t^4.
$$

So

$$
h^2=4t^2+1-2t^2+t^4=t^4+2t^2+1.
$$

Recognise the square:

$$
t^4+2t^2+1=(t^2+1)^2.
$$

Therefore

$$
h=1+t^2.
$$

Then

$$
\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}=\frac{2t}{1+t^2},
$$

and

$$
\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}=\frac{1-t^2}{1+t^2}.
$$

The triangle is a powerful memory diagram, but the supplied evidence notes that the triangle proof is naturally an acute-angle picture. For broader validity, use identity-based proofs.

### 8.3 Alternative proof using a half-angle triangle

If

$$
t=\tan\frac{\theta}{2},
$$

build a triangle with angle $\theta/2$, opposite side $t$, adjacent side $1$, and hypotenuse $\sqrt{1+t^2}$. Then

$$
\sin\frac{\theta}{2}=\frac{t}{\sqrt{1+t^2}},
\qquad
\cos\frac{\theta}{2}=\frac{1}{\sqrt{1+t^2}}.
$$

Using

$$
\sin\theta=2\sin\frac{\theta}{2}\cos\frac{\theta}{2},
$$

we get

$$
\sin\theta=2\left(\frac{t}{\sqrt{1+t^2}}\right)\left(\frac{1}{\sqrt{1+t^2}}\right)=\frac{2t}{1+t^2}.
$$

Using

$$
\cos\theta=\cos^2\frac{\theta}{2}-\sin^2\frac{\theta}{2},
$$

we get

$$
\cos\theta=\left(\frac{1}{\sqrt{1+t^2}}\right)^2-\left(\frac{t}{\sqrt{1+t^2}}\right)^2=\frac{1-t^2}{1+t^2}.
$$

Finally,

$$
\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{2t}{1-t^2}.
$$

### 8.4 Solving equations using t-formulae

The method is:

1. Define the substitution.
2. Substitute the t-formulae.
3. Clear denominators, recording restrictions.
4. Solve the algebraic equation in $t$.
5. Undo the substitution.
6. Apply the correct angle range.

Example:

$$
2\sin\theta-3\cos\theta=1.
$$

Let

$$
t=\tan\frac{\theta}{2}.
$$

Then

$$
2\left(\frac{2t}{1+t^2}\right)-3\left(\frac{1-t^2}{1+t^2}\right)=1.
$$

Multiply by $1+t^2$:

$$
4t-3(1-t^2)=1+t^2.
$$

Expand:

$$
4t-3+3t^2=1+t^2.
$$

Move all terms to the left:

$$
2t^2+4t-4=0.
$$

Divide by $2$:

$$
t^2+2t-2=0.
$$

Using the quadratic formula,

$$
t=\frac{-2\pm\sqrt{4+8}}{2}=\frac{-2\pm2\sqrt3}{2}=-1\pm\sqrt3.
$$

So

$$
\tan\frac{\theta}{2}=-1\pm\sqrt3.
$$

If $0\le\theta\le2\pi$, then

$$
0\le\frac{\theta}{2}\le\pi.
$$

Solving in this half-angle range gives

$$
\theta=1.26,\ 3.84
$$

to two decimal places.

### 8.5 Identity proofs

For identity proofs, convert both sides into $t$ and show they match.

Example:

$$
\frac{1+\cosec\theta}{\cot\theta}\equiv\frac{1+\tan(\theta/2)}{1-\tan(\theta/2)}.
$$

Let

$$
t=\tan\frac{\theta}{2}.
$$

Then

$$
\cosec\theta=\frac{1+t^2}{2t},\qquad
\cot\theta=\frac{1-t^2}{2t}.
$$

The RHS becomes

$$
\frac{1+t}{1-t}.
$$

The LHS becomes

$$
\frac{1+\frac{1+t^2}{2t}}{\frac{1-t^2}{2t}}.
$$

Write the numerator as

$$
1+\frac{1+t^2}{2t}=\frac{2t+1+t^2}{2t}.
$$

So

$$
\text{LHS}=\frac{\frac{2t+1+t^2}{2t}}{\frac{1-t^2}{2t}}=\frac{t^2+2t+1}{1-t^2}.
$$

Factorise:

$$
t^2+2t+1=(1+t)^2,
$$

and

$$
1-t^2=(1+t)(1-t).
$$

Therefore

$$
\text{LHS}=\frac{1+t}{1-t}=\text{RHS}.
$$

So the identity is proven.

### 8.6 Optional modelling and differentiation

The supplied enrichment evidence includes the displacement model

$$
s=\sin4x+2\sin2x+2.
$$

Velocity is

$$
v=\frac{ds}{dx}=4\cos4x+4\cos2x.
$$

With

$$
t=\tan x,
$$

the t-formulae give

$$
\sin2x=\frac{2t}{1+t^2},\qquad
\cos2x=\frac{1-t^2}{1+t^2}.
$$

Also

$$
\cos4x=\cos^22x-\sin^22x.
$$

So

$$
\cos4x=\left(\frac{1-t^2}{1+t^2}\right)^2-\left(\frac{2t}{1+t^2}\right)^2.
$$

Substitute into $v$:

$$
v=4\left(\frac{(1-t^2)^2-4t^2}{(1+t^2)^2}\right)+4\left(\frac{1-t^2}{1+t^2}\right).
$$

Use the common denominator $(1+t^2)^2$:

$$
v=\frac{4((1-t^2)^2-4t^2)+4(1-t^2)(1+t^2)}{(1+t^2)^2}.
$$

Expand:

$$
(1-t^2)^2-4t^2=1-6t^2+t^4,
$$

and

$$
(1-t^2)(1+t^2)=1-t^4.
$$

Therefore the numerator is

$$
4(1-6t^2+t^4)+4(1-t^4)=8-24t^2=8(1-3t^2).
$$

Hence

$$
\boxed{v=\frac{8}{(1+t^2)^2}(1-3t^2)}.
$$

Stationary points satisfy

$$
1-3t^2=0,
$$

so

$$
t=\pm\frac1{\sqrt3}.
$$

Since $t=\tan x$ and $0\le x\le\pi$,

$$
x=\frac{\pi}{6},\frac{5\pi}{6}.
$$

The supplied evidence identifies the maximum at

$$
x=\frac{\pi}{6}.
$$

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentSVG-005 | Source: Screenshot PDF page 1 visual evidence | Insert from svg/FA21TFormulaeBoundaryEnrichmentSVG-005.svg | Purpose: Show the opening complex periodic graph before the t-formulae are introduced.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentMermaid-001 | Source: AI-proposed teaching enhancement based on supplied PDF and transcript evidence | Insert from mermaid/FA21TFormulaeBoundaryEnrichmentMermaid-001.md | Purpose: Show the workflow from double-angle formulae to t-formulae.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentSVG-001 | Source: Supplied screenshot PDF and FP1 PDF derivation evidence | Insert from svg/FA21TFormulaeBoundaryEnrichmentSVG-001.svg | Purpose: Preserve the teacher’s preferred triangle memory route for deriving $\sin\theta$ and $\cos\theta$.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentTikZ-001 | Source: Supplied screenshot PDF and FP1 PDF derivation evidence | Insert from tikz/FA21TFormulaeBoundaryEnrichmentTikZ-001.tex | Purpose: Provide a precise mathematical triangle suitable for printable notes.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths enrichment evidence | Insert from svg/FA21TFormulaeBoundaryEnrichmentBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths double-angle formulae with the t-formulae extension.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentSVG-002 | Source: Supplied screenshot PDF alternative proof evidence | Insert from svg/FA21TFormulaeBoundaryEnrichmentSVG-002.svg | Purpose: Show the alternative derivation triangle with angle $\theta/2$.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentSVG-003 | Source: AI-proposed teaching enhancement based on transcript warnings | Insert from svg/FA21TFormulaeBoundaryEnrichmentSVG-003.svg | Purpose: Show why solving $\tan(\theta/2)=t$ requires the half-angle range.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentSVG-004 | Source: Transcript warnings about angle doubling | Insert from svg/FA21TFormulaeBoundaryEnrichmentSVG-004.svg | Purpose: Prevent angle-substitution errors.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentMermaid-002 | Source: Transcript explanation of translating trig equations into t-equations | Insert from mermaid/FA21TFormulaeBoundaryEnrichmentMermaid-002.md | Purpose: Show the full equation-solving pipeline.]

[VISUAL PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentTikZ-002 | Source: PDF and transcript modelling/differentiation example | Insert from tikz/FA21TFormulaeBoundaryEnrichmentTikZ-002.tex | Purpose: Show why differentiating first is cleaner than substituting first.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA21TFormulaeBoundaryEnrichmentWidget-001.html | Purpose: Enter $t$ and see exact or simplified values of $\sin\theta$, $\cos\theta$, $\tan\theta$, $\sec\theta$, $\cosec\theta$, and $\cot\theta$.]

[INTERACTIVE PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA21TFormulaeBoundaryEnrichmentWidget-002.html | Purpose: Map the original angle range to the half-angle range before solving $\tan(\theta/2)=t$.]

[INTERACTIVE PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentWidget-003 | Source: AI-proposed teaching enhancement based on identity examples | Insert from widgets/FA21TFormulaeBoundaryEnrichmentWidget-003.html | Purpose: Reveal identity proofs using t-formulae line by line.]

[INTERACTIVE PLACEHOLDER: FA21TFormulaeBoundaryEnrichmentWidget-004 | Source: AI-proposed teaching enhancement based on optional modelling evidence | Insert from widgets/FA21TFormulaeBoundaryEnrichmentWidget-004.html | Purpose: Show how differentiating first and substituting later leads to a cleaner modelling solution.]

## 11. Worked Examples

### Worked Example 1: Direct use when $\tan(\theta/2)=3/4$

Given

$$
\tan\frac{\theta}{2}=\frac34,
$$

we have

$$
t=\frac34.
$$

Find $\sin\theta$:

$$
\sin\theta=\frac{2t}{1+t^2}=\frac{2(3/4)}{1+(3/4)^2}.
$$

The numerator is

$$
2\cdot\frac34=\frac32.
$$

The denominator is

$$
1+\frac9{16}=\frac{25}{16}.
$$

Therefore

$$
\sin\theta=\frac{3/2}{25/16}=\frac32\cdot\frac{16}{25}=\frac{24}{25}.
$$

Find $\cos\theta$:

$$
\cos\theta=\frac{1-t^2}{1+t^2}=\frac{1-9/16}{1+9/16}=\frac{7/16}{25/16}=\frac7{25}.
$$

So

$$
\boxed{\sin\theta=\frac{24}{25}},\qquad
\boxed{\cos\theta=\frac7{25}}.
$$

### Worked Example 2: Find $t$ first from $\sin(\theta/2)$

Given

$$
\frac\pi2\le\frac\theta2<\pi,
\qquad
\sin\frac\theta2=\frac8{17},
$$

find $t$.

Use

$$
\cos^2\frac\theta2=1-\sin^2\frac\theta2=1-\frac{64}{289}=\frac{225}{289}.
$$

So

$$
\cos\frac\theta2=\pm\frac{15}{17}.
$$

Since $\theta/2$ is obtuse, cosine is negative:

$$
\cos\frac\theta2=-\frac{15}{17}.
$$

Then

$$
t=\tan\frac\theta2=\frac{8/17}{-15/17}=-\frac8{15}.
$$

Now

$$
\cot\theta=\frac{1-t^2}{2t}.
$$

Substitute $t=-8/15$:

$$
\cot\theta=\frac{1-64/225}{-16/15}=\frac{161/225}{-16/15}=-\frac{161}{240}.
$$

Also

$$
\sec\theta+\cosec\theta=\frac{1+t^2}{1-t^2}+\frac{1+t^2}{2t}.
$$

With $t=-8/15$,

$$
1+t^2=\frac{289}{225},\qquad 1-t^2=\frac{161}{225},\qquad 2t=-\frac{16}{15}.
$$

So

$$
\sec\theta=\frac{289}{161},\qquad \cosec\theta=-\frac{289}{240}.
$$

Therefore

$$
\sec\theta+\cosec\theta=\frac{289}{161}-\frac{289}{240}=0.590864\ldots
$$

and to 3 significant figures,

$$
\boxed{\sec\theta+\cosec\theta=0.591}.
$$

### Worked Example 3: Identity with $t=\tan\theta$

Prove

$$
\tan2\theta\cot\theta\equiv1+\sec2\theta.
$$

Because the identity involves $\theta$ and $2\theta$, let

$$
t=\tan\theta.
$$

Then

$$
\tan2\theta=\frac{2t}{1-t^2},\qquad \cot\theta=\frac1t.
$$

So

$$
\text{LHS}=\frac{2t}{1-t^2}\cdot\frac1t=\frac2{1-t^2}.
$$

Also

$$
\sec2\theta=\frac{1+t^2}{1-t^2}.
$$

Thus

$$
\text{RHS}=1+\frac{1+t^2}{1-t^2}=\frac{1-t^2}{1-t^2}+\frac{1+t^2}{1-t^2}=\frac2{1-t^2}.
$$

Therefore LHS $\equiv$ RHS.

## 12. Common Mistakes and Exam Traps

| Mistake | Repair |
|---|---|
| Treating the topic as confirmed CCEA core | Keep the boundary label: enrichment only unless direct CCEA evidence is supplied. |
| Memorising the formulae without structure | Remember $\tan\theta=2t/(1-t^2)$, then use the triangle. |
| Using $t=\tan(\theta/2)$ for a $2\theta$ identity | Match the angle ladder. For $\theta\to2\theta$, use $t=\tan\theta$. |
| Taking a square root without quadrant information | Use the range to choose the sign. |
| Clearing denominators without exclusions | Record $t\ne0$ or $t\ne\pm1$ where relevant. |
| Confusing $\cot\theta$ and $\cot2\theta$ | If $t=\tan\theta$, then $\cot\theta=1/t$. |
| Subtracting brackets wrongly | $4-(2+\sqrt2)=4-2-\sqrt2$. |
| Turning $2(2t)$ into $4t^2$ | $2(2t)=4t$. |
| Reporting $\theta/2$ instead of $\theta$ | Solve in the half-angle range, then double. |
| Calculator mode mismatch | Use radians for ranges involving $\pi$ and degrees for degree ranges. |
| Expanding target factors | Preserve useful factors such as $(1+t^2)^2$. |
| Treating $t$ as time in modelling | In the supplied model, $x$ is time and $t=\tan x$ is only a substitution. |

## 13. Practice Questions

These questions are AI-generated enrichment questions, not CCEA past-paper questions.

1. Starting from $\tan2A=\dfrac{2\tan A}{1-\tan^2A}$, derive the three t-formulae.
2. Given $\tan(\theta/2)=5/12$, find exact values of $\sin\theta$, $\cos\theta$, $\tan\theta$, $\cot\theta$, $\sec\theta$ and $\cosec\theta$.
3. Given $\pi/2<\theta/2<\pi$ and $\cos(\theta/2)=-7/25$, find $t$, $\sin\theta$, $\cos\theta$ and $\tan\theta$.
4. Let $t=\tan u$. Write down $\sin2u$, $\cos2u$ and $\tan2u$ in terms of $t$.
5. Correct each mistake: $2(2t)=4t^2$; $4-(2+\sqrt2)=4-2+\sqrt2$; if $t=\tan\theta$, then $\cot\theta=(1-t^2)/(2t)$.
6. Prove $\dfrac{1-\cos\theta}{\sin\theta}\equiv t$ where $t=\tan(\theta/2)$.
7. Solve $2\sin\theta+\cos\theta=1$ for $0\le\theta\le2\pi$.
8. Solve $3\cos\theta+4\sin\theta=0$ for $0\le\theta\le2\pi$ using $t=\tan(\theta/2)$.
9. Prove $\dfrac{1-\cos2\theta+\sin2\theta}{1+\cos2\theta+\sin2\theta}\equiv t$ where $t=\tan\theta$.
10. Optional modelling: if $s=\sin2x+\cos2x$ and $t=\tan x$, show $v=\dfrac{2(1-2t-t^2)}{1+t^2}$ and find the stationary points in $0\le x\le\pi$.

## 14. Worked Solutions

### Solution 1

As in Section 8, setting $A=\theta/2$ in the tangent double-angle formula gives

$$
\tan\theta=\frac{2t}{1-t^2}.
$$

The triangle gives opposite $2t$, adjacent $1-t^2$, hypotenuse $1+t^2$, so

$$
\sin\theta=\frac{2t}{1+t^2},\qquad \cos\theta=\frac{1-t^2}{1+t^2}.
$$

### Solution 2

With $t=5/12$,

$$
t^2=25/144,
$$

$$
1+t^2=169/144,
$$

$$
1-t^2=119/144,
$$

$$
2t=5/6.
$$

Thus

$$
\sin\theta=\frac{5/6}{169/144}=\frac{120}{169},
$$

$$
\cos\theta=\frac{119/144}{169/144}=\frac{119}{169},
$$

$$
\tan\theta=\frac{5/6}{119/144}=\frac{120}{119}.
$$

Therefore

$$
\cot\theta=\frac{119}{120},\qquad
\sec\theta=\frac{169}{119},\qquad
\cosec\theta=\frac{169}{120}.
$$

### Solution 3

Since $\cos(\theta/2)=-7/25$ and $\theta/2$ is in Quadrant II,

$$
\sin\frac\theta2=\frac{24}{25}.
$$

So

$$
t=\tan\frac\theta2=\frac{24/25}{-7/25}=-\frac{24}{7}.
$$

Then

$$
t^2=576/49,
$$

$$
1+t^2=625/49,
$$

$$
1-t^2=-527/49,
$$

$$
2t=-48/7.
$$

Therefore

$$
\sin\theta=-\frac{336}{625},\qquad
\cos\theta=-\frac{527}{625},\qquad
\tan\theta=\frac{336}{527}.
$$

### Solution 4

If $t=\tan u$,

$$
\sin2u=\frac{2t}{1+t^2},\qquad
\cos2u=\frac{1-t^2}{1+t^2},\qquad
\tan2u=\frac{2t}{1-t^2}.
$$

$\tan2u$ is undefined when $1-t^2=0$, so when $t=\pm1$.

### Solution 5

$$
2(2t)=4t.
$$

$$
4-(2+\sqrt2)=4-2-\sqrt2=2-\sqrt2.
$$

If $t=\tan\theta$, then

$$
\cot\theta=\frac1t.
$$

The expression $(1-t^2)/(2t)$ would be $\cot2\theta$.

### Solution 6

Using

$$
\sin\theta=\frac{2t}{1+t^2},\qquad
\cos\theta=\frac{1-t^2}{1+t^2},
$$

we get

$$
\frac{1-\cos\theta}{\sin\theta}
=
\frac{1-\frac{1-t^2}{1+t^2}}{\frac{2t}{1+t^2}}
=
\frac{\frac{2t^2}{1+t^2}}{\frac{2t}{1+t^2}}
=t.
$$

### Solution 7

Let $t=\tan(\theta/2)$.

$$
2\sin\theta+\cos\theta=1
$$

becomes

$$
2\left(\frac{2t}{1+t^2}\right)+\frac{1-t^2}{1+t^2}=1.
$$

Multiply by $1+t^2$:

$$
4t+1-t^2=1+t^2.
$$

So

$$
4t-2t^2=0,
$$

$$
2t(2-t)=0.
$$

Thus $t=0$ or $t=2$. Since $0\le\theta/2\le\pi$,

$$
\theta=0,
\quad
\theta=2\tan^{-1}2,
\quad
\theta=2\pi.
$$

### Solution 8

Let $t=\tan(\theta/2)$.

$$
3\cos\theta+4\sin\theta=0
$$

becomes

$$
3\left(\frac{1-t^2}{1+t^2}\right)+4\left(\frac{2t}{1+t^2}\right)=0.
$$

Multiply by $1+t^2$:

$$
3-3t^2+8t=0.
$$

So

$$
3t^2-8t-3=0.
$$

Factorise:

$$
(3t+1)(t-3)=0.
$$

Thus

$$
t=-\frac13\quad\text{or}\quad t=3.
$$

Therefore

$$
\theta=2\tan^{-1}3
$$

or

$$
\theta=2\pi-2\tan^{-1}\left(\frac13\right).
$$

### Solution 9

Let $t=\tan\theta$. Then

$$
\sin2\theta=\frac{2t}{1+t^2},\qquad
\cos2\theta=\frac{1-t^2}{1+t^2}.
$$

The numerator becomes

$$
1-\frac{1-t^2}{1+t^2}+\frac{2t}{1+t^2}=\frac{2t^2+2t}{1+t^2}=\frac{2t(t+1)}{1+t^2}.
$$

The denominator becomes

$$
1+\frac{1-t^2}{1+t^2}+\frac{2t}{1+t^2}=\frac{2+2t}{1+t^2}=\frac{2(1+t)}{1+t^2}.
$$

Thus the ratio is

$$
\frac{2t(t+1)/(1+t^2)}{2(1+t)/(1+t^2)}=t.
$$

### Solution 10

If

$$
s=\sin2x+\cos2x,
$$

then

$$
v=\frac{ds}{dx}=2\cos2x-2\sin2x.
$$

With $t=\tan x$,

$$
v=2\left(\frac{1-t^2}{1+t^2}\right)-2\left(\frac{2t}{1+t^2}\right)
=
\frac{2-2t^2-4t}{1+t^2}
=
\frac{2(1-2t-t^2)}{1+t^2}.
$$

Set $v=0$:

$$
1-2t-t^2=0.
$$

So

$$
t^2+2t-1=0,
$$

and

$$
t=-1\pm\sqrt2.
$$

Since $t=\tan x$ and $0\le x\le\pi$,

$$
x=\frac\pi8,\frac{5\pi}{8}.
$$

At $x=\pi/8$, $s=\sqrt2$; at $x=5\pi/8$, $s=-\sqrt2$. Therefore the maximum occurs at $x=\pi/8$ and the minimum at $x=5\pi/8$.

## 15. Exam Technique Notes

1. Always state the substitution, for example $t=\tan(\theta/2)$.
2. Match the angle ladder before using formulae.
3. Use exact values until the final rounding step.
4. Convert the original range into the half-angle range.
5. If $0\le\theta\le2\pi$, then $0\le\theta/2\le\pi$.
6. Record denominator restrictions when multiplying by $t$, $1-t^2$ or reciprocal expressions.
7. In identity proofs, convert both sides into $t$ and end with a clear conclusion.
8. In modelling, differentiate first and substitute second.
9. Preserve target factorisations such as $(1+t^2)^2$.
10. Keep the boundary label: this is enrichment, not confirmed CCEA core.

## 16. Syllabus Gap Check

| Item | Status |
|---|---|
| Direct CCEA t-formulae LO | Not found. |
| LO IDs invented? | No. |
| Nearest CCEA anchor | `FA21-FCALC-LO004`, not claimed as covered. |
| Related background LO | `FA21-CN-LO001`, not claimed as covered. |
| Cross-board material | Logged as enrichment. |
| Edexcel specimen example | Not treated as CCEA. |
| Weierstrass/integration context | Mentioned only as future context unless direct CCEA evidence is supplied. |

### Off-Spec Content Found but Excluded

- Direct claim that t-formulae are CCEA core: excluded.
- Edexcel FP1 specimen-paper question: not taught as CCEA core.
- Formula-book claims from the transcript: not generalised to CCEA.
- Weierstrass substitution: not taught as core in this lesson.

## 17. Recommended Enhancements Not in the Evidence

- Angle-ladder diagram.
- Half-angle range number line.
- Denominator danger map.
- Identity proof builder widget.
- t-formula substitution checker.
- Modelling route comparison: differentiate first versus substitute first.

These are AI-proposed teaching enhancements, not evidence-backed CCEA requirements.

## 18. Supplementary Sources Used

### Project sources

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

### Lesson-specific evidence

- `FP1-Chp5-tFormulae.pdf`
- `transcripts.md`
- `Chapter_5_The_t-formulae_🧩_(Further_Pure_1)_screenshots.pdf`

### Boundary statement

The evidence supports a rich t-formulae enrichment lesson. It does not support the claim that t-formulae are a confirmed CCEA Further Mathematics core topic.

## 19. Final Student Checklist

### Prerequisite checklist

- [ ] I can use Pythagoras.
- [ ] I can expand $(1-t^2)^2$.
- [ ] I can factorise $1-t^2$.
- [ ] I can simplify algebraic fractions.
- [ ] I can use $\sin^2\theta+\cos^2\theta=1$.
- [ ] I can use reciprocal trig functions.
- [ ] I can use double-angle formulae.
- [ ] I can solve tangent equations in a range.

### t-formulae checklist

- [ ] I can define $t=\tan(\theta/2)$.
- [ ] I can derive $\tan\theta=2t/(1-t^2)$.
- [ ] I can use the memory triangle.
- [ ] I can use $\sin\theta=2t/(1+t^2)$.
- [ ] I can use $\cos\theta=(1-t^2)/(1+t^2)$.
- [ ] I can check denominators.
- [ ] I can undo the substitution and range-check.

### Boundary-awareness checklist

- [x] No direct CCEA t-formulae LO found.
- [x] No LO IDs invented.
- [x] Cross-board/Pearson/Edexcel/DrFrost material labelled as enrichment.
- [x] Ordinary A-Level Maths labelled as bridge only.
- [x] Missing CCEA evidence logged honestly.

Final student statement:

$$
\boxed{\text{I can use the t-formulae as enrichment, while keeping the CCEA boundary clear.}}
$$
