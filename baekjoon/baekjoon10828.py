import sys

T = int(sys.stdin.readline())

array = []


def push(array, N):
    array.append(N)
    return


def pop(array):
    if len(array) == 0:
        return -1
    else:
        return array.pop()


def size(array):
    return len(array)


def empty(array):
    if len(array) == 0:
        return 1
    else:
        return 0


def top(array):
    if len(array) == 0:
        return -1
    else:
        return array[-1]


while T > 0:
    Command = sys.stdin.readline().strip()
    if len(Command) > 5:
        C, N = Command.split()
        N = int(N)
    else:
        C = Command

    if C == "push":
        push(array, N)
    if C == "pop":
        print(pop(array))
    if C == "size":
        print(size(array))
    if C == "empty":
        print(empty(array))
    if C == "top":
        print(top(array))
    T -= 1
