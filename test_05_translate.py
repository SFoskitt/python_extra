import unittest

from ex_05_translate import modify_string

class TranslateTests(unittest.TestCase):

    def test_string(self):
        self.assertEqual(
            'tothohe',
            modify_string('the')
        )

    def test_single_vowel(self):
        self.assertEqual(
            'a',
            modify_string('a')
        )

    def test_single_consonant(self):
        self.assertEqual(
            'vov',
            modify_string('v')
        )
    
    def test_with_numbers(self):
        self.assertEqual(
            'aror8o8e',
            modify_string('ar8e')
        )