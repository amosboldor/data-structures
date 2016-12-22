"""Implement a Priority Queue data type in python."""


from bin_heap import BinHeap


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
        self.prior_heap = BinHeap()
        if isinstance(tuples, list):
            for tup in tuples:
                self.insert(tup)
        elif tuples is not None:
            raise ValueError("PriorityQueue class must be instantiated with a list object.")


    def insert(self, tup):
        """Adds a tuple to the priority queue with a default priority of 0."""
        self.tuples.append(tup)
        self.prior_heap.push(tup[1])


    def pop(self):
        """removes the tuple with the highest priority from the queue and
        returns the value (at index 0)."""
        prior = self.prior_heap.pop()
        for tup in self.tuples:
            if tup[1] == prior:
                self.tuples.remove(tup)
                return tup[0]


    def peek(self):
        """returns the value of the tuple with the highest priority, but doesn't remove it."""
        prior = self.prior_heap.pop()
        for tup in self.tuples:
            if tup[1] == prior:
                return tup[0]
