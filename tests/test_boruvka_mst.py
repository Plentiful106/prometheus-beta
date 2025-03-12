import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from boruvka_mst import boruvka_mst

def test_simple_mst():
    """
    Test a simple graph with known MST
    Graph:
        0 -- 1 (weight 4)
        0 -- 7 (weight 8)
        1 -- 7 (weight 11)
        1 -- 2 (weight 8)
        7 -- 8 (weight 7)
        7 -- 6 (weight 1)
        2 -- 8 (weight 2)
        2 -- 5 (weight 4)
        2 -- 3 (weight 7)
        8 -- 6 (weight 6)
        6 -- 5 (weight 2)
        3 -- 5 (weight 14)
        3 -- 4 (weight 9)
        5 -- 4 (weight 10)
    """
    vertices = 9
    edges = [
        (0, 1, 4), (0, 7, 8), 
        (1, 7, 11), (1, 2, 8), 
        (7, 8, 7), (7, 6, 1), 
        (2, 8, 2), (2, 5, 4), 
        (2, 3, 7), (8, 6, 6), 
        (6, 5, 2), (3, 5, 14), 
        (3, 4, 9), (5, 4, 10)
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    # Expected total weight of MST
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 37
    assert len(mst) == vertices - 1

def test_fully_connected_graph():
    """
    Test a fully connected graph
    """
    vertices = 4
    edges = [
        (0, 1, 10), (0, 2, 6), (0, 3, 5),
        (1, 2, 3), (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 18
    assert len(mst) == vertices - 1

def test_invalid_vertices_count():
    """
    Test handling of invalid number of vertices
    """
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(0, [(0, 1, 1)])
    
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(-1, [(0, 1, 1)])

def test_empty_edges():
    """
    Test handling of empty edges list
    """
    with pytest.raises(ValueError, match="Graph must have at least one edge"):
        boruvka_mst(5, [])

def test_disconnected_graph():
    """
    Test handling of a disconnected graph
    """
    vertices = 4
    edges = [
        (0, 1, 1),  # Component 1
        (2, 3, 2)   # Component 2
    ]
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        boruvka_mst(vertices, edges)

def test_single_vertex_graph():
    """
    Test a graph with a single vertex
    """
    with pytest.raises(ValueError, match="Graph must have at least one edge"):
        boruvka_mst(1, [])