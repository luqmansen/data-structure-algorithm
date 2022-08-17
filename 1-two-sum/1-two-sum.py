class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        [2,7,8,11,15] -> 9
         
        '''
        
        calc = {}
        
        for i, n in enumerate(nums):
            if n in calc:
                calc[n].append(i)
            else:
                calc[n] = [i]
            
        for k, v in calc.items():
            
            res = target - k
            
            if res in calc:
                if len(calc[res]) > 1:
                    return calc[res]
                
                if v[0] == calc[res][0]:
                    continue
                    
                return [v[0], calc[res][0]]
        
            
        
        
        