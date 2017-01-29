import unittest

import ex_03_find_len

class FindLenTests(unittest.TestCase):

    def test_find_len(self):
        self.assertEqual(
            6,
            ex_03_find_len.find_len('string')
        )
    
    def test_empty_string(self):
        self.assertEqual(
            0,
            ex_03_find_len.find_len('')
        )

    def test_with_nums(self):
        self.assertEqual(
            6,
            ex_03_find_len.find_len('str8ng')
        )
    
    def test_with_nums_2(self):
        self.assertEqual(
            6,
            ex_03_find_len.find_len('547698')
        )
