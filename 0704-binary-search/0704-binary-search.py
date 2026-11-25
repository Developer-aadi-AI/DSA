class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def binar(i,j):
            if i>j:
                return -1
        
            mid = (i + j)//2
        
            if nums[mid] == target:
                return mid
        
            elif nums[mid] < target:
                return binar(mid+1, j)
        
            else:
                return binar(i,mid-1)
        
        return binar(0,len(nums)-1)








        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     m = l + ((r - l) // 2)
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return -1