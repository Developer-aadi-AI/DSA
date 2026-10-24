class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        h = n
        while l <= h:
            m = (l + h) // 2
            c = m * (m + 1) / 2
            if  c <= n :
                ans = m
                l = m + 1
            else:
                h = m - 1
        return ans