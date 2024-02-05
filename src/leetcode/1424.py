from collections import deque
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        _q = deque()
        _q.append((0, 0))
        result = []
        while _q:
            i, j = _q.popleft()
            result.append(nums[i][j])
            if j == 0 and i < len(nums) - 1:
                _q.append((i + 1, j))
            if j < len(nums[i]) - 1:
                _q.append((i, j + 1))
        return result


s = Solution()
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        
        