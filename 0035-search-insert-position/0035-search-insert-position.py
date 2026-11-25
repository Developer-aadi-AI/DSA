class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def lower(i,j):
            if i > j:
                return i
            mid = (i + j)//2
            if nums[mid] < target:
                return lower(mid+1, j)
            else:
                return lower(i,mid-1)
        return lower(0, len(nums)-1)
        
        
        
        
        
        
        # l = 0
        # r = len(nums) -1
        # while l <= r:
        #     m = l + ((r - l) // 2)
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return l    
            