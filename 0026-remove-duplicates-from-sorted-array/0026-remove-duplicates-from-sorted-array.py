class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i + 1]:
        #         k = nums.pop(i)
        #     else:
        #         i += 1

        if nums is None:
            return 0
        write = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[write - 1]:
                nums[write] = nums[i]
                write += 1

        return write
                
