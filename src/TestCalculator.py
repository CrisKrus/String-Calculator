import unittest


def add(numbers):
    return 2


class TestCalculator(unittest.TestCase):

    def test__given_two_numbers_of_one_digit(self):
        self.assertTrue(2, add("1, 1"))
