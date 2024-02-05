from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                prev_level = min(matrix[i-1][j-1] if j > 0 else 100001, matrix[i-1][j], matrix[i-1][j+1] if j < n - 1 else 100001)
                matrix[i][j] += prev_level
        return min(matrix[m - 1])
        
s = Solution()
print(s.minFallingPathSum([[-19, 57],[-40,-5]]))