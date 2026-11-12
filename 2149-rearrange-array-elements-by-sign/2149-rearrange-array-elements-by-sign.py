class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        even = 0
        odd = 1
        res = [0] * len(nums)
        for i in nums:
            if i > 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res 
        # i = 0
        # j = 0
        # k = []
        # n = len(nums)
        # while i < n and j < n:
        #     while nums[i] < 0:
        #         i += 1
        #     while nums[j] > 0:
        #         j += 1
        #     k.append(nums[i])
        #     k.append(nums[j])
        #     i += 1
        #     j += 1
        # return k


