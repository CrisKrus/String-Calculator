import unittest


def add(numbers):
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1 or len(numbers) == 2:
        return int(numbers)

    numbers_split = numbers.split(",")
    return int(numbers_split[0]) + int(numbers_split[1])


class TestCalculator(unittest.TestCase):

    def test__given_two_numbers(self):
        self.assertEqual(2, add("1, 1"))
        self.assertEqual(10, add("6, 4"))
        self.assertEqual(246, add("123, 123"))

    def test__given_one_number(self):
        self.assertEqual(7, add("7"))
        self.assertEqual(4, add("4"))
        self.assertEqual(11, add("11"))
        self.assertEqual(1123, add("1123"))

    def test__given_empty_string(self):
        self.assertEqual(0, add(""))
