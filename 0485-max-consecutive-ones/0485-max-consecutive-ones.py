class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        foundone = 0
        max1 = 0
        for i in nums:
            if i == 1:
                foundone += 1
            else:
                max1 = max(foundone, max1)
                foundone = 0

        return max(foundone, max1)
