from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()
            
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]

            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            if dp[i] > 0:
                queue.append(i)
            
        return max(dp)

s = Solution()
print(s.constrainedSubsetSum([10,2,-10,5,20], 2))