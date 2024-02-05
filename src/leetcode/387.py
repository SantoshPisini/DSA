from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        _map = Counter(s)
        for i, v in enumerate(s):
            if _map[v] == 1:
                return i
        return -1

    def firstUniqChar_BF(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    continue
                if s[i] == s[j]:
                    j = -1
                    break
            if j + 1 == len(s):
                return i
        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
