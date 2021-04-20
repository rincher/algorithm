import sys
from collections import deque

def DFS(start_node):
    print(start_node, end=" ")
    visited[start_node] = 1

    for i in range(N+1):
        if visited[i] == 0 and array[start_node][i] == 1:
            DFS(i)

def BFS(start_node):
    queue = [start_node]
    visited[start_node] = 0
    while queue:
        start_node = queue[0]
        print(start_node, end=" ")
        del queue[0]
        for i in range(1, N+1):
            if visited[i] == 1 and array[start_node][i] == 1:
                queue.append(i)
                visited[i] = 0



N, M, V = map(int, sys.stdin.readline().split())
array = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for i in range(1, M + 1):
    a, b = map(int, sys.stdin.readline().split())
    array[a][b] = 1
    array[b][a] = 1


DFS(V)
print("")
BFS(V)