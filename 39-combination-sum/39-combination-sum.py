class Solution:
    def combinationSum(self, candidates: List[int], target: int, memo=None) -> List[List[int]]:
        if memo is None:
            memo = {}
            
        if target in memo:
            return memo[target]
            
            
        if target == 0:
            return [[]]
        
        if target < 0:
            return []

        result = []
        for w in candidates:
            comb = self.combinationSum(candidates, target-w, memo)
            for i in comb:
                i = [w, *i]
                result.append(i)
                
        nodup = []
        temp = {}
        for i in result:
            i.sort()
            key = str(i)
            if key not in temp:
                temp[key] = None
                nodup.append(i)
        
        memo[target] = nodup
        return nodup

