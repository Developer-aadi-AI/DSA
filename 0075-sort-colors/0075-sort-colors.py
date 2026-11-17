class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Optimal solution
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid<=high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                
        # # Brute Forced Solution
        # c0 = 0
        # c1 = 0
        # c2 = 0
        # n = 0
        # for i in nums:
        #     if i == 0:
        #         c0 += 1
        #     elif i == 1:
        #         c1 += 1
        #     else:
        #         c2 += 1
        #     n += 1
        # for i in range(n):
        #     if c0:
        #         nums[i] = 0
        #         c0 -= 1
        #     elif c1:
        #         nums[i] = 1
        #         c1 -= 1
        #     else:
        #         nums[i] = 2
        #         c2 -= 1

           