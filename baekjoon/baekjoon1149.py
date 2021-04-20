import sys


n = int(sys.stdin.readline())
p = []


def find_cheapest(n):
    for i in range(n):
        p.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1, len(p)):
        # i번째 집에 빨강색으로 페인트 칠을 하면, 파란색으로 칠할때랑 초록색으로 칠할때랑 중 가장 작은 값으로
        p[j][0] = min(p[j-1][1], p[j-1][2]) + p[j][0]
        # i번째 집에 초록색으로 페인트 칠을 할때, 빨간색과 파란색중 싼거로
        p[j][1] = min(p[j-1][0], p[j-1][2]) + p[j][1]
        # i번째 집에 파란색으로 페인트 칠을 할때, 빨간색과 초록색 중 싼거로
        p[j][2] = min(p[j-1][0], p[j-1][1]) + p[j][2]
    print(min(p[n-1][0], p[n-1][1], p[n-1][2]))


find_cheapest(n)
