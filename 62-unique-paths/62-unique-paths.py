class Solution:
    def uniquePathsRecursion(self, m: int, n: int, memo={}) -> int:
        """
        recursion solution
        """
        key1 = f"{m}|{n}"
        if key1 in memo:
            return memo[key1]
        key2 = f"{n}|{m}"
        if key2 in memo:
            return memo[key2]
        
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        
        res = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1) 
        memo[key1] = res
        memo[key2] = res
        
        return res
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        """
        tabulation solution
        """
        tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        tab[1][1] = 1

        for col in range(n + 1):
            for row in range(m + 1):
                if row + 1 <= m:
                    tab[col][row + 1] += tab[col][row]
                if col + 1 <= n:
                    tab[col + 1][row] += tab[col][row]

        return tab[n][m]


        return tab[m][n]
        