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
    
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycle.
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark current node as visited
        visited.add(node)
        
        # Track the number of revisits (for cycles in small graphs)
        revisit_count = 0
        
        # Check all neighbors of the current node
        for neighbor in graph[node]:
            # If neighbor is not visited, explore it
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
            
            # If neighbor is visited 
            elif neighbor != parent:
                revisit_count += 1
                # If revisited more than once, it's definitely a cycle
                if revisit_count > 0:
                    return True
        
        return False
    
    # Track visited nodes to avoid redundant exploration
    visited: Set[int] = set()
    
    # Check each node that hasn't been visited
    for node in graph:
        if node not in visited:
            # If a cycle is found in this component, return True
            if dfs(node, -1, visited):
                return True
    
    return False