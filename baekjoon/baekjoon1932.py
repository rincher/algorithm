import sys

N = int(sys.stdin.readline())
p = []
for i in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            p[i][j] = p[i][j] + p[i-1][j]
        elif i == j:
            p[i][j] = p[i][j] + p[i-1][j-1]
        else:
            p[i][j] = max(p[i - 1][j - 1], p[i-1][j]) + p[i][j]

print(max(p[N-1]))
