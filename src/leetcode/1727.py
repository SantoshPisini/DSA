from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            
            current_row = sorted(matrix[i], reverse=True)
            for k in range(len(matrix[0])):
                result = max(result, current_row[k] * (k + 1))
        return result

s = Solution()
print(s.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
        