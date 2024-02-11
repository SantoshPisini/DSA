from functools import cache
from typing import List

# NeetCode


class Solution:
    # Not Space Efficient
    def cherryPickup_SpaceEater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        PATHS = [-1, 0, 1]

        @cache
        def dfs(r, c1, c2) -> int:
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == col:
                return 0
            if r == row - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1_i in PATHS:
                for c2_i in PATHS:
                    res = max(res, dfs(r + 1, c1_i + c1, c2 + c2_i))
            return res + grid[r][c1] + grid[r][c2]

        return dfs(0, 0, col - 1)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        PATHS = [-1, 0, 1]
        _dp = [[0] * col for _ in range(col)]
        for r in range(row - 1, -1, -1):
            local_dp = [[0] * col for _ in range(col)]
            for c1 in range(col - 1):
                for c2 in range(c1 + 1, col):
                    res = grid[r][c1] + grid[r][c2]
                    max_res = 0
                    for c1_i in PATHS:
                        for c2_i in PATHS:
                            if c1_i + c1 < 0 or c2 + c2_i == col:
                                continue
                            max_res = max(
                                max_res, _dp[c1_i + c1][c2 + c2_i] + res)
                    local_dp[c1][c2] = max_res
            _dp = local_dp
        return _dp[0][col - 1]


s = Solution()
print(s.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
