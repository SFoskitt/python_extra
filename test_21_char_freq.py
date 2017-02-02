import unittest

from ex_21_char_freq import char_freq

class TestCharFreq(unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(
            {'a': 1, ' ': 2, 'g': 1, 'i': 2, 'n': 1, 's': 2, 'r': 1, 't': 2},
            char_freq('its a string')
        )

    def test_empty_string(self):
        self.assertEqual(
            {},
            char_freq('')
        )

    def test_with_spaces(self):
        self.assertEqual(
            {' ': 5},
            char_freq('     ')
        )

    def test_with_punc(self):
        self.assertEqual(
            {';': 2, '?': 1, ',': 3, '/': 1, '.': 2},
            char_freq(',;,;./?.,')
        )