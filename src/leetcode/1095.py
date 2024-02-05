# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#        pass
   
#    def length(self) -> int:
#        pass

class Solution:
    # def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    def findInMountainArray(self, target: int, mountain_arr) -> int:
        n = mountain_arr.length()
        # Find peak
        low, high = 1, n - 2
        while low != high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low
        # Forward Binary Search
        low, high = 0, peak
        while low != high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid
        if mountain_arr.get(low) == target:
            return low
        # Reserse Binary Search
        low, high = peak + 1, n - 1
        while low != high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) > target:
                low = mid + 1
            else:
                high = mid
        if mountain_arr.get(low) == target:
            return low
        return -1