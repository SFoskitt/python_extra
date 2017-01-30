import unittest
from ex_09_is_member import is_member

class TestIsMember(unittest.TestCase):

    def test_is_member(self):
        self.assertEqual(
            True,
            is_member(6, [4, 5, 6])
        )

    def test_is_not_member(self):
        self.assertEqual(
            False,
            is_member(6, [7, 8, 9])
        )

    def test_is_string_member_true(self):
        self.assertEqual(
            True,
            is_member('abc', ['abc', 'def', 'ghi'])
        )
    def test_is_string_member(self):
        self.assertEqual(
            False,
            is_member('abc', ['def', 'ghi', 'jkl'])
        )