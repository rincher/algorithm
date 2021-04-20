import sys

N = int(input())
array = []

for _ in range(N):
    array.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
