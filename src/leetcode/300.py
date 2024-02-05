from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        _paths = []
        for n in nums:
            if len(_paths) == 0 or _paths[-1] < n:
                _paths.append(n)
            else:
                id = bisect_left(_paths, n)
                _paths[id] = n
        return len(_paths)



s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
