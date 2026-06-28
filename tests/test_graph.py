"""
Unit tests for the graph implementation and traversal.
"""

import unittest
from graph import Graph
from traversal import traverse


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        # Build a simple graph:
        # 1 - 2
        # |   |
        # 3 - 4
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 4)
        self.g.add_edge(4, 3)
        self.g.add_edge(3, 1)

    def test_vertices_and_edges(self):
        self.assertEqual(set(self.g.vertices()), {1, 2, 3, 4})
        self.assertEqual(set(self.g.edges()), {(1, 2), (1, 3), (2, 4), (3, 4)})

    def test_reflexive_edges(self):
        self.g.add_reflexive_edges()
        for v in self.g.vertices():
            self.assertIn(v, self.g.neighbors(v))

    def test_has_edge(self):
        self.assertTrue(self.g.has_edge(1, 2))
        self.assertFalse(self.g.has_edge(1, 4))

    def test_traverse_order(self):
        order = traverse(1, self.g)
        # Since we sort neighbors, the traversal order is deterministic
        self.assertEqual(order, [1, 3, 4, 2])

    def test_traverse_with_callback(self):
        visited = []

        def cb(v):
            visited.append(v)

        order = traverse(1, self.g, callback=cb)
        self.assertEqual(order, visited)

    def test_traverse_disconnected(self):
        # Add a disconnected component
        self.g.add_vertex(5)
        self.g.add_edge(5, 6)
        order = traverse(5, self.g)
        self.assertEqual(set(order), {5, 6})

    def test_traverse_self_loop(self):
        self.g.add_edge(1, 1)  # self-loop
        order = traverse(1, self.g)
        self.assertEqual(order, [1, 3, 4, 2])  # self-loop does not affect order

    def test_traverse_invalid_start(self):
        with self.assertRaises(ValueError):
            traverse(99, self.g)


if __name__ == "__main__":
    unittest.main()
