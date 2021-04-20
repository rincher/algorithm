import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
time_taken = 0
P.sort()
for i in range(N):
    if i == 0:
        P[i] = P[i]
    if i >= 1:
        P[i] = P[i] + P[i-1]
    time_taken += P[i]
print(time_taken)
