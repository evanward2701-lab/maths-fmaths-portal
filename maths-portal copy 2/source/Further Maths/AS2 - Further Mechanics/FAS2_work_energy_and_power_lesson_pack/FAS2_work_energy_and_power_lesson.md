# FAS2 Work, Energy and Power Lesson

```yaml
date_generated: 2026-06-05
course: CCEA GCE Further Mathematics
unit_code: FAS2
unit_title: Further AS 2 Applied Mathematics
applied_section: "Section A: Mechanics 1"
topic_code: "FAS2-WENG + FAS2-POW"
topic_name: "Work, Energy and Power"
topic_slug: "work_energy_and_power"
topic_pascal: "WorkEnergyAndPower"
topic_id: "FAS2WorkEnergyAndPower"
lesson_file: "FAS2_work_energy_and_power_lesson.md"
lesson_status: "Written file"
```

## Learning Outcome IDs

- FAS2-WENG-LO001
- FAS2-WENG-LO002
- FAS2-WENG-LO003
- FAS2-WENG-LO004
- FAS2-POW-LO001
- FAS2-POW-LO002

## Evidence-boundary note

This lesson is built for **CCEA FAS2 Further AS 2 Applied Mathematics, Section A: Mechanics 1**. The supplied lesson evidence is from a Further Mechanics 1 Work, Energy and Power chapter. It is used only where it matches the CCEA specification boundary. CCEA specification wording controls the final lesson boundary.

The supplied chapter evidence strongly covers work done by constant forces, direction consistency between force and displacement, work against gravity and friction, kinetic energy and gravitational potential energy, the work-energy principle, conservation of energy, power and \(P=Fv\), and vehicle power examples.

The CCEA specification also requires scalar product use for work done, variable force work using \(W=\int_a^b F\,dx\), elastic potential energy, and pump problems. Those required areas are included, with evidence limitations marked honestly.

# 2. Evidence Map

| Source | Type | Used for | Notes |
|---|---|---|---|
| CCEA Further Mathematics specification map | Project source | Official unit, topic code, LO IDs, boundaries | Main authority. |
| Further Maths README module map | Project source | Topic-to-bridge map | FAS2-WENG links to AS2 mechanics and A21 integration; FAS2-POW links to force, velocity and rates. |
| Further Maths Evidence Drop Checklist | Project source | Missing evidence and off-spec rules | Used to log evidence gaps and visual limitations. |
| CCEA ordinary Mathematics specification map | Bridge source | Ordinary AS2 mechanics, AS1 integration, A22 kinematics | Bridge only. |
| Ordinary A-Level Maths bridge extracts | Bridge source | Bridge table | Bridge only. |
| `FM1-Chp2-Work Energy and Power.pdf` | Lesson PDF/slides | Definitions, formulas, examples, slide diagrams | Cross-board but on-spec where matched to CCEA. |
| `transcripts.md` | Teacher transcript | Explanations, warnings, worked examples, modelling language | Teacher explanations and warnings preserved where mathematically useful. |
| `Chapter_2_Work,_Energy_&_Power_🎯_(Further_Mechanics_1)_screenshots.pdf` | Screenshot PDF | Visual confirmation of slides and handwritten working | Parsed text unavailable; use only visible/readable details. |

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary | Bridge |
|---|---|---|---|---|---|
| FAS2-WENG-LO001 | calculate work done by a force when its point of application undergoes a displacement, including use of the scalar product | Defines \(W=Fs\), \(W=Fs\cos\theta\), and \(W=\mathbf F\cdot\mathbf s\). | CCEA spec; PDF work slides; transcript | Core | AS2 forces, displacement, resolving, vectors |
| FAS2-WENG-LO002 | calculate the work done by a variable force, where the force is given as a simple function of displacement: \(W=\int_a^bF\,dx\) | Adds definite-integral method for variable force. | CCEA spec | Core, evidence-light | AS1 integration |
| FAS2-WENG-LO003 | demonstrate understanding of the concepts of kinetic energy, gravitational potential energy and elastic potential energy, and use the formulae to calculate these | Uses \(E_k=\frac12mv^2\), \(E_g=mgh\), and elastic potential energy formulae. | CCEA spec; PDF energy slide; transcript | Core; elastic PE evidence-light | Speed, mass, height, Hooke bridge |
| FAS2-WENG-LO004 | demonstrate understanding of and use the relationship between the change in energy of a system and the work done by the external forces, and use the Principle of Conservation of Mechanical Energy in appropriate cases | Work-energy principle and conservation equation. | CCEA spec; conservation slide; transcript | Core | Forces, SUVAT, friction |
| FAS2-POW-LO001 | use the definition of power as the rate at which a force does work, leading to \(P=Fv\), and the rate of increase of energy | Derives \(P=W/t=Fv\). | CCEA spec; PDF/transcript power | Core | Rates, speed |
| FAS2-POW-LO002 | solve problems involving power, including vehicles in motion and pumps raising and ejecting water | Vehicle and generated pump practice. | CCEA spec; transcript for vehicles | Core; pumps evidence-light | Forces, units |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to calculate work done by constant forces, angled forces and vector forces; calculate work done by a variable force using \(W=\int_a^bF(x)\,dx\); use kinetic, gravitational and elastic potential energy; set up work-energy equations; apply conservation of mechanical energy; derive and use \(P=Fv\); solve vehicle power problems; and solve pump raising/ejecting water problems.

## Bridge objectives

You should connect this lesson to ordinary A-Level Maths by using \(F=ma\), equilibrium, resolving forces, friction, speed as magnitude of velocity, and definite integration as accumulation.

## Exam technique objectives

You should state what energy is available at the start, what energy is present at the end, what work is done against friction or resistance, whether force and displacement are directionally consistent, and whether units require conversion.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should be comfortable with formula substitution, right-angled trigonometry, Pythagoras, metres, seconds, kilograms, newtons, joules and watts.

## Ordinary AS/A2 Mathematics foundations

Weight is \(mg\) and acts vertically downwards. Normal reaction \(R\) acts perpendicular to the surface. On a horizontal surface with no other vertical force, \(R=mg\). On a slope with no other perpendicular force, \(R=mg\cos\theta\). If a pulling force has an upward component, \(R\) is reduced.

Friction satisfies \(F_r\leq \mu R\). When the body is moving or at limiting equilibrium, use \(F_r=\mu R\). If the particle is stationary and not at limiting equilibrium, friction may be less than \(\mu R\).

For a force \(F\) at angle \(\theta\):
\[
F_x=F\cos\theta,\qquad F_y=F\sin\theta.
\]
Cosine means adjacent to the chosen angle; sine means opposite the chosen angle.

For a body on a slope inclined at \(\theta\), the component of weight down the slope is \(mg\sin\theta\), and the component perpendicular into the slope is \(mg\cos\theta\).

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Quantities and Units | Use SI units: kg, m, s, N, \(\text{m s}^{-2}\). | Work and energy use joules; power uses watts. | Convert kW to W, tonnes to kg, cm to m before calculating. |
| AS2 Kinematics | Speed, velocity, acceleration, \(s=vt\), SUVAT. | KE uses speed through \(\frac12mv^2\); work-energy can replace SUVAT. | In KE, \(v\) is speed, not signed velocity. |
| AS2 Forces and Newton’s laws | \(F=ma\), equilibrium, resultant force. | Energy equations track work over a whole journey. | Do not force every problem into \(F=ma\) if energy is cleaner. |
| AS2 Resolving forces | Components \(F\cos\theta\), \(F\sin\theta\), slope components. | Work uses the component in the direction of displacement. | Never multiply full force by full sloping distance unless aligned. |
| AS2 Friction | \(F_r\leq\mu R\), rough/smooth surfaces. | Work against friction is \(F_rs\). | Friction opposes motion and is not always automatically \(\mu R\) when stationary. |
| AS1 Integration | Definite integrals accumulate area. | Variable-force work is \(W=\int_a^bF(x)\,dx\). | \(W=Fs\) only works directly when force is constant. |
| Rates and kinematics | Speed is distance per unit time. | Power is work or energy per unit time. | In \(P=Fv\), use the force component in the direction of motion. |

In ordinary A-Level Maths, this idea appeared as forces causing acceleration and motion. In Further Maths, the same idea becomes a bookkeeping system for energy. The key upgrade is that work becomes the bridge between force and energy. The danger is that old habits can become too local: \(F=ma\) tells you about an instant, while work-energy often tells you about a whole journey.

# 6. Big Picture Explanation

Work, energy and power are the accounting system of mechanics. Forces tell us what is pushing, pulling or resisting. Kinematics tells us how a particle moves. Energy tells us what has been paid in, stored, spent, and transferred to heat, sound or resistance.

For a constant force in the direction of motion:
\[
W=Fs.
\]
If the force is not in the direction of motion, use components:
\[
W=Fs\cos\theta.
\]
If force and displacement are vectors:
\[
W=\mathbf F\cdot\mathbf s.
\]

A rough slope model from the evidence has a pulling force \(Y\), friction \(F_r\), normal reaction \(R\), weight \(mg\), distance \(x\) and slope angle \(30^\circ\). The energy transfer is:
\[
Yx=F_rx+mgx\sin30^\circ+\Delta E_k.
\]

Typical modelling assumptions include: particle, smooth surface, rough surface, constant speed, constant resistance, light inextensible string, small smooth pulley, line of greatest slope, and \(g=9.8\text{ m s}^{-2}\) unless otherwise stated.

# 7. Key Definitions and Notation

| Symbol | Meaning | Unit |
|---|---|---|
| \(W\) | Work done | J |
| \(F\) | Force magnitude | N |
| \(\mathbf F\) | Force vector | N |
| \(s,d\) | Distance or displacement | m |
| \(\mathbf s\) | Displacement vector | m |
| \(m\) | Mass | kg |
| \(g\) | Acceleration due to gravity | \(\text{m s}^{-2}\) |
| \(u,v\) | Initial and final speeds | \(\text{m s}^{-1}\) |
| \(h\) | Vertical height | m |
| \(E_k\) | Kinetic energy | J |
| \(E_p\) | Potential energy | J |
| \(R\) | Normal reaction or resistance, depending on definition | N |
| \(F_r\) | Frictional force | N |
| \(\mu\) | Coefficient of friction | none |
| \(P\) | Power or pulling force, depending on definition | W or N |

Work by a constant aligned force:
\[
W=Fs.
\]
Work by an angled force:
\[
W=Fs\cos\theta.
\]
Vector work:
\[
W=\mathbf F\cdot\mathbf s=F_1s_1+F_2s_2+F_3s_3.
\]
Variable-force work:
\[
W=\int_a^bF(x)\,dx.
\]
Kinetic energy:
\[
E_k=\frac12mv^2,
\]
where \(v\) is speed, not velocity. Gravitational potential energy:
\[
E_g=mgh.
\]
Elastic potential energy:
\[
E_{\text{elastic}}=\frac12kx^2\quad\text{or}\quad E_{\text{elastic}}=\frac{\lambda x^2}{2l}.
\]
Power:
\[
P=\frac{W}{t}=Fv.
\]

# 8. Core Theory

## 8.1 Work as energy transfer

Work transfers energy from one place or form to another. When a force does work, energy is being transferred. For a constant force in the direction of motion:
\[
W=Fs.
\]
A horizontal force of \(8\text{ N}\) moving a box \(5\text{ m}\) does:
\[
W=8\times5=40\text{ J}.
\]

## 8.2 Direction consistency

If a force \(F\) acts at angle \(\theta\) above the direction of motion, only the component \(F\cos\theta\) does work:
\[
W=(F\cos\theta)s=Fs\cos\theta.
\]
Alternatively, keep the force whole and resolve the displacement. For gravity on a slope, the vertical distance is often the cleanest route.

## 8.3 Scalar product work

Let
\[
\mathbf F=F_1\mathbf i+F_2\mathbf j+F_3\mathbf k,
\qquad
\mathbf s=s_1\mathbf i+s_2\mathbf j+s_3\mathbf k.
\]
Then:
\[
W=\mathbf F\cdot\mathbf s=F_1s_1+F_2s_2+F_3s_3.
\]
Also:
\[
W=|\mathbf F||\mathbf s|\cos\theta.
\]

Example:
\[
\mathbf F=3\mathbf i-2\mathbf j+6\mathbf k,
\qquad
\mathbf s=4\mathbf i+5\mathbf j-\mathbf k.
\]
Then:
\[
W=(3)(4)+(-2)(5)+(6)(-1)=12-10-6=-4\text{ J}.
\]
A negative value means the force acts overall against the displacement.

## 8.4 Work done by a variable force

If force varies with displacement \(x\), break the journey into tiny pieces:
\[
\Delta W\approx F(x)\Delta x.
\]
Adding and taking the limit gives:
\[
W=\int_a^bF(x)\,dx.
\]
Example:
\[
F(x)=3x^2+2,
\qquad 1\le x\le4.
\]
Then:
\[
W=\int_1^4(3x^2+2)\,dx=[x^3+2x]_1^4=(64+8)-(1+2)=69\text{ J}.
\]

## 8.5 Kinetic energy

\[
E_k=\frac12mv^2.
\]
A derivation from ordinary mechanics starts from \(F=ma\), \(W=Fs=mas\), and \(v^2=u^2+2as\). Since \(as=(v^2-u^2)/2\),
\[
W=\frac12mv^2-\frac12mu^2=\Delta E_k.
\]
If \(u=0\), then \(W=\frac12mv^2\).

For vector velocity, find speed first. If \(\mathbf v=3\mathbf i-4\mathbf j\), then \(|\mathbf v|=5\), so a \(4\text{ kg}\) particle has:
\[
E_k=\frac12(4)(5^2)=50\text{ J}.
\]

## 8.6 Gravitational potential energy

\[
E_g=mgh.
\]
Here \(h\) is vertical height above a chosen zero level. If a body moves a distance \(s\) up a slope inclined at \(\theta\), then:
\[
h=s\sin\theta,
\qquad
\Delta E_g=mg(s\sin\theta).
\]
Equivalently, use the component \(mg\sin\theta\) along the slope:
\[
(mg\sin\theta)s=mgs\sin\theta.
\]

## 8.7 Work done against friction

If a particle moves distance \(s\) along a rough surface and friction has magnitude \(F_r\), then:
\[
\text{work against friction}=F_rs.
\]
If sliding and \(F_r=\mu R\), then:
\[
\text{work against friction}=\mu Rs.
\]
On a slope with no other perpendicular force:
\[
R=mg\cos\theta.
\]
Gravity uses vertical height; friction uses distance along the surface.

## 8.8 Work-energy principle

The key equation is:
\[
\text{Work in}+\text{Initial KE}+\text{Initial GPE}
=
\text{Final KE}+\text{Final GPE}+\text{Work out}.
\]
Using formulae:
\[
Fs+\frac12mu^2+mgh_1=\frac12mv^2+mgh_2+Rs.
\]
Mechanical energy is conserved only when no non-conservative work is done.

## 8.9 Power

Power is rate of doing work:
\[
P=\frac{W}{t}.
\]
If \(W=Fs\), then:
\[
P=\frac{Fs}{t}=F\frac{s}{t}=Fv.
\]
Use the component of force in the direction of motion. If the force is angled:
\[
P=(F\cos\theta)v.
\]
For vehicles:
\[
F=\frac Pv.
\]
On a horizontal road with resistance \(R\):
\[
\frac Pv-R=ma.
\]
At maximum speed, \(a=0\), so:
\[
\frac Pv=R,
\qquad v=\frac PR.
\]
For uphill motion:
\[
\frac Pv-R-mg\sin\theta=ma.
\]
For pumps with mass flow rate \(r\):
\[
P=rgh
\]
for raising water, and if water is ejected with speed \(v\),
\[
P=rgh+\frac12rv^2.
\]

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerMermaid-001 | Source: CCEA FAS2-WENG/FAS2-POW specification + supplied Work, Energy and Power PDF/transcript evidence | Insert from mermaid/FAS2WorkEnergyAndPowerMermaid-001.md | Purpose: Show how force, displacement, work, kinetic energy, gravitational potential energy, elastic potential energy, resistance and power connect.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerSVG-001 | Source: FM1-Chp2-Work Energy and Power.pdf, page 2, work definition slide | Insert from svg/FAS2WorkEnergyAndPowerSVG-001.svg | Purpose: Show a horizontal force moving a box across a horizontal floor, preserving the force-distance direction consistency.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerSVG-002 | Source: FM1-Chp2-Work Energy and Power.pdf, page 3, rough slope work slide | Insert from svg/FAS2WorkEnergyAndPowerSVG-002.svg | Purpose: Show work done by a pulling force on a rough slope and the three possible energy destinations.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerSVG-003 | Source: FM1-Chp2-Work Energy and Power.pdf, page 11, conservation of energy slide + transcript energy-bank explanation | Insert from svg/FAS2WorkEnergyAndPowerSVG-003.svg | Purpose: Display the work-energy principle as an energy ledger.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerTikZ-002 | Source: CCEA FAS2-WENG-LO001 + AI-proposed teaching enhancement based on lesson evidence | Insert from tikz/FAS2WorkEnergyAndPowerTikZ-002.tex | Purpose: Show that scalar product work is the force component in the displacement direction multiplied by displacement.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerTikZ-001 | Source: FM1-Chp2-Work Energy and Power.pdf page 3 + transcript rough-slope explanation | Insert from tikz/FAS2WorkEnergyAndPowerTikZ-001.tex | Purpose: Preserve a precise rough-plane force diagram with energy-relevant components.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerSVG-004 | Source: FM1-Chp2-Work Energy and Power.pdf power slide + transcript power examples | Insert from svg/FAS2WorkEnergyAndPowerSVG-004.svg | Purpose: Show the derivation and use of \(P=Fv\), including unit conversions and vehicle interpretation.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA Further Maths specification | Insert from svg/FAS2WorkEnergyAndPowerBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2WorkEnergyAndPowerSVG-005 | Source: CCEA FAS2-POW-LO002 specification requirement + AI-proposed teaching enhancement | Insert from svg/FAS2WorkEnergyAndPowerSVG-005.svg | Purpose: Show pump raising and ejecting water, because pump problems are required by CCEA but not supplied in the lesson-specific evidence.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2WorkEnergyAndPowerWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FAS2-WENG-LO001 and lesson evidence on direction consistency | Insert from widgets/FAS2WorkEnergyAndPowerWidget-001.html | Purpose: Reinforce \(W=Fs\cos\theta\) and \(W=\mathbf F\cdot\mathbf s\).]

[INTERACTIVE PLACEHOLDER: FAS2WorkEnergyAndPowerWidget-002 | Source: AI-proposed teaching enhancement based on supplied rough-plane work-energy evidence | Insert from widgets/FAS2WorkEnergyAndPowerWidget-002.html | Purpose: Help students construct the correct work-energy equation for a particle on a rough slope.]

[INTERACTIVE PLACEHOLDER: FAS2WorkEnergyAndPowerWidget-003 | Source: AI-proposed teaching enhancement based on the work-energy principle slide and transcript energy-bank analogy | Insert from widgets/FAS2WorkEnergyAndPowerWidget-003.html | Purpose: Train students to place each term on the correct side of the energy equation.]

[INTERACTIVE PLACEHOLDER: FAS2WorkEnergyAndPowerWidget-004 | Source: AI-proposed teaching enhancement based on supplied power examples and CCEA FAS2-POW-LO002 | Insert from widgets/FAS2WorkEnergyAndPowerWidget-004.html | Purpose: Help students model vehicle power, resistance, acceleration and maximum speed.]

[INTERACTIVE PLACEHOLDER: FAS2WorkEnergyAndPowerWidget-005 | Source: AI-proposed specification-required enhancement based on CCEA FAS2-POW-LO002 | Insert from widgets/FAS2WorkEnergyAndPowerWidget-005.html | Purpose: Cover pump raising and ejecting water, an explicit CCEA requirement not directly evidenced in supplied lesson materials.]

# 11. Worked Examples

## Worked Example 1: Horizontal force doing work

A horizontal force of \(8\text{ N}\) moves a box \(5\text{ m}\) across a horizontal floor. The force and displacement are in the same direction, so:
\[
W=Fs=8\times5=40\text{ J}.
\]

## Worked Example 2: Vertical lift at constant speed

A load of bricks of mass \(30\text{ kg}\) is raised vertically \(7\text{ m}\) at constant speed. Constant speed means \(T=30g\). Work done:
\[
W=(30g)(7)=210g=2058\text{ J}=2060\text{ J}\quad(3\text{ s.f.}).
\]
Equivalently, \(W=mgh=30g\cdot7\).

## Worked Example 3: Rough horizontal floor

A \(3\text{ kg}\) box moves at \(3\text{ m s}^{-1}\) for \(2\text{ s}\) on a rough horizontal floor with \(\mu=0.45\). Since \(R=3g\),
\[
F_r=0.45(3g)=1.35g.
\]
Constant speed means the pushing force is \(1.35g\). Distance:
\[
s=3\times2=6.
\]
Work:
\[
W=(1.35g)(6)=79.38\text{ J}\approx79\text{ J}.
\]

## Worked Example 4: Work done by gravity on a smooth slide

A \(40\text{ kg}\) boy slides \(3\text{ m}\) down a smooth slide inclined at \(25^\circ\). The component of weight down the slope is \(40g\sin25^\circ\). Work:
\[
W=(40g\sin25^\circ)(3)=120g\sin25^\circ=497\text{ J}\quad(3\text{ s.f.}).
\]
Alternatively use vertical drop \(3\sin25^\circ\):
\[
W=40g(3\sin25^\circ).
\]

## Worked Example 5: Package pulled up a rough plane

A \(2\text{ kg}\) package is pulled at constant speed \(12\text{ m}\) up a rough plane inclined at \(30^\circ\). \(\mu=0.35\).

Work against gravity:
\[
h=12\sin30^\circ=6,
\quad W_g=2g(6)=117.6\text{ J}=118\text{ J}.
\]
Normal reaction:
\[
R=2g\cos30^\circ.
\]
Work against friction:
\[
W_f=0.35(2g\cos30^\circ)(12)=71.3\text{ J}.
\]
Constant speed means \(\Delta E_k=0\), so work by the pulling force is:
\[
W_P=W_g+W_f=117.6+71.291\ldots=189\text{ J}.
\]

## Worked Example 6: Kinetic energy quickfire

For \(m=4\text{ kg}\) and \(\mathbf v=3\mathbf i-4\mathbf j\), speed is:
\[
|\mathbf v|=\sqrt{3^2+(-4)^2}=5.
\]
So:
\[
E_k=\frac12(4)(5^2)=50\text{ J}.
\]
For \(m=20\text{ kg}\) and \(\mathbf v=-5\mathbf i+12\mathbf j\), speed is \(13\), so:
\[
E_k=\frac12(20)(13^2)=1690\text{ J}.
\]

## Worked Example 7: GPE from \(\tan\theta=3/4\), then speed

Since \(\tan\theta=3/4\), use a \(3\)-\(4\)-\(5\) triangle, so \(\sin\theta=3/5\). A \(3\text{ kg}\) parcel moves \(10\text{ m}\) up the slope. Height:
\[
h=10\cdot\frac35=6.
\]
GPE gained:
\[
\Delta E_p=3g(6)=176.4\text{ J}=176\text{ J}\quad(3\text{ s.f.}).
\]
If all this becomes KE:
\[
\frac12(3)v^2=176.4,
\quad 1.5v^2=176.4,
\quad v=10.8\text{ m s}^{-1}.
\]
Use unrounded \(176.4\) in part (b).

## Worked Example 8: Energy loss on a rough slope

A \(0.6\text{ kg}\) package slides \(12\text{ m}\) down a \(30^\circ\) rough plane. Speed changes from \(10\) to \(9\text{ m s}^{-1}\).

Initial KE:
\[
\frac12(0.6)(10^2)=30\text{ J}.
\]
Final KE:
\[
\frac12(0.6)(9^2)=24.3\text{ J}.
\]
KE lost:
\[
5.7\text{ J}.
\]
Vertical drop:
\[
12\sin30^\circ=6.
\]
GPE lost:
\[
0.6g(6)=35.28\text{ J}.
\]
Total loss:
\[
5.7+35.28=40.98\text{ J}=41.0\text{ J}.
\]
If this equals work against friction:
\[
\mu(0.6g\cos30^\circ)(12)=40.98,
\]
so:
\[
\mu=\frac{40.98}{0.6(9.8)\cos30^\circ\times12}=0.671\quad(3\text{ s.f.}).
\]

## Worked Example 9: Projected up a rough plane

A \(2\text{ kg}\) particle is projected at \(8\text{ m s}^{-1}\) up a rough \(45^\circ\) plane with \(\mu=0.4\). Initial KE:
\[
\frac12(2)(8^2)=64\text{ J}.
\]
Let distance travelled before rest be \(s\). Height gained is \(s\sin45^\circ\), and friction is \(0.4(2g\cos45^\circ)\). Energy equation:
\[
64=2g(s\sin45^\circ)+0.4(2g\cos45^\circ)s.
\]
Thus:
\[
s=\frac{64}{2g\sin45^\circ+0.4(2g\cos45^\circ)}=3.30\text{ m}.
\]

## Worked Example 10: Work done by a skier

Let work done by the skier be \(W\). A skier of mass \(55\text{ kg}\) passes \(A\) at \(6\text{ m s}^{-1}\), later reaches \(B\) at \(4\text{ m s}^{-1}\), with heights represented as \(50\text{ m}\) and \(25\text{ m}\) above a chosen zero level. Resistance is \(12\text{ N}\) over \(1400\text{ m}\). Energy equation:
\[
W+\frac12(55)(6^2)+55g(50)
=
\frac12(55)(4^2)+55g(25)+12(1400).
\]
Compute:
\[
W+27940=30715,
\quad W=2775\text{ J}=2780\text{ J}\quad(3\text{ s.f.}).
\]

## Worked Example 11: Jogger power

On flat ground, resistance \(30\text{ N}\) and speed \(4\text{ m s}^{-1}\):
\[
P=Fv=30\times4=120\text{ W}.
\]
Uphill with \(m=60\), \(g=10\), \(\sin\alpha=1/15\), speed \(3\):
\[
mg\sin\alpha=60(10)\frac1{15}=40\text{ N}.
\]
Driving force at constant speed:
\[
F=30+40=70\text{ N}.
\]
Power:
\[
P=70\times3=210\text{ W}.
\]

## Worked Example 12: Engine power and driving force

A van has engine power \(24\text{ kW}=24000\text{ W}\) and speed \(12\text{ m s}^{-1}\). From \(P=Fv\):
\[
F=\frac{24000}{12}=2000\text{ N}.
\]

## Worked Example 13: Vehicle acceleration

If resistance is \(800\text{ N}\) and mass is \(1250\text{ kg}\), resultant force is:
\[
2000-800=1200\text{ N}.
\]
Then:
\[
1200=1250a,
\quad a=0.96\text{ m s}^{-2}.
\]

## Worked Example 14: Maximum speed

Power \(24\text{ kW}=24000\text{ W}\), constant resistance \(800\text{ N}\). At maximum speed:
\[
\frac{24000}{v}=800,
\quad v=30\text{ m s}^{-1}.
\]

## Worked Example 15: Pump raising and ejecting water

A pump raises water at \(8\text{ kg s}^{-1}\) through \(12\text{ m}\), then ejects it at \(5\text{ m s}^{-1}\). Useful power:
\[
P_{\text{raise}}=8(9.8)(12)=940.8\text{ W},
\]
\[
P_{\text{kinetic}}=\frac12(8)(5^2)=100\text{ W}.
\]
Total:
\[
P=1040.8\text{ W}=1.04\text{ kW}\quad(3\text{ s.f.}).
\]

# 12. Common Mistakes and Exam Traps

- Using \(W=Fs\) when the force and displacement are not in the same direction. Use \(W=Fs\cos\theta\) or \(W=\mathbf F\cdot\mathbf s\).
- Confusing work done by friction with work done against friction. Work done by friction is negative if friction opposes displacement; work done against friction is a positive energy cost.
- Using vertical height for friction. Friction uses distance along the surface.
- Using slope distance inside \(mgh\). The \(h\) in \(mgh\) is vertical height.
- Using \(R=mg\) on a slope. Usually \(R=mg\cos\theta\), unless another perpendicular force acts.
- Assuming friction is always \(\mu R\). Static friction can be less than its maximum.
- Forgetting speed is the magnitude of velocity in \(E_k=\frac12mv^2\).
- Rounding too early. Use unrounded values inside later parts.
- Treating \(P\) as power when a diagram has defined \(P\) as a pulling force.
- Forgetting \(1\text{ kW}=1000\text{ W}\).
- Thinking maximum speed means maximum acceleration. At maximum speed, \(a=0\).
- Using \(P=Fv\) with the wrong force. Use the component in the direction of motion.
- In pump problems, forgetting \(\frac12rv^2\) when water is ejected with speed.

# 13. Practice Questions

These are generated practice questions, not past-paper or textbook questions.

1. A horizontal force of \(18\text{ N}\) moves a particle \(7\text{ m}\). Find the work done.
2. A force of \(40\text{ N}\) acts at \(60^\circ\) to the direction of motion. The particle moves \(5\text{ m}\). Find the work done.
3. \(\mathbf F=2\mathbf i+5\mathbf j-3\mathbf k\), \(\mathbf s=4\mathbf i-\mathbf j+2\mathbf k\). Find the work done.
4. A \(6\text{ kg}\) particle has velocity \(8\mathbf i-6\mathbf j\). Find its KE.
5. A \(12\text{ kg}\) object is raised vertically \(4.5\text{ m}\). Find GPE gain.
6. A \(5\text{ kg}\) block is pulled \(8\text{ m}\) by a \(30\text{ N}\) force at \(20^\circ\). Find work by the pull.
7. A \(3\text{ kg}\) particle moves \(10\text{ m}\) up a smooth \(25^\circ\) plane. Find work against gravity.
8. A \(4\text{ kg}\) box moves at constant speed on a rough horizontal floor, \(\mu=0.2\), distance \(6\text{ m}\). Find work by the pushing force.
9. A \(5\text{ kg}\) package is pulled at constant speed \(9\text{ m}\) up a \(30^\circ\) rough plane with \(\mu=0.25\). Find work against gravity, friction, and pulling force.
10. A \(3\text{ kg}\) particle is projected at \(10\text{ m s}^{-1}\) up a rough \(20^\circ\) plane with \(\mu=0.3\). Find distance before rest.
11. \(F(x)=4x+3\). Find work from \(x=2\) to \(x=6\).
12. An elastic string with \(k=80\text{ N m}^{-1}\) is extended by \(0.15\text{ m}\). Find elastic PE.
13. A cyclist and bicycle of mass \(70\text{ kg}\) gain \(12\text{ m}\) height over \(300\text{ m}\), speed changes from \(5\) to \(7\text{ m s}^{-1}\), resistance \(18\text{ N}\). Find work done by cyclist.
14. A motor does \(36000\text{ J}\) of work in \(45\text{ s}\). Find power.
15. A vehicle travels at \(20\text{ m s}^{-1}\) with driving force \(1500\text{ N}\). Find power in kW.
16. A \(1200\text{ kg}\) car has power \(48\text{ kW}\). At \(16\text{ m s}^{-1}\), resistance is \(900\text{ N}\). Find acceleration.
17. A vehicle has power \(60\text{ kW}\) and resistance \(1200\text{ N}\). Find maximum speed.
18. A pump raises water at \(15\text{ kg s}^{-1}\) through \(9\text{ m}\), ejecting it at \(4\text{ m s}^{-1}\). Find useful power.
19. A \(1400\text{ kg}\) vehicle moves uphill with \(\sin\theta=1/20\), resistance \(650\text{ N}\), speed \(12\text{ m s}^{-1}\), power \(54\text{ kW}\). Find acceleration.

# 14. Worked Solutions

1. \(W=18\times7=126\text{ J}\).

2. \(W=40(5)\cos60^\circ=100\text{ J}\).

3. \(W=(2)(4)+(5)(-1)+(-3)(2)=8-5-6=-3\text{ J}\).

4. Speed \(=\sqrt{8^2+(-6)^2}=10\). KE \(=\frac12(6)(10^2)=300\text{ J}\).

5. \(\Delta E_p=12(9.8)(4.5)=529.2\text{ J}=529\text{ J}\).

6. \(W=30(8)\cos20^\circ=226\text{ J}\) to 3 s.f.

7. \(h=10\sin25^\circ\). Work \(=3(9.8)(10\sin25^\circ)=124\text{ J}\).

8. \(R=4g\), \(F_r=0.2(4g)=0.8g=7.84\text{ N}\). Work \(=7.84(6)=47.0\text{ J}\).

9. \(h=9\sin30^\circ=4.5\). Gravity work \(=5(9.8)(4.5)=221\text{ J}\). Friction work \(=0.25(5g\cos30^\circ)(9)=95.5\text{ J}\). Pulling work \(=316\text{ J}\).

10. Initial KE \(=\frac12(3)(10^2)=150\). Equation:
\[
150=3g(s\sin20^\circ)+0.3(3g\cos20^\circ)s.
\]
So:
\[
s=\frac{150}{3g\sin20^\circ+0.9g\cos20^\circ}=8.18\text{ m}.
\]

11. \(W=\int_2^6(4x+3)\,dx=[2x^2+3x]_2^6=90-14=76\text{ J}\).

12. \(E=\frac12(80)(0.15^2)=0.900\text{ J}\).

13. Let work be \(W\). Equation:
\[
W+\frac12(70)(5^2)=\frac12(70)(7^2)+70g(12)+18(300).
\]
So \(W+875=1715+8232+5400=15347\), hence \(W=14472\text{ J}=14.5\text{ kJ}\).

14. \(P=36000/45=800\text{ W}\).

15. \(P=1500(20)=30000\text{ W}=30\text{ kW}\).

16. \(48\text{ kW}=48000\text{ W}\). Driving force \(=48000/16=3000\text{ N}\). Resultant \(=3000-900=2100\). \(2100=1200a\), so \(a=1.75\text{ m s}^{-2}\).

17. \(60\text{ kW}=60000\text{ W}\). At maximum speed \(a=0\): \(60000=1200v\), so \(v=50\text{ m s}^{-1}\).

18. Raise power \(=15(9.8)(9)=1323\text{ W}\). Kinetic power \(=\frac12(15)(4^2)=120\text{ W}\). Useful power \(=1443\text{ W}=1.44\text{ kW}\).

19. \(54\text{ kW}=54000\text{ W}\). Driving force \(=54000/12=4500\text{ N}\). Weight component \(=1400(9.8)(1/20)=686\text{ N}\). Resultant \(=4500-650-686=3164\). Then \(3164=1400a\), so \(a=2.26\text{ m s}^{-2}\).

# 15. Exam Technique Notes

Start with a diagram. Decide whether it is a force problem, an energy problem or a power problem. Check direction consistency before using \(W=Fs\). State the zero level for GPE. Use unrounded values during calculations. For vehicles, fixed power means \(F=P/v\), so the driving force decreases as speed increases. At maximum speed, set \(a=0\). For uphill power, include \(mg\sin\theta\). For pump problems, identify mass flow rate and whether water is ejected with speed. Define ambiguous symbols such as \(R\) and \(P\).

# 16. Syllabus Gap Check

| LO ID | Covered? | Evidence strength |
|---|---:|---|
| FAS2-WENG-LO001 | Yes | Strong for \(W=Fs\), CCEA-required for scalar product |
| FAS2-WENG-LO002 | Yes | Specification-required, lesson-specific evidence-light |
| FAS2-WENG-LO003 | Yes | Strong for KE/GPE, evidence-light for elastic PE |
| FAS2-WENG-LO004 | Yes | Strong |
| FAS2-POW-LO001 | Yes | Strong |
| FAS2-POW-LO002 | Yes | Strong for vehicles, evidence-light for pumps |

## Off-Spec Content Found but Excluded

- Full non-constant gravitational field treatment: excluded from core. Only the warning that \(mgh\) assumes constant gravity is preserved.
- Full Hooke’s law modelling: not developed here. Elastic PE included only because CCEA WENG requires it.
- Pearson exercise references: preserved only as source notes, not CCEA authority.
- Edexcel M2 labels: used only as cross-board on-spec examples, not CCEA past papers.
- Detailed limiting equilibrium friction theory: used as prerequisite warning only.

# 17. Recommended Enhancements Not in the Evidence

Recommended diagrams include constant-force work, force-at-angle projection, rough-plane work-energy, energy ledger, Newton route versus energy route, vehicle power, and pump power. Recommended widgets include scalar product calculator, rough slope work-energy builder, energy ledger drag-and-drop, vehicle power checker and pump power widget. These are proposed enhancements unless explicitly evidence-backed.

# 18. Supplementary Sources Used

Project Sources used: CCEA GCE Further Mathematics Specification Map, Further Maths README module map, Further Maths Evidence Drop Checklist, CCEA GCE Mathematics Specification Map, Ordinary A-Level Maths Bridge Spec Extracts.

Lesson-specific evidence used: `FM1-Chp2-Work Energy and Power.pdf`, `transcripts.md`, and `Chapter_2_Work,_Energy_&_Power_🎯_(Further_Mechanics_1)_screenshots.pdf`.

Ordinary A-Level Maths sources were used only as bridge context and do not override the Further Mathematics specification. Cross-board Pearson/Edexcel materials were used only where aligned with CCEA FAS2-WENG/FAS2-POW.

# 19. Final Student Checklist

## Prerequisite confidence checklist

- [ ] I can draw weight vertically downwards.
- [ ] I can draw normal reaction perpendicular to the surface.
- [ ] I can resolve forces using sine and cosine.
- [ ] I can resolve weight on slopes into \(mg\sin\theta\) and \(mg\cos\theta\).
- [ ] I can calculate friction using \(F_r=\mu R\) when appropriate.
- [ ] I can find speed from a velocity vector.
- [ ] I can integrate a simple force function.

## Further Maths method checklist

- [ ] I can calculate \(W=Fs\).
- [ ] I can calculate \(W=Fs\cos\theta\).
- [ ] I can calculate \(W=\mathbf F\cdot\mathbf s\).
- [ ] I can calculate \(W=\int_a^bF(x)\,dx\).
- [ ] I can use \(E_k=\frac12mv^2\), \(E_g=mgh\), and elastic PE.
- [ ] I can write a work-energy equation.
- [ ] I can use \(P=W/t\) and \(P=Fv\).
- [ ] I can solve vehicle and pump power problems.

## Exam technique checklist

- [ ] I convert kW to W.
- [ ] I convert tonnes to kg and cm to m.
- [ ] I use vertical height in \(mgh\).
- [ ] I use surface distance for friction work.
- [ ] I use unrounded values in working.
- [ ] I set \(a=0\) at maximum speed.
- [ ] I label generated practice honestly.
