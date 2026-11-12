class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numdict = {}
        for i in nums:
            numdict[i] = numdict.get(i,0) + 1
        
        for i,j in numdict.items():
            if j >= len(nums)/2:
                return i
        # return -1