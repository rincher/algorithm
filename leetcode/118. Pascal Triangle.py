class Solution:
    def generate(numRows):
        result = []
        first_line = [1]
        second_line = [1, 1]
        if numRows == 0:
            return result

        result.append(first_line)
        if numRows == 1:
            return result

        result.append(second_line)
        if numRows == 2:
            return result

        for i in range(2, numRows):
            this_list = list(range(i + 1))
            this_list[0] = 1
            this_list[i] = 1
            for j in range(1, i):
                this_list[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(this_list)
        return result

    numRows = 3
    print(generate(numRows))
