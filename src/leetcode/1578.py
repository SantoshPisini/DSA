from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, result = 0, 0
        while i < len(colors):
            now = i
            while i < len(colors) - 1 and colors[now] == colors[i + 1]:
                i += 1
            # print(colors[now], now, i)
            if now != i:
                # print(neededTime[now:i + 1])
                result += (sum(neededTime[now:i + 1]) -
                           max(neededTime[now:i + 1]))
            i += 1
        return result


s = Solution()
print(s.minCost("abaac", [1, 2, 3, 4, 5]))
print(s.minCost("abc", [1, 2, 3]))
print(s.minCost("aabaa", [1, 2, 3, 4, 1]))
print(s.minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))
