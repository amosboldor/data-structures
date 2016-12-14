"""Double Linked List implementation."""


class Node(object):
    """Make new data node."""

    def __init__(self, data, next_item, prev_item):
        """Initialize Node with arguments."""
        self.data = data
        self.next_item = next_item
        self.prev_item = prev_item
