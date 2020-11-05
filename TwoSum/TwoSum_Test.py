import unittest

from TwoSum import twoSum

class Test(unittest.TestCase):
    def test_two_sum(self):
        num = [2,7,11,1]
        target = 9
        result = [0,1]
        self.assertEqual(result,[0,1])

if __name__ == '__main__':
    unittest.main()