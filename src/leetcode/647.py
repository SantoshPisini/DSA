class Solution:
    def is_palindrome(self, s: str) -> bool:
        return all(s[i] == s[~i] for i in range(len(s) // 2))

    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.is_palindrome(s[i:j]):
                    result += 1
        return result


s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))
