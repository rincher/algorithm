def solve(N):
    array = []
    for i in range(N):
        array.append([0]*N)

    for j in range(N):
        for k in range(N):
            start_node = array[j][k]
            for _ in range(N-1):
                array[j][k+1] = 1
              


    return 0


def test():
    testcases = [(8, 92)]
    for testcase in testcases:
        result = solve(testcase[0])
        if result == testcase[1]:
            print(testcase[0], "is correct")
        else:
            print(testcase[0], "is INCORRECT (output",
                  result, " expected: ", testcase[1], ")")


test()
