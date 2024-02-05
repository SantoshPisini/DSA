from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        _set, i = set(), 0
        while i < len(nums):
            if nums[i] in _set:
                nums.pop(i)
                i -= 1
            else:
                _set.add(nums[i])
            i += 1
        return len(nums)


s = Solution()
print(s.removeDuplicates([1,1,2]))
