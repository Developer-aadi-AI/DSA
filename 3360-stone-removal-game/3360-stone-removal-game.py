class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, 0, -2):
            if n >= i:
                n -= i
                if n < i-1:
                    return True
                else:
                    n -= i-1
            else:
                return False
        return False

        
        # f = 10
        # while n > 0:
        #     if n >= f:
        #         n -= f
        #         f -= 1
        #         if n >= f:
        #             n -= f
        #             f -= 1
        #             if n == 0:
        #                 return False
        #         else:
        #             return True
        #     else:
        #         return False
