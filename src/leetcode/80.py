from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        item, count, i = nums[0], 1, 1
        while i < len(nums):
            if item == nums[i]:
                if count > 1:
                    nums.pop(i)
                    i -= 1
                else:
                    count += 1
            else:
                item = nums[i]
                count = 1
            i += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))