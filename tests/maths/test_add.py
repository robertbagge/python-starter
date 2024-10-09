import unittest

from maths.add import add


class TestMathsAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # add assertion here
