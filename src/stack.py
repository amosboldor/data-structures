"""Implement a Stack data type in Python."""

from linked_list import LinkedList


class Stack(object):
    """Stack object for creating a stack list.

    push(value) - Adds a value to the stack.
    The parameter is the value to be added to the stack.

    pop() - Removes a value from the stack and returns that value.
    If the stack is empty, attempts to call pop should raise an exception.
    """

    def __init__(self, data=None):
        """Initialize stack class."""
        self._container = LinkedList(data)

    def push(self, value):
        """Add a value to the stack."""
        return self._container.push(value)

    def pop(self):
        """Remove a value from the stack and returns that value."""
        return self._container.pop()
