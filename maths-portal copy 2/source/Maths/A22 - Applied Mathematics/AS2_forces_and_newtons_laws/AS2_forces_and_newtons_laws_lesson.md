# AS2 Forces and Newton's Laws Lesson

## Title and Metadata

```yaml
unit_code: AS2
unit_name: AS 2 Applied Mathematics
applied_section: Mechanics
topic_code: AS2-FORCES
topic_name: Forces and Newton's laws
topic_slug: forces_and_newtons_laws
topic_pascal: ForcesAndNewtonsLaws
topic_id: AS2ForcesAndNewtonsLaws
lesson_file: AS2_forces_and_newtons_laws_lesson.md
lo_ids:
  - AS2-FORCES-LO001
  - AS2-FORCES-LO002
  - AS2-FORCES-LO003
  - AS2-FORCES-LO004
  - AS2-FORCES-LO005
  - AS2-FORCES-LO006
  - AS2-FORCES-LO007
  - AS2-FORCES-LO008
  - AS2-FORCES-LO009
  - AS2-FORCES-LO010
  - AS2-FORCES-LO011
  - AS2-FORCES-LO012
  - AS2-FORCES-LO013
tags:
  - "#AS2"
  - "#Mechanics"
  - "#Forces"
  - "#NewtonLaws"
  - "#ResolveForces"
  - "#FreeBodyDiagram"
  - "#Friction"
  - "#Equilibrium"
status: complete_draft
```

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA GCE Mathematics Specification Map | Defines AS2-FORCES as the official CCEA topic and supplies LO IDs. |
| Project README Module Map | Supplies metadata and file naming rules. |
| Project Evidence Drop Checklist | Supplies missing-evidence, off-spec and visual-placeholder rules. |
| Chapter 5/7 Forces Transcript | Supplies teaching language, worked methods, warnings and exam technique. |
| Chapter 57 Forces Screenshots PDF | Supplies visual reference only; parsed text unavailable. |
| MechYr2 Chapter 5 Friction PDF | Cross-board support for resolving forces, inclined planes and friction. |
| MechYr2 Chapter 7 Applications of Forces PDF | Cross-board support for equilibrium, pulleys, tension and connected particles. |

## Specification Alignment

| LO ID | Coverage in this lesson |
|---|---|
| AS2-FORCES-LO001 | Newton's first law, equilibrium and the concept of a force. |
| AS2-FORCES-LO002 | Resolving forces in two dimensions. |
| AS2-FORCES-LO003 | Resultant forces by combining components. |
| AS2-FORCES-LO004 | Newton's second law, including force direction and acceleration. |
| AS2-FORCES-LO005 | Gravitational acceleration, using $g=9.8\,\mathrm{m\,s^{-2}}$ unless stated. |
| AS2-FORCES-LO006 | Weight $W=mg$ and motion under gravity. |
| AS2-FORCES-LO007 | Normal reaction and contact-force modelling. |
| AS2-FORCES-LO008 | Connected particles, strings and pulleys. |
| AS2-FORCES-LO009 | Equilibrium of forces on a particle. |
| AS2-FORCES-LO010 | Friction model $F\leq \mu R$. |
| AS2-FORCES-LO011 | Coefficient of friction. |
| AS2-FORCES-LO012 | Motion of a body on a rough surface. |
| AS2-FORCES-LO013 | Limiting friction and statics. |

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Draw a complete force diagram for a particle or body.
2. Resolve angled forces into perpendicular components using sine and cosine.
3. Decide whether to resolve horizontally/vertically or parallel/perpendicular to a plane.
4. Use equilibrium conditions such as “forces right = forces left” and “forces up = forces down”.
5. Use Newton's second law correctly as $\text{resultant force}=ma$.
6. Distinguish mass from weight: $W=mg$.
7. Understand that the normal reaction is perpendicular to the surface, not automatically equal to the weight.
8. Use the friction model $F\leq\mu R$.
9. Recognise when friction is limiting: $F=\mu R$.
10. Solve statics and dynamics problems involving strings, pulleys, inclined planes and rough surfaces.

## Prerequisite Recap

No GCSE source material is used in this lesson. The following are treated only as prerequisite mathematical skills.

| Prior skill | Needed because |
|---|---|
| AS1 vectors | Forces are vectors with magnitude and direction. |
| AS1 trigonometry | Components use sine and cosine. |
| Algebraic rearrangement | Equations such as $P\cos30^\circ=4\cos45^\circ$ must be solved cleanly. |
| Simultaneous equations | Many mechanics problems produce two equations in two unknowns. |
| AS2 quantities and units | Force is measured in newtons, mass in kilograms, acceleration in $\mathrm{m\,s^{-2}}$. |
| AS2 kinematics | Newton's laws connect force to motion through acceleration. |

## Big Picture Explanation

Mechanics is about two things dancing on the same stage:

1. **Motion:** how objects move.
2. **Forces:** why their motion changes, or why it does not change.

The bridge between the two is Newton's second law:

$$F=ma.$$

But the $F$ in this formula is not just any force. It is the **resultant force**, meaning the overall force after all competing forces have been combined.

That is why force diagrams matter so much. A mechanics problem is often not hard because the algebra is difficult. It is hard because the diagram is a small battlefield of directions. Once the forces are drawn and resolved correctly, the equations usually march out obediently.

[VISUAL PLACEHOLDER: AS2ForcesSVG-001 | Source: CCEA specification map + Chapter 5/7 Forces transcript | Insert from svg/AS2ForcesSVG-001.svg | Purpose: Overview map linking forces, motion and $F=ma$.]

## Key Definitions and Notation

### Force

A **force** is a vector quantity. It has magnitude, measured in newtons $(\mathrm{N})$, and direction.

### Mass

Mass measures the amount of matter in an object. It is measured in kilograms $(\mathrm{kg})$.

### Weight

Weight is the force due to gravity.

$$W=mg$$

where:

$$W=\text{weight in newtons},\qquad m=\text{mass in kilograms},\qquad g=\text{gravitational acceleration}.$$

For CCEA AS Mathematics, use

$$g=9.8\,\mathrm{m\,s^{-2}}$$

unless the question gives another value. Weight always acts **vertically downward**.

### Normal reaction

The normal reaction is the contact force exerted by a surface on an object. It is usually denoted by $R$. The word **normal** means perpendicular, so the normal reaction acts perpendicular to the surface.

On a horizontal surface, $R$ is vertical. On an inclined plane, $R$ is perpendicular to the plane, not vertical.

### Equilibrium

A particle is in equilibrium when the resultant force is zero. This happens when the object is at rest or moves with constant velocity.

In equilibrium:

$$\text{forces right}=\text{forces left}$$

and

$$\text{forces up}=\text{forces down}.$$

### Statics

Statics means the object is not accelerating. Static problems usually involve particles at rest or in equilibrium.

### Resultant force

The resultant force is the overall force after combining all forces. If forces act in opposite directions,

$$\text{resultant force}=\text{forces in chosen positive direction}-\text{forces in opposite direction}.$$

Newton's second law uses the resultant force:

$$\text{resultant force}=ma.$$

### Friction

Friction is a contact force that resists motion or the tendency to move.

For a rough surface:

$$F\leq \mu R$$

where $F$ is friction, $\mu$ is the coefficient of friction and $R$ is the normal reaction. The maximum possible friction is

$$F_{\max}=\mu R.$$

### Limiting friction

Friction is limiting when it has reached its maximum value:

$$F=\mu R.$$

This occurs when a particle is on the point of moving, on the point of slipping, moving under the friction model used in this course, or in limiting equilibrium.

## Core Theory

### 1. Drawing force diagrams

A force diagram should show every force acting on the particle or body. For a typical object on a surface, check for weight, normal reaction, tension, applied forces, friction and acceleration direction.

A useful rule: **do not start calculating until the diagram is honest**.

### 2. Resolving a force into components

Suppose a force of magnitude $F$ acts at an angle $\theta$ above the horizontal.

The horizontal component is adjacent to the angle:

$$F\cos\theta.$$

The vertical component is opposite the angle:

$$F\sin\theta.$$

So the force can be replaced by two perpendicular forces:

$$F\cos\theta\quad\text{and}\quad F\sin\theta.$$

These two components are perpendicular, so they can be considered independently.

[VISUAL PLACEHOLDER: AS2ForcesSVG-002 | Source: MechYr2 Chapter 5 Friction PDF + transcript | Insert from svg/AS2ForcesSVG-002.svg | Purpose: Show a force $F$ at angle $\theta$ resolved into $F\cos\theta$ and $F\sin\theta$.]

### 3. The sine/cosine component rule

If $F$ is the hypotenuse of a right-angled component triangle:

$$\text{component adjacent to }\theta = F\cos\theta,$$

$$\text{component opposite }\theta = F\sin\theta.$$

For example, if a $6\mathrm{N}$ force acts at angle $\theta$:

$$\cos\theta=\frac{\text{adjacent}}{6}$$

so

$$\text{adjacent}=6\cos\theta.$$

Also:

$$\sin\theta=\frac{\text{opposite}}{6}$$

so

$$\text{opposite}=6\sin\theta.$$

### 4. Why the second diagram matters

When a force diagram contains angled forces, redraw it as a simpler resolved diagram.

If a particle has a force $P$ acting up and right at $30^\circ$, a force $4\mathrm{N}$ acting up and left at $45^\circ$, and a downward force $Q$, then resolve:

$$P \to P\cos30^\circ \text{ right},\quad P\sin30^\circ \text{ up},$$

$$4 \to 4\cos45^\circ \text{ left},\quad 4\sin45^\circ \text{ up}.$$

The simplified diagram has:

- right: $P\cos30^\circ$;
- left: $4\cos45^\circ$;
- up: $P\sin30^\circ+4\sin45^\circ$;
- down: $Q$.

[VISUAL PLACEHOLDER: AS2ForcesSVG-003 | Source: Chapter 5/7 Forces Transcript + MechYr2 Chapter 7 PDF | Insert from svg/AS2ForcesSVG-003.svg | Purpose: Show original angled force diagram and the cleaner resolved “box” diagram.]

### 5. Equilibrium equations

If the particle is in equilibrium:

$$\text{forces right}=\text{forces left},\qquad \text{forces up}=\text{forces down}.$$

For the previous resolved diagram:

$$P\cos30^\circ=4\cos45^\circ.$$

Then:

$$P=\frac{4\cos45^\circ}{\cos30^\circ}.$$

Using exact values:

$$P=\frac{4\cdot \frac{\sqrt2}{2}}{\frac{\sqrt3}{2}}=\frac{2\sqrt2}{\frac{\sqrt3}{2}}=2\sqrt2\cdot\frac{2}{\sqrt3}=\frac{4\sqrt2}{\sqrt3}.$$

Rationalise:

$$P=\frac{4\sqrt2}{\sqrt3}\cdot\frac{\sqrt3}{\sqrt3}=\frac{4\sqrt6}{3}=3.2659\ldots$$

so

$$P=3.27\mathrm{N}\quad(3\text{s.f.}).$$

Now resolve vertically:

$$Q=P\sin30^\circ+4\sin45^\circ.$$

Substitute:

$$Q=\frac{4\sqrt6}{3}\sin30^\circ+4\sin45^\circ.$$

Use $\sin30^\circ=\frac12$ and $\sin45^\circ=\frac{\sqrt2}{2}$:

$$Q=\frac{4\sqrt6}{3}\cdot\frac12+4\cdot\frac{\sqrt2}{2}=\frac{2\sqrt6}{3}+2\sqrt2=4.4614\ldots$$

so

$$Q=4.46\mathrm{N}\quad(3\text{s.f.}).$$

### 6. Newton's first law

Newton's first law says that an object remains at rest or continues to move with constant velocity unless acted on by a resultant external force.

For this course:

$$\text{no resultant force}\Longleftrightarrow \text{no acceleration}.$$

### 7. Newton's second law

Newton's second law is:

$$F=ma.$$

In mechanics questions, read this as:

$$\text{resultant force in the direction of acceleration}=ma.$$

If a particle accelerates to the right:

$$\text{forces right}-\text{forces left}=ma.$$

If a particle accelerates down a slope:

$$\text{forces down slope}-\text{forces up slope}=ma.$$

[VISUAL PLACEHOLDER: AS2ForcesSVG-004 | Source: Chapter 5/7 Forces Transcript + MechYr2 Chapter 5 Friction PDF | Insert from svg/AS2ForcesSVG-004.svg | Purpose: Show a horizontal box pulled by a force, with resultant force in the direction of acceleration.]

### 8. Normal reaction is not automatically equal to weight

On a simple horizontal surface with no other vertical forces,

$$R=mg.$$

But if an angled force pulls upward, the normal reaction is smaller.

Example: a box of mass $8\mathrm{kg}$ lies on a smooth horizontal floor. A force of $10\mathrm{N}$ is applied at $30^\circ$ above the horizontal.

Vertical forces:

- upward: $R+10\sin30^\circ$;
- downward: $8g$.

There is no vertical acceleration:

$$R+10\sin30^\circ=8g.$$

So:

$$R=8g-10\sin30^\circ=8(9.8)-10\cdot\frac12=78.4-5=73.4\mathrm{N}.$$

### 9. Smooth and rough surfaces

A **smooth** surface has no friction. A **rough** surface has friction.

If a question says “smooth”, do not invent a friction force. If a question says “rough”, consider friction.

### 10. The friction model

For a rough surface:

$$F\leq\mu R.$$

The maximum possible friction is:

$$F_{\max}=\mu R.$$

Friction can be smaller than $\mu R$. If a box is pulled with a small force and does not move, friction matches the opposing force. It does not automatically jump to its maximum.

For example, if $R=15\mathrm{N}$ and $\mu=0.3$:

$$F_{\max}=\mu R=0.3(15)=4.5\mathrm{N}.$$

If an applied horizontal force is $2\mathrm{N}$, the friction is $2\mathrm{N}$, not $4.5\mathrm{N}$.

[VISUAL PLACEHOLDER: AS2ForcesSVG-005 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-005.svg | Purpose: Show friction growing from zero to its maximum $\mu R$, then motion beginning.]

[INTERACTIVE PLACEHOLDER: AS2ForcesWidget-001 | Source: Chapter 5/7 Forces Transcript | Insert from widgets/AS2ForcesWidget-001.html | Purpose: Interactive slider showing applied force, friction value and motion state.]

### 11. Limiting equilibrium

A particle is in limiting equilibrium when it is still in equilibrium but just about to move. That means:

$$F=\mu R.$$

It is still not accelerating, so the forces still balance.

### 12. Inclined planes

For an inclined plane, resolve forces parallel to the plane and perpendicular to the plane.

For a block of mass $m$ on a slope at angle $\theta$ to the horizontal:

- weight acts vertically downward: $mg$;
- component of weight down the plane: $mg\sin\theta$;
- component of weight perpendicular into the plane: $mg\cos\theta$.

If the surface is smooth and there are no other perpendicular forces:

$$R=mg\cos\theta.$$

If the block accelerates down the plane on a smooth slope:

$$mg\sin\theta=ma.$$

Divide by $m$:

$$a=g\sin\theta.$$

[VISUAL PLACEHOLDER: AS2ForcesSVG-006 | Source: MechYr2 Chapter 5 Friction PDF + transcript | Insert from svg/AS2ForcesSVG-006.svg | Purpose: Inclined plane force diagram showing $mg$, $R$, $mg\sin\theta$, $mg\cos\theta$.]

[INTERACTIVE PLACEHOLDER: AS2ForcesWidget-002 | Source: Chapter 5/7 Forces Transcript + MechYr2 Chapter 5 Friction PDF | Insert from widgets/AS2ForcesWidget-002.html | Purpose: Interactive model of slope angle, friction and acceleration.]

### 13. Strings, pulleys and connected particles

In mechanics models:

- a **light string** has negligible mass;
- an **inextensible string** does not stretch;
- a **smooth pulley** means the tension is the same on both sides of the pulley.

So, when a smooth pulley and light inextensible string are used, the tension $T$ is usually the same throughout the string.

[VISUAL PLACEHOLDER: AS2ForcesSVG-007 | Source: MechYr2 Chapter 7 Applications of Forces PDF + transcript | Insert from svg/AS2ForcesSVG-007.svg | Purpose: Connected particles over a smooth pulley with common tension $T$.]

## Visual Asset Integration

| Asset ID | Type | Purpose |
|---|---|---|
| AS2ForcesSVG-001 to AS2ForcesSVG-014 | SVG | Portal-ready force diagrams and concept visuals. |
| AS2ForcesTikZ-001 to AS2ForcesTikZ-012 | TikZ | Print-quality diagrams. |
| AS2ForcesMER-001 to AS2ForcesMER-010 | Mermaid | Workflow and decision diagrams. |
| AS2ForcesWidget-001 to AS2ForcesWidget-002 | HTML widgets | Interactive friction and inclined-plane exploration. |

## Worked Examples

### Worked Example 1: Resolving angled forces in equilibrium

A particle is in equilibrium under three forces:

- $4\mathrm{N}$ acting up and left at $45^\circ$ to the horizontal;
- $P\mathrm{N}$ acting up and right at $30^\circ$ to the horizontal;
- $Q\mathrm{N}$ acting vertically downward.

Find $P$ and $Q$.

[VISUAL PLACEHOLDER: AS2ForcesSVG-008 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-008.svg | Purpose: Show the angled-force equilibrium diagram and its resolved force-box version.]

#### Step 1: Resolve the $P$ force

$$P\cos30^\circ\quad\text{to the right},\qquad P\sin30^\circ\quad\text{upwards}.$$

#### Step 2: Resolve the $4\mathrm{N}$ force

$$4\cos45^\circ\quad\text{to the left},\qquad 4\sin45^\circ\quad\text{upwards}.$$

#### Step 3: Use horizontal equilibrium

$$P\cos30^\circ=4\cos45^\circ.$$

$$P=\frac{4\cos45^\circ}{\cos30^\circ}=\frac{4\sqrt6}{3}=3.2659\ldots$$

$$P=3.27\mathrm{N}\quad(3\text{s.f.}).$$

#### Step 4: Use vertical equilibrium

$$Q=P\sin30^\circ+4\sin45^\circ.$$

Substitute:

$$Q=\frac{4\sqrt6}{3}\cdot\frac12+4\cdot\frac{\sqrt2}{2}=\frac{2\sqrt6}{3}+2\sqrt2=4.4614\ldots$$

$$Q=4.46\mathrm{N}\quad(3\text{s.f.}).$$

#### Final answer

$$\boxed{P=3.27\mathrm{N}},\qquad \boxed{Q=4.46\mathrm{N}}.$$

### Worked Example 2: Smooth horizontal floor with an angled force

A box of mass $8\mathrm{kg}$ lies on a smooth horizontal floor. A force of $10\mathrm{N}$ is applied at an angle of $30^\circ$ above the horizontal, causing the box to accelerate horizontally along the floor.

Find the acceleration and the normal reaction.

[VISUAL PLACEHOLDER: AS2ForcesSVG-009 | Source: MechYr2 Chapter 5 Friction PDF + Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-009.svg | Purpose: Smooth horizontal floor with a $10\mathrm{N}$ force at $30^\circ$.]

Horizontal component:

$$10\cos30^\circ.$$

Use Newton's second law horizontally:

$$10\cos30^\circ=8a.$$

$$a=\frac{10\cos30^\circ}{8}=\frac{10\cdot\frac{\sqrt3}{2}}{8}=\frac{5\sqrt3}{8}=1.0825\ldots$$

$$a=1.1\mathrm{m\,s^{-2}}\quad(2\text{s.f.}).$$

For the normal reaction:

$$R+10\sin30^\circ=8g.$$

$$R=8g-10\sin30^\circ=8(9.8)-10\cdot\frac12=78.4-5=73.4.$$

$$R=73\mathrm{N}\quad(2\text{s.f.}).$$

### Worked Example 3: Smooth bead on a light inextensible string

A smooth bead is threaded on a light inextensible string. The bead is held in equilibrium by a horizontal force of magnitude $8\mathrm{N}$. One part of the string is vertical and the other is angled so that the relevant angle is $30^\circ$.

Find the tension in the string and the weight of the bead.

[VISUAL PLACEHOLDER: AS2ForcesSVG-010 | Source: MechYr2 Chapter 7 Applications of Forces PDF + Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-010.svg | Purpose: Smooth bead with common tension $T$, horizontal $8\mathrm{N}$ force and weight $W$.]

The bead is smooth and the string is a single light inextensible string, so the tension is the same throughout. Let the tension be $T$ and the weight be $W$.

Horizontal equilibrium:

$$T\cos30^\circ=8.$$

$$T=\frac{8}{\cos30^\circ}=\frac{8}{\frac{\sqrt3}{2}}=\frac{16}{\sqrt3}=\frac{16\sqrt3}{3}=9.2376\ldots$$

$$T=9.24\mathrm{N}\quad(3\text{s.f.}).$$

Vertical equilibrium:

$$W=T+T\sin30^\circ.$$

$$W=\frac{16\sqrt3}{3}+\frac{16\sqrt3}{3}\cdot\frac12=\frac{16\sqrt3}{3}+\frac{8\sqrt3}{3}=8\sqrt3=13.8564\ldots$$

$$W=13.9\mathrm{N}\quad(3\text{s.f.}).$$

### Worked Example 4: Two separate strings attached to a particle

A particle of weight $8\mathrm{N}$ is attached to two separate light inextensible strings. One string makes an angle of $35^\circ$ with the horizontal. The other string makes an angle of $25^\circ$ with the horizontal. The particle is in equilibrium.

Find the tension in each string.

[VISUAL PLACEHOLDER: AS2ForcesSVG-011 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-011.svg | Purpose: Separate strings labelled $T_1$ and $T_2$.]

Because the particle is attached to two separate strings, the tensions are not necessarily equal. Let $T_1$ be the tension in the string at $35^\circ$ and $T_2$ be the tension in the string at $25^\circ$.

Horizontal equilibrium:

$$T_1\cos35^\circ=T_2\cos25^\circ.$$

Make $T_1$ the subject:

$$T_1=\frac{T_2\cos25^\circ}{\cos35^\circ}.$$

Vertical equilibrium:

$$T_1\sin35^\circ+T_2\sin25^\circ=8.$$

Substitute:

$$\frac{T_2\cos25^\circ}{\cos35^\circ}\sin35^\circ+T_2\sin25^\circ=8.$$

Factorise:

$$T_2\left(\frac{\cos25^\circ\sin35^\circ}{\cos35^\circ}+\sin25^\circ\right)=8.$$

So:

$$T_2=\frac{8}{\frac{\cos25^\circ\sin35^\circ}{\cos35^\circ}+\sin25^\circ}=7.567\ldots$$

$$T_2=7.6\mathrm{N}\quad(2\text{s.f.}).$$

Then:

$$T_1=\frac{7.567\ldots\cos25^\circ}{\cos35^\circ}=8.37\ldots$$

$$T_1=8.4\mathrm{N}\quad(2\text{s.f.}).$$

### Worked Example 5: Smooth inclined plane where $\tan\alpha=\frac34$

A particle of mass $2\mathrm{kg}$ is moving on a smooth slope. A force of $4\mathrm{N}$ acts up the slope. The slope is inclined at angle $\alpha$ to the horizontal, where

$$\tan\alpha=\frac34.$$

Find the acceleration of the particle.

[VISUAL PLACEHOLDER: AS2ForcesSVG-012 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-012.svg | Purpose: Smooth inclined plane with $4\mathrm{N}$ up the slope and $\tan\alpha=\frac34$.]

Since $\tan\alpha=\frac34$, use a $3,4,5$ triangle:

$$\sin\alpha=\frac35,
\qquad
\cos\alpha=\frac45.$$

Down the slope component of the weight:

$$2g\sin\alpha=2g\cdot\frac35=\frac{6g}{5}.$$

Using $g=9.8$:

$$\frac{6g}{5}=\frac{6(9.8)}{5}=11.76.$$

Since $11.76>4$, the particle accelerates down the slope.

Taking down the slope as positive:

$$2g\sin\alpha-4=2a.$$

$$2g\cdot\frac35-4=2a.$$

$$\frac{6g}{5}-4=2a.$$

$$11.76-4=2a.$$

$$7.76=2a.$$

$$a=3.88.$$

$$\boxed{a=3.88\mathrm{m\,s^{-2}}\text{ down the slope}}.$$

### Worked Example 6: Rough horizontal surface

A particle of mass $5\mathrm{kg}$ is pulled along a rough horizontal surface by a horizontal force of magnitude $20\mathrm{N}$. The coefficient of friction is $\mu=0.2$. Find the frictional force and acceleration.

[VISUAL PLACEHOLDER: AS2ForcesSVG-013 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-013.svg | Purpose: Rough horizontal surface with pull, friction, weight and normal reaction.]

Vertical equilibrium:

$$R=5g.$$

Friction:

$$F=\mu R=0.2(5g)=g=9.8\mathrm{N}.$$

Horizontal Newton's second law:

$$20-F=5a.$$

Substitute:

$$20-9.8=5a.$$

$$10.2=5a.$$

$$a=2.04\mathrm{m\,s^{-2}}.$$

### Worked Example 7: Rough inclined plane

A particle of mass $2\mathrm{kg}$ slides down a rough slope inclined at $30^\circ$ to the horizontal. Its acceleration down the slope is $1\mathrm{m\,s^{-2}}$. Find the coefficient of friction between the particle and the plane.

[VISUAL PLACEHOLDER: AS2ForcesSVG-014 | Source: Chapter 5/7 Forces Transcript | Insert from svg/AS2ForcesSVG-014.svg | Purpose: Rough inclined plane with friction up the slope and acceleration down the slope.]

Resolve perpendicular to the plane:

$$R=2g\cos30^\circ.$$

Use Newton's second law down the slope:

$$2g\sin30^\circ-\mu R=2(1).$$

Substitute $R=2g\cos30^\circ$:

$$2g\sin30^\circ-\mu(2g\cos30^\circ)=2.$$

Rearrange:

$$2g\sin30^\circ-2=\mu(2g\cos30^\circ).$$

Divide by $2g\cos30^\circ$:

$$\mu=\frac{2g\sin30^\circ-2}{2g\cos30^\circ}.$$

Use $g=9.8$, $\sin30^\circ=\frac12$ and $\cos30^\circ=\frac{\sqrt3}{2}$:

$$\mu=\frac{2(9.8)\cdot\frac12-2}{2(9.8)\cdot\frac{\sqrt3}{2}}=\frac{9.8-2}{9.8\sqrt3}=0.4597\ldots$$

$$\boxed{\mu=0.46\quad(2\text{s.f.})}.$$

## Guided Practice

### Practice Question 1: Angled force on a smooth horizontal surface

A particle of mass $4\mathrm{kg}$ lies on a smooth horizontal surface. A force of $12\mathrm{N}$ acts at $40^\circ$ above the horizontal, causing the particle to accelerate horizontally.

Find the acceleration and the normal reaction.

### Practice Question 2: Equilibrium with two angled forces

A particle is in equilibrium under three forces:

- $6\mathrm{N}$ acting up and left at $40^\circ$ to the horizontal;
- $P\mathrm{N}$ acting up and right at $25^\circ$ to the horizontal;
- $Q\mathrm{N}$ acting vertically downward.

Find $P$ and $Q$.

### Practice Question 3: Rough horizontal surface

A particle of mass $6\mathrm{kg}$ is pulled along a rough horizontal surface by a horizontal force of $25\mathrm{N}$. The coefficient of friction is $\mu=0.3$. Find the frictional force and acceleration.

### Practice Question 4: Smooth inclined plane

A particle of mass $3\mathrm{kg}$ lies on a smooth plane inclined at $25^\circ$ to the horizontal. It is released from rest and accelerates down the plane. Find its acceleration.

### Practice Question 5: Rough inclined plane

A particle of mass $4\mathrm{kg}$ slides down a rough plane inclined at $20^\circ$ to the horizontal. The coefficient of friction is $\mu=0.15$. Find its acceleration down the plane.

## Common Mistakes and Exam Traps

### Mistake 1: Treating $F=ma$ as “force equals mass times acceleration”

The $F$ in $F=ma$ means resultant force. Use:

$$\text{resultant force}=ma.$$

### Mistake 2: Forgetting that weight acts vertically downward

Even on a slope, weight is $mg$ vertically downward. It does not act perpendicular to the slope or down the slope until you resolve it.

### Mistake 3: Drawing the normal reaction vertically on a slope

The normal reaction is perpendicular to the surface. On an inclined plane, $R$ is tilted.

### Mistake 4: Assuming $R=mg$

This is only true in simple horizontal cases with no other vertical forces.

### Mistake 5: Using $\mu R$ too early

The friction law is $F\leq\mu R$. Only use $F=\mu R$ when friction is limiting or the model says the object is sliding/moving under the usual A-Level model.

### Mistake 6: Forgetting that friction opposes motion or tendency to move

If the particle slides down a slope, friction acts up the slope. If a force tries to pull a stationary object to the right, friction acts left.

### Mistake 7: Finding $\alpha$ unnecessarily when $\tan\alpha$ is given

If $\tan\alpha=\frac34$, use the $3,4,5$ triangle:

$$\sin\alpha=\frac35,
\qquad
\cos\alpha=\frac45.$$

### Mistake 8: Using one tension for two separate strings

Same tension is justified for a single light string passing over a smooth pulley or through a smooth bead. Separate strings need separate variables.

## Exam Technique Notes

1. Draw the diagram first.
2. Use dotted component arrows for resolved components.
3. Keep paired components together.
4. Choose the easiest axes.
5. Solve the direction with fewer unknowns first.
6. Keep exact values until the final answer.
7. Use correct units: $\mathrm{N}$, $\mathrm{kg}$ and $\mathrm{m\,s^{-2}}$.
8. State direction when acceleration or friction direction matters.

## Full Worked Solutions

### Solution to Practice Question 1

Horizontal:

$$12\cos40^\circ=4a.$$

$$a=\frac{12\cos40^\circ}{4}=3\cos40^\circ=2.2981\ldots$$

$$\boxed{a=2.30\mathrm{m\,s^{-2}}}.$$

Vertical:

$$R+12\sin40^\circ=4g.$$

$$R=4g-12\sin40^\circ=4(9.8)-12\sin40^\circ=31.4866\ldots$$

$$\boxed{R=31.5\mathrm{N}}.$$

### Solution to Practice Question 2

Horizontal:

$$P\cos25^\circ=6\cos40^\circ.$$

$$P=\frac{6\cos40^\circ}{\cos25^\circ}=5.0717\ldots$$

$$\boxed{P=5.07\mathrm{N}}.$$

Vertical:

$$Q=P\sin25^\circ+6\sin40^\circ.$$

$$Q=5.0717\ldots\sin25^\circ+6\sin40^\circ=6.0001\ldots$$

$$\boxed{Q=6.00\mathrm{N}}.$$

### Solution to Practice Question 3

Vertical:

$$R=6g.$$

Friction:

$$F=\mu R=0.3(6g)=1.8g=17.64.$$

$$\boxed{F=17.6\mathrm{N}}.$$

Horizontal:

$$25-F=6a.$$

$$25-17.64=6a.$$

$$7.36=6a.$$

$$a=1.2266\ldots$$

$$\boxed{a=1.23\mathrm{m\,s^{-2}}}.$$

### Solution to Practice Question 4

Smooth slope, so no friction:

$$3g\sin25^\circ=3a.$$

$$a=g\sin25^\circ=9.8\sin25^\circ=4.1416\ldots$$

$$\boxed{a=4.14\mathrm{m\,s^{-2}}\text{ down the plane}}.$$

### Solution to Practice Question 5

Perpendicular:

$$R=4g\cos20^\circ.$$

Friction:

$$F=\mu R=0.15(4g\cos20^\circ).$$

Down the slope:

$$4g\sin20^\circ-0.15(4g\cos20^\circ)=4a.$$

Divide by $4$:

$$a=g\sin20^\circ-0.15g\cos20^\circ=g(\sin20^\circ-0.15\cos20^\circ).$$

$$a=9.8(\sin20^\circ-0.15\cos20^\circ)=1.971\ldots$$

$$\boxed{a=1.97\mathrm{m\,s^{-2}}\text{ down the plane}}.$$

## Common CCEA-Style Wording

| Wording | What it means mathematically |
|---|---|
| smooth surface | No friction force. |
| rough surface | Include friction. |
| light string | Ignore mass of string. |
| inextensible string | Connected particles share the same acceleration magnitude along the string. |
| smooth pulley | Tension is the same on both sides of the pulley. |
| particle | Treat the object as a point mass. No rotational effects. |
| in equilibrium | Resultant force is zero. |
| on the point of moving | Friction is limiting, so $F=\mu R$. |
| slides down | Friction acts up the slope. |
| acts horizontally | Force is parallel to the horizontal. |
| acts parallel to the slope | Force is already along the slope. |
| inclined at $\theta$ to the horizontal | Use $mg\sin\theta$ down the plane and $mg\cos\theta$ into the plane. |

## Syllabus Gap Check

| LO ID | Coverage status | Notes |
|---|---|---|
| AS2-FORCES-LO001 | Covered | Newton's first law, equilibrium and force concept included. |
| AS2-FORCES-LO002 | Covered | Resolving in horizontal/vertical and slope-based axes included. |
| AS2-FORCES-LO003 | Covered | Resultant force and addition of forces through components included. |
| AS2-FORCES-LO004 | Covered | Newton's second law used in horizontal and inclined-plane examples. |
| AS2-FORCES-LO005 | Covered | $g=9.8\mathrm{m\,s^{-2}}$ used unless otherwise stated. |
| AS2-FORCES-LO006 | Covered | Weight $W=mg$, vertical direction and gravity examples included. |
| AS2-FORCES-LO007 | Partially covered | Normal reaction and contact force discussed. Lift-specific examples not included because not supplied in lesson evidence. |
| AS2-FORCES-LO008 | Partially covered | Connected particles and pulley modelling discussed. A full moving connected-particles worked example is not included because supplied evidence focused more heavily on statics and resolving. |
| AS2-FORCES-LO009 | Covered | Equilibrium examples with angled forces and strings included. |
| AS2-FORCES-LO010 | Covered | $F\leq\mu R$ model included. |
| AS2-FORCES-LO011 | Covered | Coefficient of friction $\mu$ included. |
| AS2-FORCES-LO012 | Covered | Motion on rough surfaces included. |
| AS2-FORCES-LO013 | Covered | Limiting friction and statics included. |

## Off-Spec Content Found but Excluded

| Evidence item | Reason excluded from core lesson |
|---|---|
| Variable acceleration with trigonometric, exponential or logarithmic functions | Not part of AS2-FORCES. |
| Projectiles and full 2D SUVAT | Belongs to other mechanics areas, not this forces lesson. |
| A22 moments | Separate A22 mechanics topic. |
| A22 impulse and momentum | Separate A22 mechanics topic. |
| DrFrost platform promotional pages | Not lesson content. |
| Edexcel/Pearson exam references | Used only as cross-board support where content matches CCEA AS2-FORCES. |

## Visual and Interactive Asset Plan

| Asset group | Files | Purpose |
|---|---|---|
| Mermaid | `mermaid/*.md` | Workflows and decision trees. |
| SVG | `svg/*.svg` | Portal-ready visual diagrams. |
| TikZ | `tikz/*.tex` | Print-quality diagrams. |
| Widgets | `widgets/*.html` | Interactive friction and inclined-plane explorations. |

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority. |
| Chapter 5/7 Forces Transcript | Core lesson evidence for worked methods, warnings and teaching sequence. |
| Chapter 57 Forces Screenshots PDF | Visual-only support. Parsed text unavailable. |
| MechYr2 Chapter 5 Friction PDF | Cross-board support, used only where content matches AS2-FORCES. |
| MechYr2 Chapter 7 Applications of Forces PDF | Cross-board support, used only where content matches AS2-FORCES. |

## Final Student Checklist

By the end of this lesson, I can:

- [ ] Explain why force is a vector.
- [ ] Resolve a force into perpendicular components.
- [ ] Use $F\cos\theta$ for the component adjacent to $\theta$.
- [ ] Use $F\sin\theta$ for the component opposite to $\theta$.
- [ ] Draw a complete force diagram before calculating.
- [ ] Use $W=mg$ correctly.
- [ ] State that weight acts vertically downward.
- [ ] Draw $R$ perpendicular to the surface.
- [ ] Explain why $R$ is not always equal to $mg$.
- [ ] Use equilibrium equations in two perpendicular directions.
- [ ] Use Newton's second law as resultant force $=ma$.
- [ ] Resolve parallel and perpendicular to an inclined plane.
- [ ] Use $mg\sin\theta$ down a slope.
- [ ] Use $mg\cos\theta$ perpendicular into a slope.
- [ ] Use $F\leq\mu R$.
- [ ] Recognise when $F=\mu R$.
- [ ] Decide the direction of friction.
- [ ] Use smooth/light/inextensible pulley assumptions correctly.
- [ ] Keep exact values until the final rounding step.
- [ ] Write final answers with units where required.
