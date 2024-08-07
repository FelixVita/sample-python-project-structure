************
Autodoc Demo
************


The `automodule` directive takes a module filename as an argument and causes autodoc to parse that file for pydoc comments.

To learn more about this directive and its options, head to <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>

Let's try to invoke it below:

.. automodule:: projectname.submodule_a



Rather than include a whole module, you can explicitly include a code thing:

.. code-block:: rst
   :linenos:

   .. autoclass:: module.ClassName
      :members:

   .. autofunction:: function_name
   .. autodecorator:: decorator_name
   .. autodata:: data_item_name
   .. automethod:: module.Class.method
   .. autoattribute:: module.Class.attr
