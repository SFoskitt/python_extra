import unittest

import ex_02_max_of_three

class MaxOfThreeTests(unittest.TestCase):

    def test_with_three(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(4, 5, 6)
        )

    def test_rearranged(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(6, 5, 4)
        )

    def test_middle(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(4, 6, 5)
        )

    def test_two_same_1(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(6, 6, 4)
        )
    
    def test_same(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(6, 6, 6)
        )

    def test_two_same_2(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(4, 6, 6)
        )
    
    def test_neg_nums(self):
        self.assertEqual(
            0,
            ex_02_max_of_three.max_of_three(-1, -3, 0)
        )

    def test_neg_nums_2(self):
        self.assertEqual(
            0,
            ex_02_max_of_three.max_of_three(0, -1, -3)
        )
        