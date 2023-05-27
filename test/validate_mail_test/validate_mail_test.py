import unittest

from src.validate_mail.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = validate_mail()
        expected_output = "mani_1@gmail.com,manu_2@gmail.com,tina_1@gmail.com"
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
