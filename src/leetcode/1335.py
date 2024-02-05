from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        def helper(start, d) -> int:
            if d == 1:
                return max(jobDifficulty[start:])
            result, maxDifficulty = float("inf"), 0
            for i in range(start, len(jobDifficulty) - d + 1):
                maxDifficulty = max(jobDifficulty[i], maxDifficulty)
                result = min(result, maxDifficulty + helper(i + 1, d - 1))
            return result
        return helper(0, d)


s = Solution()
print(s.minDifficulty([6, 5, 4, 3, 2, 1], 2))
print(s.minDifficulty([9, 9, 9], 3))
print(s.minDifficulty([1, 1, 1], 2))
print(s.minDifficulty([6, 5, 4, 3, 2, 1], 21))
