import sys

N, K = map(int, sys.stdin.readline().split())
A = []


def find_least_coin(N, K, A):
    cnt = 0
    for _ in range(N):
        num = int(sys.stdin.readline())
        A.append(num)
        A.sort(reverse=True)

    for i in A:
        cnt += K // i
        K %= i
    print(cnt)


find_least_coin(N, K, A)
