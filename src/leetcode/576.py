class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        _goal = set()
        _possible = set(((0, -1), (0, 1), (-1, 0), (1, 0)))
        for i in range(m):
            _goal.add((i, -1))
            _goal.add((i, n))
        for i in range(n):
            _goal.add((-1, i))
            _goal.add((m, i))
        MOD = 10 ** 9 + 7

        def helper(i, j, moves):
            if moves < 1:
                return 0
            result = 0
            for possible in _possible:
                new_i, new_j = i + possible[0], j + possible[1]
                if (new_i, new_j) in _goal:
                    result += 1
                else:
                    result += (helper(new_i, new_j, moves - 1))
            return result % MOD
        return helper(startRow, startColumn, maxMove)


s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))
print(s.findPaths(1, 3, 3, 0, 1))
