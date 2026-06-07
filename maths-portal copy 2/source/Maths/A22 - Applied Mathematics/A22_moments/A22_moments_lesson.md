# A22 Moments: Rigid Bodies

## Lesson Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A22 |
| Unit name | A2 2 Applied Mathematics |
| Applied section | Mechanics |
| Topic code | A22-MOM |
| Topic name | Moments |
| Lesson focus | Rigid Bodies |
| Topic slug | moments |
| Topic Pascal | Moments |
| Topic ID | A22Moments |
| Lesson file | A22_moments_lesson.md |
| Learning outcome IDs | A22-MOM-LO001 |
| Main tags | `#A22`, `#Moments`, `#RigidBodies`, `#Statics`, `#Mechanics` |

## Evidence Map

| Source | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic, LO ID and boundary. |
| README-Module-Map.txt | Naming conventions, phase workflow and file conventions. |
| Source-Evidence-Drop-Checklist.txt | Evidence, missing evidence and visual placeholder rules. |
| MechYr2 Chapter 4: Moments | Definition of moment, rigid-body equilibrium, rods, centres of mass and tilting. |
| MechYr2 Chapter 7: Applications of Forces | Static rigid bodies with friction, rods on pegs, ladders and rough-ground examples. |
| Rigid Bodies transcript | Full teacher explanations, warnings and worked-example reasoning. |
| Screenshots PDF | Visual planning only. |

## Specification Alignment

### A22-MOM-LO001

**Official learning outcome:**  
demonstrate understanding of and use moments in simple static contexts, including rods, ladders and hinged beams.

This lesson covers the outcome through:

| Required idea | Lesson section |
|---|---|
| Moment of a force | Core Theory 1 |
| Perpendicular distance | Core Theory 1 and Worked Examples 1 to 3 |
| Static equilibrium | Core Theory 2 |
| Rods | Worked Examples 4 to 8 |
| Ladders | Worked Example 12 |
| Hinged beams | Worked Example 13 |
| Interpreting model assumptions | Core Theory 3, Exam Technique |
| Limiting equilibrium and tilting | Worked Examples 10 to 12 |

## Learning Objectives

By the end of this lesson, you should be able to:

1. define the moment of a force about a point;
2. calculate moments using perpendicular distances;
3. decide whether a moment is clockwise or anticlockwise;
4. use static equilibrium:
   \[
   \text{resultant force}=0,
   \qquad
   \text{resultant moment about any point}=0;
   \]
5. draw force diagrams for rods, beams, ladders and hinged systems;
6. choose a useful point to take moments about;
7. solve for unknown reactions, tensions, masses, distances and coefficients of friction;
8. handle uniform and non-uniform rods;
9. interpret “on the point of tilting” correctly;
10. explain how modelling assumptions such as uniform rod, smooth wall, rough ground and light inextensible string are used.

## Prerequisite Recap: Earlier A-Level Mechanics Only

This lesson does **not** use GCSE sources. The required prior knowledge is from earlier A-Level mechanics and algebra.

| Prior skill | Why it matters here |
|---|---|
| Weight | Convert mass \(m\) kg to weight \(mg\) N. |
| Resolving forces | Use horizontal and vertical equilibrium. |
| Normal reaction | Identify forces from supports, walls, pegs and ground. |
| Tension | Use upward or angled forces in strings and ropes. |
| Friction | In static problems, friction opposes the direction the body would move. |
| \(F\leq \mu R\), and in limiting equilibrium \(F=\mu R\) | Used in rough rods and ladder problems. |
| Trigonometric components | Find perpendicular distances such as \(a\cos\theta\) or \(a\sin\theta\). |
| Algebra | Rearrange linear equations, inequalities and simultaneous equations. |

## Big Picture Explanation

Earlier mechanics often models an object as a **particle**. A particle has no size, so all forces act at one point and you only ask whether the resultant force is zero or non-zero.

A **rigid body** has size. That one change opens the trapdoor into moments.

A force can now do two things:

1. translate the body;
2. rotate the body.

For a static rigid body, neither happens. So the body must satisfy:

\[
\boxed{\text{resultant force in any direction}=0}
\]

and

\[
\boxed{\text{resultant moment about any point}=0}.
\]

That phrase **about any point** is the power-tool. You choose the point. A good choice removes awkward unknowns. A bad choice turns a clean mechanics question into algebra soup.

## Key Definitions and Notation

### Rigid body

A **rigid body** is a body whose size and shape are taken into account and which is assumed not to bend or deform.

For this lesson, rigid bodies usually appear as rods, beams, ladders, hinged rods, or rods resting on supports or pegs.

### Rod

A **rod** is a rigid body whose thickness is ignored. It has length, but negligible width.

### Uniform rod

A rod is **uniform** if its mass is evenly distributed along its length.

Therefore, its weight acts at the midpoint.

If a uniform rod \(AB\) has length \(L\) and mass \(m\), then its weight \(mg\) acts at the midpoint, a distance

\[
\frac{L}{2}
\]

from each end.

### Non-uniform rod

A rod is **non-uniform** if its mass is not evenly distributed.

You cannot assume its weight acts at the midpoint.

Instead, its weight acts at its centre of mass, whose position may be given or may need to be found.

### Moment of a force

The **moment of a force** about a point measures the turning effect of the force about that point.

\[
\boxed{\text{moment of force}=\text{force}\times \text{perpendicular distance from the point to the line of action of the force}}
\]

In symbols:

\[
M = Fd,
\]

where:

- \(M\) is the moment;
- \(F\) is the force;
- \(d\) is the perpendicular distance from the pivot or chosen point to the line of action of the force.

The unit is:

\[
\text{N m}.
\]

### Line of action

The **line of action** of a force is the straight line along which the force acts.

When finding a moment, the distance must be the shortest distance from the chosen point to this line. That means the distance must be perpendicular.

### Clockwise and anticlockwise moments

A force can try to rotate a body clockwise or anticlockwise.

In equilibrium:

\[
\boxed{\text{total clockwise moment}=\text{total anticlockwise moment}}.
\]

### Normal reaction

A normal reaction is the force exerted by a surface on a body, perpendicular to the surface.

Examples:

- A horizontal support gives an upward reaction.
- A smooth vertical wall gives a horizontal reaction.
- A smooth peg touching a rod gives a reaction perpendicular to the rod.
- A hinge may give two components of reaction, usually one horizontal and one vertical.

### Friction

For a rough contact:

\[
F\leq \mu R.
\]

In limiting equilibrium:

\[
F=\mu R.
\]

Friction acts opposite to the direction the body would move if friction were absent.

### On the point of tilting

When a rigid body is on the point of tilting about a pivot, it is about to lift off any other support.

Therefore:

\[
\boxed{\text{reaction at any other support}=0.}
\]

For a suspended system, the matching idea is:

\[
\boxed{\text{tension in any cable or string that is about to go slack}=0.}
\]

## Core Theory

### 1. Moments from perpendicular distances

The formula is:

\[
M = Fd.
\]

The distance \(d\) is not always the labelled length on the rod or diagram. It must be perpendicular to the force.

If the force already acts at right angles to the rod, the perpendicular distance may be the length along the rod.

If the force is vertical and the rod is angled, the perpendicular distance is often a horizontal projection.

For example, if a force \(mg\) acts vertically downward from the midpoint of a rod of length \(3\) m at angle \(50^\circ\) to the horizontal, then the distance from the hinge to the line of action of \(mg\) is:

\[
1.5\cos50^\circ.
\]

So the moment of the weight about the hinge is:

\[
mg(1.5\cos50^\circ).
\]

### 2. Static equilibrium

For a rigid body in equilibrium:

\[
\boxed{\sum F_x=0}
\]

\[
\boxed{\sum F_y=0}
\]

\[
\boxed{\sum M=0}
\]

The evidence repeatedly phrases this as:

\[
\text{forces up}=\text{forces down}
\]

and

\[
\text{clockwise moments}=\text{anticlockwise moments}.
\]

### 3. The two tools

In rigid-body statics, there are only two mathematical actions:

1. **Resolve forces.**
2. **Take moments.**

A good solution usually uses both. The art is choosing the order.

#### When to resolve first

Resolve first when the force equation immediately gives something useful.

Example:

If reactions are \(R\) and \(2R\), and the total downward weight is \(40g+80g\), then:

\[
R+2R=40g+80g
\]

\[
3R=120g
\]

\[
R=40g.
\]

This makes the moments equation much cleaner.

#### When to take moments first

Take moments first when it removes an unknown reaction or tension.

If a rod rests on supports at \(A\) and \(C\), taking moments about \(A\) removes the reaction at \(A\), because its distance from \(A\) is zero.

\[
\text{moment of }R_A\text{ about }A=R_A\times 0=0.
\]

### 4. Choosing where to take moments

Use this decision rule:

\[
\boxed{\text{Take moments about a point where awkward unknown forces act.}}
\]

This usually eliminates those unknowns.

Good moment points are often a support, a hinge, a contact point, a point where a tension acts, a point that makes distances simple, or the point named in the question.

### 5. Uniform versus non-uniform rods

For a uniform rod:

\[
\text{weight acts at the midpoint.}
\]

For a non-uniform rod:

\[
\text{weight acts at its centre of mass, not necessarily at the midpoint.}
\]

If the centre of mass is unknown, assign a variable distance, usually from one end:

\[
x = \text{distance of centre of mass from }A.
\]

Then use moments to find \(x\).

### 6. On the point of tilting

If a beam rests on two supports and is on the point of tilting about support \(D\), then the reaction at the other support is zero.

So if the supports are \(C\) and \(D\):

\[
R_C=0.
\]

Only the pivot support still acts.

### 7. Ladders and rough ground

A common ladder model:

- ladder is a uniform rod;
- ground is rough, so friction acts at the bottom;
- wall is smooth, so only a horizontal reaction acts at the wall;
- weight of ladder acts at midpoint;
- any load acts at its given point;
- limiting equilibrium means friction is at its maximum:
  \[
  F=\mu R.
  \]

### 8. Hinged beams

A hinge can exert two components of reaction:

\[
X \quad \text{horizontal}
\]

and

\[
Y \quad \text{vertical}.
\]

When taking moments about the hinge, both hinge components disappear because their moment arms are zero.

This is why hinged questions often start with:

\[
\text{Take moments about the hinge.}
\]

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22MomentsSVG-001 | Source: MechYr2 Chapter 4 page 2 and transcript intro | Insert from svg/A22MomentsSVG-001.svg | Purpose: Door-handle model showing why greater distance from hinge increases turning effect.]

[VISUAL PLACEHOLDER: A22MomentsSVG-002 | Source: MechYr2 Chapter 4 pages 3-4 | Insert from svg/A22MomentsSVG-002.svg | Purpose: Moment definition diagram showing force, point, line of action and perpendicular distance.]

[VISUAL PLACEHOLDER: A22MomentsSVG-003 | Source: MechYr2 Chapter 4 page 12 and transcript section 2 | Insert from svg/A22MomentsSVG-003.svg | Purpose: Rigid-body equilibrium summary: resultant force zero and resultant moment zero.]

[VISUAL PLACEHOLDER: A22MomentsSVG-004 | Source: Rigid Bodies transcript sections 2-3 | Insert from svg/A22MomentsSVG-004.svg | Purpose: Uniform rod on two supports with reactions and midpoint weight.]

[VISUAL PLACEHOLDER: A22MomentsSVG-005 | Source: MechYr2 Chapter 4 page 14 | Insert from svg/A22MomentsSVG-005.svg | Purpose: Two-support beam with man standing at unknown distance.]

[VISUAL PLACEHOLDER: A22MomentsSVG-006 | Source: Rigid Bodies transcript section 4 | Insert from svg/A22MomentsSVG-006.svg | Purpose: Suspended beam with two vertical tensions.]

[VISUAL PLACEHOLDER: A22MomentsSVG-007 | Source: MechYr2 Chapter 4 pages 17 and transcript section 7 | Insert from svg/A22MomentsSVG-007.svg | Purpose: Non-uniform rod with centre of mass not at midpoint.]

[VISUAL PLACEHOLDER: A22MomentsSVG-008 | Source: MechYr2 Chapter 4 pages 20-22 and transcript section 8 | Insert from svg/A22MomentsSVG-008.svg | Purpose: On-the-point-of-tilting diagram showing reaction at other support equals zero.]

[VISUAL PLACEHOLDER: A22MomentsSVG-009 | Source: MechYr2 Chapter 7 page 15 | Insert from svg/A22MomentsSVG-009.svg | Purpose: Static rough rod resting on ground and smooth peg.]

[VISUAL PLACEHOLDER: A22MomentsSVG-010 | Source: MechYr2 Chapter 7 page 16 | Insert from svg/A22MomentsSVG-010.svg | Purpose: Ladder against smooth wall on rough ground.]

[VISUAL PLACEHOLDER: A22MomentsSVG-011 | Source: Rigid Bodies transcript section 11 | Insert from svg/A22MomentsSVG-011.svg | Purpose: Angled hinged rod held by perpendicular force.]

[INTERACTIVE PLACEHOLDER: A22MomentsWidget-001 | Source: Screenshots PDF PhET balance visuals | Insert from widgets/A22MomentsWidget-001.html | Purpose: Let the student vary force and distance to balance moments.]

## Worked Examples

### Worked Example 1: Basic moment on a seesaw

A force of \(700\text{ N}\) acts \(10\text{ m}\) from point \(A\). Tom has mass \(75\text{ kg}\) and sits \(8\text{ m}\) from point \(A\) on the other side.

Find the two moments about \(A\) and decide which way the seesaw turns.

#### Solution

Moment of the \(700\text{ N}\) force:

\[
M_1=700\times 10
\]

\[
M_1=7000\text{ N m}.
\]

Tom’s weight is:

\[
75g.
\]

Using \(g=9.8\):

\[
75g=75(9.8)=735\text{ N}.
\]

Moment of Tom’s weight:

\[
M_2=75g\times 8
\]

\[
M_2=75(9.8)(8)
\]

\[
M_2=5880\text{ N m}.
\]

Compare:

\[
7000>5880.
\]

Therefore the \(700\text{ N}\) side has the larger moment.

\[
\boxed{\text{The seesaw turns anticlockwise.}}
\]

### Worked Example 2: Moments of two forces on a lamina

A lamina has two forces acting on it about point \(P\):

- \(5\text{ N}\), with perpendicular distance \(2\text{ m}\);
- \(8\text{ N}\), where the distance line is \(2\sin50^\circ\text{ m}\).

Find the moment of each force.

#### Solution

Moment of the \(5\text{ N}\) force:

\[
M_1=5\times 2
\]

\[
M_1=10\text{ N m}.
\]

This moment is clockwise.

Moment of the \(8\text{ N}\) force:

\[
M_2=8\times 2\sin50^\circ
\]

\[
M_2=16\sin50^\circ
\]

\[
M_2=12.2567\ldots
\]

\[
M_2=12.3\text{ N m}\quad (3\text{ sf}).
\]

This moment is anticlockwise.

\[
\boxed{10\text{ N m clockwise},\quad 12.3\text{ N m anticlockwise}.}
\]

### Worked Example 3: Resultant moment with angled forces

A light rod has forces producing the following moment expression about \(P\):

\[
(6\times 3)+(4\times 3\sin40^\circ)-(5\times 4\sin80^\circ).
\]

Calculate the resultant moment and direction.

#### Solution

Calculate each part:

\[
6\times 3=18.
\]

\[
4\times 3\sin40^\circ=12\sin40^\circ.
\]

\[
12\sin40^\circ=7.7134\ldots
\]

So the anticlockwise total is:

\[
18+7.7134\ldots=25.7134\ldots
\]

The clockwise moment is:

\[
5\times 4\sin80^\circ=20\sin80^\circ.
\]

\[
20\sin80^\circ=19.6961\ldots
\]

Resultant moment:

\[
25.7134\ldots-19.6961\ldots=6.0173\ldots
\]

\[
\boxed{6.02\text{ N m anticlockwise}.}
\]

### Worked Example 4: Uniform rod on two supports

A uniform rod \(AB\) has length \(3\text{ m}\) and weight \(20\text{ N}\). It rests horizontally on supports at \(A\) and \(C\), where:

\[
AC=2\text{ m}.
\]

Find the reactions at \(A\) and \(C\).

#### Solution

Let the reactions be:

\[
R_A
\]

and

\[
R_C.
\]

Because the rod is uniform, its weight acts at the midpoint of \(AB\), which is:

\[
1.5\text{ m from }A.
\]

Taking moments about \(A\):

\[
20\times 1.5 = R_C\times 2.
\]

\[
30=2R_C.
\]

\[
R_C=15\text{ N}.
\]

Now resolve vertically:

\[
R_A+R_C=20.
\]

Substitute \(R_C=15\):

\[
R_A+15=20.
\]

\[
R_A=5\text{ N}.
\]

\[
\boxed{R_A=5\text{ N},\quad R_C=15\text{ N}.}
\]

### Worked Example 5: Uniform seesaw with unknown mass

Lewis and Tom are on a uniform seesaw of mass \(20\text{ kg}\). Lewis has mass \(70\text{ kg}\) and is \(10\text{ m}\) from the pivot. Tom is \(8\text{ m}\) from the pivot. The seesaw remains horizontal.

Find:

1. Tom’s mass;
2. the reaction force at the pivot.

#### Solution

Let Tom’s mass be \(m\text{ kg}\).

Lewis’s weight:

\[
70g.
\]

Tom’s weight:

\[
mg.
\]

Seesaw’s weight:

\[
20g.
\]

Because the seesaw is uniform, its weight acts at the midpoint. From the diagram evidence, this gives the weight \(20g\) a moment arm of \(1\text{ m}\) about the pivot.

Taking moments about the pivot:

\[
(20g\times 1)+(70g\times 10)=mg\times 8.
\]

Expand the left side:

\[
20g+700g=8mg.
\]

\[
720g=8mg.
\]

Divide by \(8g\):

\[
m=\frac{720g}{8g}.
\]

\[
m=90.
\]

So Tom’s mass is:

\[
\boxed{90\text{ kg}.}
\]

Now resolve vertically.

The upward reaction \(R\) balances all weights:

\[
R=70g+20g+90g.
\]

\[
R=180g.
\]

Using \(g=9.8\):

\[
R=180(9.8).
\]

\[
R=1764\text{ N}.
\]

\[
\boxed{R=1764\text{ N}.}
\]

### Worked Example 6: Two supports and an unknown position

A uniform beam \(AB\), of mass \(40\text{ kg}\) and length \(5\text{ m}\), rests horizontally on supports at \(C\) and \(D\), where:

\[
AC=DB=1\text{ m}.
\]

A man of mass \(80\text{ kg}\) stands at \(E\). The reaction at \(D\) is twice the reaction at \(C\).

Find:

\[
AE.
\]

#### Solution

Let the reaction at \(C\) be:

\[
R.
\]

Then the reaction at \(D\) is:

\[
2R.
\]

Because the beam is uniform, its weight \(40g\) acts at the midpoint of the \(5\text{ m}\) beam:

\[
2.5\text{ m from }A.
\]

Let:

\[
AE=x.
\]

The man’s weight is:

\[
80g.
\]

Resolve vertically:

\[
R+2R=40g+80g.
\]

\[
3R=120g.
\]

\[
R=40g.
\]

So:

\[
2R=80g.
\]

Now take moments about \(A\).

The clockwise moments from the weights are:

\[
40g\times 2.5
\]

and

\[
80g\times x.
\]

The anticlockwise moments from the reactions are:

\[
40g\times 1
\]

and

\[
80g\times 4.
\]

Therefore:

\[
(40g\times 2.5)+(80g\times x)=(40g\times 1)+(80g\times 4).
\]

Divide through by \(g\):

\[
40(2.5)+80x=40(1)+80(4).
\]

\[
100+80x=40+320.
\]

\[
100+80x=360.
\]

\[
80x=260.
\]

\[
x=\frac{260}{80}.
\]

\[
x=3.25.
\]

\[
\boxed{AE=3.25\text{ m}.}
\]

### Worked Example 7: Suspended beam with two tensions

A uniform rod \(AB\) has length \(4\text{ m}\) and weight \(20\text{ N}\). It is suspended horizontally by two vertical strings attached at \(A\) and \(B\). A particle of weight \(10\text{ N}\) is attached at point \(C\), where:

\[
AC=1.5\text{ m}.
\]

Find the tensions in the two strings.

#### Solution

Let the tensions be:

\[
T_A
\]

and

\[
T_B.
\]

Because the rod is uniform, its weight \(20\text{ N}\) acts at the midpoint:

\[
2\text{ m from }A.
\]

The \(10\text{ N}\) particle acts:

\[
1.5\text{ m from }A.
\]

Take moments about \(A\).

The clockwise moments from the downward forces are:

\[
10\times 1.5
\]

and

\[
20\times 2.
\]

The anticlockwise moment from \(T_B\) is:

\[
T_B\times 4.
\]

So:

\[
(10\times 1.5)+(20\times 2)=4T_B.
\]

\[
15+40=4T_B.
\]

\[
55=4T_B.
\]

\[
T_B=\frac{55}{4}.
\]

\[
T_B=13.75\text{ N}.
\]

\[
T_B=13.8\text{ N}\quad (3\text{ sf}).
\]

Resolve vertically:

\[
T_A+T_B=10+20.
\]

\[
T_A+13.75=30.
\]

\[
T_A=16.25\text{ N}.
\]

\[
T_A=16.3\text{ N}\quad (3\text{ sf}).
\]

\[
\boxed{T_A=16.3\text{ N},\quad T_B=13.8\text{ N}.}
\]

### Worked Example 8: Rope-breaking range

A beam \(AB\) has mass \(12\text{ kg}\) and length \(5\text{ m}\). It is held horizontally by two vertical ropes, one at \(A\) and one at \(C\), where:

\[
BC=1\text{ m}.
\]

Therefore:

\[
AC=4\text{ m}.
\]

A small load of mass \(16\text{ kg}\) is attached at a point \(y\text{ m}\) from \(A\). The rope at \(C\) breaks if its tension exceeds \(98\text{ N}\). Find the range of possible positions where the load can be attached without the rope at \(C\) breaking.

#### Solution

Let the tension at \(C\) be:

\[
T_C.
\]

The beam is uniform, so its weight \(12g\) acts at the midpoint:

\[
2.5\text{ m from }A.
\]

The added load has weight:

\[
16g.
\]

It is attached:

\[
y\text{ m from }A.
\]

Take moments about \(A\).

Clockwise moments from the weights:

\[
12g\times 2.5
\]

and

\[
16g\times y.
\]

Anticlockwise moment from \(T_C\):

\[
T_C\times 4.
\]

So:

\[
12g(2.5)+16gy=4T_C.
\]

\[
30g+16gy=4T_C.
\]

Divide by \(4\):

\[
T_C=7.5g+4gy.
\]

For the rope not to break:

\[
T_C\leq 98.
\]

Substitute:

\[
7.5g+4gy\leq 98.
\]

Using \(g=9.8\):

\[
7.5(9.8)+4(9.8)y\leq 98.
\]

\[
73.5+39.2y\leq 98.
\]

\[
39.2y\leq 24.5.
\]

\[
y\leq \frac{24.5}{39.2}.
\]

\[
y\leq 0.625.
\]

So:

\[
\boxed{y\leq 0.625\text{ m}.}
\]

To two significant figures:

\[
\boxed{y\leq 0.63\text{ m}.}
\]

Since \(y\) is a distance from \(A\), also:

\[
y\geq 0.
\]

Therefore:

\[
\boxed{0\leq y\leq 0.625\text{ m}.}
\]

### Worked Example 9: Non-uniform rod and centre of mass

A non-uniform rod \(AB\) is \(3\text{ m}\) long and has weight \(20\text{ N}\). It rests horizontally on supports at \(C\) and \(D\), where:

\[
AC=1\text{ m}
\]

and

\[
AD=2.5\text{ m}.
\]

The reaction at \(C\) is three times the reaction at \(D\).

Find the distance of the centre of mass from \(A\).

#### Solution

Let the reaction at \(D\) be:

\[
R.
\]

Then the reaction at \(C\) is:

\[
3R.
\]

Let the centre of mass be \(x\text{ m}\) from \(A\).

The weight \(20\text{ N}\) acts at this point.

Resolve vertically:

\[
3R+R=20.
\]

\[
4R=20.
\]

\[
R=5.
\]

Therefore:

\[
3R=15.
\]

Now take moments about \(A\).

The reactions produce one side of the moment equation:

\[
3R\times 1+R\times 2.5.
\]

The weight produces the other side:

\[
20x.
\]

So:

\[
3R(1)+R(2.5)=20x.
\]

Substitute \(R=5\):

\[
3(5)(1)+5(2.5)=20x.
\]

\[
15+12.5=20x.
\]

\[
27.5=20x.
\]

\[
x=\frac{27.5}{20}.
\]

\[
x=1.375.
\]

The answer should be rounded suitably:

\[
\boxed{x=1.38\text{ m from }A\quad (3\text{ sf}).}
\]

### Worked Example 10: On the point of tilting

A uniform rod \(AB\) has length \(4\text{ m}\) and mass \(12\text{ kg}\). It rests horizontally on supports at \(C\) and \(D\), where:

\[
AC=DB=0.5\text{ m}.
\]

A particle of mass \(m\text{ kg}\) is placed at \(B\). The rod is on the point of turning about \(D\).

Find \(m\).

#### Solution

Since the rod is on the point of turning about \(D\), the reaction at \(C\) is zero:

\[
R_C=0.
\]

The rod still touches \(D\), so the reaction at \(D\) may act, but if we take moments about \(D\), that reaction has zero moment.

Because the rod is uniform, its weight \(12g\) acts at the midpoint.

The rod length is \(4\text{ m}\), so its midpoint is \(2\text{ m}\) from \(A\).

Since:

\[
DB=0.5\text{ m},
\]

and:

\[
AB=4\text{ m},
\]

then:

\[
AD=4-0.5=3.5\text{ m}.
\]

The midpoint is \(2\text{ m}\) from \(A\), so the distance from the midpoint to \(D\) is:

\[
3.5-2=1.5\text{ m}.
\]

The particle at \(B\) is \(0.5\text{ m}\) from \(D\).

Take moments about \(D\).

The rod’s weight gives one moment:

\[
12g\times 1.5.
\]

The particle gives the opposing moment:

\[
mg\times 0.5.
\]

So:

\[
12g\times 1.5=mg\times 0.5.
\]

\[
18g=0.5mg.
\]

Divide by \(g\):

\[
18=0.5m.
\]

\[
m=36.
\]

\[
\boxed{m=36\text{ kg}.}
\]

### Worked Example 11: Rough ground and smooth peg

A uniform rod \(AB\) has mass \(40\text{ kg}\) and length \(10\text{ m}\). End \(A\) rests on rough horizontal ground. The rod rests against a smooth peg \(C\), where:

\[
AC=8\text{ m}.
\]

The rod is in limiting equilibrium at an angle of \(15^\circ\) to the horizontal.

Find:

1. the reaction at \(C\);
2. the coefficient of friction between the rod and the ground.

#### Solution

Forces:

- weight \(40g\) acts at the midpoint of the rod;
- reaction at peg \(C\) is \(N\), perpendicular to the rod because the peg is smooth;
- ground reaction at \(A\) is \(R\), vertically upward;
- friction at \(A\) is \(\mu R\).

Since the rod length is \(10\text{ m}\), its midpoint is:

\[
5\text{ m from }A.
\]

The weight acts vertically downward. Its perpendicular distance from \(A\) is the horizontal projection:

\[
5\cos15^\circ.
\]

Take moments about \(A\).

Moment of weight:

\[
40g\times 5\cos15^\circ.
\]

Moment of peg reaction:

\[
N\times 8.
\]

Equilibrium gives:

\[
40g\times 5\cos15^\circ=N\times 8.
\]

\[
N=\frac{40g\times 5\cos15^\circ}{8}.
\]

Using \(g=9.8\):

\[
N=\frac{40(9.8)(5\cos15^\circ)}{8}.
\]

\[
N=236.65\ldots
\]

\[
\boxed{N=240\text{ N}\quad (2\text{ sf}).}
\]

Now resolve horizontally.

The horizontal component of \(N\) is:

\[
N\sin15^\circ.
\]

This is balanced by friction:

\[
\mu R=N\sin15^\circ.
\]

Using \(N=236.65\ldots\):

\[
\mu R=236.65\ldots\sin15^\circ.
\]

\[
\mu R=61.25\ldots
\]

Now resolve vertically.

The vertical forces are:

\[
R+N\cos15^\circ=40g.
\]

So:

\[
R=40g-N\cos15^\circ.
\]

\[
R=40(9.8)-236.65\ldots\cos15^\circ.
\]

\[
R=163.41\ldots
\]

Since the rod is in limiting equilibrium:

\[
F=\mu R.
\]

So:

\[
\mu=\frac{61.25\ldots}{163.41\ldots}.
\]

\[
\mu=0.3748\ldots
\]

\[
\boxed{\mu=0.37\quad (2\text{ sf}).}
\]

### Worked Example 12: Ladder against smooth wall

A ladder \(AB\), of mass \(m\) and length \(3a\), has end \(A\) resting on rough horizontal ground. End \(B\) rests against a smooth vertical wall. A load of mass \(2m\) is fixed on the ladder at point \(C\), where:

\[
AC=a.
\]

The ladder is modelled as a uniform rod and the load as a particle. The ladder rests in limiting equilibrium at an angle of \(60^\circ\) with the ground.

Find the coefficient of friction between the ladder and the ground.

#### Solution

Forces:

- weight of load:
  \[
  2mg
  \]
  acting at \(C\), distance \(a\) from \(A\);
- weight of ladder:
  \[
  mg
  \]
  acting at midpoint, distance \(1.5a\) from \(A\);
- normal reaction at ground:
  \[
  R
  \]
  vertically upward;
- friction at ground:
  \[
  \mu R
  \]
  horizontally;
- reaction at wall:
  \[
  P
  \]
  horizontally, because the wall is smooth.

Resolve horizontally:

\[
\mu R=P.
\]

Resolve vertically:

\[
R=2mg+mg.
\]

\[
R=3mg.
\]

Take moments about \(B\). This avoids needing \(P\), because \(P\) acts at \(B\).

The moment equation from the evidence is:

\[
(2mg\times 2a\cos60^\circ)+(mg\times 1.5a\cos60^\circ)+(\mu R\times 3a\sin60^\circ)=R\times 3a\cos60^\circ.
\]

Simplify each part.

First weight term:

\[
2mg\times 2a\cos60^\circ
\]

\[
=4amg\cos60^\circ
\]

\[
=4amg\left(\frac12\right)
\]

\[
=2amg.
\]

Second weight term:

\[
mg\times 1.5a\cos60^\circ
\]

\[
=1.5amg\left(\frac12\right)
\]

\[
=0.75amg.
\]

So the two weight terms add to:

\[
2amg+0.75amg=2.75amg.
\]

Friction term:

\[
\mu R\times 3a\sin60^\circ
\]

\[
=\mu R\times 3a\left(\frac{\sqrt3}{2}\right)
\]

\[
=\frac{3\sqrt3}{2}a\mu R.
\]

Right side:

\[
R\times 3a\cos60^\circ
\]

\[
=R\times 3a\left(\frac12\right)
\]

\[
=1.5aR.
\]

So:

\[
2.75amg+\frac{3\sqrt3}{2}a\mu R=1.5aR.
\]

Cancel \(a\):

\[
2.75mg+\frac{3\sqrt3}{2}\mu R=1.5R.
\]

Use:

\[
R=3mg.
\]

Substitute:

\[
2.75mg+\frac{3\sqrt3}{2}\mu(3mg)=1.5(3mg).
\]

Divide through by \(mg\):

\[
2.75+\frac{9\sqrt3}{2}\mu=4.5.
\]

Subtract \(2.75\):

\[
\frac{9\sqrt3}{2}\mu=1.75.
\]

\[
\mu=\frac{1.75}{\frac{9\sqrt3}{2}}.
\]

\[
\mu=0.2245\ldots
\]

\[
\boxed{\mu=0.225\quad (3\text{ sf}).}
\]

The assumption that the ladder is uniform is used because its weight acts at its midpoint.

### Worked Example 13: Hinged rod held by a perpendicular force

A uniform rod \(PQ\) is hinged at \(P\). It is held in equilibrium at an angle of \(50^\circ\) to the horizontal by a force of magnitude \(F\), acting perpendicular to the rod at \(Q\). The rod has length \(3\text{ m}\) and mass \(8\text{ kg}\).

Find \(F\).

#### Solution

Forces:

- force \(F\) acts perpendicular to the rod at \(Q\);
- weight \(8g\) acts at the midpoint;
- hinge components act at \(P\), but their moments about \(P\) are zero.

Since the rod is \(3\text{ m}\) long, the midpoint is:

\[
1.5\text{ m from }P.
\]

Take moments about \(P\).

Moment of \(F\):

\[
F\times 3=3F.
\]

Moment of weight:

The weight acts vertically downward, so the perpendicular distance from \(P\) to the line of action of the weight is:

\[
1.5\cos50^\circ.
\]

So the moment of the weight is:

\[
8g(1.5\cos50^\circ).
\]

Equilibrium gives:

\[
3F=8g(1.5\cos50^\circ).
\]

\[
F=\frac{8g(1.5\cos50^\circ)}{3}.
\]

Using \(g=9.8\):

\[
F=\frac{8(9.8)(1.5\cos50^\circ)}{3}.
\]

\[
F=25.197\ldots
\]

\[
\boxed{F=25.2\text{ N}\quad (3\text{ sf}).}
\]

## Guided Practice

### Practice Question 1

A force of \(12\text{ N}\) acts at a perpendicular distance \(0.8\text{ m}\) from point \(P\).

Find the moment about \(P\).

### Practice Question 2

A uniform rod \(AB\) has length \(6\text{ m}\) and weight \(30\text{ N}\). It rests horizontally on supports at \(A\) and \(C\), where:

\[
AC=4\text{ m}.
\]

Find \(R_A\) and \(R_C\).

### Practice Question 3

A uniform beam of mass \(50\text{ kg}\) and length \(8\text{ m}\) rests horizontally on supports at its ends. A particle of mass \(20\text{ kg}\) is placed \(2\text{ m}\) from the left end.

Find the reactions at the two ends.

### Practice Question 4

A non-uniform rod \(AB\) has weight \(24\text{ N}\). It rests horizontally on supports at \(A\) and \(B\), which are \(4\text{ m}\) apart. The reaction at \(A\) is \(15\text{ N}\).

Find the distance of the centre of mass from \(A\).

### Practice Question 5

A uniform rod \(AB\) of length \(5\text{ m}\) and mass \(10\text{ kg}\) rests on supports at \(C\) and \(D\), where:

\[
AC=1\text{ m}
\]

and

\[
DB=1\text{ m}.
\]

A particle of mass \(m\text{ kg}\) is placed at \(B\), and the rod is on the point of tilting about \(D\).

Find \(m\).

### Practice Question 6

A uniform ladder of mass \(20\text{ kg}\) rests in limiting equilibrium against a smooth vertical wall and on rough horizontal ground. The ladder makes an angle of \(60^\circ\) with the ground. No extra load is present.

Find the coefficient of friction at the ground.

## Common Mistakes and Exam Traps

### Trap 1: Using the wrong distance

Moment is:

\[
\text{force}\times \text{perpendicular distance}.
\]

Not:

\[
\text{force}\times \text{nearest labelled length you can see}.
\]

When a rod is angled, distances often become:

\[
a\cos\theta
\]

or

\[
a\sin\theta.
\]

### Trap 2: Mixing force triangles and distance triangles

If the force is \(8g\), that does not appear as a side length in a distance triangle.

A distance triangle contains lengths only.

A force triangle contains forces only.

Do not make a mutant triangle. Mechanics dislikes hybrids.

### Trap 3: Forgetting that mass is not weight

Mass:

\[
m\text{ kg}.
\]

Weight:

\[
mg\text{ N}.
\]

Moments use forces, so use \(mg\), not \(m\).

### Trap 4: Assuming all reactions are equal

Reactions are equal only when symmetry or equations prove they are equal.

If a support is closer to a load, its reaction may be larger.

Use different variables unless equality is given.

### Trap 5: Misreading “reaction at \(D\) is twice reaction at \(C\)”

If:

\[
R_D=2R_C,
\]

then a good variable choice is:

\[
R_C=R,\qquad R_D=2R.
\]

Do not write both as \(R\).

### Trap 6: Forgetting the zero reaction in tilting

If the rod is on the point of tilting about \(D\), the reaction at the other support is zero.

\[
R_C=0.
\]

### Trap 7: Taking moments about a poor point

You can take moments about any point in equilibrium, but not every point is kind to you.

Choose a point that removes an awkward unknown.

### Trap 8: Forgetting to state modelling assumptions

Examples:

- uniform rod means weight acts at midpoint;
- smooth wall means no friction at the wall;
- rough ground means friction may act;
- light string means no weight for the string;
- inextensible string means connected bodies have the same acceleration;
- smooth pulley means tension is the same on both sides.

For this lesson, the pulley and connected-particle assumptions are only background unless used inside a static moments problem.

## Exam Technique Notes

### 1. Start with the diagram

Before writing equations, add weights, reactions, tensions, friction, unknown distances, centre of mass and angle information.

A clean diagram is not decoration. It is the cockpit.

### 2. Label unknowns using the question’s own distance

If the question asks for \(AE\), set:

\[
AE=x.
\]

Do not set a different distance first unless it clearly simplifies the problem.

### 3. Choose moments to remove unknowns

If you do not want \(R_A\), take moments about \(A\).

If you do not want hinge reactions, take moments about the hinge.

### 4. Use exact forms as long as possible

Keep:

\[
g
\]

or exact trig values, such as:

\[
\sin60^\circ=\frac{\sqrt3}{2},
\qquad
\cos60^\circ=\frac12.
\]

Round only at the end.

### 5. Check reasonableness

If a reaction is negative, your assumed direction may be wrong.

If a coefficient of friction is negative, the friction direction is wrong.

If a centre of mass lies outside the rod, check your distances.

If a tension range increases when a load moves away from that rope, check the moment equation.

## Full Worked Solutions to Guided Practice

### Solution 1

\[
M=Fd.
\]

\[
M=12\times 0.8.
\]

\[
M=9.6.
\]

\[
\boxed{9.6\text{ N m}.}
\]

### Solution 2

A uniform rod has weight acting at midpoint.

Rod length:

\[
6\text{ m}.
\]

Midpoint is:

\[
3\text{ m from }A.
\]

Let reactions be:

\[
R_A,\quad R_C.
\]

Take moments about \(A\):

\[
30\times 3=R_C\times 4.
\]

\[
90=4R_C.
\]

\[
R_C=22.5\text{ N}.
\]

Resolve vertically:

\[
R_A+R_C=30.
\]

\[
R_A+22.5=30.
\]

\[
R_A=7.5\text{ N}.
\]

\[
\boxed{R_A=7.5\text{ N},\quad R_C=22.5\text{ N}.}
\]

### Solution 3

Let the left reaction be \(R_L\), and the right reaction be \(R_R\).

The beam has mass \(50\text{ kg}\), so its weight is:

\[
50g.
\]

The beam is uniform, so this acts at the midpoint:

\[
4\text{ m from the left end}.
\]

The particle has mass \(20\text{ kg}\), so its weight is:

\[
20g.
\]

It acts:

\[
2\text{ m from the left end}.
\]

Take moments about the left end:

\[
R_R\times 8=(50g\times 4)+(20g\times 2).
\]

\[
8R_R=200g+40g.
\]

\[
8R_R=240g.
\]

\[
R_R=30g.
\]

\[
R_R=294\text{ N}.
\]

Resolve vertically:

\[
R_L+R_R=50g+20g.
\]

\[
R_L+30g=70g.
\]

\[
R_L=40g.
\]

\[
R_L=392\text{ N}.
\]

\[
\boxed{R_L=392\text{ N},\quad R_R=294\text{ N}.}
\]

### Solution 4

Let the centre of mass be \(x\text{ m}\) from \(A\).

The rod has weight:

\[
24\text{ N}.
\]

The reaction at \(A\) is:

\[
15\text{ N}.
\]

Resolve vertically to find the reaction at \(B\):

\[
R_A+R_B=24.
\]

\[
15+R_B=24.
\]

\[
R_B=9\text{ N}.
\]

Take moments about \(A\):

\[
R_B\times 4=24x.
\]

\[
9\times 4=24x.
\]

\[
36=24x.
\]

\[
x=\frac{36}{24}.
\]

\[
x=1.5.
\]

\[
\boxed{\text{Centre of mass is }1.5\text{ m from }A.}
\]

### Solution 5

Rod length:

\[
5\text{ m}.
\]

Since:

\[
AC=1\text{ m},\qquad DB=1\text{ m},
\]

then:

\[
AD=5-1=4\text{ m}.
\]

Because the rod is uniform, its weight \(10g\) acts at the midpoint:

\[
2.5\text{ m from }A.
\]

Distance from midpoint to \(D\):

\[
4-2.5=1.5\text{ m}.
\]

The particle at \(B\) is:

\[
1\text{ m from }D.
\]

On the point of tilting about \(D\), the reaction at the other support is zero.

Take moments about \(D\):

\[
10g\times 1.5=mg\times 1.
\]

\[
15g=mg.
\]

\[
m=15.
\]

\[
\boxed{m=15\text{ kg}.}
\]

### Solution 6

Forces on the ladder:

- weight \(20g\) acts at the midpoint;
- ground reaction \(R\) acts upward;
- friction \(F\) acts horizontally at ground;
- smooth wall reaction \(P\) acts horizontally at top.

Resolve vertically:

\[
R=20g.
\]

In limiting equilibrium:

\[
F=\mu R.
\]

Resolve horizontally:

\[
F=P.
\]

So:

\[
P=\mu R.
\]

Take moments about the bottom of the ladder.

Let the ladder length be \(L\).

Moment of wall reaction \(P\):

The top of the ladder is at vertical height:

\[
L\sin60^\circ.
\]

So moment of \(P\):

\[
P(L\sin60^\circ).
\]

Moment of weight:

The midpoint is at distance \(\frac{L}{2}\) along the ladder. Its horizontal distance from the bottom is:

\[
\frac{L}{2}\cos60^\circ.
\]

So moment of weight:

\[
20g\left(\frac{L}{2}\cos60^\circ\right).
\]

Equilibrium gives:

\[
P(L\sin60^\circ)=20g\left(\frac{L}{2}\cos60^\circ\right).
\]

Cancel \(L\):

\[
P\sin60^\circ=10g\cos60^\circ.
\]

\[
P=\frac{10g\cos60^\circ}{\sin60^\circ}.
\]

Use:

\[
\cos60^\circ=\frac12,
\qquad
\sin60^\circ=\frac{\sqrt3}{2}.
\]

\[
P=\frac{10g\cdot \frac12}{\frac{\sqrt3}{2}}.
\]

\[
P=\frac{5g}{\frac{\sqrt3}{2}}.
\]

\[
P=\frac{10g}{\sqrt3}.
\]

Since:

\[
P=\mu R
\]

and:

\[
R=20g,
\]

\[
\frac{10g}{\sqrt3}=\mu(20g).
\]

Cancel \(g\):

\[
\frac{10}{\sqrt3}=20\mu.
\]

\[
\mu=\frac{10}{20\sqrt3}.
\]

\[
\mu=\frac{1}{2\sqrt3}.
\]

\[
\mu=0.288675\ldots
\]

\[
\boxed{\mu=0.289\quad (3\text{ sf}).}
\]

## Common CCEA-Style Wording

| Wording | Meaning |
|---|---|
| “The rod is uniform” | Its weight acts at the midpoint. |
| “The rod is non-uniform” | Its weight does not necessarily act at the midpoint. |
| “The ladder is modelled as a uniform rod” | Treat its weight as acting at its midpoint. |
| “The wall is smooth” | No friction at the wall. |
| “The ground is rough” | Friction acts at the ground. |
| “Limiting equilibrium” | Friction has reached its maximum: \(F=\mu R\). |
| “On the point of tilting about \(A\)” | Reactions at other supports are zero. |
| “Hinged at \(A\)” | The hinge may exert horizontal and vertical components, both with zero moment about \(A\). |
| “Light string” | Ignore the string’s weight. |
| “Inextensible string” | Connected objects have the same acceleration, if dynamics is involved. |
| “Smooth pulley” | Tension is the same on both sides of the pulley. |

## Syllabus Gap Check

| LO ID | Requirement | Covered? | Evidence-backed coverage |
|---|---|---:|---|
| A22-MOM-LO001 | Moments in simple static contexts | Yes | Moment definition, moment equations, static equilibrium. |
| A22-MOM-LO001 | Rods | Yes | Uniform rods, non-uniform rods, supported rods, suspended rods. |
| A22-MOM-LO001 | Ladders | Yes | Ladder against smooth wall and rough ground. |
| A22-MOM-LO001 | Hinged beams | Yes | Hinged rod held by perpendicular force and hinge reaction discussion. |

## Off-Spec Content Found but Excluded

The following appeared in the evidence but is not treated as required core content for this A22-MOM lesson:

| Evidence content | Decision |
|---|---|
| Particle-only equilibrium examples | Used only as prior A-Level mechanics recap. |
| Particles moving on rough planes | Excluded from core. |
| Connected particles with friction | Excluded from core. |
| Pulley acceleration systems | Excluded from core unless used only to explain modelling assumptions. |
| Edexcel M1 old questions | Used only as cross-board practice style where content matches moments. |

## Optional Enrichment Not Required by CCEA

| Enrichment | Why it may help |
|---|---|
| PhET balance simulation | Builds intuition for balancing moments. |
| Resultant moment problems where the body is not in equilibrium | Helps understand why equilibrium means zero resultant moment. |
| Cross-board exam questions | Useful extra practice, but not official CCEA evidence. |

## Visual and Interactive Asset Plan

| Asset ID | Type | Planned file | Purpose |
|---|---|---|---|
| A22MomentsSVG-001 | SVG | svg/A22MomentsSVG-001.svg | Door hinge moment intuition. |
| A22MomentsSVG-002 | SVG | svg/A22MomentsSVG-002.svg | Force, point, line of action and perpendicular distance. |
| A22MomentsSVG-003 | SVG | svg/A22MomentsSVG-003.svg | Rigid-body equilibrium summary. |
| A22MomentsSVG-004 | SVG | svg/A22MomentsSVG-004.svg | Uniform rod on supports. |
| A22MomentsSVG-005 | SVG | svg/A22MomentsSVG-005.svg | Two-support beam with unknown position. |
| A22MomentsSVG-006 | SVG | svg/A22MomentsSVG-006.svg | Suspended beam with tensions. |
| A22MomentsSVG-007 | SVG | svg/A22MomentsSVG-007.svg | Non-uniform centre of mass. |
| A22MomentsSVG-008 | SVG | svg/A22MomentsSVG-008.svg | Point of tilting. |
| A22MomentsSVG-009 | SVG | svg/A22MomentsSVG-009.svg | Rough ground and smooth peg. |
| A22MomentsSVG-010 | SVG | svg/A22MomentsSVG-010.svg | Ladder against smooth wall. |
| A22MomentsSVG-011 | SVG | svg/A22MomentsSVG-011.svg | Hinged rod with perpendicular force. |
| A22MomentsWidget-001 | HTML widget | widgets/A22MomentsWidget-001.html | Balance moments interactively. |

## Supplementary Sources Used

| Source | Status |
|---|---|
| DrFrost Chapter 4 Moments | Non-CCEA teaching evidence, used only where matching A22 moments. |
| DrFrost Chapter 7 Applications of Forces | Non-CCEA teaching evidence, used only for static rigid-body moments. |
| Edexcel M1 references inside slides/transcript | Cross-board, used as practice-style evidence only. |
| Pearson textbook references inside slides/transcript | Referenced through uploaded slides only, not independently verified. |
| PhET screenshot evidence | Visual support only, optional enrichment. |

## Final Student Checklist

Before moving on, check that you can do each item without notes.

| Skill | Ready? |
|---|---|
| I can define the moment of a force. |  |
| I know the distance must be perpendicular to the line of action of the force. |  |
| I can decide clockwise versus anticlockwise moments. |  |
| I can use \(\text{clockwise moments}=\text{anticlockwise moments}\). |  |
| I can use \(\sum F_x=0\) and \(\sum F_y=0\). |  |
| I can draw reactions, tensions, weights and friction on a rigid-body diagram. |  |
| I know that a uniform rod’s weight acts at its midpoint. |  |
| I know that a non-uniform rod’s weight acts at its centre of mass, not necessarily its midpoint. |  |
| I can choose a point to take moments about to eliminate unknowns. |  |
| I can solve rod-on-support problems. |  |
| I can solve suspended-beam tension problems. |  |
| I can handle “on the point of tilting”. |  |
| I can solve a ladder problem with rough ground and smooth wall. |  |
| I can solve a hinge problem by taking moments about the hinge. |  |
| I can state how modelling assumptions are used. |  |
| I can round final answers appropriately and keep exact working until the end. |  |

## Phase Status

| Item | Status |
|---|---|
| Phase 0 Evidence Intake and Plan | Complete |
| Phase 1 Main Lesson Markdown | Complete |
| Phase 2 Mermaid Assets | Complete |
| Phase 3 SVG Assets | Complete |
| Phase 4 TikZ Assets | Complete |
| Phase 5 Widget Assets | Complete |
| Phase 6 Manifest and Packaging | Complete |
