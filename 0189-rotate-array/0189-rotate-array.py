class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            n = len(nums)
            if k < n:
                rotated = nums[n - k : ]
                del nums[n - k : ]
                nums[0:0] = rotated
            elif k > n:
                while k > n:
                    k -= n
                rotated = nums[n - k : ]
                del nums[n - k : ]
                nums[0:0] = rotated
            
                