import unittest

from maths.multiply import multiply


class TestMathsAdd(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
