class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if nums:
            ic = dc = 1
            mic = mdc  = 0
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    ic += 1
                    mic = max(ic, mic)
                    dc = 1
                elif nums[i] > nums[i+1]:
                    dc += 1
                    mdc = max(dc, mdc)
                    ic = 1
                else:
                    ic = dc = 1
            return max(mic, mdc,ic, dc)
