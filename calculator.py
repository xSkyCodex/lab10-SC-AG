# https://github.com/xSkyCodex/lab10-SC-AG.git
# Partner 1: Skyler Cabrera
# Partner 2: Andres Godoy
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
    if b == 0:
        raise ValueError("Division by 0.")
    return a / b

def logarithm(base, argument):
    if base <= 0 or argument <= 0:
        raise ValueError("Base and argument must be positive numbers.")
    return math.log(argument, base)

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def square_root(n):
    if n < 0:
                raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(n)

