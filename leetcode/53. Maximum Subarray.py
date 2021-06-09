def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    sum1 = min(nums)
    sum2 = 0
    for i in range(len(nums)):
        if sum2 < 0:
            sum2 = 0
        sum2 += nums[i]
        sum1 = max(sum1, sum2)
    return sum1


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
