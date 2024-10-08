*****************
Title (Asterisks)
*****************

##################
Sub-Title (Hashes)
##################

=====================
Section (Equal-Signs)
=====================

Sub-Section (Dashes)
---------------------

Heading depth is determined based on context, but being consistent is helpful.

For *italics* use one star.

For **bold** use two stars.

For ``inline code`` use two backticks.

For a horizontal separator use any punctuation in a row repeated more than 4 times (with a blank line above and below), usually dashes:

---------

List markup
-----------

* First thing
* Second thing with a line break
  and a continuation (note the indentation)


Numbered lists can either be explicit (using numbers) or implicit (using asterisks):

1. Numbered
2. Works

#. As well
#. Notice a single blank line doesn't create a new list

External Links
--------------

Visit `<www.realpython.com>`_ today!

Visit `RealPython <https://www.realpython.com>`_ today!


Creating Internal links
-----------------------

To create internal links, just write the following anywhere in an rst file:

``.. _name_of_internal_link:``

Note the syntax: Two dots followed by a space, then an underscore.
This is the syntax for creating a named reference.

Using Internal Links
---------------------

Insert a link to the named reference (can be used without :ref: if local to the file, but usually better practice to always be explicit):

:ref:`lorem-ipsum`


Show alternate text as the link instead of the link name:

:ref:`Alternate Text <lorem-ipsum>`


Directives and Comments
------------------------

A directive is a block of instructions.

* Names, arguments, options, and content.
* Code blocks, notes, warnings, and more!

.. code-block:: python
    :linenos:

    for x in range(1, 10):
        print(x)


All directives start with a double period and are marked with a double colon.

.. A directive without a double colon is treated as a comment.

A comment is a line of text that is not rendered.


Images
------

The **image** directive takes a single argument, the name of the file to be inserted.

The path is either relative to the document file the directive is in, or it can be fully qualified.


.. image:: ./images/monet_wildenstein.png
    :width: 309px
    :align: left
    :height: 208px
    :alt: Monet Wildenstein

Images can be a little tricky.
What formats they support and how sizes are treated are dependent on what the output supports.

For HTML, you can use the same kind of image formats you'd use on the Web.

Some output formats, like LaTeX, support embedding PDFs.

PDFs can be tricky when it comes to sizes, so the options specifying width and height here may or may not be effective depending on the output format.


The **figure** directive is essentially an image directive that supports captions. The content portion of the directive is where you specify the contents of the caption.

.. figure:: ./images/monet_waterloo_bridge.jpg
    :figclass: align-center

    Figures are like images with a caption


Notes and Warnings
------------------

.. note:: This is a **note** box

.. warning:: This is a **warning** box. Again, note the space between the directive and the text.

#######
Include
#######

Sphinx supports the ability to embed other files into your file using the include directive.
The options here allow you to include only a portion of the file if you wish.

==============
Normal Include
==============

Inserts a file or fragment of a file as a block.
Directive options like `start-after` and `end-before` can be used to specify  only part of a file to be included.

Example 1 (.rst)
-------------------------------

Embed a smaller part of the Lorem Ipsum text in submodule_b.rst (docs) file:

.. include:: submodule_b.rst
    :start-after: magna aliqua.
    :end-before: Duis


Example 2 (.md)
-------------------------------

Embed a smaller part of the README.md file in the root directory:

.. include:: ..\README.md
    :start-line: 0
    :end-line: 3

.. warning:: Can't see any README excerpt above?
    For most CI-based docs builds, this will indeed fail, due to the relative path being outside the docs directory.
    In general, you should probably avoid writing your docs in a way such that you are relying on any files outside the docs directory.
    If you really want to include the repo-level README, then maybe add some bash commands to your CI workflow to copy the README file into the docs dir before building, or something? Idk.

.. For more options for this directive, see https://stackoverflow.com/a/54519037

===============
Literal Include
===============

Inserts a file or fragment of a file verbatim.
Optionally add line numbers and language syntax highlighting.
Supports the partial inclusion options as above.

Example 3 (.py)
--------------------------------

Embed the entire submodule_b.py (code) file:

.. literalinclude:: ..\src\packagename\submodule_b\b.py
    :linenos:
    :language: python

.. warning:: Can't see any python code excerpt above?
    Same problem as in the previous warning box about the README file:
    Its relative path is outside the docs directory.

################
Credits
################

Most of the content in this rst file was adapted from Christopher Trudeau's
`Sphinx RST Cheat Sheet for Python Docstrings <https://trudeau.dev/cheatsheets/rst.html>`_
as featured in the RealPython course `Documenting Python Projects With Sphinx and Read the Docs <https://realpython.com/courses/python-sphinx/>`_.