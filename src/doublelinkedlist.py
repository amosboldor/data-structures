"""Double Linked List implementation."""


class Node(object):
    """Make new data node."""

    def __init__(self, data=None, next_item=None, prev_item=None):
        """Initialize Node class with arguments."""
        self.data = data
        self.next_item = next_item
        self.prev_item = prev_item


class DoubleLinkedList(object):
    """DoubleLinkedList class.

    push(val):
    will insert the value val at the head of the list.
    append(val):
    will append the value val at the tail of the list.
    pop():
    will pop the first value off the head of the list and return it.
    shift():
    will remove the last value from the tail of the list and return it.
    remove(val):
    will remove the first instance of val found in the list,
    starting from the head. If val is not present, it will raise an
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
        old_head_data = self.head.data
        if new_head:
            new_head.prev_item = None
        self.head = new_head
        self.size -= 1
        if self.size < 1:
            self.tail = None
        return old_head_data

    def shift(self):
        """Take the first value off the tail of the list and return it."""
        if self.tail is None:
            raise IndexError('Cannot shift from an empty list.')
        new_tail = self.tail.prev_item
        old_tail_data = self.tail.data
        if new_tail:
            self.tail.next_item = None
        self.tail = new_tail
        self.size -= 1
        if self.size < 1:
            self.head = None
        return old_tail_data

    def remove(self, val):
        """Remove a given val in the list."""
        curr = self.head.data
        curr_node = self.head
        try:
            while curr:
                if curr == val:
                    break
                else:
                    curr = curr_node.next_item.data
                    curr_node = curr_node.next_item
        except AttributeError:
            raise ValueError('list.remove({0}): {0} not in list.'.format(val))
        if curr is self.head.data:
            self.pop()
        elif curr is self.tail.data:
            self.shift()
        else:
            curr_node.prev_item.next_item = curr_node.next_item
            curr_node.next_item.prev_item = curr_node.prev_item
            self.size -= 1
