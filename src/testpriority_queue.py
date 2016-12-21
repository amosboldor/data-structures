"""Tests for priority queue"""


import pytest


@pytest.fixture
def empty_priorityqueue():
    """Define new instance of PriorityQueue class"""
    from priority_queue import PriorityQueue
    return PriorityQueue()


@pytest.fixture
def full_priorityqueue():
    """Define new instance of PriorityQueue class"""
    from priority_queue import PriorityQueue
    return PriorityQueue([(100, 7), (150, 1), (200, 5), (250, 0)])