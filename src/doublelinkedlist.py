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

    """
    push(val):
    will insert the value ‘val’ at the head of the list.
    append(val):
    will append the value ‘val’ at the tail of the list.
    pop():
    will pop the first value off the head of the list and return it.
    shift():
    will remove the last value from the tail of the list and return it.
    remove(val):
    will remove the first instance of ‘val’ found in the list,
    starting from the head. If ‘val’ is not present, it will raise an
    appropriate Python exception.

    """

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
                self.push(data)

    def push(self, val):
        """Push a node to the head of the DoubleLinkedList."""
        new_node = Node(val, next_item=self.head)
        if self.size < 1:
            self.tail = new_node
        else:
            self.head.prev_item = new_node
        self.head = new_node
        self.size += 1

    def append(self, val):
        """Append a node to the tail of the DoubleLinkedList."""
        new_node = Node(val, prev_item=self.tail)
        if self.size < 1:
            self.head = new_node
        else:
            self.tail.next_item = new_node
        self.tail = new_node
        self.size += 1

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.head is None:
            raise IndexError('Cannot pop from an empty list.')
        new_head = self.head.next_item
        old_head = self.head.data
        self.head = new_head
        self.head.prev_item = None
        self.size -= 1
        return old_head

    def shift(self):
        """Take the first value off the tail of the list and return it."""
        if self.tail is None:
            raise IndexError('Cannot shift from an empty list.')
        new_tail = self.tail.prev_item
        old_tail = self.tail.data
        self.tail = new_tail
        self.tail.next_item = None
        self.size -= 1
        return old_tail

    def remove(self, node):
        """Remove a given node in the list."""
        curr = self.head
        while curr:
            if curr == node:
                break
            curr = curr.next_item
        else:
            raise ValueError('list.remove(x): x not in list.')
        if curr is self.head:
            self.head = curr.next_item
            curr.prev_item = None
        elif curr is self.tail:
            self.tail = self.tail.prev_item
            curr.next_item = None
        else:
            curr.prev_item.next_item = curr.next_item
            curr.next_item.prev_item = curr.prev_item
