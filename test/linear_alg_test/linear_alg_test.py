import unittest

from src.linear_alg.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = linear_alg()
        expected_output = 0.0
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
