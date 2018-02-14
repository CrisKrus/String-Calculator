import re
import unittest


def add(numbers):
    if len(numbers) == 0:
        return 0

    if numbers[0] == "/" and numbers[1] == "/":
        pattern = "[" + numbers[2] + "\n]"
    else:
        pattern = "[,\n]"

    numbers_split = re.compile(pattern).split(numbers)

    if len(numbers_split) == 1:
        return int(numbers)

    result = 0
    for n in numbers_split:
        if n != "//":
            result += int(n)

    return result


class TestCalculator(unittest.TestCase):

    def test__given_empty_string(self):
        self.assertEqual(0, add(""))

    def test__given_other_delimiters(self):
        self.assertEqual(34, add("//;22; 7 \n5"))

    def test__given_two_numbers(self):
        self.assertEqual(2, add("1, 1"))
        self.assertEqual(10, add("6, 4"))
        self.assertEqual(246, add("123, 123"))
        self.assertEqual(246, add("123 \n 123"))

    def test__given_one_number(self):
        self.assertEqual(7, add("7"))
        self.assertEqual(4, add("4"))
        self.assertEqual(11, add("11"))
        self.assertEqual(1123, add("1123"))

    def test__given_more_than_two_numbers(self):
        self.assertEqual(28, add("1, 2, 3, 4, 5, 6, 7"))
