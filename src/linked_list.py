"""Singly-Linked List in Python."""


class Node(object):
    """docstring for LinkedList."""

    def __init__(self, data, next_item=None):
        """Init for instance of a node."""
        self.data = data
        self.next_item = next_item


class LinkedList(object):
    """Class for head of Linked List."""

    def __init__(self, data=None):
        """Initialize the head node."""
        self.head = None
        if data:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item)
                    else:
                        self.head = Node(item, self.head)
            except TypeError:
                self.head = Node(data)

    def push(self, data=None):
        """Create new node in front of head."""
        new_head = Node(data)
        new_head.next_item = self.head
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
        curr = self.head
        result = None
        while val != curr.data:
            curr = curr.next_item
        else:
            result = curr
        return result

    def remove(self, node):
        """Remove a given node in the list."""
        curr = self.head
        previous = None
        while curr:
            if curr == node:
                break
            previous = curr
            curr = previous.next_item
        if previous is None:
            self.head = curr.next_item
        else:
            previous.next_item = curr.next_item

    def display(self):
        """Return a string of the linked list."""
        return_tuple = '('
        curr = self.head
        while curr:
            return_tuple = return_tuple + str(curr.data) + ', '
            curr = curr.next_item
        return return_tuple[:-2] + ')'
