import unittest
from ex_15_find_longest import find_longest

class TestFindLongest(unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(
            5,
            find_longest(['one', 'two', 'three', 'four', 'five'])
        )

    def test_empty_list(self):
        self.assertEqual(
            0,
            find_longest([])
        )
    
    def test_all_same(self):
        self.assertEqual(
            3,
            find_longest(['one', 'two', 'egg'])
        )