class Solution():
    def urlIfy(self, s: str) -> str:
        return s.replace(' ', '%20')

s = Solution()
print("test search", "->", s.urlIfy("test search"))
