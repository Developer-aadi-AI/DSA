class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        res = float('-inf')
        for i in range(len(nums)):
            if sum == 0:
                start = i 
            sum += nums[i]
            if sum > res:
                res = sum
                subs = start
                sube = i
            if sum < 0:
                sum = 0
        print(nums[subs:sube + 1])
        return res
            