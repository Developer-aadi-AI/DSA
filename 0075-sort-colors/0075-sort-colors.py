class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0
        n = 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1
            n += 1
        for i in range(n):
            if c0:
                nums[i] = 0
                c0 -= 1
            elif c1:
                nums[i] = 1
                c1 -= 1
            else:
                nums[i] = 2
                c2 -= 1

           