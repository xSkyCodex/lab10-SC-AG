# https://github.com/xSkyCodex/lab10-SC-AG.git
# Partner 1: Skyler Cabrera
# Partner 2: Andres Godoy

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual((5, 5), 25)
        self.assertNotEqual((99, 99), 100)
        self.assertEqual((12, 12), 12)

    def test_divide(self): # 3 assertions
        self.assertEqual((1, 1), 1)
        self.assertNotEqual((10, 2), 27)
        self.assertEqual((8, 4), 2)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 7)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual((3, 4), 5)
        self.assertNotEqual((5, 5), 100)
        self.assertEqual((6, 7), 11)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
           square_root(-5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()