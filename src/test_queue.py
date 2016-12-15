"""Test functionality of queue data structure."""

import pytest


@pytest.fixture
def new_queue():
    """Define new instance of Queue class."""
    from queue import Queue
    a_queue = Queue([1, 2, 3, 4, 5])
    return a_queue


def test_queue_creates_list_with_a_size(new_queue):
    """Test creating a new Queue, creates a list with size."""
    assert new_queue._container.size == 5


def test_data_in_queue(new_queue):
    """Test when creating a new queue, creates a list with data."""
    assert new_queue._container.head.data == 5
