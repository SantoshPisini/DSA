from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations), 0, -1):
            if citations[i - 1] >= i:
                return i
        return 0


s = Solution()
print(s.hIndex([1, 3, 1]))
