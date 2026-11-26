class Solution:
    def canAliceWin(self, n: int) -> bool:
        f = 10
        while n > 0:
            if n >= f:
                n -= f
                f -= 1
                if n >= f:
                    n -= f
                    f -= 1
                    if n == 0:
                        return False
                else:
                    return True
            else:
                return False
