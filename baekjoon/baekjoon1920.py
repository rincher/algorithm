import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
for i in B:
    lowest = 0
    highest = N - 1
    answer = 0
    while lowest <= highest:
        middle = (highest + lowest) // 2
        if A[middle] == i:
            answer = 1
            break
        elif i < A[middle]:
            highest = middle - 1
        else:
            lowest = middle + 1
    print(answer)
