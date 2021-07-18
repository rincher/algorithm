class Solution:
    def reverse(x):
        value = 0
        if x > 0:
            value = int(str(x)[::-1])
        else:
            value = int(str(x * -1)[::-1])
            value = value * -1
        return value

    x = 120
    print(reverse(x))
