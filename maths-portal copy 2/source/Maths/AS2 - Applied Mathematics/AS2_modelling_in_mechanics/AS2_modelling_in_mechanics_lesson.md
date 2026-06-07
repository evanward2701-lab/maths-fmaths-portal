# AS2 Modelling in Mechanics

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | AS2: AS 2 Applied Mathematics |
| Applied section | Mechanics |
| Primary official topic | AS2-QUNITS: Quantities and units in mechanics |
| Linked official topics | AS2-KIN: Kinematics; AS2-FORCES: Forces and Newton's laws |
| Lesson title | Modelling in Mechanics |
| topic_slug | modelling_in_mechanics |
| topic_pascal | ModellingInMechanics |
| topic_id | AS2ModellingInMechanics |
| lesson_file | AS2_modelling_in_mechanics_lesson.md |

## Evidence Map

This lesson uses the CCEA specification map as the syllabus authority and the uploaded lesson materials as lesson evidence. The evidence introduces mechanics as the study of **motion**, **forces**, and the way they are connected, then builds the vocabulary of modelling assumptions, SI units, scalar quantities, vector quantities and component conversion.

| Evidence source | Status | Use in lesson |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Available | Authority for AS2 unit identity, topic codes, LO IDs and boundaries. |
| Project README module map | Available | Authority for file naming, phases, metadata and pack structure. |
| Project evidence checklist | Available | Authority for missing evidence, visual evidence and off-spec logging. |
| MechYr1-Chp8-Introduction.pdf | Available | Core lesson evidence for overview, assumptions, SI units, scalar/vector content, worked examples and practice prompts. |
| Chapter_8_Modelling_in_Mechanics_Transcript.md | Available | Teacher explanation, modelling consequences, warnings and worked-example reasoning. |
| Chapter_8_Modelling_in_Mechanics_Screenshots.pdf | Available but visual-only | Used as visual confirmation only; no parsed text was available. |

## Specification Alignment

| Lesson section | LO IDs |
|---|---|
| SI units | AS2-QUNITS-LO001, AS2-QUNITS-LO002 |
| Scalar and vector quantities | AS2-KIN-LO001, AS1-VEC-LO001, AS1-VEC-LO002 |
| Mechanics overview | AS2-KIN-LO001, AS2-KIN-LO002, AS2-KIN-LO003, AS2-FORCES-LO001, AS2-FORCES-LO004 |
| Force diagrams and force types | AS2-FORCES-LO001, AS2-FORCES-LO002, AS2-FORCES-LO003 |
| Modelling assumptions | AS2-FORCES-LO008, AS2-FORCES-LO009, AS2-FORCES-LO010 |
| Component conversion examples | AS1-VEC-LO002, AS2-KIN-LO004, AS2-FORCES-LO002 |

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain what mechanics studies: **motion**, **forces**, and the connection between them.
2. Use the required SI units for mechanics.
3. Distinguish between scalar and vector quantities.
4. Convert a 2D vector to scalar magnitude using Pythagoras.
5. Convert a magnitude and direction into vector/component form using trigonometry.
6. Recognise common modelling assumptions and state their mathematical consequences.
7. Explain why modelling assumptions are mathematical instructions, not decorative wording.

## Prerequisite Recap

No external GCSE material is used here. The required prior mathematical tools are:

- Pythagoras' theorem:

  $$
  \text{magnitude}=\sqrt{x^2+y^2}
  $$

- Basic trigonometry in a right-angled triangle:

  $$
  \cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}},
  \qquad
  \sin\theta=\frac{\text{opposite}}{\text{hypotenuse}},
  \qquad
  \tan\theta=\frac{\text{opposite}}{\text{adjacent}}.
  $$

- Unit vector notation:

  $$
  \mathbf{i}=\text{unit vector in the positive }x\text{-direction},
  \qquad
  \mathbf{j}=\text{unit vector in the positive }y\text{-direction}.
  $$

- Column vector notation:

  $$
  \begin{pmatrix}x\\y\end{pmatrix}
  $$

  means \(x\) units horizontally and \(y\) units vertically.

## Big Picture Explanation

Mechanics is the mathematical study of how objects move and why they move.

The evidence describes mechanics as concerning:

$$
\text{motion},\qquad \text{forces},\qquad \text{and how the two interrelate}.
$$

That gives the whole AS mechanics story:

$$
\boxed{\text{Forces}}
\quad
\longleftrightarrow
\quad
\boxed{F=ma}
\quad
\longleftrightarrow
\quad
\boxed{\text{Motion}}.
$$

The bridge is Newton's second law:

$$
F=ma.
$$

This connects:

- \(F\), the resultant force;
- \(m\), the mass;
- \(a\), the acceleration.

So mechanics is not a heap of unrelated formulae. It is a small engine room:

$$
\text{forces produce acceleration, and acceleration changes motion.}
$$

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-001 | Source: MechYr1-Chp8-Introduction.pdf p.3 | Insert from svg/AS2ModellingInMechanicsSVG-001.svg | Purpose: Show the overview map linking forces, \(F=ma\), and motion.]

## Key Definitions and Notation

### Scalar quantity

A **scalar quantity** has magnitude only.

Magnitude means size.

Examples from the evidence:

| Scalar form | Meaning |
|---|---|
| Distance | How far travelled, with no direction |
| Speed | How fast moving, with no direction |

A distance of \(5\,\text{m}\) is scalar because it only says how large the distance is. It does not say which way the movement is directed.

A scalar distance is always positive:

$$
5\,\text{m}>0.
$$

### Vector quantity

A **vector quantity** has magnitude and direction.

Examples from the evidence:

| Scalar form | Vector form |
|---|---|
| Distance | Displacement |
| Speed | Velocity |

Other quantities which can be vectors or scalars:

$$
\text{force},\qquad \text{acceleration}.
$$

Quantities which can only be scalars:

$$
\text{time},\qquad \text{mass}.
$$

### One-dimensional vectors

A one-dimensional vector can look like a scalar because we do not usually write it in brackets.

But it is still a vector because it has direction.

If the positive direction is to the right, then moving \(3\,\text{m}\) to the left gives:

$$
\text{distance}=3\,\text{m},
$$

but

$$
\text{displacement}=-3\,\text{m}.
$$

That negative sign is direction encoded inside the number.

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-002 | Source: MechYr1-Chp8-Introduction.pdf p.6 | Insert from svg/AS2ModellingInMechanicsSVG-002.svg | Purpose: Show scalar distance versus vector displacement on a one-dimensional line.]

## Core Theory

## 1. SI Units

The SI system is the standard international system of units.

The evidence gives the following units:

| Quantity | Unit | Symbol |
|---|---|---|
| Mass | kilogram | \(\text{kg}\) |
| Length/displacement | metre | \(\text{m}\) |
| Time | seconds | \(\text{s}\) |
| Speed/velocity | metres per second | \(\text{m s}^{-1}\) |
| Acceleration | metres per second per second | \(\text{m s}^{-2}\) |
| Force/weight | newton | \(\text{N}=\text{kg m s}^{-2}\) |

### Important unit warnings

Mass must be in kilograms:

$$
1000\,\text{g}=1\,\text{kg}.
$$

Length or displacement must be in metres:

$$
100\,\text{cm}=1\,\text{m}.
$$

Speed and velocity must be in metres per second:

$$
\text{m s}^{-1}=\frac{\text{m}}{\text{s}}.
$$

Acceleration must be in metres per second per second:

$$
\text{m s}^{-2}=\frac{\text{m}}{\text{s}^2}.
$$

Force is measured in newtons:

$$
1\,\text{N}=1\,\text{kg m s}^{-2}.
$$

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-003 | Source: MechYr1-Chp8-Introduction.pdf p.5 | Insert from svg/AS2ModellingInMechanicsSVG-003.svg | Purpose: Present the SI units table for fundamental and derived mechanics quantities.]

## 2. Motion Vocabulary

The evidence introduces five key constant-acceleration quantities, often called SUVAT:

| Symbol | Meaning |
|---|---|
| \(s\) | displacement |
| \(u\) | initial velocity |
| \(v\) | final velocity |
| \(a\) | acceleration |
| \(t\) | time |

The evidence previews these constant acceleration formulae:

$$
s=ut+\frac12at^2,
$$

$$
s=\left(\frac{u+v}{2}\right)t,
$$

$$
v^2=u^2+2as,
$$

$$
v=u+at.
$$

These are previewed here only. A later kinematics lesson teaches when and how to choose each one.

## 3. Motion Graphs

The evidence previews two graph facts.

For a displacement-time graph:

$$
\text{gradient}=\text{velocity}.
$$

For a velocity-time graph:

$$
\text{gradient}=\text{acceleration},
$$

and

$$
\text{area under graph}=\text{distance travelled}.
$$

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-004 | Source: MechYr1-Chp8-Introduction.pdf p.3 | Insert from svg/AS2ModellingInMechanicsSVG-004.svg | Purpose: Show displacement-time and velocity-time graph interpretations.]

## 4. Non-constant Acceleration Preview

The evidence gives this example:

$$
s=2t^3+3t.
$$

Velocity is the derivative of displacement with respect to time:

$$
v=\frac{ds}{dt}.
$$

Differentiate term by term:

$$
\frac{d}{dt}(2t^3)=6t^2,
$$

$$
\frac{d}{dt}(3t)=3.
$$

Therefore:

$$
v=\frac{ds}{dt}=6t^2+3.
$$

This is a future-facing idea. For this AS2 introduction, it is only included to show that calculus can connect displacement, velocity and acceleration when acceleration is not constant.

## 5. Force Vocabulary

The evidence's force diagram includes:

| Force | Meaning |
|---|---|
| Weight | The force due to gravity, acting vertically downwards |
| Friction | A force that resists motion |
| Tension | A pulling force in a string |
| Reaction force | The force from a surface that prevents an object sinking into it |

Forces can be treated as vectors because they have direction.

The magnitude of the force vector gives the size of the force.

If an object is stationary, Newton's first law means the forces balance:

$$
\text{force left}=\text{force right},
$$

and

$$
\text{force up}=\text{force down}.
$$

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-005 | Source: MechYr1-Chp8-Introduction.pdf p.3 | Insert from svg/AS2ModellingInMechanicsSVG-005.svg | Purpose: Show the object on a table with weight, reaction, friction and tension.]

## 6. Modelling Assumptions

In mechanics, a model is a simplified version of a real situation.

The evidence states that modelling assumptions are made:

$$
\text{to make the maths cleaner or to use well-known mathematical approaches.}
$$

### Common assumptions

| Assumption | Meaning | Mathematical consequence |
|---|---|---|
| Particle | Dimensions of object are negligible | Mass is concentrated at a single point; rotational forces and air resistance can be ignored |
| Rough surface | Object in contact with the surface experiences friction | Friction must be considered |
| Smooth surface | Object in contact with the surface does not experience friction | Friction can be ignored |
| Smooth/light pulley | No friction; pulley has no mass | Tension is the same in the string either side of the pulley |
| Inextensible string | String does not stretch under load | Acceleration is the same in any connected objects |
| Rod | One dimension is negligible, like a pole or beam | Mass is concentrated along a line; rigid |
| Peg/support | A support from which a body can be suspended or rested | Dimensionless and fixed; can be rough or smooth depending on question |

[VISUAL PLACEHOLDER: AS2ModellingInMechanicsSVG-006 | Source: MechYr1-Chp8-Introduction.pdf p.4 | Insert from svg/AS2ModellingInMechanicsSVG-006.svg | Purpose: Create modelling assumption cards for particle, rough/smooth surface, pulley, inextensible string, rod and peg/support.]

### Assumption: particle

If a body is modelled as a particle, then its dimensions are negligible.

That means:

$$
\text{mass concentrated at a single point}.
$$

So the model can ignore:

$$
\text{air resistance},
$$

and

$$
\text{rotation/spin}.
$$

### Assumption: smooth surface

If a surface is smooth:

$$
\text{friction}=0.
$$

### Assumption: rough surface

If a surface is rough:

$$
\text{friction is present}.
$$

### Assumption: light string

The transcript explains that a light string is used in calculations by treating the tension as equal throughout the string.

So if a light string has tension \(T\), then:

$$
T_{\text{top}}=T_{\text{bottom}}.
$$

The important exam idea is not only:

$$
\text{the string has no mass}.
$$

The useful calculation consequence is:

$$
\boxed{\text{tension is equal throughout the string}.}
$$

### Assumption: inextensible string

An inextensible string does not stretch.

If two particles are connected by an inextensible string, then they have the same acceleration.

So:

$$
a_1=a_2.
$$

The useful calculation consequence is:

$$
\boxed{\text{connected particles have the same acceleration}.}
$$

### Assumption: smooth pulley

A smooth pulley has no friction.

The useful calculation consequence is:

$$
\boxed{\text{tension is equal on either side of the pulley}.}
$$

So if a string passes over a smooth pulley:

$$
T_{\text{left}}=T_{\text{right}}.
$$

## Visual Asset Integration

The lesson includes placeholders for diagrams and one interactive widget. The actual asset files are included in the pack subfolders.

| Asset ID | Type | Purpose |
|---|---|---|
| AS2ModellingInMechanicsSVG-001 | SVG | Mechanics overview map |
| AS2ModellingInMechanicsSVG-002 | SVG | Scalar versus vector one-dimensional displacement |
| AS2ModellingInMechanicsSVG-003 | SVG | SI units table |
| AS2ModellingInMechanicsSVG-004 | SVG | Motion graphs |
| AS2ModellingInMechanicsSVG-005 | SVG | Force diagram |
| AS2ModellingInMechanicsSVG-006 | SVG | Modelling assumptions cards |
| AS2ModellingInMechanicsSVG-007 | SVG | Vector component triangles |
| AS2ModellingInMechanicsWidget-001 | HTML widget | Interactive vector resolver |

[INTERACTIVE PLACEHOLDER: AS2ModellingInMechanicsWidget-001 | Source: Evidence-based teaching enhancement | Insert from widgets/AS2ModellingInMechanicsWidget-001.html | Purpose: Let students adjust magnitude and angle to see horizontal and vertical vector components.]

# Worked Examples

## Worked Example 1: Convert scalar magnitude and angle to vector form

A displacement has magnitude \(5\,\text{m}\) and makes an angle of \(60^\circ\) above the positive horizontal direction.

Find the vector form.

### Step 1: Draw the component triangle

Let the horizontal component be \(x\).

Let the vertical component be \(y\).

The hypotenuse is \(5\).

The angle with the horizontal is \(60^\circ\).

### Step 2: Find the horizontal component

Use cosine because the horizontal side is adjacent to the angle:

$$
\cos 60^\circ=\frac{x}{5}.
$$

Multiply both sides by \(5\):

$$
x=5\cos 60^\circ.
$$

Since the vector points to the right, this component is positive.

### Step 3: Find the vertical component

Use sine because the vertical side is opposite the angle:

$$
\sin 60^\circ=\frac{y}{5}.
$$

Multiply both sides by \(5\):

$$
y=5\sin 60^\circ.
$$

Since the vector points upwards, this component is positive.

### Step 4: Write the vector

$$
\begin{pmatrix}
5\cos60^\circ\\
5\sin60^\circ
\end{pmatrix}
\text{m}.
$$

Evaluate:

$$
5\cos60^\circ=2.5,
$$

$$
5\sin60^\circ=4.33\ldots.
$$

So:

$$
\boxed{
\begin{pmatrix}
2.5\\
4.33
\end{pmatrix}
\text{m}
}
$$

to 3 significant figures.

## Worked Example 2: Convert vector velocity to scalar speed

A velocity is:

$$
\begin{pmatrix}
5\\
-12
\end{pmatrix}
\text{m s}^{-1}.
$$

Find the speed.

Speed is the magnitude of velocity.

Use Pythagoras:

$$
\text{speed}=\sqrt{5^2+(-12)^2}.
$$

Square each component:

$$
5^2=25,
$$

$$
(-12)^2=144.
$$

Add:

$$
25+144=169.
$$

Take the square root:

$$
\sqrt{169}=13.
$$

Therefore:

$$
\boxed{13\,\text{m s}^{-1}}.
$$

## Worked Example 3: Convert a force into vector form

A force of \(8\,\text{N}\) acts \(45^\circ\) below the positive horizontal direction.

Find its vector form.

### Step 1: Identify directions

The force points:

$$
\text{right and down}.
$$

So:

$$
x\text{-component is positive},
$$

$$
y\text{-component is negative}.
$$

### Step 2: Horizontal component

The horizontal component is adjacent to the angle:

$$
8\cos45^\circ.
$$

### Step 3: Vertical component

The vertical component is opposite the angle:

$$
8\sin45^\circ.
$$

But it acts downwards, so it is negative:

$$
-8\sin45^\circ.
$$

### Step 4: Write vector form

$$
\begin{pmatrix}
8\cos45^\circ\\
-8\sin45^\circ
\end{pmatrix}
\text{N}.
$$

Evaluate:

$$
8\cos45^\circ=8\cdot\frac{\sqrt2}{2}=4\sqrt2,
$$

$$
-8\sin45^\circ=-8\cdot\frac{\sqrt2}{2}=-4\sqrt2.
$$

Therefore:

$$
\boxed{
\begin{pmatrix}
4\sqrt2\\
-4\sqrt2
\end{pmatrix}
\text{N}
}.
$$

## Worked Example 4: Force acting down and left

A force of \(6\,\text{N}\) acts down and left, with the angle arranged so that the components are:

$$
-6\sin60^\circ
$$

horizontally and

$$
-6\cos60^\circ
$$

vertically.

Write the force in vector form.

Since the force points left:

$$
x<0.
$$

Since the force points down:

$$
y<0.
$$

So:

$$
\begin{pmatrix}
-6\sin60^\circ\\
-6\cos60^\circ
\end{pmatrix}
\text{N}.
$$

Evaluate the horizontal component:

$$
-6\sin60^\circ
=
-6\cdot\frac{\sqrt3}{2}
=
-3\sqrt3.
$$

Evaluate the vertical component:

$$
-6\cos60^\circ
=
-6\cdot\frac12
=
-3.
$$

Therefore:

$$
\boxed{
\begin{pmatrix}
-3\sqrt3\\
-3
\end{pmatrix}
\text{N}
}.
$$

## Worked Example 5: Convert acceleration vector to scalar magnitude

An acceleration is:

$$
(6\mathbf{i}-8\mathbf{j})\,\text{m s}^{-2}.
$$

This is the same as:

$$
\begin{pmatrix}
6\\
-8
\end{pmatrix}
\text{m s}^{-2}.
$$

Find the magnitude.

$$
|\mathbf{a}|=\sqrt{6^2+(-8)^2}.
$$

Square each component:

$$
6^2=36,
$$

$$
(-8)^2=64.
$$

Add:

$$
36+64=100.
$$

Take the square root:

$$
\sqrt{100}=10.
$$

Therefore:

$$
\boxed{10\,\text{m s}^{-2}}.
$$

## Worked Example 6: Displacement in \(\mathbf{i},\mathbf{j}\) form

A displacement of \(4\,\text{m}\) acts up and left with the components:

$$
-4\cos30^\circ
$$

horizontally and

$$
4\sin30^\circ
$$

vertically.

Write it in \(\mathbf{i},\mathbf{j}\) form.

The horizontal direction is left, so it is negative:

$$
-4\cos30^\circ.
$$

The vertical direction is up, so it is positive:

$$
4\sin30^\circ.
$$

Therefore:

$$
\text{displacement}
=
(-4\cos30^\circ)\mathbf{i}
+
(4\sin30^\circ)\mathbf{j}.
$$

Evaluate:

$$
-4\cos30^\circ
=
-4\cdot\frac{\sqrt3}{2}
=
-2\sqrt3.
$$

$$
4\sin30^\circ
=
4\cdot\frac12
=
2.
$$

Therefore:

$$
\boxed{
(-2\sqrt3\mathbf{i}+2\mathbf{j})\,\text{m}
}.
$$

## Worked Example 7: Resultant displacement and total distance

A man walks from \(A\) to \(B\) and then from \(B\) to \(C\).

His displacement from \(A\) to \(B\) is:

$$
6\mathbf{i}+4\mathbf{j}\,\text{m}.
$$

His displacement from \(B\) to \(C\) is:

$$
5\mathbf{i}-12\mathbf{j}\,\text{m}.
$$

### Part (a): Find the magnitude of the displacement from \(A\) to \(C\)

The displacement from \(A\) to \(C\) is:

$$
\overrightarrow{AC}
=
\overrightarrow{AB}
+
\overrightarrow{BC}.
$$

Substitute:

$$
\overrightarrow{AC}
=
(6\mathbf{i}+4\mathbf{j})
+
(5\mathbf{i}-12\mathbf{j}).
$$

Collect \(\mathbf{i}\) components:

$$
6\mathbf{i}+5\mathbf{i}=11\mathbf{i}.
$$

Collect \(\mathbf{j}\) components:

$$
4\mathbf{j}-12\mathbf{j}=-8\mathbf{j}.
$$

So:

$$
\overrightarrow{AC}=11\mathbf{i}-8\mathbf{j}.
$$

Now find the magnitude:

$$
|\overrightarrow{AC}|
=
\sqrt{11^2+(-8)^2}.
$$

Square each component:

$$
11^2=121,
$$

$$
(-8)^2=64.
$$

Add:

$$
121+64=185.
$$

Take the square root:

$$
\sqrt{185}=13.601\ldots.
$$

Therefore:

$$
\boxed{|\overrightarrow{AC}|=13.6\,\text{m}}
$$

to 3 significant figures.

### Part (b): Find the total distance walked

Total distance is not the magnitude of the final displacement.

It is:

$$
|\overrightarrow{AB}|+|\overrightarrow{BC}|.
$$

First:

$$
|\overrightarrow{AB}|
=
\sqrt{6^2+4^2}.
$$

$$
6^2=36,
\qquad
4^2=16.
$$

$$
36+16=52.
$$

$$
\sqrt{52}=7.211\ldots.
$$

So:

$$
|\overrightarrow{AB}|=7.21\,\text{m}.
$$

Next:

$$
|\overrightarrow{BC}|
=
\sqrt{5^2+(-12)^2}.
$$

$$
5^2=25,
\qquad
(-12)^2=144.
$$

$$
25+144=169.
$$

$$
\sqrt{169}=13.
$$

So:

$$
|\overrightarrow{BC}|=13\,\text{m}.
$$

Total distance:

$$
7.21+13=20.21.
$$

Therefore:

$$
\boxed{20.21\,\text{m}}.
$$

**Evidence note:** the slide solution appears to display kilometres, but the question statement uses metres. This CCEA-clean solution keeps metres.

## Worked Example 8: Angle made with the unit vector \(\mathbf{i}\)

A raccoon has velocity:

$$
\begin{pmatrix}
3\\
-1
\end{pmatrix}
\text{m s}^{-1}.
$$

Determine the angle its trajectory makes with the unit vector \(\mathbf{i}\).

The vector means:

$$
3 \text{ units to the right},
$$

and

$$
1 \text{ unit down}.
$$

Let the angle below the positive \(\mathbf{i}\)-direction be \(\theta\).

Use tangent:

$$
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}.
$$

Here:

$$
\text{opposite}=1,
$$

$$
\text{adjacent}=3.
$$

So:

$$
\tan\theta=\frac13.
$$

Apply inverse tangent:

$$
\theta=\tan^{-1}\left(\frac13\right).
$$

Calculate:

$$
\theta=18.4349\ldots^\circ.
$$

To 3 significant figures:

$$
\theta=18.4^\circ.
$$

The direction matters. Since the vector has a negative vertical component, it points below \(\mathbf{i}\).

Therefore:

$$
\boxed{18.4^\circ \text{ below the unit vector }\mathbf{i}}.
$$

## Guided Practice

### Question 1

Convert this velocity to a speed:

$$
\begin{pmatrix}
9\\
12
\end{pmatrix}
\text{m s}^{-1}.
$$

### Question 2

A force of \(10\,\text{N}\) acts right and down at \(30^\circ\) to the horizontal.

Write the force in vector form.

### Question 3

A particle moves \(7\mathbf{i}+24\mathbf{j}\) metres.

Find the magnitude of its displacement.

### Question 4

Explain the modelling consequence of each assumption:

a. the string is inextensible;

b. the pulley is smooth;

c. the body is modelled as a particle.

## Common Mistakes and Exam Traps

### Trap 1: Treating displacement and distance as the same

Distance is scalar.

Displacement is vector.

For the man walking example:

$$
|\overrightarrow{AC}|\ne |\overrightarrow{AB}|+|\overrightarrow{BC}|.
$$

The first is final displacement magnitude.

The second is total distance travelled.

### Trap 2: Forgetting signs in vector components

Right is positive.

Up is positive.

Left is negative.

Down is negative.

So for a vector acting down and left:

$$
\begin{pmatrix}
-\\
-
\end{pmatrix}.
$$

For a vector acting right and down:

$$
\begin{pmatrix}
+\\
-
\end{pmatrix}.
$$

### Trap 3: Writing only “light string means no mass”

That may define the assumption, but the calculation consequence is usually:

$$
\boxed{\text{tension is equal throughout the string}.}
$$

### Trap 4: Writing only “inextensible means does not stretch”

That may define the assumption, but the calculation consequence is usually:

$$
\boxed{\text{connected particles have the same acceleration}.}
$$

### Trap 5: Giving an angle without direction

For the raccoon example, this is incomplete:

$$
18.4^\circ.
$$

This is complete:

$$
18.4^\circ \text{ below the unit vector }\mathbf{i}.
$$

## Exam Technique

When converting magnitude and angle into vector form:

1. Draw a component triangle.
2. Decide which component is adjacent to the angle.
3. Decide which component is opposite the angle.
4. Use:

   $$
   F\cos\theta
   $$

   for the side adjacent to the angle.

5. Use:

   $$
   F\sin\theta
   $$

   for the side opposite the angle.

6. Add signs last:
   - right \(+\),
   - up \(+\),
   - left \(-\),
   - down \(-\).

When converting vector form to scalar magnitude:

$$
\text{magnitude}=\sqrt{x^2+y^2}.
$$

Always square the negative component using brackets:

$$
(-12)^2=144,
$$

not

$$
-12^2=-144.
$$

## Full Worked Solutions to Guided Practice

### Solution 1

Velocity:

$$
\begin{pmatrix}
9\\
12
\end{pmatrix}
\text{m s}^{-1}.
$$

Speed is magnitude:

$$
\text{speed}=\sqrt{9^2+12^2}.
$$

Square:

$$
9^2=81,
$$

$$
12^2=144.
$$

Add:

$$
81+144=225.
$$

Take the square root:

$$
\sqrt{225}=15.
$$

Therefore:

$$
\boxed{15\,\text{m s}^{-1}}.
$$

### Solution 2

A force of \(10\,\text{N}\) acts right and down at \(30^\circ\) to the horizontal.

Horizontal component is adjacent:

$$
10\cos30^\circ.
$$

Vertical component is opposite:

$$
10\sin30^\circ.
$$

Since the force acts down, the vertical component is negative:

$$
-10\sin30^\circ.
$$

So the vector is:

$$
\begin{pmatrix}
10\cos30^\circ\\
-10\sin30^\circ
\end{pmatrix}
\text{N}.
$$

Evaluate:

$$
10\cos30^\circ
=
10\cdot\frac{\sqrt3}{2}
=
5\sqrt3.
$$

$$
-10\sin30^\circ
=
-10\cdot\frac12
=
-5.
$$

Therefore:

$$
\boxed{
\begin{pmatrix}
5\sqrt3\\
-5
\end{pmatrix}
\text{N}
}.
$$

### Solution 3

Displacement:

$$
7\mathbf{i}+24\mathbf{j}.
$$

Magnitude:

$$
\sqrt{7^2+24^2}.
$$

Square:

$$
7^2=49,
$$

$$
24^2=576.
$$

Add:

$$
49+576=625.
$$

Take the square root:

$$
\sqrt{625}=25.
$$

Therefore:

$$
\boxed{25\,\text{m}}.
$$

### Solution 4

a. Inextensible string:

$$
\boxed{\text{the connected objects have the same acceleration}.}
$$

b. Smooth pulley:

$$
\boxed{\text{the tension is the same on either side of the pulley}.}
$$

c. Particle:

$$
\boxed{\text{the dimensions are negligible, so mass is treated as concentrated at a single point}.}
$$

This can also allow rotational effects and air resistance to be ignored, depending on context.

## Common CCEA-Style Wording

Questions may use phrases such as:

- model the object as a particle;
- the string is light and inextensible;
- the pulley is smooth;
- the surface is rough or smooth;
- find the magnitude of the velocity;
- find the angle the trajectory makes with \(\mathbf{i}\);
- state the modelling assumption used.

When asked for a modelling assumption, write the consequence that affects the mathematics.

## Syllabus Gap Check

| LO ID | Coverage status |
|---|---|
| AS2-QUNITS-LO001 | Covered |
| AS2-QUNITS-LO002 | Covered |
| AS2-KIN-LO001 | Covered |
| AS2-KIN-LO002 | Preview only |
| AS2-KIN-LO003 | Preview only |
| AS2-KIN-LO004 | Bridge through vector components |
| AS2-FORCES-LO001 | Preview only |
| AS2-FORCES-LO002 | Bridge through resolving components |
| AS2-FORCES-LO003 | Preview only |
| AS2-FORCES-LO004 | Preview only through \(F=ma\) |
| AS2-FORCES-LO008 | Preview through connected-particle assumptions |
| AS2-FORCES-LO009 | Preview through equilibrium language |
| AS2-FORCES-LO010 | Vocabulary preview through rough/smooth surfaces |

## Visual and Interactive Asset Plan

| Asset | Status |
|---|---|
| Mermaid diagrams | Generated in `mermaid/` |
| SVG diagrams | Generated in `svg/` |
| TikZ diagrams | Generated in `tikz/` |
| Interactive widget | Generated in `widgets/` |

## Supplementary Sources Used

The lesson evidence is third-party A-Level mechanics support, not a CCEA source. It is used only because its content aligns with the supplied CCEA AS2 mechanics specification boundaries. Cross-board advertising references from the PDF are not used as lesson content.

## Final Student Checklist

Before moving on, the student should be able to say yes to each statement:

| Skill | Check |
|---|---|
| I know the SI units for mass, length, time, velocity, acceleration and force | ☐ |
| I can explain the difference between distance and displacement | ☐ |
| I can explain the difference between speed and velocity | ☐ |
| I can find the magnitude of a vector using Pythagoras | ☐ |
| I can convert a magnitude and angle into vector form | ☐ |
| I can decide whether a component should be positive or negative | ☐ |
| I can explain what a particle model means | ☐ |
| I can explain what a smooth surface means | ☐ |
| I can explain what an inextensible string means in calculations | ☐ |
| I can explain what a smooth pulley means in calculations | ☐ |
| I understand that \(F=ma\) is the bridge between force and motion | ☐ |

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix and topic identity are correct | Passed: AS2 with primary AS2-QUNITS and linked AS2-KIN/AS2-FORCES |
| LO IDs are preserved exactly | Passed |
| On-spec evidence is covered | Passed |
| Off-spec material is excluded or marked | Passed |
| Placeholders match actual files | Passed |
| Manifest and source reference are updated | Passed |
| Unresolved issues | None found after checking logged limitations |
