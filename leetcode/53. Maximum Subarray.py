def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    sum1 = min(nums)
    sum2 = 0
    # instead of using range, adding the numbers directly has improved the runtime in leetcode
    for i in nums:
        if sum2 < 0:
            sum2 = 0
        sum2 += i
        sum1 = max(sum1, sum2)
    return sum1


nums = [5, 4, -1, 7, 8]
print(maxSubArray(nums))
