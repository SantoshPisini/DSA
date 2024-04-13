from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = startMax = endMax = 0
        startIdx, endIdx = 0, len(height) - 1

        while startIdx < endIdx:
            if height[startIdx] < height[endIdx]:
                startMax = max(startMax, height[startIdx])
                result += (startMax - height[startIdx])
                startIdx += 1
            else:
                endMax = max(endMax, height[endIdx])
                result += (endMax - height[endIdx])
                endIdx -= 1
        return result


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
