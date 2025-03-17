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
        for neighbor in graph[node]:
            # If neighbor is not visited, explore it
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
            # If neighbor is visited and is not the parent, it's a back edge (cycle)
            elif neighbor != parent:
                return True
        
        return False
    
    # Track globally visited nodes to ensure we cover all components
    global_visited: Set[int] = set()
    
    # Check if all nodes can form a cycle
    for node in graph:
        if node not in global_visited:
            # Create a new visited set for this component
            visited: Set[int] = set()
            # If a cycle is found, return True
            if dfs(node, -1, visited):
                return True
            # Mark all nodes in this component as visited
            global_visited.update(visited)
    
    return False