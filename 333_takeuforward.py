def isSorted(nums):
        #your code goes here
        l = 0
        r = len(nums) - 1
        def check(l, r):
            if l <= r:
                if nums[l] > nums[r]:
                    return False
                return check(l + 1, r - 1)
            else:
                return True
        return check(l, r)

print(isSorted([1, 2, 3, 2, 4, 5]))