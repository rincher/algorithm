def longestCommonPrefix(strs):
    strs.sort(key=lambda x: len(x))

    if len(strs) == 0:
        return ""
    else:
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
