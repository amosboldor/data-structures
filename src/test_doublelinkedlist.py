"""Tests for double linked list class."""


def test_new_node_is_empty():
    """Test a new node is empty."""
    from doublelinkedlist import Node
    new_node = Node()
    assert new_node.data is None
    assert new_node.next_item is None
    assert new_node.prev_item is None
