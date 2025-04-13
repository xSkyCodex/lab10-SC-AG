# https://github.com/xSkyCodex/lab10-SC-AG.git

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Must be real numbers")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    pass


