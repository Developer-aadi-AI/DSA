class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]
        # if num >= 1 and num < 10 ** 8:
            
        #     s = 0
        #     if num % 2 == 1:
        #         for i in range(1,num//2 + 1,2):
        #             if num % i == 0:
        #                 s += i
        #                 if num < s:
        #                     return False
        #     else:
        #         for i in range(1,num//2 + 1):
        #             if num % i == 0:
        #                 s += i
        #                 if num < s:
        #                     return False
        #     if s == num:
        #         return True
        #     return False
        # else:
        #     return False