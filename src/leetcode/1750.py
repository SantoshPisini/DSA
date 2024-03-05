class Solution:
    def minimumLength(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start < end and s[start] == s[end]:
            temp = s[start]
            while start <= end and s[start] == temp:
                start += 1
            while end >= start and s[end] == temp:
                end -= 1
        return end - start + 1


s = Solution()
print(s.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbbb"))
