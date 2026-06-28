"""
Unified graph traversal API.

Provides a single function `traverse` that performs an iterative depth-first search
using an explicit stack. The function accepts an optional callback that is called
for each visited vertex. Reflexive edges are handled naturally by the adjacency
list; self-loops are visited only once because visited vertices are tracked.
"""

from __future__ import annotations
from typing import Any, Callable, Iterable, Set, List
from graph import Graph


def traverse(
    start: Any,
    graph: Graph,
    callback: Callable[[Any], None] | None = None,
) -> List[Any]:
    """
    Perform an iterative depth-first traversal starting from `start`.

    Parameters
    ----------
    start : Any
        The starting vertex.
    graph : Graph
        The graph to traverse.
    callback : Callable[[Any], None], optional
        Function called with each visited vertex. If None, no callback is invoked.

    Returns
    -------
    List[Any]
        The list of vertices in the order they were visited.

    Notes
    -----
    - The traversal visits each vertex at most once.
    - Reflexive edges (self-loops) are ignored after the first visit.
    - The function is safe for disconnected graphs; it only explores the component
      containing `start`.
    """
    if start not in graph:
        raise ValueError(f"Start vertex {start!r} not in graph")

    visited: Set[Any] = set()
    stack: List[Any] = [start]
    order: List[Any] = []

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        if callback:
            callback(vertex)
        # Add neighbors in reverse order to preserve natural adjacency order
        for nbr in reversed(sorted(graph.neighbors(vertex))):
            if nbr not in visited:
                stack.append(nbr)

    return order
