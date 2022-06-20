"""
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The
robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""
from pprint import pprint


class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        key = f"{m}|{n}"
        if key in memo:
            return memo[key]

        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        memo[key] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

        return memo[key]

    def uniquePathsFib(self, m: int, n: int) -> int:
        tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        tab[1][1] = 1

        for col in range(n + 1):
            for row in range(m + 1):
                if row + 1 <= m:
                    tab[col][row + 1] += tab[col][row]
                if col + 1 <= n:
                    tab[col + 1][row] += tab[col][row]

        return tab[n][m]

if __name__ == '__main__':
    s = Solution()
    r = s.uniquePathsFib(3, 7)
    print(r)
