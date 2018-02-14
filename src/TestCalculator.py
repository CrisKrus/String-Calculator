import unittest


class TestCalculator(unittest.TestCase):

    def test__should_return_two_given_one_plus_one(self):
        self.assertTrue(2, add("1, 1"))
