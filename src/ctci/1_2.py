class Solution():
    def isPermutation(self, x: str, y: str) -> bool:
        if len(x) != len(y):
            return False
        
        _letters = [0] * 128
        for c in x:
            _letters[ord(c)] += 1
        
        for c in y:
            if _letters[ord(c)] == 0:
                return False
            _letters[ord(c)] -= 1
        return True

s = Solution()
print("abd", "bda", s.isPermutation("abd", "bda"))
print("aba", "aab", s.isPermutation("aba", "aab"))
print("abc", "abd", s.isPermutation("abc", "abd"))
