class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
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
        