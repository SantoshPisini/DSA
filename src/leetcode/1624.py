class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        _map, result = {}, -1
        for i in range(len(s)):
            if s[i] in _map:
                result = max(result, i - _map[s[i]] - 1)
            else:
                _map[s[i]] = i
        return result

s = Solution()
print(s.maxLengthBetweenEqualCharacters("aa"))