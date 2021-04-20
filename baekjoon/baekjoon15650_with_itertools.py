import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

C = combinations(range(1, N+1), M)
for i in C:
    print(' '.join(map(str, i)))
