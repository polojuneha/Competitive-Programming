import unittest
import math

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items')

    high = max(list_of_ints[0], list_of_ints[1])
    low  = min(list_of_ints[0], list_of_ints[1])
    high2 = list_of_ints[0] * list_of_ints[1]
    low2  = list_of_ints[0] * list_of_ints[1]

    high3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]


    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        high3 = max(high3,current * high2,current * low2)

        # new highest product of two
        high2 = max(high2,
                        current * high,
                        current * low)

        # new lowest product of two
        low2 = min(low2,current * high,current * low)

        # new highest
        high = max(high, current)

        # new lowest
        low = min(low, current)

    return high3
    



# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)