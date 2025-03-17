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
        
        # Check all neighbors of the current node
        visited_neighbors = 0
        for neighbor in graph[node]:
            # If neighbor is not visited, explore it
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
            # Count visited neighbors (excluding parent)
            elif neighbor != parent:
                visited_neighbors += 1
        
        # If more than one neighbor is already visited (excluding parent), it's a cycle
        return visited_neighbors > 0
    
    # Track globally visited nodes
    global_visited: Set[int] = set()
    
    # Track if a cycle is found
    cycle_found = False
    
    # Check each node that hasn't been visited
    for node in graph:
        if node not in global_visited:
            # Create a new visited set for this component
            visited: Set[int] = set()
            # Check if a cycle exists in this component
            component_has_cycle = dfs(node, -1, visited)
            global_visited.update(visited)
            
            # Update cycle_found if a cycle is found
            cycle_found |= component_has_cycle
    
    return cycle_found