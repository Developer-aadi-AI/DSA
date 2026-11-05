class Solution:
    def check(self, nums: list[int]) -> bool:
        # if nums == sorted(nums):
        #     return True
        # n = len(nums)
        # def rev(nums, n):   
        #     nums.insert(0, nums.pop())
        #     if nums == sorted(nums):
        #         return True
        #     else:
        #         if n:
        #             return rev(nums, n-1)
        #         else:
        #             return False
        # return rev(nums, n)

        
        if nums:
            count = 0
            for i in range(len(nums) - 1):
                if nums[i] >  nums[i+1]:
                    count += 1
                
            if nums[-1] > nums[0]:
                count += 1

            if count > 1:
                return False
            return True    
