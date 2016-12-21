"""Implement a Priority Queue data type in python."""


class PriorityQueue(object):
    """Datastructure to organize members by their priority (index 1 of tuple)

    insert(value) - Adds value to the priority queue.
    The value must be a tuple in which index 1 is the priority ranking.

    pop() - removes the most prioritized tuple and returns the value (at index 0) from the tuple.

    peek() - returns the value at index 0 of the prioritized tuple without removing it.
    """

    def __init__(self, tuples=None):
        """Creates an instance of a PriorityQueue object."""
        self.tuples = []
        if isinstance(tuples, list):
            for tup in tuples:
                self.insert(tup)
        elif tuples is not None:
            raise ValueError("PriorityQueue class must be instantiated with a list object.")


    def insert(self, value):
        """Adds a tuple to the priority queue with a default priority of 0."""
        pass


    def pop(self):
        """removes the tuple with the highest priority from the queue and
        returns the value (at index 0)."""
        pass


    def peek(self):
        """returns the value of the tuple with the highest priority, but doesn't remove it."""
        pass
