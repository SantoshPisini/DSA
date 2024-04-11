from typing import List


class Solution_BF:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = []
        for digit in digits:
            if not result:
                result = [char for char in phone_map[digit]]
            else:
                temp = []
                for char in phone_map[digit]:
                    temp.extend([x+char for x in result])
                result = temp
        return result

# Backtracking solution


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone_map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = []

        def backtracking(idx, s):
            if idx > len(digits) - 1:
                result.append(s)
                return
            for char in phone_map[digits[idx]]:
                backtracking(idx + 1, s + char)
        backtracking(0, "")
        return result
