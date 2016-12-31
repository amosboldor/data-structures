"""Tests methods on a directional graph data structure."""


import pytest


@pytest.fixture
def empty_graph():
    """Create a graph containing no nodes and no edges."""
    from simple_graph import Graph
    return Graph()


@pytest.fixture
def full_node_graph():
    """Create a graph with nodes but no edges."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('A')
    graph.add_node('Hello My Name is Bob')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node(2)
    graph.add_node('D')
    graph.add_node(3.5)
    graph.add_node('E')
    return graph


@pytest.fixture
def full_edges_graph():
    """Create a graph with nodes and edges."""
    graph = full_node_graph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'A')
    graph.add_edge('A', 2)
    graph.add_edge(3.5, 2)
    graph.add_edge('Hello My Name is Bob', 'A')
    return graph


def test_empty_graph(empty_graph):
    """Test empty graph as empty dictionary."""
    assert len(empty_graph._nodes) == 0


def test_adding_node_to_full_graph(full_node_graph):
    """Test adding a node to full graph."""
    assert len(full_node_graph._nodes) == 8


def test_nodes_method_on_empty_graph(empty_graph):
    """Test nodes methods returns empty list."""
    assert empty_graph.nodes() == []


def test_nodes_method_returns_list(full_node_graph):
    """Test that nodes method returns list of edges."""
    graph = full_node_graph.nodes()
    for node in range(len(graph)):
        graph[node] = str(graph[node])
    assert sorted(graph) == ['2', '3.5', 'A', 'B', 'C', 'D', 'E', 'Hello My Name is Bob']


def test_add_edge_method_on_empty_list(empty_graph):
    """Test that adding and edge on empty list creates the nodes and the edge."""
    empty_graph.add_edge('A', 'B')
    assert empty_graph._nodes['A'] == ['B'] and empty_graph._nodes['B'] == []


def test_add_edge_method_on_full_node_graph(full_node_graph):
    """Test that add_edge on graph full of nodes."""
    full_node_graph.add_edge('B', 'C')
    assert full_node_graph._nodes['B'] == ['C'] and full_node_graph._nodes['C'] == []


def test_add_edge_method_on_full_node_graph_existing_node(full_node_graph):
    """Test that add_edge on graph full of nodes one of the nodes exists."""
    full_node_graph.add_edge('A', 'S')
    assert full_node_graph._nodes['A'] == ['S'] and full_node_graph._nodes['S'] == []


def test_add_edge_method_on_full_node_graph_existing_node_reverse(full_node_graph):
    """Test that add_edge on graph full of nodes one of the nodes exists."""
    full_node_graph.add_edge('S', 'A')
    assert full_node_graph._nodes['S'] == ['A'] and full_node_graph._nodes['A'] == []


def test_edges_empty_graph(empty_graph):
    """Test that edges() method on an empty graph returns an empty list."""
    assert empty_graph.edges() == []


def test_edges_full_graph(full_edges_graph):
    """Test that edges() method on a graph with edges returns the proper list of edges."""
    graph = full_edges_graph.edges()
    for edge in range(len(graph)):
        graph[edge] = str(graph[edge])
    assert sorted(graph) == sorted(["('A', 'B')", "('B', 'A')", "('A', 2)", "(3.5, 2)", "('Hello My Name is Bob', 'A')"])


def test_edges_duplicates(full_edges_graph):
    """Test that adding edges that already exist does not create duplicates."""
    full_edges_graph.add_edge('A', 'B')
    graph = full_edges_graph.edges()
    for edge in range(len(graph)):
        graph[edge] = str(graph[edge])
    assert sorted(graph) == sorted(["('A', 'B')", "('B', 'A')", "('A', 2)", "(3.5, 2)", "('Hello My Name is Bob', 'A')"])


def test_delete_node_empty(empty_graph):
    """Test that deleting a node from an empty graph throws an error."""
    with pytest.raises(KeyError):
        empty_graph.del_node('A')


def test_delete_missing_node_full(full_node_graph):
    """Test that deleting a node that doesn't exist throws an error."""
    with pytest.raises(KeyError):
        full_node_graph.del_node('blargh')


def test_delete_node_full(full_node_graph):
    """Test that deleting a node that exists from a graph removes the node."""
    full_node_graph.del_node('A')
    graph = full_node_graph.nodes()
    for node in range(len(graph)):
        graph[node] = str(graph[node])
    assert sorted(graph) == ['2', '3.5', 'B', 'C', 'D', 'E', 'Hello My Name is Bob']


def test_delete_edge_method_on_empty(empty_graph):
    """Test that deleting and edge on empty list raises error."""
    with pytest.raises(KeyError):
        empty_graph.del_edge(1, 2)


def test_delete_edge_method_on_full_graph_on_non_existing_edge1(full_edges_graph):
    """Test that deleting a non-existing edge on a full list raises error."""
    with pytest.raises(ValueError):
        full_edges_graph.del_edge("A", "Dole")


def test_delete_edge_method_on_full_graph_on_non_existing_edge2(full_edges_graph):
    """Test that deleting a non-existing edge on a full list raises error."""
    with pytest.raises(KeyError):
        full_edges_graph.del_edge("Bob", "Dole")


def test_delete_edge_on_full_graph(full_edges_graph):
    """Test that deleting an edge from an existing node."""
    full_edges_graph.del_edge('A', 'B')
    graph = full_edges_graph.edges()
    for edge in range(len(graph)):
        graph[edge] = str(graph[edge])
    assert sorted(graph) == sorted(["('B', 'A')", "('A', 2)", "(3.5, 2)", "('Hello My Name is Bob', 'A')"])


def test_has_node_method_false(full_node_graph):
    """Test has_node method with non-existing node."""
    assert full_node_graph.has_node('BOB') is False


def test_has_node_method_true(full_node_graph):
    """Test has_node method with existing node."""
    assert full_node_graph.has_node('A') is True
