from typing import List, Tuple, Dict
import sys

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help detect cycles in the graph.
    """
    def __init__(self, vertices: int):
        """
        Initialize the disjoint set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Merge two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if sets were merged, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def boruvka_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    :param vertices: Number of vertices in the graph
    :param edges: List of edges in the format (u, v, weight)
    :return: List of edges in the minimum spanning tree
    :raises ValueError: If input is invalid or no MST can be formed
    """
    # Input validation
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    if not edges:
        raise ValueError("Graph must have at least one edge")

    # Sort edges by weight to help with processing
    edges.sort(key=lambda x: x[2])

    # Initialize disjoint set
    ds = DisjointSet(vertices)
    
    # Result MST
    mst = []
    
    # Number of disjoint sets
    num_sets = vertices

    # Continue until we have a single set (complete MST)
    while num_sets > 1:
        # Cheapest edges for each component
        cheapest = [None] * vertices

        # Find cheapest edge for each component
        for u, v, weight in edges:
            set_u = ds.find(u)
            set_v = ds.find(v)

            # Skip if in same set (would create a cycle)
            if set_u == set_v:
                continue

            # Update cheapest edge for components
            if cheapest[set_u] is None or weight < cheapest[set_u][2]:
                cheapest[set_u] = (u, v, weight)
            
            if cheapest[set_v] is None or weight < cheapest[set_v][2]:
                cheapest[set_v] = (u, v, weight)

        # Add the cheapest edges to MST
        for edge in cheapest:
            if edge is not None:
                u, v, weight = edge
                if ds.union(u, v):
                    mst.append(edge)
                    num_sets -= 1

        # Break if no more edges can be added
        if not mst:
            break

    # Verify if a complete MST was formed
    if len(mst) != vertices - 1:
        raise ValueError("Graph is not connected, cannot form a complete MST")

    return mst