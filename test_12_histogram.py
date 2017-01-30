import unittest
from ex_12_histogram import histogram

class TestHistogram(unittest.TestCase):

    def test_histogram_all_equal(self):
        self.assertEqual(
            '***\n'
            '***\n'
            '***\n',
            histogram([3, 3, 3])
        )

    def test_histogram_all_different(self):
        self.assertEqual(
            '*\n'
            '**\n'
            '***\n',
            histogram([1, 2, 3])
        )

    def test_histogram_empty_list(self):
        self.assertEqual(
            '',
            histogram([])
        )