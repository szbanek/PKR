import sys
import random
import numpy as np
import math

t = int(sys.argv[1])
n = int(sys.argv[2])
p = int(sys.argv[3])
s = int(sys.argv[4])

a = np.array([s]+[random.randrange(0, p) for _ in range(t-1)])

print(a)

shares = [sum([a[y]*pow(x, y) for y in range(t)])%p for x in range(1, n+1)]

shares = [(shares[i], i+1) for i in range(n)]

# print(shares)

random.shuffle(shares)
print(shares[:t])

lagrange_poly = []

for j in range(t):
    l = 1
    x0 = shares[j][1]
    for i in range(t):
        if i!=j:
            x1 = shares[i][1]
            l *= x1*pow(x1-x0, -1, p)
    lagrange_poly.append(l%p)

print(lagrange_poly)
res = sum([(lagrange_poly[i]*shares[i][0]) for i in range(len(lagrange_poly))])%p

print(res)