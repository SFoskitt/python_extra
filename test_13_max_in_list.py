import unittest
from ex_13_max_in_list import max_in_list

class TestMaxInList(unittest.TestCase):

    def test_max_in_list1(self):
        self.assertEqual(
            6,
            max_in_list([4, 5, 6])
        )
    
    def test_max_in_list2(self):
        self.assertEqual(
            -1,
            max_in_list([-3, -2, -1])
        )

    def test_max_in_list3(self):
        self.assertEqual(
            0,
            max_in_list([0, 0, 0, 0, 0])
        )

    def test_max_in_empty_list(self):
        self.assertEqual(
            None,
            max_in_list([])
        )
    