"""Double Linked List implementation."""


class Node(object):
    """Make new data node."""

    def __init__(self, data=None, next_item=None, prev_item=None):
        """Initialize Node class with arguments."""
        self.data = data
        self.next_item = next_item
        self.prev_item = prev_item


class DoubleLinkedList(object):
    """DoubleLinkedList class."""

    def __init__(self, data=None):
        """Initialize DoubleLinkedList class with arguments."""
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            try:
                for item in data:
                    self.push(item)
            except TypeError:
                self.head = Node(data)

    def push(self, val):
        """Push a node in initialized Double Linked List."""
        new_node = Node(val, next_item=self.head)
        if self.size < 1:
            self.tail = new_node
        else:
            self.head.prev_item = new_node
        self.head = new_node
        self.size += 1
