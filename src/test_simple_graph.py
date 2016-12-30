"""Tests methods on a directional graph data structure."""


import pytest


@pytest.fixture
def empty_graph():
    """Creates a graph containing no nodes and no edges"""
    from simple_graph import Graph
    return Graph()
