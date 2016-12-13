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

    def pop(self):
        """Remove the first value off the head of the list and return it."""
        new_head = self.head.next_item
        old_head = self.head.data
        self.head = new_head
        return old_head


    def size(self):
        """Count the objects in linked list."""
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next_item
        return count

    def search(self, val):
        """Iterate through the linked list to find instance containing val."""
        pass
