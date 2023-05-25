import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = 'abrackdabra'
        expected_output = 'abrackdabra'
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
