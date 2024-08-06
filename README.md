# sample-python-project-structure

For python applications with internal packages.

This was adapted from <https://realpython.com/python-application-layouts/> and extended in a number of ways, including:

- src layout instead of a flat layout — see [here](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) and [here](https://www.b-list.org/weblog/2023/dec/15/python-packaging-src-layout/)
- pytest for testing
- pyproject.toml for project configuration
- vscode workspace settings
- vscode workspace extensions
- sphinx for documentation

Several ideas were also borrowed from <https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510?permalink_comment_id=4974632> such as

- notebooks dir
- data dir
- scripts dir

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

#### Note to future self 1: Why `venv` over other tools?

I've decided go with `venv` instead of `virtualenv` (or any other similar tool) because it's included in the standard library.
For a good run-down of these tools, see this stackoverflow thread:
[What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrapper).
I've also considered `poetry`, but it seems overkill, and to be perfectly honest I still don't understand what problem it's trying to solve.

#### Note to future self 2: How is `python -m pip install -e .` different from `python -m pip install -r requirements.txt`?

First of all, we're not using `requirements.txt` anymore.
We're instead following the new PEP 517/518 standard and using `pyproject.toml` for project configuration.

The normal way to install dependencies from `pyproject.toml` is to run `python -m pip install .`.

However, we're using the `-e` flag, which is shorthand for `--editable`.

Using the command `python -m pip install -e .` means that all dependencies will still be installed the normal way, except your own package, which will now instead be installed in "editable" mode.
This means that any changes you make to your own source code will be immediately reflected, without having to re-install your own package with pip every time you make a change.

The rationale for installing your own package into the environment (rather than just using the source code directly) is that it gives you a way to test it in the same way that your users will be installing it and running it.

For more info, I recommend watching [this video](https://www.youtube.com/watch?v=QMY-OkckDwo)

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

> Tip: If this fails (for example due to Microsoft ASR blocking .exe files and causing an "Access is denied" error), then you can instead try to run `python -m sphinx.cmd.quickstart`. According to a [post on StackOverflow](https://stackoverflow.com/a/46507300), this  explicitly loads Sphinx's quickstart module.

You will be faced with the choice of separating the source and build directories.
If you do so, you'll place your markdown and/or reStructuredText files in the source directory.
The build directory will contain the generated HTML files.

When prompted about the "Project release", if you don't know what to write, then you can just type something like `0.0.1`

For more info, see <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-quickstart.html>

Alternatively, you can watch the Real Python tutorial video series [Documenting Python Projects With Sphinx and Read the Docs](https://realpython.com/lessons/sphinx-basics-python/)

To build the documentation on Windows, run

```bash
.\make html
```

## Testing

This project uses `pytest` for testing.

To run the tests either use the built-in vscode "Testing" pane, or simply open a terminal and run

```bash
python -m pytest -v
```

To see test coverage, run

```bash
python -m pytest -v --cov=src
```

In theory those two simple commands are all you need to run tests and check code coverage.

However, as a developer, especially if you're doing TDD, another important way that you'll be using tests (if not THE most important) is running tests repeatedly when writing code.
This usually involves running just one or two tests over and over again (often in debug mode), and for this I prefer to use the vscode GUI's Testing pane.
For a nice summary of what buttons to click in vscode, see vscode's officials docs: [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)

## Notebooks

This repo includes a demo of Quarto Notebooks and Jupyter Notebooks.
Feel free to have a look inside these files for more info.

Quarto is the spiritual successor to Jupyter Notebooks, and I personally prefer it, both as a prototyping tool and as a code presentation tool — i.e. both of the things that I used to use Jupyter Notebooks for.

## GitHub Actions

This repo includes a GitHub Actions workflow that runs the tests on every push and pull request.

You can find the workflow file in `.github/workflows/ci.yaml`.

This was adapted from the YouTube video [Unit testing Python code using Pytest + GitHub Actions](https://www.youtube.com/watch?v=0aEJBygCn5Q) by Carberra.
