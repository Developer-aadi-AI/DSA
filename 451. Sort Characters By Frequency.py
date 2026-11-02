def frequencySort(self, s: str) -> str:
        a = {}
        
        for i in set(s):
            a[i] = s.count(i)
        
        a = dict(sorted(a.items(), key=lambda item: item[1], reverse = True))
        b = list(a.keys())
        c = ""

        for i in b:
            c += i * s.count(i)
        return c