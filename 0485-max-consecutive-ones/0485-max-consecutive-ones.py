class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        foundone = 0
        max1 = 0
        for i in nums:
            if i == 1:
                foundone += 1
                max1 = max(foundone, max1)
            else:
                foundone = 0

        return max1