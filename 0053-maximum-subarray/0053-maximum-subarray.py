class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        res = float('-inf') 
        subarr = []
        for i in nums:
            sum += i
            res = max(sum,res)
            if sum < 0 :
                sum = 0
        return res