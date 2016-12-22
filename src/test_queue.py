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
    assert new_queue._size == 5


def test_data_in_queue(new_queue):
    """Test when creating a new queue, creates a queue with data."""
    assert new_queue._container.head.data == 5


def test_when_enqueue_list_size_grows(new_queue):
    """When I enqueue, the size of the queue grows."""
    new_queue.enqueue(5)
    assert new_queue._size == 6


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
    with pytest.raises(IndexError,
                       message="Cannot remove a node from an empty list."):
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
    assert new_queue.dequeue() == 5


def test_peek_size(new_queue):
    """When peek runs size should stay the same."""
    list_size = new_queue._size
    new_queue.peek()
    assert new_queue._size == list_size


def test_peek_returns_data_at_head(new_queue):
    """When peek runs it returns the data at the head."""
    assert new_queue.peek() == new_queue._container.head.data


def test_peek_on_empty_queue_returns_none():
    """When peek runs on an empty queue it returns None."""
    from queue import Queue
    assert Queue().peek() is None


def test_size_empty_queue():
    """Test that the size returns 0 if queue has nothing."""
    from queue import Queue
    assert Queue().size() == 0


def test_size_full_queue(new_queue):
    """Test that size of queue initialized with length of 5 is 5."""
    assert new_queue.size() == 5


def test_size_full_queue_after_dequeue(new_queue):
    """Test size of queue of 5 dequeued twice and enqueued once is 4."""
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.enqueue(3)
    assert new_queue.size() == 4


def test_dequeue_on_queue_of_one():
    """Test dequeue on queue of 1."""
    from queue import Queue
    queue = Queue(5)
    queue.dequeue()
    assert queue._size == 0
