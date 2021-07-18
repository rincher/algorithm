def mysqrt(x):
    x = 8
    i = 1
    j = x

    while i < j:
        mid = (i+j)//2
        if mid * mid > x:
            j = mid
        else:
            i = mid + 1

    return i - 1


print(mysqrt(8))
