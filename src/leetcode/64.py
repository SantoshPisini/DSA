from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]
        for c in range(1, n):
            grid[0][c] += grid[0][c - 1]

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[m - 1][n - 1]

s = Solution()
print(s.minPathSum([[1, 3,1],[1,5,1],[4,2,1]]))