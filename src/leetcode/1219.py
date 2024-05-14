from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = 0

        def maxGold(m, n) -> int:
            if not (0 <= m < len(grid) and 0 <= n < len(grid[0])) or grid[m][n] == 0:
                return 0
            max_gold = 0
            current_gold = grid[m][n]
            # To mark it as visited
            grid[m][n] = 0
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, maxGold(m + x, n + y))
            # Revert: To mark it as visited
            grid[m][n] = current_gold
            return max_gold + current_gold

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                result = max(result, maxGold(m, n))
        return result


s = Solution()
print(s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))

