class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        i = 0
        j = 0
        k = []
        n = len(nums)
        while i < n and j < n:
            while nums[i] < 0:
                i += 1
            while nums[j] > 0:
                j += 1
            k.append(nums[i])
            k.append(nums[j])
            i += 1
            j += 1
        return k