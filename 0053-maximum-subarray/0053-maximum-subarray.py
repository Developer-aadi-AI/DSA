class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        res = float('-inf')
        for i in nums:
            sum += i
            if sum > res:
                res = sum

            if sum < 0:
                sum = 0
        return res
            