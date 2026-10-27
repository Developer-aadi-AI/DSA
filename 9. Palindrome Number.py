class Solution:

    def isPalindrome(self, x: int) -> bool:
    
        if x < 0:
            return False
        else:
            rev = 0
            a = x
            if x == 0:
                return True
            while a > 0:
                r = a % 10
                rev *= 10
                rev += r
                a //= 10
            if rev == x:
                return True
            else:
                return False
# yessssssssssssssssssssssssssss
