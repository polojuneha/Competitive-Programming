def get_max_profit(stock_prices):

    # Calculate max profit
	if len(stock_prices) > 2:
		result = -1000000
		for x in range(0,len(stock_prices)-1):
			for y in range(x+1,len(stock_prices)):
				sum = stock_prices[y] - stock_prices[x]
				if sum > result:
					result = sum
		return result
	if len(stock_prices) < 2:
		raise Exception ("invalid input")


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)