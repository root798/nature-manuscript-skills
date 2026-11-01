---
name: nature-research-figures
description: Design, revise and audit data figures for research manuscripts using explicit comparisons, reproducible colour profiles, caption checks and final-size rendering. Use for publication figures, Results panels, palette selection and figure–text reconciliation.
---

# Research figures for manuscripts

Start with the sentence that the finished figure must support. Identify the observations, comparator, unit, direction and limiting condition. Point to the mark or pair of marks that should let the reader judge the claim. If the manuscript only allows a caption revision, work in the permitted revision copy.

| Request | Use |
|---|---|
| Design a new figure or rebuild a confusing Results figure | [Evidence, panels, encodings and interpretation](references/figure-workflow.zh-CN.md). Write the role of each panel before selecting a chart. |
| Choose macaron colours for a new figure or recolour selected panels | Start with the [macaron selection workflow](references/macaron-selection.zh-CN.md). Bind one scientific variable to the slots and proof the actual marks. Use the [original-card example](assets/macaron-original-four.example.tsv) for an exact-card constraint or the [Palette C role map](assets/macaron-role-map.example.tsv) for the four-category extension. |
| Reproduce an approved figure or match its legend | Inspect the generating script and accepted figure together. Look up the matching [colour and marker guide](references/colour-guide.zh-CN.md), [machine-readable profiles](assets/palettes.json) and [swatch atlas](assets/palette-atlas.svg). Preserve the established category mapping. |
| Replace measurements or repair one panel | Keep an old render and source table. Compare panel identities, values, limits, aspect ratio, legend, caption and citations after editing. |
| Prepare the delivery files | [Final-size, export and caption checks](references/delivery.zh-CN.md). Inspect the actual file embedded in the manuscript. |
| Run a working template | [Synthetic paired example](references/example.zh-CN.md). From this skill's directory run `python3 scripts/render_example.py --out build`. One input CSV produces editable PDF and SVG, a PNG and a table of derived values. |

**Deliver a readable comparison.** A specific observation can explain how a mark is computed; the complete eligible sample determines how widely the conclusion holds. A new panel should add evidence, an informative control, a mechanism test or an explicit boundary. Move redundant displays out of the main argument.

**Protect scope.** For a locked main figure, report the exact mismatch and place suggested caption or text revisions in a separate revision document. Changes in direction or denominator require a substantive decision before swapping in numbers. A new supplementary panel needs a distinct purpose and authority to create it.

**Make style deterministic.** Set a physical canvas and assign colours, shapes, line roles, units and intervals once. Keep the source script and inputs with the final version. Use the destination journal's current artwork specifications for final delivery. The included profiles are reusable visual choices.
