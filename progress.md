# Progress Log

## 2026-04-06

### Book Navigation Ordering

- Reordered `_quarto.yml` so the Pandas chapter is followed immediately by the Pandas practice notebooks.
- Kept the NumPy chapter grouped with the NumPy practice notebooks after the Pandas section.
- This makes the sidebar flow match the learning sequence more naturally.

### Book Navigation Reordered Again

- Updated `_quarto.yml` so the NumPy chapter and NumPy practice notebooks now come before the Pandas section.
- Updated the part intro and `README.md` so the documented learning order matches the new book order.
- Added reflection prompts to all three NumPy practice notebooks so they match the pandas exercise format.
- Renamed the NumPy notebook titles to include `Practice` so the sidebar naming is consistent and less confusing.

## 2026-04-05

### Repository Understanding Baseline

- Mapped the repository structure.
- Confirmed this is a Quarto book project rather than a traditional application codebase.
- Identified `_quarto.yml` as the main project configuration.
- Confirmed the current authored book content is concentrated in part 1.
- Reviewed `.github/workflows/deploy.yml` and confirmed GitHub Pages deployment on pushes to `main`.

### Documentation Baseline

- Added `README.md` with a concise project overview, build instructions, deployment flow, and maintenance rule.
- Added `progress.md` to track changes and decisions over time.

### Ongoing Working Agreement

- Keep `README.md` updated when repository structure, setup, usage, or workflows change.
- Keep `progress.md` updated for each meaningful change we make going forward.

### Pandas Tutorial Expansion

- Added a new pandas chapter at `parts/part-1-python-foundations/03_pandas_for_ai_engineers.qmd`.
- Structured the chapter around the official pandas getting-started progression.
- Added three practice notebooks under `labs/pandas/` covering basics, transformations, and time/text handling.
- Updated `_quarto.yml` so the new chapter and notebooks are part of the rendered book.
- Updated `parts/part-1-python-foundations/_intro.qmd` to reflect the new learning path.
- Updated `README.md` to document the new pandas tutorial track.
- Verified the notebooks as valid JSON and rendered the book successfully with `QUARTO_PYTHON=.venv/bin/python quarto render`.
- Removed a render-time side effect from the pandas chapter so it no longer writes a sample CSV into the source tree.

### Quarto Preview Troubleshooting

- Investigated a local Quarto preview error: `BadResource: Bad resource ID`.
- Confirmed the generated pandas notebook pages existed and the full book render still succeeded.
- Cleared `.quarto/project-cache` and `.quarto/preview` to reset local Quarto preview state.
- Updated `README.md` with a preview-cache troubleshooting note and the recommended restart command.

### Exercise Style Upgrade

- Updated the pandas practice notebooks to use guided starter code instead of blank `# Your code here` cells.
- Added partial expressions, variable scaffolds, and `TODO` prompts so the exercises feel more like fill-in-the-gap learning.
- Documented the guided exercise style in `README.md`.

### NumPy Tutorial Expansion

- Added a new NumPy chapter at `parts/part-1-python-foundations/04_numpy_for_ai_engineers.qmd`.
- Structured the chapter around the official NumPy absolute beginners guide and user guide.
- Added three guided notebooks under `labs/numpy/` covering array basics, vectorized operations, and shapes with aggregations.
- Updated `_quarto.yml` so the NumPy chapter and notebooks are part of the rendered book.
- Updated `parts/part-1-python-foundations/_intro.qmd` to include NumPy in the part overview.
- Updated `README.md` to document the new NumPy tutorial track.
