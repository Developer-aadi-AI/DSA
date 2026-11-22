class Solution:
    def checkString(self, s: str) -> bool:
        ans = True
        j = 0
        while j< len(s):
            if s[j] == 'b':
                break
            j += 1
        while j < len(s):
            if s[j] == 'a':
                return False
            j += 1
        return True 
        
        