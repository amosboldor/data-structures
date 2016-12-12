"""Singly-Linked List in Python."""


class Node(object):
    """docstring for LinkedList."""

    def __init__(self, data=None, next_item=None):
        """Init for instance of a node."""
        self.data = data
        self.next_item = next_item

    def update_next(self, new_node):
        """Update the next item in linked list."""
        self.next_item = new_node


class LinkedList(object):
    """Class for head of Linked List."""

    def __init__(self, head=None):
        """Initialize the head node."""
        self.head = head

    def push(self, data=None):
        """Create new node in front of head."""
        new_head = Node(data)
        new_head.update_next(self.head)
        self.head = new_head
