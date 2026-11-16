class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            mapp = {}
            for i in range(len(nums)):
                check = target - nums[i]
                if check in mapp:
                    return [mapp.get(check), i]
                else:
                    mapp[nums[i]] = i
            return [0]