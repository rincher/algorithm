def getRow(rowIndex):
    DP = [0] * (rowIndex + 1)
    for i in range(len(DP)):
        DP[i] = [0] * (i+1)
    DP[0][0] = 1
    for i in range(rowIndex + 1):
        for j in range(i+1):
            if j == 0 or j == i:
                DP[i][j] = 1
            else:
                DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

    return DP[rowIndex]


rowIndex = 3
print(getRow(rowIndex))
