class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        for i in s:
            if 96<ord(i)<123 or 47<ord(i)<58:
                s1 += i 
        n = len(s1)
        def pal(p, l, n):
            if l > n//2:
                return True
            else:
                r = n - (l + 1)
                if p[l] !=  p[r]:
                    return False
                else:
                    return pal(p,l+1, n)
        if s1:
            return pal(s1, 0, n)
        else: 
            return True
        