def vv(nums):
    res = [nums[-1]]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > res[-1]:
            res.append(nums[i])
    return res[::-1]
print(vv([1, 2, 5, 3, 1, 2]))
print(vv([-3, 4, 5, 1, -4, -5]))
