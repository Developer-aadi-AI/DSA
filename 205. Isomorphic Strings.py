def isIsomorphic(self, s: str, t: str) -> bool:        
    d = {}
    l = []
    for i in range(len(s)):
        if d.get(s[i], False):
            if d.get(s[i]) != t[i]:
                return False
        else:
            if t[i] not in l:
                d[s[i]] = t[i]
                l.append(t[i])
            else:
                return False
    return True
