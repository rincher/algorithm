def romanToInt(s):
    roman2int = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    charList = list(s)
    intList = []
    for char in charList:
        intList.append(roman2int.get(char))

    retValue = 0

    for i in range(0, len(intList)):
        if i == len(intList) - 1:
            retValue += intList[i]
        elif intList[i] >= intList[i + 1]:
            retValue += intList[i]
        elif intList[i] < intList[i+1]:
            retValue -= intList[i]
    return retValue


s = "VI"
print(romanToInt(s))
