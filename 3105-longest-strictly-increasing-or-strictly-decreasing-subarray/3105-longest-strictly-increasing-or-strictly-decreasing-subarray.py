class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if nums:
            ic = dc = ans = 1
            
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    ic += 1
                    dc = 1
                elif nums[i] > nums[i+1]:
                    dc += 1
                    ic = 1
                else:
                    ic = dc = 1
                ans = max(ic, dc, ans)
            return ans
