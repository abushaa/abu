from math import *
def A(x):
    if x!=1:
        y=(x**7+2*x**3-3/(1+x**2))/(1/(1-x)+21/8)
        return y
    else:
        return None

def B(x):
    if x>0 and x!=1:
        z=1/((sin(x/(x**2+2)))**2+exp(log(x)+1))
        return z
    else:
        return None

for x in range (1,11):
    print(x, A(x), B(x))