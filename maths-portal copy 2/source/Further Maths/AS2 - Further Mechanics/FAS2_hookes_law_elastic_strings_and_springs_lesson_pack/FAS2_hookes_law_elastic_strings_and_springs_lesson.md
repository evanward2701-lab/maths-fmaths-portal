# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-04
course: CCEA GCE Further Mathematics
unit_code: FAS2
unit_title: Further AS 2 Applied Mathematics
applied_section: Section A: Mechanics 1
primary_topic_code: FAS2-HOOKE
primary_topic_name: Hooke's law
linked_topic_code: FAS2-WENG
linked_topic_name: Work and energy
lesson_title: Elastic Strings and Springs
topic_slug: hookes_law_elastic_strings_and_springs
topic_pascal: HookesLawElasticStringsAndSprings
topic_id: FAS2HookesLawElasticStringsAndSprings
lesson_file: FAS2_hookes_law_elastic_strings_and_springs_lesson.md
primary_lo_ids:
  - FAS2-HOOKE-LO001
  - FAS2-HOOKE-LO002
linked_lo_ids:
  - FAS2-WENG-LO001
  - FAS2-WENG-LO002
  - FAS2-WENG-LO003
  - FAS2-WENG-LO004
bridge_tags:
  - Ordinary AS2 Forces and Newton's Laws
  - Ordinary AS2 Quantities and Units
  - Ordinary AS2 Equilibrium
  - Ordinary AS2 Friction
  - Ordinary A-Level Mechanics Energy
topic_tags:
  - Hooke's Law
  - Elastic Strings
  - Elastic Springs
  - Modulus of Elasticity
  - Natural Length
  - Extension
  - Compression
  - Tension
  - Thrust
  - Elastic Limit
  - Elastic Potential Energy
```

# 2. Evidence Map

| Source | Use | Status |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Official topic boundary, unit, LO IDs and wording | Authoritative Further Maths source |
| `Further_Maths_README_module_map.md` | Topic mapping and bridge context | Project source |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence handling rules | Project source |
| `FM1-Chp3-Elastic Strings and Springs.pdf` | Slide definitions, formulas, worked examples, diagrams and energy section | Lesson-specific evidence |
| `transcripts.md` | Teacher narrative, warnings, worked method and wording traps | Lesson-specific evidence |
| `Chapter_3_Elastic_Strings_&_Springs_🎯_(Further_Mechanics_1)_screenshots.pdf` | Visual confirmation of diagrams, handwritten annotations and slide flow | Lesson-specific visual evidence |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary A-Level Mechanics bridge only | Bridge source |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary CCEA A-Level Maths bridge only | Bridge source |

Visual evidence limitation: the screenshots PDF contains many screen recording/navigation frames. Only readable mathematical content is preserved. No uninspected diagram detail is claimed.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Boundary |
|---|---|---|---|
| `FAS2-HOOKE-LO001` | use Hooke's law as a model, relating the force in an elastic string or spring to the extension or compression, and understand the term modulus of elasticity | Defines and uses `T = lambda x/l`, tension, thrust, natural length, extension/compression, and modulus of elasticity | Core |
| `FAS2-HOOKE-LO002` | demonstrate understanding of and use the modelling assumptions in problems involving the application of Hooke's law, including familiarity with the idea of elastic limits | Light strings/springs, elastic limit, strings cannot resist compression, springs can compress, limitations of model | Core |
| `FAS2-WENG-LO001` | calculate work done by a force when its point of application undergoes a displacement, including use of the scalar product | Work done against resistance and external work in energy examples | Linked work-energy content |
| `FAS2-WENG-LO002` | calculate the work done by a variable force, where the force is given as a simple function of displacement: `W = integral_a^b F dx` | Derivation of elastic potential energy from Hooke's Law | Linked work-energy content |
| `FAS2-WENG-LO003` | demonstrate understanding of the concepts of kinetic energy, gravitational potential energy and elastic potential energy, and use the formulae to calculate these | Uses `KE`, `GPE`, and `EPE = lambda x^2/(2l)` | Linked work-energy content |
| `FAS2-WENG-LO004` | demonstrate understanding of and use the relationship between the change in energy of a system and the work done by the external forces, and use the Principle of Conservation of Mechanical Energy in appropriate cases | Energy equations for greatest distance, speed, bumper compression and further compression | Linked work-energy content |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Use Hooke's Law in the form

\[
T=\frac{\lambda x}{l}.
\]

2. Explain the meaning and units of the modulus of elasticity \(\lambda\).
3. Distinguish natural length, extension, compression and total current length.
4. Decide whether the elastic force is tension, thrust, or zero.
5. Explain why elastic springs can be compressed but elastic strings cannot resist compression.
6. Use modelling assumptions, including light strings/springs and elastic limits.
7. Combine Hooke's Law with equilibrium, resolving forces, friction and \(F=ma\).
8. Solve connected string/spring problems by linking extensions and forces.
9. Use elastic potential energy when the work-energy method is appropriate:

\[
EPE=\frac{\lambda x^2}{2l}.
\]

## Bridge objectives

You should be able to explain how ordinary A-Level Mechanics changes when the string or spring becomes elastic.

| Ordinary idea | Further Mechanics upgrade |
|---|---|
| Inextensible string has a tension determined from the force diagram | Elastic string has tension depending on extension: \(T=\lambda x/l\) |
| Equilibrium gives one force equation | Equilibrium plus Hooke's Law often gives simultaneous equations |
| Energy includes \(KE\) and \(GPE\) | Elastic problems add \(EPE=\lambda x^2/(2l)\) |

# 5. Explicit Prerequisite Recap

## GCSE foundations

You need rearranging equations, fractions, ratios, trigonometry, Pythagoras and unit conversion.

## Ordinary AS/A-Level Mathematics foundations

You need:

\[
\text{weight}=mg,\qquad \sum F=0,\qquad F=ma,\qquad F\leq \mu R,
\]

and the energy formulae:

\[
KE=\frac12mv^2,\qquad GPE=mgh.
\]

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary AS2 Mechanics: Forces and Newton's Laws | Draw force diagrams, use \(F=ma\), resolve forces, and set resultant force to zero in equilibrium | Elastic strings/springs add a force whose size depends on extension or compression | Do not assume tension is fixed independently of geometry |
| Ordinary AS2 Mechanics: Friction | Use \(F\leq \mu R\), and \(F=\mu R\) at limiting equilibrium | Elastic force may oppose or assist impending motion depending on position | Friction direction is chosen from impending motion |
| Ordinary AS2 Mechanics: Units and modelling | Use newtons, metres, kilograms and \(g\) | \(\lambda\) is in newtons; \(x\) and \(l\) must be in matching length units | cm and m must not be mixed |
| Ordinary trigonometry | Use \(\sin\), \(\cos\), \(\tan\), and right-angled geometry | Extension may be hidden inside a triangle | Wrong side of the triangle gives wrong elastic force |
| Ordinary Mechanics Energy | Use \(KE\), \(GPE\), work done and conservation | Add elastic potential energy \(\lambda x^2/(2l)\) | Energy is not the method for acceleration |

In ordinary A-Level Maths, this idea appeared as force balance, resolving, friction, \(F=ma\) and energy conservation.

In Further Maths, the same idea becomes elastic modelling: the force is not merely “some tension”. It is a force generated by extension or compression.

The key upgrade is:

\[
\boxed{\text{Elastic force}=\text{mechanics force equation}+\text{geometry of extension}}.
\]

The danger is treating an elastic string like an inextensible string.

# 6. Big Picture Explanation

Elastic strings and springs are where Further Mechanics starts acting like a mechanical puzzle-box. In ordinary Mechanics a string is usually inextensible, so tension is found from force balance. In this topic the object stretches or compresses, so the force also obeys

\[
T=\frac{\lambda x}{l}.
\]

Every elastic problem has two worlds:

| World | What it tells you |
|---|---|
| Elastic world | force depends on extension/compression |
| Mechanics world | equilibrium, \(F=ma\), friction, resolving, or energy gives another relationship |

Static questions usually combine \(T=\lambda x/l\) with \(\sum F=0\). Dynamics questions combine it with \(F=ma\). Speed and distance questions often use energy with \(EPE=\lambda x^2/(2l)\).

# 7. Key Definitions and Notation

## Elastic string or spring

An elastic string or spring is modelled as an object obeying Hooke's Law within the range considered.

## Natural length

The natural length is the unstretched length, denoted \(l\). Write \(l\) clearly so it is not confused with \(1\).

## Extension

If current length is \(L\) and natural length is \(l\), then

\[
x=L-l.
\]

## Compression

For a spring compressed from natural length \(l\) to length \(L\),

\[
x=l-L.
\]

## Tension

Tension is a pulling elastic force, usually denoted \(T\).

## Thrust

Thrust is a pushing force in a compressed spring.

## Modulus of elasticity

The modulus of elasticity is \(\lambda\), measured in newtons. If a string of natural length \(l\) is stretched to length \(2l\), then \(x=l\), so

\[
T=\frac{\lambda l}{l}=\lambda.
\]

Thus \(\lambda\) may be understood as the force needed to double the length.

## Hooke's Law

\[
\boxed{T=\frac{\lambda x}{l}}
\]

where \(T\) is elastic force magnitude, \(\lambda\) is modulus of elasticity, \(x\) is extension/compression and \(l\) is natural length.

## Elastic limit

Hooke's Law applies only up to the elastic limit. Beyond this, the object may deform or break and force may no longer be proportional to extension.

## Elastic potential energy

\[
\boxed{EPE=\frac{\lambda x^2}{2l}}.
\]

# 8. Core Theory

## 8.1 Hooke's Law as the new force model

Ordinary Mechanics might give \(T=mg\). Elastic modelling also gives

\[
T=\frac{\lambda x}{l}.
\]

So a typical problem is solved by writing both equations and solving them together.

**Bridge Note:** In ordinary A-Level Maths, a force diagram found the tension. Here, Further Maths makes the tension depend on the geometry of the elastic object.

## 8.2 Why the formula is \(T=\lambda x/l\)

Hooke's Law says \(T\propto x\), so \(T=kx\). In this model, \(k=\lambda/l\). Therefore

\[
T=\frac{\lambda}{l}x=\frac{\lambda x}{l}.
\]

## 8.3 Interpreting \(\lambda\)

If the current length is \(2l\), then \(x=l\). Hence

\[
T=\frac{\lambda l}{l}=\lambda.
\]

So \(\lambda\) is the force needed to double the length.

## 8.4 Extension is not total length

If natural length is \(l\) and the string is stretched to length \(3l\), then

\[
x=3l-l=2l,
\]

not \(3l\). The phrases “stretched to” and “extended by” are different. “To” usually gives the total length; “by” gives the change.

## 8.5 Strings versus springs

A stretched string or spring produces tension. A compressed spring produces thrust. A compressed string goes slack and has

\[
T=0.
\]

## 8.6 Light strings and springs

In the A-Level model, strings and springs are light, so they have no weight and do not extend under their own weight. The model ignores their mass.

## 8.7 Elastic limit and the force-extension graph

In the Hooke's Law region, the force-extension graph is a straight line through the origin with gradient \(\lambda/l\). After the elastic limit, Hooke's Law is not assumed to hold.

## 8.8 Standard two-equation method

1. Draw a diagram.
2. Find \(x\), the extension/compression.
3. Write Hooke's Law.
4. Write the mechanics equation.
5. Solve and interpret.

## 8.9 Simple vertical equilibrium

For a particle of mass \(m\) hanging at rest:

\[
T=mg,
\]

and

\[
T=\frac{\lambda x}{l}.
\]

So

\[
mg=\frac{\lambda x}{l},\qquad x=\frac{mgl}{\lambda}.
\]

Total length is \(l+x\).

## 8.10 Horizontal compression of a spring

If a spring is compressed by \(x\), its thrust magnitude is

\[
P=\frac{\lambda x}{l}.
\]

If held by an external force \(F\), equilibrium gives

\[
F=\frac{\lambda x}{l}.
\]

## 8.11 Combined strings and springs

If springs \(PQ\) and \(QR\) are joined in a line, the extensions are linked by total length and the tensions are linked by equilibrium.

For the evidence example:

\[
l_{PQ}=1.6,\quad \lambda_{PQ}=20,\quad l_{QR}=1.4,\quad \lambda_{QR}=28,\quad PR=4.
\]

Total natural length is \(3\), so total extension is \(1\). Let the extension of \(PQ\) be \(x\). Then extension of \(QR\) is \(1-x\). Equilibrium at \(Q\) gives

\[
\frac{20x}{1.6}=\frac{28(1-x)}{1.4}.
\]

This leads to

\[
x=\frac{8}{13},\qquad T=\frac{100}{13}=7.69\text{ N}.
\]

## 8.12 Particle between two vertical springs

If two identical springs of natural length \(l\) and modulus \(2mg\) are fixed \(4l\) apart with a mass \(m\) at the join, let the top extension be \(x\), so the bottom extension is \(2l-x\). Vertical equilibrium gives

\[
\frac{2mgx}{l}=\frac{2mg(2l-x)}{l}+mg.
\]

Divide by \(mg\) and multiply by \(l\):

\[
2x=2(2l-x)+l=5l-2x.
\]

So

\[
4x=5l,
\qquad x=\frac{5l}{4}.
\]

Distance below \(P\):

\[
l+x=l+\frac{5l}{4}=\frac{9l}{4}.
\]

## 8.13 Resolving forces with an elastic string at an angle

For an elastic string at angle \(\alpha\) with the vertical, held by a horizontal force \(28\) N and weight \(4g\):

\[
T\sin\alpha=28,
\qquad
T\cos\alpha=4g.
\]

Divide:

\[
\tan\alpha=\frac{28}{4g}.
\]

Then find \(T\), use Hooke's Law to find extension, and add natural length if the question asks for \(OP\).

## 8.14 Midpoint of an elastic string

If a particle is attached to the midpoint of a string, the two halves act like independent strings. Each half has half the natural length, but the same modulus of elasticity as the original string.

For a string of natural length \(2l\), modulus \(4mg\), with each half at \(30^\circ\) to the horizontal:

\[
T=Mg
\]

from vertical equilibrium, and

\[
AP=\frac{l}{\cos30^\circ}=\frac{2\sqrt3}{3}l.
\]

Extension of each half:

\[
x=\left(\frac{2\sqrt3}{3}-1\right)l.
\]

Hooke's Law:

\[
T=4mg\left(\frac{2\sqrt3}{3}-1\right).
\]

Therefore

\[
M=4m\left(\frac{2\sqrt3}{3}-1\right)=0.619m\text{ to 3 s.f.}
\]

## 8.15 Slopes, friction and elastic springs

For a slope at \(30^\circ\),

\[
R=mg\cos30^\circ=\frac{\sqrt3}{2}mg.
\]

If \(\mu=\sqrt3/3\), limiting friction is

\[
F=\mu R=\frac{\sqrt3}{3}\cdot\frac{\sqrt3}{2}mg=\frac12mg.
\]

Also,

\[
mg\sin30^\circ=\frac12mg.
\]

For the evidence spring of natural length \(a\), modulus \(3mg\), the limiting lower position gives

\[
T=\frac12mg+\frac12mg=mg.
\]

If \(AP=L\), then

\[
mg=\frac{3mg(L-a)}{a}.
\]

Cancel \(mg\):

\[
1=\frac{3(L-a)}{a},\quad a=3L-3a,
\quad 4a=3L,
\quad L=\frac{4a}{3}.
\]

At the upper limiting position, friction balances the down-slope component of weight with zero elastic force, so \(AP=a\). Hence

\[
\boxed{a\le AP\le \frac{4a}{3}}.
\]

## 8.16 Dynamics with Hooke's Law

For a particle on an elastic string, use \(F=ma\). Maximum speed occurs when \(a=0\); greatest displacement occurs when \(v=0\).

Evidence example: natural length \(0.5\) m, modulus \(20\) N, mass \(2\) kg, initial length \(1.5\) m.

Initial extension:

\[
x=1.5-0.5=1.0.
\]

Initial tension:

\[
T=\frac{20(1)}{0.5}=40\text{ N}.
\]

Taking upward positive:

\[
40-2g=2a,
\quad 40-19.6=2a,
\quad a=10.2\text{ m s}^{-2}.
\]

Maximum speed occurs when \(a=0\), so

\[
T=2g.
\]

Thus

\[
\frac{20x}{0.5}=2g,
\quad 40x=19.6,
\quad x=0.49.
\]

Length is

\[
0.5+0.49=0.99\text{ m}.
\]

## 8.17 When to use energy

Use \(F=ma\) for acceleration and force. Use energy for speed, greatest distance and work done.

## 8.18 Elastic potential energy

Hooke's Law gives force at extension \(s\):

\[
F=\frac{\lambda s}{l}.
\]

Work done stretching from \(0\) to \(x\):

\[
W=\int_0^x \frac{\lambda s}{l}\,ds
=\frac{\lambda}{l}\left[\frac{s^2}{2}\right]_0^x
=\frac{\lambda x^2}{2l}.
\]

So

\[
EPE=\frac{\lambda x^2}{2l}.
\]

## 8.19 Conservation of energy with elastic strings and springs

Use

\[
\text{Work in}+KE_1+GPE_1+EPE_1=KE_2+GPE_2+EPE_2+\text{Work out}.
\]

At greatest distance, \(v=0\). At maximum speed, \(a=0\). They are not the same condition.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsMermaid-001 | Source: CCEA Further Mathematics specification + FM1 Elastic Strings and Springs lesson evidence | Insert from mermaid/FAS2HookesLawElasticStringsAndSpringsMermaid-001.md | Purpose: Show the standard two-equation method for Hooke's Law problems. Description: Flowchart begins with “Draw diagram”, branches to “Find extension/compression \(x\)” and “Write mechanics equation”, then joins at “Use \(T=\lambda x/l\)” and ends with “Solve and interpret units”.]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsMermaid-002 | Source: FM1 problem-solving considerations evidence | Insert from mermaid/FAS2HookesLawElasticStringsAndSpringsMermaid-002.md | Purpose: Help students choose between Hooke's Law with \(F=ma\) and the work-energy method. Description: Decision tree asks whether the question asks for acceleration/force/equilibrium or distance/speed/greatest displacement, then routes to the correct method.]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsSVG-001 | Source: FM1-Chp3-Elastic Strings and Springs.pdf, Hooke's Law: When it Applies | Insert from svg/FAS2HookesLawElasticStringsAndSpringsSVG-001.svg | Purpose: Recreate the force-extension graph showing the proportional Hooke's Law region, elastic limit and non-linear region beyond the elastic limit. Description: Axes labelled Force and Extension; initial straight-line region from origin; marked elastic limit; curve beyond elastic limit; note that Hooke's Law applies only in the proportional region.]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsSVG-002 | Source: FM1 PDF + teacher transcript distinction between strings and springs | Insert from svg/FAS2HookesLawElasticStringsAndSpringsSVG-002.svg | Purpose: Compare elastic string and elastic spring behaviour under stretching and compression. Description: Four panels: stretched string with tension; stretched spring with tension; compressed spring with thrust; compressed string shown slack with \(T=0\).]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsSVG-003 | Source: FM1 combined strings/springs worked example | Insert from svg/FAS2HookesLawElasticStringsAndSpringsSVG-003.svg | Purpose: Show how two spring extensions are linked in a horizontal combined-spring problem. Description: Horizontal line from \(P\) to \(R\), joined point \(Q\), total distance \(4\), natural lengths \(1.6\), \(1.4\), extensions \(x\), \(1-x\), equal opposing tensions at \(Q\).]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA Further Mathematics specification | Insert from svg/FAS2HookesLawElasticStringsAndSpringsBridgeSVG-001.svg | Purpose: Compare prior ordinary Mechanics tension handling with Further Mechanics Hooke's Law extension. Description: Left side shows ordinary inextensible string with tension found from equilibrium; right side shows elastic string with force equation plus \(T=\lambda x/l\).]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsTikZ-001 | Source: FM1 simple vertical elastic string example | Insert from tikz/FAS2HookesLawElasticStringsAndSpringsTikZ-001.tex | Purpose: Show a particle hanging from an elastic string with natural length and extension labelled. Description: Fixed point at top, vertical elastic string, particle at bottom, upward \(T\), downward \(4g\), side labels for natural length \(l=2\) and extension \(x\).]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsTikZ-002 | Source: FM1 angled statics example | Insert from tikz/FAS2HookesLawElasticStringsAndSpringsTikZ-002.tex | Purpose: Show resolving of elastic tension at an angle. Description: Fixed point \(O\), particle \(P\), string \(OP\) making angle \(\alpha\) with vertical, horizontal applied force \(28\text{ N}\), weight \(4g\), components \(T\sin\alpha\), \(T\cos\alpha\).]

[VISUAL PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsTikZ-003 | Source: FM1 rough inclined plane inequality example | Insert from tikz/FAS2HookesLawElasticStringsAndSpringsTikZ-003.tex | Purpose: Show force diagram for a particle attached to an elastic spring on a rough inclined plane. Description: Plane inclined at \(30^\circ\), point \(A\) up the plane, particle \(P\), spring along plane, \(R\), \(mg\), \(mg\sin30^\circ\), \(mg\cos30^\circ\), friction direction for limiting up/down cases.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2HookesLawElasticStringsAndSpringsWidget-001.html | Purpose: Reinforce use of \(T=\lambda x/l\), correct units, and interpretation of tension/thrust.]

[INTERACTIVE PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2HookesLawElasticStringsAndSpringsWidget-002.html | Purpose: Train students to distinguish “stretched to a length” from “extended by a distance”.]

[INTERACTIVE PLACEHOLDER: FAS2HookesLawElasticStringsAndSpringsWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence and linked `FAS2-WENG` coverage | Insert from widgets/FAS2HookesLawElasticStringsAndSpringsWidget-003.html | Purpose: Help students build work-energy equations involving \(KE\), \(GPE\), \(EPE\), work in and work out.]

# 11. Worked Examples

## 11.1 Hanging particle on an elastic string

An elastic string has natural length \(2\) m and modulus \(29.4\) N. A particle of mass \(4\) kg hangs at rest. Find the extension.

For equilibrium,

\[
T=4g.
\]

Hooke's Law gives

\[
T=\frac{29.4x}{2}.
\]

Thus

\[
4g=\frac{29.4x}{2}.
\]

Since \(29.4=3g\),

\[
4g=\frac{3gx}{2}.
\]

Multiply by \(2\):

\[
8g=3gx.
\]

Cancel \(g\):

\[
x=\frac83.
\]

So the extension is

\[
\boxed{\frac83\text{ m}=2.67\text{ m}}.
\]

If the total distance below the fixed point were requested, it would be

\[
2+\frac83=\frac{14}{3}=4.67\text{ m}.
\]

## 11.2 Compressed spring and modulus of elasticity

A spring has natural length \(1.5\) m and is compressed to \(1.0\) m by a horizontal force of \(6\) N. Find \(\lambda\).

Compression:

\[
x=1.5-1.0=0.5.
\]

Equilibrium gives thrust \(=6\) N, so

\[
6=\frac{\lambda(0.5)}{1.5}.
\]

Since \(0.5/1.5=1/3\),

\[
6=\frac{\lambda}{3},
\qquad \lambda=18.
\]

\[
\boxed{18\text{ N}}.
\]

## 11.3 Quickfire wording examples

If natural length is \(l\) and \(\lambda=123\) N:

- stretched to \(2l\): \(x=l\), so \(T=123\) N;
- stretched to \(3l\): \(x=2l\), so \(T=246\) N;
- extended by \(2l\): \(x=2l\), so \(T=246\) N.

A spring of natural length \(3\) m stretched to \(6\) m by \(99\) N has doubled its length, so \(\lambda=99\) N.

A spring of natural length \(l\) and \(\lambda=40\) N compressed to \(3l/4\) has compression \(l/4\), so

\[
T=\frac{40(l/4)}{l}=10\text{ N}.
\]

A compressed string is slack, so \(T=0\) and Hooke's Law compression is not used.

## 11.4 Two joined springs in series

Natural lengths \(1.6\) and \(1.4\); moduli \(20\) and \(28\); endpoint distance \(4\). Total extension is \(1\). Let extension of \(PQ\) be \(x\), so extension of \(QR\) is \(1-x\).

\[
\frac{20x}{1.6}=\frac{28(1-x)}{1.4}.
\]

\[
\frac{25}{2}x=20(1-x)=20-20x.
\]

\[
\frac{65}{2}x=20,
\qquad x=\frac{40}{65}=\frac{8}{13}.
\]

\[
T=\frac{20(8/13)}{1.6}=\frac{100}{13}=7.69\text{ N}.
\]

## 11.5 Two vertical springs with a particle at the join

Two springs each have natural length \(l\) and modulus \(2mg\). Fixed points are \(4l\) apart. A particle of mass \(m\) is at \(Q\). Let top extension be \(x\), so bottom extension is \(2l-x\). Equilibrium:

\[
\frac{2mgx}{l}=\frac{2mg(2l-x)}{l}+mg.
\]

Divide by \(mg\) and multiply by \(l\):

\[
2x=2(2l-x)+l=5l-2x.
\]

\[
4x=5l,
\quad x=\frac{5l}{4}.
\]

Distance below \(P\):

\[
l+x=l+\frac{5l}{4}=\frac{9l}{4}.
\]

## 11.6 Angled elastic string and horizontal force

A string has natural length \(2\) m, modulus \(98\) N, and holds a \(4\) kg particle with horizontal force \(28\) N. If angle with vertical is \(\alpha\), then

\[
T\sin\alpha=28,
\qquad T\cos\alpha=4g.
\]

Divide:

\[
\tan\alpha=\frac{28}{4g}=\frac{5}{7}.
\]

So

\[
\alpha=35.5^\circ.
\]

Using \(T=28/\sin\alpha\),

\[
T=48.173\ldots\text{ N}.
\]

Hooke's Law:

\[
48.173\ldots=\frac{98x}{2}=49x,
\qquad x=0.983\ldots.
\]

Thus

\[
OP=2+0.983\ldots=2.98\text{ m}.
\]

## 11.7 Midpoint of a string

For natural length \(2l\), modulus \(4mg\), and each half at \(30^\circ\): each half has natural length \(l\) and modulus \(4mg\). Let particle mass be \(M\).

Vertical equilibrium:

\[
T\sin30^\circ+T\sin30^\circ=Mg,
\quad T=Mg.
\]

Geometry:

\[
AP=\frac{l}{\cos30^\circ}=\frac{2\sqrt3}{3}l.
\]

Extension:

\[
x=\left(\frac{2\sqrt3}{3}-1\right)l.
\]

Hooke's Law:

\[
T=\frac{4mgx}{l}=4mg\left(\frac{2\sqrt3}{3}-1\right).
\]

Equate tensions:

\[
Mg=4mg\left(\frac{2\sqrt3}{3}-1\right).
\]

Cancel \(g\):

\[
\boxed{M=4m\left(\frac{2\sqrt3}{3}-1\right)=0.619m}.
\]

## 11.8 Rough slope range

For the evidence slope problem with \(\theta=30^\circ\), \(\mu=\sqrt3/3\), spring natural length \(a\), modulus \(3mg\):

\[
R=mg\cos30^\circ=\frac{\sqrt3}{2}mg,
\]

\[
F=\mu R=\frac{\sqrt3}{3}\cdot\frac{\sqrt3}{2}mg=\frac12mg,
\]

and

\[
mg\sin30^\circ=\frac12mg.
\]

At the lower limiting point, friction acts down the plane and tension acts up:

\[
T=\frac12mg+\frac12mg=mg.
\]

Let \(AP=L\). Then

\[
mg=\frac{3mg(L-a)}{a}.
\]

\[
1=\frac{3(L-a)}{a},
\quad a=3L-3a,
\quad 4a=3L,
\quad L=\frac{4a}{3}.
\]

At the upper limiting point, the spring force is zero, so \(L=a\). Hence

\[
\boxed{a\le AP\le \frac{4a}{3}}.
\]

## 11.9 Dynamics with Hooke's Law

Natural length \(0.5\) m, modulus \(20\) N, mass \(2\) kg, released from length \(1.5\) m.

Initial extension:

\[
x=1.5-0.5=1.0.
\]

Tension:

\[
T=\frac{20(1)}{0.5}=40.
\]

Taking upwards positive:

\[
40-2g=2a,
\quad 40-19.6=2a,
\quad a=10.2\text{ m s}^{-2}.
\]

Maximum speed occurs when \(a=0\), so \(T=2g\):

\[
\frac{20x}{0.5}=2g,
\quad 40x=19.6,
\quad x=0.49.
\]

Length:

\[
0.5+0.49=0.99\text{ m}.
\]

## 11.10 Elastic potential energy example

Natural length \(1.4\) m, modulus \(6\) N, length \(1.6\) m. Extension:

\[
x=1.6-1.4=0.2.
\]

\[
EPE=\frac{6(0.2)^2}{2(1.4)}=\frac{0.24}{2.8}=0.0857\text{ J}.
\]

## 11.11 Greatest distance below a fixed point

Mass \(0.5\) kg, natural length \(2\) m, modulus \(19.6\) N, released from \(O\). Let greatest distance be \(2+x\). At lowest point, \(v=0\).

\[
0.5g(2+x)=\frac{19.6x^2}{2(2)}=\frac{19.6x^2}{4}.
\]

Using \(g=9.8\):

\[
4.9(2+x)=4.9x^2.
\]

\[
2+x=x^2,
\quad x^2-x-2=0,
\quad (x-2)(x+1)=0.
\]

Valid extension:

\[
x=2.
\]

Greatest distance:

\[
2+x=4\text{ m}.
\]

## 11.12 Car compressing spring bumper

Mass \(1\) kg, initial speed \(3\), slope \(15^\circ\), resistance \(20\) N, compression \(0.10\) m, bumper spring natural length \(0.20\) m, modulus \(50\) N.

Initial KE:

\[
\frac12(1)(3^2)=4.5.
\]

Height lost:

\[
0.10\sin15^\circ.
\]

GPE lost:

\[
9.8(0.10\sin15^\circ)=0.98\sin15^\circ.
\]

EPE after compression:

\[
\frac{50(0.10)^2}{2(0.20)}=1.25.
\]

Work against resistance:

\[
20(0.10)=2.
\]

Energy equation:

\[
4.5+0.98\sin15^\circ=\frac12v^2+1.25+2.
\]

\[
4.753642\ldots=\frac12v^2+3.25.
\]

\[
1.503642\ldots=\frac12v^2,
\quad v^2=3.007284\ldots,
\quad v=1.73\text{ m s}^{-1}.
\]

## 11.13 Work done in further compression

A spring with \(\lambda=10\) N and \(l=0.6\) m is compressed further from \(0.1\) m to \(0.3\) m.

\[
EPE_1=\frac{10(0.1)^2}{2(0.6)}=\frac{0.1}{1.2}=\frac1{12}.
\]

\[
EPE_2=\frac{10(0.3)^2}{2(0.6)}=\frac{0.9}{1.2}=\frac34.
\]

\[
W=EPE_2-EPE_1=\frac34-\frac1{12}=\frac9{12}-\frac1{12}=\frac23\text{ J}.
\]

# 12. Common Mistakes and Exam Traps

1. Using total length instead of extension.
2. Forgetting to add natural length back on when total length is requested.
3. Treating a string as if it can be compressed.
4. Forgetting \(\lambda\) is measured in newtons.
5. Confusing \(\lambda\) with Young's modulus.
6. Thinking Hooke's Law applies beyond the elastic limit.
7. Missing the word “light”.
8. Assuming all tensions are equal.
9. Halving the modulus when a string is split at the midpoint.
10. Using energy when the question asks for acceleration.
11. Using \(F=ma\) when the question asks for greatest distance.
12. Confusing maximum speed \((a=0)\) with greatest displacement \((v=0)\).
13. Forgetting work done against resistance.
14. Squaring total length instead of extension in \(EPE\).
15. Mixing centimetres and metres.

# 13. Practice Questions

These are generated practice questions, not past-paper questions. Use \(g=9.8\text{ m s}^{-2}\).

1. An elastic string has natural length \(0.8\) m and modulus \(24\) N. It is stretched to length \(1.4\) m. Find the tension.
2. A spring has natural length \(1.2\) m and is compressed to \(0.9\) m by a force of \(15\) N. Find \(\lambda\).
3. A string has natural length \(l\) and \(\lambda=60\) N. Find the tension when it is (a) stretched to \(4l\), (b) extended by \(4l\).
4. A \(3\) kg particle hangs at rest from a string with natural length \(1.5\) m and \(\lambda=63\) N. Find extension and total distance below the fixed point.
5. A string has natural length \(1.6\) m and \(\lambda=80\) N. A \(2\) kg particle is held by a horizontal force \(12\) N with \(OP\) at angle \(\alpha\) to the vertical. Find \(\alpha\) and \(OP\).
6. Springs \(PQ\) and \(QR\) are fixed \(3.6\) m apart. \(PQ\): \(l=1.2\), \(\lambda=18\). \(QR\): \(l=1.8\), \(\lambda=24\). Find the tension.
7. Two identical springs each have natural length \(a\), modulus \(3mg\), fixed \(5a\) apart vertically, with mass \(m\) at the join. Assuming both are stretched, find distance below the top fixed point.
8. A particle rests on a rough plane at \(30^\circ\), \(\mu=1/\sqrt3\), attached to a spring of natural length \(a\), modulus \(4mg\). Find the range of \(AP\).
9. A string has natural length \(0.4\) m, modulus \(16\) N, and attached mass \(1.5\) kg. It is released from length \(1.0\) m. Find initial acceleration and length at maximum speed.
10. A spring has natural length \(0.5\) m and modulus \(30\) N. Find energy stored when compressed to \(0.35\) m.
11. A \(0.8\) kg particle is attached to a string of natural length \(1.5\) m and modulus \(24\) N, released from the fixed point. Find greatest distance below it.
12. A spring has natural length \(0.75\) m and modulus \(18\) N. Find work done increasing compression from \(0.10\) m to \(0.25\) m.

# 14. Worked Solutions

## 14.1 Solution to Question 1

\[
x=1.4-0.8=0.6,
\quad T=\frac{24(0.6)}{0.8}=18\text{ N}.
\]

## 14.2 Solution to Question 2

\[
x=1.2-0.9=0.3,
\quad 15=\frac{\lambda(0.3)}{1.2}=\frac{\lambda}{4},
\quad \lambda=60\text{ N}.
\]

## 14.3 Solution to Question 3

(a) Stretched to \(4l\):

\[
x=4l-l=3l,
\quad T=\frac{60(3l)}{l}=180\text{ N}.
\]

(b) Extended by \(4l\):

\[
x=4l,
\quad T=\frac{60(4l)}{l}=240\text{ N}.
\]

## 14.4 Solution to Question 4

\[
T=3g=29.4,
\quad 29.4=\frac{63x}{1.5}.
\]

\[
29.4(1.5)=63x,
\quad x=0.7\text{ m}.
\]

Total distance:

\[
1.5+0.7=2.2\text{ m}.
\]

## 14.5 Solution to Question 5

\[
T\sin\alpha=12,
\qquad T\cos\alpha=2g.
\]

\[
\tan\alpha=\frac{12}{19.6},
\quad \alpha=31.5^\circ.
\]

\[
T=\frac{12}{\sin\alpha}=22.967\ldots.
\]

\[
22.967\ldots=\frac{80x}{1.6}=50x,
\quad x=0.45934\ldots.
\]

\[
OP=1.6+0.45934\ldots=2.06\text{ m}.
\]

## 14.6 Solution to Question 6

Total extension:

\[
3.6-(1.2+1.8)=0.6.
\]

Let extension of \(PQ\) be \(x\). Then extension of \(QR\) is \(0.6-x\).

\[
\frac{18x}{1.2}=\frac{24(0.6-x)}{1.8}.
\]

\[
15x=\frac{40}{3}(0.6-x).
\]

Using \(0.6=3/5\):

\[
45x=40\left(\frac35-x\right)=24-40x.
\]

\[
85x=24,
\quad x=\frac{24}{85}.
\]

\[
T=15x=\frac{360}{85}=\frac{72}{17}=4.24\text{ N}.
\]

## 14.7 Solution to Question 7

Total extension:

\[
5a-2a=3a.
\]

Let top extension be \(x\), bottom \(3a-x\). Equilibrium:

\[
\frac{3mgx}{a}=\frac{3mg(3a-x)}{a}+mg.
\]

Divide by \(mg\), multiply by \(a\):

\[
3x=3(3a-x)+a=10a-3x.
\]

\[
6x=10a,
\quad x=\frac{5a}{3}.
\]

Distance below top:

\[
a+x=a+\frac{5a}{3}=\frac{8a}{3}.
\]

## 14.8 Solution to Question 8

\[
R=mg\cos30^\circ=\frac{\sqrt3}{2}mg.
\]

\[
F=\mu R=\frac1{\sqrt3}\cdot\frac{\sqrt3}{2}mg=\frac12mg.
\]

\[
mg\sin30^\circ=\frac12mg.
\]

Lower extreme:

\[
T=mg,
\quad mg=\frac{4mg(L-a)}{a}.
\]

\[
1=\frac{4(L-a)}{a},
\quad a=4L-4a,
\quad 5a=4L,
\quad L=\frac{5a}{4}.
\]

Upper extreme gives \(L=a\). Hence

\[
\boxed{a\le AP\le \frac{5a}{4}}.
\]

## 14.9 Solution to Question 9

Initial extension:

\[
x=1.0-0.4=0.6.
\]

\[
T=\frac{16(0.6)}{0.4}=24.
\]

\[
24-1.5g=1.5a,
\quad 24-14.7=1.5a,
\quad a=6.20\text{ m s}^{-2}.
\]

At maximum speed, \(a=0\), so \(T=1.5g=14.7\):

\[
14.7=\frac{16x}{0.4}=40x,
\quad x=0.3675.
\]

Length:

\[
0.4+0.3675=0.768\text{ m}.
\]

## 14.10 Solution to Question 10

\[
x=0.5-0.35=0.15.
\]

\[
EPE=\frac{30(0.15)^2}{2(0.5)}=0.675\text{ J}.
\]

## 14.11 Solution to Question 11

Let greatest distance be \(1.5+x\). At lowest point, \(v=0\).

\[
0.8g(1.5+x)=\frac{24x^2}{2(1.5)}=8x^2.
\]

\[
7.84(1.5+x)=8x^2.
\]

\[
11.76+7.84x=8x^2,
\quad 8x^2-7.84x-11.76=0.
\]

Divide by \(0.08\):

\[
100x^2-98x-147=0.
\]

\[
x=\frac{98\pm\sqrt{9604+58800}}{200}
=\frac{98\pm\sqrt{68404}}{200}.
\]

Positive root:

\[
x=1.79770\ldots.
\]

Distance:

\[
1.5+x=3.30\text{ m}.
\]

## 14.12 Solution to Question 12

\[
EPE_1=\frac{18(0.10)^2}{2(0.75)}=0.12.
\]

\[
EPE_2=\frac{18(0.25)^2}{2(0.75)}=0.75.
\]

\[
W=EPE_2-EPE_1=0.75-0.12=0.630\text{ J}.
\]

# 15. Exam Technique Notes

- Start with a diagram.
- Identify \(x\) before using Hooke's Law.
- Convert cm to m before substituting.
- Decide whether the force is tension, thrust or zero.
- Use \(\sum F=0\) for statics.
- Use \(F=ma\) for acceleration.
- Use energy for speeds, distances and work.
- Maximum speed: \(a=0\).
- Greatest displacement: \(v=0\).
- If a midpoint string is split, halve natural length but keep modulus the same.
- In slope problems, friction opposes impending motion.
- Round only at the final line unless instructed otherwise.

# 16. Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---|---|
| `FAS2-HOOKE-LO001` | Yes | Hooke's Law, extension/compression, modulus of elasticity, tension/thrust |
| `FAS2-HOOKE-LO002` | Yes | Light strings/springs, elastic limit, strings cannot compress, modelling limitations |
| `FAS2-WENG-LO001` | Partly | Work done against resistance and external work in linked examples |
| `FAS2-WENG-LO002` | Yes | Derivation of EPE using integration |
| `FAS2-WENG-LO003` | Yes | KE, GPE and EPE in examples |
| `FAS2-WENG-LO004` | Yes | Conservation of energy and work-energy examples |

## Off-Spec Content Found but Excluded

| Content | Decision |
|---|---|
| Full Young's modulus physics treatment | Excluded from core; warning only |
| STEP III extension problem | Excluded from core; optional enrichment only |
| Detailed moments with elastic strings | Excluded until later topic evidence supports it |
| Padlet/navigation frames | Excluded as non-mathematical evidence |

## Missing Evidence Log

| Missing evidence | Consequence |
|---|---|
| Official CCEA Hooke's Law past-paper questions | Practice questions are generated, not past-paper |
| Clean source diagrams for every screenshot | Some diagrams are AI-proposed reconstructions |
| Full Pearson textbook chapter | Only supplied slide extracts/transcript are used |

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements:

- force-extension graph with elastic limit;
- string versus spring comparison grid;
- extension versus total length strip diagram;
- two-spring series diagram;
- midpoint string geometry diagram;
- energy bar model;
- Hooke's Law calculator;
- wording trap checker;
- energy equation builder;
- friction direction selector.

These are proposed enhancements, not evidence-backed original diagrams.

# 18. Supplementary Sources Used

Project Sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`

Lesson-specific sources used:

- `FM1-Chp3-Elastic Strings and Springs.pdf`
- `transcripts.md`
- `Chapter_3_Elastic_Strings_&_Springs_🎯_(Further_Mechanics_1)_screenshots.pdf`

Ordinary A-Level Maths bridge sources used:

- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

Ordinary A-Level Maths sources are labelled as bridge context only, not Further Maths authority.

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] Draw force diagrams.
- [ ] Resolve forces horizontally and vertically.
- [ ] Resolve forces on a slope.
- [ ] Use \(F=ma\).
- [ ] Use \(F=\mu R\) at limiting equilibrium.
- [ ] Use \(KE=\frac12mv^2\) and \(GPE=mgh\).
- [ ] Convert cm to m.

## Further Maths method

- [ ] State \(T=\lambda x/l\).
- [ ] Define \(\lambda\), \(x\), and \(l\).
- [ ] Explain why \(\lambda\) has units newtons.
- [ ] Distinguish extension from total length.
- [ ] Explain why springs can compress but strings cannot.
- [ ] Use Hooke's Law with equilibrium and \(F=ma\).
- [ ] Solve two-spring problems.
- [ ] Use \(EPE=\lambda x^2/(2l)\).

## Exam technique

- [ ] Did I define \(x\) clearly?
- [ ] Did I use natural length in the denominator?
- [ ] Did I use metres?
- [ ] Did I decide tension/thrust/slack?
- [ ] Did I add natural length back on if total length is requested?
- [ ] Did I use \(a=0\) for maximum speed?
- [ ] Did I use \(v=0\) for greatest displacement?
- [ ] Did I include work against resistance?
- [ ] Did I include units?
