import unittest

from FindThreeLargestNumbers import findThreeLargestNumbers

class TestNumbers(unittest.TestCase):
    def test_case(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])