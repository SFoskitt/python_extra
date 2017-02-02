import unittest

from ex_18_panagram import panagram

class TestPanagram(unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(
            True,
            panagram('the quick brown fox jumps over the lazy dog')
        )
    
    def test_twice_alphabet(self):
        self.assertEqual(
            True,
            panagram('the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog')
        )
    
    def test_all_punc(self):
        self.assertEqual(
            False,
            panagram('..  ,,  ;;  ""')
        )

    def test_empty_string(self):
        self.assertEqual(
            False,
            panagram('    ')
        )