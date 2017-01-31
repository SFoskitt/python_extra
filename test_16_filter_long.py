import unittest

from ex_16_filter_long import filter_long_words

class TestFilterLong(unittest.TestCase):

    def test_filter_long(self):
        self.assertEqual(
            ['three', 'four', 'five'],
            filter_long_words(['one', 'two', 'three', 'four', 'five'], 3)
        )

    def test_filter_none(self):
        self.assertEqual(
            [],
            filter_long_words(['one', 'two', 'three', 'four', 'five'], 6)
        )

    def test_filter_all(self):
        self.assertEqual(
            ['one', 'two', 'three', 'four', 'five'],
            filter_long_words(['one', 'two', 'three', 'four', 'five'], 1)
        )

    def test_filter_with_integers(self):
        self.assertEqual(
            ['one', 'two', 'three', '6' 'four', 'five'],
            filter_long_words(['one', 'two', 'three', '6' 'four', 'five'], 1)
        )