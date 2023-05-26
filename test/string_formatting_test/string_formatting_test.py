import unittest

from src.string_formatting.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = print_formatted(4)
        expected_output = ['1', '2', '3', '4'], ['1', '2', '3', '4'], ['1', '2', '3', '4'], ['1', '10', '11', '100']
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
