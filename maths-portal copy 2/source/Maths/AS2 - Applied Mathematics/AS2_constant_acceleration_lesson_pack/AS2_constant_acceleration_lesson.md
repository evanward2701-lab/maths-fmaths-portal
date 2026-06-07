# AS2 Constant Acceleration Lesson

## Title and Metadata

**Course:** CCEA GCE Mathematics  
**Unit code:** AS2  
**Unit name:** AS 2 Applied Mathematics  
**Applied section:** Mechanics  
**Topic code:** AS2-KIN  
**Official topic name:** Kinematics  
**Lesson focus:** Constant Acceleration  
**Topic slug:** constant_acceleration  
**Topic Pascal:** ConstantAcceleration  
**Topic ID:** AS2ConstantAcceleration  
**Lesson file:** AS2_constant_acceleration_lesson.md

### Primary Learning Outcomes

- **AS2-KIN-LO001:** demonstrate understanding of and use the language of kinematics: position, displacement, distance travelled, velocity, speed and acceleration
- **AS2-KIN-LO002:** demonstrate understanding of, use and interpret graphs in kinematics for motion in a straight line: displacement against time and interpretation of gradient; velocity against time and interpretation of gradient and area under the graph
- **AS2-KIN-LO003:** demonstrate understanding of and use the formulae for constant acceleration for motion in a straight line

### Linked Supporting Learning Outcomes

- **AS2-FORCES-LO005:** demonstrate understanding of and use the gravitational acceleration, \(g\), and its value in SI units to varying degrees of accuracy
- **AS2-FORCES-LO006:** demonstrate understanding of and use weight and motion in a straight line under gravity

### Syllabus Gap Logged

- **AS2-KIN-LO004:** demonstrate understanding of and use the constant acceleration formulae in two dimensions using vectors. This is on-spec for AS2 Kinematics, but the supplied Constant Acceleration evidence focuses on straight-line motion, graph methods, SUVAT and vertical motion under gravity. It is logged for a future lesson.

---

## Evidence Map

| Source | Evidence role | Lesson use |
|---|---|---|
| CCEA specification map | Authority for AS2-KIN topic and LO IDs | Defines syllabus boundary and learning outcome alignment |
| README-Module-Map | Project metadata and file structure rules | Determines naming, phase structure and placeholder format |
| Source-Evidence-Drop-Checklist | Project evidence quality rules | Determines missing evidence log, off-spec log and asset placeholder rules |
| MechYr1 Chapter 9 Constant Acceleration PDF | Main mathematical slide evidence | Definitions, graphs, SUVAT formulae, examples and vertical motion |
| Teacher transcript | Explanation and method evidence | Warnings, reasoning, exam technique and step-by-step commentary |
| Screenshots PDF | Visual evidence | Confirms diagrams and slide visuals for placeholders |
| Embedded textbook examples in slides | Worked example evidence | Used only where question text and solutions are visible in the uploaded evidence |

---

## Specification Alignment

| LO ID | Lesson coverage | Evidence-backed content |
|---|---|---|
| AS2-KIN-LO001 | Strong | Position, displacement, distance travelled, velocity, speed and acceleration |
| AS2-KIN-LO002 | Strong | Displacement-time graphs, velocity-time graphs, gradients and areas |
| AS2-KIN-LO003 | Strong | Derivation and application of constant-acceleration formulae |
| AS2-KIN-LO004 | Not covered | Logged as a gap because 2D vector SUVAT is not in the supplied evidence |
| AS2-FORCES-LO005 | Supporting | Use of \(g=9.8\,\text{m s}^{-2}\) |
| AS2-FORCES-LO006 | Supporting | Straight-line vertical motion under gravity |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain the difference between distance and displacement.
2. Explain the difference between speed and velocity.
3. Find velocity from the gradient of a displacement-time graph.
4. Find acceleration from the gradient of a velocity-time graph.
5. Find displacement or distance travelled using the area under a velocity-time graph.
6. Use trapezium areas confidently in velocity-time graph problems.
7. Define \(s,u,v,a,t\) and select the correct SUVAT equation.
8. Derive the main SUVAT formulae from a velocity-time graph.
9. Use SUVAT formulae only when acceleration is constant.
10. Apply SUVAT to vertical motion under gravity using a consistent sign convention.
11. Use \(g=9.8\,\text{m s}^{-2}\) unless a question states otherwise.
12. Interpret multiple time solutions in quadratic SUVAT problems.

---

## Prerequisite Recap

No GCSE sources are used as lesson evidence. The lesson assumes prior fluency with gradient, area of a trapezium, solving linear and quadratic equations, using units and interpreting directed quantities.

| Prior skill | Why it matters here |
|---|---|
| Gradient of a straight line | Used for velocity from displacement-time graphs and acceleration from velocity-time graphs |
| Area of a trapezium | Used for displacement from velocity-time graphs |
| Algebraic rearrangement | Used in deriving and solving SUVAT formulae |
| Quadratic equations | Used when \(s=ut+\frac12at^2\) gives two possible times |
| Unit conversion | Used when speeds are given in \(\text{km h}^{-1}\) but mechanics calculations require SI units |
| Directed quantities | Used for velocity, displacement and acceleration signs |

---

## Big Picture Explanation

Constant acceleration is the first major engine-room topic in AS mechanics. It turns motion from something we describe into something we can calculate. The four connected parts are:

1. **Displacement-time graphs:** gradient gives velocity.
2. **Velocity-time graphs:** gradient gives acceleration and area gives displacement or distance travelled.
3. **SUVAT formulae:** shortcuts for constant-acceleration motion, derived from the velocity-time graph.
4. **Vertical motion under gravity:** constant acceleration with \(g=9.8\,\text{m s}^{-2}\) acting downwards.

> Golden rule: use SUVAT only when acceleration is constant.

---

## Key Definitions and Notation

### Position

**Position** describes where an object is relative to a chosen origin.

### Displacement

**Displacement** is the change in position from the starting point to the finishing point. It has direction.

If a cyclist travels \(5\text{ km}\) away from home and returns home, her final displacement from home is

\[
0.
\]

### Distance travelled

**Distance travelled** is the total length of the path followed.

If a cyclist travels \(5\text{ km}\) out and \(5\text{ km}\) back, the total distance travelled is

\[
5+5=10\text{ km}.
\]

### Velocity

**Velocity** is the rate of change of displacement.

\[
\text{Average velocity}=\frac{\text{displacement from starting point}}{\text{time taken}}.
\]

Velocity has direction.

### Speed

**Speed** is the rate of change of distance travelled.

\[
\text{Average speed}=\frac{\text{total distance travelled}}{\text{time taken}}.
\]

Speed does not need a direction.

### Acceleration

**Acceleration** is the rate of change of velocity.

\[
a=\frac{\text{change in velocity}}{\text{time taken}}.
\]

If velocity decreases, acceleration may be negative relative to the chosen positive direction.

### Deceleration

**Deceleration** means slowing down. In calculations, it is often represented by a negative acceleration if the positive direction is chosen as the direction of motion.

For example, a deceleration of \(1.5\,\text{m s}^{-2}\) may be written as

\[
a=-1.5\,\text{m s}^{-2}
\]

when positive is taken in the original direction of motion.

### SUVAT notation

For constant acceleration in a straight line:

| Symbol | Meaning |
|---|---|
| \(s\) | displacement |
| \(u\) | initial velocity |
| \(v\) | final velocity |
| \(a\) | acceleration |
| \(t\) | time |

Each SUVAT equation connects four of these five quantities.

---

## Core Theory

## 1. Displacement-Time Graphs

On a displacement-time graph:

- the horizontal axis is time,
- the vertical axis is displacement,
- the gradient gives velocity.

### Stationary object

If displacement does not change as time passes, the graph is horizontal.

\[
\text{gradient}=0
\]

so

\[
\text{velocity}=0.
\]

### Constant velocity

If displacement increases at a constant rate, the graph is a straight sloping line. The gradient is constant, so velocity is constant.

### Accelerating object

If the displacement-time graph gets steeper, the velocity is increasing. That means the object is accelerating.

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-001 | Source: MechYr1 Chapter 9 PDF, displacement-time graph recap | Insert from svg/AS2ConstantAccelerationSVG-001.svg | Purpose: Show stationary motion, constant velocity and accelerating motion on displacement-time graphs.]

---

## 2. Velocity-Time Graphs

On a velocity-time graph:

- the horizontal axis is time,
- the vertical axis is velocity,
- the gradient gives acceleration,
- the area under the graph gives displacement or distance travelled, depending on whether direction changes are involved.

### Stationary object

If the velocity is \(0\) for all time, the graph is a horizontal line on the time axis.

\[
v=0.
\]

### Constant velocity

If velocity is constant, the graph is horizontal above the time axis. The gradient is

\[
0,
\]

so the acceleration is

\[
0.
\]

### Constant acceleration

If velocity increases at a constant rate, the velocity-time graph is a straight sloping line. The gradient is constant, so acceleration is constant.

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-002 | Source: MechYr1 Chapter 9 PDF, velocity-time graph recap | Insert from svg/AS2ConstantAccelerationSVG-002.svg | Purpose: Show stationary motion, constant velocity and constant acceleration on velocity-time graphs.]

---

## 3. Area Under a Velocity-Time Graph

For a constant velocity rectangle:

\[
\text{distance}=\text{speed}\times\text{time}.
\]

On a velocity-time graph:

\[
\text{height}=\text{velocity},\qquad \text{width}=\text{time}.
\]

So the area of the rectangle is

\[
\text{area}=\text{velocity}\times\text{time}.
\]

Therefore,

\[
\text{area under a velocity-time graph}=\text{distance travelled}
\]

for non-negative velocity.

When the shape is a trapezium, use

\[
\text{Area of trapezium}=\frac12(a+b)h,
\]

where \(a\) and \(b\) are the parallel sides and \(h\) is the distance between them.

**Exam warning:** Do not split trapezia into rectangles and triangles unless there is a clear reason. The evidence repeatedly recommends using the trapezium formula because algebraic graph questions become cleaner.

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-003 | Source: MechYr1 Chapter 9 PDF and transcript, velocity-time area explanation | Insert from svg/AS2ConstantAccelerationSVG-003.svg | Purpose: Show why area under a velocity-time graph gives distance or displacement.]

---

## 4. First SUVAT Formula: \(v=u+at\)

For constant acceleration, the velocity-time graph is a straight line from initial velocity \(u\) to final velocity \(v\) over time \(t\).

The acceleration is the gradient of the velocity-time graph:

\[
a=\frac{\text{change in velocity}}{\text{change in time}}.
\]

The change in velocity is

\[
v-u.
\]

The change in time is

\[
t.
\]

So

\[
a=\frac{v-u}{t}.
\]

Multiply both sides by \(t\):

\[
at=v-u.
\]

Add \(u\) to both sides:

\[
u+at=v.
\]

Therefore,

\[
\boxed{v=u+at}.
\]

---

## 5. Second SUVAT Formula: \(s=\left(\frac{u+v}{2}\right)t\)

The displacement is the area under the velocity-time graph. For a straight-line velocity-time graph from \(u\) to \(v\), the area is a trapezium.

The parallel sides are

\[
u\quad\text{and}\quad v.
\]

The distance between them is

\[
t.
\]

So

\[
s=\frac{u+v}{2}\times t.
\]

Therefore,

\[
\boxed{s=\left(\frac{u+v}{2}\right)t}.
\]

This is the A-Level version of

\[
\text{distance}=\text{average speed}\times\text{time}.
\]

---

## 6. Third SUVAT Formula: \(v^2=u^2+2as\)

Start with

\[
v=u+at.
\]

Rearrange to make \(t\) the subject:

\[
v-u=at,
\]

so

\[
t=\frac{v-u}{a}.
\]

Now use

\[
s=\left(\frac{u+v}{2}\right)t.
\]

Substitute \(t=\frac{v-u}{a}\):

\[
s=\left(\frac{u+v}{2}\right)\left(\frac{v-u}{a}\right).
\]

Multiply both sides by \(2a\):

\[
2as=(u+v)(v-u).
\]

Use the difference of two squares:

\[
(u+v)(v-u)=v^2-u^2.
\]

So

\[
2as=v^2-u^2.
\]

Add \(u^2\) to both sides:

\[
u^2+2as=v^2.
\]

Therefore,

\[
\boxed{v^2=u^2+2as}.
\]

---

## 7. Fourth SUVAT Formula: \(s=ut+\frac12at^2\)

Start with

\[
s=\left(\frac{u+v}{2}\right)t.
\]

Use

\[
v=u+at.
\]

Substitute \(u+at\) for \(v\):

\[
s=\left(\frac{u+(u+at)}{2}\right)t.
\]

Simplify inside the bracket:

\[
u+(u+at)=2u+at.
\]

So

\[
s=\left(\frac{2u+at}{2}\right)t.
\]

Split the fraction:

\[
\frac{2u+at}{2}=u+\frac12at.
\]

Therefore,

\[
s=\left(u+\frac12at\right)t.
\]

Multiply by \(t\):

\[
s=ut+\frac12at^2.
\]

Therefore,

\[
\boxed{s=ut+\frac12at^2}.
\]

This formula is a quadratic in \(t\), so it can produce two times.

---

## 8. Fifth SUVAT Formula: \(s=vt-\frac12at^2\)

Start with

\[
v=u+at.
\]

Make \(u\) the subject:

\[
u=v-at.
\]

Now use

\[
s=\left(\frac{u+v}{2}\right)t.
\]

Substitute \(v-at\) for \(u\):

\[
s=\left(\frac{(v-at)+v}{2}\right)t.
\]

Simplify inside the bracket:

\[
(v-at)+v=2v-at.
\]

So

\[
s=\left(\frac{2v-at}{2}\right)t.
\]

Split the fraction:

\[
\frac{2v-at}{2}=v-\frac12at.
\]

Therefore,

\[
s=\left(v-\frac12at\right)t.
\]

Multiply by \(t\):

\[
s=vt-\frac12at^2.
\]

Therefore,

\[
\boxed{s=vt-\frac12at^2}.
\]

---

## 9. The SUVAT Formula Set

\[
\boxed{v=u+at}
\]

\[
\boxed{s=\left(\frac{u+v}{2}\right)t}
\]

\[
\boxed{v^2=u^2+2as}
\]

\[
\boxed{s=ut+\frac12at^2}
\]

\[
\boxed{s=vt-\frac12at^2}
\]

### Method for choosing a formula

Write down all five letters first:

\[
s,\quad u,\quad v,\quad a,\quad t.
\]

Then fill in what you know and mark what you want. Choose the equation that includes the quantity you want, includes the known quantities and excludes the irrelevant or missing quantity.

---

## 10. Vertical Motion Under Gravity

If there is no air resistance, objects moving under gravity have constant acceleration.

Near the surface of the Earth, use

\[
g=9.8\,\text{m s}^{-2}
\]

unless the question states otherwise.

Gravity acts downwards. If **upwards is positive**, then

\[
a=-9.8.
\]

If **downwards is positive**, then

\[
a=+9.8.
\]

The sign convention is a choice, but it must be consistent within each equation.

### Important warning

Do not use \(10\) or \(9.81\) for \(g\) unless instructed. Because \(g=9.8\) is given to 2 significant figures, answers in vertical motion questions are often rounded to 2 significant figures unless the question or mark scheme suggests otherwise.

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-004 | Source: MechYr1 Chapter 9 PDF, vertical motion under gravity | Insert from svg/AS2ConstantAccelerationSVG-004.svg | Purpose: Show upward-positive and downward-positive sign conventions.]

---

# Visual Asset Integration

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-001 | Source: MechYr1 Chapter 9 PDF, displacement-time graph recap | Insert from svg/AS2ConstantAccelerationSVG-001.svg | Purpose: Compare stationary motion, constant velocity and acceleration on displacement-time graphs.]

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-002 | Source: MechYr1 Chapter 9 PDF, velocity-time graph recap | Insert from svg/AS2ConstantAccelerationSVG-002.svg | Purpose: Compare stationary motion, constant velocity and constant acceleration on velocity-time graphs.]

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-003 | Source: MechYr1 Chapter 9 PDF and transcript, velocity-time graph area | Insert from svg/AS2ConstantAccelerationSVG-003.svg | Purpose: Show area under a velocity-time graph as distance or displacement.]

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-004 | Source: MechYr1 Chapter 9 PDF, vertical motion under gravity | Insert from svg/AS2ConstantAccelerationSVG-004.svg | Purpose: Show sign convention choices for vertical motion.]

[VISUAL PLACEHOLDER: AS2ConstantAccelerationSVG-005 | Source: MechYr1 Chapter 9 PDF, SUVAT derivation graph | Insert from svg/AS2ConstantAccelerationSVG-005.svg | Purpose: Derive SUVAT formulae from a straight-line velocity-time graph.]

[INTERACTIVE PLACEHOLDER: AS2ConstantAccelerationWidget-001 | Source: Teaching enhancement based on supplied SUVAT evidence | Insert from widgets/AS2ConstantAccelerationWidget-001.html | Purpose: Let students choose known SUVAT quantities and identify the correct formula.]

[INTERACTIVE PLACEHOLDER: AS2ConstantAccelerationWidget-002 | Source: Teaching enhancement based on vertical motion examples | Insert from widgets/AS2ConstantAccelerationWidget-002.html | Purpose: Show how changing the positive direction changes signs but not the physical answer.]

---

# Worked Examples

## Worked Example 1: Displacement-Time Graph and Average Velocity

A cyclist rides in a straight line for \(20\) minutes. She waits for half an hour, then returns in a straight line to her starting point in \(15\) minutes.

The displacement-time graph has points:

\[
O=(0,0),\quad A=(20,5),\quad B=(50,5),\quad C=(65,0),
\]

where time is in minutes and displacement is in kilometres.

### Part (a): Average velocity for each stage in \(\text{km h}^{-1}\)

#### Stage \(OA\)

\[
\text{average velocity}=\frac{5}{20}=0.25\text{ km min}^{-1}.
\]

Convert to \(\text{km h}^{-1}\):

\[
0.25\times 60=15.
\]

\[
\boxed{15\text{ km h}^{-1}}
\]

#### Stage \(AB\)

The displacement does not change, so

\[
\boxed{0\text{ km h}^{-1}}.
\]

#### Stage \(BC\)

\[
\text{change in displacement}=0-5=-5\text{ km}.
\]

\[
\text{time}=65-50=15\text{ min}.
\]

\[
\text{average velocity}=\frac{-5}{15}=-\frac13\text{ km min}^{-1}.
\]

Convert:

\[
-\frac13\times 60=-20.
\]

\[
\boxed{-20\text{ km h}^{-1}}
\]

or \(20\text{ km h}^{-1}\) towards the starting point.

### Part (b): Average velocity for the whole journey

The cyclist finishes where she started, so total displacement is \(0\). Hence

\[
\text{average velocity}=\frac{0}{65}=0.
\]

\[
\boxed{0\text{ km h}^{-1}}
\]

### Part (c): Average speed for the whole journey

Total distance travelled:

\[
5+5=10\text{ km}.
\]

Total time:

\[
65\text{ min}.
\]

\[
\text{average speed}=\frac{10}{65}=\frac{2}{13}\text{ km min}^{-1}.
\]

Convert to \(\text{km h}^{-1}\):

\[
\frac{2}{13}\times 60=\frac{120}{13}=9.2307\ldots
\]

\[
\boxed{9.23\text{ km h}^{-1}\text{ to 3 significant figures}}
\]

### Key lesson

Average velocity can be \(0\) even when a journey has happened, because displacement can be \(0\). Average speed uses total distance travelled.

---

## Worked Example 2: Velocity-Time Graph, Area and Deceleration

A cyclist moves along a straight road for \(12\) seconds. For the first \(8\) seconds, she moves at a constant speed of \(6\,\text{m s}^{-1}\). She then decelerates uniformly, stopping after a further \(4\) seconds.

### Part (a): Displacement after \(12\) seconds

The graph forms a trapezium. The parallel sides are \(8\) and \(12\), and the height is \(6\):

\[
\text{area}=\frac{8+12}{2}\times 6=\frac{20}{2}\times 6=10\times 6=60.
\]

\[
\boxed{60\text{ m}}
\]

### Part (b): Rate of deceleration

\[
a=\frac{\Delta v}{\Delta t}=\frac{0-6}{12-8}=\frac{-6}{4}=-1.5.
\]

The acceleration is \(-1.5\,\text{m s}^{-2}\), so the deceleration is

\[
\boxed{1.5\,\text{m s}^{-2}}.
\]

---

## Worked Example 3: Algebraic Velocity-Time Graph

A particle accelerates uniformly from rest to \(8\,\text{m s}^{-1}\) in \(T\) seconds, travels at \(8\,\text{m s}^{-1}\) for \(5T\) seconds, then decelerates uniformly to rest in a further \(40\) seconds. The total displacement is \(600\text{ m}\). Find \(T\).

The velocity-time graph is a trapezium. Upper parallel side:

\[
5T.
\]

Lower parallel side:

\[
T+5T+40=6T+40.
\]

Height:

\[
8.
\]

Use area:

\[
\frac{5T+(6T+40)}{2}\times 8=600.
\]

Simplify:

\[
\frac{11T+40}{2}\times 8=600.
\]

\[
4(11T+40)=600.
\]

\[
44T+160=600.
\]

\[
44T=440.
\]

\[
T=10.
\]

\[
\boxed{T=10\text{ s}}
\]

---

## Worked Example 4: SUVAT with \(s\) and \(a\)

A cyclist accelerates at a constant rate from \(4\,\text{m s}^{-1}\) to \(7.5\,\text{m s}^{-1}\) in \(40\) seconds. Find the distance travelled and acceleration.

List values:

\[
u=4,\quad v=7.5,\quad t=40.
\]

### Part (a): Distance travelled

\[
s=\left(\frac{u+v}{2}\right)t.
\]

\[
s=\left(\frac{4+7.5}{2}\right)40=\left(\frac{11.5}{2}\right)40=5.75\times 40=230.
\]

\[
\boxed{230\text{ m}}
\]

### Part (b): Acceleration

\[
v=u+at.
\]

\[
7.5=4+40a.
\]

\[
3.5=40a.
\]

\[
a=\frac{3.5}{40}=0.0875.
\]

\[
\boxed{0.0875\,\text{m s}^{-2}}
\]

---

## Worked Example 5: Constant Deceleration and Direction

A particle moves from \(A\) to \(B\) with constant deceleration \(1.5\,\text{m s}^{-2}\). The velocity at \(A\) is \(8\,\text{m s}^{-1}\), and the velocity at \(B\) is \(2\,\text{m s}^{-1}\). Take \(AB\) as positive.

Because the particle is decelerating:

\[
a=-1.5.
\]

### Part (a): Time from \(A\) to \(B\)

\[
v=u+at.
\]

\[
2=8-1.5t.
\]

\[
-6=-1.5t.
\]

\[
t=4.
\]

\[
\boxed{4\text{ s}}
\]

### Part (b): Distance from \(A\) to \(B\)

\[
s=\left(\frac{8+2}{2}\right)4=5\times 4=20.
\]

\[
\boxed{20\text{ m}}
\]

### Part (c): Velocity after 6 seconds from \(A\)

\[
v=8+(-1.5)(6)=8-9=-1.
\]

So the particle is moving at

\[
\boxed{1\,\text{m s}^{-1}\text{ in the direction }BA}.
\]

### Part (d): Displacement from \(A\) after 6 seconds

\[
s=\left(\frac{8+(-1)}{2}\right)6=\frac72\times 6=21.
\]

\[
\boxed{21\text{ m}}
\]

---

## Worked Example 6: Unit Conversion Before SUVAT

A car starts from rest. After \(30\) seconds it passes a speed-trap at \(45\,\text{km h}^{-1}\). Find the acceleration and distance from the traffic lights.

Convert:

\[
45\times \frac{1000}{3600}=45\times\frac{5}{18}=\frac{225}{18}=12.5\,\text{m s}^{-1}.
\]

So

\[
u=0,\quad v=12.5,\quad t=30.
\]

### Acceleration

\[
12.5=0+30a.
\]

\[
a=\frac{12.5}{30}=\frac{25}{60}=\frac{5}{12}.
\]

\[
\boxed{\frac{5}{12}\,\text{m s}^{-2}}
\]

### Distance

\[
s=\left(\frac{0+12.5}{2}\right)30=6.25\times 30=187.5.
\]

\[
\boxed{187.5\text{ m}}
\]

---

## Worked Example 7: SUVAT Without Time

A particle moves from \(A\) to \(B\) with constant acceleration \(5\,\text{m s}^{-2}\). Its velocity at \(A\) is \(3\,\text{m s}^{-1}\), and its velocity at \(B\) is \(18\,\text{m s}^{-1}\). Find \(AB\).

\[
u=3,\quad v=18,\quad a=5,\quad s=?
\]

Use

\[
v^2=u^2+2as.
\]

\[
18^2=3^2+2(5)s.
\]

\[
324=9+10s.
\]

\[
315=10s.
\]

\[
s=31.5.
\]

\[
\boxed{31.5\text{ m}}
\]

---

## Worked Example 8: Two Times from a Quadratic

A particle passes through \(O\) with speed \(13\,\text{m s}^{-1}\) towards \(A\), where \(OA=20\text{ m}\), with constant deceleration \(4\,\text{m s}^{-2}\). Take \(OA\) as positive.

\[
u=13,\quad a=-4.
\]

### Times when the particle passes through \(A\)

At \(A\), \(s=20\). Use

\[
s=ut+\frac12at^2.
\]

\[
20=13t+\frac12(-4)t^2.
\]

\[
20=13t-2t^2.
\]

\[
2t^2-13t+20=0.
\]

\[
(2t-5)(t-4)=0.
\]

\[
t=\frac52\quad\text{or}\quad t=4.
\]

\[
\boxed{t=2.5\text{ s and }t=4\text{ s}}
\]

The two times occur because the particle passes \(A\), slows, turns around, and passes \(A\) again.

### Time when the particle returns to \(O\)

At \(O\), \(s=0\):

\[
0=13t-2t^2.
\]

\[
0=t(13-2t).
\]

\[
t=0\quad\text{or}\quad t=\frac{13}{2}=6.5.
\]

The \(t=0\) solution is the start. Therefore the return time is

\[
\boxed{6.5\text{ s}}.
\]

---

## Worked Example 9: A Falling Book

A book falls from a shelf \(1.4\text{ m}\) above the floor. Find the time to reach the floor and impact speed. Take downwards as positive.

\[
s=1.4,\quad u=0,\quad a=+9.8.
\]

### Time

\[
s=ut+\frac12at^2.
\]

\[
1.4=0+\frac12(9.8)t^2=4.9t^2.
\]

\[
t^2=\frac{1.4}{4.9}=0.285714\ldots
\]

\[
t=0.5345\ldots
\]

\[
\boxed{0.53\text{ s}}
\]

### Speed

\[
v^2=u^2+2as.
\]

\[
v^2=0^2+2(9.8)(1.4)=27.44.
\]

\[
v=\sqrt{27.44}=5.238\ldots
\]

\[
\boxed{5.2\,\text{m s}^{-1}}
\]

---

## Worked Example 10: A Ball Projected Upwards from a Height

A ball is projected vertically upwards from a point \(X\), which is \(7\text{ m}\) above the ground, with speed \(21\,\text{m s}^{-1}\). Take upwards as positive.

\[
a=-9.8.
\]

### Greatest height above ground

At greatest height, \(v=0\). From \(X\):

\[
u=21,\quad v=0,\quad a=-9.8,\quad s=?
\]

\[
v^2=u^2+2as.
\]

\[
0^2=21^2+2(-9.8)s.
\]

\[
0=441-19.6s.
\]

\[
19.6s=441.
\]

\[
s=\frac{441}{19.6}=22.5.
\]

This is the height gained above \(X\). Greatest height above the ground:

\[
22.5+7=29.5.
\]

\[
\boxed{29.5\text{ m}}
\]

### Time of flight

From \(X\) to the ground:

\[
s=-7.
\]

\[
-7=21t+\frac12(-9.8)t^2.
\]

\[
-7=21t-4.9t^2.
\]

\[
4.9t^2-21t-7=0.
\]

Solving gives

\[
t=4.5965\ldots\quad\text{or}\quad t=-0.3108\ldots
\]

Reject the negative time. Therefore

\[
\boxed{4.6\text{ s}}
\]

to 2 significant figures.

---

## Worked Example 11: Time Above a Height

A ball is projected vertically upwards from ground level at \(20\,\text{m s}^{-1}\). Determine the time the ball is at least \(10\text{ m}\) above ground level. Take upwards as positive.

At height \(10\text{ m}\):

\[
s=10,\quad u=20,\quad a=-9.8.
\]

\[
s=ut+\frac12at^2.
\]

\[
10=20t+\frac12(-9.8)t^2.
\]

\[
10=20t-4.9t^2.
\]

\[
4.9t^2-20t+10=0.
\]

Solving gives

\[
t=0.5834\ldots\quad\text{and}\quad t=3.4983\ldots
\]

The first time is when the ball rises through \(10\text{ m}\). The second time is when it falls back through \(10\text{ m}\). Therefore the time above \(10\text{ m}\) is

\[
3.4983\ldots-0.5834\ldots=2.9149\ldots
\]

\[
\boxed{2.9\text{ s}}
\]

to 2 significant figures.

---

## Guided Practice

### Practice Question 1: Displacement and Speed

A walker travels \(3\text{ km}\) east in \(30\) minutes, stops for \(20\) minutes, then walks \(3\text{ km}\) west back to the starting point in \(40\) minutes.

Find:

1. the average velocity for the whole journey,
2. the average speed for the whole journey.

### Practice Question 2: Velocity-Time Graph Area

A particle moves with velocity \(4\,\text{m s}^{-1}\) for \(5\) seconds, then decelerates uniformly to rest over the next \(3\) seconds.

Find:

1. the displacement over the whole \(8\)-second journey,
2. the deceleration.

### Practice Question 3: SUVAT Formula Choice

A car accelerates uniformly from \(6\,\text{m s}^{-1}\) to \(18\,\text{m s}^{-1}\) in \(8\) seconds.

Find:

1. its acceleration,
2. its displacement.

### Practice Question 4: Vertical Motion

A stone is dropped from rest from a height of \(19.6\text{ m}\). Take downwards as positive and use \(g=9.8\,\text{m s}^{-2}\).

Find:

1. the time taken to reach the ground,
2. the speed with which it hits the ground.

### Practice Question 5: Quadratic Times

A particle passes through \(O\) with speed \(10\,\text{m s}^{-1}\) and has constant acceleration \(-2\,\text{m s}^{-2}\) in the chosen positive direction. Find the times when the particle is \(12\text{ m}\) from \(O\) in the positive direction.

---

# Common Mistakes and Exam Traps

1. **Using SUVAT when acceleration is not constant.** SUVAT formulae require constant acceleration.
2. **Confusing speed and velocity.** Speed uses total distance. Velocity uses displacement and direction.
3. **Forgetting direction.** A negative velocity is not automatically wrong; it means motion opposite to the chosen positive direction.
4. **Using the wrong value of \(g\).** Use \(9.8\,\text{m s}^{-2}\) unless instructed otherwise.
5. **Mixing sign conventions.** If up is positive, \(a=-9.8\). If down is positive, \(a=+9.8\).
6. **Splitting trapezia unnecessarily.** Use the trapezium formula in velocity-time graph problems.
7. **Averaging speeds incorrectly.** Use total distance divided by total time.
8. **Ignoring the second time from a quadratic.** A particle or ball can pass the same position twice.
9. **Keeping impossible time values.** Negative time values usually do not fit the physical journey.
10. **Missing the final context sentence.** If velocity is signed, state direction.

---

# Exam Technique Notes

- Start every SUVAT problem with a row: \(s,u,v,a,t\).
- Draw a quick diagram for vertical motion and mark the positive direction.
- Convert units early: mechanics usually uses m, s, \(\text{m s}^{-1}\), \(\text{m s}^{-2}\).
- Use graph methods when the question gives or requests a graph.
- Substitute values before rearranging where possible.
- Look for hidden conditions: rest means \(u=0\) or \(v=0\); meeting at a point often means equal displacement.
- Model critique can appear: perfectly uniform acceleration may be unrealistic for a car.

---

# Full Worked Solutions to Guided Practice

## Solution to Practice Question 1

Total displacement:

\[
3-3=0.
\]

Total distance:

\[
3+3=6\text{ km}.
\]

Total time:

\[
30+20+40=90\text{ min}=1.5\text{ h}.
\]

Average velocity:

\[
\frac{0}{1.5}=0.
\]

\[
\boxed{0\,\text{km h}^{-1}}
\]

Average speed:

\[
\frac{6}{1.5}=4.
\]

\[
\boxed{4\,\text{km h}^{-1}}
\]

## Solution to Practice Question 2

Use a trapezium for the whole graph. Parallel sides: \(5\) and \(8\). Height: \(4\).

\[
s=\frac{5+8}{2}\times 4=\frac{13}{2}\times4=26.
\]

\[
\boxed{26\text{ m}}
\]

Deceleration:

\[
a=\frac{0-4}{3}=-\frac43.
\]

Acceleration is \(-\frac43\,\text{m s}^{-2}\), so deceleration is

\[
\boxed{\frac43\,\text{m s}^{-2}}.
\]

## Solution to Practice Question 3

\[
u=6,\quad v=18,\quad t=8.
\]

\[
18=6+8a.
\]

\[
12=8a.
\]

\[
a=\frac{12}{8}=\frac32=1.5.
\]

\[
\boxed{1.5\,\text{m s}^{-2}}
\]

\[
s=\left(\frac{6+18}{2}\right)8=12\times8=96.
\]

\[
\boxed{96\text{ m}}
\]

## Solution to Practice Question 4

Take downwards as positive:

\[
u=0,\quad s=19.6,\quad a=9.8.
\]

\[
19.6=0+\frac12(9.8)t^2=4.9t^2.
\]

\[
t^2=4.
\]

\[
t=2.
\]

\[
\boxed{2\text{ s}}
\]

\[
v=0+9.8(2)=19.6.
\]

\[
\boxed{19.6\,\text{m s}^{-1}}
\]

## Solution to Practice Question 5

\[
u=10,\quad a=-2,\quad s=12.
\]

\[
12=10t+\frac12(-2)t^2.
\]

\[
12=10t-t^2.
\]

\[
t^2-10t+12=0.
\]

Use the quadratic formula:

\[
t=\frac{-(-10)\pm\sqrt{(-10)^2-4(1)(12)}}{2(1)}.
\]

\[
t=\frac{10\pm\sqrt{100-48}}{2}.
\]

\[
t=\frac{10\pm\sqrt{52}}{2}=\frac{10\pm2\sqrt{13}}{2}=5\pm\sqrt{13}.
\]

\[
\boxed{t=5-\sqrt{13}\text{ s}}
\]

or

\[
\boxed{t=5+\sqrt{13}\text{ s}}.
\]

Approximate values:

\[
t=1.39\text{ s or }8.61\text{ s to 3 significant figures}.
\]

---

# Common CCEA-Style Wording

- “Use and interpret a displacement-time graph.”
- “Use and interpret a velocity-time graph.”
- “Find the acceleration from the gradient.”
- “Find the displacement from the area under the graph.”
- “Given constant acceleration, find the time/displacement/velocity.”
- “A particle moves in a straight line.”
- “A particle is projected vertically upwards.”
- “A particle falls freely under gravity.”
- “Take \(g=9.8\,\text{m s}^{-2}\).”
- “State the direction of motion.”
- “Interpret the answer in context.”

---

# Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---:|---|
| AS2-KIN-LO001 | Yes | Kinematics language is defined and used |
| AS2-KIN-LO002 | Yes | Displacement-time and velocity-time graphs are covered |
| AS2-KIN-LO003 | Yes | SUVAT formulae are derived and applied |
| AS2-KIN-LO004 | No | 2D vector SUVAT is on-spec but not in supplied evidence |
| AS2-FORCES-LO005 | Partly | \(g\) is used in vertical motion |
| AS2-FORCES-LO006 | Yes as support | Straight-line motion under gravity is included |

---

# Off-Spec or Boundary-Risk Log

| Evidence item | Risk | Decision |
|---|---|---|
| Edexcel M1 labels | Cross-board exam board | Used only for on-spec methods; not treated as CCEA past-paper evidence |
| Pearson textbook references | Original textbook pages not independently supplied | Use only embedded question text visible in slides |
| MAT/UKMT extension references | Not CCEA AS2 core | Excluded |
| Website registration/promotional slides | Not mathematical content | Excluded |
| Non-constant acceleration comments | Beyond this lesson’s core method | Mentioned only as a warning not to use SUVAT |
| Integration link from velocity to displacement | Pure calculus explanation beyond immediate AS2 requirement | Mentioned only as conceptual context |
| A2/A22 vector kinematics | On-spec elsewhere but not this evidence | Logged as gap for future lesson |

---

# Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| AS2ConstantAccelerationSVG-001 | SVG | Displacement-time graph types |
| AS2ConstantAccelerationSVG-002 | SVG | Velocity-time graph types |
| AS2ConstantAccelerationSVG-003 | SVG | Area under velocity-time graph |
| AS2ConstantAccelerationSVG-004 | SVG | Vertical motion sign conventions |
| AS2ConstantAccelerationSVG-005 | SVG | SUVAT derivation from velocity-time graph |
| AS2ConstantAccelerationMermaid-001 | Mermaid | SUVAT formula selection flowchart |
| AS2ConstantAccelerationTikZ-001 | TikZ | Clean mathematical velocity-time graph for derivation |
| AS2ConstantAccelerationWidget-001 | HTML widget | SUVAT formula selector |
| AS2ConstantAccelerationWidget-002 | HTML widget | Vertical motion sign convention explorer |

---

# Supplementary Sources Used

No external web sources were used.

Cross-board/supporting sources in the uploaded evidence include Dr Frost/Pearson/Edexcel-labelled examples. These are used only where the mathematical content matches the CCEA AS2 Kinematics and supporting gravity boundaries.

---

# Final Student Checklist

## Graphs

- [ ] I can explain displacement, distance, velocity, speed and acceleration.
- [ ] I can find velocity from a displacement-time graph.
- [ ] I can find acceleration from a velocity-time graph.
- [ ] I can find displacement or distance from the area under a velocity-time graph.
- [ ] I can use a trapezium area instead of splitting into rectangles and triangles.

## SUVAT

- [ ] I know what \(s,u,v,a,t\) mean.
- [ ] I can write the five SUVAT formulae.
- [ ] I can choose the correct SUVAT formula by identifying the missing quantity.
- [ ] I can derive \(v=u+at\) from a velocity-time graph.
- [ ] I can derive \(s=\left(\frac{u+v}{2}\right)t\) from a velocity-time graph.
- [ ] I can derive \(v^2=u^2+2as\).
- [ ] I can derive \(s=ut+\frac12at^2\).
- [ ] I can derive \(s=vt-\frac12at^2\).

## Vertical Motion

- [ ] I know that gravity acts downwards.
- [ ] I use \(g=9.8\,\text{m s}^{-2}\) unless told otherwise.
- [ ] I can choose up or down as positive and keep signs consistent.
- [ ] I can explain why a negative velocity means motion in the opposite direction.
- [ ] I can interpret two time solutions from a quadratic.

## Exam Readiness

- [ ] I write all SUVAT values before choosing a formula.
- [ ] I convert units before calculating.
- [ ] I reject impossible negative times when appropriate.
- [ ] I include units in final answers.
- [ ] I state directions when velocity or displacement is signed.
- [ ] I can explain why SUVAT is only valid for constant acceleration.
