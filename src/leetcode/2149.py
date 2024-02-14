from typing import List


class Solution:
    # More Space
    def rearrangeArray_MoreSpace(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for n in nums:
            if n > 0:
                positive.append(n)
            else:
                negative.append(n)
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 1
        result = [0] * len(nums)
        for n in nums:
            if n > 0:
                result[positive] = n
                positive += 2
            else:
                result[negative] = n
                negative += 2
        return result


s = Solution()
print(s.rearrangeArray([3, 1, -2, -5, 2, -4]))
