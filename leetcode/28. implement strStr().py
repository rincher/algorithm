def strStr(haystack, needle):
    try:
        index = haystack.index(needle)
        return index
    except ValueError:
        return -1


print(strStr("aaaaaaaaa", "bba"))
