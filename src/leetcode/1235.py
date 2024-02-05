from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTime = [x[0] for x in jobs]
        @lru_cache()
        def helper(index):
            if index == n:
                return 0
            endIndex = bisect_left(startTime, jobs[index][1])
            return max(helper(index + 1), helper(endIndex) + jobs[index][2])
        return helper(0)


s = Solution()
print(s.jobScheduling(startTime=[1, 2, 3, 3], endTime=[
      3, 4, 5, 6], profit=[50, 10, 40, 70]))
