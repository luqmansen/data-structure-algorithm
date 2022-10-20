class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m * n:
            return []
        
        res = []
        
        last = 0
        
        for _ in range(m):
            
            res.append(original[last:last+n])
            last +=n
            
        return res
        