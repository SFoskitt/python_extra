import unittest

import ex_01_max_fun

class MaxFunTests(unittest.TestCase):
        
    def test_max_second(self):
        self.assertEqual(
            4,
            ex_01_max_fun.max(3, 4)
        )

    def test_max_first(self):
        self.assertEqual(
            4,
            ex_01_max_fun.max(4, 3)
        )

    def test_negative_values(self):
        self.assertEqual(
            -5,
            ex_01_max_fun.max(-5, -9)
        )

    def test_mixed_values(self):
        self.assertEqual(
            0,
            ex_01_max_fun.max(-5, 0)
        )
    
    def test_mixed_values_reversed(self):
        self.assertEqual(
            0,
            ex_01_max_fun.max(0, -9)
        )

