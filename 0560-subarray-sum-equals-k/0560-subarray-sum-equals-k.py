class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        d = {0:1}
        isum = 0
        for i in nums:
            isum += i
            remove = isum - k
            cnt += d.get(remove, 0)
            d[isum] = d.get(isum, 0) + 1
        return cnt
