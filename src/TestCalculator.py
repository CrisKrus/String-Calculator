import unittest


def add(numbers):
    return int(numbers[0]) + int(numbers[3])


class TestCalculator(unittest.TestCase):

    def test__given_two_numbers_of_one_digit(self):
        self.assertEqual(2, add("1, 1"))
        self.assertEqual(10, add("6, 4"))

    def test__given_one_number(self):
        self.assertEqual(7, add("7"))
