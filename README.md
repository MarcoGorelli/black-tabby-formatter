[![Build Status](https://github.com/MarcoGorelli/black-tabby-formatter/workflows/tox/badge.svg)](https://github.com/MarcoGorelli/black-tabby-formatter/actions?workflow=tox)
[![Coverage](https://codecov.io/gh/MarcoGorelli/black-tabby-formatter/branch/main/graph/badge.svg)](https://codecov.io/gh/MarcoGorelli/black-tabby-formatter)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MarcoGorelli/black-tabby-formatter/main.svg)](https://results.pre-commit.ci/latest/github/MarcoGorelli/black-tabby-formatter/main)

black-tabby-formatter
=====================

A tool (and pre-commit hook) to run `black`, but with tabs instead of spaces.

## Installation

```console
$ pip install black-tabby-formatter
```

## Usage as a pre-commit hook (recommended)

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/MarcoGorelli/black-tabby-formatter
    rev: v0.1.0
    hooks:
    -   id: black-tabby-formatter
```

## Command-line

```console
black-tabby-formatter file.py
```

To run on a directory, you can do:

```console
black-tabby-formatter `find . -name "*.py"`
```

or, using pre-commit,

```console
pre-commit try-repo https://github.com/MarcoGorelli/black-tabby-formatter
```

.

## Configuration

You can pass extra command-line flags that `black` would normally accept, such as `--check`. Furthermore, any option you specify
in `pyproject.toml` will be respected.
