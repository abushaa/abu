x0=4
x1=4.25
def f(y,z):
    global a
    a=108-(815-1500/z)/y
    return a
for i in range (31):
    f(x1,x0)
    [x0,x1]=[x1,x0]
    x1=a
print(a)
