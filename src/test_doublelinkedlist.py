"""Tests for double linked list class."""

import pytest


@pytest.fixture
def new_list():
    """Create a new empty double linked list."""
    from doublelinkedlist import DoubleLinkedList
    this_list = DoubleLinkedList()
    return this_list


def test_new_node_is_empty():
    """Test a new node is empty."""
    from doublelinkedlist import Node
    new_node = Node()
    assert new_node.data is None
    assert new_node.next_item is None
    assert new_node.prev_item is None


def test_new_node_with_data_has_data():
    """A new node with data has data."""
    from doublelinkedlist import Node
    new_node = Node(5)
    assert new_node.data == 5


def test_new_node_with_next_has_next():
    """A new node with data and next has next and data."""
    from doublelinkedlist import Node
    node1 = Node(5)
    node3 = Node(1)
    node2 = Node(4, node1, node3)
    assert node2.next_item is node1
    assert node2.prev_item is node3


def test_new_doublelist_has_no_head(new_list):
    """A new double linked list is without a head."""
    assert new_list.head is None
    assert new_list.tail is None


def test_when_push_list_size_grows(new_list):
    """When I push to my list, the size of the list grows."""
    new_list.push(5)
    assert new_list.size == 1
