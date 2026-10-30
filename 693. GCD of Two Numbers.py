def GCD(self, n1, n2):
        if n1 >= 1 and n2 >= 1 and n1 <= 1000 and n2 <= 1000:
            if n2 % n1 == 0:
                return n1
            elif n1 % n2 == 0:
                return n2
            l1 = []
            l2 = []
            if n1 % 2 == 0: 
                for i in range(1, n1//2 + 1):
                    if n1 % i == 0:
                        l1.append(i)
                l1.append(n1)
            else:
                for i in range(1, n1//2 + 1, 2):
                    if n1 % i == 0:
                        l1.append(i)
                l1.append(n1)
            
            if n2 % 2 == 0: 
                for i in range(1, n2//2 + 1):
                    if n2 % i == 0:
                        l2.append(i)
                l2.append(n2)
            else:
                for i in range(1, n2//2 + 1, 2):
                    if n2 % i == 0:
                        l2.append(i)
                l2.append(n2)
            
            max = 1
            for i in l1:
                for j in l2:
                    if i == j:
                        max = i
                        break   
            print(l1, l2)
            return max
        else:
            return False