"""Tests for priority queue."""


import pytest


@pytest.fixture
def empty_priorityqueue():
    """Define new instance of PriorityQueue class."""
    from priority_queue import PriorityQueue
    return PriorityQueue()


@pytest.fixture
def full_priorityqueue():
    """Define new instance of PriorityQueue class."""
    from priority_queue import PriorityQueue
    return PriorityQueue([(100, 7), (150, 1), (200, 5), (250, 0)])


def test_insert_in_empty_priorityqueue(empty_priorityqueue):
    """Test insert on empty queue without priority."""
    epq = empty_priorityqueue()
    epq.insert(123)
    assert epq.tuple[0] == (123, 0)


def test_insert_in_empty_priorityqueue_with_priority(empty_priorityqueue):
    """Test insert on empty queue with priority."""
    epq = empty_priorityqueue()
    epq.insert(123, 4)
    assert epq.tuple[0] == (123, 4)


def test_insert_in_full_priorityqueue(full_priorityqueue):
    """Test insert on full queue without priority."""
    fpq = full_priorityqueue()
    fpq.insert(123)
    assert (123, 0) in fpq.tuple


def test_insert_in_full_priorityqueue_with_priority(full_priorityqueue):
    """Test insert on full queue with priority."""
    fpq = full_priorityqueue()
    fpq.insert(123, 4)
    assert (123, 4) in fpq.tuple
