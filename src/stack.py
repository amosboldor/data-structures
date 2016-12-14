"""Implement a Stack data type in Python."""

from linked_list import LinkedList


class Stack(object):
    """Stack object for creating a stack list."""

    def __init__(self, data=None):
        """Initialize stack class."""
        self.container = LinkedList(data)

    def push(self, value):
        """Add a value to the stack."""
        self.container.push(value)

    def pop(self):
        """Remove a value from the stack and returns that value."""
        return self.container.pop()
