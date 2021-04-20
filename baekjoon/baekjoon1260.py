import sys


def DFS(start_node):
    # 시작한 노드 출력 -> 다음 노드 출력
    print(start_node, end=" ")
    # 시작한 노드는 이미 갔다 옴을 표시 하기 위해서 1로 설정
    visited[start_node] = 1
    for i in range(N+1):
        # visted 하지 않았고 입력 받은 좌표가 맞으면 DFS 재귀
        if visited[i] == 0 and edge[start_node][i] == 1:
            DFS(i)


def BFS(start_node):
    # queue 에서 노드 값을 넣고
    queue = [start_node]
    # 시작하기 전에 DFS에서 1로 한것을 초기화
    visited[start_node] = 0
    while queue:
        start_node = queue[0]
        # queue 있는 노드를 출력하고
        print(start_node, end=" ")
        # 다음에 올 노드를 위해서 비우기
        del queue[0]
        for i in range(1, N+1):
            if visited[i] == 1 and edge[start_node][i] == 1:
                queue.append(i)
                visited[i] = 0


N, M, V = map(int, sys.stdin.readline().split())

edge = [[0] * (N+1) for _ in range(N+1)]
visited = [0 for __ in range(N+1)]

for j in range(1, M+1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a][b] = 1
    edge[b][a] = 1

DFS(V)
print("")
BFS(V)
