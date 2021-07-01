class Solution:
    def plusOne(digits):
        answer = ""
        number = ""
        array = []

        for digit in digits:
            number += str(digit)

        answer = int(number) + 1

        for char in str(answer):
            array.append(char)
        return array

    digits = ["1", "2", "3"]
    print(plusOne(digits))
