from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        times = result = 0
        while k:
            val = happiness.pop() - times
            if val < 0:
                break
            result += val
            times += 1
            k -= 1
        return result



s = Solution()
print(s.maximumHappinessSum([1, 2, 3], 2))