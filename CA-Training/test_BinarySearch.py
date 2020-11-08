import unittest

from BinarySearch import binarySearch

class TestBinarySearch(unittest.TestCase):
    def test_case(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 3), 9)



