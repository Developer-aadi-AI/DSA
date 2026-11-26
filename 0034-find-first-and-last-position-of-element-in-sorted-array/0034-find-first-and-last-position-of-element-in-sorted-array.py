class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        st = -1
        ed = -1
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                st = mid
                high = mid -1
            else:
                low = mid + 1
        if st >= 0:
            low = st
            high = len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] == target:
                    ed = mid
                    low = mid + 1
                else:
                    low = mid + 1

        return [st,ed]