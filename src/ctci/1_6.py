class Solution:
    def compression(self, s: str) -> str:
        result = []
        prev_index = i = 0
        result.append(s[0])
        for i in range(1, len(s)):
            if s[i] != s[prev_index]:
                result.append(str(i - prev_index))
                result.append(s[i])
                prev_index = i
        result.append(str(i - prev_index + 1))
        result = ''.join(result)
        return s if len(s) < len(result) else result


s = Solution()
print(s.compression("abcdef"))
print(s.compression("aabcccccaaa"))
print(s.compression("aabccccca"))
