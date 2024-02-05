from typing import List


class Solution:
    def dailyTemperatures_BF(self, temperatures):
        result = [0]
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i + 1] > temperatures[i]:
                result.insert(0, 1)
            else:
                j, r = i + 1, 1
                while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                    r += 1
                    j += 1
                result.insert(0, 0 if j == len(temperatures) else r)
        return result
    
    def dailyTemperatures(self, temperatures):
        result = [0]
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i + 1] > temperatures[i]:
                result.insert(0, 1)
            else:
                j, r = i + 1, 1
                while j < len(temperatures) and temperatures[i] > temperatures[j]:
                    r += result[0]
                    j += (result[0] + 1)
                result.insert(0, 0 if j == len(temperatures) else r)
        return result


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
print(s.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
