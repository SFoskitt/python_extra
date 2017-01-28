import unittest
import ex_02_max_of_three

class MaxOfThreeTests(unittest.TestCase):

    def test_with_three(self):
        self.assertEqual(
            6,
            ex_02_max_of_three.max_of_three(4, 5, 6)
        )

