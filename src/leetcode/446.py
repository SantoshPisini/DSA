from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        result, n = 0, len(nums)
        for i in range(n):
            for prevI in range(i):
                diff = nums[i] - nums[prevI]
                prevCount = dp[(i, diff)]
                prevPrevCount = dp[(prevI, diff)]

                dp[(i, diff)] = prevCount + prevPrevCount + 1
                result += prevPrevCount
        return result


s = Solution()
print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
