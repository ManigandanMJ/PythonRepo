import unittest

from src.Iterators.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = iterables()
        expected_output = 0.8333333333333334
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
