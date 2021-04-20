def romanToInt(s):
    roman2int = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
                 "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    value = 0
    cursor = 0
    while cursor < len(s):
        if (cursor+1) != len(s) and s[cursor]+s[cursor+1] in roman2int:
            value += roman2int[s[cursor]+s[cursor+1]]
            cursor += 2
        else:
            value += roman2int[s[cursor]]
            cursor += 1
    return value


s = "MCMXCIV"
print(romanToInt(s))
