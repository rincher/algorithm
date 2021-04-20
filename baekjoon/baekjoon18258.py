import sys
from collections import deque

N = int(sys.stdin.readline())
array = deque()


def push(array, number):
    array.append(number)


def pop(array):
    if len(array) == 0:
        return -1
    else:
        return array.popleft()


def front(array):
    if len(array) == 0:
        return -1
    else:
        return array[0]


def back(array):
    if len(array) == 0:
        return -1
    else:
        return array[-1]


def size(array):
    return len(array)


def empty(array):
    if len(array) == 0:
        return 1
    else:
        return 0


while N > 0:
    Command = sys.stdin.readline().strip()
    if len(Command) > 5:
        C, number = Command.split()
        number = int(number)
    else:
        C = Command

    if C == "push":
        push(array, number)

    if C == "front":
        print(front(array))

    if C == "back":
        print(back(array))

    if C == "pop":
        print(pop(array))

    if C == "size":
        print(size(array))

    if C == "empty":
        print(empty(array))
    N -= 1
