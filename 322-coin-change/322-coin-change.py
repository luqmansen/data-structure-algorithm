
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        result = []
        memo = {}
        
        for c in coins:
            amt = self.do(coins, memo, amount)
            if amt > 0 and amt != math.inf:
                result.append(amt)
            
        return min(result) if len(result) > 0 else -1
    
    
    def do(self, coins, memo, remainder):
        if remainder in memo:
            return memo[remainder]
        
        if remainder == 0:
            return 0
        if remainder < 0:
            return math.inf
        
        temp = math.inf
        
        for c in coins:
            temp = min(temp, self.do(coins,memo, remainder - c))
        
        memo[remainder] = 1 + temp
        
        return 1 + temp
            
            
        
        
 