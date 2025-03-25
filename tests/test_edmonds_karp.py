import pytest
from src.edmonds_karp import edmonds_karp_max_flow

def test_simple_max_flow():
    """Test a simple graph with known max flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 5) == 19

def test_disconnected_graph():
    """Test a graph with no path from source to sink."""
    graph = {
        0: {1: 5},
        1: {0: 5},
        2: {3: 10},
        3: {2: 10}
    }
    assert edmonds_karp_max_flow(graph, 0, 3) == 0

def test_single_path_graph():
    """Test a graph with a single path."""
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 2) == 5

def test_multiple_paths_graph():
    """Test a graph with multiple potential paths."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 5) == 19

def test_zero_capacity_graph():
    """Test a graph with zero capacities."""
    graph = {
        0: {1: 0},
        1: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 1) == 0

def test_invalid_source_node():
    """Test raising an error for invalid source node."""
    graph = {1: {2: 10}, 2: {}}
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 0, 2)

def test_invalid_sink_node():
    """Test raising an error for invalid sink node."""
    graph = {0: {1: 10}, 1: {}}
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 0, 2)

def test_empty_graph():
    """Test an empty graph."""
    graph = {}
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 0, 1)