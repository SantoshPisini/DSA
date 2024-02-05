from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = now = last = 0
        for i in range(len(nums) - 1):
            last = max(last, i + nums[i])
            if i == now:
                result += 1
                now = last
        return result

s = Solution()
print(s.jump([2,3,1,1,4]))