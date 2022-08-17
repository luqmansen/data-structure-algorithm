class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        
        maks= 0
        
        for n in nums:
            if n in cnt:
                cnt[n] +=1
            else:
                cnt[n] = 1
            
            maks = max(maks, cnt[n])
        
        res = [0] * (maks+1)

        for key, v in cnt.items():
            if res[v] == 0:
                res[v] = [key]
            else:
                res[v].append(key)
        
        # O (n log n) solution, because we do sorting 
        # res = sorted(res, reverse=True, key=lambda x: x[1])
        # return [i[0] for i in res][:k]
        
        kk = []
        for i in reversed(res):
            if i != 0:
                kk = [*kk, *i]
                
        return kk[:k] 