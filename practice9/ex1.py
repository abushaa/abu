eps = 1.0
eps2 = eps * 0.5
eps3 = eps2 + 1.0
while eps3 > 1.0:
    eps = eps2
    eps2 = eps * 0.5
    eps3 = eps2 + 1.0
print(eps)