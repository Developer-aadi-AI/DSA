class Solution:
    def check(self, nums: list[int]) -> bool:
        if nums == sorted(nums):
            return True
        n = len(nums)
        def rev(nums, n):   
            nums.insert(0, nums.pop())
            print(nums, "turururur", n)
            if nums == sorted(nums):
                return True
            else:
                if n:
                    return rev(nums, n-1)
                else:
                    return False
        return rev(nums, n)

        
