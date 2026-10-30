def LCM(self, n1, n2):
        if n1 >= 1 and n2 >= 1 and n1 <= 1000 and n2 <= 1000:
            if n1 == n2:
                return n1
            elif n1 % n2 == 0:
                return n1
            elif n2 % n1 == 0:
                return n2
            else:
                a,b = n1,n2
                while a > 0 and b > 0:
                    if a > b:
                        a = a % b
                    else:
                        b = b % a
                gcd = max(a,b)
                return (n1 * n2)//gcd





                
                # Brute Forced below
                # if n1 > n2:
                #     for i in range(2,n2+1):
                #         if (n1 * i) % n2 == 0:
                #             return (n1 * i)
                # else:
                #     for i in range(2,n1+1):
                #         if (n2 * i) % n1 == 0:
                #             return (n2 * i)
