class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                k = nums.pop(i)
            else:
                i += 1