"""Tests for stack module."""


def test_stack():
    """Test the stack class to see if it created LinkedList."""
    from stack import Stack
    stack_obj = Stack(1)
    assert stack_obj.container.head.data == 1


def test_stack_push_data():
    """Test Stack push data."""
    from stack import Stack
    stack_obj = Stack(1)
    stack_obj.push(2)
    assert stack_obj.container.head.data == 2


def test_stack_push_new_to_old():
    """Test Stack push data new head should point to the old head."""
    from stack import Stack
    stack_obj = Stack(1)
    old = stack_obj.container.head
    stack_obj.push(2)
    assert stack_obj.container.head.next_item == old
