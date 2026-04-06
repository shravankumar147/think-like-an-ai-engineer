# Think Like an AI Engineer

This repository contains a Quarto-based book project focused on AI engineering as a systems discipline.

## What This Repo Contains

- A Quarto book configuration in `_quarto.yml`
- Source chapters written in `.qmd` files
- Generated site output in `_site`
- Quarto cache and freeze artifacts in `.quarto` and `_freeze`
- A GitHub Actions workflow that renders and deploys the book to GitHub Pages

## Current Structure

- `index.qmd`: Book landing page
- `parts/part-1-python-foundations/`: Active authored chapters currently included in the book
- `labs/numpy/`: Practice notebooks for hands-on NumPy work
- `labs/pandas/`: Practice notebooks for hands-on pandas work
- `front-matter/`: Preface and roadmap scaffolding
- `parts/part2_machine-learning/` to `parts/part6_production-ai/`: Planned future sections
- `.github/workflows/deploy.yml`: CI/CD workflow for rendering and deployment

## NumPy Tutorial Track

The repo includes a NumPy learning track inspired by the official NumPy beginner and user-guide documentation:

- `parts/part-1-python-foundations/04_numpy_for_ai_engineers.qmd`: Guided NumPy tutorial chapter
- `labs/numpy/01_numpy_array_basics.ipynb`: Array creation, shape, dtype, and indexing practice
- `labs/numpy/02_numpy_vectorized_operations.ipynb`: Vectorized math, broadcasting, and dot product practice
- `labs/numpy/03_numpy_shapes_and_aggregations.ipynb`: Reshape, axis-based summaries, and stacking practice

This material follows the official NumPy progression around array creation, indexing, vectorized computation, broadcasting, aggregation, reshaping, randomness, and basic linear algebra.

The practice notebooks use guided starter code rather than blank exercise cells, so learners can focus on completing the critical NumPy operation in an Andrew Ng style workflow.

## Pandas Tutorial Track

The repo also includes a pandas learning track inspired by the official pandas getting-started documentation:

- `parts/part-1-python-foundations/03_pandas_for_ai_engineers.qmd`: Guided pandas tutorial chapter
- `labs/pandas/01_pandas_basics_practice.ipynb`: DataFrame basics and filtering practice
- `labs/pandas/02_pandas_transformations_practice.ipynb`: Grouping, reshaping, and joins practice
- `labs/pandas/03_pandas_time_text_practice.ipynb`: Datetime and text processing practice

This material follows the official pandas learning progression around tabular data handling, selection, plotting, derived columns, summary statistics, reshaping, combining tables, time series, and text operations.

The practice notebooks use the same guided starter-code style as the NumPy exercises so learners complete key operations instead of starting from empty cells.

## Build And Preview

Prerequisites:

- Quarto installed
- Python 3.11 or compatible local environment
- Dependencies from `requirements.txt` installed if you want executable Python code cells to run during render

Typical commands:

```bash
quarto preview
```

```bash
quarto render
```

If you are using the repository virtual environment for executable notebook cells, render with:

```bash
QUARTO_PYTHON=.venv/bin/python quarto render
```

The rendered static site is written to `_site/`.

## Preview Troubleshooting

If `quarto preview` fails with a local cache error such as `BadResource: Bad resource ID`, clear Quarto's local preview cache and restart preview with the repository virtual environment:

```bash
rm -rf .quarto/project-cache .quarto/preview
QUARTO_PYTHON=.venv/bin/python quarto preview
```

This is a local environment issue rather than a content problem when the full render still succeeds.

## Deployment

On every push to `main`, GitHub Actions:

1. Checks out the repository
2. Sets up Python
3. Installs notebook-related dependencies
4. Installs Quarto and TinyTeX
5. Runs `quarto render`
6. Deploys `_site` to GitHub Pages

## Maintenance Rule

We keep both `README.md` and `progress.md` updated whenever we make meaningful repository changes, so the repo documentation and change history stay aligned with the actual work.
