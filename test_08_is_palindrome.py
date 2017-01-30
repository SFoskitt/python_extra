import unittest
from ex_08_is_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(
            True,
            is_palindrome('aba')
        )
    
    def test_is_pal_empty(self):
        self.assertEqual(
            True,
            is_palindrome('')
        )

    def test_is_pal_equal_string(self):
        self.assertEqual(
            True,
            is_palindrome('aaa')
        )