************
Autodoc Demo
************



The `automodule` directive takes a module filename as an argument and causes autodoc to parse that file for pydoc comments.

To learn more about this directive and its options, head to `<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>`_


===================
Invoking automodule
===================

We can invoke the automodule directive to parse any python module and display its pydoc contents.

For example, we can invoke the automodule directive to parse the module `packagename.submodule_b.b`.

Let's try it:

.. automodule:: packagename.submodule_b.b
   :members:
   :undoc-members:
   :private-members:
   :special-members:


If you don't see anything between the line "Let's try it:" above and this line, then the automodule directive is not working as expected.

----------------


Invoking specific code objects
------------------------------

You can invoke specific code objects instead of a whole module.

For example, we can specifically grab only the `add` function from the `packagename.submodule_a.a` module.

Let's try it:

.. autofunction:: packagename.submodule_a.a.add


If you don't see anything between the line "Let's try it:" above and this line, then the automodule directive is not working as expected.

----------------

Here are some other directives you can use to invoke specific code objects:

.. code-block:: rst
   :linenos:

   .. autoclass:: module.ClassName
      :members:

   .. autofunction:: function_name
   .. autodecorator:: decorator_name
   .. autodata:: data_item_name
   .. automethod:: module.Class.method
   .. autoattribute:: module.Class.attr

