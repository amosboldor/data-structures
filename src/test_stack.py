"""Tests for stack module."""


def test_stack():
    """Test the stack class to see if it created LinkedList."""
    from stack import Stack
    stack_obj = Stack(1)
    assert stack_obj.container.head.data == 1
