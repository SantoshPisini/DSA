class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        _set = set(s)
        result = 0
        for _s in _set:
            left, right = s.index(_s), s.rindex(_s)
            _middle = set(s[left + 1: right])
            result += len(_middle)
        return result


    def countPalindromicSubsequence_TLE(self, s: str) -> int:
        def is_palindrome(s: str):
            return s == s[::-1]

        _set = set()
        for i in range(len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                for k in range(j + 1, len(s)):
                    _set.add(s[i]+s[j]+s[k])
        result = 0
        for item in _set:
            if is_palindrome(item):
                result += 1
        return result


s = Solution()
print(s.countPalindromicSubsequence("aabca"))
print(s.countPalindromicSubsequence("abc"))
print(s.countPalindromicSubsequence("bbcbaba"))
