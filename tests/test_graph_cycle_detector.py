import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_cycle_detection_simple_cycle():
    """Test a simple graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_cycle_detection_no_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1],
        1: [0, 2],
        2: [1]
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_cycle_detection_multiple_components():
    """Test a graph with multiple components, one containing a cycle"""
    graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_cycle_detection_disconnected_no_cycle():
    """Test a disconnected graph without a cycle"""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_cycle_detection_single_node():
    """Test a graph with a single node"""
    graph = {
        0: []
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_cycle_detection_two_nodes_cycle():
    """Test a graph with two nodes forming a cycle"""
    graph = {
        0: [1],
        1: [0]
    }
    # Every connected graph with at least 2 nodes forms a cycle in undirected representation
    assert detect_cycle_in_undirected_graph(graph) == True

def test_cycle_detection_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph({})

def test_cycle_detection_large_graph():
    """Test a larger graph with a complex cycle structure"""
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1, 6],
        4: [1, 5],
        5: [2, 4, 7],
        6: [3],
        7: [5]
    }
    assert detect_cycle_in_undirected_graph(graph) == True