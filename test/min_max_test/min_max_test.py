import unittest

from src.min_max.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = min_max()
        expected_output = 3
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
