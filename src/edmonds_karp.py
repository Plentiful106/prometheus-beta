from typing import List, Dict, Optional
from collections import deque

def edmonds_karp_max_flow(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find the maximum flow in a network.

    Args:
        graph (Dict[int, Dict[int, int]]): A graph represented as an adjacency list 
            where graph[u][v] represents the capacity from node u to node v.
        source (int): The source node of the network.
        sink (int): The sink node of the network.

    Returns:
        int: The maximum flow from source to sink.

    Raises:
        ValueError: If source or sink nodes are not in the graph,
                    or if graph is not properly formatted.
    """
    # Validate input graph
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")

    # Create a residual graph to track remaining capacities
    residual_graph = {u: graph[u].copy() for u in graph}
    for u in graph:
        for v in graph[u]:
            if u not in residual_graph.get(v, {}):
                if v not in residual_graph:
                    residual_graph[v] = {}
                residual_graph[v][u] = 0

    def bfs_find_path(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> Optional[List[int]]:
        """
        Find an augmenting path using Breadth-First Search.

        Args:
            graph (Dict[int, Dict[int, int]]): The residual graph.
            source (int): The source node.
            sink (int): The sink node.

        Returns:
            Optional[List[int]]: A path from source to sink, or None if no path exists.
        """
        # Track visited nodes and parent relationships
        visited = {source}
        parent = {source: None}
        queue = deque([source])

        while queue:
            u = queue.popleft()

            # Check neighbors
            for v, capacity in graph.get(u, {}).items():
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)

                    # Found a path to sink
                    if v == sink:
                        # Reconstruct the path
                        path = []
                        current = sink
                        while current is not None:
                            path.append(current)
                            current = parent[current]
                        return list(reversed(path))

        return None

    # Track total maximum flow
    max_flow = 0

    # Find augmenting paths
    while True:
        # Find an augmenting path
        path = bfs_find_path(residual_graph, source, sink)
        
        # No more augmenting paths exist
        if not path:
            break

        # Find the minimum residual capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            path_flow = min(path_flow, residual_graph[u][v])

        # Update residual capacities
        max_flow += path_flow
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow

    return max_flow