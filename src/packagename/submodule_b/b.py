"""This is a module that defines a Stack class, just for demonstration purposes."""

class Stack:
    """Placeholder docstring for the Stack class."""
    def __init__(self):
        """Placeholder docstring for the __init__ method."""
        self._storage = []

    def __len__(self):
        """Placeholder docstring for the __len__ method."""
        return len(self._storage)

    def push(self, item):
        """Placeholder docstring for the push method."""
        self._storage.append(item)

    def pop(self):
        """Placeholder docstring for the pop method."""
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item
