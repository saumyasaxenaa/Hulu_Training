import unittest

from PalindromeCheck import isPalindrome

class TestPalindrome(unittest.TestCase):
    def test_case(self):
        self.assertEqual(isPalindrome('abcdcba'), True)