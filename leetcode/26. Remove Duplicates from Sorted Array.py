class Solution:
    def removeDuplicates(nums):
        array = list(sorted(set(nums)))

        for i, v in enumerate(array):
            nums[i] = v

        return len(array)

    nums = [1, 1, 2]
    length = removeDuplicates(nums)
    print(length, nums[:length])
