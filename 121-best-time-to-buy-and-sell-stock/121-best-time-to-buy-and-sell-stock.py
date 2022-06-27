class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIdx = 0
        sellIdx = 1
        profit = 0
        
        while sellIdx < len(prices):
            buy = prices[buyIdx]
            sell = prices[sellIdx]
            
            if buy < sell:
                profit = max(profit, sell - buy)
            else:
                buyIdx=sellIdx
            
            sellIdx+=1
        
        return profit
            
            
 
        
#     def maxProfit(self, prices: List[int]) -> int:
#         curmin = math.inf
#         curmax = -math.inf
        
#         for idx in range(len(prices)):
#             today = prices[idx]
#             # print(future, curmax, today, curmin)

#             if today < curmin:
#                 for idx2 in range(idx+1, len(prices)):
#                     future = prices[idx2]

#                     if future - today > curmax - curmin:
#                         curmin = today
#                         curmax = future
                    
#         if curmin != math.inf and curmax != -math.inf:
#             profit = curmax - curmin
#             return profit if profit >0 else 0
#         return 0
                        
                
        