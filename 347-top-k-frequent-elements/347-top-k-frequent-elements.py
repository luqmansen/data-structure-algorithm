class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        
        for n in nums:
            if n in cnt:
                cnt[n] +=1
            else:
                cnt[n] = 1
        
        res = []
        
        for key, v in cnt.items():
            res.append((key,v))
        
        # print(cnt)
        # print(res)
        res = sorted(res, reverse=True, key=lambda x: x[1])
        # print(res)
        
            
        return [i[0] for i in res][:k]
            
            
        
        