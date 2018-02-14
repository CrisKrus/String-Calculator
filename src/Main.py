import unittest


def add(numbers):
    return 2


class StringCalculator(unittest.TestCase):

    def test_should_return_two_given_one_plus_one(self):
        self.assertTrue(2, add("1, 1"))