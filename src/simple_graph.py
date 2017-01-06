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

    depth_first_traversal(start): creates a path of nodes that stem out from the start node,
    completing each branch before continuing to the next.

    breadth_first_traversal(start): creates a path of nodes that stem out from the start node,
    traversing each branch at once.
    """

    def __init__(self):
        """Creates a new instance of a directional graph."""
        self._nodes = {}

    def nodes(self):
        """returns a list of all nodes in the graph."""
        return list(self._nodes.keys())

    def edges(self):
        """returns a list of all the edges in the graph."""
        edges = []
        for key in self._nodes:
            for node in self._nodes[key]:
                edges.append((key, node[0], node[1]))
        return edges

    def add_node(self, node):
        """adds a new node to the graph."""
        self._nodes[node] = []

    def add_edge(self, node1, node2, weight=1):
        """adds an edge from node1 to node2,
        adding the nodes to the dictionary if they don't exist."""
        self._nodes.setdefault(node1, [])
        self._nodes.setdefault(node2, [])
        for node_and_weight in self._nodes[node1]:
            if node2 == node_and_weight[0]:
                self._nodes[node1].remove(node_and_weight)
        self._nodes[node1].append((node2, weight))

    def del_node(self, node):
        """deletes a node from the graph and all edges associated with that node."""
        del self._nodes[node]
        for key in self._nodes:
            for item in self._nodes[key]:
                if node == item[0]:
                    self._nodes[key].remove(item)

    def del_edge(self, node1, node2):
        """deltes an edge from the graph."""
        deleted = False
        for node in self._nodes[node1]:
            if node2 == node[0]:
                deleted = True
                self._nodes[node1].remove(node)
        if not deleted:
            raise ValueError

    def has_node(self, node):
        """returns True if specified node exists, and False if it doesn't."""
        return node in self._nodes

    def neighbors(self, node):
        """returns the list of all nodes connected to specified node by edges,
        or raises an error if node doesn't exist."""
        return self._nodes[node]

    def adjacent(self, node1, node2):
        """returns True if there is exactly one degree of separation between two nodes."""
        if node1 not in self._nodes or node2 not in self._nodes:
            raise KeyError()
        for node_and_weight in self.neighbors(node1):
            if node_and_weight[0] == node2:
                return True
        return False

    def depth_first_traversal(self, start, prev=None):
        """returns a list containing the nodes of the graph in order of depth-first traversal."""
        if prev is None:
            prev = []
        if start in prev:
            return []
        lst = [start]
        nodes = self._nodes[start[0]]
        prev.append(start)
        for node in nodes:
            lst.extend(self.depth_first_traversal(node, prev))
        return lst

    def breadth_first_traversal(self, parent, prev=None):
        """returns a list containing the nodes of the graph in order of breadth-first traversal."""
        if prev is None:
            prev = []
        if not isinstance(parent, list):
            prev.append(parent)
            parent = [parent]
        children = []
        for item in parent:
            for edge in self._nodes[item[0]]:
                if edge not in prev:
                    children.append(edge)
        prev.extend(children)
        if len(children) == 0:
            return prev
        return self.breadth_first_traversal(children, prev)


if __name__ == "__main__":
    import timeit
    graph = Graph()
    for i in range(4):
        for ind in range(10 ** i, 10 ** (i + 1)):
            graph.add_edge(ind // 10, ind)

    other_graph = Graph()
    for i in range(14):
        for ind in range(2 ** i, 2 ** (i + 1)):
            other_graph.add_edge(ind // 2, ind)

    def time_depth_trav_bin():
        return other_graph.depth_first_traversal(0)

    def time_breadth_trav_bin():
        return other_graph.breadth_first_traversal(0)

    def time_depth_trav_dec():
        return graph.depth_first_traversal(0)

    def time_breadth_trav_dec():
        return graph.breadth_first_traversal(0)

    print("Depth First Binary", timeit.repeat(
        stmt="time_depth_trav_bin()",
        setup="from __main__ import time_depth_trav_bin, other_graph",
        number=1,
        repeat=3
    ))

    print("Breadth First Binary", timeit.repeat(
        stmt="time_breadth_trav_bin()",
        setup="from __main__ import time_breadth_trav_bin, other_graph",
        number=1,
        repeat=3
    ))

    print("Depth First Decimal", timeit.repeat(
        stmt="time_depth_trav_dec()",
        setup="from __main__ import time_depth_trav_dec, other_graph",
        number=1,
        repeat=3
    ))

    print("Breadth First Decimal", timeit.repeat(
        stmt="time_breadth_trav_dec()",
        setup="from __main__ import time_breadth_trav_dec, other_graph",
        number=1,
        repeat=3
    ))
