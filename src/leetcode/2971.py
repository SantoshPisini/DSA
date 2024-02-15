from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = -1
        for i in range(1, len(nums)):
            current = nums[i]
            nums[i] += nums[i - 1]
            if current < nums[i - 1]:
                result = nums[i]
        return result


s = Solution()
print(s.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
print(s.largestPerimeter([5, 5, 50]))
