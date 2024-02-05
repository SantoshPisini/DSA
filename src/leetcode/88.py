from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for _ in range(n):
            nums1.pop()
        i = 0
        for num in nums2:
            while nums1[i] < num:
                i += 1
            nums1.insert(i, num)
        

s = Solution()
nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1, 2, 2]
s.merge(nums1, 6, nums2, 3)
print(nums1)