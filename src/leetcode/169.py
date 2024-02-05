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
        