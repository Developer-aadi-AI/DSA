class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        suff = pref = 1
        res = float('-inf')
        n = len(nums) - 1
        for i in range(n + 1):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref *= nums[i]
            suff *= nums[n-i]
            res = max(pref, res, suff)
        return res