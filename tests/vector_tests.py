import unittest
from satclave import Vector

class TestVector(unittest.TestCase):
    def test_addition(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 + v2, Vector([5, 7, 9]))

    def test_subtraction(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 - v2, Vector([-3, -3, -3]))

    def test_dot_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1.dot(v2), 32)

    def test_cross_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1.cross(v2), Vector([-3, 6, -3]))

    def test_magnitude(self):
        v = Vector([1, 2, 3])
        self.assertAlmostEqual(v.magnitude(), 3.74165, places=5)

    def test_normalize(self):
        v = Vector([1, 2, 3])
        self.assertEqual(v.normalize(), Vector([0.26726, 0.53452, 0.80178]))

if __name__ == '__main__':
    unittest.main()
