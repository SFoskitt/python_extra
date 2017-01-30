import unittest

from ex_06_sum import sum
from ex_06_sum import multiply

# BOTH METHODS TAKE A LIST OF NUMBERS
# HOW TO SUBMIT A LIST OF NUMBERS WITH PY.TEST

class SumMultiplyTests(unittest.TestCase):

# Test the sum method
    def test_sum(self):
        self.assertEqual(
            4,
            sum([2,2])
        )
    
    def test_sum_negatives(self):
        self.assertEqual(
            0,
            sum([-1, 1])
        )
    
    def test_sum_all_negatives(self):
        self.assertEqual(
            -6,
            sum([-1, -2, -3])
        )
    
    def test_sum_empty_list(self):
        self.assertEqual(
            0,
            sum([])
        )

# Test the multiply method
    def test_multiply(self):
        self.assertEqual(
            4,
            multiply([2,2])            
        )
    
    def test_mult_negatives(self):
        self.assertEqual(
            -5,
            multiply([-1, 5])
        )
    
    def test_mult_all_negs(self):
        self.assertEqual(
            6,
            multiply([-1, 2, -3])
        )

    def test_mult_empty_list(self):
        self.assertEqual(
            1,
            multiply([])
        )
