# A21 Algebraic Methods: Proof by Contradiction

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `A21` |
| Unit name | A2 1 Pure Mathematics |
| Topic code | `A21-AF`, inferred anchor |
| Topic name | Algebra and functions, lesson focus: Algebraic Methods, Proof by Contradiction |
| Topic slug | `algebraic_methods_proof_by_contradiction` |
| Topic Pascal | `AlgebraicMethodsProofByContradiction` |
| Topic ID | `A21AlgebraicMethodsProofByContradiction` |
| Lesson file | `A21_algebraic_methods_proof_by_contradiction_lesson.md` |
| Primary specification link | Overarching proof and reasoning theme: proof by contradiction at A level |
| Related LO IDs | `A21-AF-LO001` to `A21-AF-LO009`, preserved as topic anchor IDs but not all taught in this proof-only lesson |
| Tags | `#A21`, `#Proof`, `#Contradiction`, `#Reasoning`, `#RationalIrrational`, `#ExamTechnique` |

---

## Evidence Map

This lesson uses the following evidence sources.

| Evidence source | Role in lesson |
|---|---|
| `CCEA_GCE_Mathematics_Specification_Map copy.md` | Specification authority for unit structure, A21 topic anchor and proof by contradiction as an A-Level proof theme. |
| `README-Module-Map.txt` | Project metadata and file/folder conventions. |
| `Source-Evidence-Drop-Checklist.txt` | Evidence hierarchy, missing evidence log, off-spec log and visual placeholder rules. |
| `Maths-Portal-Build-–-Knowledge-Evidence-(Standard-A‑Level).txt` | Lesson section order and phase expectations. |
| `Chapter_1a_Algebraic_Methods,_Proof_💡_(Pure_Year_2)_Transcript.md` | Teacher explanations, proof structure, worked examples and warnings. |
| `P2-Chp1-AlgebraicMethods_RevealBlocksRemoved 2.pdf` | Slide/text support for proof by contradiction, negation, examples and extension prompts. |
| `Chapter_1a_Algebraic_Methods,_Proof_💡_(Pure_Year_2)_Screenshots.pdf` | Visual support only. The file is image-based and was not used to invent uninspected detail. |

Evidence priority: CCEA specification map first, then project metadata/checklist, then transcript and PDF/slide evidence. Cross-board or third-party evidence is used only where the CCEA boundary confirms the content is on-spec.

---

## Specification Alignment

| Specification / evidence item | Lesson coverage |
|---|---|
| CCEA overarching proof theme: proof by contradiction at A level | Full method taught and practised. |
| Mathematical language and notation | Explicit focus on negation, implication, contradiction wording, variables, integer assumptions and final conclusion. |
| A21-AF algebraic fluency | Used in examples involving parity, integer divisibility, expansion, factorisation and rational forms. |
| `A21-AF-LO001` | Supporting algebraic manipulation only. |
| `A21-AF-LO008` partial fractions | Excluded from this proof-only lesson and reserved for a separate algebraic fractions/partial fractions lesson. |
| Cross-board proof examples | Used only when they match the CCEA A-Level proof boundary. |

### Learning Outcome Register

| LO ID | Status in this lesson | Notes |
|---|---|---|
| Overarching proof theme | Core | Proof by contradiction is the direct lesson target. |
| `A21-AF-LO001` | Supporting only | Algebraic fluency supports contradiction examples. |
| `A21-AF-LO002` | Not targeted | Function definition is not taught in this proof-only lesson. |
| `A21-AF-LO003` | Not targeted | Domain and range are not taught here. |
| `A21-AF-LO004` | Not targeted | Composite functions are not taught here. |
| `A21-AF-LO005` | Not targeted | Inverse functions are not taught here. |
| `A21-AF-LO006` | Not targeted | Modulus function is not taught here. |
| `A21-AF-LO007` | Not targeted | Graph transformations are not taught here. |
| `A21-AF-LO008` | Excluded from core | Partial fractions appear in the wider chapter but are reserved for a separate lesson. |
| `A21-AF-LO009` | Not targeted | Function modelling is not taught here. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain what proof by contradiction is and why it works.
2. Start a contradiction proof by assuming the **negation** of the statement.
3. Negate statements involving “there exists”, “there is no”, “all”, and “if \(A\), then \(B\)”.
4. Use algebra to force a contradiction.
5. Write a final conclusion sentence that clearly restates the original statement.
6. Prove statements involving odd/even integers, integer divisibility, rational and irrational numbers.
7. Recognise which examples are core proof practice and which are enrichment.

---

## Prerequisite Recap, A-Level Evidence Only

No GCSE sources are used. The required prior knowledge is treated as mathematical fluency needed for A-Level Pure.

| Skill | Needed because |
|---|---|
| Even and odd integer forms | Proofs use \(2k\) and \(2k+1\). |
| Expanding brackets | Needed for \((2k+1)^2\) and \((a+4b)^2\). |
| Factorising | Needed to turn expressions into contradiction-friendly form. |
| Fractions and rational numbers | Rational numbers are written as integer fractions. |
| Integer divisibility | Used in examples such as \(25a+15b=1\). |
| Prime factorisation | Used in \(\sqrt2\), \(\log_2 7\), and the infinitely-many-primes proof. |
| Mathematical implication | Needed for conditional statements such as “if \(n^2\) is even, then \(n\) is even”. |

---

## Big Picture Explanation

A direct proof tries to build a statement from the ground up: start with known facts, climb step by step, reach the result.

Proof by contradiction uses a different engine. You temporarily enter the “wrong universe”: assume the statement you want is false. Then you do valid mathematics inside that wrong universe until the walls buckle. If the assumption forces something impossible, the assumption must be false. Therefore the original statement must be true.

The evidence gives this structure:

- Assume the statement is false.
- Prove this would lead to a contradiction.
- Therefore the assumption was wrong, so the statement must be true.

In symbols, if the original statement is \(S\), proof by contradiction assumes \(\neg S\). If \(\neg S\) leads to an impossibility, then \(\neg S\) is false. Therefore \(S\) is true.

---

## Key Definitions and Notation

### Contradiction

A **contradiction** is a result that cannot be true under the assumptions made.

In this lesson, contradictions often look like:

\[
\text{an integer}=\frac15,
\]

or

\[
n^2 \text{ is even and } n^2 \text{ is odd},
\]

or

\[
a \text{ and } b \text{ have no common factor, but both are even}.
\]

### Negation

The **negation** of a statement is the statement that says the original statement is false.

Careful: the negation is not always the casual “opposite”.

| Statement | Correct negation |
|---|---|
| There are infinitely many primes. | There are finitely many primes. |
| All members of a set have property \(P\). | At least one member does not have property \(P\). |
| There is no object with property \(P\). | There exists an object with property \(P\). |
| If \(A\), then \(B\). | \(A\) is true and \(B\) is false. |

### Even integer

An integer \(n\) is even if

\[
n=2k
\]

for some integer \(k\).

### Odd integer

An integer \(n\) is odd if

\[
n=2k+1
\]

for some integer \(k\).

### Rational number

A number is **rational** if it can be written in the form

\[
\frac{a}{b},
\]

where \(a,b\in\mathbb Z\) and \(b\neq0\).

In irrationality proofs, we usually choose \(\frac ab\) in lowest terms, so \(a\) and \(b\) have no common factor greater than \(1\).

Useful set notation:

- \(\mathbb Q\): rational numbers. The letter \(Q\) comes from quotient.
- \(\mathbb R\): real numbers.
- \(\mathbb N\): natural numbers.
- \(\mathbb Z\): integers.

### Irrational number

A number is **irrational** if it cannot be written as

\[
\frac{a}{b},
\]

where \(a,b\in\mathbb Z\) and \(b\neq0\).

Examples from the evidence include:

\[
\pi,\quad e,\quad \sqrt2,\quad \sqrt3.
\]

---

## Core Theory

### The proof-by-contradiction skeleton

For a statement \(S\):

1. Assume, for contradiction, that \(S\) is false.
2. Use valid mathematics to derive something impossible.
3. State the contradiction clearly.
4. Conclude that the assumption was false.
5. Therefore \(S\) is true.

A polished proof can follow this template:

```text
Assume for contradiction that [negation of statement].

[Mathematical reasoning.]

This contradicts [specific assumption/fact].

Therefore [original statement].
```

### Conditional statements

For a statement of the form

\[
\text{If } A,\text{ then } B,
\]

the negation is:

\[
A \text{ is true and } B \text{ is false}.
\]

So for:

\[
\text{If } n^2 \text{ is even, then } n \text{ is even},
\]

the contradiction assumption is:

\[
n^2 \text{ is even and } n \text{ is odd}.
\]

Do **not** negate both parts. The negation is not:

\[
n^2 \text{ is odd and } n \text{ is odd}.
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionSVG-001 | Source: CCEA proof theme + transcript | Insert from svg/A21AlgebraicMethodsProofByContradictionSVG-001.svg | Purpose: Show the proof-by-contradiction logic loop: assume negation, derive contradiction, conclude original statement.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionSVG-002 | Source: Dr Frost negation slide | Insert from svg/A21AlgebraicMethodsProofByContradictionSVG-002.svg | Purpose: Compare common statement types with their correct negations.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionSVG-003 | Source: transcript rational/irrational section | Insert from svg/A21AlgebraicMethodsProofByContradictionSVG-003.svg | Purpose: Show \(\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\) and irrational numbers inside \(\mathbb R\setminus\mathbb Q\).]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionSVG-004 | Source: transcript \(\sqrt2\) proof | Insert from svg/A21AlgebraicMethodsProofByContradictionSVG-004.svg | Purpose: Show the contradiction chain \(\sqrt2=\frac ab \Rightarrow a,b\text{ both even}\).]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionSVG-005 | Source: Euclid primes example | Insert from svg/A21AlgebraicMethodsProofByContradictionSVG-005.svg | Purpose: Show \(N=p_1p_2\cdots p_n+1\) and why division by listed primes leaves remainder \(1\).]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionMermaid-001 | Source: CCEA proof theme + transcript | Insert from mermaid/A21AlgebraicMethodsProofByContradictionMermaid-001.md | Purpose: Text-based proof-by-contradiction logic loop.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsProofByContradictionTikZ-001 | Source: CCEA proof theme + transcript | Insert from tikz/A21AlgebraicMethodsProofByContradictionTikZ-001.tex | Purpose: Printable formal proof-by-contradiction loop.]

[INTERACTIVE PLACEHOLDER: A21AlgebraicMethodsProofByContradictionWidget-001 | Source: proof-by-contradiction structure | Insert from widgets/A21AlgebraicMethodsProofByContradictionWidget-001.html | Purpose: Let students choose the correct negation and build the proof skeleton step by step.]

---

## Worked Examples

### Worked Example 1: Prove that there is no greatest odd integer

**Claim.**

\[
\text{There is no greatest odd integer.}
\]

**Proof by contradiction.**

Assume for contradiction that there **is** a greatest odd integer.

Let this greatest odd integer be \(n\).

Since \(n\) is odd, adding \(2\) gives another odd integer:

\[
n+2.
\]

Also,

\[
n+2>n.
\]

So \(n+2\) is an odd integer greater than \(n\).

This contradicts the assumption that \(n\) was the greatest odd integer.

Therefore, there is no greatest odd integer.

---

### Worked Example 2: If \(n^2\) is even, then \(n\) must be even

**Claim.**

\[
\text{If } n^2 \text{ is even, then } n \text{ is even.}
\]

**Proof by contradiction.**

The statement has the form:

\[
\text{If } A,\text{ then } B.
\]

The contradiction assumption is:

\[
A \text{ is true and } B \text{ is false}.
\]

So assume for contradiction that:

\[
n^2 \text{ is even and } n \text{ is odd}.
\]

Since \(n\) is odd,

\[
n=2k+1
\]

for some integer \(k\).

Now square \(n\):

\[
n^2=(2k+1)^2.
\]

Expand:

\[
n^2=(2k+1)(2k+1).
\]

\[
n^2=4k^2+2k+2k+1.
\]

\[
n^2=4k^2+4k+1.
\]

Factor out \(2\) from the first two terms:

\[
n^2=2(2k^2+2k)+1.
\]

Since \(2k^2+2k\) is an integer,

\[
2(2k^2+2k)+1
\]

is odd.

So \(n^2\) is odd.

But we assumed \(n^2\) is even.

This is a contradiction.

Therefore, if \(n^2\) is even, then \(n\) must be even.

---

### Worked Example 3: No integers \(a,b\) satisfy \(25a+15b=1\)

**Claim.**

There do not exist integers \(a\) and \(b\) such that

\[
25a+15b=1.
\]

**Proof by contradiction.**

Assume for contradiction that there **do** exist integers \(a\) and \(b\) such that

\[
25a+15b=1.
\]

Both terms on the left are multiples of \(5\), so factor out \(5\):

\[
5(5a+3b)=1.
\]

Divide both sides by \(5\):

\[
5a+3b=\frac15.
\]

Since \(a\) and \(b\) are integers,

\[
5a
\]

is an integer, and

\[
3b
\]

is an integer.

Therefore,

\[
5a+3b
\]

is an integer.

But the equation says:

\[
5a+3b=\frac15.
\]

Since \(\frac15\) is not an integer, this is impossible.

This is a contradiction.

Therefore, there do not exist integers \(a\) and \(b\) such that

\[
25a+15b=1.
\]

---

### Worked Example 4: Given rational \(a\) and irrational \(b\), prove that \(a-b\) is irrational

**Claim.**

Given a rational number \(a\) and an irrational number \(b\),

\[
a-b
\]

is irrational.

**Proof by contradiction.**

Assume for contradiction that:

- \(a\) is rational,
- \(b\) is irrational,
- \(a-b\) is rational.

Since \(a\) is rational, write

\[
a=\frac cd,
\]

where \(c,d\in\mathbb Z\) and \(d\neq0\).

Since \(a-b\) is rational, write

\[
a-b=\frac ef,
\]

where \(e,f\in\mathbb Z\) and \(f\neq0\).

Now rearrange

\[
a-b=\frac ef
\]

to make \(b\) the subject.

Subtract \(a\) from both sides:

\[
-b=\frac ef-a.
\]

Multiply by \(-1\):

\[
b=a-\frac ef.
\]

Substitute

\[
a=\frac cd.
\]

\[
b=\frac cd-\frac ef.
\]

Use a common denominator:

\[
b=\frac{cf}{df}-\frac{ed}{fd}.
\]

\[
b=\frac{cf-ed}{df}.
\]

Now \(cf-ed\) is an integer because it is made from products and differences of integers.

Also, \(df\) is an integer and \(df\neq0\).

Therefore,

\[
b=\frac{cf-ed}{df}
\]

is rational.

But this contradicts the assumption that \(b\) is irrational.

Therefore, given rational \(a\) and irrational \(b\), \(a-b\) is irrational.

---

### Worked Example 5: Prove that \(\sqrt2\) is irrational

**Claim.**

\[
\sqrt2
\]

is irrational.

**Proof by contradiction.**

Assume for contradiction that \(\sqrt2\) is rational.

Then

\[
\sqrt2=\frac ab,
\]

where \(a,b\in\mathbb Z\), \(b\neq0\), and \(\frac ab\) is in its simplest form.

This means \(a\) and \(b\) have no common factor greater than \(1\).

Square both sides:

\[
(\sqrt2)^2=\left(\frac ab\right)^2.
\]

\[
2=\frac{a^2}{b^2}.
\]

Multiply both sides by \(b^2\):

\[
2b^2=a^2.
\]

So \(a^2\) is even.

If \(a^2\) is even, then \(a\) is even.

Therefore, for some integer \(k\),

\[
a=2k.
\]

Substitute \(a=2k\) into

\[
2b^2=a^2.
\]

\[
2b^2=(2k)^2.
\]

\[
2b^2=4k^2.
\]

Divide both sides by \(2\):

\[
b^2=2k^2.
\]

So \(b^2\) is even.

If \(b^2\) is even, then \(b\) is even.

So \(a\) is even and \(b\) is even.

Therefore, \(a\) and \(b\) share a common factor of \(2\).

This contradicts the assumption that \(\frac ab\) was in simplest form.

Therefore,

\[
\sqrt2
\]

is irrational.

---

### Worked Example 6: Prove that there are infinitely many prime numbers

**Claim.**

There are infinitely many prime numbers.

**Proof by contradiction.**

Assume for contradiction that there are finitely many prime numbers.

Then we can list all of them:

\[
p_1,p_2,p_3,\ldots,p_n.
\]

Now form the number

\[
N=p_1p_2p_3\cdots p_n+1.
\]

Consider what happens when \(N\) is divided by one of the primes in the list, say \(p_i\).

Since \(p_i\) divides the product

\[
p_1p_2p_3\cdots p_n,
\]

we can write

\[
p_1p_2p_3\cdots p_n = p_i \times M
\]

for some integer \(M\).

Then

\[
N=p_iM+1.
\]

So when \(N\) is divided by \(p_i\), the remainder is \(1\).

Therefore, \(N\) is not divisible by \(p_i\).

This is true for every prime in the list:

\[
p_1,p_2,\ldots,p_n.
\]

So \(N\) is not divisible by any prime in the supposed complete list.

Now either:

1. \(N\) is prime, in which case there is a prime not in the list, or
2. \(N\) is composite, in which case its prime factorisation contains a prime not in the list.

Either way, the list

\[
p_1,p_2,\ldots,p_n
\]

was not complete.

This contradicts the assumption that there were finitely many prime numbers.

Therefore, there are infinitely many prime numbers.

---

### Worked Example 7: No integers \(x,y\) satisfy \(15x+20y=1\)

**Claim.**

There do not exist integers \(x\) and \(y\) such that

\[
15x+20y=1.
\]

**Proof by contradiction.**

Assume for contradiction that there do exist integers \(x\) and \(y\) such that

\[
15x+20y=1.
\]

Factor out \(5\):

\[
5(3x+4y)=1.
\]

Divide by \(5\):

\[
3x+4y=\frac15.
\]

Since \(x,y\in\mathbb Z\),

\[
3x\in\mathbb Z
\]

and

\[
4y\in\mathbb Z.
\]

Therefore,

\[
3x+4y\in\mathbb Z.
\]

But

\[
3x+4y=\frac15,
\]

and

\[
\frac15\notin\mathbb Z.
\]

This is a contradiction.

Therefore, there do not exist integers \(x\) and \(y\) such that

\[
15x+20y=1.
\]

---

### Worked Example 8: No positive integers \(a,b\), with \(a\) odd, satisfy \(a+4b=4\sqrt{ab}\)

**Claim.**

There are no positive integers \(a\) and \(b\), with \(a\) odd, such that

\[
a+4b=4\sqrt{ab}.
\]

**Proof by contradiction.**

Assume for contradiction that there are positive integers \(a\) and \(b\), with \(a\) odd, such that

\[
a+4b=4\sqrt{ab}.
\]

Square both sides:

\[
(a+4b)^2=(4\sqrt{ab})^2.
\]

Expand the left-hand side:

\[
(a+4b)^2=a^2+2(a)(4b)+(4b)^2.
\]

\[
(a+4b)^2=a^2+8ab+16b^2.
\]

Square the right-hand side:

\[
(4\sqrt{ab})^2=16ab.
\]

So

\[
a^2+8ab+16b^2=16ab.
\]

Bring all terms to one side:

\[
a^2+8ab+16b^2-16ab=0.
\]

\[
a^2-8ab+16b^2=0.
\]

Factorise:

\[
(a-4b)^2=0.
\]

Therefore,

\[
a-4b=0.
\]

So

\[
a=4b.
\]

But

\[
4b=2(2b),
\]

so \(a\) is even.

This contradicts the assumption that \(a\) is odd.

Therefore, there are no positive integers \(a\) and \(b\), with \(a\) odd, such that

\[
a+4b=4\sqrt{ab}.
\]

---

### Worked Example 9: Prove that \(\log_2 7\) is irrational

**Claim.**

\[
\log_2 7
\]

is irrational.

**Proof by contradiction.**

Assume for contradiction that

\[
\log_2 7
\]

is rational.

Then

\[
\log_2 7=\frac ab,
\]

where \(a,b\in\mathbb Z\), \(b\neq0\), and \(\frac ab\) is in simplest form.

Since

\[
\log_2 7=\frac ab,
\]

rewrite in exponential form:

\[
2^{a/b}=7.
\]

Raise both sides to the power \(b\):

\[
\left(2^{a/b}\right)^b=7^b.
\]

Use the index law:

\[
2^a=7^b.
\]

Now \(2^a\) has only prime factor \(2\), while \(7^b\) has only prime factor \(7\).

By uniqueness of prime factorisation, this is impossible for positive integer powers.

Equivalently, since \(\log_2 7>0\), we may take \(a\) and \(b\) to have the same sign and use \(b>0\). Then \(a>0\), so

\[
2^a
\]

is even, while

\[
7^b
\]

is odd.

An even number cannot equal an odd number.

This is a contradiction.

Therefore,

\[
\log_2 7
\]

is irrational.

This is treated as enrichment/supporting proof, not a separate numbered CCEA learning outcome.

---

## Guided Practice

Try these without looking at the solutions first.

### Practice 1: Negations

Write the negation of each statement.

1. There is no greatest even integer.
2. Every integer is rational.
3. If \(m^2\) is odd, then \(m\) is odd.
4. There are infinitely many multiples of \(3\).
5. \(x\) is rational and \(y\) is irrational.

### Practice 2: No greatest even integer

Prove by contradiction that there is no greatest even integer.

### Practice 3: If \(m^2\) is odd, then \(m\) is odd

Prove by contradiction that if \(m^2\) is odd, then \(m\) is odd.

### Practice 4: No integer solutions to \(14p+21q=1\)

Prove by contradiction that there do not exist integers \(p\) and \(q\) such that

\[
14p+21q=1.
\]

### Practice 5: Rational plus irrational is irrational

Let \(r\) be rational and \(s\) be irrational. Prove by contradiction that

\[
r+s
\]

is irrational.

### Practice 6: \(\sqrt3\) is irrational

Prove by contradiction that

\[
\sqrt3
\]

is irrational.

---

## Common Mistakes and Exam Traps

### Mistake 1: Negating “all” as “none”

Wrong:

\[
\text{All integers have property }P
\]

negates to

\[
\text{No integers have property }P.
\]

Correct:

\[
\text{At least one integer does not have property }P.
\]

### Mistake 2: Negating “if \(A\), then \(B\)” incorrectly

Wrong:

\[
\text{If } A,\text{ then } B
\]

negates to

\[
\text{not }A \text{ and not }B.
\]

Correct:

\[
A \text{ and not } B.
\]

### Mistake 3: Not saying “for contradiction”

The phrase “Assume for contradiction...” is not magic, but it helps the examiner see your plan. It makes clear that the next assumption is intentionally false-looking.

### Mistake 4: Trying examples instead of proving all cases

For integer nonexistence proofs, testing a few values does not prove the result. A proof must cover every integer, not just some integers.

### Mistake 5: Writing an irrational number as a fraction

You cannot say

\[
b=\frac mn
\]

if \(b\) is irrational.

Instead, write the rational quantities as fractions and rearrange until the irrational number is forced to be rational.

### Mistake 6: Forgetting the final conclusion sentence

A contradiction proof is not finished when the contradiction appears. You must say what it proves.

Write:

```text
This contradicts the assumption that ...
Therefore [original statement].
```

---

## Exam Technique Notes

### The four-line exam skeleton

Use this whenever you feel the proof fog rolling in:

1. **Assume for contradiction that...**
2. **Then...** followed by algebra.
3. **This contradicts...**
4. **Therefore...** original statement.

### How to choose the “do some maths” step

| Evidence pattern | Useful move |
|---|---|
| Odd/even integer | Write \(2k\) or \(2k+1\). |
| Square root | Square both sides. |
| Rational number | Write \(\frac ab\), usually in lowest terms. |
| Integer equation with common factor | Factor or divide by the common factor. |
| Logarithm | Rewrite in exponential form. |
| Finite list of primes | Multiply all listed primes and add \(1\). |

### Make the contradiction explicit

Do not just write:

\[
\text{Contradiction.}
\]

Write what contradicted what:

\[
\text{This contradicts the assumption that } n^2 \text{ is even.}
\]

or

\[
\text{This contradicts that } \frac ab \text{ was in simplest form.}
\]

---

## Full Worked Solutions to Guided Practice

### Solution 1: Negations

1. Statement: There is no greatest even integer.  
   Negation: There exists a greatest even integer.

2. Statement: Every integer is rational.  
   Negation: There exists at least one integer that is not rational.

3. Statement: If \(m^2\) is odd, then \(m\) is odd.  
   Negation:

\[
m^2 \text{ is odd and } m \text{ is not odd}.
\]

Since an integer that is not odd is even, this becomes:

\[
m^2 \text{ is odd and } m \text{ is even}.
\]

4. Statement: There are infinitely many multiples of \(3\).  
   Negation: There are finitely many multiples of \(3\).

5. Statement: \(x\) is rational and \(y\) is irrational.  
   Negation:

\[
x \text{ is irrational or } y \text{ is rational}.
\]

### Solution 2: No greatest even integer

Assume for contradiction that there is a greatest even integer. Let this greatest even integer be \(n\). Since \(n\) is even, \(n+2\) is also even. Also, \(n+2>n\). This contradicts the assumption that \(n\) is the greatest even integer. Therefore, there is no greatest even integer.

### Solution 3: If \(m^2\) is odd, then \(m\) is odd

Assume for contradiction that \(m^2\) is odd and \(m\) is even. Since \(m\) is even,

\[
m=2k
\]

for some integer \(k\). Squaring gives

\[
m^2=(2k)^2=4k^2=2(2k^2).
\]

Since \(2k^2\) is an integer, \(m^2\) is even. This contradicts the assumption that \(m^2\) is odd. Therefore, if \(m^2\) is odd, then \(m\) is odd.

### Solution 4: No integer solutions to \(14p+21q=1\)

Assume for contradiction that there exist integers \(p\) and \(q\) such that

\[
14p+21q=1.
\]

Factor out \(7\):

\[
7(2p+3q)=1.
\]

Divide by \(7\):

\[
2p+3q=\frac17.
\]

Since \(p,q\in\mathbb Z\), \(2p+3q\in\mathbb Z\). But \(\frac17\notin\mathbb Z\). This is a contradiction. Therefore, there do not exist integers \(p\) and \(q\) such that \(14p+21q=1\).

### Solution 5: Rational plus irrational is irrational

Assume for contradiction that \(r\) is rational, \(s\) is irrational, and \(r+s\) is rational.

Since \(r\) is rational,

\[
r=\frac ab,
\]

where \(a,b\in\mathbb Z\) and \(b\neq0\).

Since \(r+s\) is rational,

\[
r+s=\frac cd,
\]

where \(c,d\in\mathbb Z\) and \(d\neq0\).

Rearrange to make \(s\) the subject:

\[
s=\frac cd-r.
\]

Substitute \(r=\frac ab\):

\[
s=\frac cd-\frac ab.
\]

Use a common denominator:

\[
s=\frac{bc}{bd}-\frac{ad}{bd}.
\]

\[
s=\frac{bc-ad}{bd}.
\]

Now \(bc-ad\in\mathbb Z\), and \(bd\in\mathbb Z\), with \(bd\neq0\). Therefore \(s\) is rational. This contradicts the assumption that \(s\) is irrational. Therefore \(r+s\) is irrational.

### Solution 6: \(\sqrt3\) is irrational

Assume for contradiction that \(\sqrt3\) is rational. Then

\[
\sqrt3=\frac ab,
\]

where \(a,b\in\mathbb Z\), \(b\neq0\), and \(\frac ab\) is in simplest form.

Square both sides:

\[
3=\frac{a^2}{b^2}.
\]

Multiply both sides by \(b^2\):

\[
3b^2=a^2.
\]

So \(a^2\) is divisible by \(3\). Therefore \(a\) is divisible by \(3\). Let

\[
a=3k
\]

for some integer \(k\).

Substitute into \(3b^2=a^2\):

\[
3b^2=(3k)^2.
\]

\[
3b^2=9k^2.
\]

Divide both sides by \(3\):

\[
b^2=3k^2.
\]

So \(b^2\) is divisible by \(3\). Therefore \(b\) is divisible by \(3\). So \(a\) and \(b\) are both divisible by \(3\). This contradicts the assumption that \(\frac ab\) is in simplest form. Therefore \(\sqrt3\) is irrational.

---

## Common CCEA-Style Wording

```text
Assume for contradiction that...
```

```text
This contradicts the assumption that...
```

```text
Therefore our assumption was false.
```

```text
Hence [restate the original statement].
```

For conditional statements:

```text
Assume for contradiction that [condition is true] but [conclusion is false].
```

For rational/irrational proofs:

```text
Let [rational expression] = a/b, where a,b are integers, b ≠ 0, and the fraction is in its simplest form.
```

For integer divisibility proofs:

```text
Since x and y are integers, [integer combination] is an integer, but the equation implies it equals a non-integer. This is a contradiction.
```

---

## Syllabus Gap Check

| Item | Covered? | Notes |
|---|---|---|
| Proof by contradiction | Yes | Direct core lesson target. |
| Negation of statements | Yes | Includes “all”, “there exists”, “there is no”, conditional statements. |
| Rational and irrational number definitions | Yes | Used in proofs. |
| Standard \(\sqrt2\) irrationality proof | Yes | Full worked proof included. |
| Integer divisibility contradiction | Yes | \(25a+15b=1\), \(15x+20y=1\), \(14p+21q=1\). |
| Euclid infinitely many primes proof | Yes, enrichment-weighted | Included as proof practice, not a separate numbered CCEA LO. |
| A21-AF partial fractions | No | Excluded, belongs to separate lesson. |
| A21-AF full algebraic fractions chapter | No | Excluded from this proof-only lesson. |
| Official CCEA mark schemes | No | Not supplied; no mark allocations invented. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose | File |
|---|---|---|---|
| `A21AlgebraicMethodsProofByContradictionMermaid-001` | Mermaid | Proof-by-contradiction logic loop | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-001.md` |
| `A21AlgebraicMethodsProofByContradictionMermaid-002` | Mermaid | Statement negation map | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-002.md` |
| `A21AlgebraicMethodsProofByContradictionMermaid-003` | Mermaid | Conditional statement proof flow | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-003.md` |
| `A21AlgebraicMethodsProofByContradictionMermaid-004` | Mermaid | Rational/irrational proof strategy | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-004.md` |
| `A21AlgebraicMethodsProofByContradictionMermaid-005` | Mermaid | \(\sqrt2\) contradiction chain | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-005.md` |
| `A21AlgebraicMethodsProofByContradictionMermaid-006` | Mermaid | Euclid prime proof flow | `mermaid/A21AlgebraicMethodsProofByContradictionMermaid-006.md` |
| `A21AlgebraicMethodsProofByContradictionSVG-001` | SVG | Core proof-by-contradiction loop | `svg/A21AlgebraicMethodsProofByContradictionSVG-001.svg` |
| `A21AlgebraicMethodsProofByContradictionSVG-002` | SVG | Correct negation map | `svg/A21AlgebraicMethodsProofByContradictionSVG-002.svg` |
| `A21AlgebraicMethodsProofByContradictionSVG-003` | SVG | Number sets for rational/irrational proofs | `svg/A21AlgebraicMethodsProofByContradictionSVG-003.svg` |
| `A21AlgebraicMethodsProofByContradictionSVG-004` | SVG | \(\sqrt2\) proof chain | `svg/A21AlgebraicMethodsProofByContradictionSVG-004.svg` |
| `A21AlgebraicMethodsProofByContradictionSVG-005` | SVG | Euclid prime proof flow | `svg/A21AlgebraicMethodsProofByContradictionSVG-005.svg` |
| `A21AlgebraicMethodsProofByContradictionTikZ-001` | TikZ | Formal contradiction-proof loop | `tikz/A21AlgebraicMethodsProofByContradictionTikZ-001.tex` |
| `A21AlgebraicMethodsProofByContradictionTikZ-002` | TikZ | Negation map | `tikz/A21AlgebraicMethodsProofByContradictionTikZ-002.tex` |
| `A21AlgebraicMethodsProofByContradictionTikZ-003` | TikZ | \(\sqrt2\) proof chain | `tikz/A21AlgebraicMethodsProofByContradictionTikZ-003.tex` |
| `A21AlgebraicMethodsProofByContradictionTikZ-004` | TikZ | Euclid proof flow | `tikz/A21AlgebraicMethodsProofByContradictionTikZ-004.tex` |
| `A21AlgebraicMethodsProofByContradictionTikZ-005` | TikZ | Rational/irrational proof strategy | `tikz/A21AlgebraicMethodsProofByContradictionTikZ-005.tex` |
| `A21AlgebraicMethodsProofByContradictionWidget-001` | HTML widget | Negation quiz, proof builder and \(\sqrt2\) chain trainer | `widgets/A21AlgebraicMethodsProofByContradictionWidget-001.html` |

---

## Supplementary Sources Used

No web sources were used.

The Dr Frost/Pearson-style PDF and transcript are cross-board or third-party A-Level sources. They are used only because the supplied CCEA specification map confirms proof by contradiction as an A-Level proof requirement. Board-specific branding, STEP/MAT/UKMT extension content, algebraic fractions and partial fractions are not treated as CCEA core for this proof-only lesson.

---

## Final Student Checklist

Before leaving this lesson, check that you can do each item without peeking:

| Skill | Can I do it? |
|---|---|
| I can explain proof by contradiction in one sentence. | |
| I can write “Assume for contradiction that...” correctly. | |
| I can negate “there is no...” statements. | |
| I can negate “if \(A\), then \(B\)” statements. | |
| I can prove there is no greatest odd or even integer. | |
| I can prove “if \(n^2\) is even, then \(n\) is even”. | |
| I can use integer divisibility to create a contradiction. | |
| I can write rational numbers as \(\frac ab\) with \(a,b\in\mathbb Z\), \(b\neq0\). | |
| I can explain why irrational numbers should not be written as fractions. | |
| I can prove \(\sqrt2\) is irrational. | |
| I can state the contradiction clearly. | |
| I can finish with a full conclusion sentence. | |

---

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix correct | Yes, `A21` |
| Unit name correct | Yes, A2 1 Pure Mathematics |
| Topic identity complete | Yes, with caveat that proof by contradiction is an overarching proof theme rather than a numbered A21-AF LO |
| LO IDs preserved exactly | Yes, A21-AF IDs preserved where used |
| On-spec evidence covered | Yes, proof by contradiction is the core lesson target |
| Off-spec material excluded or marked | Yes |
| Cross-board evidence controlled | Yes |
| Missing evidence logged | Yes |
| Visual placeholders match generated files | Yes |
| Unresolved issues | None found, except that official CCEA proof mark schemes were not supplied, so no mark allocations are claimed. |
