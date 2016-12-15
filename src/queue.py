"""mplementation of a queue list."""


from doublelinkedlist import DoubleLinkedList


class Queue():
    """Class for queue.

    enqueue(value): adds value to the queue
    dequeue(): removes the correct item from the queue and
    returns its value (should raise an error if the queue is empty)

    peek(): returns the next value in the queue without dequeueing it.
    If the queue is empty, returns None

    size(): return the size of the queue.
    Should return 0 if the queue is empty.
    """

    def __init__(self, data=None):
        """Initialization of queue."""
        self._container = DoubleLinkedList(data)
        self._size = self._container.size

    def enqueue(self, val):
        """Add a value to the end of the queue."""
        return self._container.append(val)

    def dequeue(self):
        """Remove a value off the head of the queue."""
        return self._container.pop()

    def peek(self):
        """Return the next value in the queue."""
        return self._container.head.data
