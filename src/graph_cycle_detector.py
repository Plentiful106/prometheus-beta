from typing import Dict, List, Set

def detect_cycle_in_undirected_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if there is a cycle in an undirected graph.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes
    
    Returns:
        bool: True if a cycle is detected, False otherwise
    
    Raises:
        ValueError: If the input graph is empty or None
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def has_back_edge(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Detect if a graph contains a back edge (indicating a cycle).
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a back edge is found, False otherwise
        """
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            # If neighbor hasn't been visited, recursively explore
            if neighbor not in visited:
                if has_back_edge(neighbor, node, visited):
                    return True
            # If neighbor is visited and is not the parent, it's a back edge
            elif neighbor != parent:
                return True
        
        return False
    
    # Track nodes we've already processed to avoid redundant work
    processed: Set[int] = set()
    
    # Iterate through each node in the graph
    for start_node in graph:
        # If this node hasn't been processed yet
        if start_node not in processed:
            # Create a new visited set for each component
            visited: Set[int] = set()
            
            # Check for a cycle starting from this node
            if has_back_edge(start_node, -1, visited):
                return True
            
            # Mark all nodes in this component as processed
            processed.update(visited)
    
    return False