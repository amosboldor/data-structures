"""Test LinkedList class."""

import pytest


LIST_DATA = [
    ['string'],
    [123],
    [[]],
    [{}]
]

DATA = [
    [1, 1],
    [[1, 2, 3], 3],
    ['string', 'g']
]


@pytest.mark.parametrize("n", LIST_DATA)
def test_initiate_node(n):
    """Test if attributes in node class match what is expected."""
    from linked_list import Node
    assert Node(n).data == n


@pytest.mark.parametrize("n, result", DATA)
def test_initiate_linkedlist(n, result):
    """Test if linked list is initiated for iterable or not."""
    from linked_list import LinkedList
    linked_list = LinkedList(n)
    assert linked_list.head.data == result


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
    """Test search method if finds a value in linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push('1')
    linked_list.push('2')
    linked_list.push('3')
    assert linked_list.search('2').data == '2'


def test_remove_tail():
    """Test if remove method removes last node from linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    to_remove = linked_list.search(2)
    linked_list.remove(to_remove)
    assert linked_list.size() == 2


def test_remove_middle():
    """Test if remove method removes middle node from linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    to_remove = linked_list.search(2)
    linked_list.remove(to_remove)
    assert linked_list.size() == 2


def test_remove_middle_head():
    """Test if remove method removes head node from linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    to_remove = linked_list.search(2)
    linked_list.remove(to_remove)
    assert linked_list.size() == 2


def test_display():
    """Test of display returns data from linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push('1')
    linked_list.push('2')
    linked_list.push('3')
    assert linked_list.display() == '(3, 2, 1)'
