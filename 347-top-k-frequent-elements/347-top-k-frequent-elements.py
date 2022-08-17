class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        
        res = [[] for i in range(len(nums)+1)] 
        
        for key, v in cnt.items():
            res[v].append(key)
        
        # O (n log n) solution, because we do sorting 
        # res = sorted(res, reverse=True, key=lambda x: x[1])
        # return [i[0] for i in res][:k]
        
        # O (n) solution
        kk = []
        for i in reversed(res):
            for n in i:
                kk.append(n)
                if len(kk) == k:
                    return kk
                