from math import *
def f(x):
    if 5/4+1/x**15 != 0:
        y=log((1/(exp(sin(x)+1)))/(5/4+1/x**15), 1+x**2)
        return y
    else:
        return None

print(f(1), f(10), f(1000))
