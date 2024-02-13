from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        return all(s[i] == s[~i] for i in range(len(s) // 2))

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""


s = Solution()
print(s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
