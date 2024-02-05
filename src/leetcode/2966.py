from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i+1] <= k and nums[i+1] - nums[i] <= k and nums[i+2] - nums[i] <= k:
                result.append(nums[i:i+3])
            else:
                return []
        return result


s = Solution()
print(s.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
print(s.divideArray([1, 3, 3, 2, 7, 3], 3))
print(s.divideArray([15, 13, 12, 13, 12, 14, 12, 2, 3,
      13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2], 2))
