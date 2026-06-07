# Optional Enrichment Lesson: Transportation Problems

**Suggested file name:** `offspec_transportation_problems_enrichment_lesson.md`  
**CCEA status:** **Off-spec enrichment only.** This lesson must not be filed as a required CCEA FAS1/FAS2/FA21/FA22 lesson unless later CCEA evidence confirms Transportation Problems are on-spec.

---

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics portal, enrichment only |
| CCEA status | Off-spec enrichment, not required CCEA core content |
| Unit | Not assigned |
| Applied section | Discrete and Decision Mathematics enrichment |
| Topic code | Not assigned |
| Topic name | Transportation Problems |
| Topic slug | `transportation_problems_enrichment` |
| Topic Pascal | `TransportationProblemsEnrichment` |
| Topic ID | `OffSpecTransportationProblemsEnrichment` |
| Lesson file name | `offspec_transportation_problems_enrichment_lesson.md` |
| CCEA LO IDs | None. No CCEA Further Mathematics LO found for transportation problems in supplied Project Sources. |
| Closest CCEA-adjacent area | FA22 Section D contains two-variable simplex tableau, but transportation problems are not the same as the CCEA two-variable simplex-tableau outcome. |
| Bridge tags | ordinary algebra, tables, inequalities, constraints, optimisation, decision maths enrichment |
| Topic tags | transportation, source, destination, supply, demand, cost matrix, north-west corner method, dummy point, degenerate solution, shadow cost, improvement index, stepping-stone method, linear programming |

This optional enrichment chapter teaches transportation problems: moving goods most efficiently, by time or cost, from a supply point/source such as a factory to a demand point/destination such as a warehouse, depot, shop or customer.

---

# 2. Evidence Map

| Evidence source | Evidence type | Used? | Notes |
|---|---:|---:|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | CCEA specification map | Yes, boundary only | No CCEA LO was found for transportation problems. |
| `Further_Maths_README_module_map.md` | Project map | Yes | Used for workflow and metadata conventions. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence checklist | Yes | Used for missing evidence and off-spec logging. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary Maths bridge source | Yes, bridge only | Used for tables, algebra, inequalities, optimisation language. |
| `Chapter_1_Transportation_Problems_⌨️_(Decision_2)_screenshots.pdf` | Visual lesson evidence | Yes | Image-only PDF. Rendered pages show D2 Transportation Problems, tables and north-west corner method slides. |
| `transcripts.md` | Teacher transcript | Yes | Main teaching evidence. Covers north-west corner method, unbalanced problems, degenerate solutions, shadow costs, improvement indices, stepping-stone method, LP and exam questions. |

## Visual evidence limitation

The screenshot PDF was uploaded as an image-based PDF, so no text was parsed automatically. The lesson relies mainly on transcript evidence and uses visible screenshot previews for table/diagram planning.

> Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

---

# 3. Specification Alignment

| CCEA LO ID | Official wording | Lesson coverage | Boundary decision |
|---|---|---|---|
| None | None found for transportation problems | Not applicable | This is off-spec enrichment only. |

## Nearest CCEA-adjacent link

CCEA confirms two-variable linear programming with simplex tableau in FA22, but this lesson uses transportation tableaux with many route variables \(x_{ij}\), north-west corner allocation and stepping-stone improvement. It is enrichment only and must not replace a CCEA simplex-tableau lesson.

---

# 4. Learning Objectives

By the end of this optional enrichment lesson, the student should be able to:

1. Interpret a transportation table: sources, destinations, unit costs, stock/supply totals and demand totals.
2. Decide whether a problem is balanced or unbalanced.
3. Use the north-west corner method to obtain an initial feasible allocation.
4. Calculate total cost from allocations and unit costs.
5. Add dummy demand or dummy supply points with zero transport costs.
6. Detect degeneracy using \(m+n-1\).
7. Repair degeneracy using a zero allocation.
8. Find shadow costs \(u_i\) and \(v_j\).
9. Find improvement indices \(I_{ij}=c_{ij}-(u_i+v_j)\).
10. Identify entering and exiting cells.
11. Use the stepping-stone method.
12. Formulate a transportation problem using route variables \(x_{ij}\).

---

# 5. Explicit Prerequisite Recap

## GCSE foundations

You need row totals, column totals, subtraction of remaining supply/demand, and multiplication of costs by quantities.

If 11 loads are sent at 180 per load:

\[
11\times 180=1980.
\]

## Ordinary A-Level foundations

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Algebra and notation | Define variables and form expressions | Route variables \(x_{ij}\) represent units transported from source \(i\) to destination \(j\). | Subscripts matter. |
| Inequalities and constraints | Write constraints such as \(x\ge 0\) | Every transported quantity satisfies \(x_{ij}\ge 0\). | Negative transported units are meaningless. |
| Tables and data interpretation | Read headings, rows and columns | Central cells are costs; edge values are supply/demand. | Do not confuse a cost with a stock or demand total. |
| Optimisation | Minimise or maximise an expression | Minimise total transportation cost subject to supply/demand constraints. | Feasible does not mean optimal. |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary algebra | A variable represents an unknown quantity | \(x_{ij}\) represents a route quantity. | \(x_{AR}\) and \(x_{RA}\) are not interchangeable. |
| Ordinary inequalities | Quantities can be constrained | Supply and demand become row/column constraints. | Supply and demand constraints have different contextual meanings. |
| Ordinary table reading | Tables organise information | A transportation table stores costs and constraints simultaneously. | Edge totals are not costs. |
| Ordinary optimisation | Optimise an expression | The objective is a sum of route cost terms. | Initial allocation may not be cheapest. |

In ordinary A-Level Maths, this idea appeared as forming expressions and constraints. In this enrichment topic, the same idea becomes a table-based transport system. The key upgrade is that every cell can represent a route. The danger is that the arithmetic looks simple, but one wrong row/column move derails the algorithm.

---

# 6. Big Picture Explanation

Transportation problems ask:

> How should goods be moved from suppliers to destinations so that demand is met at minimum cost?

The method has two broad stages:

1. Find an initial feasible allocation.
2. Improve it until no cheaper adjustment is available.

The north-west corner method gives the starting allocation. Shadow costs, improvement indices and the stepping-stone method test and improve it.

---

# 7. Key Definitions and Notation

## Source

A **source** is a supply point, such as a factory or supplier. Sources are usually listed down the left-hand side.

## Destination

A **destination** is a demand point, such as a warehouse, depot, shop or customer. Destinations are usually listed across the top.

## Unit cost

\(c_{ij}\) is the cost of transporting one unit from source \(i\) to destination \(j\).

## Allocation

\(x_{ij}\) is the number of units transported from source \(i\) to destination \(j\). Since a transported quantity cannot be negative:

\[
x_{ij}\ge 0.
\]

## Balanced problem

\[
\text{total supply}=\text{total demand}.
\]

## Unbalanced problem

\[
\text{total supply}\ne\text{total demand}.
\]

If supply exceeds demand, add dummy demand. If demand exceeds supply, add dummy supply. Dummy route costs are zero.

## Degenerate solution

For \(m\) sources and \(n\) destinations, a non-degenerate basic feasible transportation solution should have:

\[
m+n-1
\]

occupied cells. Fewer means degenerate.

## Shadow costs

For occupied cell \((i,j)\):

\[
u_i+v_j=c_{ij}.
\]

## Improvement index

For an unoccupied cell:

\[
I_{ij}=c_{ij}-(u_i+v_j).
\]

A negative value is potentially improving.

## Entering and exiting cells

The entering cell is usually the unused cell with the most negative improvement index. The exiting cell is the cell reduced to zero by the stepping-stone adjustment and then left blank.

## Theta

\(\theta\) is the amount diverted around a stepping-stone loop. Choose it as large as possible without making an allocation negative.

---

# 8. Core Theory

## 8.1 Transportation table anatomy

Example table:

| Source / Destination | \(W\) | \(X\) | \(Y\) | \(Z\) | Stock |
|---|---:|---:|---:|---:|---:|
| \(A\) | 180 | 110 | 130 | 290 | 14 |
| \(B\) | 190 | 250 | 150 | 280 | 16 |
| \(C\) | 240 | 270 | 190 | 120 | 20 |
| Demand | 11 | 15 | 14 | 10 | 50 |

Central entries are costs. Right-edge values are supplies. Bottom-edge values are demands.

Check balance:

\[
14+16+20=50,
\]

\[
11+15+14+10=50.
\]

So the problem is balanced.

## 8.2 North-west corner method

Algorithm:

1. Start in the north-west cell.
2. Allocate as much as possible: \(\min(\text{remaining supply},\text{remaining demand})\).
3. If demand is fulfilled, move right.
4. If supply is depleted, move down.
5. Repeat until complete.
6. Never move diagonally.

For the main example:

\[
x_{AW}=11,
\]
\[
x_{AX}=3,
\]
\[
x_{BX}=12,
\]
\[
x_{BY}=4,
\]
\[
x_{CY}=10,
\]
\[
x_{CZ}=10.
\]

Allocation table:

| Source / Destination | \(W\) | \(X\) | \(Y\) | \(Z\) | Stock |
|---|---:|---:|---:|---:|---:|
| \(A\) | 11 | 3 |  |  | 14 |
| \(B\) |  | 12 | 4 |  | 16 |
| \(C\) |  |  | 10 | 10 | 20 |
| Demand | 11 | 15 | 14 | 10 | 50 |

## 8.3 Total cost

\[
C=11(180)+3(110)+12(250)+4(150)+10(190)+10(120).
\]

\[
C=1980+330+3000+600+1900+1200=9010.
\]

\[
\boxed{C=9010}
\]

## 8.4 Occupied cells

Here \(m=3\) and \(n=4\), so:

\[
m+n-1=3+4-1=6.
\]

The occupied cells are:

\[
AW,AX,BX,BY,CY,CZ.
\]

There are 6, so the solution is non-degenerate.

## 8.5 Unbalanced problems

If total supply exceeds total demand:

\[
\text{dummy demand}=\text{total supply}-\text{total demand}.
\]

If total demand exceeds total supply:

\[
\text{dummy supply}=\text{total demand}-\text{total supply}.
\]

Dummy routes have zero cost.

Example excess supply:

\[
\text{demand}=50+40+30=120,
\]
\[
\text{supply}=40+60+50=150.
\]

Add dummy demand:

\[
150-120=30.
\]

Example excess demand:

\[
\text{supply}=55+70+65=190,
\]
\[
\text{demand}=74+72+68=214.
\]

Add dummy supply:

\[
214-190=24.
\]

If dummy supply is used for shop \(C\), then shop \(C\) has not actually had that demand met.

## 8.6 Degeneracy

If a \(4\)-source, \(3\)-destination allocation has only \(5\) occupied cells:

\[
4+3-1=6,
\]

and

\[
5<6.
\]

So it is degenerate. Add a zero allocation in a suitable unoccupied cell and treat it as occupied.

## 8.7 Shadow costs for the main example

Occupied costs:

\[
c_{AW}=180,
\quad c_{AX}=110,
\quad c_{BX}=250,
\quad c_{BY}=150,
\quad c_{CY}=190,
\quad c_{CZ}=120.
\]

Set:

\[
u_A=0.
\]

Then:

\[
0+v_W=180\Rightarrow v_W=180,
\]

\[
0+v_X=110\Rightarrow v_X=110,
\]

\[
u_B+110=250\Rightarrow u_B=140,
\]

\[
140+v_Y=150\Rightarrow v_Y=10,
\]

\[
u_C+10=190\Rightarrow u_C=180,
\]

\[
180+v_Z=120\Rightarrow v_Z=-60.
\]

So:

\[
u_A=0,
\quad u_B=140,
\quad u_C=180,
\]

\[
v_W=180,
\quad v_X=110,
\quad v_Y=10,
\quad v_Z=-60.
\]

## 8.8 Improvement indices

For unused cells:

\[
I_{ij}=c_{ij}-(u_i+v_j).
\]

\[
I_{AY}=130-(0+10)=120,
\]

\[
I_{AZ}=290-(0+(-60))=350,
\]

\[
I_{BW}=190-(140+180)=-130,
\]

\[
I_{BZ}=280-(140+(-60))=200,
\]

\[
I_{CW}=240-(180+180)=-120,
\]

\[
I_{CX}=270-(180+110)=-20.
\]

The most negative is \(-130\), so \(BW\) is the entering cell.

## 8.9 Stepping-stone method

Entering cell:

\[
BW.
\]

Loop:

\[
BW\rightarrow BX\rightarrow AX\rightarrow AW\rightarrow BW.
\]

Apply:

\[
BW=+\theta,
\quad BX=12-\theta,
\quad AX=3+\theta,
\quad AW=11-\theta.
\]

Choose:

\[
\theta=\min(11,12)=11.
\]

Then:

\[
AW=0,
\quad AX=14,
\quad BW=11,
\quad BX=1.
\]

The exiting cell is \(AW\). It is left blank.

Saving:

\[
11(130)=1430.
\]

Improved cost:

\[
9010-1430=7580.
\]

A further iteration gives final cost:

\[
\boxed{7560}.
\]

Final allocation from the transcript:

- \(W\) gets 11 from \(B\);
- \(X\) gets 14 from \(A\) and 1 from \(C\);
- \(Y\) gets 5 from \(B\) and 9 from \(C\);
- \(Z\) gets 10 from \(C\).

## 8.10 Linear programming formulation

Let:

\[
x_{ij}=\text{number of units transported from source }i\text{ to destination }j.
\]

Objective:

\[
\text{minimise }P=\sum_i\sum_j c_{ij}x_{ij}.
\]

Supply constraints:

\[
\sum_j x_{ij}\le s_i.
\]

Demand constraints:

\[
\sum_i x_{ij}\ge d_j.
\]

Non-negativity:

\[
x_{ij}\ge 0.
\]

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-001 | Source: Screenshot PDF page 1 + teacher transcript | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-001.svg | Purpose: Show the anatomy of a transportation table, including sources, destinations, unit-cost cells, supply/stock column and demand row.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-002 | Source: Screenshot PDF pages 3 to 8 + teacher transcript | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-002.svg | Purpose: Show the north-west corner allocation path using right/down movements only.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-003 | Source: Screenshot PDF pages 11 to 21 + teacher transcript | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-003.svg | Purpose: Explain why a non-degenerate transportation solution should have \(m+n-1\) occupied cells.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-004 | Source: Screenshot PDF pages 24 to 35 + teacher transcript | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-004.svg | Purpose: Compare balanced, excess-supply and excess-demand cases.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-005 | Source: Teacher transcript Transportation Problems 3 | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-005.svg | Purpose: Show how a degenerate solution is repaired by adding a zero allocation.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-006 | Source: Teacher transcript Transportation Problems 4 | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-006.svg | Purpose: Show how shadow costs \(u_i\) and \(v_j\) are fitted around the occupied cost cells.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentSVG-007 | Source: Teacher transcript Transportation Problems 5 | Insert from svg/OffSpecTransportationProblemsEnrichmentSVG-007.svg | Purpose: Show improvement indices for unoccupied cells and identify the entering cell.]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentTikZ-001 | Source: Teacher transcript Transportation Problems 6 | Insert from tikz/OffSpecTransportationProblemsEnrichmentTikZ-001.tex | Purpose: Show the \(\theta\)-loop for introducing entering cell \(BW\).]

[VISUAL PLACEHOLDER: OffSpecTransportationProblemsEnrichmentMermaid-001 | Source: Teacher transcript Transportation Problems 8 | Insert from mermaid/OffSpecTransportationProblemsEnrichmentMermaid-001.md | Purpose: Map a transportation table to decision variables, objective function and constraints.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: OffSpecTransportationProblemsEnrichmentWidget-001 | Source: AI-proposed teaching enhancement based on transcript evidence | Insert from widgets/OffSpecTransportationProblemsEnrichmentWidget-001.html | Purpose: Check whether a transportation problem is balanced and identify the required dummy point.]

[INTERACTIVE PLACEHOLDER: OffSpecTransportationProblemsEnrichmentWidget-002 | Source: AI-proposed teaching enhancement based on transcript evidence | Insert from widgets/OffSpecTransportationProblemsEnrichmentWidget-002.html | Purpose: Let students practise north-west corner allocation step by step.]

[INTERACTIVE PLACEHOLDER: OffSpecTransportationProblemsEnrichmentWidget-003 | Source: AI-proposed teaching enhancement based on transcript evidence | Insert from widgets/OffSpecTransportationProblemsEnrichmentWidget-003.html | Purpose: Check whether an allocation is degenerate.]

[INTERACTIVE PLACEHOLDER: OffSpecTransportationProblemsEnrichmentWidget-004 | Source: AI-proposed teaching enhancement based on transcript evidence | Insert from widgets/OffSpecTransportationProblemsEnrichmentWidget-004.html | Purpose: Practise calculating improvement indices from supplied shadow costs.]

[INTERACTIVE PLACEHOLDER: OffSpecTransportationProblemsEnrichmentWidget-005 | Source: AI-proposed teaching enhancement based on transcript evidence | Insert from widgets/OffSpecTransportationProblemsEnrichmentWidget-005.html | Purpose: Practise choosing \(\theta\) from the decreasing cells in a stepping-stone loop.]

---

# 11. Worked Examples

## Worked Example 1: Interpret a transportation table

Explain the entries 180, 15, 16 and 50 in the main table.

- 180 is the cost per unit from supplier \(A\) to depot \(W\).
- 15 is the demand at depot \(X\).
- 16 is the stock/supply at supplier \(B\).
- 50 is the total demand and total supply in this balanced example.

## Worked Example 2: North-west corner method

The main allocation is:

\[
x_{AW}=11,
\quad x_{AX}=3,
\quad x_{BX}=12,
\quad x_{BY}=4,
\quad x_{CY}=10,
\quad x_{CZ}=10.
\]

Total cost:

\[
11(180)+3(110)+12(250)+4(150)+10(190)+10(120)=9010.
\]

## Worked Example 3: Excess supply

Demands:

\[
50+40+30=120.
\]

Supplies:

\[
40+60+50=150.
\]

Add dummy demand:

\[
150-120=30.
\]

Interpretation: 30 units of supply are left over.

## Worked Example 4: Excess demand

Supplies:

\[
55+70+65=190.
\]

Demands:

\[
74+72+68=214.
\]

Add dummy supply:

\[
214-190=24.
\]

If those 24 are assigned to shop \(C\), shop \(C\) has not had its demand fully met.

## Worked Example 5: Degenerate solution

For \(m=4,n=3\):

\[
m+n-1=4+3-1=6.
\]

If only 5 cells are occupied:

\[
5<6.
\]

The solution is degenerate. Add a zero allocation.

## Worked Example 6: Shadow costs and improvement indices

Setting \(u_A=0\), the shadow costs are:

\[
u_A=0,
\quad u_B=140,
\quad u_C=180,
\quad v_W=180,
\quad v_X=110,
\quad v_Y=10,
\quad v_Z=-60.
\]

Improvement indices include:

\[
I_{BW}=190-(140+180)=-130,
\]

so \(BW\) enters.

## Worked Example 7: Stepping-stone first iteration

Use loop:

\[
BW\rightarrow BX\rightarrow AX\rightarrow AW\rightarrow BW.
\]

\[
\theta=\min(11,12)=11.
\]

New allocation has \(BW=11\), \(AX=14\), \(BX=1\), and \(AW\) exits.

Cost improves to:

\[
7580.
\]

## Worked Example 8: Linear programming formulation

\[
\text{minimise }P=\sum_i\sum_j c_{ij}x_{ij}
\]

subject to supply, demand and non-negativity constraints:

\[
\sum_j x_{ij}\le s_i,
\quad
\sum_i x_{ij}\ge d_j,
\quad
x_{ij}\ge 0.
\]

---

# 12. Common Mistakes and Exam Traps

- Confusing middle cost cells with edge supply/demand totals.
- Moving diagonally in the north-west corner method.
- Forgetting to check whether the problem is balanced.
- Adding dummy supply when dummy demand is needed, or vice versa.
- Forgetting dummy route costs are zero.
- Treating dummy supply as real supply.
- Forgetting the occupied-cell count \(m+n-1\).
- Mixing allocation tables with cost tables.
- Sign errors in \(I_{ij}=c_{ij}-(u_i+v_j)\).
- Choosing the wrong entering cell.
- Choosing \(\theta\) from increasing cells rather than decreasing cells.
- Forgetting to blank the exiting cell.

---

# 13. Practice Questions

1. A table has \(m=2\) sources and \(n=3\) destinations. How many occupied cells should a non-degenerate solution have?
2. Total supply is 85 and total demand is 100. What dummy point is needed?
3. Total supply is 120 and total demand is 95. What dummy point is needed?
4. Find \(I_{ij}\) when \(c_{ij}=42,u_i=15,v_j=31\).
5. Find \(I_{ij}\) when \(c_{ij}=18,u_i=24,v_j=-3\).
6. Explain why \(x_{AR}\ge 0\).
7. Write a supply constraint for supplier \(A\) supplying \(R,S,T\) with total supply 30.
8. Write a demand constraint for destination \(T\) requiring at least 45 units from \(A,B,C\).
9. Use the north-west corner method for a balanced \(3\times3\) table and calculate total cost.
10. Check degeneracy for a \(3\times3\) problem with four occupied cells.
11. Given shadow costs, calculate improvement indices and identify the entering cell.
12. Given decreasing cells \(18-\theta,7-\theta,12-\theta\), find \(\theta\) and the exiting cell.

---

# 14. Worked Solutions

1. \(m+n-1=2+3-1=4\).
2. Demand exceeds supply by \(100-85=15\), so add dummy supply 15.
3. Supply exceeds demand by \(120-95=25\), so add dummy demand 25.
4. \(I_{ij}=42-(15+31)=-4\). Potentially improving.
5. \(I_{ij}=18-(24+(-3))=18-21=-3\). Potentially improving.
6. A transported quantity cannot be negative, so \(x_{AR}\ge0\).
7. \(x_{AR}+x_{AS}+x_{AT}\le30\), or equality if all supply is used.
8. \(x_{AT}+x_{BT}+x_{CT}\ge45\), or equality if exactly met.
9. Follow the north-west corner method: allocate the minimum of remaining row supply and column demand at each active cell, then multiply allocations by route costs and add.
10. For \(m=3,n=3\), required occupied cells \(=3+3-1=5\). Four occupied cells means degenerate; add a zero allocation.
11. Use \(I_{ij}=c_{ij}-(u_i+v_j)\). The most negative value is the entering cell.
12. \(\theta=\min(18,7,12)=7\). The cell with \(7-\theta\) exits.

---

# 15. Exam Technique Notes

1. Check balance before allocating.
2. Keep allocation and cost matrices separate.
3. Show row and column checks.
4. Count occupied cells.
5. Set one shadow cost equal to zero.
6. Calculate improvement indices only for unoccupied cells.
7. Choose the most negative improvement index as the entering cell.
8. Build a valid loop using occupied cells plus the entering cell.
9. Choose \(\theta\) from decreasing cells only.
10. Leave the exiting cell blank.
11. State optimality when all improvement indices are non-negative.
12. In LP formulation, define variables, objective, constraints and non-negativity.

---

# 16. Syllabus Gap Check

| Check | Status |
|---|---|
| CCEA LO coverage | None. This is off-spec enrichment only. |
| Evidence coverage | Transcript evidence covered for major methods. |
| Bridge coverage | Ordinary Maths bridge included and labelled as bridge-only. |
| Off-spec warning | Included throughout. |
| Visual limitation | Screenshot PDF was image-only. |

## Off-Spec Content Found but Excluded from CCEA Core

- North-west corner method.
- Transportation tableaux.
- Shadow costs.
- Improvement indices.
- Stepping-stone method.
- Transportation LP with many variables.

---

# 17. Recommended Enhancements Not in the Evidence

- Animated north-west corner method.
- Degeneracy checker.
- Shadow-cost reveal.
- Improvement-index calculator.
- Theta-loop trainer.
- Comparison with CCEA two-variable simplex tableau to prevent syllabus confusion.

---

# 18. Supplementary Sources Used

Project Sources used for boundary checking and bridge context:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

Lesson-specific evidence:

- `Chapter_1_Transportation_Problems_⌨️_(Decision_2)_screenshots.pdf`
- `transcripts.md`

Evidence boundary statement: this lesson is optional enrichment, not CCEA core.

---

# 19. Final Student Checklist

## Prerequisites

- [ ] I can read a table by rows and columns.
- [ ] I can add row and column totals.
- [ ] I can multiply allocation by cost.
- [ ] I can use \(x_{ij}\ge0\).

## Transportation method

- [ ] I can identify sources and destinations.
- [ ] I can check whether a problem is balanced.
- [ ] I can add the correct dummy point.
- [ ] I can use the north-west corner method.
- [ ] I can calculate total cost.
- [ ] I can check \(m+n-1\).
- [ ] I can repair degeneracy with a zero allocation.

## Improvement method

- [ ] I can find shadow costs.
- [ ] I can find improvement indices.
- [ ] I can identify entering and exiting cells.
- [ ] I can form a stepping-stone loop.
- [ ] I can choose \(\theta\).
- [ ] I can decide when a solution is optimal.

## Off-spec awareness

- [ ] I know this is optional enrichment.
- [ ] I know no CCEA LO ID was found.
- [ ] I know this does not replace the CCEA FA22 simplex-tableau lesson.
