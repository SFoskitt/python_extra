import unittest
from ex_17_more_pali import more_pali

class TestMorePali(unittest.TestCase):

    def test_more_pali(self):
        self.assertEqual(
            True,
            more_pali("Rise to vote sir")
        )

    def test_more_pali_2(self):
        self.assertEqual(
            True,
            more_pali("Was it a rat I saw?")
        )

    def test_more_pali_3(self):
        self.assertEqual(
            True,
            more_pali("Sit on a potato pan, Otis")
        )

    def test_more_pali_4(self):
        self.assertEqual(
            True,
            more_pali("Dammit, I'm mad!")
        )