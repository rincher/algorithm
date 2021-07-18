class Solution:
    def searchInsert(nums, target):
        lowest = 0
        highest = len(nums) - 1
        while lowest <= highest:
            mid = (lowest + highest) // 2
            if nums[mid] > target:
                highest = mid - 1
            elif nums[mid] < target:
                lowest = mid + 1
            else:
                return mid
        return lowest

    nums = [1, 3, 5, 6]
    target = 7
    print(searchInsert(nums, target))
