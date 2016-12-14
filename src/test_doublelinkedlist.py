"""Tests for double linked list class."""

import pytest

ITER_TABLE = [
    [[1, 2, 3]],
    ["Hello"],
    [("a", "b", "c")],
    [{"one": 1, "two": 2}]
]


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


def test_new_list_has_zero_size(new_list):
    """When I make a new linked list its size is zero."""
    assert new_list.size == 0


def test_when_push_new_head_points_to_old_head(new_list):
    """When I push, my new head's next points to the old head."""
    new_list.push(1)
    old = new_list.head
    new_list.push(2)
    assert new_list.head.next_item is old


def test_when_push_old_head_prev_item_is_new_head(new_list):
    """When I push, my old heads prev points to the new head."""
    new_list.push(1)
    old = new_list.head
    new_list.push(2)
    assert old.prev_item is new_list.head


@pytest.mark.parametrize("my_iter", ITER_TABLE)
def test_when_initialize_with_iterable_makes_nodes(my_iter):
    """When I pass an iterable on initialization I make nodes out of it."""
    from doublelinkedlist import DoubleLinkedList
    dll = DoubleLinkedList(my_iter)
    assert dll.size == len(my_iter)


def test_when_initialize_with_single_value_size_is_1():
    """Test when double linked list is initialised it creates one node."""
    from doublelinkedlist import DoubleLinkedList
    dll = DoubleLinkedList(1)
    assert dll.size == 1
    assert dll.head == dll.tail
