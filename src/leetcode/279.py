class Solution:
    # https://leetcode.com/problems/perfect-squares/solutions/4694883/beats-99-users-c-java-python-javascript-explained/
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j, min_val = 0, n
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]


s = Solution()
print(s.numSquares(12))
