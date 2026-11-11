class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        arr = []
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                arr.append(nums[i])
        for i in range(n - len(arr)):
            arr.append(0)
        nums[:] = arr
        