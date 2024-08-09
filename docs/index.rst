.. packagename documentation master file, created by
   sphinx-quickstart on Fri Aug  2 13:19:41 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

packagename documentation
=========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

Version: |release|

The paired pipe symbols ``|`` in the source code here are a variable replacement mechanism. So, ``|release|`` will be replaced with the value of the `release` variable in your `conf.py` file.

Your index.rst file should include a table of contents directive, aka a toctree:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   submodule_a.rst
   submodule_b.rst
   autodoc_demo.rst

A couple of things to note about the toctree:

- The ``caption`` option just lets you replace "Contents:" (default) with whatever you wish, e.g. "My Wacky Contents:"
- The ``maxdepth`` option specifies how deep to display the toctree. If = 2, you'll see two levels of headers (i.e. title and section, but no sub- or sub-subsection headers).
- When listing out the contents, for example ``submodule_a.rst``, use the path to file relative to the index.rst file. The file extension is optional, but I like to include it for clarity.
