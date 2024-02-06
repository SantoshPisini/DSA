from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = defaultdict(list)
        for s in strs:
            _map["".join(sorted(s))].append(s)
        return list(_map.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
