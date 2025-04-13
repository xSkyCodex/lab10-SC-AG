# https://github.com/xSkyCodex/lab10-SC-AG.git
# Partner 1: Skyler Cabrera
# Partner 2: Andres Godoy

import math

def add(a ,b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return b / a

def logarithm(base, argument):
    if a <= 0 or b <= 0:
        raise ValueError("Must be real numbers or greater than zero!")
    return math.log(argument, base)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Must be a real number!")
    return math.sqrt(a)

def hypotenuse(a, b):
    a = abs(a)
    b = abs(b)
    return math.hypot(a, b)

