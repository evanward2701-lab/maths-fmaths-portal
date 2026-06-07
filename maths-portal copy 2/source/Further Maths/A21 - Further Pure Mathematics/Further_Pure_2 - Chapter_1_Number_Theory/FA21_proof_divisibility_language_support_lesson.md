# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA21`: Further A2 1 Pure Mathematics |
| Applied section | Not applicable: Pure Mathematics |
| Official CCEA topic code | `FA21-PROOF` |
| Official CCEA topic name | Proof |
| Boundary-safe lesson title | Proof: Divisibility Language Support for Induction |
| Topic slug | `proof_divisibility_language_support` |
| Topic Pascal | `ProofDivisibilityLanguageSupport` |
| Topic ID | `FA21ProofDivisibilityLanguageSupport` |
| Lesson file | `FA21_proof_divisibility_language_support_lesson.md` |
| Core LO IDs | `FA21-PROOF-LO001` |
| Related split-topic LO IDs | `FAS2-PROB-LO001`, `FAS2-PROB-LO002`, `FAS2-PROB-LO003`, `FAS2-PROB-LO004`, `FA22-GENFUNC-LO003` |
| Bridge tags | `#Bridge`, `#GCSEFactors`, `#OrdinaryMathsProof`, `#Algebra`, `#CountingSeparated` |
| Topic tags | `#FA21`, `#PROOF`, `#Proof`, `#Induction`, `#DivisibilityLanguage`, `#ExamTechnique` |
| Evidence boundary warning | The uploaded FP2 Number Theory chapter is not treated as a CCEA core Number Theory topic because no official CCEA Number Theory topic code or LO ID was found in the supplied CCEA Further Mathematics specification map. |

> **Boundary statement for students:**  
> This lesson is not claiming that FP2 Number Theory is a standalone CCEA Further Mathematics topic. The CCEA core target here is proof, especially induction. Divisibility language from the uploaded Number Theory evidence is used only where it helps you read and write divisibility proof statements cleanly.

# 2. Evidence Map

| Evidence category | Source used | Details preserved | Use in this lesson |
|---|---|---|---|
| CCEA Further Maths specification | CCEA GCE Further Mathematics Specification Map | `FA21-PROOF-LO001`: construct proofs using mathematical induction; elaboration includes divisibility contexts | Core syllabus authority |
| Project module map | Further Maths README module map | Unit codes, topic metadata rules, phase workflow and file naming conventions | Workflow authority |
| Project evidence checklist | Further Maths Evidence Drop Checklist | Missing evidence log, visual evidence rules, off-spec handling | Quality control |
| Lesson transcript | `transcripts.md` | Number Theory chapter overview; notation \(a\mid b\), \(a\nmid b\), \(\gcd(a,b)\); divisor/coprime language; division algorithm; Euclidean algorithm; modular arithmetic; divisibility tests; congruences; Fermat; combinatorics | Mostly enrichment. Divisibility notation and language used as support for proof literacy only. |
| Screenshot PDF | `Chapter_1_Number_Theory_♾️_(Further_Pure_2)_screenshots.pdf` | Page 1 chapter overview; pages 5 to 6 notation table; pages 16 to 21 divisor examples and proof; pages 22 to 30 division algorithm examples | Visual evidence for support/enrichment, not CCEA core |
| Ordinary A-Level bridge | Ordinary A-Level Maths Bridge Spec Extracts | Algebraic proof, factorisation, sequences, proof language, counting | Bridge context only |
| Cross-board / non-CCEA evidence | FP2 chapter label in transcript and screenshots | Treated as non-CCEA evidence because “FP2 Number Theory” is not a CCEA unit/topic code in this project | Off-spec unless used as language support |

# 3. Specification Alignment

## 3.1 Core CCEA Alignment

| CCEA LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA21-PROOF-LO001` | construct proofs using mathematical induction | This lesson prepares the divisibility notation and proof language needed for induction-style divisibility questions. It does not replace the induction method. | CCEA Further Maths Specification Map; transcript support for divisor notation | Core method must be mathematical induction. Direct divisibility proofs, Euclidean algorithm and modular arithmetic are not treated as the required CCEA method. | AS1/A21 algebraic proof, sequence notation, factorisation, general \(n\)-statements |

## 3.2 Evidence Items Not Mapped to Core CCEA LO

| Evidence item | Why not core in this lesson | Future handling |
|---|---|---|
| Division algorithm | No matching supplied CCEA LO in FA21-PROOF | Optional enrichment only |
| Euclidean algorithm | No matching supplied CCEA LO in FA21-PROOF | Optional enrichment only |
| Reverse Euclidean algorithm / Bézout identity | No matching supplied CCEA LO in FA21-PROOF | Optional enrichment only |
| Modular arithmetic | No matching supplied CCEA LO in FA21-PROOF | Optional enrichment only |
| Linear congruence equations | No matching supplied CCEA LO in FA21-PROOF | Optional enrichment only |
| Fermat’s little theorem | No matching supplied CCEA LO in supplied CCEA map | Optional enrichment only |
| Combinatorics | CCEA has related counting outcomes, but in FAS2 Probability and FA22 Generating Functions, not this FA21 proof lesson | Split into a future FAS2 or FA22 lesson |

# 4. Learning Objectives

## 4.1 Core Further Maths Objectives

By the end of the CCEA-core part of this lesson, the student should be able to:

1. Recognise that `FA21-PROOF-LO001` requires **mathematical induction**.
2. Read divisibility notation such as \(a\mid b\) as “\(a\) divides \(b\)”.
3. Translate \(a\mid b\) into \(b=ka,\;k\in\mathbb Z\).
4. Use divisibility language correctly when preparing induction proofs.
5. Distinguish between checking examples and proving a statement for all permitted integers.
6. Write final proof conclusions in complete mathematical sentences.

## 4.2 Bridge Objectives

The student should be able to connect ordinary Maths ideas to Further Maths proof language:

1. Replace “factor of” with “divisor of” where formal notation is needed.
2. Replace “highest common factor” with “greatest common divisor” where the evidence uses gcd language.
3. Recognise that ordinary factorisation still matters, but proof requires a general argument.
4. Understand why a single numerical example does not prove a universal statement.

## 4.3 Exam Technique Objectives

The student should be able to:

1. Preserve integer conditions such as \(a,b,c,m,n\in\mathbb Z\).
2. State the base case, inductive hypothesis and inductive step when the CCEA question asks for induction.
3. Avoid presenting Euclidean algorithm or modular arithmetic as a substitute for induction unless the question explicitly gives that route.
4. Mark off-spec enrichment methods as extra, not required CCEA core.

# 5. Explicit Prerequisite Recap

## 5.1 GCSE Foundations

| GCSE idea | Meaning | Example | Why it matters here |
|---|---|---|---|
| Factor | A number that divides another number exactly | \(3\) is a factor of \(12\) | Further Maths often replaces this with the word **divisor**. |
| Multiple | A number obtained by multiplying by an integer | \(12\) is a multiple of \(3\) | Divisibility proofs are usually written by showing something is a multiple of the divisor. |
| Highest common factor | The largest positive factor shared by two integers | HCF of \(15\) and \(25\) is \(5\) | The uploaded FP2 evidence uses **greatest common divisor**, written \(\gcd(a,b)\). |
| Prime number | A positive integer greater than \(1\) with exactly two positive factors | \(11\) | Coprime numbers and gcd notation depend on understanding factors. |
| Even / odd | Integers of the form \(2k\) or \(2k+1\) | \(8=2(4)\), \(9=2(4)+1\) | Induction divisibility proofs often need this kind of structural rewriting. |

## 5.2 Ordinary AS/A2 Mathematics Foundations

| Ordinary A-Level skill | Example | How it appears in this lesson |
|---|---|---|
| Factorising common factors | \(6n+9=3(2n+3)\) | To prove \(3\mid 6n+9\), show \(6n+9\) is \(3\) times an integer. |
| Substitution | If \(b=ka\), replace \(b\) in an expression | Used in direct divisibility proofs. |
| Expanding brackets | \((k+1)^2=k^2+2k+1\) | Used in induction steps. |
| Rearranging expressions | \(P(k+1)-P(k)\) | Used to connect the \(k\)-case to the \(k+1\)-case. |
| Quantifiers | “For all \(n\in\mathbb N\)” | Proof must cover every allowed integer, not just examples. |

## 5.3 Previous Further Mathematics Foundations

This lesson assumes the student is beginning `FA21-PROOF`, so no previous FA21 proof chapter is assumed. However, it helps if the student has already met formal notation such as \(\in\), \(\mathbb Z\), \(\mathbb N\), exact algebra and mathematical structure.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| GCSE factors and multiples | A factor divides a number exactly. HCF means highest common factor. | The uploaded FP2 evidence uses **divisor**, **divides**, **does not divide**, **greatest common divisor** and **coprime**. | Do not write vague sentences such as “it goes into it”. Use \(a\mid b\), \(a\nmid b\), or \(\gcd(a,b)\) when formal notation is needed. |
| Ordinary AS algebra | Factorisation shows structure, for example \(6n+9=3(2n+3)\). | Further Maths proof turns this into a divisibility argument: since \(2n+3\in\mathbb Z\), \(3\mid 6n+9\). | Pulling out a factor is not enough unless you also say the remaining bracket is an integer. |
| Ordinary proof by algebra | You may have proved identities or shown expressions are positive. | CCEA `FA21-PROOF-LO001` requires mathematical induction. Direct proof language helps, but induction is the official method. | Do not answer an induction question using only pattern spotting or numerical examples. |
| Ordinary sequences | You worked with \(u_n\), \(S_n\), and statements involving \(n\). | Induction proves a statement \(P(n)\) for all allowed \(n\), often \(n\in\mathbb N\). | Do not assume the pattern continues just because it works for \(n=1,2,3\). |
| Ordinary counting and binomial coefficients | You may have met \({}^nC_r\), factorials and binomial coefficients. | These appear in separate CCEA Further Maths topics, especially FAS2 Probability and FA22 Generating Functions. | Do not merge the transcript’s combinatorics section into this FA21 proof lesson. |

In ordinary A-Level Maths, this idea appeared as factorising, simplifying, checking cases and proving identities.  
In Further Maths, the same idea becomes a more formal proof machine: define the statement, state the integer conditions, prove the base case, assume the \(k\)-case, and prove the \(k+1\)-case.  
The key upgrade is that “this works for the examples I tried” becomes “this must work for every allowed value”.  
The danger is that ordinary language can sound convincing while still not being a proof.

# 6. Big Picture Explanation

## 6.1 Why this topic exists

The official CCEA topic here is **Proof**, not Number Theory as a standalone topic. The core learning outcome is:

\[
\texttt{FA21-PROOF-LO001: construct proofs using mathematical induction.}
\]

Mathematical induction is a method for proving infinitely many statements in one finite argument. It is most often used when the statement depends on a positive integer \(n\), for example:

\[
P(n):\quad 3\mid (4^n-1).
\]

## 6.2 What problem it solves

Suppose you are asked to prove:

\[
7\mid (8^n-1)\quad \text{for all } n\in\mathbb N.
\]

Trying examples gives:

\[
8^1-1=7,
\]

\[
8^2-1=64-1=63=7(9),
\]

\[
8^3-1=512-1=511=7(73).
\]

These examples are comforting, but they do not prove the statement for all \(n\). There are infinitely many positive integers. Induction gives a route:

1. Prove the first case.
2. Assume the result is true for \(n=k\).
3. Use that assumption to prove the result for \(n=k+1\).
4. Conclude that the result is true for all required \(n\).

## 6.3 How it extends ordinary Maths

Ordinary Maths asks questions such as:

\[
\text{Is } 3 \text{ a factor of } 12?
\]

Further Maths proof language turns this into:

\[
3\mid 12.
\]

Then proof work turns it into a statement about integer multiples:

\[
12=4(3),\qquad 4\in\mathbb Z.
\]

So the real proof upgrade is:

\[
a\mid b
\quad\Longleftrightarrow\quad
b=ka\text{ for some }k\in\mathbb Z.
\]

## 6.4 What the student should be watching for

| Wording | Translation |
|---|---|
| “\(a\) divides \(b\)” | \(a\mid b\) |
| “\(a\) does not divide \(b\)” | \(a\nmid b\) |
| “\(b\) is divisible by \(a\)” | \(a\mid b\) |
| “\(b\) is a multiple of \(a\)” | \(b=ka\), where \(k\in\mathbb Z\) |
| “prove for all \(n\)” | You likely need a general proof, often induction in FA21 |
| “prove by induction” | You must use the induction structure |

## 6.5 Boundary Warning: Number Theory Evidence

The uploaded FP2 chapter includes the division algorithm, Euclidean algorithm, reverse Euclidean algorithm, modular arithmetic, divisibility tests, congruence equations, Fermat’s little theorem and combinatorics. These are valuable enrichment topics, and parts of the language are helpful for proof. However, they are not treated here as CCEA core unless they directly support `FA21-PROOF-LO001`.

# 7. Key Definitions and Notation

## 7.1 Sets of numbers

| Symbol | Meaning | Example |
|---|---|---|
| \(\mathbb Z\) | the integers | \(\ldots,-3,-2,-1,0,1,2,3,\ldots\) |
| \(\mathbb N\) | the natural numbers | Often \(1,2,3,\ldots\), unless a source states otherwise |
| \(a\in\mathbb Z\) | \(a\) is an integer | \(5\in\mathbb Z\), \(-2\in\mathbb Z\) |
| \(n\in\mathbb N\) | \(n\) is a natural number | Used in induction statements |

> **Notation warning:** Always check the starting value in an induction question. Some courses define \(\mathbb N\) as \(1,2,3,\ldots\), while some include \(0\). In an exam, the question usually tells you the starting value clearly.

## 7.2 Divisor notation

| Previous language | New language | New notation | Example |
|---|---|---|---|
| \(a\) is a factor of \(b\) | \(a\) divides \(b\) | \(a\mid b\) | \(3\mid 12\) |
| \(a\) is not a factor of \(b\) | \(a\) does not divide \(b\) | \(a\nmid b\) | \(5\nmid 12\) |
| common factor of \(a\) and \(b\) | common divisor of \(a\) and \(b\) | \(c\mid a\) and \(c\mid b\) | \(3\mid 12\) and \(3\mid 15\) |
| highest common factor of \(a\) and \(b\) | greatest common divisor of \(a\) and \(b\) | \(\gcd(a,b)\) | \(\gcd(15,25)=5\) |
| HCF of \(a\) and \(b\) is \(1\) | \(a\) and \(b\) are coprime or relatively prime | \(\gcd(a,b)=1\) | \(\gcd(10,21)=1\) |

## 7.3 The definition of \(a\mid b\)

Let \(a,b\in\mathbb Z\), with \(a\neq 0\). Then

\[
a\mid b
\]

means:

\[
b=ka\quad\text{for some }k\in\mathbb Z.
\]

Read this as:

\[
a\text{ divides }b
\quad\Longleftrightarrow\quad
b\text{ is an integer multiple of }a.
\]

### Example 1

\[
11\mid 143
\]

because

\[
143=13(11),
\]

and \(13\in\mathbb Z\).

### Example 2

\[
-4\mid 28
\]

because

\[
28=(-7)(-4),
\]

and \(-7\in\mathbb Z\). This preserves the uploaded evidence’s important upgrade: negative integers can also be divisors in this formal setting.

### Example 3

\[
15\nmid 47
\]

because

\[
47=3(15)+2.
\]

The remainder \(2\) blocks divisibility.

### Example 4

\[
16\mid 0
\]

because

\[
0=0(16),
\]

and \(0\in\mathbb Z\). More generally, for any non-zero integer \(a\), \(a\mid 0\).

## 7.4 Important caveat about zero

The notation \(a\mid b\) is normally used with \(a\neq 0\), because division by zero is not allowed.

- \(16\mid 0\) is true, since \(0=0(16)\).
- \(0\mid 16\) is false, because there is no integer \(k\) such that \(16=k(0)\).
- \(0\mid 0\) is usually avoided in school-level divisibility notation because the divisor \(0\) is not allowed.

So the safe CCEA-proof definition is:

\[
a\mid b
\quad\text{means}\quad
b=ka\text{ for some }k\in\mathbb Z,\quad a\neq 0.
\]

## 7.5 Greatest common divisor

The greatest common divisor of \(a\) and \(b\), written \(\gcd(a,b)\), is the greatest positive integer that divides both \(a\) and \(b\). For example:

\[
\gcd(15,25)=5.
\]

This means \(5\mid 15\) and \(5\mid 25\), and no positive integer greater than \(5\) divides both \(15\) and \(25\).

## 7.6 Coprime or relatively prime

Integers \(a\) and \(b\) are **coprime** or **relatively prime** if

\[
\gcd(a,b)=1.
\]

For example, \(\gcd(10,21)=1\), so \(10\) and \(21\) are coprime.

## 7.7 Induction notation

A statement depending on \(n\) is often written as \(P(n)\). For example:

\[
P(n):\quad 7\mid (8^n-1).
\]

The induction proof usually has this skeleton:

1. **Base case:** prove \(P(1)\), or the first required value.
2. **Inductive hypothesis:** assume \(P(k)\) is true for some \(k\in\mathbb N\).
3. **Inductive step:** prove \(P(k+1)\) is true.
4. **Conclusion:** therefore \(P(n)\) is true for all required \(n\).

# 8. Core Theory

## 8.1 From “factor” to “divides”

In ordinary Maths, you might say:

\[
3\text{ is a factor of }12.
\]

In Further Maths proof language, write:

\[
3\mid 12.
\]

This means:

\[
12=4(3),\qquad 4\in\mathbb Z.
\]

So the proof sentence is:

\[
3\mid 12\quad\text{because }12=4(3)\text{ and }4\in\mathbb Z.
\]

**Bridge Note:** In ordinary A-Level Maths, we used factors and multiples informally. Here, Further Maths extends this by requiring a precise integer-multiple statement.

## 8.2 How to prove \(a\mid b\)

To prove \(a\mid b\), show that \(b\) can be written as \(a\) multiplied by an integer:

\[
b=ka,\qquad k\in\mathbb Z.
\]

For example, prove \(6\mid 18\):

\[
18=3(6),\qquad 3\in\mathbb Z.
\]

Therefore \(6\mid 18\).

### General proof pattern

To prove \(a\mid E\), aim for:

\[
E=a(\text{integer expression}).
\]

Then explain why the bracket is an integer.

For example, prove \(5\mid 10n\) for all \(n\in\mathbb Z\):

\[
10n=5(2n).
\]

Since \(n\in\mathbb Z\), \(2n\in\mathbb Z\). Therefore \(10n\) is \(5\) times an integer, so \(5\mid 10n\).

**Bridge Note:** In ordinary A-Level Maths, factorising \(10n\) as \(5(2n)\) might have felt like the whole answer. In Further Maths proof, the bracket being an integer is the little golden key.

## 8.3 How to prove \(a\nmid b\)

To prove \(a\nmid b\), show that \(b\) cannot be written as \(ka\) for any integer \(k\). A simple way is to show a non-zero remainder.

For example:

\[
47=3(15)+2.
\]

Since the remainder is \(2\), \(47\) is not an integer multiple of \(15\). Therefore \(15\nmid 47\).

## 8.4 Formal divisibility proof from the uploaded evidence

Given \(a,b,c\in\mathbb Z\), prove that if \(a\mid b\) and \(a\mid c\), then \(a\mid bn+cm\) for all \(m,n\in\mathbb Z\).

### Full proof

Let \(a,b,c,m,n\in\mathbb Z\). Assume \(a\mid b\) and \(a\mid c\).

Since \(a\mid b\), by definition of divisibility, there exists an integer \(k\) such that

\[
b=ka,\qquad k\in\mathbb Z.
\]

Since \(a\mid c\), there exists an integer \(j\) such that

\[
c=ja,\qquad j\in\mathbb Z.
\]

Now consider:

\[
bn+cm.
\]

Substitute \(b=ka\) and \(c=ja\):

\[
bn+cm=(ka)n+(ja)m.
\]

Use associativity and commutativity of multiplication:

\[
bn+cm=kan+jam.
\]

Factor out \(a\):

\[
bn+cm=a(kn)+a(jm),
\]

\[
bn+cm=a(kn+jm).
\]

Since \(k,j,n,m\in\mathbb Z\), we have \(kn\in\mathbb Z\), \(jm\in\mathbb Z\), and by closure under addition:

\[
kn+jm\in\mathbb Z.
\]

Let \(t=kn+jm\). Then \(t\in\mathbb Z\), and:

\[
bn+cm=at.
\]

So \(bn+cm\) is an integer multiple of \(a\). Therefore:

\[
a\mid bn+cm.
\]

Hence, if \(a\mid b\) and \(a\mid c\), then \(a\mid bn+cm\) for all \(m,n\in\mathbb Z\).

**Bridge Note:** In ordinary Maths, you might test \(3\mid 9\) and \(3\mid 12\), then observe that \(3\mid 9n+12m\). In Further Maths, we replace the numbers by symbols and prove the structure for every allowed integer.

## 8.5 Why integer closure matters

Number theory is mostly concerned with integers. Integers are closed under addition, subtraction and multiplication, but not division. For example, \(9\div 2=4.5\), which is not an integer.

This matters because divisibility proofs rely on statements such as:

\[
kn+jm\in\mathbb Z.
\]

Since \(k,n\in\mathbb Z\), \(kn\in\mathbb Z\). Since \(j,m\in\mathbb Z\), \(jm\in\mathbb Z\). Therefore \(kn+jm\in\mathbb Z\).

## 8.6 The official CCEA proof method: induction

The official CCEA outcome is not “do Number Theory algorithms”. It is:

\[
\text{construct proofs using mathematical induction.}
\]

A typical divisibility statement might be:

\[
P(n):\quad 3\mid (4^n-1).
\]

This means:

\[
4^n-1=3\times\text{an integer}.
\]

## 8.7 Induction structure for divisibility

To prove \(3\mid (4^n-1)\) for all \(n\in\mathbb N\):

### Stage 1: Define the statement

\[
P(n):\quad 3\mid (4^n-1).
\]

### Stage 2: Base case

For \(n=1\):

\[
4^1-1=4-1=3.
\]

Since \(3=1(3)\), \(P(1)\) is true.

### Stage 3: Inductive hypothesis

Assume that \(P(k)\) is true for some \(k\in\mathbb N\). That is:

\[
3\mid (4^k-1).
\]

By definition of divisibility, there exists \(t\in\mathbb Z\) such that:

\[
4^k-1=3t.
\]

Rearrange:

\[
4^k=3t+1.
\]

### Stage 4: Inductive step

We must prove \(P(k+1)\), which is:

\[
3\mid (4^{k+1}-1).
\]

Start with:

\[
4^{k+1}-1.
\]

Use the exponent law:

\[
4^{k+1}=4\cdot 4^k.
\]

So:

\[
4^{k+1}-1=4\cdot 4^k-1.
\]

Substitute \(4^k=3t+1\):

\[
4^{k+1}-1=4(3t+1)-1.
\]

Expand:

\[
4(3t+1)-1=12t+4-1.
\]

\[
12t+4-1=12t+3.
\]

Factor out \(3\):

\[
12t+3=3(4t+1).
\]

Since \(t\in\mathbb Z\), \(4t+1\in\mathbb Z\). Therefore:

\[
4^{k+1}-1=3(4t+1),
\]

where \(4t+1\in\mathbb Z\). So:

\[
3\mid (4^{k+1}-1).
\]

### Stage 5: Final conclusion

Since \(P(1)\) is true, and \(P(k)\Rightarrow P(k+1)\), by mathematical induction:

\[
3\mid (4^n-1)
\]

for all \(n\in\mathbb N\).

## 8.8 Why the induction proof works

The base case is the first domino. The inductive step says every domino knocks over the next one:

\[
P(k)\Rightarrow P(k+1).
\]

So \(P(1)\Rightarrow P(2)\Rightarrow P(3)\Rightarrow\cdots\). The proof does not list infinitely many cases. It builds a mechanism that carries truth along the whole chain.

## 8.9 Common divisibility induction pattern

Many divisibility induction proofs use this shape:

\[
P(n):\quad d\mid E_n.
\]

Assume:

\[
d\mid E_k.
\]

Then:

\[
E_k=dt,\qquad t\in\mathbb Z.
\]

Now show:

\[
E_{k+1}=d(\text{integer expression}).
\]

Then conclude:

\[
d\mid E_{k+1}.
\]

The crucial move is usually to rewrite \(E_{k+1}\) so that \(E_k\), or a close relative of \(E_k\), appears.

## 8.10 Worked mini-theory example: powers

Prove:

\[
7\mid (8^n-1)\quad\text{for all }n\in\mathbb N.
\]

Let \(P(n):\;7\mid (8^n-1)\).

For \(n=1\):

\[
8^1-1=8-1=7,
\]

so \(P(1)\) is true.

Assume \(P(k)\) is true for some \(k\in\mathbb N\). Then:

\[
8^k-1=7t,\qquad t\in\mathbb Z.
\]

Hence:

\[
8^k=7t+1.
\]

Now:

\[
8^{k+1}-1=8\cdot 8^k-1.
\]

Substitute:

\[
8^{k+1}-1=8(7t+1)-1.
\]

\[
=56t+8-1.
\]

\[
=56t+7.
\]

\[
=7(8t+1).
\]

Since \(t\in\mathbb Z\), \(8t+1\in\mathbb Z\). Therefore \(7\mid (8^{k+1}-1)\). Hence, by mathematical induction:

\[
7\mid (8^n-1)\quad\text{for all }n\in\mathbb N.
\]

## 8.11 Worked mini-theory example: direct divisibility support

Prove:

\[
4\mid n(n+1)(n+2)(n+3)
\]

for all \(n\in\mathbb Z\).

This is not an induction proof as written. It is a direct divisibility proof because the statement is about four consecutive integers. It is useful as proof-language support, but if CCEA asks specifically for induction, use induction.

Among four consecutive integers \(n,n+1,n+2,n+3\), there must be at least one multiple of \(4\). Therefore their product is divisible by \(4\). A more formal route uses cases modulo \(4\), but modular arithmetic is not treated as CCEA core here because the supplied CCEA map does not list it as a core topic.

## 8.12 What not to do in a CCEA induction question

Suppose the question says:

“Prove by induction that \(3\mid (4^n-1)\) for all positive integers \(n\).”

The following is not enough:

\[
4^1-1=3,
\]

\[
4^2-1=15,
\]

\[
4^3-1=63.
\]

All are divisible by \(3\), so it seems true. This only checks three cases. It does not prove \(3\mid (4^n-1)\) for every positive integer \(n\). A CCEA induction proof must have base case, inductive hypothesis, inductive step and conclusion.

## 8.13 Boundary-safe use of the division algorithm evidence

The uploaded evidence develops the division algorithm and writes division in the form:

\[
a=bq+r,
\]

with \(r\) as the remainder. It also emphasises that a remainder should satisfy the correct non-negative range, for example \(0\leq r<b\) when dividing by a positive integer \(b\). This is helpful enrichment for understanding remainders, but it is not treated as core CCEA FA21-PROOF content here.

If dividing \(17\) by \(3\):

\[
17=3(5)+2.
\]

Here \(q=5\) and \(r=2\). This says \(17\) is not divisible by \(3\), because the remainder is \(2\). But in a CCEA induction proof, the expected route is not usually “use the division algorithm”. The expected route is the induction chain.

# 9. Visual Asset Integration

## 9.1 Visual Evidence Limitation

The screenshot PDF could not be parsed as text, but the rendered pages show readable visual evidence. Page 1 displays the chapter title **“FP2: Chapter 1, Number Theory”**, with a menu containing Ex 1A The division algorithm, Ex 1B The Euclidean algorithm, Ex 1C Modular arithmetic, Ex 1D Divisibility tests, Ex 1E Solving congruence equations, Ex 1F Fermat’s little theorem, Ex 1G Combinatorics and Exam Questions. Pages 5 to 6 show the notation table for factor/divisor language, \(a\mid b\), \(a\nmid b\), \(\gcd(a,b)\), and coprime numbers. Pages 16 to 21 show examples using divisor notation and a proof that if \(a\mid b\) and \(a\mid c\), then \(a\mid bn+cm\). Pages 22 to 30 show division algorithm examples and warnings about positive remainders.

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

## 9.2 Visual Placeholder Register

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA `FA21-PROOF-LO001` + uploaded Number Theory notation evidence | Insert from svg/FA21ProofDivisibilityLanguageSupportBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths factor/HCF language with Further Maths divisor/proof language.]

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportMermaid-001 | Source: CCEA `FA21-PROOF-LO001` + lesson core theory | Insert from mermaid/FA21ProofDivisibilityLanguageSupportMermaid-001.md | Purpose: Show the logical flow of a divisibility induction proof.]

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportSVG-001 | Source: Uploaded transcript + screenshot notation table | Insert from svg/FA21ProofDivisibilityLanguageSupportSVG-001.svg | Purpose: Preserve the visible notation table as a clean learning visual.]

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportTikZ-001 | Source: CCEA `FA21-PROOF-LO001` + lesson proof examples | Insert from tikz/FA21ProofDivisibilityLanguageSupportTikZ-001.tex | Purpose: Use a precise mathematical ladder diagram to show how \(P(1)\), \(P(k)\Rightarrow P(k+1)\), and the final conclusion connect.]

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportSVG-002 | Source: Uploaded transcript proof \(a\mid b\), \(a\mid c\Rightarrow a\mid bn+cm\) | Insert from svg/FA21ProofDivisibilityLanguageSupportSVG-002.svg | Purpose: Preserve the algebraic route of the evidence-backed divisibility proof.]

[VISUAL PLACEHOLDER: FA21ProofDivisibilityLanguageSupportMermaid-002 | Source: CCEA Further Maths specification boundary + uploaded FP2 Number Theory evidence | Insert from mermaid/FA21ProofDivisibilityLanguageSupportMermaid-002.md | Purpose: Help students see which uploaded Number Theory topics are core, support, or enrichment.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA21ProofDivisibilityLanguageSupportWidget-001 | Source: AI-proposed teaching enhancement based on uploaded notation evidence and CCEA proof boundary | Insert from widgets/FA21ProofDivisibilityLanguageSupportWidget-001.html | Purpose: Practise converting ordinary factor language into formal divisor notation and integer-multiple proof sentences.]

The student inputs two integers \(a\) and \(b\). The widget checks whether \(a\mid b\), displays a proof sentence using \(b=ka\), and warns about reversing the notation or using zero as the divisor. It uses exact integer arithmetic and avoids decimals.

[INTERACTIVE PLACEHOLDER: FA21ProofDivisibilityLanguageSupportWidget-002 | Source: AI-proposed teaching enhancement based on CCEA `FA21-PROOF-LO001` | Insert from widgets/FA21ProofDivisibilityLanguageSupportWidget-002.html | Purpose: Help students build a CCEA-style induction proof for divisibility statements.]

The student selects a safe built-in example such as \(5\mid (6^n-1)\) or \(3\mid(n^3-n)\). The widget displays the statement \(P(n)\), base case, inductive hypothesis, inductive step, integer check and final conclusion.

[INTERACTIVE PLACEHOLDER: FA21ProofDivisibilityLanguageSupportWidget-003 | Source: AI-proposed teaching enhancement based on common exam traps and bridge context | Insert from widgets/FA21ProofDivisibilityLanguageSupportWidget-003.html | Purpose: Train students to distinguish examples, direct proof, exhaustion and induction.]

The widget shows a proof attempt and asks the student to classify it as example checking only, direct proof, proof by exhaustion, induction proof, or invalid/incomplete. It checks the common error of treating examples as proof.

# 11. Worked Examples

## 11.1 Evidence-backed Worked Example 1: Use new notation for divisibility

**Evidence source:** Uploaded transcript and screenshot pages 16 to 19.  
**On-spec status:** Supportive proof-language evidence, not a standalone CCEA Number Theory LO.  
**Ordinary Maths idea used:** Factor and multiple.  
**Further Maths upgrade:** Use \(a\mid b\) and \(a\nmid b\).

### Question

For each pair of integers, determine whether the first integer divides the second, writing your answer using the new notation:

\[
\text{a) }11,143
\]

\[
\text{b) }-4,28
\]

\[
\text{c) }15,47
\]

\[
\text{d) }3,2
\]

\[
\text{e) }16,0
\]

### Solution

#### Part a

We test whether \(11\mid 143\). To show \(11\mid 143\), write \(143\) as an integer multiple of \(11\):

\[
143=13\times 11.
\]

Since \(13\in\mathbb Z\),

\[
\boxed{11\mid 143}.
\]

#### Part b

We test whether \(-4\mid 28\):

\[
28=(-7)\times(-4).
\]

Since \(-7\in\mathbb Z\),

\[
\boxed{-4\mid 28}.
\]

#### Part c

\[
47=3\times 15+2.
\]

There is a remainder of \(2\). Therefore:

\[
\boxed{15\nmid 47}.
\]

#### Part d

\[
2=0\times 3+2.
\]

There is a remainder of \(2\). Therefore:

\[
\boxed{3\nmid 2}.
\]

#### Part e

\[
0=0\times 16.
\]

Since \(0\in\mathbb Z\),

\[
\boxed{16\mid 0}.
\]

## 11.2 Evidence-backed Worked Example 2: Find all divisors

Find all the divisors of \(8\) and \(11\), including negative divisors.

For \(8\), positive factor pairs are \(1\times 8\) and \(2\times 4\). Including negatives:

\[
\boxed{-8,-4,-2,-1,1,2,4,8}.
\]

For \(11\), since \(11\) is prime, the divisors are:

\[
\boxed{-11,-1,1,11}.
\]

## 11.3 Evidence-backed Worked Example 3: Formal divisibility proof

Given \(a,b,c\in\mathbb Z\), prove that if \(a\mid b\) and \(a\mid c\), then \(a\mid bn+cm\) for all \(m,n\in\mathbb Z\).

Since \(a\mid b\), there exists \(k\in\mathbb Z\) such that:

\[
b=ka.
\]

Since \(a\mid c\), there exists \(j\in\mathbb Z\) such that:

\[
c=ja.
\]

Now:

\[
bn+cm=(ka)n+(ja)m.
\]

\[
bn+cm=kan+jam.
\]

\[
bn+cm=a(kn+jm).
\]

Since \(j,k,n,m\in\mathbb Z\), \(kn+jm\in\mathbb Z\). Therefore \(bn+cm\) is \(a\) times an integer, so:

\[
\boxed{a\mid bn+cm}.
\]

## 11.4 CCEA-core Worked Example 4: Induction proof for divisibility

Prove by induction that:

\[
3\mid (4^n-1)
\]

for all positive integers \(n\).

Let:

\[
P(n):\quad 3\mid (4^n-1).
\]

For \(n=1\):

\[
4^1-1=4-1=3.
\]

Since \(3=3(1)\), \(P(1)\) is true.

Assume \(P(k)\) is true for some positive integer \(k\). Then:

\[
4^k-1=3t,\qquad t\in\mathbb Z.
\]

Hence:

\[
4^k=3t+1.
\]

Now:

\[
4^{k+1}-1=4\cdot 4^k-1.
\]

Substitute:

\[
4^{k+1}-1=4(3t+1)-1.
\]

\[
=12t+4-1.
\]

\[
=12t+3.
\]

\[
=3(4t+1).
\]

Since \(t\in\mathbb Z\), \(4t+1\in\mathbb Z\). Therefore \(3\mid (4^{k+1}-1)\). Since \(P(1)\) is true and \(P(k)\Rightarrow P(k+1)\), by mathematical induction:

\[
\boxed{3\mid (4^n-1)\text{ for all positive integers }n.}
\]

## 11.5 CCEA-core Worked Example 5: Induction proof with a polynomial expression

Prove by induction that:

\[
6\mid n(n+1)(n+2)
\]

for all positive integers \(n\).

Let:

\[
P(n):\quad 6\mid n(n+1)(n+2).
\]

For \(n=1\):

\[
1(1+1)(1+2)=1\cdot2\cdot3=6.
\]

Since \(6=6(1)\), \(P(1)\) is true.

Assume \(P(k)\) is true for some positive integer \(k\). Then:

\[
k(k+1)(k+2)=6t,\qquad t\in\mathbb Z.
\]

We need to prove:

\[
6\mid (k+1)(k+2)(k+3).
\]

Start with:

\[
(k+1)(k+2)(k+3).
\]

Rewrite:

\[
(k+1)(k+2)(k+3)=k(k+1)(k+2)+3(k+1)(k+2).
\]

Using the inductive hypothesis:

\[
(k+1)(k+2)(k+3)=6t+3(k+1)(k+2).
\]

Since \(k+1\) and \(k+2\) are consecutive integers, one of them is even. Therefore \((k+1)(k+2)\) is even, so there exists \(s\in\mathbb Z\) such that:

\[
(k+1)(k+2)=2s.
\]

Then:

\[
3(k+1)(k+2)=3(2s)=6s.
\]

Therefore:

\[
(k+1)(k+2)(k+3)=6t+6s=6(t+s).
\]

Since \(t+s\in\mathbb Z\),

\[
6\mid (k+1)(k+2)(k+3).
\]

By mathematical induction:

\[
\boxed{6\mid n(n+1)(n+2)\text{ for all positive integers }n.}
\]

## 11.6 Boundary-only Worked Example 6: Division algorithm with a negative dividend

**On-spec status:** Off-spec enrichment for this CCEA lesson. Included only in the boundary log and optional enrichment.

Use the division algorithm to find integers \(q\) and \(r\) such that:

\[
-232=11q+r,
\]

where \(0\leq r<11\).

The tempting choice \(q=-21\) gives:

\[
11(-21)=-231,
\]

so:

\[
-232=11(-21)-1.
\]

This gives \(r=-1\), which is not allowed. Instead use \(q=-22\):

\[
11(-22)=-242.
\]

To reach \(-232\), add \(10\):

\[
-242+10=-232.
\]

So:

\[
-232=11(-22)+10.
\]

Therefore:

\[
\boxed{q=-22,\qquad r=10.}
\]

# 12. Common Mistakes and Exam Traps

## 12.1 Mistake: treating examples as proof

Checking \(n=1,2,3\) is not enough to prove a statement for all \(n\in\mathbb N\). The safe route for `FA21-PROOF-LO001` is induction: base case, inductive hypothesis, inductive step and final conclusion.

## 12.2 Mistake: writing \(a\mid b\) backwards

\[
a\mid b
\]

means \(a\) divides \(b\). It does not mean \(b\) divides \(a\).

For example, \(3\mid 12\) is true because \(12=4(3)\), but \(12\mid 3\) is false.

## 12.3 Mistake: thinking the divisor must be smaller

\(16\mid 0\) because \(0=0(16)\). A non-zero divisor can be larger than the number it divides when the second number is \(0\).

## 12.4 Mistake: forgetting negative divisors

At GCSE, students often list only positive factors. In the uploaded evidence, negative integers are also allowed as divisors. For example:

\[
-4\mid 28
\]

because:

\[
28=(-7)(-4).
\]

## 12.5 Mistake: not saying the bracket is an integer

A common proof line is:

\[
10n=5(2n).
\]

Do not stop there. Say: since \(n\in\mathbb Z\), \(2n\in\mathbb Z\). Therefore \(10n\) is \(5\) multiplied by an integer, so \(5\mid 10n\).

## 12.6 Mistake: using decimal division inside proof

Avoid using decimals as proof language. For non-divisibility, write:

\[
47=3(15)+2.
\]

Then the non-zero remainder shows \(15\nmid 47\).

## 12.7 Mistake: using a negative remainder in the division algorithm

For \(-232=11q+r\), the line \(-232=11(-21)-1\) gives a negative remainder. The enrichment evidence uses \(-232=11(-22)+10\), so \(q=-22\), \(r=10\).

## 12.8 Mistake: importing off-spec methods into a CCEA proof answer

If the CCEA question says “prove by induction”, use induction. Do not replace the requested method with Euclidean algorithm, reverse Euclidean algorithm, modular arithmetic, Fermat’s little theorem, a calculator pattern, or examples only.

## 12.9 Mistake: weak final conclusion

A proof should not end with \(=3(4t+1)\). Finish by saying that since \(t\in\mathbb Z\), \(4t+1\in\mathbb Z\), so the expression is divisible by \(3\), and therefore by mathematical induction the result holds for all required \(n\).

## 12.10 Mistake: assuming \(P(k+1)\)

In the inductive step, you may assume \(P(k)\), but not \(P(k+1)\). Assuming what you are trying to prove makes the proof circular.

# 13. Practice Questions

The following questions are AI-generated on-spec practice questions unless explicitly marked as evidence-backed. They are not past-paper or textbook questions.

## 13.1 Basic Fluency Questions

### Question 1

For each statement, decide whether it is true or false.

\[
\text{a) }7\mid 56
\]

\[
\text{b) }9\mid 42
\]

\[
\text{c) }-5\mid 35
\]

\[
\text{d) }12\mid 0
\]

\[
\text{e) }0\mid 12
\]

### Question 2

Find all integer divisors of \(6\), \(13\), and \(-10\).

### Question 3

Write each statement using formal divisibility notation:

- \(4\) divides \(28\).
- \(6\) does not divide \(20\).
- \(15\) is divisible by \(3\).
- \(a\) divides \(b\).
- \(d\) is a common divisor of \(m\) and \(n\).

## 13.2 Bridge Questions

### Question 4

Prove that:

\[
5\mid 20n
\]

for all \(n\in\mathbb Z\).

### Question 5

Prove that:

\[
4\mid (8a+12b)
\]

for all \(a,b\in\mathbb Z\).

### Question 6

Let \(a,b,c\in\mathbb Z\). Prove that if \(a\mid b\) and \(a\mid c\), then \(a\mid(2b-3c)\).

## 13.3 Standard CCEA-Style Induction Questions

### Question 7

Prove by induction that:

\[
5\mid (6^n-1)
\]

for all positive integers \(n\).

### Question 8

Prove by induction that:

\[
7\mid (8^n-1)
\]

for all positive integers \(n\).

### Question 9

Prove by induction that:

\[
3\mid (n^3-n)
\]

for all positive integers \(n\).

## 13.4 Harder Synthesis Questions

### Question 10

Prove by induction that \(4\mid(5^n-1)\) for all positive integers \(n\). Then explain why checking \(n=1,2,3\) would not be enough.

### Question 11

Prove by induction that \(6\mid n(n+1)(n+2)\) for all positive integers \(n\).

### Question 12

A student writes \(2^1+1=3\), \(2^2+1=5\), \(2^3+1=9\). They conclude \(3\mid (2^n+1)\) for all positive integers \(n\). Explain why the conclusion is false, and identify the proof mistake.

# 14. Worked Solutions

## 14.1 Solution to Question 1

### Part a

\[
56=8(7),\qquad 8\in\mathbb Z.
\]

Therefore \(7\mid 56\) is true.

### Part b

\[
42=4(9)+6.
\]

The remainder is \(6\), not \(0\). Therefore \(9\mid 42\) is false.

### Part c

\[
35=(-7)(-5),\qquad -7\in\mathbb Z.
\]

Therefore \(-5\mid 35\) is true.

### Part d

\[
0=0(12),\qquad 0\in\mathbb Z.
\]

Therefore \(12\mid 0\) is true.

### Part e

\(0\mid 12\) would require \(12=k(0)\) for some \(k\in\mathbb Z\). But \(k(0)=0\) for every integer \(k\), so this is false.

## 14.2 Solution to Question 2

All integer divisors of \(6\):

\[
\boxed{-6,-3,-2,-1,1,2,3,6}.
\]

All integer divisors of \(13\):

\[
\boxed{-13,-1,1,13}.
\]

All integer divisors of \(-10\):

\[
\boxed{-10,-5,-2,-1,1,2,5,10}.
\]

## 14.3 Solution to Question 3

\[
\text{a) }4\mid 28
\]

\[
\text{b) }6\nmid 20
\]

\[
\text{c) }3\mid 15
\]

\[
\text{d) }a\mid b
\]

\[
\text{e) }d\mid m\text{ and }d\mid n
\]

## 14.4 Solution to Question 4

\[
20n=5(4n).
\]

Since \(n\in\mathbb Z\), \(4n\in\mathbb Z\). Therefore \(5\mid 20n\).

## 14.5 Solution to Question 5

\[
8a+12b=4(2a)+4(3b)=4(2a+3b).
\]

Since \(a,b\in\mathbb Z\), \(2a+3b\in\mathbb Z\). Therefore \(4\mid(8a+12b)\).

## 14.6 Solution to Question 6

Since \(a\mid b\), \(b=ka\) for some \(k\in\mathbb Z\). Since \(a\mid c\), \(c=ja\) for some \(j\in\mathbb Z\). Then:

\[
2b-3c=2(ka)-3(ja)=2ka-3ja=a(2k-3j).
\]

Since \(2k-3j\in\mathbb Z\), \(a\mid(2b-3c)\).

## 14.7 Solution to Question 7

Let \(P(n):\;5\mid(6^n-1)\).

For \(n=1\):

\[
6^1-1=5,
\]

so \(P(1)\) is true.

Assume \(P(k)\) is true. Then:

\[
6^k-1=5t,\qquad t\in\mathbb Z.
\]

So:

\[
6^k=5t+1.
\]

Now:

\[
6^{k+1}-1=6\cdot6^k-1=6(5t+1)-1=30t+6-1=30t+5=5(6t+1).
\]

Since \(6t+1\in\mathbb Z\), \(5\mid(6^{k+1}-1)\). Therefore by mathematical induction:

\[
\boxed{5\mid(6^n-1)\text{ for all positive integers }n.}
\]

## 14.8 Solution to Question 8

Let \(P(n):\;7\mid(8^n-1)\). For \(n=1\), \(8^1-1=7\), so \(P(1)\) is true.

Assume \(P(k)\) is true:

\[
8^k-1=7t,\qquad t\in\mathbb Z.
\]

Then \(8^k=7t+1\), and:

\[
8^{k+1}-1=8\cdot8^k-1=8(7t+1)-1=56t+7=7(8t+1).
\]

Since \(8t+1\in\mathbb Z\), \(7\mid(8^{k+1}-1)\). Therefore by mathematical induction:

\[
\boxed{7\mid(8^n-1)\text{ for all positive integers }n.}
\]

## 14.9 Solution to Question 9

Let \(P(n):\;3\mid(n^3-n)\). For \(n=1\), \(1^3-1=0=3(0)\), so \(P(1)\) is true.

Assume \(P(k)\) is true:

\[
k^3-k=3t,\qquad t\in\mathbb Z.
\]

Now:

\[
(k+1)^3-(k+1)=k^3+3k^2+3k+1-k-1.
\]

\[
=k^3+3k^2+2k.
\]

Rewrite to include the inductive hypothesis expression:

\[
k^3+3k^2+2k=(k^3-k)+3k^2+3k.
\]

Substitute:

\[
=3t+3k^2+3k=3(t+k^2+k).
\]

Since \(t+k^2+k\in\mathbb Z\), \(3\mid((k+1)^3-(k+1))\). Therefore by induction:

\[
\boxed{3\mid(n^3-n)\text{ for all positive integers }n.}
\]

## 14.10 Solution to Question 10

Let \(P(n):\;4\mid(5^n-1)\). For \(n=1\), \(5^1-1=4\), so \(P(1)\) is true.

Assume \(P(k)\):

\[
5^k-1=4t,\qquad t\in\mathbb Z.
\]

Then \(5^k=4t+1\), and:

\[
5^{k+1}-1=5\cdot5^k-1=5(4t+1)-1=20t+4=4(5t+1).
\]

Since \(5t+1\in\mathbb Z\), \(4\mid(5^{k+1}-1)\). Therefore by induction:

\[
\boxed{4\mid(5^n-1)\text{ for all positive integers }n.}
\]

Checking \(n=1,2,3\) is not enough because it proves only those three cases, not all positive integers. Induction proves the starting case and the rule that every true case forces the next true case.

## 14.11 Solution to Question 11

This is the same proof as Worked Example 11.5. The key lines are:

\[
(k+1)(k+2)(k+3)=k(k+1)(k+2)+3(k+1)(k+2).
\]

By the hypothesis, \(k(k+1)(k+2)=6t\). Since \(k+1\) and \(k+2\) are consecutive, \((k+1)(k+2)=2s\) for some \(s\in\mathbb Z\). Hence:

\[
(k+1)(k+2)(k+3)=6t+3(2s)=6(t+s),
\]

so \(6\mid(k+1)(k+2)(k+3)\). Therefore by induction:

\[
\boxed{6\mid n(n+1)(n+2)\text{ for all positive integers }n.}
\]

## 14.12 Solution to Question 12

The conclusion is false because:

\[
2^2+1=4+1=5,
\]

and:

\[
3\nmid 5.
\]

The proof mistake is treating selected examples as proof for all positive integers. A single counterexample disproves a universal statement.

# 15. Exam Technique Notes

## 15.1 When the question says “prove by induction”

Use:

```text
Let P(n) be the statement...
Base case...
Assume P(k) is true...
Now prove P(k+1)...
Therefore by mathematical induction...
```

Do not skip the conclusion.

## 15.2 When the question involves divisibility

Translate:

\[
d\mid E
\]

into:

\[
E=dt,\qquad t\in\mathbb Z.
\]

In the inductive hypothesis, write:

\[
d\mid E_k
\]

so:

\[
E_k=dt,\qquad t\in\mathbb Z.
\]

Then aim to prove:

\[
E_{k+1}=d(\text{integer}).
\]

## 15.3 Use exact algebra, not decimals

Avoid decimal division. Use exact integer-multiple form or quotient-and-remainder form.

## 15.4 Keep integer conditions visible

Good proof writing includes statements like \(t\in\mathbb Z\), \(4t+1\in\mathbb Z\), and \(t+s\in\mathbb Z\).

## 15.5 Show the inductive hypothesis being used

A weak induction proof says “Assume true for \(n=k\).” A stronger proof writes exactly what that means:

\[
5\mid(6^k-1)\Rightarrow 6^k-1=5t,\quad t\in\mathbb Z.
\]

## 15.6 Do not over-import the uploaded Number Theory material

The uploaded material includes algorithms and modular arithmetic. That is mathematically valuable, but for this CCEA lesson it stays outside the core unless CCEA evidence confirms it.

## 15.7 Calculator use

A calculator may help check arithmetic, but it does not prove the general statement. Exact algebra gets the marks.

# 16. Syllabus Gap Check

## 16.1 LO Coverage Table

| LO ID | Official CCEA wording | Covered? | Evidence strength | Notes |
|---|---|---:|---|---|
| `FA21-PROOF-LO001` | construct proofs using mathematical induction | Yes | Strong | Core induction structure taught explicitly, with divisibility examples. |

## 16.2 Evidence Coverage Table

| Evidence item | Covered in lesson? | Core or enrichment? | Notes |
|---|---:|---|---|
| Factor to divisor language | Yes | Support | Used to prepare formal proof language. |
| \(a\mid b\), \(a\nmid b\) | Yes | Support | Used throughout. |
| \(\gcd(a,b)\), coprime | Yes | Support/enrichment | Defined because uploaded evidence foregrounds it, but not central to CCEA induction. |
| Direct proof \(a\mid b\), \(a\mid c\Rightarrow a\mid bn+cm\) | Yes | Support | Included as evidence-backed worked example. |
| Integer closure under addition, subtraction and multiplication | Yes | Support | Used in direct divisibility proof and induction. |
| Division algorithm | Mentioned only | Enrichment | Not treated as CCEA core. |
| Euclidean algorithm | Mentioned only | Enrichment | Not taught as core. |
| Reverse Euclidean algorithm / Bézout identity | Mentioned only | Enrichment | Not taught as core. |
| Modular arithmetic | Mentioned only | Enrichment | Not taught as core. |
| Divisibility tests | Excluded from core | Enrichment | Could become separate enrichment pack. |
| Congruence equations | Excluded from core | Enrichment | Could become separate enrichment pack if desired. |
| Fermat’s little theorem | Excluded from core | Enrichment | No CCEA LO found in supplied map. |
| Combinatorics | Excluded from this lesson | Separate CCEA topics possible | Related to FAS2 Probability and FA22 Generating Functions, not FA21-PROOF. |

## 16.3 Bridge Coverage Table

| Bridge area | Covered? | How |
|---|---:|---|
| GCSE factors and multiples | Yes | Factor/divisor notation and examples. |
| Ordinary algebra | Yes | Factorisation and substitution in proofs. |
| Ordinary proof | Yes | Difference between example checking and proof. |
| Sequences and \(n\)-statements | Yes | Induction structure and \(P(n)\). |
| Counting | Boundary only | Mentioned as separate topic because transcript includes combinatorics but CCEA places related content elsewhere. |

## 16.4 Off-Spec Content Found but Excluded

The following material appears in the uploaded FP2 Number Theory evidence but is not taught as CCEA core in this lesson because no matching official CCEA Further Mathematics topic code or LO ID was found in the supplied CCEA specification map:

| Off-spec or boundary-risk content | Exclusion reason |
|---|---|
| Division algorithm as a full topic | Not identified as a CCEA `FA21-PROOF` LO. |
| Euclidean algorithm | Not identified as a CCEA `FA21-PROOF` LO. |
| Reverse Euclidean algorithm | Not identified as a CCEA `FA21-PROOF` LO. |
| Bézout identity | Not identified as a CCEA `FA21-PROOF` LO. |
| Modular arithmetic | Not identified as a CCEA `FA21-PROOF` LO. |
| Solving congruence equations | Not identified as a CCEA `FA21-PROOF` LO. |
| Fermat’s little theorem | Not identified as a CCEA `FA21-PROOF` LO. |
| Divisibility tests as a chapter | Not identified as a CCEA `FA21-PROOF` LO. |
| FP2 combinatorics chapter content | Related CCEA material belongs to separate FAS2/FA22 topics, not this FA21 proof lesson. |

## 16.5 Optional Enrichment Not Required by CCEA

1. Division algorithm and remainders.
2. Euclidean algorithm for gcd.
3. Reverse Euclidean algorithm.
4. Bézout identity.
5. Modular arithmetic.
6. Congruence equations.
7. Fermat’s little theorem.
8. Number Theory applications to cryptography.
9. Combinatorics extension, split properly into FAS2 Probability and FA22 Generating Functions where relevant.

## 16.6 Weak Evidence Warnings

| Issue | Warning |
|---|---|
| Screenshot PDF text could not be parsed | Visual content was interpreted from rendered pages and transcript, not full OCR text. |
| No official CCEA Number Theory topic found | Lesson is boundary-safe under `FA21-PROOF`, not a claimed CCEA Number Theory chapter. |
| FP2 label in uploaded evidence | FP2 is not one of the allowed CCEA project unit prefixes. It is treated as lesson-specific external evidence. |
| Transcript is long and includes wider material | Only divisibility language and proof-support material is used in the core. |
| No CCEA past-paper examples supplied | Practice questions are generated and labelled as such. No past-paper claim is made. |

## 16.7 Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| Official CCEA Number Theory LO IDs | Cannot build a core CCEA Number Theory lesson. |
| Topic-specific CCEA README for Number Theory | Cannot verify a Number Theory module boundary. |
| Topic-specific evidence checklist for Number Theory | Cannot verify expected asset/evidence checklist. |
| Independent textbook extract | Cannot independently verify textbook wording. |
| CCEA past-paper examples for divisibility induction | Generated examples are not labelled as past-paper. |
| Fully parsed screenshot PDF text | Some visual details remain limited to visible rendered pages and transcript. |

# 17. Recommended Enhancements Not in the Evidence

These are proposed enhancements only. They are not evidence-backed claims and are not required by CCEA unless later confirmed.

## 17.1 Proposed diagrams

1. A clean “ordinary factor language to formal divisor notation” bridge diagram.
2. An induction ladder for divisibility proof.
3. A proof skeleton diagram showing \(d\mid E_k\Rightarrow E_k=dt\Rightarrow E_{k+1}=d(\text{integer})\).
4. A boundary map separating CCEA core, proof-language support, off-spec enrichment, and future split-topic content.

## 17.2 Proposed animations

1. Domino animation for induction: \(P(1)\Rightarrow P(2)\Rightarrow P(3)\Rightarrow\cdots\).
2. Divisibility transformation animation: \(a\mid b\Rightarrow b=ka\).
3. Induction substitution animation: \(6^k=5t+1\) flowing into \(6^{k+1}-1=6(5t+1)-1\).

## 17.3 Proposed widgets

1. Divisibility notation translator.
2. Induction proof skeleton builder.
3. Proof or not proof classifier.
4. Integer closure checker.

## 17.4 Proposed extra examples

1. Induction with \(9\mid(10^n-1)\).
2. Induction with \(2\mid n(n+1)\).
3. Induction with \(5\mid(n^5-n)\) as a challenging extension, clearly labelled enrichment unless CCEA evidence is supplied.

## 17.5 Proposed bridge visuals

1. “Factor” vs “divisor” terminology card.
2. “Testing examples” vs “proving all cases” comparison.
3. “Direct proof” vs “induction proof” route map.
4. “When to use induction” decision tree.

# 18. Supplementary Sources Used

## 18.1 Project Sources Used

| Source | Use |
|---|---|
| CCEA GCE Further Mathematics Specification Map | Official unit/topic/LO boundary. |
| Further Maths README module map | Project metadata and lesson-pack workflow. |
| Further Maths Evidence Drop Checklist | Missing evidence, visual evidence and off-spec control. |
| Ordinary A-Level Maths Bridge Spec Extracts | Bridge context only. |
| CCEA GCE Mathematics Specification Map | Ordinary Maths bridge context only. |

## 18.2 Lesson-Specific Evidence Used

| Source | Use |
|---|---|
| `transcripts.md` | Supplied FP2 Number Theory transcript. Used for notation, divisor examples, direct proof structure, division algorithm enrichment warnings and off-spec logs. |
| `Chapter_1_Number_Theory_♾️_(Further_Pure_2)_screenshots.pdf` | Visual evidence for chapter menu, notation table and worked examples. Parsed text unavailable, so visible rendered page content and transcript were used cautiously. |

## 18.3 Ordinary A-Level Maths Bridge Sources Used

Ordinary A-Level Mathematics sources were used only to explain prior knowledge: factors, multiples, algebraic proof, factorisation, sequences and \(n\)-statements, and counting as a separate future topic. They do not override the CCEA Further Mathematics specification boundary.

## 18.4 Cross-Board or Non-CCEA Source Notes

The uploaded evidence is labelled FP2 and includes a broad Number Theory chapter. Since FP2 is not one of this project’s allowed CCEA unit prefixes, it is treated as lesson-specific external evidence. It is used only as divisibility notation support for CCEA proof work and as optional enrichment, clearly excluded from core.

## 18.5 Evidence Limitations

1. The screenshot PDF had no parsed text available.
2. Only visible rendered screenshot information and transcript text were used.
3. No official CCEA Number Theory topic code was found in the supplied CCEA map.
4. No CCEA past-paper questions were supplied for this exact lesson.
5. AI-generated practice questions are clearly labelled as generated practice, not past-paper or textbook questions.

# 19. Final Student Checklist

## 19.1 Prerequisite Confidence Checklist

- [ ] I know what an integer is.
- [ ] I understand factors and multiples.
- [ ] I can factorise expressions such as \(12t+3=3(4t+1)\).
- [ ] I can expand expressions such as \((k+1)^3\).
- [ ] I understand that examples do not prove a universal statement.
- [ ] I know that \(0\) is divisible by every non-zero integer.

## 19.2 Divisibility Language Checklist

- [ ] I can read \(a\mid b\) as “\(a\) divides \(b\)”.
- [ ] I can read \(a\nmid b\) as “\(a\) does not divide \(b\)”.
- [ ] I know that \(a\mid b\) means \(b=ka\) for some \(k\in\mathbb Z\).
- [ ] I can explain why \(-4\mid 28\).
- [ ] I can explain why \(15\nmid 47\).
- [ ] I can find positive and negative integer divisors of a number.
- [ ] I understand \(\gcd(a,b)\).
- [ ] I understand that \(\gcd(a,b)=1\) means \(a\) and \(b\) are coprime.

## 19.3 Further Maths Method Checklist

- [ ] I can state \(P(n)\) clearly.
- [ ] I can prove a base case.
- [ ] I can write an inductive hypothesis.
- [ ] I can translate a divisibility hypothesis into \(E_k=dt,\;t\in\mathbb Z\).
- [ ] I can manipulate \(E_{k+1}\) until it becomes \(d(\text{integer})\).
- [ ] I can write a final induction conclusion.

## 19.4 Exam Technique Checklist

- [ ] I do not use decimal division as a proof.
- [ ] I do not stop after checking examples.
- [ ] I do not assume \(P(k+1)\).
- [ ] I state why the bracket is an integer.
- [ ] I keep exact values.
- [ ] I use the proof method requested by the question.
- [ ] I do not import modular arithmetic or Euclidean algorithm into a CCEA induction proof unless the question asks for it.

## 19.5 Bridge Checklist

- [ ] I can explain how “factor” becomes “divisor”.
- [ ] I can explain how “HCF” becomes “gcd”.
- [ ] I can explain how ordinary algebra becomes proof language.
- [ ] I can explain why induction is stronger than checking examples.
- [ ] I can identify which uploaded FP2 Number Theory topics are enrichment only for this CCEA lesson.

## 19.6 Visual and Interactive Understanding Checklist

- [ ] I can use the notation ladder visual to translate ordinary language into formal notation.
- [ ] I can use the induction ladder visual to explain the proof flow.
- [ ] I can use the divisibility proof map to show \(a\mid b\Rightarrow b=ka\).
- [ ] I understand that the boundary map separates CCEA core from enrichment.
- [ ] I can use the planned widgets to practise notation and proof classification when generated later.
