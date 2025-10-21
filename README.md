# largest-remainder [![codecov](https://codecov.io/gh/fido-id/largest-remainder-py/graph/badge.svg?token=WHZvIR6im8)](https://codecov.io/gh/fido-id/largest-remainder-py)


Utilities for working with the **Largest Remainder (Hamilton)** apportionment
algorithm. The package exposes a single `LargestRemainder` helper that rounds
floating point allocations to integers while preserving the requested total.

## Features

- ✅ Deterministic rounding that always matches the requested total
- ✅ Supports both sequences and mappings while keeping the original order of keys
- ✅ Fully type annotated API with comprehensive unit tests

## Installation

The package is published on PyPI. Install it with your preferred Python package
manager:

```bash
pip install largest-remainder
# or
uv add largest-remainder
```

## Usage

```python
from largest_remainder import LargestRemainder

# Round a list of quotas to an integer total
LargestRemainder.round([1, 2, 3], total=10)
# -> [2, 3, 5]

# Round a mapping and keep the original keys
LargestRemainder.round({"a": 1.0, "b": 2.0}, total=10)
# -> {"a": 3, "b": 7}
```

Values can be any non-negative numbers. The algorithm scales the inputs so that
their sum matches the requested `total` and then distributes the remaining units
to the elements with the largest fractional parts.

## Development

1. Install the development dependencies using [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync --all-extras --dev
   ```
2. Run the linters and unit tests:
   ```bash
   uv run ruff check .
   uv run mypy
   uv run pytest
   ```

## Contributing and community

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for
instructions on setting up a development environment and submitting changes.
Participation in this project is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Security

If you discover a security issue, please follow the process described in
[SECURITY.md](SECURITY.md).

## License

This project is licensed under the terms of the [MIT License](LICENSE).
