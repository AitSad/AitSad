import unittest
from satclave import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)

    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertIn(4, self.graph.vertices)

    def test_add_edge(self):
        self.graph.add_edge(3, 1)
        self.assertIn(1, self.graph.edges[3])
        self.assertIn(3, self.graph.edges[1])

    def test_remove_edge(self):
        self.graph.remove_edge(1, 2)
        self.assertNotIn(2, self.graph.edges[1])
        self.assertNotIn(1, self.graph.edges[2])

    def test_remove_vertex(self):
        self.graph.remove_vertex(2)
        self.assertNotIn(2, self.graph.vertices)
        self.assertNotIn(2, self.graph.edges[1])
        self.assertNotIn(2, self.graph.edges[3])

    def test_is_connected(self):
        self.assertTrue(self.graph.is_connected())

    def test_depth_first_search(self):
        self.assertEqual(self.graph.depth_first_search(1), [1, 2, 3])

    def test_breadth_first_search(self):
        self.assertEqual(self.graph.breadth_first_search(1), [1, 2, 3])

    def test_get_shortest_path(self):
        self.assertEqual(self.graph.get_shortest_path(1, 3), [1, 2, 3])
    def test_get_connected_components(self):
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
        self.graph.add_edge(4, 5)
        self.assertEqual(self.graph.get_connected_components(), [{1, 2, 3}, {4, 5}])

    def test_is_cyclic(self):
        self.assertFalse(self.graph.is_cyclic())

        self.graph.add_edge(3, 1)
        self.assertTrue(self.graph.is_cyclic())

if __name__ == '__main__':
    unittest.main()
