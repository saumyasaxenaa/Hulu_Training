import unittest

from NthFibonacciSeries import getNthFib

class TestFib(unittest.TestCase):
    def test_case(self):
        self.assertEqual(getNthFib(6), 5)