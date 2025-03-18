import pytest
from src.ford_fulkerson import Graph

def test_basic_max_flow():
    """
    Test a simple graph with known maximum flow
    """
    graph = Graph(4)
    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 3, 2)
    
    assert graph.ford_fulkerson(0, 3) == 5

def test_single_edge_flow():
    """
    Test a graph with a single edge
    """
    graph = Graph(2)
    graph.add_edge(0, 1, 10)
    
    assert graph.ford_fulkerson(0, 1) == 10

def test_no_flow_graph():
    """
    Test a graph with no possible flow
    """
    graph = Graph(3)
    
    assert graph.ford_fulkerson(0, 2) == 0

def test_complex_max_flow():
    """
    Test a more complex graph with multiple paths
    """
    graph = Graph(6)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 10)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 4)
    graph.add_edge(1, 4, 8)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 5, 10)
    graph.add_edge(4, 3, 6)
    graph.add_edge(4, 5, 10)
    
    assert graph.ford_fulkerson(0, 5) == 19

def test_invalid_source_vertex():
    """
    Test handling of invalid source vertex
    """
    graph = Graph(3)
    
    with pytest.raises(ValueError, match="Source or sink vertex is out of bounds"):
        graph.ford_fulkerson(-1, 2)

def test_invalid_sink_vertex():
    """
    Test handling of invalid sink vertex
    """
    graph = Graph(3)
    
    with pytest.raises(ValueError, match="Source or sink vertex is out of bounds"):
        graph.ford_fulkerson(0, 3)

def test_same_source_and_sink():
    """
    Test when source and sink are the same vertex
    """
    graph = Graph(3)
    
    assert graph.ford_fulkerson(1, 1) == 0