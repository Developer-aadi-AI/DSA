class Solution:
    def reverse(self, x: int) -> int:
        check1 = -(2 ** 31)
        check2 = (2 ** 31) - 1
        a = x
        rev = 0 
        if x == 0:
            return 0
        if a < 0:
            a = a * (-1)
        while a > 0:
            r = a % 10
            rev *= 10
            rev += r
            a //= 10
        if rev > check1 and  rev < check2:
            if x < 0:    
                return rev * (-1)
            else:
                return rev
        else:
            return 0    