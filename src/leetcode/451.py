from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        _map = Counter(s)
        _count = defaultdict(list)
        for k in _map:
            _count[_map[k]].append(k)
        result = ""
        for count in sorted(_count.keys(), reverse=True):
            result += ("".join([(count * x) for x in _count[count]]))
        return result

    def frequencySort_Looks_Good(self, s: str) -> str:
        cache = Counter(s)
        result = ""
        for k in sorted(cache, key=cache.get, reverse=True): # type: ignore
            result += k * cache[k]
        return result

s = Solution()
print(s.frequencySort("txxxree"))
