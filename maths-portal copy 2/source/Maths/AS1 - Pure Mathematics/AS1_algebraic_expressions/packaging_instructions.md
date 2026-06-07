# packaging_instructions.md

## Packaging Plan

## Output Folder

Created folder:

```text
AS1_algebraic_expressions/
```

Inside it:

```text
AS1_algebraic_expressions_lesson.md
manifest.md
source_reference.md
packaging_instructions.md
mermaid/
svg/
tikz/
widgets/
```

## Recommended Zip Name

```text
AS1_algebraic_expressions_lesson_pack.zip
```

## Packaging Command

From the parent directory of `AS1_algebraic_expressions/`, run:

```bash
zip -r AS1_algebraic_expressions_lesson_pack.zip AS1_algebraic_expressions/
```

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix is standard CCEA Mathematics | Passed: AS1 |
| Unit name is correct | Passed: AS 1 Pure Mathematics |
| Topic code is correct | Passed: AS1-AF |
| Topic identity is complete | Passed |
| LO IDs are preserved exactly | Passed |
| On-spec evidence is covered | Passed for AS1-AF-LO001, AS1-AF-LO002 and most of AS1-AF-LO010 |
| Off-spec material is excluded or marked | Passed |
| Cross-board examples are controlled | Passed |
| Missing evidence is logged | Passed |
| SVG placeholders match drafted files | Passed |
| Widget placeholders match drafted files | Passed |
| Mermaid assets written | Passed, supplementary |
| TikZ assets written | Passed, supplementary |
| Manifest written | Passed |
| Source reference written | Passed |
| Files written to disk | Passed |
| Zip package created | Passed |

## Unresolved Issues

1. Simple algebraic division is part of AS1-AF-LO010 but was not fully developed in the supplied chapter evidence.
2. Factor theorem and remainder theorem are part of AS1-AF-LO011 but are not taught in this lesson.
3. Mermaid and TikZ assets are supplementary unless matching placeholders are added into the lesson Markdown.
