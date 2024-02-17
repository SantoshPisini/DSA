from heapq import heappop, heappush
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heappush(q, diff)
            if len(q) > ladders:
                bricks -= heappop(q)
            if bricks < 0:
                return i
        return len(heights) - 1

    def furthestBuilding_TLE(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        steps = 0
        for i in range(len(heights) - 1):
            if heights[i + 1] <= heights[i]:
                continue
            diff_height = heights[i + 1] - heights[i]
            if len(q) < ladders:
                q.append(diff_height)
            else:
                if not q:
                    steps += diff_height
                else:
                    min_val = min(q)
                    if diff_height < min_val:
                        steps += diff_height
                    else:
                        q.remove(min_val)
                        steps += min_val
                        q.append(diff_height)
            if steps == bricks:
                return i + 1
            elif steps > bricks:
                return i
        return i + 1


s = Solution()
print(s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
print(s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
print(s.furthestBuilding([14, 3, 19, 3], 17, 0))
print(s.furthestBuilding([2, 7, 9, 12], 5, 1))
