# https://github.com/xSkyCodex/lab10-SC-AG.git
# Partner 1: Skyler Cabrera
# Partner 2: Andres Godoy

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 5), 25)
        self.assertNotEqual(mul(99, 99), 100)
        self.assertEqual(mul(12, 12), 12)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 1), 1)
        self.assertNotEqual(div(10, 2), 27)
        self.assertEqual(div(8, 4), 2)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2)

    
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 7)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertNotEqual(hypotenuse(5, 5), 100)
        self.assertEqual(hypotenuse(6, 7), 11)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()