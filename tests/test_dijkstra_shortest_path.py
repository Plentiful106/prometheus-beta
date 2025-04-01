import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_simple_path():
    """Test a simple graph with a clear shortest path."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_single_node_path():
    """Test path from a node to itself."""
    graph = {'A': {}, 'B': {}}
    with pytest.raises(ValueError, match="No path exists"):
        dijkstra_shortest_path(graph, 'A', 'B')

def test_non_existent_start_node():
    """Test error when start node doesn't exist."""
    graph = {'A': {}, 'B': {}}
    with pytest.raises(ValueError, match="Start node 'X' not in graph"):
        dijkstra_shortest_path(graph, 'X', 'A')

def test_non_existent_end_node():
    """Test error when end node doesn't exist."""
    graph = {'A': {}, 'B': {}}
    with pytest.raises(ValueError, match="End node 'X' not in graph"):
        dijkstra_shortest_path(graph, 'A', 'X')

def test_complex_path():
    """Test a more complex graph with multiple possible paths."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4

def test_disconnected_graph():
    """Test when no path exists between nodes."""
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists"):
        dijkstra_shortest_path(graph, 'A', 'B')

def test_weighted_graph_with_longer_path():
    """Test a graph where the shorter path is not the most direct."""
    graph = {
        'A': {'B': 10, 'C': 3},
        'B': {'D': 2},
        'C': {'B': 1, 'D': 8},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4