from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by, trusts = defaultdict(int), defaultdict(int)
        for t in trust:
            trusted_by[t[0]] += 1
            trusts[t[1]] += 1
        for i in range(1, n + 1):
            if trusts[i] == n - 1 and trusted_by[i] == 0:
                return i
        return -1


s = Solution()
print(s.findJudge(2, [[1, 2]]))
print(s.findJudge(3, [[1, 3], [2, 3]]))
print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
