class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            
            n -= 2**int(math.log(n, 2))
            cnt +=1
            # print(n, cnt)
        
        return cnt
            
            
    
    
        