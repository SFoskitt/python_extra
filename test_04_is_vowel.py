import unittest
from ex_04_is_vowel import is_vowel

class IsVowelTests(unittest.TestCase):

    def test_is_vowel(self):
        self.assertEqual(
            True,
            is_vowel('A')
        )
    
    def test_long_string(self):
        self.assertEqual(
            False,
            is_vowel('string')
        )

    def test_long_string_of_vowels(self):
        self.assertEqual(
            False,
            is_vowel('AEIOU')
        )

    def test_with_consonant(self):
        self.assertEqual(
            False,
            is_vowel('n')
        )