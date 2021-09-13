import numpy as np
from sympy import var
from sympy import *
from sympy.core.sympify import sympify
from sympy.utilities.lambdify import lambdify

# Compute area from unique best fit quadratics
def simpsonsRule(function, lower, upper, n):
    if lower > upper:
        lower, upper = upper, lower
    
    # Strip width = h
    h = (upper-lower)/n
    xs = np.linspace(lower, upper, n+1)
    ys = [lambdify(var('x'), function)(xi) for xi in xs]

    # h * ( sum of endpoints + 4*sum of odd non-ends + 2*sum of even non-ends) / 3
    # = h * ( 4*sum of all - 2*sum of even non-ends - sum of endpoints) / 3
    return h*(4*sum(ys) - 2*sum(ys[i] for i in range(0,len(ys),2)) - ys[0] - ys[-1])/3


if __name__ == "__main__":
    # Take input function, bounds and strips from the user to integrate over
    print("Enter f(x):")
    func = sympify(input())

    print("Enter lower bound: ")
    try:
        a = float(input())
    except ValueError:
        print("Please enter a float as a lower bound: ")
        a = float(input())
    
    print("Enter upper bound: ")
    try:
        b = float(input())
    except ValueError:
        print("Please enter a float as a lower bound: ")
        b = float(input())
    
    print("Enter an even number of strips: ")
    try:
        n = int(input())
    except ValueError:
        print("Please enter an EVEN NUMBER of strips: ")
        n = int(input())

    print(f"∫f(x)dx from {a} to {b} is " + str(simpsonsRule(func, a, b, n)))