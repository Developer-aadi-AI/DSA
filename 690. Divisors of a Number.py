def divisors(self, n):
        if 0<n<1001:
            r = []
            if n % 2 == 0:
                for i in range(1, (n//2)+1):
                    if n % i == 0:
                        r.append(i)
                r.append(n)
                return r
            else:
                for i in range(1, (n//2)+1, 2):
                    if n % i == 0:
                        r.append(i)
                r.append(n)
                return r