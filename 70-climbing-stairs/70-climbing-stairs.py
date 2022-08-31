class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb({}, n, 0)
    
    def climb(self, seen, curr, res=0):
        
        if curr in seen:
            return seen[curr]

        if curr < 0:
            return 0

        if curr == 0:
            return 1

        for i in [1, 2]:
            res += self.climb(seen, curr - i)
        
        seen[curr] = res
        
        return res
