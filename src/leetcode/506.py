import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap_score = [(-x, i) for i, x in enumerate(score)]
        heapq.heapify(heap_score)
        result = [''] * len(score)
        rank = 1
        while heap_score:
            val = heapq.heappop(heap_score)
            if rank == 1:
                result[val[1]] = 'Gold Medal'
            elif rank == 2:
                result[val[1]] = 'Silver Medal'
            elif rank == 3:
                result[val[1]] = 'Bronze Medal'
            else:
                result[val[1]] = str(rank)
            rank += 1
        return result


s = Solution()
print(s.findRelativeRanks([10, 3, 8, 9, 4]))
