# Manifest: A22 Normal Distribution Lesson Pack

## Topic Identity

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A22 |
| Unit name | A2 2 Applied Mathematics |
| Applied section | Statistics |
| Primary topic code | A22-NORMAL |
| Official topic name | Statistical distributions |
| Lesson title | Normal Distribution |
| topic_slug | normal_distribution |
| topic_pascal | NormalDistribution |
| topic_id | A22NormalDistribution |
| lesson_file | A22_normal_distribution_lesson.md |
| Generation status | Written to files and packaged |

## Primary Learning Outcomes

| LO ID | Official / mapped learning outcome | Status |
|---|---|---|
| A22-NORMAL-LO001 | demonstrate understanding of and use the normal distribution as an example of a continuous probability distribution | Covered |
| A22-NORMAL-LO002 | find probabilities using the normal distribution | Covered |
| A22-NORMAL-LO003 | select an appropriate probability distribution for a context, with appropriate reasoning, including recognising when a binomial or normal model may not be appropriate | Covered |

## Adjacent On-Spec Learning Outcomes

| LO ID | Official / mapped learning outcome | Status |
|---|---|---|
| A22-HT-LO001 | demonstrate understanding and use the language of statistical hypothesis testing: null hypothesis, alternative hypothesis, significance level, test statistic, 1-tail test, 2-tail test, critical value, critical region, acceptance region and p-value | Included as adjacent support |
| A22-HT-LO002 | demonstrate understanding that a sample is being used to make an inference about the population and appreciate that the significance level is the probability of incorrectly rejecting the null hypothesis | Included as adjacent support |
| A22-HT-LO004 | conduct a statistical hypothesis test for the mean of a normal distribution with known, given or assumed variance and interpret the results in context | Included as adjacent support |

## Syllabus Boundary

### Core content included

- Normal distribution as a continuous probability distribution.
- Bell curve shape, symmetry, mean, median and mode.
- Notation \(X\sim N(\mu,\sigma^2)\).
- Meaning of \(\mu\), \(\sigma\), and \(\sigma^2\).
- Area under the normal curve as probability.
- Probability density.
- \(P(X=a)=0\) for continuous random variables.
- Points of inflection at \(\mu-\sigma\) and \(\mu+\sigma\).
- 68-95-99.7 rule.
- Calculator-based normal probability calculations.
- Left-tail, right-tail, interval and outside-region probabilities.
- Inverse normal calculations.
- Standardising with \(Z=\frac{X-\mu}{\sigma}\).
- Finding missing \(\mu\) and/or \(\sigma\) from probabilities.
- Choosing between binomial, normal, normal approximation, or neither.
- Binomial-to-normal approximation using \(Y\sim N(np,np(1-p))\).
- Continuity corrections.
- Adjacent hypothesis testing for the mean of a normal distribution.
- Sampling distribution \(\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right)\).

### Excluded or enrichment-only content

- MAT extension references.
- DrFrostMaths platform practice instructions.
- Bayesian maximum entropy context.
- CERN 5-sigma context.
- Formal Type I error theory beyond the CCEA boundary.
- Binomial proportion hypothesis testing as a core part of this lesson.
- Correlation coefficient hypothesis testing as a core part of this lesson.

## Phase Status

| Phase | Output | Status |
|---|---|---|
| Phase 0 | Evidence Intake and Plan | Complete |
| Phase 1 | Main Lesson Markdown | Complete |
| Phase 2 | Mermaid diagrams | Complete |
| Phase 3 | SVG assets | Complete |
| Phase 4 | TikZ assets | Complete |
| Phase 5 | Interactive widgets | Complete |
| Phase 6 | Manifest, source reference and packaging | Complete |
| File writing | Physical folder and ZIP creation | Complete |

## Folder Structure

```txt
A22_normal_distribution_lesson_pack/
  A22_normal_distribution_lesson.md
  manifest.md
  source_reference.md
  mermaid/
    A22NormalDistributionMER-001.md
    A22NormalDistributionMER-002.md
    A22NormalDistributionMER-003.md
  svg/
    A22NormalDistributionSVG-001.svg
    A22NormalDistributionSVG-002.svg
    A22NormalDistributionSVG-003.svg
    A22NormalDistributionSVG-004.svg
    A22NormalDistributionSVG-005.svg
    A22NormalDistributionSVG-006.svg
    A22NormalDistributionSVG-007.svg
    A22NormalDistributionSVG-008.svg
    A22NormalDistributionSVG-009.svg
    A22NormalDistributionSVG-010.svg
    A22NormalDistributionSVG-011.svg
  tikz/
    A22NormalDistributionTIKZ-001.tex
    A22NormalDistributionTIKZ-002.tex
    A22NormalDistributionTIKZ-003.tex
    A22NormalDistributionTIKZ-004.tex
  widgets/
    A22NormalDistributionWID-001.html
    A22NormalDistributionWID-002.html
    A22NormalDistributionWID-003.html
    A22NormalDistributionWID-004.html
```

## Asset Register

### Mermaid assets

| Asset ID | File | Purpose |
|---|---|---|
| A22NormalDistributionMER-001 | mermaid/A22NormalDistributionMER-001.md | Distribution-choice flowchart |
| A22NormalDistributionMER-002 | mermaid/A22NormalDistributionMER-002.md | Normal-probability method selector |
| A22NormalDistributionMER-003 | mermaid/A22NormalDistributionMER-003.md | Hypothesis-test decision route |

### SVG assets

| Asset ID | File | Purpose |
|---|---|---|
| A22NormalDistributionSVG-001 | svg/A22NormalDistributionSVG-001.svg | Bell curve with mean |
| A22NormalDistributionSVG-002 | svg/A22NormalDistributionSVG-002.svg | Effect of changing standard deviation |
| A22NormalDistributionSVG-003 | svg/A22NormalDistributionSVG-003.svg | Points of inflection at \(\mu\pm\sigma\) |
| A22NormalDistributionSVG-004 | svg/A22NormalDistributionSVG-004.svg | 68-95-99.7 rule |
| A22NormalDistributionSVG-005 | svg/A22NormalDistributionSVG-005.svg | Left-tail normal probability |
| A22NormalDistributionSVG-006 | svg/A22NormalDistributionSVG-006.svg | Outside-region normal probability |
| A22NormalDistributionSVG-007 | svg/A22NormalDistributionSVG-007.svg | Inverse normal boundary |
| A22NormalDistributionSVG-008 | svg/A22NormalDistributionSVG-008.svg | Continuity correction |
| A22NormalDistributionSVG-009 | svg/A22NormalDistributionSVG-009.svg | \(X\) versus \(\bar X\) |
| A22NormalDistributionSVG-010 | svg/A22NormalDistributionSVG-010.svg | Calculator workflow |
| A22NormalDistributionSVG-011 | svg/A22NormalDistributionSVG-011.svg | Hypothesis-test p-value decision |

### TikZ assets

| Asset ID | File | Purpose |
|---|---|---|
| A22NormalDistributionTIKZ-001 | tikz/A22NormalDistributionTIKZ-001.tex | Exam-style normal curve |
| A22NormalDistributionTIKZ-002 | tikz/A22NormalDistributionTIKZ-002.tex | Continuity correction diagram |
| A22NormalDistributionTIKZ-003 | tikz/A22NormalDistributionTIKZ-003.tex | Two-tailed critical region |
| A22NormalDistributionTIKZ-004 | tikz/A22NormalDistributionTIKZ-004.tex | Inverse normal diagram |

### Widget assets

| Asset ID | File | Purpose |
|---|---|---|
| A22NormalDistributionWID-001 | widgets/A22NormalDistributionWID-001.html | \(\mu,\sigma\) normal curve slider |
| A22NormalDistributionWID-002 | widgets/A22NormalDistributionWID-002.html | Continuity-correction converter |
| A22NormalDistributionWID-003 | widgets/A22NormalDistributionWID-003.html | Normal probability concept demo |
| A22NormalDistributionWID-004 | widgets/A22NormalDistributionWID-004.html | Normal mean hypothesis-test trainer |

## Placeholder Consistency Check

| Placeholder family | Phase generated | Status |
|---|---|---|
| Mermaid placeholders | Phase 2 | Matched |
| SVG placeholders | Phase 3 | Matched |
| TikZ placeholders | Phase 4 | Matched |
| Widget placeholders | Phase 5 | Matched |

## Final Generation Status

All lesson-pack phases have been drafted and written to files. The ZIP package has been created.
