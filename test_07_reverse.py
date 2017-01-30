import unittest
from ex_07_reverse_string import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(
            'dcba',
            reverse_string('abcd')
        )
    
    def test_reverse_empty_string(self):
        self.assertEqual(
            '',
            reverse_string('')
        )