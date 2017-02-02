import unittest

from ex_20_eng_to_swed import eng_to_swed

class TestEngToSwed(unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(
            'gott nytt yar ',
            eng_to_swed('happy new year')
        )

    def test_empty_string(self):
        self.assertEqual(
            '',
            eng_to_swed('')
        )