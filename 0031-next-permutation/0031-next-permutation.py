class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 2
        while j>=0 and nums[j] >= nums[j+1]:
            j -= 1
        print(j)
        if j == -1:
            nums[:] = sorted(nums[:])
            return nums
            
        
        
        for i in range(n-1,j, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
            
        nums[j+1:] = reversed(nums[j+1:])
        