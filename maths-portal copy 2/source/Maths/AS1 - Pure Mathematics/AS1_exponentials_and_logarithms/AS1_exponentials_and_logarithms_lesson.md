# AS1 Exponentials and Logarithms

## Lesson Title and Metadata

| Field | Value |
|---|---|
| Lesson title | Exponentials and Logarithms |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-EXPLOG |
| Topic name | Exponentials and logarithms |
| Topic slug | `exponentials_and_logarithms` |
| Topic Pascal | `ExponentialsAndLogarithms` |
| Topic ID | `AS1ExponentialsAndLogarithms` |
| Lesson file | `AS1_exponentials_and_logarithms_lesson.md` |
| Core LO IDs | AS1-EXPLOG-LO001, AS1-EXPLOG-LO002, AS1-EXPLOG-LO003, AS1-EXPLOG-LO004, AS1-EXPLOG-LO005, AS1-EXPLOG-LO006, AS1-EXPLOG-LO007, AS1-EXPLOG-LO008, AS1-EXPLOG-LO009, AS1-EXPLOG-LO010 |
| Tags | `#AS1`, `#Exponentials`, `#Logarithms`, `#GraphSketching`, `#GrowthDecay`, `#Modelling`, `#LawsOfLogs` |

---

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Official topic identity, LO IDs, core scope and boundaries |
| Project README / module map | Naming conventions, phases, folders, metadata fields |
| Project Evidence Drop Checklist | Evidence logging, missing evidence, off-spec control, placeholders |
| Chapter 14 PDF: Exponentials and Logarithms | Main mathematical content, graph examples, log laws, modelling examples |
| Chapter 14 transcript | Teacher explanations, warnings, modelling language, calculator notes |
| Chapter 14 screenshots PDF | Visual evidence for graph sketches and handwritten annotation sequence |
| Pearson / Dr Frost / Edexcel-style examples inside uploaded evidence | Used only where matching CCEA AS1-EXPLOG |
| MAT/AEA/PAT/complex-log content inside uploaded evidence | Excluded from core, logged as enrichment/off-spec |

---

## Specification Alignment

| LO ID | Lesson section where covered | Evidence basis |
|---|---|---|
| AS1-EXPLOG-LO001 | Core Theory 1 to 5 | Graphs $y=a^x$, growth vs decay, positive base |
| AS1-EXPLOG-LO002 | Core Theory 6 to 7 | $e^x$, Euler's number, simple transformations |
| AS1-EXPLOG-LO003 | Core Theory 8 to 10 | Logarithms as inverse functions |
| AS1-EXPLOG-LO004 | Core Theory 10 to 11 | Graph of $\ln x$, vertical asymptote, transformations |
| AS1-EXPLOG-LO005 | Core Theory 11 and 19 | $\ln x$ and $e^x$ cancelling as inverse functions |
| AS1-EXPLOG-LO006 | Core Theory 12 to 16 | Laws of logarithms and proof |
| AS1-EXPLOG-LO007 | Core Theory 17 to 20 | Solving $a^x=b$ using logarithms |
| AS1-EXPLOG-LO008 | Core Theory 21 | Exponential inequalities and monotonicity |
| AS1-EXPLOG-LO009 | Core Theory 22 | Growth and decay models |
| AS1-EXPLOG-LO010 | Core Theory 22 and Worked Examples 10 to 11 | Modelling population, continuous growth/decay, pesticide-style decay |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Sketch $y=a^x$, including growth when $a>1$ and decay when $0<a<1$.
2. Explain why $a^x$ is different from $x^a$.
3. Sketch $y=e^x$ and simple transformations such as $y=e^{3x}$, $y=5e^{-x}$, and $y=2+e^{x/3}$.
4. Use logarithms as inverse functions of exponentials.
5. Convert between exponential form and logarithmic form.
6. Sketch logarithmic graphs, including their domain and asymptote.
7. Use and prove the laws of logarithms.
8. Solve exponential equations using logarithms.
9. Solve simple exponential inequalities.
10. Interpret exponential growth and decay models in context, including initial value, growth/decay behaviour and long-term reasonableness.

---

## Prerequisite Recap

No external GCSE source is used here. The recap is only a readiness check using general mathematical skills already needed for AS Pure.

| Skill | Why it matters here |
|---|---|
| Index laws | Exponentials and log laws both grow from index laws |
| Negative powers | $2^{-x}$, $e^{-x}$, decay graphs and reciprocal forms |
| Fractional powers | Explains why negative bases are avoided for real exponential functions |
| Graph transformations | Used for $y=f(x)+a$, $y=f(x+a)$, $y=f(ax)$, $y=af(x)$ |
| Inverse operations | Logs undo exponentials |
| Solving equations | Needed when isolating $x$ after taking logs |
| Calculator use | Needed for $e^x$, $\ln x$, $\log x$, and $\log_a x$ |

---

## Big Picture Explanation

Exponential functions appear when a quantity is multiplied by the same factor repeatedly. Linear models live in the world of “add the same amount each step”. Exponentials live in the world of “multiply by the same amount each step”.

A savings account with 5% compound interest can be modelled by

$$1000(1.05)^t,$$

because each year the amount is multiplied by $1.05$.

A decreasing animal population might be modelled by

$$900(0.86)^t,$$

because multiplying by $0.86$ means keeping $86\%$ of the previous amount, so the population decreases by $14\%$ each year.

The logarithm is the inverse machine. If an exponential hides the variable in the power, the logarithm lets you retrieve it.

---

## Key Definitions and Notation

### Exponential function

An exponential function has the variable in the power:

$$y=a^x,$$

where $a>0$.

The number $a$ is called the **base**.

Important contrast:

$$a^x \quad \text{is exponential, because the variable is in the power;}$$

$$x^a \quad \text{is not exponential in this sense, because the variable is in the base.}$$

For example:

$$2^x \neq x^2.$$

They grow differently and they are handled differently.

### Euler's number and “the” exponential function

Euler's number is

$$e=2.71828\ldots$$

The function

$$y=e^x$$

is called **the exponential function**.

Any $y=a^x$ is an exponential function, but $y=e^x$ has special importance because of its behaviour in calculus. The uploaded evidence discusses differentiation of $e^x$, but differentiating $e^{kx}$ is logged as optional enrichment rather than required CCEA AS1-EXPLOG core.

### Logarithm

For $a>0$, $a\neq 1$, and $n>0$,

$$\log_a n=x$$

means

$$a^x=n.$$

Read $\log_a n$ as “log base $a$ of $n$”. The log function outputs the missing power.

Example:

$$\log_2 8=3$$

because

$$2^3=8.$$

### Natural logarithm

The inverse of $y=e^x$ is

$$y=\ln x.$$

This means

$$\ln x=\log_e x.$$

The inverse identities are

$$\ln(e^x)=x$$

and

$$e^{\ln x}=x, \qquad x>0.$$

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-001 | Source: Chapter 14 PDF and screenshot evidence | Insert from svg/AS1ExponentialsAndLogarithmsSVG-001.svg | Purpose: Plot $y=2^x$ using the table $x=-2,-1,0,1,2,3,4$.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-002 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-002.svg | Purpose: Compare $y=3^x$, $y=2^x$, and $y=1.5^x$ on the same axes.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-003 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-003.svg | Purpose: Show exponential growth versus exponential decay using $y=2^x$ and $y=2^{-x}$.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-004 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-004.svg | Purpose: Show the transformation $y=2^{x+3}$, including the new $y$-intercept.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-005 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-005.svg | Purpose: Show $y=e^x$, $y=5e^{-x}$, and $y=2+e^{x/3}$ with asymptotes.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-006 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-006.svg | Purpose: Show $y=\log_2 x$, its root $x=1$, and vertical asymptote $x=0$.]

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-007 | Source: CCEA specification plus Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-007.svg | Purpose: Show $y=e^x$ and $y=\ln x$ as inverse functions reflected in $y=x$.]

[INTERACTIVE PLACEHOLDER: AS1ExponentialsAndLogarithmsWidget-001 | Source: Chapter 14 transcript Desmos slider discussion | Insert from widgets/AS1ExponentialsAndLogarithmsWidget-001.html | Purpose: Let the student vary $a$ in $y=a^x$ and observe growth, decay and the fixed $y$-intercept.]

[INTERACTIVE PLACEHOLDER: AS1ExponentialsAndLogarithmsWidget-002 | Source: Chapter 14 PDF and transcript | Insert from widgets/AS1ExponentialsAndLogarithmsWidget-002.html | Purpose: Convert between $\log_a n=x$ and $a^x=n$.]

[INTERACTIVE PLACEHOLDER: AS1ExponentialsAndLogarithmsWidget-003 | Source: Chapter 14 PDF and transcript | Insert from widgets/AS1ExponentialsAndLogarithmsWidget-003.html | Purpose: Explore growth and decay models.]

---

# Core Theory

## 1. The graph of $y=2^x$

Start with the function

$$y=2^x.$$

Calculate values carefully:

$$2^{-2}=\frac{1}{2^2}=\frac14=0.25,$$

$$2^{-1}=\frac{1}{2}=0.5,$$

$$2^0=1,$$

$$2^1=2,$$

$$2^2=4,$$

$$2^3=8,$$

$$2^4=16.$$

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $y=2^x$ | $0.25$ | $0.5$ | $1$ | $2$ | $4$ | $8$ | $16$ |

Key graph facts:

1. The graph passes through $(0,1)$ because $2^0=1$.
2. As $x$ becomes more negative, $2^x$ gets closer to $0$, but never becomes $0$.
3. The horizontal asymptote is $y=0$.
4. The graph is increasing because each time $x$ increases by $1$, the value doubles.

For example,

$$2^{-8}=\frac{1}{2^8}=\frac{1}{256}=0.00390625.$$

This is very small, but it is not zero.

---

## 2. Why exponential functions matter

For $y=a^x$,

$$a^{x+1}=a^x\cdot a.$$

This means $a^x$ gets $a$ times bigger each time $x$ increases by $1$.

That is the signature move of an exponential model: multiply by the same factor each step.

For example, if money grows by 5% each year, the multiplier is

$$1+\frac{5}{100}=1.05.$$

A possible model is

$$S=1000(1.05)^t.$$

At $t=0$,

$$S=1000(1.05)^0$$

$$S=1000(1)$$

$$S=1000.$$

After one year,

$$S=1000(1.05)^1$$

$$S=1050.$$

After two years,

$$S=1000(1.05)^2$$

$$S=1000(1.1025)$$

$$S=1102.50.$$

The increase from year 1 to year 2 is larger than the increase from year 0 to year 1 because the 5% is being taken from a larger amount.

---

## 3. Growth and decay for $y=a^x$

### Case 1: $a>1$

If $a>1$, then $y=a^x$ is an exponential growth graph.

Examples:

$$y=1.5^x,\qquad y=2^x,\qquad y=3^x.$$

All pass through $(0,1)$ because $a^0=1$.

For $x>0$, the larger the base, the larger the $y$-value:

$$1.5^x<2^x<3^x.$$

For $x<0$, the larger the base, the smaller the $y$-value:

$$3^x<2^x<1.5^x.$$

This happens because negative powers create reciprocals. At $x=-1$:

$$3^{-1}=\frac13,\qquad 2^{-1}=\frac12,\qquad 1.5^{-1}=\frac{1}{1.5}=\frac23.$$

Therefore

$$\frac13<\frac12<\frac23.$$

### Case 2: $0<a<1$

If $0<a<1$, then $y=a^x$ is an exponential decay graph.

Example:

$$y=\left(\frac12\right)^x.$$

Each time $x$ increases by $1$, the output is multiplied by $\frac12$.

Important identity:

$$\left(\frac12\right)^x=2^{-x}.$$

Reason:

$$\left(\frac12\right)^x=(2^{-1})^x=2^{-x}.$$

Therefore $y=2^{-x}$ is an exponential decay graph.

---

## 4. Reflection property of $y=2^{-x}$

Let

$$f(x)=2^x.$$

Then

$$f(-x)=2^{-x}.$$

Using negative powers,

$$2^{-x}=\frac{1}{2^x}.$$

Also,

$$\frac{1}{2^x}=\left(\frac12\right)^x.$$

So

$$f(-x)=\left(\frac12\right)^x.$$

The transformation $y=f(-x)$ is a reflection of $y=f(x)$ in the $y$-axis, which is the line $x=0$.

---

## 5. Exponential graph transformations

A useful sketching method is:

1. Decide the shape: growth or decay.
2. Find the $y$-intercept by setting $x=0$.
3. Find the horizontal asymptote.

### Example: sketch $y=2^{x+3}$

The base graph is $y=2^x$.

The input $x$ has been replaced by $x+3$, so this is a horizontal translation left by $3$.

Find the $y$-intercept by setting $x=0$:

$$y=2^{0+3}$$

$$y=2^3$$

$$y=8.$$

So the graph crosses the $y$-axis at $(0,8)$.

The horizontal asymptote is unchanged: $y=0$.

---

## 6. The exponential function $y=e^x$

Euler's number is

$$e=2.71828\ldots$$

The function

$$y=e^x$$

is called **the exponential function**.

Key facts:

$$e^0=1,$$

so the graph passes through $(0,1)$.

The graph has horizontal asymptote $y=0$ and is increasing for all real $x$.

---

## 7. Simple transformations of $e^x$

### Example: sketch $y=e^{3x}$

The input $x$ has been replaced by $3x$. This corresponds to a stretch parallel to the $x$-axis with scale factor $\frac13$.

For a sketch, use the three-point method.

Shape: exponential growth.

$y$-intercept:

$$y=e^{3(0)}=e^0=1.$$

Horizontal asymptote: $y=0$.

### Example: sketch $y=5e^{-x}$

The negative sign in the power gives decay. The factor $5$ is outside the exponential term, so it is a vertical stretch by scale factor $5$.

Find the $y$-intercept:

$$y=5e^{-0}=5e^0=5(1)=5.$$

So the graph passes through $(0,5)$ and has horizontal asymptote $y=0$.

### Example: sketch $y=2+e^{x/3}$

Rewrite the power:

$$\frac{x}{3}=\frac13x.$$

The input has been multiplied by $\frac13$, so the graph is stretched parallel to the $x$-axis by scale factor $3$.

The $+2$ outside the exponential moves the graph up by $2$.

The original asymptote $y=0$ moves up to $y=2$.

Find the $y$-intercept:

$$y=2+e^{0/3}=2+e^0=2+1=3.$$

So the graph crosses the $y$-axis at $(0,3)$ and has horizontal asymptote $y=2$.

Important exam warning: when a graph is translated vertically, the horizontal asymptote must also be translated and labelled.

### Example: sketch $y=e^{-2x}-1$

Shape: decay-type graph because the exponent has negative coefficient.

$y$-intercept:

$$y=e^{-2(0)}-1=e^0-1=1-1=0.$$

So the graph passes through $(0,0)$.

Asymptote: $y=e^{-2x}$ has asymptote $y=0$. The $-1$ moves the graph down by $1$, so the new asymptote is $y=-1$.

---

## 8. Logarithms as inverse functions

A logarithm is the inverse of an exponential function.

The statement

$$\log_a n=x$$

means

$$a^x=n.$$

The log gives the missing power.

Examples:

$$\log_3 81=4 \quad \text{because} \quad 3^4=81.$$

$$\log_2\left(\frac18\right)=-3 \quad \text{because} \quad 2^{-3}=\frac18.$$

$$\log_4 1=0 \quad \text{because} \quad 4^0=1.$$

$$\log_a a^3=3.$$

---

## 9. Domain warning for logarithms

A logarithm can output a negative number, for example

$$\log_2\left(\frac12\right)=-1.$$

But you cannot take the logarithm of a negative number in AS real-valued mathematics, and $\log_a 0$ is not defined.

Reason: the graph $y=a^x$, where $a>0$, never reaches zero and never becomes negative.

So for logarithm inputs,

$$x>0.$$

---

## 10. The graph of $y=\log_2 x$

Use the inverse relationship with $y=2^x$.

If

$$y=\log_2 x,$$

then

$$2^y=x.$$

| $x$ | $\frac14$ | $\frac12$ | $1$ | $2$ | $4$ | $8$ |
|---:|---:|---:|---:|---:|---:|---:|
| $y=\log_2 x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |

Important graph facts:

1. The graph is not defined for $x\leq0$.
2. The graph has vertical asymptote $x=0$.
3. The root is $x=1$, because $\log_2 1=0$.
4. The graph is increasing, but its gradient gradually decreases.

---

## 11. Natural logarithms and $e^x$

The inverse of $y=e^x$ is $y=\ln x$.

This means

$$\ln x=\log_e x.$$

Since $e^x$ and $\ln x$ are inverse functions,

$$\ln(e^x)=x$$

and

$$e^{\ln x}=x.$$

### Example: solve $e^x=5$

Apply $\ln$ to both sides:

$$\ln(e^x)=\ln 5.$$

Since $\ln(e^x)=x$,

$$x=\ln 5.$$

### Example: solve $2\ln x+1=5$

Subtract $1$ from both sides:

$$2\ln x=4.$$

Divide by $2$:

$$\ln x=2.$$

Apply $e^{(\cdot)}$ to both sides:

$$e^{\ln x}=e^2.$$

Since $e^{\ln x}=x$,

$$x=e^2.$$

---

## 12. Laws of logarithms

For $a>0$, $a\neq1$, $x>0$, and $y>0$:

### Product law

$$\log_a x+\log_a y=\log_a(xy).$$

### Quotient law

$$\log_a x-\log_a y=\log_a\left(\frac{x}{y}\right).$$

### Power law

$$k\log_a x=\log_a(x^k).$$

Equivalently,

$$\log_a(x^k)=k\log_a x.$$

Special cases:

$$\log_a a=1,$$

because $a^1=a$.

$$\log_a 1=0,$$

because $a^0=1$.

$$\log\left(\frac1x\right)=\log(x^{-1})=-\log x.$$

The base must be consistent when using the laws.

---

## 13. Proof of the product law

Let

$$p=\log_a x$$

and

$$q=\log_a y.$$

By the definition of logarithms,

$$a^p=x$$

and

$$a^q=y.$$

Multiply these equations:

$$xy=a^p\cdot a^q.$$

Using the index law $a^p a^q=a^{p+q}$,

$$xy=a^{p+q}.$$

Convert back into logarithmic form:

$$\log_a(xy)=p+q.$$

Now substitute back:

$$p=\log_a x, \qquad q=\log_a y.$$

Therefore

$$\boxed{\log_a x+\log_a y=\log_a(xy)}.$$

---

## 14. Proof of the quotient law

Let

$$p=\log_a x$$

and

$$q=\log_a y.$$

Then

$$a^p=x$$

and

$$a^q=y.$$

Divide:

$$\frac{x}{y}=\frac{a^p}{a^q}.$$

Using the index law

$$\frac{a^p}{a^q}=a^{p-q},$$

we get

$$\frac{x}{y}=a^{p-q}.$$

Convert back into logarithmic form:

$$\log_a\left(\frac{x}{y}\right)=p-q.$$

Substitute back:

$$\boxed{\log_a x-\log_a y=\log_a\left(\frac{x}{y}\right)}.$$

---

## 15. Proof of the power law

Let

$$p=\log_a x.$$

Then

$$a^p=x.$$

Raise both sides to the power $k$:

$$(a^p)^k=x^k.$$

Using the index law $(a^p)^k=a^{pk}$,

$$a^{pk}=x^k.$$

Convert back into logarithmic form:

$$\log_a(x^k)=pk.$$

Since $p=\log_a x$,

$$\boxed{k\log_a x=\log_a(x^k)}.$$

---

## 16. Anti-laws: mistakes to avoid

Wrong:

$$\log_a(b+c)=\log_a b+\log_a c.$$

There is no law for the logarithm of a sum.

Correct:

$$\log_a(bc)=\log_a b+\log_a c.$$

Also correct:

$$\log_2(x^3)=3\log_2 x.$$

Wrong:

$$(\log_2 x)^3=3\log_2 x.$$

The power law applies when the power is on the input $x$, not when the whole logarithm has been cubed.

---

## 17. Solving equations of the form $a^x=b$

### Situation A: matching bases

Example:

$$3^{2x+1}=27.$$

Write $27$ as a power of $3$:

$$27=3^3.$$

So

$$3^{2x+1}=3^3.$$

Since the bases are equal, the powers are equal:

$$2x+1=3.$$

Subtract $1$:

$$2x=2.$$

Divide by $2$:

$$x=1.$$

### Situation B: logarithms needed

Example:

$$3^x=20.$$

Apply $\log_3$ to both sides:

$$\log_3(3^x)=\log_3 20.$$

Since $\log_3(3^x)=x$,

$$x=\log_3 20.$$

Using a calculator,

$$x=2.727\ldots$$

So

$$x=2.727\quad \text{to 3 d.p.}$$

---

## 18. Solving exponential equations where both sides contain powers

Example:

$$3^x=2^{x+1}.$$

Take natural logarithms of both sides:

$$\ln(3^x)=\ln(2^{x+1}).$$

Use the log power law:

$$x\ln3=(x+1)\ln2.$$

Expand the right-hand side:

$$x\ln3=x\ln2+\ln2.$$

Move the $x$-terms to one side:

$$x\ln3-x\ln2=\ln2.$$

Factorise $x$:

$$x(\ln3-\ln2)=\ln2.$$

Divide by $\ln3-\ln2$:

$$x=\frac{\ln2}{\ln3-\ln2}.$$

Using a calculator,

$$x=1.710\quad \text{to 3 d.p.}$$

---

## 19. Solving equations involving $\ln x$

### Example 1: solve $e^x-3=0$

$$e^x-3=0$$

$$e^x=3$$

$$\ln(e^x)=\ln3$$

$$x=\ln3.$$

### Example 2: solve $\ln(2x)=4$

$$\ln(2x)=4$$

$$e^{\ln(2x)}=e^4$$

$$2x=e^4$$

$$x=\frac{e^4}{2}.$$

Domain check: $2x>0$, so $x>0$. The solution is positive, so it is valid.

### Example 3: solve $e^{3x+2}=3$

$$e^{3x+2}=3$$

$$\ln(e^{3x+2})=\ln3$$

$$3x+2=\ln3$$

$$3x=\ln3-2$$

$$x=\frac{\ln3-2}{3}.$$

---

## 20. Solving logarithmic equations

Example:

$$\log_2(2x)=\log_2(5x+4)-3.$$

Move the $-3$ to the left:

$$\log_2(2x)+3=\log_2(5x+4).$$

Write $3$ as a logarithm base $2$:

$$3=\log_2 8,$$

because $2^3=8$.

So

$$\log_2(2x)+\log_2 8=\log_2(5x+4).$$

Use the product law:

$$\log_2(16x)=\log_2(5x+4).$$

If the logarithms have the same base and are equal, then their inputs are equal:

$$16x=5x+4.$$

Subtract $5x$:

$$11x=4.$$

Divide by $11$:

$$x=\frac4{11}.$$

Domain check:

$$2x>0 \Rightarrow x>0,$$

and

$$5x+4>0.$$

For $x=\frac4{11}$,

$$2x=\frac8{11}>0$$

and

$$5x+4=\frac{20}{11}+\frac{44}{11}=\frac{64}{11}>0.$$

So

$$\boxed{x=\frac4{11}}.$$

---

## 21. Exponential inequalities

The key idea is monotonicity.

For $a>1$, the graph $y=a^x$ is increasing. Taking logarithms preserves the inequality direction.

Example:

$$2^x<10.$$

Take $\log_2$ of both sides:

$$\log_2(2^x)<\log_2 10.$$

So

$$x<\log_2 10.$$

Using a calculator,

$$\log_2 10=3.322\ldots$$

Therefore

$$x<3.322\quad \text{to 3 d.p.}$$

For $0<a<1$, the graph $y=a^x$ is decreasing, so the inequality direction must be handled carefully.

Example:

$$\left(\frac12\right)^x<8.$$

Rewrite

$$\left(\frac12\right)^x=2^{-x}.$$

So

$$2^{-x}<8.$$

Write $8=2^3$:

$$2^{-x}<2^3.$$

Since $2^u$ is increasing,

$$-x<3.$$

Multiply by $-1$, reversing the inequality:

$$x>-3.$$

---

## 22. Exponential growth and decay models

A common exponential model is

$$y=Aa^t.$$

Another common continuous model is

$$y=Ae^{kt}.$$

In either case, $A$ is the initial value because when $t=0$,

$$y=Aa^0=A$$

or

$$y=Ae^{k(0)}=Ae^0=A.$$

### Growth

If $a>1$, then $y=Aa^t$ models growth.

Example:

$$S=1000(1.05)^t$$

means the amount is multiplied by $1.05$ each year, so it increases by $5\%$ each year.

### Decay

If $0<a<1$, then $y=Aa^t$ models decay.

Example:

$$P=900(0.86)^t$$

means the amount is multiplied by $0.86$ each year, so it decreases by

$$1-0.86=0.14=14\%.$$

### Continuous $e$-based decay

If

$$P=160e^{-0.006t},$$

then the initial amount is $160$ because

$$P=160e^{-0.006(0)}=160e^0=160.$$

The negative sign in the exponent tells us this is decay.

As $t$ becomes large, $e^{-0.006t}$ gets closer to $0$, so $P$ gets closer to $0$, but does not become negative.

---

# Worked Examples

## Worked Example 1: Plot and sketch $y=2^x$

Complete the table and sketch $y=2^x$.

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $y=2^x$ |  |  |  |  |  |  |  |

### Solution

For $x=-2$:

$$y=2^{-2}=\frac{1}{2^2}=\frac14.$$

For $x=-1$:

$$y=2^{-1}=\frac12.$$

For $x=0$:

$$y=2^0=1.$$

For $x=1$:

$$y=2^1=2.$$

For $x=2$:

$$y=2^2=4.$$

For $x=3$:

$$y=2^3=8.$$

For $x=4$:

$$y=2^4=16.$$

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $y=2^x$ | $\frac14$ | $\frac12$ | $1$ | $2$ | $4$ | $8$ | $16$ |

Sketch features:

- passes through $(0,1)$;
- increasing;
- horizontal asymptote $y=0$;
- approaches the $x$-axis as $x\to-\infty$ but never touches it.

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-001 | Source: Chapter 14 PDF and screenshot evidence | Insert from svg/AS1ExponentialsAndLogarithmsSVG-001.svg | Purpose: Plot $y=2^x$ using the table.]

---

## Worked Example 2: Compare $y=3^x$, $y=2^x$, and $y=1.5^x$

All three graphs have $y$-intercept $1$, because

$$3^0=2^0=1.5^0=1.$$

For $x>0$:

$$1.5^x<2^x<3^x.$$

For $x<0$:

$$3^x<2^x<1.5^x.$$

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-002 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-002.svg | Purpose: Compare $y=3^x$, $y=2^x$, and $y=1.5^x$.]

---

## Worked Example 3: Sketch $y=2^{x+3}$

Start from $y=2^x$.

The $x$ has been replaced by $x+3$, so the graph is translated left by $3$.

Find the $y$-intercept:

$$x=0,$$

$$y=2^{0+3}=2^3=8.$$

So the graph crosses the $y$-axis at $(0,8)$.

The horizontal asymptote remains $y=0$.

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-004 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-004.svg | Purpose: Show $y=2^{x+3}$.]

---

## Worked Example 4: Sketch $y=2+e^{x/3}$

The basic graph is $y=e^x$.

The power is $x/3$, which gives a stretch parallel to the $x$-axis by scale factor $3$.

The $+2$ outside the exponential moves the graph up by $2$.

Shape: exponential growth.

$y$-intercept:

$$y=2+e^{0/3}=2+e^0=2+1=3.$$

Asymptote: $y=2$.

Therefore the sketch must show $(0,3)$ and $y=2$.

[VISUAL PLACEHOLDER: AS1ExponentialsAndLogarithmsSVG-005 | Source: Chapter 14 PDF | Insert from svg/AS1ExponentialsAndLogarithmsSVG-005.svg | Purpose: Show $e^x$ transformations and asymptotes.]

---

## Worked Example 5: Convert between log and exponential form

### Part A

Write $6^2=36$ in logarithmic form.

The base is $6$, the power is $2$, and the result is $36$.

$$\boxed{\log_6 36=2}.$$

### Part B

Write $\log_3 81=4$ in exponential form.

$$\boxed{3^4=81}.$$

### Part C

Evaluate $\log_2\left(\frac18\right)$.

We need the power of $2$ that gives $\frac18$.

Since

$$\frac18=\frac{1}{2^3}=2^{-3},$$

$$\boxed{\log_2\left(\frac18\right)=-3}.$$

---

## Worked Example 6: Use the laws of logarithms

Simplify

$$2\log_2 x+\log_2 3-\log_2 6.$$

Use the power law:

$$2\log_2 x=\log_2(x^2).$$

So

$$2\log_2 x+\log_2 3-\log_2 6=\log_2(x^2)+\log_2 3-\log_2 6.$$

Use the product law:

$$\log_2(x^2)+\log_2 3=\log_2(3x^2).$$

So

$$\log_2(3x^2)-\log_2 6=\log_2\left(\frac{3x^2}{6}\right).$$

Simplify:

$$\frac{3x^2}{6}=\frac{x^2}{2}.$$

Therefore

$$\boxed{\log_2\left(\frac{x^2}{2}\right)}.$$

---

## Worked Example 7: Solve $3^x=20$

Take $\log_3$ of both sides:

$$\log_3(3^x)=\log_3 20.$$

So

$$x=\log_3 20=2.7268\ldots$$

$$\boxed{x=2.727\text{ to 3 d.p.}}$$

---

## Worked Example 8: Solve $5^{4x-1}=61$

Take $\log_5$ of both sides:

$$\log_5(5^{4x-1})=\log_5 61.$$

So

$$4x-1=\log_5 61.$$

Add $1$:

$$4x=\log_5 61+1.$$

Divide by $4$:

$$x=\frac{\log_5 61+1}{4}=0.8886\ldots$$

$$\boxed{x=0.889\text{ to 3 d.p.}}$$

---

## Worked Example 9: Solve $3^x=2^{x+1}$

Take natural logarithms:

$$\ln(3^x)=\ln(2^{x+1}).$$

Use the power law:

$$x\ln3=(x+1)\ln2.$$

Expand:

$$x\ln3=x\ln2+\ln2.$$

Collect terms:

$$x\ln3-x\ln2=\ln2.$$

Factorise:

$$x(\ln3-\ln2)=\ln2.$$

Divide:

$$x=\frac{\ln2}{\ln3-\ln2}=1.7095\ldots$$

$$\boxed{x=1.710\text{ to 3 d.p.}}$$

---

## Worked Example 10: Pesticide decay model

The density of a pesticide in a given section of field, $P$ mg/m$^2$, is modelled by

$$P=160e^{-0.006t},$$

where $t$ is the time in days since the pesticide was first applied.

### Part A: Estimate the density after 15 days

Substitute $t=15$:

$$P=160e^{-0.006(15)}.$$

Calculate the exponent:

$$-0.006(15)=-0.09.$$

So

$$P=160e^{-0.09}=146.237\ldots$$

$$\boxed{P=146.2\text{ mg/m}^2\text{ to 1 d.p.}}$$

### Part B: Interpret the meaning of 160

The value $160$ is the initial density.

At $t=0$:

$$P=160e^{-0.006(0)}=160e^0=160(1)=160.$$

So $160$ means the pesticide density was initially

$$\boxed{160\text{ mg/m}^2}.$$

### Part C: Sketch the graph of $P$ against $t$

The exponent is negative, so this is exponential decay.

At $t=0$, $P=160$.

As $t$ increases, $P$ decreases towards $0$.

The graph must show:

- vertical intercept $160$;
- decay shape;
- horizontal asymptote $P=0$;
- no negative pesticide density.

---

## Worked Example 11: Radioactive decay model

The mass $m$ grams of a radioactive substance $t$ years after being observed is modelled by

$$m=25e^{-0.05t}.$$

Find the mass after six months.

The time $t$ is measured in years. Six months is half a year, so $t=0.5$.

Substitute:

$$m=25e^{-0.05(0.5)}.$$

Calculate the exponent:

$$-0.05(0.5)=-0.025.$$

So

$$m=25e^{-0.025}=24.3827\ldots$$

$$\boxed{m=24.4\text{ g to 3 s.f.}}$$

---

## Worked Example 12: Exponential inequality

Solve

$$2^x<50.$$

Take $\log_2$ of both sides:

$$\log_2(2^x)<\log_2 50.$$

So

$$x<\log_2 50.$$

Using a calculator,

$$\log_2 50=5.6438\ldots$$

Therefore

$$\boxed{x<5.644\text{ to 3 d.p.}}$$

---

# Guided Practice

Attempt these before reading the full solutions.

## Practice Question 1

Complete the table for $y=3^x$.

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---:|---:|---:|---:|---:|---:|---:|
| $y=3^x$ |  |  |  |  |  |  |

State the $y$-intercept and horizontal asymptote.

## Practice Question 2

Sketch $y=4e^{-x}$. State the graph type, the $y$-intercept, and the horizontal asymptote.

## Practice Question 3

Write each statement in the other form.

a. $5^3=125$

b. $\log_4 64=3$

c. $\log_7\left(\frac17\right)=-1$

## Practice Question 4

Simplify

$$\log_3 x+\log_3 12-\log_3 4.$$

## Practice Question 5

Simplify

$$3\ln2+\ln5.$$

Give the answer as a single logarithm.

## Practice Question 6

Solve

$$e^x-7=0.$$

## Practice Question 7

Solve

$$\ln(3x)=5.$$

## Practice Question 8

Solve

$$4^{2x-1}=18.$$

Give your answer to 3 decimal places.

## Practice Question 9

Solve

$$5^x=3^{x+2}.$$

Give your answer to 3 decimal places.

## Practice Question 10

Solve

$$3^x>40.$$

Give your answer to 3 decimal places.

## Practice Question 11

A population is modelled by

$$P=1200(1.04)^t,$$

where $t$ is the number of years after recording begins.

a. State the initial population.  
b. State the annual percentage increase.  
c. Find the population after 8 years, to the nearest whole number.

## Practice Question 12

The concentration $C$ of a drug in the bloodstream is modelled by

$$C=80e^{-0.12t},$$

where $t$ is measured in hours.

a. State the initial concentration.  
b. Find the concentration after 6 hours, to 1 decimal place.  
c. Describe the long-term behaviour of the model.

---

# Common Mistakes and Exam Traps

## Trap 1: confusing $a^x$ with $x^a$

$2^x$ has the variable in the power. $x^2$ has the variable in the base. They behave differently.

## Trap 2: forgetting that all $a^x$ graphs pass through $(0,1)$

For any positive base $a$, $a^0=1$.

If there is a vertical multiplier or translation, recalculate the intercept. Do not just write $1$ out of habit.

## Trap 3: forgetting to label the asymptote

For basic exponential graphs, $y=0$ is the horizontal asymptote.

For $y=2+e^{x/3}$, the asymptote is $y=2$, not $y=0$.

For logarithmic graphs, $x=0$ is the vertical asymptote for $y=\ln x$ or $y=\log_a x$.

## Trap 4: trying to log a negative number

A logarithm may output a negative number, but the input must be positive.

## Trap 5: inventing a log law for addition

Wrong:

$$\log_a(x+y)=\log_a x+\log_a y.$$

Correct:

$$\log_a(xy)=\log_a x+\log_a y.$$

## Trap 6: moving powers from the wrong place

Correct:

$$\log_a(x^k)=k\log_a x.$$

Wrong:

$$(\log_a x)^k=k\log_a x.$$

## Trap 7: not checking logarithm equation solutions

If solving a logarithmic equation leads to possible values of $x$, check each one in the original equation. Reject values that make a log input zero or negative.

## Trap 8: using the wrong time unit in modelling

If $t$ is measured in years, six months means $t=0.5$, not $t=6$.

## Trap 9: interpreting the initial value incorrectly

In $P=Ae^{kt}$, the initial value is $A$ because $P=Ae^0=A$ at $t=0$.

## Trap 10: ignoring whether a model is sensible for large $t$

The CCEA boundary includes evaluating whether predictions are appropriate, especially for large values of $t$.

---

# Exam Technique Notes

## 1. For sketching exponential graphs

Use the three-feature method:

1. Shape: growth or decay.
2. $y$-intercept: set $x=0$.
3. Asymptote: usually $y=0$, unless shifted vertically.

Example:

$$y=5e^{-x}+2.$$

Shape: decay.

$y$-intercept:

$$y=5e^0+2=5+2=7.$$

Asymptote: $y=2$.

## 2. For converting logs

Use the sentence:

$$\log_a n=x$$

means:

$$a \text{ to the power } x \text{ gives } n.$$

## 3. For solving $a^x=b$

If $b$ is an obvious power of $a$, match bases.

If not, use logs:

$$a^x=b$$

$$\log_a(a^x)=\log_a b$$

$$x=\log_a b.$$

Or use natural logs:

$$\ln(a^x)=\ln b$$

$$x\ln a=\ln b$$

$$x=\frac{\ln b}{\ln a}.$$

## 4. For different bases on both sides

Use natural logs and collect $x$-terms.

## 5. For logarithmic equations

Before solving, note the domain restrictions. After solving, check answers in the original logarithms.

## 6. For modelling questions

Always identify:

1. what the variables represent;
2. the time unit;
3. the initial value;
4. whether the model grows or decays;
5. the required rounding;
6. whether the prediction is sensible in context.

---

# Common CCEA-Style Wording

| Wording | What it usually wants |
|---|---|
| “Sketch the graph” | Shape, intercepts and asymptotes, not a perfect plotted graph |
| “State the initial value” | Substitute $t=0$ |
| “Interpret the constant” | Explain in context, not just “it is $A$” |
| “Use the model to estimate” | Substitute the given value and calculate |
| “Solve” | Give exact form if possible, otherwise rounded as requested |
| “Show that” | Write enough algebra that the stated result appears naturally |
| “Hence” | Use the previous result rather than restarting |
| “Comment on the model” | Discuss reasonableness, limitations or large-$t$ behaviour |

---

# Full Worked Solutions to Guided Practice

## Solution 1

For $y=3^x$:

$$3^{-2}=\frac19,$$

$$3^{-1}=\frac13,$$

$$3^0=1,$$

$$3^1=3,$$

$$3^2=9,$$

$$3^3=27.$$

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---:|---:|---:|---:|---:|---:|---:|
| $y=3^x$ | $\frac19$ | $\frac13$ | $1$ | $3$ | $9$ | $27$ |

The $y$-intercept is $(0,1)$. The horizontal asymptote is $y=0$.

## Solution 2

For $y=4e^{-x}$, the exponent is negative, so the graph is exponential decay.

$y$-intercept:

$$y=4e^{-0}=4e^0=4.$$

The $y$-intercept is $(0,4)$ and the horizontal asymptote is $y=0$.

## Solution 3

a. $5^3=125$ gives $\boxed{\log_5 125=3}$.

b. $\log_4 64=3$ gives $\boxed{4^3=64}$.

c. $\log_7\left(\frac17\right)=-1$ gives $\boxed{7^{-1}=\frac17}$.

## Solution 4

$$\log_3 x+\log_3 12-\log_3 4$$

$$=\log_3(12x)-\log_3 4$$

$$=\log_3\left(\frac{12x}{4}\right)$$

$$=\boxed{\log_3(3x)}.$$

## Solution 5

$$3\ln2+\ln5=\ln(2^3)+\ln5$$

$$=\ln8+\ln5$$

$$=\ln(8\cdot5)$$

$$=\boxed{\ln40}.$$

## Solution 6

$$e^x-7=0$$

$$e^x=7$$

$$\ln(e^x)=\ln7$$

$$\boxed{x=\ln7}.$$

## Solution 7

$$\ln(3x)=5$$

$$e^{\ln(3x)}=e^5$$

$$3x=e^5$$

$$\boxed{x=\frac{e^5}{3}}.$$

Domain check: $3x>0$, so $x>0$. The solution is valid.

## Solution 8

$$4^{2x-1}=18$$

$$\log_4(4^{2x-1})=\log_4 18$$

$$2x-1=\log_4 18$$

$$2x=\log_4 18+1$$

$$x=\frac{\log_4 18+1}{2}=1.5850\ldots$$

$$\boxed{x=1.585\text{ to 3 d.p.}}$$

## Solution 9

$$5^x=3^{x+2}$$

$$\ln(5^x)=\ln(3^{x+2})$$

$$x\ln5=(x+2)\ln3$$

$$x\ln5=x\ln3+2\ln3$$

$$x\ln5-x\ln3=2\ln3$$

$$x(\ln5-\ln3)=2\ln3$$

$$x=\frac{2\ln3}{\ln5-\ln3}=4.3037\ldots$$

$$\boxed{x=4.304\text{ to 3 d.p.}}$$

## Solution 10

$$3^x>40$$

$$\log_3(3^x)>\log_3 40$$

$$x>\log_3 40=3.3578\ldots$$

$$\boxed{x>3.358\text{ to 3 d.p.}}$$

## Solution 11

$$P=1200(1.04)^t.$$

Initial population:

$$P=1200(1.04)^0=1200.$$

Annual percentage increase:

$$1.04=1+0.04,$$

so the increase is $4\%$.

After 8 years:

$$P=1200(1.04)^8=1642.827\ldots$$

Nearest whole number:

$$\boxed{1643}.$$

## Solution 12

$$C=80e^{-0.12t}.$$

Initial concentration:

$$C=80e^{-0.12(0)}=80e^0=80.$$

After 6 hours:

$$C=80e^{-0.12(6)}=80e^{-0.72}=38.939\ldots$$

To 1 decimal place:

$$\boxed{38.9}.$$

Because the exponent is negative, the model is exponential decay. As $t$ becomes large, $C$ gets closer to $0$ but does not become negative.

---

# Syllabus Gap Check

| LO ID | Coverage status | Evidence/comment |
|---|---|---|
| AS1-EXPLOG-LO001 | Covered | $a^x$, growth/decay, positive base, graph features |
| AS1-EXPLOG-LO002 | Covered | $e^x$, graph, transformations |
| AS1-EXPLOG-LO003 | Covered | $\log_a x$ as inverse of $a^x$ |
| AS1-EXPLOG-LO004 | Covered | $\ln x$, graph features and asymptote |
| AS1-EXPLOG-LO005 | Covered | $\ln x$ as inverse of $e^x$ |
| AS1-EXPLOG-LO006 | Covered | log laws plus proofs |
| AS1-EXPLOG-LO007 | Covered | $a^x=b$, including matching bases and logs |
| AS1-EXPLOG-LO008 | Covered | exponential inequalities |
| AS1-EXPLOG-LO009 | Covered | growth and decay models |
| AS1-EXPLOG-LO010 | Covered | compound growth, population growth, radioactive/drug-style decay, pesticide decay; limitations noted |

## Evidence-backed but excluded from core

| Evidence item | Decision |
|---|---|
| Differentiating $e^{kx}$, such as $\frac{d}{dx}(e^{5x})=5e^{5x}$ | Logged as boundary-risk because it is not part of the AS1-EXPLOG LO list used for this lesson |
| Differential equations and rate proportional to amount | Logged as enrichment only, not required core |
| Limit definition of $e$ | Logged as enrichment only |
| Chilli sweet and Secret Santa/derangements | Excluded from core |
| Complex logarithm $\log_4(-1)=\frac{i\pi}{\ln4}$ | Excluded from core |
| MAT/AEA/PAT questions | Excluded from required CCEA core |
| Log-linear regression/non-linear data transformations | Optional extension only unless separately mapped to a required CCEA outcome |

---

# Visual and Interactive Asset Plan

| Asset ID | Type | Phase | Purpose |
|---|---|---:|---|
| AS1ExponentialsAndLogarithmsSVG-001 | SVG | Phase 3 | Plot $y=2^x$ from table |
| AS1ExponentialsAndLogarithmsSVG-002 | SVG | Phase 3 | Compare $y=3^x$, $y=2^x$, $y=1.5^x$ |
| AS1ExponentialsAndLogarithmsSVG-003 | SVG | Phase 3 | Growth vs decay, $y=2^x$ and $y=2^{-x}$ |
| AS1ExponentialsAndLogarithmsSVG-004 | SVG | Phase 3 | Transformation $y=2^{x+3}$ |
| AS1ExponentialsAndLogarithmsSVG-005 | SVG | Phase 3 | $e^x$ transformations and asymptotes |
| AS1ExponentialsAndLogarithmsSVG-006 | SVG | Phase 3 | Graph of $y=\log_2x$ |
| AS1ExponentialsAndLogarithmsSVG-007 | SVG | Phase 3 | $e^x$ and $\ln x$ as inverse functions |
| AS1ExponentialsAndLogarithmsMermaid-001 | Mermaid | Phase 2 | Flowchart for solving exponential equations |
| AS1ExponentialsAndLogarithmsMermaid-002 | Mermaid | Phase 2 | Flowchart for choosing log laws |
| AS1ExponentialsAndLogarithmsMermaid-003 | Mermaid | Phase 2 | Exponential graph sketching checklist |
| AS1ExponentialsAndLogarithmsMermaid-004 | Mermaid | Phase 2 | Logarithmic and exponential form converter flow |
| AS1ExponentialsAndLogarithmsMermaid-005 | Mermaid | Phase 2 | Growth/decay modelling interpretation flow |
| AS1ExponentialsAndLogarithmsTikZ-001 | TikZ | Phase 4 | Clean graph of exponential growth and decay |
| AS1ExponentialsAndLogarithmsTikZ-002 | TikZ | Phase 4 | Clean graph of $\ln x$ |
| AS1ExponentialsAndLogarithmsTikZ-003 | TikZ | Phase 4 | $e^x$ and $\ln x$ reflected in $y=x$ |
| AS1ExponentialsAndLogarithmsTikZ-004 | TikZ | Phase 4 | Transformation $y=2+e^{x/3}$ |
| AS1ExponentialsAndLogarithmsWidget-001 | HTML widget | Phase 5 | Slider for $y=a^x$ |
| AS1ExponentialsAndLogarithmsWidget-002 | HTML widget | Phase 5 | Log/exponential form converter |
| AS1ExponentialsAndLogarithmsWidget-003 | HTML widget | Phase 5 | Growth/decay model calculator |

---

# Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority |
| Project README/module map | Workflow and metadata authority |
| Project Evidence Drop Checklist | Evidence handling and logging authority |
| Chapter 14 Exponentials and Logarithms PDF | Lesson evidence, on-spec parts only |
| Chapter 14 transcript | Lesson explanation evidence, on-spec parts only |
| Chapter 14 screenshot PDF | Visual evidence, used only where clear |
| Pearson/Dr Frost/Edexcel-style items inside uploaded evidence | Used only where matching CCEA AS1-EXPLOG |
| MAT/AEA/PAT/complex-log extension material | Not used as required CCEA core |

---

# Final Student Checklist

## Graphs

- [ ] I can sketch $y=a^x$ for $a>1$.
- [ ] I can sketch $y=a^x$ for $0<a<1$.
- [ ] I know that $y=a^x$ passes through $(0,1)$.
- [ ] I know that the basic horizontal asymptote is $y=0$.
- [ ] I can sketch $y=e^x$.
- [ ] I can handle simple transformations such as $y=e^{3x}$, $y=5e^{-x}$, and $y=2+e^{x/3}$.
- [ ] I remember to update and label asymptotes after vertical translations.

## Logarithms

- [ ] I can explain $\log_a n=x\iff a^x=n$.
- [ ] I can convert between logarithmic and exponential form.
- [ ] I know that logs can output negative numbers.
- [ ] I know that log inputs must be positive.
- [ ] I can sketch $y=\log_a x$.
- [ ] I can sketch $y=\ln x$.
- [ ] I know that $y=e^x$ and $y=\ln x$ are inverse functions.

## Laws of logarithms

- [ ] I can use $\log_a x+\log_a y=\log_a(xy)$.
- [ ] I can use $\log_a x-\log_a y=\log_a\left(\frac{x}{y}\right)$.
- [ ] I can use $k\log_a x=\log_a(x^k)$.
- [ ] I can prove the three log laws from index laws.
- [ ] I do not split $\log_a(x+y)$.
- [ ] I check domains after solving log equations.

## Equations and inequalities

- [ ] I can solve $a^x=b$ using matching bases where possible.
- [ ] I can solve $a^x=b$ using logs where needed.
- [ ] I can solve equations like $3^x=2^{x+1}$.
- [ ] I can solve equations involving $e^x$ and $\ln x$.
- [ ] I can solve basic exponential inequalities.
- [ ] I handle inequality direction carefully when rewriting bases or multiplying by a negative.

## Modelling

- [ ] I can identify the initial value from $A$ in $Aa^t$ or $Ae^{kt}$.
- [ ] I can interpret growth multipliers such as $1.04$ as $4\%$ growth.
- [ ] I can interpret decay multipliers such as $0.86$ as $14\%$ decay.
- [ ] I can substitute time values using the correct unit.
- [ ] I can describe long-term behaviour.
- [ ] I can comment on whether a model is sensible for large $t$.

---

# Progress Manifest

| Item | Status |
|---|---|
| Phase 0 Evidence Intake and Plan | Complete |
| Phase 1 Main Lesson Markdown | Complete |
| Phase 2 Mermaid assets | Complete |
| Phase 3 SVG assets | Complete |
| Phase 4 TikZ assets | Complete |
| Phase 5 Widgets | Complete |
| Phase 6 Manifest/source reference/packaging | Complete |
| Files written | Yes |
| Zip pack created | Yes |
