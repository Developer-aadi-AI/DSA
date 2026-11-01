if len(strs) == 1:
            return strs[0]
        ans = ""
        strs.sort()
        min_len = len(strs[0])
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
        
        for i in range(min_len):
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
            else:
                return ans
        return ans