import sys
import math

T = int(sys.stdin.readline())


def find_gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


def find_lcm(x, y):
    gdc = find_gcd(x, y)
    lcm = (x//gdc)*gdc*(y//gdc)
    return lcm


while T > 0:
    A, B = map(int, sys.stdin.readline().split())
    print(find_lcm(A, B))
    T -= 1
