import unittest
from src.marks_percentage.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # actual input :2, jeeva 55 77 89, sima 89 78 87, sima
        actual_input = average_marks()
        expected_output = ('sima', '84.67')
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
