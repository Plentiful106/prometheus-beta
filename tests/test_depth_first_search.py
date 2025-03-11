import pytest
from src.depth_first_search import depth_first_search

def test_basic_graph_dfs():
    """Test DFS on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_single_node_graph():
    """Test DFS on a graph with a single node."""
    graph = {'A': []}
    
    result = depth_first_search(graph, 'A')
    assert result == ['A']

def test_disconnected_graph():
    """Test DFS on a disconnected graph."""
    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_visit_function():
    """Test DFS with a visit function."""
    visited_nodes = []
    
    def mock_visit(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': [],
        'D': []
    }
    
    depth_first_search(graph, 'A', visit_func=mock_visit)
    assert visited_nodes == ['A', 'B', 'D', 'C']

def test_invalid_start_node():
    """Test DFS with a start node not in the graph."""
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_invalid_graph_type():
    """Test DFS with an invalid graph type."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        depth_first_search([], 'A')