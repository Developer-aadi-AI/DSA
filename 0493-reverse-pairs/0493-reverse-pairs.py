class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def mergeSort(arr):
            n = len(arr)
            cnt = 0
            
            if n<=1:
                return cnt
            mid = n//2
            left_half = arr[:mid]
            right_half = arr[mid:]

            cnt += mergeSort(left_half)
            cnt += mergeSort(right_half)
            cnt += countPairs(left_half, right_half)

            merge(arr, left_half, right_half)

            return cnt

        def countPairs(left, right):
            j = 0
            cnt = 0
            for i in left:
                while j < len(right) and i > right[j] * 2: 
                    j+= 1
                cnt += j
            return cnt

        def merge(arr, left, right):
            new = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1
                
            new.extend(left[i:])
            new.extend(right[j:])

            arr[:] = new

        return mergeSort(nums)