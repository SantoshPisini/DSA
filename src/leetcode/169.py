from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element, count = int("-inf"), 0
        for n in nums:
            if count == 0:
                element = n
                
            if element == n:
                count += 1
            else:
                count -= 1
        return element


class Solution_O1_Space:
    def majorityElement(self, nums: List[int]) -> int:
        result = max_count = 0
        for n in nums:
            if max_count == 0:
                result = n
            max_count += (1 if n == result else -1)
        return result
