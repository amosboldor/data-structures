"""Class containing a directional graph datatype."""


class Graph(object):
    """
    A graph containing nodes and single-directional edges between them.

    nodes(): return a list of all nodes in the graph

    edges(): return a list of all eduges in the graph

    add_node(node): adds a new node 'node' to the graph

    add_edge(node1, node2): adds a new edge to the graph connecting 'node1' and 'node2',
    if either node1 or node2 are not already present in the graph, they should be added.

    del_node(node): deletes the node 'node' from the graph, raises an error if no such node exists.

    del_edge(node1, node2): deletes the edge connecting 'node1' and 'node2' from the graph,
    raises an error if no such edge exists

    has_node(node): True if node 'node' is contained in the graph, False if not.

    neighbors(node): returns the list of all nodes connected to 'node' by edges,
    raises error if n is not in graph

    adjacent(node1, node2): returns True if there is an edge connecting node1 and node2,
    False if not, raises an error if either of the supplied nodes are not in graph
    """

    def __init__(self):
        """Creates a new instance of a directional graph."""
        pass

    def nodes(self):
        """returns a list of all nodes in the graph."""
        pass

    def edges(self):
        """returns a list of all the edges in the graph."""
        pass

    def add_node(self, node):
        """adds a new node to the graph."""
        pass

    def add_edge(self, node1, node2):
        """adds an edge between two nodes, adding the nodes too if they don't exist."""
        pass

    def del_node(self, node):
        """deletes a node from the graph and all edges associated with that node."""
        pass

    def del_edge(self, node1, node2):
        """deltes an edge from the graph."""
        pass

    def has_node(self, node):
        """returns True if specified node exists, and False if it doesn't."""
        pass

    def neighbors(self, node):
        """returns the list of all nodes connected to specified node by edges,
        or raises an error if node doesn't exist."""
        pass

    def adjacent(self, node1, node2):
        """returns True if there is exactly one degree of separation between two nodes."""
        pass
