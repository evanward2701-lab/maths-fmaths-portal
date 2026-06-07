# AS2 Forces and Newton's Laws: Forces and Motion

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS2 |
| Unit name | AS 2 Applied Mathematics |
| Applied section | Mechanics |
| Topic code | AS2-FORCES |
| Topic name | Forces and Newton's laws |
| Topic slug | forces_and_newtons_laws |
| Topic Pascal | ForcesAndNewtonsLaws |
| Topic ID | AS2ForcesAndNewtonsLaws |
| Lesson file | AS2_forces_and_newtons_laws_lesson.md |
| Evidence chapter | Chapter 10: Forces and Motion |
| Phase | Phase 1: Main Lesson Markdown |

## Evidence Map

| Evidence source | Role in lesson | Notes |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Authority for unit, topic code, LO IDs and boundaries | Used to identify AS2-FORCES and LO001 to LO013. |
| Project module map | Metadata rules and file naming rules | Used for unit/topic ID and output file conventions. |
| Project evidence checklist | Evidence completeness and missing-evidence logging | Used to control source priority and off-spec logging. |
| `MechYr1-Chp10-ForcesAndMotion.pdf` | Slide evidence | Supplies diagrams, examples and structure. |
| `Chapter_10_Forces_🚀_(Applied_Year_1,_Mechanics)_Transcript.md` | Teacher transcript | Supplies explanations, worked-example reasoning and warnings. |
| `Chapter_10_Forces_🚀_(Applied_Year_1,_Mechanics)_Screenshots.pdf` | Visual screenshot evidence | Parsed text unavailable; only visible/slide-supported content used. |

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| AS2-FORCES-LO001 | Newton's first law, concept of a force, equilibrium and balanced forces. |
| AS2-FORCES-LO002 | Resolving forces horizontally, vertically and through vector components. |
| AS2-FORCES-LO003 | Addition of forces to find resultants, including vector resultants. |
| AS2-FORCES-LO004 | Newton's second law, including forces given as 2D vectors. |
| AS2-FORCES-LO005 | Gravitational acceleration, using `g=9.8 m s^{-2}` unless told otherwise. |
| AS2-FORCES-LO006 | Weight and motion in a straight line under gravity. |
| AS2-FORCES-LO007 | Newton's third law in contact-force and lift problems. |
| AS2-FORCES-LO008 | Connected particles, strings, tensions and pulleys. |
| AS2-FORCES-LO009 | Equilibrium of forces on a particle. |
| AS2-FORCES-LO010 | Logged as missing: no supplied evidence for `F <= mu R`. |
| AS2-FORCES-LO011 | Logged as missing: no supplied evidence for coefficient of friction. |
| AS2-FORCES-LO012 | Partially covered: rough surfaces with a given constant friction/resistance. |
| AS2-FORCES-LO013 | Logged as missing: no supplied evidence for limiting friction/statics. |

## Learning Objectives

By the end of this lesson, you should be able to:

1. Draw a clear force diagram for one particle at a time.
2. Identify weight, normal reaction, tension, friction/resistance and applied forces.
3. Use Newton's first law to recognise equilibrium.
4. Resolve forces vertically and horizontally.
5. Find resultant forces from scalar diagrams and vector forces.
6. Use `F=ma`, remembering that `F` means **resultant force**.
7. Use `W=mg` and `g=9.8 m s^{-2}`.
8. Combine `F=ma` with constant-acceleration formulae.
9. Use vector equations of motion in two dimensions.
10. Set up connected-particle equations using common acceleration and tension.
11. Use Newton's third law without cancelling forces acting on different bodies.
12. Model pulley systems using separate equations for each particle.

## Prerequisite Recap

Earlier A-Level mechanics and pure mathematics needed here:

\[
v=u+at, \qquad s=ut+\frac12at^2, \qquad v^2=u^2+2as.
\]

Vector notation:

\[
\begin{pmatrix}a\\b\end{pmatrix}=a\mathbf{i}+b\mathbf{j}.
\]

Vector magnitude:

\[
\left|\begin{pmatrix}a\\b\end{pmatrix}\right|=\sqrt{a^2+b^2}.
\]

For a direction/bearing problem, use right-triangle trigonometry such as

\[
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}.
\]

## Big Picture Explanation

Kinematics describes how objects move. Forces explain why motion changes. The central bridge is

\[
\boxed{F=ma},
\]

but the letter `F` is not any force from the diagram. It is the **resultant force in the chosen direction**.

That gives the usual mechanics chain:

\[
\text{force diagram}\rightarrow F=ma\rightarrow a\rightarrow \text{SUVAT}.
\]

## Key Definitions and Notation

### Particle model

A particle is a model of an object as a point with negligible dimensions. We ignore size and shape and focus on mass and the forces acting on it.

### Force

A force is an interaction that can change the motion of a body. Force is measured in newtons, N.

### Weight

Weight is the force due to gravity:

\[
\boxed{W=mg}.
\]

Weight always acts vertically downwards. Mass is measured in kg; weight is measured in N.

### Normal reaction

The normal reaction is the contact force from a surface on a body. It acts perpendicular to the surface. It is often written as `R`.

### Tension

Tension is the pulling force in a string, rope or cable. Tension acts away from the particle along the direction of the string. It is usually written as `T`.

### Friction or resistance

Friction or resistance acts against motion or attempted motion. In this evidence, friction is usually given directly as a constant force. The model `F <= mu R` is not taught from this evidence and is logged as missing.

### Resultant force

The resultant force is the overall force acting on a body in a chosen direction. If forces are balanced,

\[
\text{resultant force}=0.
\]

If the resultant force is not zero, the object accelerates in the direction of the resultant force.

### Resolving forces

To resolve forces means to calculate the net force in a chosen direction. For example,

\[
R(\uparrow): 40-5=35\text{ N}, \qquad R(\rightarrow):30-30=0\text{ N}.
\]

### Equilibrium

A particle is in equilibrium when the resultant force is zero. It may be at rest or moving with constant velocity.

### Newton's first law

An object at rest stays at rest, and an object moving with constant velocity continues at that velocity, unless an unbalanced force acts. In this lesson:

\[
\text{no acceleration}\iff \text{forces are balanced}.
\]

### Newton's second law

\[
\boxed{F=ma}
\]

where `F` is the resultant force, `m` is mass, and `a` is acceleration. The force and acceleration must be in the same chosen direction.

### Newton's third law

For every action there is an equal and opposite reaction. Equal and opposite forces act on **different objects**.

## Core Theory

### 1. Drawing force diagrams

A force diagram should be drawn from the point of view of the body being considered. Consider the forces acting on each object one at a time.

For a block on a rough horizontal surface being pulled to the right, the typical forces are:

- weight `W=mg` vertically downwards;
- normal reaction `R` vertically upwards;
- pulling force or tension to the right;
- friction or resistance to the left.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-001 | Source: MechYr1 Chapter 10 slide page 3 + transcript Forces 1 | Insert from svg/AS2ForcesAndNewtonsLawsSVG-001.svg | Purpose: Show a free-body diagram with `R`, `W`, `T/P`, and friction/resistance.]

### 2. Direction conventions

- Weight always acts vertically downwards.
- Normal reaction is perpendicular to the surface.
- Tension acts away from the body along the string.
- Friction/resistance opposes motion or attempted motion.
- Acceleration is often marked with a double arrow.

### 3. Resultant force in one direction

For a particle with `40 N` upwards, `5 N` downwards, `30 N` left and `30 N` right:

\[
R(\uparrow)=40-5=35\text{ N},
\]

\[
R(\rightarrow)=30-30=0\text{ N}.
\]

So the resultant is `35 N upwards`.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-002 | Source: MechYr1 Chapter 10 slide page 3 | Insert from svg/AS2ForcesAndNewtonsLawsSVG-002.svg | Purpose: Show resolved resultant force from vertical and horizontal forces.]

### 4. Negative resultants

A negative resultant tells you the actual resultant is in the opposite direction to the direction chosen positive.

Example:

\[
R(\uparrow)=4-6=-2\text{ N},
\]

so the resultant is `2 N downwards`.

### 5. Equilibrium

If a particle is stationary or moving with constant velocity, there is no acceleration. Therefore

\[
F=ma=m(0)=0.
\]

So forces are balanced:

\[
\text{forces up}=\text{forces down}, \qquad \text{forces left}=\text{forces right}.
\]

### 6. Forces as vectors

Forces have magnitude and direction, so they can be written as vectors:

\[
2\mathbf{i}+3\mathbf{j}=\begin{pmatrix}2\\3\end{pmatrix}.
\]

The resultant of forces written as vectors is found by adding the vectors component by component. If the particle is in equilibrium, the resultant is

\[
\begin{pmatrix}0\\0\end{pmatrix}.
\]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-003 | Source: MechYr1 Chapter 10 slide page 5 | Insert from svg/AS2ForcesAndNewtonsLawsSVG-003.svg | Purpose: Add vector forces and find magnitude and bearing.]

### 7. Newton's second law as the bridge to motion

Use

\[
F=ma,
\]

where `F` is the resultant force in the direction of acceleration. Then use the acceleration in SUVAT if the question asks for distance, speed or time.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-004 | Source: MechYr1 Chapter 10 slide pages 8 to 10 + transcript Forces 5 and 6 | Insert from svg/AS2ForcesAndNewtonsLawsSVG-004.svg | Purpose: Show `F=ma` as resultant force equals mass times acceleration.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-005 | Source: Combining `F=ma` with SUVAT slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-005.svg | Purpose: Show acceleration as the bridge between force and kinematics.]

### 8. Vector `F=ma`

Because force and acceleration are vectors,

\[
\mathbf{F}=m\mathbf{a}.
\]

For example, if

\[
\mathbf{F}=\begin{pmatrix}3\\8\end{pmatrix}\text{ N},\qquad m=0.5\text{ kg},
\]

then

\[
\begin{pmatrix}3\\8\end{pmatrix}=0.5\mathbf{a}
\]

so

\[
\mathbf{a}=\begin{pmatrix}6\\16\end{pmatrix}\text{ m s}^{-2}.
\]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-006 | Source: Motion in 2 dimensions slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-006.svg | Purpose: Show `F=ma` with vectors.]

### 9. Connected particles

For particles connected by a light inextensible string:

- light means the mass of the string is negligible;
- inextensible means the string does not stretch;
- connected particles have the same acceleration magnitude;
- the tension is the same throughout one light string.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-007 | Source: Connected particles slides | Insert from svg/AS2ForcesAndNewtonsLawsSVG-007.svg | Purpose: Show two connected particles on a rough horizontal plane.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-012 | Source: Connected particles transcript and slide pages 15 to 16 | Insert from svg/AS2ForcesAndNewtonsLawsSVG-012.svg | Purpose: Show same acceleration and equal tension assumptions.]

### 10. Newton's third law

If body `A` exerts a force on body `B`, then body `B` exerts a force on body `A` that has the same magnitude and opposite direction. The forces act on different bodies.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-008 | Source: Newton's third law slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-008.svg | Purpose: Show equal and opposite forces acting on different bodies.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-013 | Source: Newton's third law scale-pan example | Insert from svg/AS2ForcesAndNewtonsLawsSVG-013.svg | Purpose: Show contact force diagram for stacked masses.]

### 11. Lift problems

In lift problems, decide the acceleration direction, not just the direction of motion. A lift moving upwards but decelerating has downward acceleration.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-009 | Source: Lift examples in transcript | Insert from svg/AS2ForcesAndNewtonsLawsSVG-009.svg | Purpose: Show lift tension and normal reaction diagrams.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-014 | Source: Lift transcript | Insert from svg/AS2ForcesAndNewtonsLawsSVG-014.svg | Purpose: Distinguish direction of motion from acceleration.]

### 12. Pulleys

A pulley is a wheel over which a string, rope or cable passes. In this evidence:

- smooth pulley means tension is the same on both sides;
- light inextensible string means the particles have equal acceleration magnitude;
- tension acts away from each object along the string;
- for two hanging masses, write separate equations because the particles move in different directions.

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-010 | Source: Pulleys slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-010.svg | Purpose: Show two masses connected over a smooth pulley.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-011 | Source: Horizontal and vertical string slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-011.svg | Purpose: Show pulley-on-table force diagram.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-015 | Source: Pulley example with unknown k | Insert from svg/AS2ForcesAndNewtonsLawsSVG-015.svg | Purpose: Show masses `km` and `3m` over a pulley.]

[VISUAL PLACEHOLDER: AS2ForcesAndNewtonsLawsSVG-016 | Source: Horizontal and vertical string subsequent motion slide | Insert from svg/AS2ForcesAndNewtonsLawsSVG-016.svg | Purpose: Show two-stage pulley-on-table motion.]

## Worked Examples

### Worked Example 1: Resultant force from a force diagram

A particle has `40 N` upwards, `5 N` downwards, `30 N` left and `30 N` right. Find the resultant force.

**Solution**

Resolve vertically:

\[
R(\uparrow)=40-5=35.
\]

Resolve horizontally:

\[
R(\rightarrow)=30-30=0.
\]

Therefore the resultant force is

\[
\boxed{35\text{ N upwards}}.
\]

### Worked Example 2: Unknown horizontal force

A particle has `5 N` upwards, `5 N` downwards, `3 N` left and `P N` right. Find the resultant.

\[
R(\uparrow)=5-5=0.
\]

\[
R(\rightarrow)=P-3.
\]

So the resultant is

\[
\boxed{(P-3)\text{ N to the right}}.
\]

If `P<3`, this expression is negative, so the actual resultant is leftwards.

### Worked Example 3: Diagonal resultant

Forces are `4 N` upwards, `6 N` downwards, `7 N` left, `2 N` right and `3 N` right.

Vertical resolving:

\[
R(\uparrow)=4-6=-2,
\]

so the vertical resultant is `2 N downwards`.

Horizontal resolving leftwards:

\[
R(\leftarrow)=7-2-3=2,
\]

so the horizontal resultant is `2 N leftwards`.

Magnitude, if required:

\[
|R|=\sqrt{2^2+2^2}=2\sqrt2\text{ N}.
\]

Direction is `45° down-left`.

### Worked Example 4: Vector forces in equilibrium

Forces

\[
2\mathbf{i}+3\mathbf{j},\quad 4\mathbf{i}-\mathbf{j},\quad -3\mathbf{i}+2\mathbf{j},\quad a\mathbf{i}+b\mathbf{j}
\]

act on an object in equilibrium. Find `a` and `b`.

Because the object is in equilibrium,

\[
\begin{pmatrix}2\\3\end{pmatrix}
+\begin{pmatrix}4\\-1\end{pmatrix}
+\begin{pmatrix}-3\\2\end{pmatrix}
+\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}0\\0\end{pmatrix}.
\]

Top components:

\[
2+4-3+a=0,
\]

\[
3+a=0,
\]

\[
a=-3.
\]

Bottom components:

\[
3-1+2+b=0,
\]

\[
4+b=0,
\]

\[
b=-4.
\]

Therefore

\[
\boxed{a=-3,\quad b=-4}.
\]

### Worked Example 5: Vector resultant, magnitude and bearing

Forces

\[
2\mathbf{i}+\mathbf{j},\quad 3\mathbf{i}-2\mathbf{j},\quad -\mathbf{i}+4\mathbf{j}
\]

act on a particle. The vector `i` is east and `j` is north. Find the resultant force, magnitude and bearing.

Add vectors:

\[
\begin{pmatrix}2\\1\end{pmatrix}
+\begin{pmatrix}3\\-2\end{pmatrix}
+\begin{pmatrix}-1\\4\end{pmatrix}
=\begin{pmatrix}4\\3\end{pmatrix}.
\]

So

\[
\mathbf{R}=4\mathbf{i}+3\mathbf{j}.
\]

Magnitude:

\[
|\mathbf{R}|=\sqrt{4^2+3^2}=5\text{ N}.
\]

Let `theta` be the angle above east:

\[
\tan\theta=\frac34,
\]

\[
\theta=36.9^\circ.
\]

Bearing:

\[
90^\circ-36.9^\circ=53.1^\circ.
\]

So the bearing is

\[
\boxed{053.1^\circ}.
\]

### Worked Example 6: Car with driving and resisting forces

A car of mass `2000 kg` has a driving force of `800 N` and resisting forces of `200 N`. Determine its acceleration.

Resolve to the right:

\[
800-200=2000a.
\]

\[
600=2000a.
\]

\[
a=\frac{600}{2000}=0.3.
\]

\[
\boxed{a=0.3\text{ m s}^{-2}}.
\]

### Worked Example 7: Weight of a child

A child has mass `50 kg`. Find their weight.

\[
W=mg=50g=50(9.8)=490.
\]

\[
\boxed{W=490\text{ N}}.
\]

### Worked Example 8: Falling sheep with air resistance

A sheep of mass `70 kg` falls with air resistance `300 N`. Find its acceleration.

Resolve downwards:

\[
70g-300=70a.
\]

\[
70(9.8)-300=70a.
\]

\[
686-300=70a.
\]

\[
386=70a.
\]

\[
a=\frac{386}{70}=5.514285\ldots
\]

\[
\boxed{a=5.51\text{ m s}^{-2}\text{ downwards}}.
\]

### Worked Example 9: `F=ma` with SUVAT

A `5 kg` body is pulled along a rough horizontal table by a `20 N` force against a constant friction force of `4 N`. It starts from rest. Find acceleration, distance travelled in 4 seconds, and normal reaction.

Resolve horizontally:

\[
20-4=5a.
\]

\[
16=5a.
\]

\[
a=3.2\text{ m s}^{-2}.
\]

Use SUVAT:

\[
u=0,\quad a=3.2,\quad t=4.
\]

\[
s=ut+\frac12at^2.
\]

\[
s=(0)(4)+\frac12(3.2)(4^2).
\]

\[
s=25.6\text{ m}.
\]

Vertical forces are balanced:

\[
R=5g=5(9.8)=49\text{ N}.
\]

### Worked Example 10: Object sinking into soft ground

A `4 kg` particle reaches the ground with speed `28 m s^{-1}`, then sinks into soft ground before coming to rest. The ground exerts a constant resistance of `5000 N`. Find the sinking distance.

Take downwards as positive. Forces while sinking:

\[
4g-5000=4a.
\]

\[
4(9.8)-5000=4a.
\]

\[
39.2-5000=4a.
\]

\[
-4960.8=4a.
\]

\[
a=-1240.2\text{ m s}^{-2}.
\]

Use SUVAT:

\[
u=28,\quad v=0,\quad a=-1240.2.
\]

\[
v^2=u^2+2as.
\]

\[
0=28^2+2(-1240.2)s.
\]

\[
0=784-2480.4s.
\]

\[
s=\frac{784}{2480.4}=0.316078\ldots
\]

\[
\boxed{s=0.316\text{ m}}.
\]

### Worked Example 11: Vector `F=ma`

A force `(3i+8j) N` acts on a particle of mass `0.5 kg`.

\[
\begin{pmatrix}3\\8\end{pmatrix}=0.5\mathbf{a}.
\]

\[
\mathbf{a}=\begin{pmatrix}6\\16\end{pmatrix}=6\mathbf{i}+16\mathbf{j}.
\]

Magnitude:

\[
|\mathbf{a}|=\sqrt{6^2+16^2}=17.1\text{ m s}^{-2} \quad (3\text{ s.f.}).
\]

Bearing:

\[
\theta=\tan^{-1}\left(\frac{16}{6}\right)=69.443\ldots^\circ.
\]

\[
\text{bearing}=90^\circ-69.443\ldots^\circ=020.6^\circ.
\]

### Worked Example 12: Unknowns in vector forces

A boat of mass `60 kg` is acted on by

\[
\mathbf{F}_1=\begin{pmatrix}80\\50\end{pmatrix},\quad
\mathbf{F}_2=\begin{pmatrix}10p\\20q\end{pmatrix},\quad
\mathbf{F}_3=\begin{pmatrix}-75\\100\end{pmatrix}.
\]

The acceleration is

\[
\begin{pmatrix}0.8\\-1.5\end{pmatrix}.
\]

Resultant force:

\[
\begin{pmatrix}80\\50\end{pmatrix}
+\begin{pmatrix}10p\\20q\end{pmatrix}
+\begin{pmatrix}-75\\100\end{pmatrix}
=\begin{pmatrix}5+10p\\150+20q\end{pmatrix}.
\]

Use `F=ma`:

\[
\begin{pmatrix}5+10p\\150+20q\end{pmatrix}
=60\begin{pmatrix}0.8\\-1.5\end{pmatrix}
=\begin{pmatrix}48\\-90\end{pmatrix}.
\]

Top components:

\[
5+10p=48,
\]

\[
10p=43,
\]

\[
p=4.3.
\]

Bottom components:

\[
150+20q=-90,
\]

\[
20q=-240,
\]

\[
q=-12.
\]

### Worked Example 13: Connected particles on a rough horizontal plane

Particles `P` and `Q` of masses `5 kg` and `3 kg` are connected by a light inextensible string. `P` is pulled by a `40 N` force. `P` has friction `10 N`; `Q` has friction `6 N`. Find acceleration and tension.

Whole system:

\[
40-10-6=8a.
\]

\[
24=8a.
\]

\[
a=3\text{ m s}^{-2}.
\]

Consider `P`:

\[
40-T-10=5(3).
\]

\[
30-T=15.
\]

\[
T=15\text{ N}.
\]

Modelling assumptions: inextensible gives same acceleration; light gives same tension throughout one string and negligible string mass.

### Worked Example 14: Scale pan and Newton's third law

A light scale pan carries masses `A=0.4 kg` and `B=0.6 kg`. The system accelerates upwards at `0.5 m s^{-2}`.

Whole system for tension:

\[
T-1g=1(0.5).
\]

\[
T=9.8+0.5=10.3\text{ N}.
\]

Consider mass `A` to find the contact force `R` from `B` on `A`:

\[
R-0.4g=0.4(0.5).
\]

\[
R=0.4(9.8)+0.2=3.92+0.2=4.12\text{ N}.
\]

By Newton's third law, force exerted on `B` by `A` has magnitude `4.12 N`, downwards on `B`.

If `S` is the force exerted on `B` by the scale pan:

\[
S-0.6g-4.12=0.6(0.5).
\]

\[
S=0.6(9.8)+4.12+0.3=5.88+4.12+0.3=10.3\text{ N}.
\]

### Worked Example 15: Lift moving upwards but decelerating

A woman of mass `50 kg` is in a lift of mass `950 kg`. The lift moves upwards but decelerates at `2 m s^{-2}`. Find the cable tension and the reaction on the woman.

Take upwards as positive. Since the lift is moving upwards and decelerating,

\[
a=-2.
\]

Whole system mass:

\[
950+50=1000\text{ kg}.
\]

Cable tension:

\[
T-1000g=1000(-2).
\]

\[
T=1000g-2000=9800-2000=7800\text{ N}.
\]

Woman alone:

\[
R-50g=50(-2).
\]

\[
R=50g-100=490-100=390\text{ N}.
\]

### Worked Example 16: Two hanging particles over a pulley

Particles have masses `2m` and `3m`, connected by a light inextensible string over a smooth fixed pulley. The system is released from rest.

Let `3m` move down and `2m` move up with acceleration `a`.

For `2m`, upwards positive:

\[
T-2mg=2ma.
\]

For `3m`, downwards positive:

\[
3mg-T=3ma.
\]

Add:

\[
(T-2mg)+(3mg-T)=2ma+3ma.
\]

\[
mg=5ma.
\]

\[
a=\frac{g}{5}.
\]

Tension:

\[
T=2ma+2mg=2m\left(\frac{g}{5}\right)+2mg=\frac{2mg}{5}+\frac{10mg}{5}=\frac{12mg}{5}.
\]

Force on the pulley by the string:

\[
2T=\frac{24mg}{5}.
\]

Distance in 4 seconds from rest:

\[
s=ut+\frac12at^2=0+\frac12\left(\frac{g}{5}\right)(4^2)=\frac{8g}{5}=15.7\text{ m}\quad (g=9.8).
\]

### Worked Example 17: Pulley with unknown mass ratio

Particles `P` and `Q` have masses `km` and `3m`, with `k<3`. `Q` descends with acceleration `g/3`. Find `T` and `k`.

For `Q`, downwards positive:

\[
3mg-T=3m\left(\frac13g\right).
\]

\[
3mg-T=mg.
\]

\[
T=2mg.
\]

For `P`, upwards positive:

\[
T-kmg=km\left(\frac13g\right).
\]

Substitute `T=2mg`:

\[
2mg-kmg=\frac13kmg.
\]

Divide by `mg`:

\[
2-k=\frac13k.
\]

\[
2=\frac43k.
\]

\[
k=\frac32.
\]

### Worked Example 18: Pulley on table with subsequent motion

Particle `A` has mass `0.4 kg` and lies on a rough horizontal table. Particle `B` has mass `0.8 kg` and hangs freely. The friction on `A` is `0.08g N`. `B` is initially `0.5 m` above the ground. The system starts from rest.

While the string is taut:

For `A`, towards the pulley:

\[
T-0.08g=0.4a.
\]

For `B`, downwards:

\[
0.8g-T=0.8a.
\]

Add:

\[
0.72g=1.2a.
\]

\[
a=0.6g=5.88\text{ m s}^{-2}.
\]

Time for `B` to reach ground:

\[
s=0.5,\quad u=0,\quad a=5.88.
\]

\[
0.5=\frac12(5.88)t^2.
\]

\[
0.5=2.94t^2.
\]

\[
t=0.412393\ldots\approx0.41\text{ s}.
\]

Speed at that instant:

\[
v=u+at=5.88(0.412393\ldots)=2.42487\ldots\text{ m s}^{-1}.
\]

After `B` reaches the ground, the string becomes slack. `A` is slowed by friction only. For `A`:

\[
-0.08g=0.4a.
\]

\[
a=-0.2g=-1.96\text{ m s}^{-2}.
\]

Use SUVAT for the second stage:

\[
v^2=u^2+2as.
\]

\[
0=(2.42487\ldots)^2+2(-1.96)s.
\]

\[
0=5.88-3.92s.
\]

\[
s=1.5\text{ m}.
\]

Stage 1 distance for `A` is `0.5 m`, so total distance is

\[
0.5+1.5=2.0\text{ m}.
\]

## Guided Practice

1. A particle has forces `12 N` right, `5 N` left, `9 N` up and `9 N` down. Find the resultant.
2. A particle is stationary. It has `P N` right, `18 N` left, `R N` up and `4g N` down. Find `P` and `R`.
3. Forces `(4,-1)`, `(-2,5)` and `(a,b)` act on a particle in equilibrium. Find `a` and `b`.
4. A `12 kg` body is pulled by `50 N` with resistance `14 N`. Find acceleration.
5. A `6 kg` particle is pulled from rest by a resultant force of `18 N`. Find acceleration and distance travelled in 5 seconds.
6. A `4 kg` particle is acted on by resultant force `(20,-12) N`. Find acceleration vector.
7. Two particles of masses `4 kg` and `6 kg` are connected by a light inextensible string. A `40 N` force pulls the `6 kg` particle forwards. Resistances are `3 N` and `7 N`. Find acceleration and tension.
8. A `70 kg` person stands in a lift accelerating upwards at `1.5 m s^{-2}`. Find the normal reaction.

## Common Mistakes and Exam Traps

1. Using `F=ma` with one force instead of the resultant force.
2. Confusing mass and weight.
3. Putting weight along a string or slope. Weight is vertical.
4. Drawing normal reaction vertically on a non-horizontal surface. It must be perpendicular to the surface.
5. Thinking Newton's third law forces cancel on one body. They act on different bodies.
6. Forgetting deceleration means acceleration opposite to motion.
7. Treating pulley particles as one horizontal system.
8. Forgetting the second stage when a string becomes slack after a hanging mass reaches the ground.

## Exam Technique Notes

- Start with a diagram.
- Mark acceleration clearly.
- Resolve in the direction of acceleration where possible.
- Write one clear equation of motion, such as `20-4=5a`.
- Leave `g` as `g` in symbolic pulley problems until late.
- Explain modelling assumptions precisely: light, inextensible, smooth and particle.

## Full Worked Solutions to Guided Practice

### Solution 1

\[
R(\rightarrow)=12-5=7,\qquad R(\uparrow)=9-9=0.
\]

\[
\boxed{7\text{ N to the right}}.
\]

### Solution 2

Stationary means equilibrium.

\[
P=18,\qquad R=4g=39.2\text{ N}.
\]

### Solution 3

\[
\begin{pmatrix}4\\-1\end{pmatrix}+\begin{pmatrix}-2\\5\end{pmatrix}+\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.
\]

Top:

\[
4-2+a=0\Rightarrow a=-2.
\]

Bottom:

\[
-1+5+b=0\Rightarrow b=-4.
\]

### Solution 4

\[
50-14=12a.
\]

\[
36=12a.
\]

\[
\boxed{a=3\text{ m s}^{-2}}.
\]

### Solution 5

\[
18=6a\Rightarrow a=3\text{ m s}^{-2}.
\]

\[
s=ut+\frac12at^2=0(5)+\frac12(3)(5^2)=37.5\text{ m}.
\]

### Solution 6

\[
\begin{pmatrix}20\\-12\end{pmatrix}=4\mathbf{a}.
\]

\[
\mathbf{a}=\begin{pmatrix}5\\-3\end{pmatrix}=5\mathbf{i}-3\mathbf{j}.
\]

### Solution 7

Whole system:

\[
40-3-7=10a.
\]

\[
30=10a.
\]

\[
a=3\text{ m s}^{-2}.
\]

For the `4 kg` particle:

\[
T-3=4(3).
\]

\[
T=15\text{ N}.
\]

### Solution 8

Let `R` be the normal reaction. Resolve upwards:

\[
R-70g=70(1.5).
\]

\[
R=70(9.8)+105=686+105=791\text{ N}.
\]

## Syllabus Gap Check

| LO ID | Status | Note |
|---|---|---|
| AS2-FORCES-LO001 | Covered | Force diagrams, Newton's first law and equilibrium. |
| AS2-FORCES-LO002 | Covered | Horizontal, vertical and vector resolving. |
| AS2-FORCES-LO003 | Covered | Scalar and vector resultants. |
| AS2-FORCES-LO004 | Covered | Scalar and vector `F=ma`. |
| AS2-FORCES-LO005 | Covered | `g=9.8 m s^{-2}` and `W=mg`. |
| AS2-FORCES-LO006 | Covered | Weight and vertical motion under gravity. |
| AS2-FORCES-LO007 | Covered | Newton's third law and lift/scale-pan examples. |
| AS2-FORCES-LO008 | Covered | Connected particles and pulleys. |
| AS2-FORCES-LO009 | Covered | Equilibrium examples. |
| AS2-FORCES-LO010 | Missing | `F <= mu R` not supplied in lesson evidence. |
| AS2-FORCES-LO011 | Missing | Coefficient of friction not supplied in lesson evidence. |
| AS2-FORCES-LO012 | Partial | Rough surface motion with given constant friction only. |
| AS2-FORCES-LO013 | Missing | Limiting friction/statics not supplied in lesson evidence. |

## Visual and Interactive Asset Plan

### SVG Assets

- `svg/AS2ForcesAndNewtonsLawsSVG-001.svg` to `svg/AS2ForcesAndNewtonsLawsSVG-016.svg`

### Mermaid Assets

- `mermaid/AS2ForcesAndNewtonsLawsMermaid-001.md` to `mermaid/AS2ForcesAndNewtonsLawsMermaid-016.md`

### TikZ Assets

- `tikz/AS2ForcesAndNewtonsLawsTikZ-001.tex` to `tikz/AS2ForcesAndNewtonsLawsTikZ-016.tex`

### Widgets

- `widgets/AS2ForcesAndNewtonsLawsWidget-001.html`
- `widgets/AS2ForcesAndNewtonsLawsWidget-002.html`
- `widgets/AS2ForcesAndNewtonsLawsWidget-003.html`
- `widgets/AS2ForcesAndNewtonsLawsWidget-004.html`

## Supplementary Sources Used

Cross-board labels in the evidence, including Edexcel/Pearson references, are not treated as CCEA authority. They are used only where the mathematics matches the CCEA AS2-FORCES boundary. Promotional and extension references are excluded from the core lesson.

## Final Student Checklist

### Force diagrams

- [ ] I can draw one force diagram for one object at a time.
- [ ] I can label weight `mg` vertically downwards.
- [ ] I can label normal reaction perpendicular to the surface.
- [ ] I can label tension away from the object along the string.
- [ ] I can label friction/resistance against motion.

### Newton's laws

- [ ] I know equilibrium means zero resultant force.
- [ ] I know `F=ma` uses resultant force.
- [ ] I can use Newton's third law without cancelling forces acting on different bodies.

### Calculations

- [ ] I can resolve forces horizontally and vertically.
- [ ] I can add vector forces.
- [ ] I can find acceleration from resultant force.
- [ ] I can combine `F=ma` with SUVAT.
- [ ] I can use `W=mg`.

### Connected particles and pulleys

- [ ] I know light string, inextensible string and smooth pulley assumptions.
- [ ] I can form equations of motion for connected particles.
- [ ] I can add equations to eliminate tension where appropriate.
- [ ] I can handle pulley particles moving in different directions.

### Gaps to revise later

- [ ] `F <= mu R`.
- [ ] Coefficient of friction `mu`.
- [ ] Limiting friction and statics.
