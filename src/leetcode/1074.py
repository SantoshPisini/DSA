from typing import List


class Solution:
    def subMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        for m in range(i, k + 1):
                            for n in range(j, l + 1):
                                print(matrix[m][n], end=' ')
                            print()
                        print()

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        self.subMatrix(matrix)
        return -99


s = Solution()
print(s.numSubmatrixSumTarget([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0))
# print(s.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
