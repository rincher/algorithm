import math
import sys
a, b = map(int, sys.stdin.readline().split())
33, 12
p = []
q = []


def Greatest_common_factor(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


def Least_common_multiplier(x, y):
    gcd = Greatest_common_factor(x, y)
    lcm = ((a // gcd) * gcd * (b//gcd))
    return lcm


print(Greatest_common_factor(a, b))
print(Least_common_multiplier(a, b))
