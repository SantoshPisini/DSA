from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        k = max(count.values())
        A = list(count.elements())
        return [A[i::k] for i in range(k)]


s = Solution()
print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))
