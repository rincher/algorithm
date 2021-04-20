import sys


def get_minimum_days(m, n, array):
    # print(m, n, array)
    day_count = 0
    yesterday_array = []

    for i in range(n):
        temporary_array = []
        for j in range(m):
            temporary_array.append(2)
        yesterday_array.append(temporary_array)

    # while문 종료조건
    while True:
        # 종료조건 1: 모든 값이 1 혹은 -1 이면 종료 (day_count 리턴)
        count = 0

        for i in range(n):
            for j in range(m):
                if array[i][j] == 1 or array[i][j] == -1:
                    count += 1

        if count == m*n:
            return day_count

        # 종료조건 2: 종료조건 1에 일치하지 않고, 전날의 array가 오늘 array와 완전히 같으면 -1을 반환
        new_count = 0
        for i in range(n):
            for j in range(m):
                if yesterday_array[i][j] == array[i][j]:
                    new_count += 1
        if new_count == m*n:
            return -1

        # 종료조건을 피했을때
        # yesterday_array = array[:]

        for i in range(n):
            for j in range(m):
                yesterday_array[i][j] = array[i][j]

        for i in range(n):
            for j in range(m):
                if yesterday_array[i][j] == 1:
                    if i - 1 >= 0 and yesterday_array[i - 1][j] == 0:
                        array[i - 1][j] = 1
                    if i + 1 < n and yesterday_array[i + 1][j] == 0:
                        array[i + 1][j] = 1
                    if j - 1 >= 0 and yesterday_array[i][j - 1] == 0:
                        array[i][j - 1] = 1
                    if j + 1 < m and yesterday_array[i][j + 1] == 0:
                        array[i][j + 1] = 1

        day_count += 1

    return day_count


def submit():
    m, n = map(int, sys.stdin.readline().split())
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().split())))
    print(get_minimum_days(m, n, array))


def test():
    testcases = [
        (6, 4, [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]], 8),
        (6, 4, [[0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]], -1),
        (6, 4, [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]], 6),
        (5, 5, [[-1, 1, 0, 0, 0], [0, -1, -1, -1, 0], [0, -1, -
                                                       1, -1, 0], [0, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0]], 14),
        (2, 2, [[1, -1], [-1, 1]], 0)
    ]

    for testcase in testcases:
        result = get_minimum_days(testcase[0], testcase[1], testcase[2])

        if result == testcase[3]:
            print("Test Pass")
        else:
            print("Test FAIL: (result:", result, " expected: ", testcase[3])


test()
# submit()
