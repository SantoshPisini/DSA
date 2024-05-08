class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        start_len = len(s) % k
        result = []
        if start_len:
            result.append(s[:start_len])
        for i in range(start_len, len(s), k):
            result.append(s[i:i + k])
        return '-'.join(result)


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
