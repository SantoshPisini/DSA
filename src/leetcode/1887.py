from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                result += (i + 1)
        return result
    
    def reductionOperations_LowToHigh(self, nums: List[int]) -> int:
        nums.sort()
        result, _counter = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i -1]:
                _counter += 1
            result += _counter
        return result


s = Solution()
print(s.reductionOperations([5, 1, 3]))
