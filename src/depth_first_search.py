from typing import Dict, List, Any, Optional, Callable

def depth_first_search(graph: Dict[Any, List[Any]], 
                       start: Any, 
                       visit_func: Optional[Callable[[Any], None]] = None) -> List[Any]:
    """
    Perform a depth-first search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph.
        start (Any): Starting node for the DFS traversal.
        visit_func (Optional[Callable[[Any], None]], optional): Optional function to call on each visited node.
                    Defaults to None.

    Returns:
        List[Any]: List of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid adjacency list.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary (adjacency list)")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")

    # Set to keep track of visited nodes
    visited = set()
    # List to store the order of visited nodes
    traversal_order = []

    def _dfs(node):
        """
        Recursive depth-first search helper function.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark the node as visited
        visited.add(node)
        
        # Optional visit function
        if visit_func:
            visit_func(node)
        
        # Add to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)

    # Start DFS from the start node
    _dfs(start)

    return traversal_order