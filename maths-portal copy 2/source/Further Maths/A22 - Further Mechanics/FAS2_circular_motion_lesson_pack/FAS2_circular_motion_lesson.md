# Circular Motion and Further Circular Motion

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Applied section | Section A: Mechanics 1 plus Section B: Mechanics 2 |
| Topic code | `FAS2-CM` and `FAS2-FCM` |
| Topic name | Circular motion and Further circular motion |
| Topic slug | `circular_motion` |
| Topic Pascal | `CircularMotion` |
| Topic ID | `FAS2CircularMotion` |
| Lesson file name | `FAS2_circular_motion_lesson.md` |
| LO IDs | `FAS2-CM-LO001`, `FAS2-CM-LO002`, `FAS2-CM-LO003`, `FAS2-FCM-LO001` |
| Bridge tags | `#Radians`, `#Kinematics`, `#Forces`, `#NewtonSecondLaw`, `#WorkEnergy`, `#Projectiles`, `#ResolvingForces` |
| Topic tags | `#FAS2`, `#CircularMotion`, `#HorizontalCircles`, `#VerticalCircles`, `#AngularSpeed`, `#RadialAcceleration`, `#ConicalPendulum`, `#BankedCorners`, `#Energy`, `#MechanicsRoute` |

## Boundary Statement

This lesson is a combined CCEA FAS2 mechanics-route chapter because the supplied evidence covers both:

- `FAS2-CM`: horizontal circular motion;
- `FAS2-FCM`: vertical circular motion.

The CCEA specification map remains the authority. Cross-board Edexcel material in the supplied evidence is used only where it matches these CCEA learning outcomes. Sliding and overturning on banked corners are not core here because they belong to `FA22-FCM-LO001`.

# 2. Evidence Map

| Evidence source | How it is used in this lesson |
|---|---|
| CCEA Further Mathematics specification map | Determines unit, section, topic codes, LO IDs and boundaries. |
| Further Maths module map | Confirms bridge links: radians, kinematics, forces, FAS2 circular motion, work-energy. |
| Further Maths evidence checklist | Used as intake checklist. |
| `FM2-Chp1-Circular Motion_v200111.pdf` | Lesson-specific mathematical content, worked examples, diagrams and warnings. |
| `Chapter_1_Circular_Motion_🚗_(Further_Mechanics_2)_screenshots.pdf` | Visual evidence for annotated slides and teacher diagram additions where visible. |
| `transcripts.md` | Teacher phrasing and detailed explanation, especially angular speed, \(v=r\omega\), and vertical-circle reasoning. |
| Ordinary A-Level Maths bridge extracts | Bridge context only. Does not override CCEA Further Maths. |

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-CM-LO001` | demonstrate understanding of the concept of angular speed for a particle moving in a circle, and use the relation \(v=r\omega\) | Defines angular speed, radians per second, \(\omega\), revolution conversions, and derives \(v=r\omega\) from \(s=r\theta\). | CCEA map, PDF angular speed slides, transcript derivation. | Core. | Radians, arc length, differentiation of displacement. |
| `FAS2-CM-LO002` | demonstrate understanding that the acceleration of a particle moving in a circle with constant speed is directed towards the centre of the circle, and use \(a=r\omega^2\) and \(a=v^2/r\) | Derives/uses radial acceleration, explains acceleration despite constant speed, gives unit-aware examples. | CCEA map, PDF acceleration slides. | Core. | Velocity/acceleration, Newton’s second law. |
| `FAS2-CM-LO003` | solve problems that can be modelled by the motion of a particle moving in a horizontal circle with constant speed, including the conical pendulum and banked corners, but excluding sliding or overturning problems | Covers horizontal force models, friction, conical pendulum, banked corner without friction, two-string horizontal circle model. | CCEA map, PDF examples. | Core except sliding/overturning. | Resolving forces, friction, reaction, tension. |
| `FAS2-FCM-LO001` | solve problems involving motion in a vertical circle, including proofs of standard results | Covers non-constant speed, energy, radial \(F=ma\), tension/reaction conditions, constrained/unconstrained cases, complete-circle conditions. | CCEA map, PDF vertical-circle section, transcript. | Core. | Work-energy, projectiles, force components. |

# 4. Learning Objectives

## Core Further Maths Objectives

By the end of this lesson, you should be able to:

1. Define angular speed and use the unit \(\mathrm{rad\,s^{-1}}\).
2. Convert between revolutions, radians, seconds and minutes.
3. Use arc length \(s=r\theta\) to derive and apply
   \[
   v=r\omega.
   \]
4. Explain why a particle moving at constant speed in a circle still has acceleration.
5. Use radial acceleration formulae
   \[
   a=r\omega^2,\qquad a=\frac{v^2}{r}.
   \]
6. Resolve forces in horizontal circular motion, using the real force that provides the inward resultant.
7. Solve conical pendulum and banked-corner problems without sliding or overturning.
8. Use energy and radial \(F=ma\) in vertical-circle problems.
9. Distinguish constrained circular motion from unconstrained circular motion.
10. State the conditions for completing a circle in rod/string/wire/surface models.

## Bridge Objectives

You should be able to connect this lesson to ordinary A-Level Maths by:

1. Recalling that a full turn is \(2\pi\) radians.
2. Using \(s=r\theta\) only when \(\theta\) is in radians.
3. Differentiating displacement with respect to time to obtain speed or velocity.
4. Resolving forces into perpendicular components.
5. Applying \(F=ma\) in a chosen direction.
6. Applying conservation of energy using kinetic energy and gravitational potential energy.
7. Treating motion after leaving a circle as projectile motion.

## Exam Technique Objectives

You should be able to:

1. Convert all quantities to standard SI units before substituting.
2. Draw the acceleration arrow towards the centre, not along the direction of motion.
3. Avoid calling “centripetal force” a new force.
4. Use \(F=\mu R\) only at limiting friction.
5. Choose \(a=r\omega^2\) or \(a=v^2/r\) according to the data in the question.
6. For vertical circles, define the zero level for G.P.E. before writing energy equations.
7. For unconstrained cases, switch to projectile motion once \(T=0\) or \(R=0\).
8. Use exact values until the final answer, then round appropriately.

# 5. Explicit Prerequisite Recap

## GCSE Foundations

You should already be comfortable with rearranging formulae, using \(\pi\), Pythagoras’ theorem, trigonometric ratios, units such as \(\mathrm{m}\), \(\mathrm{s}\), \(\mathrm{kg}\), \(\mathrm{N}\), and interpreting arrows on diagrams.

## Ordinary AS/A2 Mathematics Foundations

You need:

\[
s=r\theta,\qquad 1\text{ revolution}=2\pi\text{ radians},\qquad v=\frac{ds}{dt},\qquad F=ma,
\]
\[
W=mg,\qquad \mathrm{K.E.}=\frac12mv^2,\qquad \mathrm{G.P.E.}=mgh.
\]

## Previous Further Mathematics Foundations

For this combined FAS2 chapter, the important earlier Further Maths links are:

- `FAS2-CM` comes before `FAS2-FCM`;
- the vertical-circle topic uses the horizontal-circle formulae;
- work-energy methods from FAS2 mechanics are reused in vertical circles.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Radians and circular measure | A full turn is \(2\pi\) radians and \(s=r\theta\). | The angle changes with time, so \(\dfrac{d\theta}{dt}\) becomes angular speed \(\omega\). | Do not use degrees inside \(s=r\theta\), \(v=r\omega\), or \(a=r\omega^2\). |
| Kinematics | Speed is rate of change of distance or displacement. | Even at constant speed, direction changes, so acceleration exists. | Constant speed is not the same as zero acceleration. |
| Newton’s laws | Resolve forces and use \(F=ma\). | Resolve towards the centre of the circle and set the resultant equal to \(m\dfrac{v^2}{r}\) or \(mr\omega^2\). | “Centripetal force” is not an extra force. Tension, friction, reaction or weight components may provide the inward resultant. |
| Work-energy | Use K.E. and G.P.E. to compare positions. | Vertical circles use energy to find speed at different heights, then radial \(F=ma\) to find tension/reaction. | Choose the G.P.E. zero level carefully. Using energy after a particle leaves a circle must keep horizontal kinetic energy. |
| Projectiles | Motion under gravity after launch. | An unconstrained particle that leaves a circle becomes a projectile. | The particle may still have kinetic energy at its highest point because horizontal velocity may not be zero. |

In ordinary A-Level Maths, this idea appeared as straight-line motion, force resolution and energy bookkeeping.

In Further Maths, the same idea becomes circular: the direction of acceleration is no longer automatically the direction of motion. The key upgrade is that you must separate the motion into radial and tangential thinking. The danger is that old habits from straight-line mechanics can make you point \(ma\) the wrong way.

# 6. Big Picture Explanation

Circular motion is what happens when a particle moves in a circle or along an arc of a circle.

The lesson-specific evidence begins by shifting from particles moving in a straight line to particles moving in circles or arcs. Examples include cars going around corners, planets orbiting stars, a ball on a string moving in a horizontal circle, and rollercoaster loops.

The central idea is:

> A particle can have constant speed but still be accelerating, because its velocity direction is changing.

For horizontal circles, the speed is constant, so the acceleration is purely towards the centre:

\[
\text{inward resultant force}=m\frac{v^2}{r}
\]

or

\[
\text{inward resultant force}=mr\omega^2.
\]

For vertical circles, the speed is usually not constant. The particle speeds up when it loses height and slows down when it gains height. That means vertical circles need two machines working together:

1. **Energy** to find how \(v\) changes with height.
2. **Radial \(F=ma\)** to find tension, reaction, thrust or loss of contact.

For unconstrained vertical circles, the circular model can break. If a string goes slack or a surface reaction becomes zero, the particle no longer follows the circular path. It becomes a projectile.

# 7. Key Definitions and Notation

A **particle** is a body whose size is ignored. Its mass is assumed to act at a point.

Let \(r\) be the radius of the circular path, measured in metres.

Let \(\theta\) be the angle swept out at the centre of the circle. For circular-measure formulae, \(\theta\) must be in radians.

A full revolution is:

\[
2\pi\text{ radians}.
\]

If a particle moves along an arc subtending angle \(\theta\) at the centre, then:

\[
s=r\theta.
\]

Angular speed measures the rate of rotation. It is denoted by lower-case omega:

\[
\omega.
\]

Its standard unit is:

\[
\mathrm{rad\,s^{-1}}.
\]

In this lesson:

\[
\omega=\frac{d\theta}{dt}.
\]

Let \(v\) be the linear speed of the particle around the circumference. Units:

\[
[v]=\mathrm{m\,s^{-1}}.
\]

The key relation is:

\[
v=r\omega.
\]

The acceleration of a particle moving in a circle with constant speed is directed towards the centre of the circle. Its magnitude is:

\[
a=r\omega^2
\]

or

\[
a=\frac{v^2}{r}.
\]

Tension \(T\) is a pulling force in a string or rod. A string can pull but cannot push.

Thrust is a pushing force in a rod. A rod can pull or push.

The normal reaction \(R\) is the contact force perpendicular to a surface.

At limiting friction:

\[
F=\mu R.
\]

Here \(\mu\) is the coefficient of friction. It has no units.

A particle is **constrained** to a circular path if it cannot leave the circle. Examples include a bead on a circular wire or a particle attached to a rigid rod.

A particle is **unconstrained** if it may leave the circular path. Examples include a particle attached to a string or a particle moving on the outside of a smooth sphere.

# 8. Core Theory

## 8.1 Angular Speed: Same Rotation Rate, Different Linear Speed

Suppose a clock hand rotates at a constant rate. A point near the centre and a point near the tip complete each revolution in the same time. Therefore they have the same angular speed.

But the tip travels a longer arc in the same time, so it has a larger linear speed.

\[
\text{same }\omega \not\Rightarrow \text{same }v.
\]

Instead,

\[
v\propto r
\]

when \(\omega\) is fixed.

**Bridge Note:** In ordinary A-Level Maths, \(s=r\theta\) linked arc length to angle. Here, Further Maths lets the angle change with time, so rates of change enter the story.

## 8.2 Converting Revolutions to Radians

A full revolution is:

\[
1\text{ rev}=2\pi\text{ rad}.
\]

A second hand of a clock completes one full revolution in \(60\) seconds.

Therefore:

\[
\omega=2\pi\ \mathrm{rad\,min^{-1}}.
\]

In radians per second:

\[
\omega=\frac{2\pi}{60}\ \mathrm{rad\,s^{-1}}=\frac{\pi}{30}\ \mathrm{rad\,s^{-1}}.
\]

In revolutions per second:

\[
\omega=\frac{1}{60}\ \mathrm{rev\,s^{-1}}.
\]

This also follows from:

\[
\frac{\pi}{30}\div 2\pi
=
\frac{\pi}{30}\times \frac{1}{2\pi}
=
\frac{1}{60}.
\]

## 8.3 Deriving \(v=r\omega\)

Let a particle move from \(A\) to \(B\) along a circle of radius \(r\).

Let:

- \(s\) be the arc length from \(A\) to \(B\);
- \(\theta\) be the angle at the centre;
- \(v\) be the linear speed;
- \(\omega\) be the angular speed.

From circular measure:

\[
s=r\theta.
\]

Differentiate with respect to time \(t\):

\[
\frac{ds}{dt}=\frac{d}{dt}(r\theta).
\]

The radius \(r\) is constant for circular motion, so:

\[
\frac{ds}{dt}=r\frac{d\theta}{dt}.
\]

Now define:

\[
v=\frac{ds}{dt}
\]

and

\[
\omega=\frac{d\theta}{dt}.
\]

Therefore:

\[
v=r\omega.
\]

**Important warning:** The radius is unaffected by differentiation only because \(r\) is constant. This is true for circular motion in this lesson, but it would not be true for more general paths such as ellipses or variable-radius polar motion.

## 8.4 Angular Speed Example

A particle moves round the circumference of a circle with radius \(10\ \mathrm{m}\) at speed \(20\ \mathrm{m\,s^{-1}}\). Find its angular speed.

Use:

\[
v=r\omega.
\]

Substitute:

\[
20=10\omega.
\]

Divide by \(10\):

\[
\omega=2.
\]

So:

\[
\boxed{\omega=2\ \mathrm{rad\,s^{-1}}}.
\]

## 8.5 Why Constant Speed Still Gives Acceleration

Velocity has two ingredients: speed and direction.

In circular motion at constant speed, the speed is fixed but the direction is constantly changing. Therefore the velocity is changing, so the particle is accelerating. That acceleration points towards the centre of the circle.

**Bridge Note:** In ordinary straight-line kinematics, constant speed often meant zero acceleration. In circular motion, that habit becomes dangerous because the velocity direction is changing.

## 8.6 Radial Acceleration Formulae

For a particle moving with constant angular speed \(\omega\) in a circle of radius \(r\), the acceleration towards the centre has magnitude:

\[
a=r\omega^2.
\]

Using:

\[
v=r\omega,
\]

we get:

\[
\omega=\frac{v}{r}.
\]

Substitute into \(a=r\omega^2\):

\[
a=r\left(\frac{v}{r}\right)^2
=
r\cdot\frac{v^2}{r^2}
=
\frac{v^2}{r}.
\]

So the two forms are:

\[
\boxed{a=r\omega^2}
\]

and

\[
\boxed{a=\frac{v^2}{r}}.
\]

Use \(a=r\omega^2\) when \(\omega\) is given. Use \(a=\dfrac{v^2}{r}\) when \(v\) is given.

## 8.7 Radial Acceleration Example

A particle moves in a horizontal circular path of radius \(30\ \mathrm{cm}\) with constant angular speed \(4\ \mathrm{rad\,s^{-1}}\). Find the acceleration.

First convert radius to metres:

\[
30\ \mathrm{cm}=0.30\ \mathrm{m}.
\]

Use:

\[
a=r\omega^2.
\]

Substitute:

\[
a=0.30(4)^2=0.30\times 16=4.8.
\]

Therefore:

\[
\boxed{a=4.8\ \mathrm{m\,s^{-2}}\text{ towards the centre of the circle}}.
\]

## 8.8 Horizontal Circular Motion: The Force Equation

In a horizontal circle with constant speed:

\[
\text{vertical direction: usually equilibrium}
\]

and

\[
\text{horizontal radial direction: resultant force }=m\frac{v^2}{r}
\]

or

\[
\text{horizontal radial direction: resultant force }=mr\omega^2.
\]

The evidence gives a useful general strategy:

1. Resolve vertically where forces are in equilibrium.
2. Resolve horizontally where the acceleration is:
   \[
   a=r\omega^2
   \]
   or
   \[
   a=\frac{v^2}{r}.
   \]

## 8.9 Do Not Invent a New Force Called “Centripetal Force”

The phrase “centripetal force” can describe the inward resultant force, but it is not an extra physical force.

In different problems, the inward force may be provided by friction, tension, normal reaction, a component of tension, a component of reaction, or a component of weight.

Correct exam thinking:

\[
\text{real inward resultant force}=m\frac{v^2}{r}.
\]

Incorrect exam thinking:

\[
\text{centripetal force}+T+mg=ma.
\]

That adds a ghost force to the diagram.

## 8.10 Friction Round a Bend

Suppose a car of mass \(M\ \mathrm{kg}\) travels round a bend that is an arc of a circle of radius \(140\ \mathrm{m}\). The greatest speed without slipping is \(45\ \mathrm{km\,h^{-1}}\). Find the coefficient of friction between the tyres and the road.

First convert to standard units:

\[
45\ \mathrm{km\,h^{-1}}
=
45\times 1000\div 3600\ \mathrm{m\,s^{-1}}
=
12.5\ \mathrm{m\,s^{-1}}.
\]

For the vertical direction, the car has no vertical acceleration:

\[
R=Mg.
\]

For the horizontal radial direction, friction provides the inward force. At greatest speed without slipping, friction is limiting:

\[
F=\mu R.
\]

The radial equation is:

\[
F=M\frac{v^2}{r}.
\]

So:

\[
\mu R=M\frac{v^2}{r}.
\]

Substitute \(R=Mg\):

\[
\mu Mg=M\frac{v^2}{r}.
\]

Cancel \(M\):

\[
\mu g=\frac{v^2}{r}.
\]

Divide by \(g\):

\[
\mu=\frac{v^2}{rg}.
\]

Substitute \(v=12.5\), \(r=140\):

\[
\mu=\frac{12.5^2}{140g}.
\]

Using \(g=9.8\):

\[
\mu=\frac{156.25}{140\times 9.8}
=
\frac{156.25}{1372}
=
0.113884\ldots
\]

To three significant figures:

\[
\boxed{\mu=0.114}.
\]

The coefficient of friction has no units.

## 8.11 Conical Pendulum

A conical pendulum is a particle moving in a horizontal circle while attached to a string inclined to the vertical.

Let:

- \(m\) be the mass;
- \(T\) be the tension;
- \(r\) be the radius of the horizontal circle;
- \(l\) be the length of the string;
- \(\alpha\) be the angle between the string and the vertical.

For the vertical direction:

\[
T\cos\alpha=mg.
\]

For the horizontal radial direction:

\[
T\sin\alpha=m r\omega^2.
\]

This is the classic two-direction split:

\[
\text{vertical equilibrium, horizontal circular acceleration}.
\]

## 8.12 Conical Pendulum Example

A particle of mass \(2\ \mathrm{kg}\) is attached to one end of a light inextensible string of length \(0.5\ \mathrm{m}\). The other end is attached to a fixed point \(A\). The particle moves with constant angular speed in a horizontal circle of radius \(0.4\ \mathrm{m}\). The centre of the circle is vertically below \(A\). Calculate the tension and the angular speed.

Let \(\alpha\) be the angle between the string and the vertical.

\[
\sin\alpha=\frac{0.4}{0.5}=\frac45.
\]

Therefore:

\[
\cos\alpha=\frac35.
\]

Vertical equilibrium:

\[
T\cos\alpha=mg.
\]

Substitute \(m=2\):

\[
T\cdot \frac35=2g.
\]

Divide by \(\frac35\):

\[
T=2g\cdot \frac53=\frac{10g}{3}.
\]

Using \(g=9.8\):

\[
T=\frac{98}{3}=32.666\ldots
\]

So:

\[
\boxed{T=32.7\ \mathrm{N}\text{ to 3 s.f.}}.
\]

Resolve horizontally:

\[
T\sin\alpha=mr\omega^2.
\]

Substitute:

\[
32.666\ldots \times \frac45=2(0.4)\omega^2.
\]

\[
26.133\ldots=0.8\omega^2.
\]

\[
\omega^2=32.666\ldots
\]

\[
\omega=5.715\ldots
\]

Therefore:

\[
\boxed{\omega=5.72\ \mathrm{rad\,s^{-1}}\text{ to 3 s.f.}}.
\]

## 8.13 Banked Corner Without Friction

A banked corner lets the normal reaction have a horizontal component.

If there is no friction, the only forces are weight \(mg\) vertically down and normal reaction \(R\) perpendicular to the surface.

Let the bank angle be \(\alpha\).

Vertical equilibrium:

\[
R\cos\alpha=mg.
\]

Horizontal radial equation:

\[
R\sin\alpha=m\frac{v^2}{r}.
\]

Divide the horizontal equation by the vertical equation:

\[
\frac{R\sin\alpha}{R\cos\alpha}
=
\frac{m\dfrac{v^2}{r}}{mg}.
\]

Cancel \(R\) and \(m\):

\[
\tan\alpha=\frac{v^2}{rg}.
\]

Therefore:

\[
v^2=rg\tan\alpha.
\]

So:

\[
\boxed{v=\sqrt{rg\tan\alpha}}.
\]

## 8.14 Banked Corner Example

A boy rides his cycle round a circular track of radius \(25\ \mathrm{m}\). The track is banked at \(20^\circ\) to the horizontal. There is no force due to friction. By modelling the boy and his cycle as a particle of mass \(75\ \mathrm{kg}\), find the speed at which the boy is cycling.

Let:

\[
m=75,\qquad r=25,\qquad \alpha=20^\circ.
\]

Vertical equilibrium:

\[
R\cos20^\circ=75g.
\]

So:

\[
R=\frac{75g}{\cos20^\circ}.
\]

Horizontal radial equation:

\[
R\sin20^\circ=75\frac{v^2}{25}.
\]

Since:

\[
\frac{75}{25}=3,
\]

we get:

\[
R\sin20^\circ=3v^2.
\]

Substitute \(R=\dfrac{75g}{\cos20^\circ}\):

\[
\frac{75g}{\cos20^\circ}\sin20^\circ=3v^2.
\]

Use:

\[
\frac{\sin20^\circ}{\cos20^\circ}=\tan20^\circ.
\]

So:

\[
75g\tan20^\circ=3v^2.
\]

Divide by \(3\):

\[
25g\tan20^\circ=v^2.
\]

Therefore:

\[
v=\sqrt{25g\tan20^\circ}.
\]

Using \(g=9.8\):

\[
v=9.44\ldots
\]

So:

\[
\boxed{v=9.44\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

**Diagram warning:** The inward acceleration arrow is not a force. It should be drawn detached from the particle, often as a double arrow, to show acceleration rather than a physical force.

## 8.15 Vertical Circles: Why the Method Changes

In a vertical circle, the speed is usually not constant.

At the bottom of the swing, the particle has its highest speed. As it moves towards the top, it gains height, so kinetic energy is converted into gravitational potential energy. At the top, it has its lowest speed.

Therefore vertical circles are not solved like horizontal circles.

The radial component is still:

\[
a_{\text{radial}}=\frac{v^2}{r}.
\]

The tangential component, when needed, comes from a component of weight and often has magnitude:

\[
g\sin\theta.
\]

Most CCEA-style vertical-circle mechanics uses energy for speed and radial \(F=ma\) for tension or reaction.

## 8.16 Vertical Circles: The Two Main Ideas

### Idea 1: Work-Energy Principle

\[
\text{Work in}+\text{Initial K.E.}+\text{Initial G.P.E.}
=
\text{Final K.E.}+\text{Final G.P.E.}+\text{Work out}.
\]

In many FAS2 vertical-circle questions, the only work done that changes mechanical energy is due to gravity. Tension or normal reaction is radial, so it is perpendicular to the motion and does no work.

So often:

\[
\text{Initial K.E.}+\text{Initial G.P.E.}
=
\text{Final K.E.}+\text{Final G.P.E.}.
\]

### Idea 2: Radial Newton’s Second Law

At a particular point on the circle:

\[
\text{resultant force towards centre}
=
m\frac{v^2}{r}.
\]

This is used to find tension \(T\), reaction \(R\), thrust in a rod, or conditions for losing contact or going slack.

## 8.17 Choosing the G.P.E. Zero Level

For vertical circles, start by saying where:

\[
\mathrm{G.P.E.}=0.
\]

Common choices are the lowest point or the centre of circle. The lowest point is often easiest, but sometimes the centre makes calculations cleaner.

## 8.18 Vertical Circle Geometry

Suppose a particle is attached to a string or rod of length \(r\), with centre/fixed point \(B\).

Let \(\theta\) be the angle from the downward vertical.

At the lowest point, take:

\[
\mathrm{G.P.E.}=0.
\]

At angle \(\theta\), the vertical rise above the lowest point is:

\[
r-r\cos\theta.
\]

Factorise:

\[
r(1-\cos\theta).
\]

So the gain in G.P.E. is:

\[
mg r(1-\cos\theta).
\]

## 8.19 Vertical Circle Tension Example: General Expression

A particle of mass \(0.4\ \mathrm{kg}\) is attached to one end of a light inextensible string of length \(0.3\ \mathrm{m}\). The other end is attached to a fixed point \(B\). The particle is hanging in equilibrium when it is set in motion with horizontal speed \(u\ \mathrm{m\,s^{-1}}\). Find an expression for the tension in the string, in terms of \(u\), when it is at an angle \(\theta\) to the downward vertical through \(B\).

Let:

\[
m=0.4,\qquad r=0.3.
\]

Set:

\[
\mathrm{G.P.E.}=0
\]

at the lowest point.

At the lowest point:

\[
\mathrm{K.E.}+\mathrm{G.P.E.}
=
\frac12(0.4)u^2+0
=
0.2u^2.
\]

At general angle \(\theta\), let the speed be \(v\). The vertical rise is:

\[
0.3-0.3\cos\theta.
\]

So:

\[
\mathrm{K.E.}+\mathrm{G.P.E.}
=
0.2v^2+0.4g(0.3-0.3\cos\theta).
\]

By conservation of energy:

\[
0.2v^2+0.4g(0.3-0.3\cos\theta)=0.2u^2.
\]

This is the energy equation.

Now use radial \(F=ma\). Towards the centre, the tension \(T\) acts inwards. The component of weight along the inward radial direction is:

\[
-0.4g\cos\theta
\]

when \(\theta\) is measured from the downward vertical.

So:

\[
T-0.4g\cos\theta=0.4\frac{v^2}{0.3}.
\]

From energy:

\[
0.2v^2=0.2u^2-0.4g(0.3-0.3\cos\theta).
\]

Divide by \(0.2\):

\[
v^2=u^2-2g(0.3-0.3\cos\theta)
=
u^2-0.6g(1-\cos\theta).
\]

Now radial equation:

\[
T-0.4g\cos\theta=\frac43v^2.
\]

Substitute:

\[
T-0.4g\cos\theta=\frac43\left[u^2-0.6g(1-\cos\theta)\right].
\]

Expand:

\[
T-0.4g\cos\theta=\frac43u^2-0.8g+0.8g\cos\theta.
\]

Add \(0.4g\cos\theta\) to both sides:

\[
T=\frac43u^2-0.8g+1.2g\cos\theta.
\]

Therefore:

\[
\boxed{T=1.2g\cos\theta+\frac43u^2-0.8g}.
\]

## 8.20 Complete Circle Conditions

The condition depends on the constraint.

### Constrained Cases

Examples:

- rigid rod;
- bead on a circular wire.

The particle cannot leave the circular path.

For a complete circle, require speed at the top to be positive:

\[
v_{\text{top}}>0.
\]

If it does not complete the circle, it moves backwards and forwards along an arc rather than flying away.

### Unconstrained Cases

Examples:

- string;
- outside of a sphere.

The particle can leave the path.

For a string, the string must remain taut:

\[
T>0.
\]

For a particle on a surface, contact requires:

\[
R>0.
\]

If \(T=0\), the string goes slack.

If \(R=0\), the particle loses contact.

After that point, the particle moves freely under gravity.

## 8.21 String Complete Circle Condition for the Previous Example

Using:

\[
T=1.2g\cos\theta+\frac43u^2-0.8g,
\]

for the particle to perform a complete circle on a string, the most critical point is the top:

\[
\theta=180^\circ.
\]

At the top:

\[
\cos180^\circ=-1.
\]

Substitute:

\[
T=1.2g(-1)+\frac43u^2-0.8g
=
\frac43u^2-2g.
\]

For the string to remain taut:

\[
T>0.
\]

So:

\[
\frac43u^2-2g>0.
\]

\[
\frac43u^2>2g.
\]

\[
u^2>\frac32g.
\]

Therefore:

\[
\boxed{u>\sqrt{\frac32g}}.
\]

## 8.22 When a Particle Leaves the Circle

In unconstrained situations, when a particle leaves the circle:

- it moves freely under gravity;
- its initial velocity for projectile motion is the velocity at the leaving point;
- the direction is tangent to the circle at that point.

Warning: at the highest point after leaving the circle, the particle generally still has kinetic energy because the horizontal component of velocity is not zero.

# 9. Visual Asset Integration

## Visual Evidence Limitation Note

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

The screenshots PDF has no parsed text and many pages are repeated screenshots from video playback. Where a diagram is clearly visible, the lesson preserves the mathematical structure and labels. Where the slide contains a green box labelled “Diagram?”, this is treated as a missing diagram space in the original teaching material, not as a supplied final diagram.

[VISUAL PLACEHOLDER: FAS2CircularMotionMermaid-001 | Source: CCEA Further Maths specification boundary + lesson PDF chapter overview + teacher transcript | Insert from mermaid/FAS2CircularMotionMermaid-001.md | Purpose: Show the decision pathway for circular motion problems. The diagram must branch into horizontal circles, vertical circles, constrained vertical circles, unconstrained vertical circles, and projectile motion after leaving the path.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-001 | Source: Lesson PDF angular speed slide + screenshots clock animation | Insert from svg/FAS2CircularMotionSVG-001.svg | Purpose: Show that points at different radii can have the same angular speed but different linear speeds.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-002 | Source: Lesson PDF arc-length derivation + teacher transcript | Insert from svg/FAS2CircularMotionSVG-002.svg | Purpose: Show the geometry behind \(s=r\theta\) and the calculus step leading to \(v=r\omega\).]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-003 | Source: Lesson PDF acceleration slide | Insert from svg/FAS2CircularMotionSVG-003.svg | Purpose: Show radial acceleration directed towards the centre at several positions on a circle.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-004 | Source: Lesson PDF car-friction example | Insert from svg/FAS2CircularMotionSVG-004.svg | Purpose: Show how friction supplies the inward resultant for a car moving round a bend.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-005 | Source: Lesson PDF conical pendulum example | Insert from svg/FAS2CircularMotionSVG-005.svg | Purpose: Show a conical pendulum with tension components and horizontal circular acceleration.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-006 | Source: Lesson PDF banked surface example | Insert from svg/FAS2CircularMotionSVG-006.svg | Purpose: Show a banked corner without friction and the detached acceleration arrow.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-007 | Source: Lesson PDF vertical circles slide + teacher transcript | Insert from svg/FAS2CircularMotionSVG-007.svg | Purpose: Show radial and tangential acceleration in a vertical circle.]

[VISUAL PLACEHOLDER: FAS2CircularMotionSVG-008 | Source: Lesson PDF vertical-circle constrained/unconstrained examples + transcript | Insert from svg/FAS2CircularMotionSVG-008.svg | Purpose: Compare constrained and unconstrained circular paths.]

[VISUAL PLACEHOLDER: FAS2CircularMotionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2CircularMotionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2CircularMotionTikZ-001 | Source: Lesson PDF arc-length derivation | Insert from tikz/FAS2CircularMotionTikZ-001.tex | Purpose: Provide a precise mathematical diagram for \(s=r\theta\) and \(v=r\omega\).]

[VISUAL PLACEHOLDER: FAS2CircularMotionTikZ-002 | Source: Lesson PDF vertical-circle energy example | Insert from tikz/FAS2CircularMotionTikZ-002.tex | Purpose: Provide precise vertical-circle height geometry for \(r-r\cos\theta\).]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2CircularMotionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CircularMotionWidget-001.html | Purpose: Convert angular speed units and calculate \(v\) and \(a\).]

The student inputs angular speed in \(\mathrm{rad\,s^{-1}}\), \(\mathrm{rev\,s^{-1}}\), or \(\mathrm{rev\,min^{-1}}\), radius \(r\), and optionally linear speed \(v\). The widget displays converted angular speed, \(v=r\omega\), and \(a=r\omega^2\) or \(a=v^2/r\).

[INTERACTIVE PLACEHOLDER: FAS2CircularMotionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CircularMotionWidget-002.html | Purpose: Build force equations for horizontal circular motion.]

The student chooses a model such as friction on a flat road, conical pendulum, banked corner without friction, or two-string horizontal circle. The widget reinforces vertical equilibrium and horizontal inward resultant equations.

[INTERACTIVE PLACEHOLDER: FAS2CircularMotionWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CircularMotionWidget-003.html | Purpose: Practise vertical-circle energy plus radial \(F=ma\).]

The student inputs mass, radius, initial speed, target angle and model type. The widget displays height gain \(r(1-\cos\theta)\), the energy equation, radial force equation, and constraint checks.

# 11. Worked Examples

## Worked Example 1: Angular Speed of a Clock Second Hand

What is the angular speed of the seconds hand of a clock:

a. in \(\mathrm{rad\,min^{-1}}\);  
b. in \(\mathrm{rad\,s^{-1}}\);  
c. in \(\mathrm{rev\,s^{-1}}\)?

The second hand completes one full revolution in \(60\) seconds.

One full revolution is:

\[
2\pi\text{ radians}.
\]

Since \(60\) seconds is \(1\) minute:

\[
\omega=2\pi\ \mathrm{rad\,min^{-1}}.
\]

For radians per second:

\[
\omega=\frac{2\pi}{60}\ \mathrm{rad\,s^{-1}}
=
\frac{\pi}{30}\ \mathrm{rad\,s^{-1}}.
\]

For revolutions per second:

\[
\omega=\frac{1}{60}\ \mathrm{rev\,s^{-1}}.
\]

Alternatively:

\[
\frac{\pi}{30}\div 2\pi
=
\frac{\pi}{30}\times\frac{1}{2\pi}
=
\frac{1}{60}.
\]

Final answers:

\[
\boxed{2\pi\ \mathrm{rad\,min^{-1}},\quad \frac{\pi}{30}\ \mathrm{rad\,s^{-1}},\quad \frac{1}{60}\ \mathrm{rev\,s^{-1}}}.
\]

## Worked Example 2: Finding Angular Speed from Linear Speed

A particle moves round the circumference of a circle with radius \(10\ \mathrm{m}\) at speed \(20\ \mathrm{m\,s^{-1}}\). Calculate its angular speed.

\[
v=r\omega.
\]

\[
20=10\omega.
\]

\[
\omega=2.
\]

\[
\boxed{\omega=2\ \mathrm{rad\,s^{-1}}}.
\]

## Worked Example 3: Radial Acceleration from Angular Speed

A particle is moving on a horizontal circular path of radius \(30\ \mathrm{cm}\) with constant angular speed \(4\ \mathrm{rad\,s^{-1}}\). Calculate the acceleration of the particle.

\[
30\ \mathrm{cm}=0.30\ \mathrm{m}.
\]

\[
a=r\omega^2=0.30(4)^2=0.30(16)=4.8.
\]

\[
\boxed{a=4.8\ \mathrm{m\,s^{-2}}\text{ towards the centre of the circle}}.
\]

## Worked Example 4: Car Round a Bend with Friction

A car of mass \(M\ \mathrm{kg}\) is travelling round a bend which is an arc of a circle of radius \(140\ \mathrm{m}\). The greatest speed at which the car can travel round the bend without slipping is \(45\ \mathrm{km\,h^{-1}}\). Find the coefficient of friction between the tyres of the car and the road.

\[
45\ \mathrm{km\,h^{-1}}=45\times1000\div3600=12.5\ \mathrm{m\,s^{-1}}.
\]

Vertical direction:

\[
R=Mg.
\]

At the greatest speed without slipping:

\[
F=\mu R.
\]

Horizontally, friction supplies the inward resultant:

\[
F=M\frac{v^2}{r}.
\]

Therefore:

\[
\mu R=M\frac{v^2}{r}.
\]

Substitute \(R=Mg\):

\[
\mu Mg=M\frac{v^2}{r}.
\]

Cancel \(M\):

\[
\mu=\frac{v^2}{rg}
=
\frac{12.5^2}{140g}
=
\frac{156.25}{1372}
=
0.113884\ldots
\]

\[
\boxed{\mu=0.114\text{ to 3 s.f.}}.
\]

## Worked Example 5: Conical Pendulum

A particle of mass \(2\ \mathrm{kg}\) is attached to a light inextensible string of length \(0.5\ \mathrm{m}\). The particle moves with constant angular speed in a horizontal circle of radius \(0.4\ \mathrm{m}\). The centre of the circle is vertically below \(A\). Calculate the tension in the string and the angular speed.

Let \(\alpha\) be the angle the string makes with the vertical.

\[
\sin\alpha=\frac{0.4}{0.5}=\frac45,\qquad \cos\alpha=\frac35.
\]

Resolve vertically:

\[
T\cos\alpha=2g.
\]

\[
T\cdot\frac35=2g.
\]

\[
T=2g\cdot\frac53=\frac{10g}{3}=32.666\ldots
\]

\[
\boxed{T=32.7\ \mathrm{N}\text{ to 3 s.f.}}.
\]

Resolve horizontally towards the centre:

\[
T\sin\alpha=mr\omega^2.
\]

\[
32.666\ldots\times\frac45=2(0.4)\omega^2.
\]

\[
26.133\ldots=0.8\omega^2.
\]

\[
\omega^2=32.666\ldots
\]

\[
\omega=5.715\ldots
\]

\[
\boxed{\omega=5.72\ \mathrm{rad\,s^{-1}}\text{ to 3 s.f.}}.
\]

## Worked Example 6: Banked Corner with No Friction

A boy rides his cycle round a circular track of radius \(25\ \mathrm{m}\). The track is banked at \(20^\circ\) to the horizontal. There is no force due to friction. By modelling the boy and his cycle as a particle of mass \(75\ \mathrm{kg}\), find the speed at which the boy is cycling.

Resolve vertically:

\[
R\cos20^\circ=75g.
\]

Therefore:

\[
R=\frac{75g}{\cos20^\circ}.
\]

Resolve horizontally towards the centre:

\[
R\sin20^\circ=75\frac{v^2}{25}=3v^2.
\]

Substitute \(R=\dfrac{75g}{\cos20^\circ}\):

\[
\frac{75g}{\cos20^\circ}\sin20^\circ=3v^2.
\]

\[
75g\tan20^\circ=3v^2.
\]

\[
25g\tan20^\circ=v^2.
\]

\[
v=\sqrt{25g\tan20^\circ}=9.44\ldots
\]

\[
\boxed{v=9.44\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

## Worked Example 7: Two Strings in a Horizontal Circle

A particle \(P\) of mass \(m\) is attached by two strings to fixed points \(A\) and \(B\), where \(A\) is vertically above \(B\). The strings are both taut and \(P\) is moving in a horizontal circle with constant angular speed

\[
2\sqrt{3g}\ \mathrm{rad\,s^{-1}}.
\]

Both strings are \(0.5\ \mathrm{m}\) in length and inclined at \(60^\circ\) to the vertical. Calculate the tension in the two strings.

Let the tensions be \(T_A\) in the upper string and \(T_B\) in the lower string.

\[
r=0.5\sin60^\circ=0.5\times\frac{\sqrt3}{2}=\frac{\sqrt3}{4}.
\]

\[
\omega=2\sqrt{3g}
\]

so

\[
\omega^2=(2\sqrt{3g})^2=12g.
\]

Resolve vertically:

\[
T_A\cos60^\circ=T_B\cos60^\circ+mg.
\]

Since \(\cos60^\circ=\frac12\):

\[
\frac12T_A=\frac12T_B+mg.
\]

\[
T_A=T_B+2mg.
\]

So:

\[
T_A-T_B=2mg.
\]

Resolve horizontally towards the centre:

\[
T_A\sin60^\circ+T_B\sin60^\circ=mr\omega^2.
\]

\[
(T_A+T_B)\frac{\sqrt3}{2}
=
m\cdot\frac{\sqrt3}{4}\cdot12g.
\]

Right-hand side:

\[
m\cdot\frac{\sqrt3}{4}\cdot12g=3\sqrt3mg.
\]

Therefore:

\[
(T_A+T_B)\frac{\sqrt3}{2}=3\sqrt3mg.
\]

Divide by \(\frac{\sqrt3}{2}\):

\[
T_A+T_B=6mg.
\]

Solve:

\[
T_A+T_B=6mg,\qquad T_A-T_B=2mg.
\]

Add the equations:

\[
2T_A=8mg.
\]

\[
T_A=4mg.
\]

Then:

\[
T_B=2mg.
\]

\[
\boxed{T_A=4mg\ \mathrm{N},\qquad T_B=2mg\ \mathrm{N}}.
\]

## Worked Example 8: Vertical Circle with a Rod Released from Rest

A particle of mass \(0.4\ \mathrm{kg}\) is attached to one end \(A\) of a light rod \(AB\) of length \(0.3\ \mathrm{m}\). The rod is free to rotate in a vertical plane about \(B\). The particle is held at rest with \(AB\) horizontal and released.

a. Calculate the speed of the particle as it passes through the lowest point of the path.  
b. Calculate the tension in the rod at this point.

### Part a

The particle drops by:

\[
h=0.3\ \mathrm{m}.
\]

Set G.P.E. zero at the lowest point.

\[
mgh=\frac12mv^2.
\]

Cancel \(m\):

\[
gh=\frac12v^2.
\]

\[
v^2=2gh=2(9.8)(0.3)=5.88.
\]

\[
v=\sqrt{5.88}=2.424\ldots
\]

\[
\boxed{v=2.42\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

### Part b

At the lowest point, the acceleration is upwards towards \(B\).

\[
a=\frac{v^2}{r}=\frac{5.88}{0.3}=19.6.
\]

Resolve upwards towards the centre:

\[
T-0.4g=0.4a.
\]

\[
T=0.4(19.6)+0.4g.
\]

Using \(g=9.8\):

\[
T=7.84+3.92=11.76.
\]

\[
\boxed{T=11.8\ \mathrm{N}\text{ to 3 s.f.}}.
\]

## Worked Example 9: Vertical Circle String Tension in Terms of \(u\)

A particle of mass \(0.4\ \mathrm{kg}\) is attached to one end of a light inextensible string of length \(0.3\ \mathrm{m}\). The other end is attached to a fixed point \(B\). The particle is hanging in equilibrium when it is set in motion with horizontal speed \(u\ \mathrm{m\,s^{-1}}\). Find an expression for the tension in the string, in terms of \(u\), when it is at an angle \(\theta\) to the downward vertical through \(B\).

Let:

\[
m=0.4,\qquad r=0.3.
\]

Set:

\[
\mathrm{G.P.E.}=0
\]

at the lowest point.

At the lowest point:

\[
\mathrm{K.E.}+\mathrm{G.P.E.}
=
\frac12(0.4)u^2+0
=
0.2u^2.
\]

At a general point where the speed is \(v\), the height above the lowest point is:

\[
0.3-0.3\cos\theta.
\]

So the energy is:

\[
0.2v^2+0.4g(0.3-0.3\cos\theta).
\]

By conservation of energy:

\[
0.2v^2+0.4g(0.3-0.3\cos\theta)=0.2u^2.
\]

Towards the centre:

\[
T-0.4g\cos\theta=0.4\frac{v^2}{0.3}.
\]

From energy:

\[
v^2=u^2-0.6g(1-\cos\theta).
\]

Substitute into radial equation:

\[
T-0.4g\cos\theta=\frac43\left[u^2-0.6g(1-\cos\theta)\right].
\]

\[
T-0.4g\cos\theta=\frac43u^2-0.8g+0.8g\cos\theta.
\]

\[
T=\frac43u^2-0.8g+1.2g\cos\theta.
\]

\[
\boxed{T=1.2g\cos\theta+\frac43u^2-0.8g}.
\]

# 12. Common Mistakes and Exam Traps

## 12.1 Units Trap

Do not use \(\mathrm{km\,h^{-1}}\), centimetres or revolutions per minute directly in the main formulae unless the formula has been adapted.

Convert to standard SI units first:

\[
\mathrm{m},\quad \mathrm{s},\quad \mathrm{kg},\quad \mathrm{N}.
\]

## 12.2 Degrees Versus Radians

The formula

\[
s=r\theta
\]

requires \(\theta\) in radians. The angular speed unit in this lesson is normally:

\[
\mathrm{rad\,s^{-1}}.
\]

## 12.3 Constant Speed Does Not Mean No Acceleration

In circular motion, constant speed still gives acceleration because direction changes.

\[
a=\frac{v^2}{r}
\]

towards the centre.

## 12.4 Acceleration Arrow Is Not a Force

In a force diagram, only draw actual forces on the particle. The acceleration arrow may be useful, but it is not a force.

## 12.5 “Centripetal Force” Is Not an Extra Force

Do not add a separate force called centripetal force. The phrase means the resultant force towards the centre.

## 12.6 Friction Trap

Only use:

\[
F=\mu R
\]

when friction is limiting.

Phrases such as “greatest speed”, “on the point of slipping”, and “least coefficient of friction” often indicate limiting friction.

## 12.7 Mass Cancelling Trap

In many circular motion problems, mass cancels. Do not panic if the answer is independent of mass.

## 12.8 Horizontal Versus Vertical Circle Trap

Horizontal circles with constant speed usually use force resolution. Vertical circles usually use energy first, then radial \(F=ma\).

## 12.9 Tension Versus Thrust in a Rod

A string can only pull. A rod can pull or push.

## 12.10 String Going Slack

For a string:

\[
T\geq 0.
\]

If a calculation gives \(T<0\), the string would have to push, which it cannot do. The circular model has broken before that point.

## 12.11 Surface Contact Trap

For a particle on a surface:

\[
R\geq 0.
\]

If \(R=0\), the particle is just losing contact. If \(R<0\), the model is impossible because the surface cannot pull the particle.

## 12.12 Highest Point Energy Trap

For projectile motion after leaving a circle, do not assume all kinetic energy disappears at the highest point. Horizontal velocity remains.

## 12.13 G.P.E. Zero Level Trap

Before writing energy equations, choose and state where:

\[
\mathrm{G.P.E.}=0.
\]

## 12.14 Formula Selection Trap

Use:

\[
a=r\omega^2
\]

if angular speed is given.

Use:

\[
a=\frac{v^2}{r}
\]

if linear speed is given.

Use:

\[
v=r\omega
\]

to convert between them.

# 13. Practice Questions

These questions are generated practice questions. They are not CCEA past-paper questions and are not textbook questions.

## 13.1 Basic Fluency Questions

1. Convert \(90\ \mathrm{rev\,min^{-1}}\) into \(\mathrm{rad\,s^{-1}}\).
2. A particle moves in a circle of radius \(0.8\ \mathrm{m}\) with angular speed \(5\ \mathrm{rad\,s^{-1}}\). Find its linear speed.
3. A particle moves in a circle of radius \(2\ \mathrm{m}\) with speed \(6\ \mathrm{m\,s^{-1}}\). Find its acceleration towards the centre.
4. A particle moves with angular speed \(3\ \mathrm{rad\,s^{-1}}\) in a circle of radius \(4\ \mathrm{m}\). Find its acceleration towards the centre.

## 13.2 Bridge Questions

5. Starting from \(s=r\theta\), derive \(v=r\omega\). State clearly what each symbol means.
6. Explain why a particle moving at constant speed in a circle is accelerating.
7. A student writes \(T+\text{centripetal force}=m\dfrac{v^2}{r}\). Explain why this is wrong.

## 13.3 Standard Exam-Style Questions

8. A car travels round a flat circular bend of radius \(80\ \mathrm{m}\). The coefficient of friction between the tyres and the road is \(0.45\). Find the greatest speed at which the car can travel without slipping.
9. A particle of mass \(0.5\ \mathrm{kg}\) is attached to a light inextensible string and moves as a conical pendulum. The string makes an angle of \(30^\circ\) with the vertical. The radius of the horizontal circle is \(0.6\ \mathrm{m}\). Find the tension and angular speed.
10. A cyclist rides round a banked circular track of radius \(40\ \mathrm{m}\). The track is banked at \(15^\circ\) to the horizontal and friction is negligible. Find the speed for which the cyclist can ride without slipping sideways.

## 13.4 Harder Synthesis Questions

11. A particle of mass \(0.3\ \mathrm{kg}\) is attached to a light rod of length \(0.5\ \mathrm{m}\), fixed at one end. The rod rotates in a vertical plane. The particle is released from rest when the rod is horizontal. Find the speed and force in the rod at the lowest point.
12. A particle of mass \(m\) is attached to a light inextensible string of length \(r\). It is projected horizontally from the lowest point of a vertical circle with speed \(u\). Show that, at an angle \(\theta\) to the downward vertical, the speed \(v\) satisfies
\[
v^2=u^2-2gr(1-\cos\theta).
\]
Then find an expression for the tension \(T\) in the string.
13. Using your answer to Question 12, find the condition on \(u\) for the particle to complete a full vertical circle with the string taut throughout.

# 14. Worked Solutions

## Solution 1

\[
90\ \mathrm{rev\,min^{-1}}=90\div60=\frac32\ \mathrm{rev\,s^{-1}}.
\]

Since \(1\ \mathrm{rev}=2\pi\ \mathrm{rad}\),

\[
\omega=\frac32\times2\pi=3\pi.
\]

\[
\boxed{3\pi\ \mathrm{rad\,s^{-1}}}.
\]

## Solution 2

\[
v=r\omega=0.8(5)=4.
\]

\[
\boxed{v=4\ \mathrm{m\,s^{-1}}}.
\]

## Solution 3

\[
a=\frac{v^2}{r}=\frac{6^2}{2}=\frac{36}{2}=18.
\]

\[
\boxed{a=18\ \mathrm{m\,s^{-2}}\text{ towards the centre}}.
\]

## Solution 4

\[
a=r\omega^2=4(3)^2=4(9)=36.
\]

\[
\boxed{a=36\ \mathrm{m\,s^{-2}}\text{ towards the centre}}.
\]

## Solution 5

\[
s=r\theta.
\]

Differentiate with respect to time:

\[
\frac{ds}{dt}=\frac{d}{dt}(r\theta).
\]

Since \(r\) is constant:

\[
\frac{ds}{dt}=r\frac{d\theta}{dt}.
\]

Now:

\[
v=\frac{ds}{dt},\qquad \omega=\frac{d\theta}{dt}.
\]

Therefore:

\[
\boxed{v=r\omega}.
\]

## Solution 6

Acceleration means rate of change of velocity. Velocity includes direction as well as speed. In circular motion at constant speed, the speed is constant but the direction changes continuously. Therefore velocity changes and the particle accelerates towards the centre.

## Solution 7

“Centripetal force” is not an additional force. The phrase means the resultant force towards the centre.

If tension is the only inward force:

\[
T=m\frac{v^2}{r}.
\]

If there are several real forces:

\[
\text{resultant of real inward/outward force components}=m\frac{v^2}{r}.
\]

## Solution 8

At greatest speed, friction is limiting:

\[
F=\mu R.
\]

Vertically:

\[
R=mg.
\]

So:

\[
F=\mu mg.
\]

Radially:

\[
F=m\frac{v^2}{r}.
\]

Therefore:

\[
\mu mg=m\frac{v^2}{r}.
\]

Cancel \(m\):

\[
\mu g=\frac{v^2}{r}.
\]

\[
v^2=\mu gr.
\]

Substitute:

\[
v^2=0.45(9.8)(80)=352.8.
\]

\[
v=\sqrt{352.8}=18.782\ldots
\]

\[
\boxed{v=18.8\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

## Solution 9

\[
m=0.5,\qquad \alpha=30^\circ,\qquad r=0.6.
\]

Resolve vertically:

\[
T\cos30^\circ=mg=0.5g.
\]

\[
T=\frac{0.5g}{\cos30^\circ}=\frac{g}{\sqrt3}=5.658\ldots
\]

\[
\boxed{T=5.66\ \mathrm{N}\text{ to 3 s.f.}}.
\]

Resolve horizontally:

\[
T\sin30^\circ=mr\omega^2.
\]

\[
5.658\ldots\times\frac12=0.5(0.6)\omega^2.
\]

\[
2.829\ldots=0.3\omega^2.
\]

\[
\omega^2=9.430\ldots
\]

\[
\omega=3.070\ldots
\]

\[
\boxed{\omega=3.07\ \mathrm{rad\,s^{-1}}\text{ to 3 s.f.}}.
\]

## Solution 10

For a banked track with no friction:

\[
R\cos\alpha=mg,\qquad R\sin\alpha=m\frac{v^2}{r}.
\]

Divide:

\[
\tan\alpha=\frac{v^2}{rg}.
\]

\[
v^2=rg\tan\alpha.
\]

Substitute:

\[
v^2=40(9.8)\tan15^\circ=105.04\ldots.
\]

\[
v=10.249\ldots
\]

\[
\boxed{v=10.2\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

## Solution 11

The particle drops by \(h=0.5\ \mathrm{m}\).

Energy:

\[
mgh=\frac12mv^2.
\]

\[
v^2=2gh=2g(0.5)=g=9.8.
\]

\[
v=\sqrt{9.8}=3.130\ldots
\]

\[
\boxed{v=3.13\ \mathrm{m\,s^{-1}}\text{ to 3 s.f.}}.
\]

At the lowest point:

\[
a=\frac{v^2}{r}=\frac{9.8}{0.5}=19.6.
\]

Resolve upwards:

\[
T-mg=ma.
\]

\[
T-0.3g=0.3(19.6).
\]

\[
T=0.3(19.6)+0.3g=5.88+2.94=8.82.
\]

\[
\boxed{T=8.82\ \mathrm{N}}.
\]

## Solution 12

At the lowest point, set \(\mathrm{G.P.E.}=0\).

Initial energy:

\[
\frac12mu^2.
\]

At angle \(\theta\), the height above the lowest point is:

\[
h=r-r\cos\theta=r(1-\cos\theta).
\]

Energy at angle \(\theta\):

\[
\frac12mv^2+mg r(1-\cos\theta).
\]

By conservation of energy:

\[
\frac12mv^2+mg r(1-\cos\theta)=\frac12mu^2.
\]

Divide by \(m\):

\[
\frac12v^2+g r(1-\cos\theta)=\frac12u^2.
\]

Multiply by \(2\):

\[
v^2+2gr(1-\cos\theta)=u^2.
\]

\[
\boxed{v^2=u^2-2gr(1-\cos\theta)}.
\]

Towards the centre:

\[
T-mg\cos\theta=m\frac{v^2}{r}.
\]

Substitute \(v^2\):

\[
T-mg\cos\theta=\frac{m}{r}\left[u^2-2gr(1-\cos\theta)\right].
\]

\[
T-mg\cos\theta=\frac{mu^2}{r}-2mg+2mg\cos\theta.
\]

\[
T=\frac{mu^2}{r}-2mg+3mg\cos\theta.
\]

\[
\boxed{T=\frac{mu^2}{r}+mg(3\cos\theta-2)}.
\]

## Solution 13

At the top:

\[
\theta=\pi,\qquad \cos\pi=-1.
\]

Using:

\[
T=\frac{mu^2}{r}+mg(3\cos\theta-2),
\]

\[
T_{\text{top}}=\frac{mu^2}{r}+mg(3(-1)-2).
\]

\[
T_{\text{top}}=\frac{mu^2}{r}-5mg.
\]

For the string to remain taut:

\[
T_{\text{top}}>0.
\]

\[
\frac{mu^2}{r}-5mg>0.
\]

\[
\frac{u^2}{r}>5g.
\]

\[
u^2>5gr.
\]

\[
\boxed{u>\sqrt{5gr}}.
\]

# 15. Exam Technique Notes

1. First identify whether the circle is horizontal or vertical.
2. Convert all quantities to standard SI units.
3. Use \(v=r\omega\) to connect linear and angular speed.
4. Use \(a=r\omega^2\) when \(\omega\) is known.
5. Use \(a=\dfrac{v^2}{r}\) when \(v\) is known.
6. Draw only real forces: \(mg\), \(T\), \(R\), friction \(F\), thrust/compression if a rod pushes.
7. Do not draw “centripetal force” as an additional arrow.
8. For vertical circles, choose the zero G.P.E. level, write energy, then use radial \(F=ma\).
9. Check constraint:
   - string: \(T\geq0\);
   - surface: \(R\geq0\);
   - rod/wire: the particle remains constrained, but force may change direction.
10. Unless a question specifies otherwise, mechanics answers are usually rounded to three significant figures.

# 16. Syllabus Gap Check

## LO Coverage Table

| LO ID | Covered? | Evidence level | Notes |
|---|---:|---|---|
| `FAS2-CM-LO001` | Yes | Strong | Angular speed, radians, revolutions, \(v=r\omega\), derivation from \(s=r\theta\). |
| `FAS2-CM-LO002` | Yes | Strong | Radial acceleration towards centre, \(a=r\omega^2\), \(a=\dfrac{v^2}{r}\). |
| `FAS2-CM-LO003` | Yes | Strong | Horizontal circles, conical pendulum, banked corners without sliding/overturning, friction examples. |
| `FAS2-FCM-LO001` | Yes | Strong | Vertical circles, energy, radial \(F=ma\), standard complete-circle results, constrained/unconstrained distinction. |

## Evidence Coverage Table

| Evidence type | Used? | Limitation |
|---|---:|---|
| CCEA Further Maths specification map | Yes | Defines boundary, topic codes and LO IDs. |
| Module map | Yes | Used to support bridge and topic identity. |
| Evidence checklist | Yes | Used for intake quality control. |
| Lesson PDF | Yes | Some symbols were lost in extraction, but context and visible screenshots support restoration. |
| Teacher transcript | Yes | Used heavily for explanations and warnings. |
| Screenshots PDF | Partly | No parsed text; only visible pages inspected. |
| Ordinary Maths bridge extracts | Yes | Bridge only. |
| Cross-board Edexcel material | Limited | Used only when content matches CCEA topic boundary. |

## Bridge Coverage Table

| Bridge area | Covered? | Where |
|---|---:|---|
| Radians and arc length | Yes | Sections 5, 7, 8, 11 |
| Differentiating displacement | Yes | Sections 5, 8 |
| Newton’s laws and resolving | Yes | Sections 8, 11, 15 |
| Friction and reaction | Yes | Sections 8, 11, 12 |
| Work-energy | Yes | Sections 8, 11, 15 |
| Projectiles after leaving path | Yes | Sections 8, 12, 15 |

### Off-Spec Content Found but Excluded

| Content | Reason excluded |
|---|---|
| Sliding and overturning on banked corners | The FAS2 LO explicitly includes banked corners but excludes sliding or overturning problems; those belong to a later FA22 boundary. |
| General polar acceleration with changing \(r\) | Not required by `FAS2-CM` or `FAS2-FCM`. |
| Coriolis term | Enrichment only, not CCEA core for this lesson. |
| Telecanape / Cambridge Engineering extension | Interesting but not required for CCEA FAS2. |
| Edexcel specification as authority | Cross-board; CCEA map is the authority. |

### Optional Enrichment Not Required by CCEA

The following may be included in a portal enrichment panel, clearly separated from core revision:

- polar form with variable \(r\);
- radial and transverse acceleration beyond circular motion;
- Coriolis term;
- engineering applications of circular motion;
- comparison of angular speed and angular velocity as vector/scalar ideas.

### Weak Evidence Warnings

- Some formulas in the PDF parsed text lost variables due to extraction.
- Screenshots include repeated video frames and some iPad overlay obstructions.
- No CCEA-specific exam questions were supplied.
- Cross-board Edexcel questions are not to be labelled as CCEA past-paper questions.

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed teaching enhancements based on the lesson evidence. They are not claimed as original evidence.

## Extra Diagrams

1. A “same \(\omega\), different \(v\)” clock-hand diagram.
2. A force-library diagram showing which real forces can provide inward resultant.
3. A vertical-circle decision diagram.
4. A “leave circle then projectile” transition diagram.

## Extra Animations

1. Rotating radius showing \(\theta\), \(s\), \(v\) and \(\omega\).
2. Particle moving in a horizontal circle with inward acceleration arrows.
3. Vertical circle showing speed increasing downward and decreasing upward.
4. String slack animation showing transition to projectile motion.

## Extra Widgets

1. Unit conversion widget for rev/min, rev/s and rad/s.
2. Force-equation builder for horizontal-circle models.
3. Vertical-circle energy checker.
4. Constrained/unconstrained diagnostic quiz.

## Extra Examples

1. Flat circular road with unknown maximum speed.
2. Conical pendulum with unknown radius.
3. Banked corner with unknown banking angle.
4. Vertical string with unknown minimum projection speed.
5. Outside sphere losing contact and becoming projectile.

# 18. Supplementary Sources Used

## Project Sources Used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`

## Lesson-Specific Evidence Used

- `FM2-Chp1-Circular Motion_v200111.pdf`
- `Chapter_1_Circular_Motion_🚗_(Further_Mechanics_2)_screenshots.pdf`
- `transcripts.md`

## Ordinary A-Level Maths Bridge Sources Used

- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

These are used as bridge context only. They do not override the CCEA Further Mathematics specification.

## Cross-Board Source Notes

The supplied lesson PDF references Edexcel Further Mechanics / M3 material. These references are used only where the CCEA Further Mathematics specification confirms the material is on-topic.

No cross-board source is used as the syllabus authority.

## Evidence Limitations

- The screenshots PDF was not text-parseable.
- Some screenshot pages contain video playback overlays.
- Some PDF formula text lost variables during extraction.
- No CCEA-specific question-paper evidence was supplied for this lesson.
- Some examples were reconstructed from the visible PDF/transcript evidence and standard mechanics algebra.

## Final Evidence Boundary Statement

The core lesson covers only:

- `FAS2-CM-LO001`;
- `FAS2-CM-LO002`;
- `FAS2-CM-LO003`;
- `FAS2-FCM-LO001`.

All other material is either bridge context, optional enrichment or explicitly excluded.

# 19. Final Student Checklist

## Prerequisite Confidence Checklist

Before moving on, check that you can:

- [ ] convert between revolutions and radians;
- [ ] use \(1\text{ rev}=2\pi\text{ rad}\);
- [ ] use \(s=r\theta\) with \(\theta\) in radians;
- [ ] differentiate \(s\) with respect to \(t\) to obtain speed;
- [ ] resolve forces into components;
- [ ] use \(F=ma\);
- [ ] use \(W=mg\);
- [ ] use \(\mathrm{K.E.}=\frac12mv^2\);
- [ ] use \(\mathrm{G.P.E.}=mgh\).

## Further Maths Method Checklist

You should now be able to:

- [ ] define angular speed;
- [ ] use \(\omega\) for angular speed;
- [ ] use \(\mathrm{rad\,s^{-1}}\);
- [ ] derive \(v=r\omega\);
- [ ] use \(a=r\omega^2\);
- [ ] use \(a=\dfrac{v^2}{r}\);
- [ ] explain why acceleration is towards the centre;
- [ ] solve flat-road friction circular motion problems;
- [ ] solve conical pendulum problems;
- [ ] solve banked-corner problems without friction;
- [ ] use energy in vertical-circle problems;
- [ ] use radial \(F=ma\) in vertical-circle problems;
- [ ] identify constrained and unconstrained circular motion.

## Exam Technique Checklist

In exam questions, remember to:

- [ ] convert all units first;
- [ ] draw only real forces on the particle;
- [ ] draw acceleration separately if needed;
- [ ] avoid adding “centripetal force” as a new force;
- [ ] state the direction of acceleration;
- [ ] decide whether the circle is horizontal or vertical;
- [ ] choose \(a=r\omega^2\) or \(a=\dfrac{v^2}{r}\);
- [ ] define the G.P.E. zero level in vertical-circle questions;
- [ ] check whether \(T\), \(R\) or thrust is physically possible;
- [ ] switch to projectile motion if the particle leaves the circle;
- [ ] round final mechanics answers sensibly, usually to three significant figures.

## Bridge Checklist

You should be able to explain:

- [ ] how \(s=r\theta\) becomes \(v=r\omega\);
- [ ] why constant speed can still mean acceleration;
- [ ] why \(F=ma\) is used radially;
- [ ] how energy helps find changing speeds in vertical circles;
- [ ] why projectile motion may appear after a particle leaves a circular path.

## Diagram and Visual Understanding Checklist

You should be able to identify:

- [ ] radius \(r\);
- [ ] centre of circle;
- [ ] tangent velocity direction;
- [ ] inward acceleration direction;
- [ ] real forces;
- [ ] components of tension or reaction;
- [ ] vertical height gain \(r(1-\cos\theta)\);
- [ ] point where \(T=0\) or \(R=0\);
- [ ] tangent launch direction after leaving the circle.
