# https://github.com/xSkyCodex/lab10-SC-AG.git
# Partner 1: Skyler Cabrera
# Partner 2: Andres Godoy

import math

def add(a ,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return b / a

def logarithm(a, b):
    if a >= 0 or b >= 0:
        raise ValueError("Must be real numbers or greater than zero!")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


