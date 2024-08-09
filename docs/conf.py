# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import imp
from datetime import datetime


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "packagename"
author = "John Smith"

# This bit of code is used to dynamically set the copyright string
year = datetime.now().year
if year > 2024:
    copyright = f"2024-{year}, {author}"
else:
    copyright = f"2024, {author}"

# This bit of code is used to dynamically set the version number, so that it only needs to be updated in one place (the __init__.py file)
mod = imp.load_source("packagename", "../src/packagename/__init__.py")
release = mod.__version__
# This `release` variable can be called as a variable in the documentation by using the pipe character, like so: |release|


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# If you're using autodoc, make sure to add it to the extensions list:
extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# You can use the sphinx-rtd-theme (for the HTML output) by pip installing sphinx-rtd-theme it and adding it to the html_theme variable below:
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
