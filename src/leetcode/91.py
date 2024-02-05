class Solution:
    def numDecodings(self, s: str) -> int:
        _set = set(str(i) for i in range(1, 27))
        
        
s = Solution()
print(s.numDecodings("12"))