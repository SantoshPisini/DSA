from typing import Counter, List


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        _counter = Counter(arr)
        _counts = sorted(_counter.items(), key=lambda x: x[1])

        for key, val in _counts:
            if k >= val:
                k -= val
                del _counter[key]
            else:
                break

        return len(_counter)

    def findLeastNumOfUniqueInts_VerrrrySloww(self, arr: List[int], k: int) -> int:
        _counter = {}
        for a in arr:
            if a in _counter:
                _counter[a] += 1
            else:
                _counter[a] = 1
        _map = []
        for c in _counter.keys():
            if _counter[c] == 1 and k > 0:
                k -= 1
            else:
                _map.append((c, _counter[c]))
        del _counter
        _map.sort(key=lambda x: x[1])
        while k > 0:
            k -= _map[0][1]
            if k > -1:
                _map = _map[1:]
        return len(_map)


s = Solution()
print(s.findLeastNumOfUniqueInts([2, 1, 1, 2, 3, 3], 3))
print(s.findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3))
print(s.findLeastNumOfUniqueInts([5, 5, 4], 1))
print(s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
