class Solution:
    def pivotInteger_BF(self, n: int) -> int:
        nums = [x for x in range(1, n + 1)]
        i = 0
        while i < len(nums):
            if sum(nums[:i + 1]) == sum(nums[i:]):
                return nums[i]
            i += 1
        return -1

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        total_sum = (n * (n + 1)) // 2
        prefix_sum = [0]
        for i in range(1, n + 1):
            diff = total_sum - prefix_sum[-1]
            if prefix_sum[-1] + i == diff:
                return i
            prefix_sum.append(prefix_sum[-1] + i)
        print(prefix_sum, total_sum)
        return -1


s = Solution()
print(s.pivotInteger(8))
