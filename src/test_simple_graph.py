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

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'A')
    graph.add_edge('A', 2)
    graph.add_edge(3.5, 2)
    graph.add_edge('Hello My Name is Bob', 'A')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 2)
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
    assert empty_graph._nodes['A'] == [('B', 1)] and empty_graph._nodes['B'] == []


def test_add_edge_method_on_full_node_graph(full_node_graph):
    """Test that add_edge on graph full of nodes."""
    full_node_graph.add_edge('B', 'C')
    assert full_node_graph._nodes['B'] == [('C', 1)] and full_node_graph._nodes['C'] == []


def test_add_edge_method_on_full_node_graph_existing_node(full_node_graph):
    """Test that add_edge on graph full of nodes one of the nodes exists."""
    full_node_graph.add_edge('A', 'S')
    assert full_node_graph._nodes['A'] == [('S', 1)] and full_node_graph._nodes['S'] == []


def test_add_edge_method_on_full_node_graph_existing_node_reverse(full_node_graph):
    """Test that add_edge on graph full of nodes one of the nodes exists."""
    full_node_graph.add_edge('S', 'A')
    assert full_node_graph._nodes['S'] == [('A', 1)] and full_node_graph._nodes['A'] == []


def test_edges_empty_graph(empty_graph):
    """Test that edges() method on an empty graph returns an empty list."""
    assert empty_graph.edges() == []


def test_edges_full_graph(full_edges_graph):
    """Test that edges() method on a graph with edges returns the proper list of edges."""
    edges = full_edges_graph.edges()
    for ind in range(len(edges)):
        edges[ind] = str(edges[ind])
    assert sorted(edges) == sorted([
        "('A', 'B', 1)",
        "('B', 'A', 1)",
        "('A', 2, 1)",
        "(3.5, 2, 1)",
        "('Hello My Name is Bob', 'A', 1)",
        "('C', 'D', 1)",
        "('C', 'E', 1)",
        "('D', 2, 1)",
    ])


def test_edges_duplicates(full_edges_graph):
    """Test that adding edges that already exist does not create duplicates."""
    full_edges_graph.add_edge('A', 'B')
    edges = full_edges_graph.edges()
    for ind in range(len(edges)):
        edges[ind] = str(edges[ind])
    assert sorted(edges) == sorted([
        "('A', 'B', 1)",
        "('B', 'A', 1)",
        "('A', 2, 1)",
        "(3.5, 2, 1)",
        "('Hello My Name is Bob', 'A', 1)",
        "('C', 'D', 1)",
        "('C', 'E', 1)",
        "('D', 2, 1)",
    ])


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
    full_edges_graph.del_edge('A', ('B', 1))
    edges = full_edges_graph.edges()
    for ind in range(len(edges)):
        edges[ind] = str(edges[ind])
    assert sorted(edges) == sorted([
        "('B', 'A', 1)",
        "('A', 2, 1)",
        "(3.5, 2, 1)",
        "('Hello My Name is Bob', 'A', 1)",
        "('C', 'D', 1)",
        "('C', 'E', 1)",
        "('D', 2, 1)",
    ])


def test_has_node_method_false(full_node_graph):
    """Test has_node method with non-existing node."""
    assert full_node_graph.has_node('BOB') is False


def test_has_node_method_true(full_node_graph):
    """Test has_node method with existing node."""
    assert full_node_graph.has_node('A') is True


def test_neighbors_empty(empty_graph):
    """Tests that neighbors method on an empty graph throws a key error."""
    with pytest.raises(KeyError):
        empty_graph.neighbors('A')


def test_neighbors_full_node_graph(full_node_graph):
    """Tests that neighbors method on a node without edges returns an empty list."""
    assert full_node_graph.neighbors('A') == []


def test_neighbors_full_edges_graph(full_edges_graph):
    """Tests that neighbors method on a node with edges returns the correct list of edges."""
    assert full_edges_graph.neighbors('A') == [('B', 1), (2, 1)]


def test_adjacent_non_existant1(full_edges_graph):
    """Tests that finding adjacent nodes on a non-existing node throws a key error."""
    with pytest.raises(KeyError):
        full_edges_graph.adjacent('Bob', 'B')


def test_adjacent_non_existant2(full_node_graph):
    """Tests that finding non-existing nodes adjacent to an existing node throws a key error."""
    with pytest.raises(KeyError):
        full_node_graph.adjacent('A', 'Dole')


def test_adjacent_without_edges(full_edges_graph):
    """Tests that finding existing nodes that aren't connected returns False."""
    assert not full_edges_graph.adjacent('A', 'C')


def test_adjacent_with_edges(full_edges_graph):
    """Tests that finding existing nodes that are connected returns True."""
    assert full_edges_graph.adjacent('A', 2)


def test_adjacent_reverse(full_edges_graph):
    """Tests that finding existing nodes that are connected in the opposite direction
    (node2 points to node1) returns False."""
    assert not full_edges_graph.adjacent(2, 'A')


def test_depth_first_traversal(full_edges_graph):
    """Tests that depth_first_traversal function returns correct path of traversal."""
    assert full_edges_graph.depth_first_traversal(('C', 1)) == [('C', 1), ('D', 1), (2, 1), ('E', 1)]


def test_depth_first_traversal_with_loops(full_edges_graph):
    """Tests that depth_first_traversal doesn't get caught in a loop."""
    assert full_edges_graph.depth_first_traversal(('A', 1)) == [('A', 1), ('B', 1), (2, 1)]


def test_depth_first_traversal_with_bad_start(full_edges_graph):
    """Tests that depth_first_traversal throws an error if the start node isn't part of the graph."""
    with pytest.raises(KeyError):
        full_edges_graph.depth_first_traversal("blargh")


def test_depth_first_traversal_with_isolated_node(full_node_graph):
    """Tests that depth_first_traversal returns a single node if start node is isolated."""
    assert full_node_graph.depth_first_traversal('A') == ['A']


def test_breadth_first_traversal(full_edges_graph):
    """Tests that depth_first_traversal function returns corret path of traversal."""
    assert full_edges_graph.breadth_first_traversal(('C', 1)) == [('C', 1), ('D', 1), ('E', 1), (2, 1)]


def test_breadth_first_traversal_with_loops(full_edges_graph):
    """Tests that breadth_first_traversal doesn't get caught in a loop."""
    assert full_edges_graph.breadth_first_traversal(('A', 1)) == [('A', 1), ('B', 1), (2, 1)]


def test_breadth_first_traversal_with_bad_start(full_edges_graph):
    """Tests that breadth_first_traversal throws an error if the start node isn't part of the graph."""
    with pytest.raises(KeyError):
        full_edges_graph.breadth_first_traversal("blargh")


def test_breadth_first_traversal_with_isolated_node(full_node_graph):
    """Tests that breadth_first_traversal returns a single node if start node is isolated."""
    assert full_node_graph.breadth_first_traversal('A') == ['A']


def test_explicit_weight(full_edges_graph):
    """Test that add_edge with explicit weight create the correct tuple."""
    full_edges_graph.add_edge('A', 'C', weight=5)
    assert ('C', 5) in full_edges_graph._nodes['A']


def test_replace_weight(full_edges_graph):
    """Test that add_edge replaces an edge that already exist."""
    full_edges_graph.add_edge('A', 'B', weight=5)
    assert ('B', 5) in full_edges_graph._nodes['A']


def test_empty_graph_weight(empty_graph):
    """Test that add_edge with explicit weight create the correct tuple in empty graph."""
    empty_graph.add_edge('A', 'C', weight=5)
    assert ('C', 5) in empty_graph._nodes['A']
