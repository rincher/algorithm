import sys
from collections import deque


def dfs(array , start_node):
    visted = []
    stack = [start_node]

    while stack:
        n = stack.pop()
        if n not in visted:
            visted.append(n)
            if n in array:
                

N, M, V = map(int, sys.stdin.readline().split())

array = {}
for i in range(N):
    array[i+1] = set()

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    array[a].add(b)
    array[b].add(a)

print(dfs(array, V))