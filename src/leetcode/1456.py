from functools import cache
from typing import List


class Solution_Partial_BruteForce:
    def getListOfSize(self, nums, size):
        result = []
        for i in range(len(nums) - size + 1):
            result.append(nums[i: i + size])
        return result

    def dotProduct(self, l1, l2):
        result = 0
        for i in range(len(l1)):
            result += l1[i] * l2[i]
        return result
    
    def getMaxValue(self, l1, l2):
        result = float('-inf')
        for i in l1:
            for j in l2:
                print(i, j, self.dotProduct(i, j))
                result = max(result, self.dotProduct(i, j))
        return result

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        max_length = min(len(nums1), len(nums2))
        result = float('-inf')
        for size in range(max_length, 0, -1):
            nums1_list = self.getListOfSize(nums1, size)
            nums2_list = self.getListOfSize(nums2, size)
            print(nums1_list,"-------" ,nums2_list)
            # result = max(result, self.getMaxValue(nums1_list, nums2_list))

        return result # type: ignore

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            calc = nums1[i] * nums2[j] + dp(i+1, j+1)
            return max(calc, dp(i+1, j), dp(i, j+1))
            
        return dp(0,0)

s = Solution()
print(s.maxDotProduct([2,1,-2,5], [3,0,-6])) # 18