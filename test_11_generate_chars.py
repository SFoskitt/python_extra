
import unittest
from ex_11_generate_n_chars import generate_n_chars

class TestGenerateChars(unittest.TestCase):

    def test_generate_chars(self):
        self.assertEqual(
            'ccc',
            generate_n_chars(3, 'c')
        )

    def test_gen_chars_empty(self):
        self.assertEqual(
            '',
            generate_n_chars(0, 'c')
        )