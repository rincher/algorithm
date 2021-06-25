class Solution:
    def getRow(rowIndex):
        result = []
        first_line = [1]
        second_line = [1, 1]
        if rowIndex == 0:
            result = first_line
            return result
        if rowIndex == 1:
            result = second_line
            return result
        for i in range(2, rowIndex):
            this_list = list(range(i+1))
            this_list[0] = 1
            this_list[i] = 1
            for j in range(1, i):
                this_list[j] = result[i - 1][j - 1] + result[i - 1][j]
            result = this_list
        return result

    rowIndex = 3
    print(getRow(rowIndex))
