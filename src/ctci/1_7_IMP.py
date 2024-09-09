'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?
'''

from typing import List


class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        if arr is None or len(arr) != len(arr[0]):
            return
        left, right = 0, len(arr) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                current = arr[top][left + i]
                arr[top][left + i] = arr[bottom - i][left]
                arr[bottom - i][left] = arr[bottom][right - i]
                arr[bottom][right - i] = arr[top + i][right]
                arr[top + i][right] = current
            right -= 1
            left += 1


s = Solution()
ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(ip)
for row in ip:
    print(row)
