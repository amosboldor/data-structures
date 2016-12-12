"""Singly-Linked List in Python."""


class LinkedList(object):
    """docstring for LinkedList."""

    def __init__(self, data=None, next_item=None):
        """Init for instance of a node."""
        self.data = data
        self.next_item = next_item
