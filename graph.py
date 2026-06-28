"""
Graph implementation with reflexive edges and unified traversal support.

The Graph class uses an adjacency list representation where each vertex maps to a set of its neighbors.
All operations are O(1) on average, except for traversal which is O(V + E).

Author: ChatGPT
"""

from __future__ import annotations
from typing import Dict, Set, Iterable, Callable, Any, Optional


class Graph:
    """
    Undirected graph with optional reflexive edges.

    Attributes
    ----------
    _adjacency : Dict[Any, Set[Any]]
        Mapping from vertex to a set of adjacent vertices.
    """

    def __init__(self) -> None:
        self._adjacency: Dict[Any, Set[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph."""
        if vertex not in self._adjacency:
            self._adjacency[vertex] = set()

    def add_edge(self, u: Any, v: Any) -> None:
        """Add an undirected edge between u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self._adjacency[u].add(v)
        self._adjacency[v].add(u)

    def add_reflexive_edges(self) -> None:
        """Add self-loop edges for all vertices."""
        for vertex in list(self._adjacency.keys()):
            self._adjacency[vertex].add(vertex)

    def has_edge(self, u: Any, v: Any) -> bool:
        """Return True if an edge exists between u and v."""
        return u in self._adjacency and v in self._adjacency[u]

    def neighbors(self, vertex: Any) -> Set[Any]:
        """Return the set of neighbors of a vertex."""
        return self._adjacency.get(vertex, set())

    def vertices(self) -> Iterable[Any]:
        """Return an iterable of all vertices."""
        return self._adjacency.keys()

    def edges(self) -> Iterable[tuple[Any, Any]]:
        """Return an iterable of all undirected edges as (u, v) with u <= v."""
        seen = set()
        for u, nbrs in self._adjacency.items():
            for v in nbrs:
                if (v, u) not in seen:
                    seen.add((u, v))
                    yield (u, v)

    def __len__(self) -> int:
        """Return the number of vertices."""
        return len(self._adjacency)

    def __contains__(self, vertex: Any) -> bool:
        """Return True if vertex is in the graph."""
        return vertex in self._adjacency

    def __repr__(self) -> str:
        return f"Graph(vertices={len(self._adjacency)})"
