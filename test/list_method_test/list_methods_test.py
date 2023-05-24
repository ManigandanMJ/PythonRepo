import unittest
from  src.list_method.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = list_methods()
        expected_output = [2]
        self.assertEqual(actual_input,expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
