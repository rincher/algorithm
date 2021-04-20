import sys

T = int(sys.stdin.readline())


def all_cases(N, M):

    nom = 1
    denom = 1
    x = 1
    y = 1

    for i in range(1, M + 1):
        nom = nom * i

    for j in range(1, (M-N)+1):
        x = x * j

    for k in range(1, N+1):
        y = y*k

    denom = x * y
    return (nom//denom)


while T > 0:
    N, M = map(int, sys.stdin.readline().split())
    print(all_cases(N, M))
    T -= 1
