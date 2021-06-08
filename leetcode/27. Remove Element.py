def removeElement(nums, val):
    answer = [num for num in nums if num != val]

    for i in range(len(answer)):
        nums[i] = answer[i]

    nums = nums[:len(answer)]

    return nums


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))
