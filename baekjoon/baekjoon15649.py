import itertools

N, M = map(int, input().split())

answer = itertools.permutations(range(1,N+1),M)

for i in answer:
    print(' '.join(map(str, i)))
