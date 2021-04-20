import sys
import collections

N = int(sys.stdin.readline())
T = []
for i in range(N):
    T.append(int(sys.stdin.readline()))
T.sort()

# avg
print(round(sum(T) / N))

# middle
print(T[N // 2])

# most frequent
H = collections.Counter(T).most_common()
if len(H) > 1:
    if H[0][1] == H[1][1]:
        print(H[1][0])
    else:
        print(H[0][0])
else:
    print(H[0][0])

# range
print(T[-1] - T[0])
