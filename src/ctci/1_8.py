'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''

from typing import List


class Solution:
    def zeroMatrix(self, arr: List[List[int]]) -> List[List[int]]:
        M, N = len(arr), len(arr[0])

        def setZero(r: int, c: int):
            for i in range(M):
                for j in range(N):
                    if i == r or c == j:
                        arr[i][j] = 0
        positions = []
        for i in range(M):
            for j in range(N):
                if arr[i][j] == 0:
                    positions.append([i, j])
        for r, c in positions:
            setZero(r, c)
        return arr

# Time: O(N*M) + O(K * N * M), where K is number of zero's
# Space: O(K)

s = Solution()
print(s.zeroMatrix([
    [1, 0, 2],
    [1, 3, 2],
    [5, 4, 2],
    [1, 1, 0],
]))
