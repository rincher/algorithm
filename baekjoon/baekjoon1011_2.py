import sys


def solve(distance):
    distance_travelled = 0
    turns = 0
    speed = 0

    while distance_travelled < distance:
        speed += 1

        # add left
        turns += 1
        distance_travelled += speed
        if distance_travelled >= distance:
            break

        # add right
        turns += 1
        distance_travelled += speed
        if distance_travelled >= distance:
            break

    return turns


def submit():
    T = int(sys.stdin.readline())

    while T:
        T -= 1
        x, y = map(int, sys.stdin.readline().split())
        result = solve(y-x)
        print(result)


def test():
    testcases = [(1, 1), (2, 2), (3, 3), (4, 3), (5, 4), (6, 4), (7, 5), (8, 5),
                 (9, 5), (10, 6), (11, 6), (12, 6), (13, 7), (14, 7), (15, 7), (16, 7), (17, 8)]

    for testcase in testcases:
        result = solve(testcase[0])

        if result == testcase[1]:
            print(testcase[0], "is correct")
        else:
            print(testcase[0], "is INCORRECT (output",
                  result, " expected: ", testcase[1], ")")


# test()
submit()
