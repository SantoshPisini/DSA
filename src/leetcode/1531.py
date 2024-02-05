from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def helper(i, k, prev, prev_count):
            if k < 0:
                return float("-inf")
            if i == len(s):
                return 0
            if s[i] == prev:
                result = (1 if prev_count in [
                          1, 9, 99] else 0) + helper(i + 1, k, prev, prev_count + 1)
            else:
                result = min(
                    helper(i + 1, k - 1, prev, prev_count),  # del s[i]
                    1 + helper(i + 1, k, s[i], 1)  # no del
                )
            return result
        return helper(0, k, "", 0)


class Solution_Partial:
    def getLengthOfOptimalCompression_Partial(self, s: str, k: int) -> int:
        _map = []
        i = 0
        compressed = ""
        while i < len(s):
            c = 1
            while i < len(s) - 1 and s[i] == s[i+1]:
                c += 1
                i += 1
            compressed += s[i]
            if c > 1:
                compressed += str(c)
            _map.append((s[i], c))
            i += 1
        result = len(compressed)
        while k:
            # Single
            for i, mapItem in enumerate(_map):
                _, v = mapItem
                if v == 1:
                    del _map[i]
                    break
            result -= 1
            k -= 1
        return result


s = Solution()
print(s.getLengthOfOptimalCompression("aaabcccd", 2))
print(s.getLengthOfOptimalCompression("aabbaa", 2))
print(s.getLengthOfOptimalCompression("aaaaaaaaaaa", 0))
# print(s.getLengthOfOptimalCompression("aaaaaaaaaabbbbbbbbbb", 2))
