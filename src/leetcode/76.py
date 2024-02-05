from collections import defaultdict, Counter


class Solution:
    # https://leetcode.com/problems/minimum-window-substring/solutions/26804/12-lines-python
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        _map, t_len = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            t_len -= _map[c] > 0
            _map[c] -= 1
            if not t_len:
                while i < j and _map[s[i]] < 0:
                    _map[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    def minWindow_TLE(self, s: str, t: str) -> str:
        _map = defaultdict(int)
        if len(s) < len(t):
            return ""
        for c in t:
            _map[c] += 1
        # print(_map)
        result = ""
        for i in range(len(s)):
            if s[i] not in _map:
                continue
            start = end = i
            temp_t = list(t)
            while start <= end and end < len(s):
                if s[end] not in temp_t:
                    end += 1
                    continue
                temp_t.remove(s[end])
                if len(temp_t) == 0 and (result == "" or len(result) > (end - start + 1)):
                    # print(s[start:end+1])
                    result = s[start:end+1]
                    break
                end += 1
        return result


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "b"))
