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
    from linked_list import LinkedList
    example = LinkedList(n)
    assert example.data == n
