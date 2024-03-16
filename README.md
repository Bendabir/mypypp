# MyPy++

![GitHub Tag](https://img.shields.io/github/v/tag/bendabir/mypypp?sort=semver&label=version)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypypp)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/mypypp)
![PyPI - License](https://img.shields.io/pypi/l/mypypp)
![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/mypypp)
![GitHub deployments](https://img.shields.io/github/deployments/bendabir/mypypp/release?label=release)

Collection of experimental plugins for MyPy.

## Installation

First, install the plugins with your favorie package manager (`pip`, `poetry`, etc.).

```python
pip install mypypp
```

## Usage

In your MyPy configuration file, declare the plugins you want to use. For example, within a `pyproject.toml` configuration file :

```toml
[tool.mypy]
plugins = ["mypypp.deprecated"]
```

## Development

The whole project relies on Poetry for setup. It has been developed with Python 3.8 for backward compatibility.

### Environment

```bash
poetry env use python3.8
poetry lock
poetry install --with dev
poetry run pre-commit install
```

### Quality

```bash
poetry run black . # Format code
poetry run ruff check --fix --force-exclude . # Lint code
poetry run mypy --ignore-missing-imports --scripts-are-modules . # Type check code
```

```bash
poetry run python -m pytest --cov=src/mypypp tests # Run all tests
```

### Build

```bash
poetry build -f wheel
```
