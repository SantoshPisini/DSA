

class Solution():
    def palindromePermutation(self, s: str) -> bool:
        _set = set()
        for c in s:
            if c == ' ':
                continue
            if c in _set:
                _set.remove(c)
            else:
                _set.add(c)
        return len(_set) < 2


s = Solution()
print("test search", "->", s.palindromePermutation("test search"))
print("tact coa", "->", s.palindromePermutation("tact coa"))
