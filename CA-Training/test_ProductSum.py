import unittest

from ProductSum import productSum

class TestProductSum(unittest.TestCase):
    def test_case(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)