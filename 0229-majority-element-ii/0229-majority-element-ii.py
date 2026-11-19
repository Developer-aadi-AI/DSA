class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt1 = cnt2 = 0
        res1 = res2 = None

        for i in nums:
            if i == res1:
                cnt1 += 1
            elif i == res2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 += 1
                res1 = i
            elif cnt2 == 0:
                cnt2 += 1
                res2 = i
            else:
                cnt1 -= 1
                cnt2 -= 1

        return [
                res 
                for res in (res1, res2)
                if nums.count(res) > len(nums) // 3
                ] 