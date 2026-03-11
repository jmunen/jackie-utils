# jackie_utils

A reusable Python utility library packaged with modern python standards using 'pyproject.toml',
'src/' layout, PyTest, Github Actions CI, and PyPI publishing.

## Why I built this

I built this project to learn how Python code moves from local source files to a reusable,
installable package that other developers can consume through PyPI.

The project focuses on:
- modern Python packaging
- clean 'src/'-based project structure
- automated testing with PyTest
- CI validation with GitHub Actions
- distribution through PyPI

## Features

- 'moving_average(values, window)' for simple rolling-average calculations
- 'list_files(directory)' for listing file paths in a directory

## Installation

```bash
pip install jackie-utils