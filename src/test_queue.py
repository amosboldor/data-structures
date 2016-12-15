"""Test functionality of queue data structure."""

# import pytest


def test_queue_creates_list_with_a_size():
    """Test creating a new Queue, creates a list with size."""
    from queue import Queue
    new_queue = Queue([1, 2, 3, 4])
    assert new_queue._container.size == 4
