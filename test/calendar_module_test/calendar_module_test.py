import unittest
from src.calendar_module.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = calendar_module()
        expected_input = "WEDNESDAY"
        self.assertEqual(actual_input,expected_input)  # add assertion here


if __name__ == '__main__':
    unittest.main()
