from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        _map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        low_len, hight_len = len(str(low)),  len(str(high))
        result = []
        for _len in range(low_len, hight_len + 1):
            for i in range(9 - _len + 1):
                val = int("".join(_map[i: i + _len]))
                if low <= val <= high:
                    result.append(val)
        return result


s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(100, 3000))
