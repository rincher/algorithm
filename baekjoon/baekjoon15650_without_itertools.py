import sys

N, M = map(int, sys.stdin.readline().split())
visited = [0]*N
out = []


def solve(depth, idx, N, M):
    if depth == M:
        print(" ".join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            out.append(i+1)
            solve(depth + 1, i+1, N, M)
            visited[i] = 0
            out.pop()


solve(0, 0, N, M)
