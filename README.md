# sample-python-project-structure

For python applications with internal packages.

This was adapted from <https://realpython.com/python-application-layouts/> and extended in a number of ways, including:

- src layout instead of a flat layout — see [here](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) and [here](https://www.b-list.org/weblog/2023/dec/15/python-packaging-src-layout/)
- pytest for testing
- pyproject.toml for project configuration
- vscode workspace settings
- vscode workspace extensions
- sphinx for documentation

## Steps after cloning

### 1. Create a virtual environment

```bash
python -m venv venv
```

Install the dependencies from pyproject.toml

```bash
python -m pip install -e .
```

Optionally, you may also install the development dependencies

```bash
python -m pip install -e .[dev]
```

#### Note to future self: Why `venv` over other tools?

I've decided go with `venv` instead of `virtualenv` (or any other similar tool) because it's included in the standard library.
For a good run-down of these tools, see this stackoverflow thread:
[What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrapper).
I've also considered `poetry`, but it seems overkill, and to be perfectly honest I still don't understand what problem it's trying to solve.

### 2. Install vscode extensions

Install the workspace recommended extensions listed in `.vscode/extensions.json`.

Additionally, you may want to install some of the following extensions:

#### To help you write documentation

- Paste image from clipboard: `mushan.vscode-paste-image`
- Markdown formatting: `yzhang.markdown-all-in-one`
- Markdown linting: `DavidAnson.vscode-markdownlint`
- Markdown emoji support: `bierner.markdown-emoji`
- reStructuredText support: `lextudio.restructuredtext`

## What is pyproject.toml?

As of PEP 517/518, the `pyproject.toml` file is the new unified Python project settings file.
It is a configuration file that allows you to specify the build system, dependencies, and other project metadata.

In most projects, the `pyproject.toml` file entirely replaces `setup.py` and `requirements.txt`.

For more info, see:

- [What the heck is pyproject.toml?](https://snarky.ca/what-the-heck-is-pyproject-toml/) by Brett Cannon
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6) by Chad Smith
- [What is pyproject.toml file for?](https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for) on stackoverflow
- [Python Packaging User Guide: Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) on Python.org

### You may still need setup.py

If you wish to use `pip install --editable` and your project is not [PEP 660](https://peps.python.org/pep-0660/) compliant, then you still need a minimal `setup.py` file:

```python
#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup()
```

We can refer to this `setup.py` file as a _shim_, because it is providing a minimal and temporary compatibility layer that allows the use of `setuptools` in conjunction with modern PEP 517/518 build systems.

Read more at <https://stackoverflow.com/a/69711730>

### You may still need requirements.txt

If you need compatibility with tools expecting requirements.txt or want to ensure exact environment replication, maintaining both files might be necessary.

You can generate a `requirements.txt` file from the `pyproject.toml` by using the `pip-compile` tool.

## Docs

I recommend using Sphinx.
To get started, navigate to the `docs` directory and run `sphinx-quickstart`.
This will create the necessary files and directory structure.

You will be faced with the choice of separating the source and build directories.
If you do so, you'll place your markdown and/or reStructuredText files in the source directory.
The build directory will contain the generated HTML files.

For more info, see <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-quickstart.html>
