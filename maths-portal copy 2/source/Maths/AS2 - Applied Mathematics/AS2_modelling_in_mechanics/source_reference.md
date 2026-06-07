# Source Reference: AS2 Modelling in Mechanics

## Source Priority

The lesson uses the project evidence hierarchy:

1. CCEA Mathematics specification map or extract.
2. Topic metadata and evidence checklist.
3. Lesson PDF, transcript, slide text and visual evidence.
4. Cross-board or third-party material only where CCEA confirms the content is on-spec.

The CCEA specification map is the authority for unit names, topic codes, learning outcomes and syllabus boundaries.

## Core CCEA Specification Source

### CCEA GCE Mathematics Specification Map

Used for:

- Unit identity: AS2, AS 2 Applied Mathematics.
- Official AS2 mechanics topic areas:
  - AS2-QUNITS: Quantities and units in mechanics.
  - AS2-KIN: Kinematics.
  - AS2-FORCES: Forces and Newton's laws.
- LO IDs and topic boundaries.
- Decision that this lesson is primarily an AS2 mechanics introduction.

Relevant specification interpretation:

- The lesson is not filed as a separate official CCEA topic called “Modelling in Mechanics”.
- It is filed as `AS2_modelling_in_mechanics_lesson.md` with primary topic code `AS2-QUNITS`.
- It also previews AS2-KIN and AS2-FORCES content.

## Project Control Sources

### README-Module-Map.txt

Used for:

- Required metadata fields.
- Folder and file structure.
- Phase definitions.
- Placeholder format.
- Final packaging structure.

### Source-Evidence-Drop-Checklist.txt

Used for:

- Missing evidence log.
- Off-spec or boundary-risk log.
- Visual evidence checklist.
- Mathematical preservation checklist.
- End-of-phase checking rules.

## Lesson Evidence Sources

### MechYr1-Chp8-Introduction.pdf

Used for:

- Mechanics overview:
  - motion,
  - forces,
  - \(F=ma\) as the bridge.
- Force diagram:
  - weight,
  - friction,
  - tension,
  - reaction force.
- Motion graph interpretations:
  - displacement-time gradient gives velocity,
  - velocity-time gradient gives acceleration,
  - area under velocity-time graph gives distance.
- SUVAT preview.
- Non-constant acceleration preview:

  $$
  s=2t^3+3t,\qquad v=\frac{ds}{dt}=6t^2+3.
  $$

- Modelling assumptions:
  - particle,
  - rough/smooth surface,
  - smooth/light pulley,
  - inextensible string,
  - rod,
  - peg/support.
- SI units table.
- Scalar/vector comparison.
- Worked examples converting between scalar and vector forms.
- Test-your-understanding vector examples.

### Chapter_8_Modelling_in_Mechanics_Transcript.md

Used for:

- Teacher explanation of mechanics as motion, forces and their connection.
- Verbal explanation of force types and Newton's laws.
- Modelling-assumption consequences:
  - particle means dimensions negligible and mass concentrated at a point;
  - smooth surface means no friction;
  - rough surface means friction present;
  - smooth/light pulley gives equal tension on both sides;
  - inextensible string gives equal acceleration in connected objects.
- Scalar/vector explanation:
  - distance versus displacement;
  - speed versus velocity;
  - one-dimensional signed displacement.
- Worked-example reasoning:
  - \(5\cos60^\circ\) and \(5\sin60^\circ\);
  - vector magnitude by Pythagoras;
  - correct component signs for left/right/up/down;
  - angle with \(\mathbf{i}\) for the raccoon example.

### Chapter_8_Modelling_in_Mechanics_Screenshots.pdf

Used for:

- Visual support only.
- The file had no parsed text available, so no unique mathematical wording was taken from it.
- It helped confirm the visual layout of the introduction slide sequence.

## Cross-Board / Third-Party Status

The DrFrost/Pearson evidence is not CCEA-specific. It was used only because the CCEA AS2 mechanics specification confirms the relevant content areas:

- quantities and units;
- kinematics language;
- motion graphs;
- force concepts;
- Newton's laws;
- vectors/components as mechanics preparation;
- modelling and assumptions.

Any source branding or cross-board references appearing in the lesson evidence were excluded from the core lesson.

## Off-Spec or Boundary-Risk Log

| Evidence item | Why it is risky | Decision | Where logged |
|---|---|---|---|
| DrFrost/Pearson source | Not CCEA-specific | Used only as on-spec support | Phase 0, Phase 1, manifest |
| Cross-board logos/references | Not CCEA lesson content | Excluded | Phase 0, manifest |
| Rod and peg/support | More naturally linked to later mechanics contexts | Included only as future modelling vocabulary | Phase 1 modelling assumptions |
| Non-constant acceleration by calculus | Beyond this AS2 introduction | Mentioned only as future context | Phase 1 core theory |
| Pearson Exercise 8D | Full questions not supplied | Not reproduced | Phase 0 missing evidence |

## Evidence Limitations

| Limitation | Effect |
|---|---|
| No CCEA topic-specific README for “Modelling in Mechanics” was supplied | Topic identity inferred from the AS2 specification map |
| Screenshots PDF had no parsed text | No unique text was extracted from it |
| Full Pearson textbook exercise was not supplied | Only visible slide/test-your-understanding content was used |
| No official CCEA modelling assumptions extract was supplied | Assumptions are treated as lesson evidence aligned to AS2 mechanics, not as separate official wording |

## Asset Source Map

| Asset | Source basis |
|---|---|
| MER-001, SVG-001, TIKZ-001 | Mechanics overview slide |
| MER-002, SVG-002, TIKZ-002 | Scalars/vectors slide and transcript |
| MER-003, SVG-003, TIKZ-003 | SI units slide |
| MER-004, SVG-004, TIKZ-004 | Motion graph overview |
| MER-005, SVG-005, TIKZ-005 | Force diagram slide and transcript |
| MER-006, SVG-006, TIKZ-006 | Modelling assumptions slide and transcript |
| MER-007, SVG-007, TIKZ-007 | Scalar-to-vector resolving examples |
| MER-008 | Vector-to-scalar magnitude examples |
| MER-009 | Man walking from \(A\) to \(B\) to \(C\) example |
| MER-010 | Raccoon velocity angle example |
| Widget-001 | Interactive teaching enhancement based on component resolving |

## Final Source Decision

This lesson is suitable as a CCEA AS2 Applied Mathematics mechanics introduction, provided it remains labelled as:

- core for AS2-QUNITS and AS2-KIN language;
- bridge/preview for AS2-KIN graphs and SUVAT;
- bridge/preview for AS2-FORCES;
- not a standalone official CCEA topic called “Modelling in Mechanics”.
