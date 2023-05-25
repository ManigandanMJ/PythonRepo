import unittest
import numpy as np
from src.floor_ceil_rint.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = np.floor(floor_fun())
        expected_output = np.array([ 1.  ,2.  ,3.  ,4.  ,5.  ,6.  ,7.  ,8.  ,9.])
        self.assertEqual(actual_input, expected_output)  # add assertion here
    def test_something1(self):
        actual_input = ceil_fun()
        expected_output = np.array([2.,3.,4.,5.,6.,7., 8.,9. ,10.])
        self.assertEqual(actual_input, expected_output)  # add assertion here
    def test_something2(self):
        actual_input = rint_fun()
        expected_output = np.array([  1.,2.,3.,4.,6.,7.,8.,9.,10.])
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
