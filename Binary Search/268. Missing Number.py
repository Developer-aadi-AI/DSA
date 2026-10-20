# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         n = len(nums)
#         return (n * (n + 1) // 2) - sum(nums) 

def missingNumber(nums: list[int]) -> int:
        result = 0
    
        for counter,value in enumerate(nums):
        
            result ^= counter+1 # XOR result with numbers from the complete series
            print(f"counter {counter}, result {result} ")
            result ^= value # XOR with the numbers given in num series
            print(f"value {value}, result {result} ")
            print("*" * 20)
        return result

n = [3,0,1]

print("Missing : ", missingNumber(n))