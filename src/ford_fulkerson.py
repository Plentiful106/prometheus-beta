from typing import List, Dict
from collections import deque

class Graph:
    """
    A class representing a flow network for the Ford-Fulkerson algorithm.
    
    Attributes:
        vertices (int): Number of vertices in the graph
        graph (List[List[int]]): Adjacency matrix representing the graph
    """
    
    def __init__(self, vertices: int):
        """
        Initialize the graph with a given number of vertices.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u: int, v: int, capacity: int) -> None:
        """
        Add an edge to the graph with a given capacity.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            capacity (int): Edge capacity
        """
        self.graph[u][v] = capacity
    
    def bfs(self, source: int, sink: int, parent: List[int]) -> bool:
        """
        Perform Breadth-First Search to find an augmenting path.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
            parent (List[int]): List to store the parent of each vertex
        
        Returns:
            bool: True if a path is found, False otherwise
        """
        # Track visited vertices
        visited = [False] * self.vertices
        
        # Create a queue for BFS
        queue = deque()
        
        # Start BFS from source
        queue.append(source)
        visited[source] = True
        parent[source] = -1
        
        # BFS to find an augmenting path
        while queue:
            u = queue.popleft()
            
            # Check all adjacent vertices
            for v in range(self.vertices):
                # If vertex is not visited and there's remaining capacity
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    parent[v] = u
                    visited[v] = True
                    
                    # If sink is reached, augmenting path found
                    if v == sink:
                        return True
        
        # No path found
        return False
    
    def ford_fulkerson(self, source: int, sink: int) -> int:
        """
        Implement the Ford-Fulkerson algorithm to find maximum flow.
        
        Args:
            source (int): Source vertex
            sink (int): Sink vertex
        
        Returns:
            int: Maximum flow from source to sink
        
        Raises:
            ValueError: If source or sink is out of graph bounds
        """
        # Validate source and sink vertices
        if source < 0 or source >= self.vertices or sink < 0 or sink >= self.vertices:
            raise ValueError("Source or sink vertex is out of bounds")
        
        if source == sink:
            return 0
        
        # Initialize flow network with the same structure as original graph
        max_flow = 0
        
        # Create a parent list for storing path
        parent = [-1] * self.vertices
        
        # Residual graph (will be modified during the algorithm)
        residual_graph = [row[:] for row in self.graph]
        
        # Augment the flow while there's a path from source to sink
        while self.bfs(source, sink, parent):
            # Find the minimum flow (bottleneck capacity) in the path
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, residual_graph[u][v])
                v = parent[v]
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]
            
            # Add path flow to total max flow
            max_flow += path_flow
        
        return max_flow