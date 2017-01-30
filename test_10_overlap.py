import unittest
from ex_10_overlapping import overlapping

class TestOverlapping(unittest.TestCase):

    def test_overlap_true(self):
        self.assertEqual(
            True,
            overlapping(['abc', 'def', 'ghi'], ['abc', 'jkl', 'mno'])
        )

    def test_overlap_false(self):
        self.assertEqual(
            False,
            overlapping(['abc', 'def', 'ghi'], ['pqr', 'jkl', 'mno'])
        )

    def test_overlap_empty_list(self):
        self.assertEqual(
            False,
            overlapping([], ['abc', 'def', 'ghi'])
        )

    def test_overlap_empty_list2(self):
        self.assertEqual(
            False,
            overlapping(['abc', 'def', 'ghi'], [])
        )
    