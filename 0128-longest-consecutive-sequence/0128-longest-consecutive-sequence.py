class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 1
        for i in nums:
            if i-1 not in nums:
                cnt = 1
                n = i 
                while n+1 in nums:
                    n += 1
                    cnt += 1
                longest = max(cnt, longest)
        return longest

