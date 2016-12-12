"""Test LinkedList class."""

import pytest


LIST_DATA = [
    ['string'],
    [123],
    [[]],
    [{}]
]


@pytest.mark.parametrize("n", LIST_DATA)
def test_initiate_linkedlist(n):
    """Test if attributes in linked list match what is expected."""
    from linked_list import Node
    example = Node(n)
    assert example.data == n


@pytest.mark.parametrize("n", LIST_DATA)
def test_push(n):
    """Test push updates head of the linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(n)
    assert linked_list.head.data == n


def test_size():
    """Test if size returns the number of objects in list."""
    from linked_list import LinkedList
    from linked_list import Node
    node1 = Node('1')
    node2 = Node('2', node1)
    node3 = Node('3', node2)
    linked_list = LinkedList(node1)
    assert linked_list.size(node3) == 3
