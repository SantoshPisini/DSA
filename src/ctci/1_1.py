class Solution():
    def hasUniqueChar(self, s: str) -> bool:
        if len(s) > 128:
            return False
        _set = [False] * 128
        for c in s:
            if _set[ord(c)]:
                return False
            _set[ord(c)] = True
        return True

s = Solution()
print("abd", s.hasUniqueChar("abd"))
print("aba", s.hasUniqueChar("aba"))
