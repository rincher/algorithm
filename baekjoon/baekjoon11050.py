import sys

a, b = map(int, sys.stdin.readline().split())


def find_binomial_factorial(a, b):
    nom = 1
    x = 1
    y = 1
    denom = 1

    for i in range(1, a+1):
        nom = nom * i

    for j in range(1, b+1):
        x = x * j

    for k in range(1, (a-b)+1):
        y = y * k

    denom = x * y

    print(nom//denom)


find_binomial_factorial(a, b)
