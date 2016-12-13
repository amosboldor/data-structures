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
    linked_list = LinkedList()
    linked_list.push('1')
    linked_list.push('2')
    linked_list.push('3')
    assert linked_list.size() == 3


def test_pop():
    """Test pop method if removes the first value and return it."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push('1')
    linked_list.push('2')
    linked_list.push('3')
    popped_item = linked_list.pop()
    assert popped_item == '3'


def test_search():
    """Test search method if finds a value in linked_list."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push('1')
    linked_list.push('2')
    linked_list.push('3')
    assert linked_list.search('2').data == '2'
