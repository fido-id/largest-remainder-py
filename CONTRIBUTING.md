# Contributing

Thank you for considering contributing to `largest-remainder`! We welcome bug
reports, feature requests, and pull requests from the community. This document
describes how to get started.

## Prerequisites

- Python 3.9 or newer
- [uv](https://docs.astral.sh/uv/) for dependency management (or pip if you
  prefer)

## Setting up a development environment

1. Fork and clone the repository.
2. Install the development dependencies:
   ```bash
   uv sync --all-extras --dev
   ```
3. Install the package in editable mode (optional but recommended):
   ```bash
   uv run pip install -e .
   ```

## Running the checks

Before opening a pull request, please ensure the automated checks pass:

```bash
uv run ruff check .
uv run mypy
uv run pytest
```

Formatting is handled by Ruff; you can automatically format the code with:

```bash
uv run ruff format .
```

## Pull request guidelines

- Keep changes focused and describe the motivation in the pull request body.
- Update or add tests for any behavior change.
- Update documentation when applicable.
- Follow conventional commit messages if possible (e.g. `feat:`, `fix:`, `docs:`).

## Communication

If you have questions or need help, feel free to open a discussion or reach out
at [community@trustfull.com](mailto:community@trustfull.com).
