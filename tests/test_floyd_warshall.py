import pytest
import math
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic_graph():
    """Test Floyd-Warshall on a basic connected graph."""
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_disconnected_graph():
    """Test Floyd-Warshall on a graph with disconnected vertices."""
    graph = [
        [0, 5, float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 5, float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_negative_weights():
    """Test Floyd-Warshall with a graph containing negative weights."""
    graph = [
        [0, -1, 4],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, -1, 2],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_empty_graph():
    """Test Floyd-Warshall with an empty graph."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_floyd_warshall_non_square_matrix():
    """Test Floyd-Warshall with a non-square matrix."""
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [float('inf'), 0]
        ])

def test_floyd_warshall_single_vertex():
    """Test Floyd-Warshall with a single vertex graph."""
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_floyd_warshall_negative_cycle():
    """Test Floyd-Warshall with a graph containing a negative cycle."""
    graph = [
        [0, 1, float('inf')],
        [float('inf'), 0, -3],
        [-1, float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result is None