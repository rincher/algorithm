import sys
numbers = list(map(int, sys.stdin.readline().split()))


def solution(numbers):
    n = len(numbers)
    answer = []
    for i in range(n):
        for j in range(i+1, n):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    return answer


print(solution(numbers))
