def largestOddNumber(self, num: str) -> str:
        if 0<len(num)<=10**5:
            l = 0
            r = len(num) - 1
            while num[l] == "0":
                l += 1
            while l <= r:
                if int(num[r]) % 2 == 0:
                    r -= 1
                else:
                    return num[l:r+1]
            return ""
        else:
            return ""