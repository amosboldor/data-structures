"""Test functionality of queue data structure."""

import pytest


@pytest.fixture
def new_queue():
    """Define new instance of Queue class."""
    from queue import Queue
    a_queue = Queue([1, 2, 3, 4, 5])
    return a_queue


def test_queue_creates_list_with_a_size(new_queue):
    """Test creating a new Queue, creates a queue with size."""
    assert new_queue._container.size == 5


def test_data_in_queue(new_queue):
    """Test when creating a new queue, creates a queue with data."""
    assert new_queue._container.head.data == 5


def test_when_enqueue_list_size_grows(new_queue):
    """When I enqueue, the size of the queue grows."""
    new_queue.enqueue(5)
    assert new_queue._container.size == 6


def test_when_append_new_tail_points_to_old_tail(new_queue):
    """When I enqueue, my new tail's next points to the old tail."""
    new_queue.enqueue(1)
    old = new_queue._container.tail
    new_queue.enqueue(2)
    assert new_queue._container.tail.prev_item is old


def test_when_enqueue_old_tail_next_item_is_new_tail(new_queue):
    """When I enqueue, my old tails next points to the new tail."""
    new_queue.enqueue(1)
    old = new_queue._container.tail
    new_queue.enqueue(2)
    assert old.next_item is new_queue._container.tail


def test_when_pop_on_empty_list_raise_indexerr():
    """When I dequeue from empty queue, raise IndexError."""
    from queue import Queue
    with pytest.raises(IndexError, message="Cannot pop from an empty list."):
        Queue().dequeue()


def test_when_dequeue_new_head_is_old_head_next(new_queue):
    """When I dequeue new head is old head next."""
    old_head = new_queue._container.head.next_item
    new_queue.dequeue()
    assert new_queue._container.head == old_head


def test_when_dequeue_then_dequeue_returns_data(new_queue):
    """When I enqueue then dequeue from list return that data."""
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    assert new_queue.dequeue() == 1
