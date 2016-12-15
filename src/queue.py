"""mplementation of a queue list."""


from doublelinkedlist import DoubleLinkedList


class Queue():
    """Class for queue list."""

    def __init__(self, data=None):
        """Initialization of Queue list."""
        self._container = DoubleLinkedList(data)
        self._size = self._container.size
