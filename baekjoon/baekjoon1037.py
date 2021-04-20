import sys

N = int(sys.stdin.readline())
p = []

p = list(map(int, sys.stdin.readline().split()))

print(max(p)*min(p))
