import sys

N = int(sys.stdin.readline())
array = []


for i in range(N):
    K = int(sys.stdin.readline())
    if K == 0:
        array.pop()
    else:
        array.append(K)
print(sum(array))
