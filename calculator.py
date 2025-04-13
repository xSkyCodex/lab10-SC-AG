# https://github.com/xSkyCodex/lab10-SC-AG.git

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Must be real numbers")
    return math.log(b, a)

def exp(a, b):
    return a ** b




